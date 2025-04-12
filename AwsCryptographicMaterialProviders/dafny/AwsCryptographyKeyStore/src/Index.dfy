// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../Model/AwsCryptographyKeyStoreTypes.dfy"
include "AwsCryptographyKeyStoreOperations.dfy"
include "DefaultKeyStorageInterface.dfy"
include "KeyStoreErrorMessages.dfy"
include "KmsArn.dfy"

module {:extern "software.amazon.cryptography.keystore.internaldafny"} KeyStore refines AbstractAwsCryptographyKeyStoreService
{
  import opened AwsKmsUtils
  import Operations = AwsCryptographyKeyStoreOperations
  import KMSOperations = Com.Amazonaws.Kms
  import DDBOperations =  Com.Amazonaws.Dynamodb
  import KMS = ComAmazonawsKmsTypes
  import DDB = ComAmazonawsDynamodbTypes
  import UUID
  import ErrorMessages = KeyStoreErrorMessages
  import KmsArn
  import KMSKeystoreOperations
  import DefaultKeyStorageInterface

  // At this time the user agent is not configurable in Dafny.
  // It is neither configurable on creation nor on request.
  //= aws-encryption-sdk-specification/framework/branch-key-store.md#initialization
  //= type=exception
  //# On initialization the KeyStore SHOULD
  //# append a user agent string to the AWS KMS SDK Client with
  //# the value `aws-kms-hierarchy`.

  // There is no sensible default, so define something that passes verification but will fail at runtime
  function method DefaultKeyStoreConfig(): KeyStoreConfig
  {
    KeyStoreConfig(
      kmsConfiguration := KMSConfiguration.kmsKeyArn("arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"),
      logicalKeyStoreName := "None"
    )
  }

  method {:vcs_split_on_every_assert} KeyStore(config: KeyStoreConfig)
    returns (res: Result<KeyStoreClient, Error>)
    //= aws-encryption-sdk-specification/framework/branch-key-store.md#initialization
    //= type=implication
    //# If neither [Storage](#storage) nor [Table Name](#table-name) is configured initialization MUST fail.
    ensures config.storage.None? && config.ddbTableName.None? ==> res.Failure?
    //= aws-encryption-sdk-specification/framework/branch-key-store.md#initialization
    //= type=implication
    //# If both [Storage](#storage) and [Table Name](#table-name) are configured initialization MUST fail.
    ensures config.storage.Some? && config.ddbTableName.Some? ==> res.Failure?
    //= aws-encryption-sdk-specification/framework/branch-key-store.md#initialization
    //= type=implication
    //# If both [Storage](#storage) and [DynamoDb Client](#dynamodb-client) are configured initialization MUST fail.
    ensures config.storage.Some? && config.ddbClient.Some? ==> res.Failure?
    //= aws-encryption-sdk-specification/framework/branch-key-store.md#initialization
    //= type=implication
    //# If both [KeyManagement](#keymanagement) and [KMS Client](#kms-client) are configured initialization MUST fail.
    ensures config.keyManagement.Some? && config.kmsClient.Some? ==> res.Failure?
    //= aws-encryption-sdk-specification/framework/branch-key-store.md#initialization
    //= type=implication
    //# If both [KeyManagement](#keymanagement) and [Grant Tokens](#aws-kms-grant-tokens) are configured initialization MUST fail.
    ensures config.keyManagement.Some? && config.grantTokens.Some? ==> res.Failure?

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#aws-kms-configuration
    //= type=implication
    //# This ARN MUST NOT be an Alias.
    ensures
      && KMSKeystoreOperations.HasKeyId(config.kmsConfiguration)
      && AwsArnParsing.ParseAwsKmsArn(KMSKeystoreOperations.GetKeyId(config.kmsConfiguration)).Success?
      && AwsArnParsing.ParseAwsKmsArn(KMSKeystoreOperations.GetKeyId(config.kmsConfiguration)).value.resource.resourceType == "alias"
      ==> res.Failure?

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#initialization
    //= type=implication
    //# If [Storage](#storage) is configured with [KeyStorage](#keystorage)
    //# then this MUST be the configured [KeyStorage interface](./key-store/key-storage.md#interface).
    ensures
      && res.Success?
      && config.storage.Some?
      && config.storage.value.custom? ==>
        && res.value.config.storage == config.storage.value.custom

    ensures
      && res.Success?
      && !(config.storage.Some? && config.storage.value.custom?) ==>
        //= aws-encryption-sdk-specification/framework/branch-key-store.md#initialization
        //= type=implication
        //# If [Storage](#storage) is not configured with [KeyStorage](#keystorage)
        //# a [default key storage](./key-store/default-key-storage.md#initialization) MUST be created.
        && fresh(res.value.config.storage)
        && res.value.config.storage is DefaultKeyStorageInterface.DynamoDBKeyStorageInterface
        && var storage: DefaultKeyStorageInterface.DynamoDBKeyStorageInterface := res.value.config.storage;

        //= aws-encryption-sdk-specification/framework/branch-key-store.md#initialization
        //= type=implication
        //# This constructed [default key storage](./key-store/default-key-storage.md#overview)
        //# MUST be configured with the provided [logical keystore name](#logical-keystore-name).
        && storage.logicalKeyStoreName == config.logicalKeyStoreName

        //= aws-encryption-sdk-specification/framework/branch-key-store.md#initialization
        //= type=implication
        //# This constructed [default key storage](./key-store/default-key-storage.md#initialization)
        //# MUST be configured with either the [Table Name](#table-name) or the [DynamoDBTable](#dynamodbtable) table name
        //# depending on which one is configured.
        && (config.ddbTableName.Some? ==> storage.ddbTableName == config.ddbTableName.value)
        && (config.storage.Some? ==> storage.ddbTableName == config.storage.value.ddb.ddbTableName)

        //= aws-encryption-sdk-specification/framework/branch-key-store.md#initialization
        //= type=implication
        //# This constructed [default key storage](./key-store/default-key-storage.md#initialization)
        //# MUST be configured with either the [DynamoDb Client](#dynamodb-client), the DDB client in the [DynamoDBTable](#dynamodbtable)
        //# or a constructed DDB client depending on what is configured.
        && ((config.ddbTableName.Some? && config.ddbClient.Some?) ==> storage.ddbClient == config.ddbClient.value)
        && ((config.storage.Some? && config.storage.value.ddb.ddbClient.Some?) ==> storage.ddbClient == config.storage.value.ddb.ddbClient.value)
        && ((
              || (config.ddbTableName.Some? && config.ddbClient.None?)
              || (config.storage.Some? && config.storage.value.ddb.ddbClient.None?)
            ) ==> fresh(storage.ddbClient))

    ensures
      && res.Success?
      && !(config.storage.Some? && config.storage.value.custom?)
      && (
           || (config.ddbTableName.Some? && config.ddbClient.None?)
           || (config.storage.Some? && config.storage.value.ddb.ddbClient.None?)
         )

      //= aws-encryption-sdk-specification/framework/branch-key-store.md#initialization
      //= type=implication
      //# If a DDB client needs to be constructed and the AWS KMS Configuration is KMS Key ARN or KMS MRKey ARN,
      //# a new DynamoDb client MUST be created with the region of the supplied KMS ARN.
      && (config.kmsConfiguration.kmsKeyArn? || config.kmsConfiguration.kmsMRKeyArn?)
      ==>
        && KmsArn.IsValidKeyArn(KMSKeystoreOperations.GetKeyId(config.kmsConfiguration)).Success?
        && var arn := KmsArn.IsValidKeyArn(KMSKeystoreOperations.GetKeyId(config.kmsConfiguration)).value;
        && res.value.config.ddbConstructedRegion == Some(arn.region)

    ensures
      && res.Success?
      && !(config.storage.Some? && config.storage.value.custom?)
      && (
           || (config.ddbTableName.Some? && config.ddbClient.None?)
           || (config.storage.Some? && config.storage.value.ddb.ddbClient.None?)
         )

      //= aws-encryption-sdk-specification/framework/branch-key-store.md#initialization
      //= type=implication
      //# If a DDB client needs to be constructed and the AWS KMS Configuration is Discovery,
      //# a new DynamoDb client MUST be created with the default configuration.
      && (config.kmsConfiguration.discovery?)
      ==>
        && res.value.config.ddbConstructedRegion == None

    ensures
      && res.Success?
      && !(config.storage.Some? && config.storage.value.custom?)
      && (
           || (config.ddbTableName.Some? && config.ddbClient.None?)
           || (config.storage.Some? && config.storage.value.ddb.ddbClient.None?)
         )

      //= aws-encryption-sdk-specification/framework/branch-key-store.md#initialization
      //= type=implication
      //# If a DDB client needs to be constructed and the AWS KMS Configuration is MRDiscovery,
      //# a new DynamoDb client MUST be created with the region configured in the MRDiscovery.
      && (config.kmsConfiguration.mrDiscovery?)
      ==>
        && res.value.config.ddbConstructedRegion == Some(config.kmsConfiguration.mrDiscovery.region)

    ensures
      && res.Success?

      //= aws-encryption-sdk-specification/framework/branch-key-store.md#initialization
      //= type=implication
      //# If no AWS KMS client is provided one MUST be constructed.
      && !(
           && config.keyManagement.Some?
           && config.keyManagement.value.kms?
           && config.keyManagement.value.kms.kmsClient.Some?
         )
      && !(config.kmsClient.Some?)
      ==>
        && fresh(res.value.config.kmsClient)

    ensures
      && res.Success?
      && !(
           && config.keyManagement.Some?
           && config.keyManagement.value.kms?
           && config.keyManagement.value.kms.kmsClient.Some?
         )
      && !(config.kmsClient.Some?)

      //= aws-encryption-sdk-specification/framework/branch-key-store.md#initialization
      //= type=implication
      //# If AWS KMS client needs to be constructed and the AWS KMS Configuration is KMS Key ARN or KMS MRKey ARN,
      //# a new AWS KMS client MUST be created with the region of the supplied KMS ARN.
      && (config.kmsConfiguration.kmsKeyArn? || config.kmsConfiguration.kmsMRKeyArn?)
      ==>
        && KmsArn.IsValidKeyArn(KMSKeystoreOperations.GetKeyId(config.kmsConfiguration)).Success?
        && var arn := KmsArn.IsValidKeyArn(KMSKeystoreOperations.GetKeyId(config.kmsConfiguration)).value;
        && res.value.config.kmsConstructedRegion == Some(arn.region)

    ensures
      && res.Success?
      && !(
           && config.keyManagement.Some?
           && config.keyManagement.value.kms?
           && config.keyManagement.value.kms.kmsClient.Some?
         )
      && !(config.kmsClient.Some?)

      //= aws-encryption-sdk-specification/framework/branch-key-store.md#initialization
      //= type=implication
      //# If AWS KMS client needs to be constructed and the AWS KMS Configuration is Discovery,
      //# a new AWS KMS client MUST be created with the default configuration.
      && (config.kmsConfiguration.discovery?)
      ==>
        && res.value.config.kmsConstructedRegion == None

    ensures
      && res.Success?
      && !(
           && config.keyManagement.Some?
           && config.keyManagement.value.kms?
           && config.keyManagement.value.kms.kmsClient.Some?
         )
      && !(config.kmsClient.Some?)

      //= aws-encryption-sdk-specification/framework/branch-key-store.md#initialization
      //= type=implication
      //# If AWS KMS client needs to be constructed and the AWS KMS Configuration is MRDiscovery,
      //# a new AWS KMS client MUST be created with the region configured in the MRDiscovery.
      && (config.kmsConfiguration.mrDiscovery?)
      ==>
        && res.value.config.kmsConstructedRegion == Some(config.kmsConfiguration.mrDiscovery.region)

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#aws-kms-configuration
    //= type=implication
    //# This ARN MUST be a valid
    //# [AWS KMS Key ARN](./aws-kms/aws-kms-key-arn.md#a-valid-aws-kms-arn).
    ensures
      && KMSKeystoreOperations.HasKeyId(config.kmsConfiguration)
      && res.Success?
      ==> AwsArnParsing.ParseAwsKmsArn(KMSKeystoreOperations.GetKeyId(config.kmsConfiguration)).Success?

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#aws-kms-configuration
    //= type=implication
    //# To be clear, an KMS ARN for a Multi-Region Key MAY be provided to the `KMS Key ARN` configuration,
    //# and a KMS ARN for non Multi-Region Key MAY be provided to the `KMS MRKey ARN` configuration.
    ensures
      && (config.kmsConfiguration.kmsKeyArn? || config.kmsConfiguration.kmsMRKeyArn?)
      && res.Success?
      ==>
        var arn := AwsArnParsing.ParseAwsKmsArn(KMSKeystoreOperations.GetKeyId(config.kmsConfiguration)).value;
        || !AwsArnParsing.IsMultiRegionAwsKmsArn(arn)
        || AwsArnParsing.IsMultiRegionAwsKmsArn(arn)

  {

    :- Need(
      && !(config.keyManagement.Some? && config.kmsClient.Some?)
      && !(config.keyManagement.Some? && config.grantTokens.Some?)
    , Types.KeyStoreException(
        message := "Both keyManagement and kmsClient/grantTokens configuration is not supported.")
    );

    :- Need(
      config.storage.Some? || config.ddbTableName.Some?
    , Types.KeyStoreException(
        message := "A storage or ddbTableName configured is required.")
    );

    :- Need(
      && !(config.storage.Some? && config.ddbTableName.Some?)
      && !(config.storage.Some? && config.ddbClient.Some?)
    , Types.KeyStoreException(
        message := "Both storage and ddbTableName/ddbClient configuration is not supported.")
    );

    // These values are not assigned on purpose.
    // Since Dafny will prove definite assignment when these values
    // are used the MUST have values.
    // This helps bind their assignment to the correctness
    // that they are used when referencing them in the specification.
    // By looking at the value
    var inferredRegion: Option<string>;
    var kmsConstructedRegion: Option<string>;
    var ddbConstructedRegion: Option<string>;

    if KMSKeystoreOperations.HasKeyId(config.kmsConfiguration) {
      var parsedArn :- KmsArn.IsValidKeyArn(KMSKeystoreOperations.GetKeyId(config.kmsConfiguration));
      // If KMS Configuration is a KMS Key ARN,
      // try to get KMS && DDB Clients for that Key's Region
      inferredRegion := Some(parsedArn.region);
    } else if config.kmsConfiguration.mrDiscovery? {
      inferredRegion := Some(config.kmsConfiguration.mrDiscovery.region);
    } else {
      inferredRegion := None;
    }

    var grantTokens := GetValidGrantTokens(config.grantTokens);
    :- Need(
      && grantTokens.Success?,
      Types.KeyStoreException(
        message := "Grant Tokens passed to Key Store configuration are invalid.")
    );

    var keyStoreId;

    if config.id.Some? {
      keyStoreId := config.id.value;
    } else {
      //= aws-encryption-sdk-specification/framework/branch-key-store.md#keystore-id
      //# If one is not supplied, then a [version 4 UUID](https://www.ietf.org/rfc/rfc4122.txt) MUST be used.
      var maybeUuid := UUID.GenerateUUID();
      var uuid :- maybeUuid
      .MapFailure(e => Types.KeyStoreException(message := e));
      keyStoreId := uuid;
    }

    var kmsClient: KMS.IKMSClient;
    if
      && config.keyManagement.Some?
      && config.keyManagement.value.kms?
      && config.keyManagement.value.kms.kmsClient.Some?
    {
      kmsClient := config.keyManagement.value.kms.kmsClient.value;
      kmsConstructedRegion := None;
    } else if
      && config.kmsClient.Some?
    {
      kmsClient := config.kmsClient.value;
      kmsConstructedRegion := None;
    } else {
      if inferredRegion.Some?
      {
        var maybeKmsClient := KMSOperations.KMSClientForRegion(inferredRegion.value);
        kmsClient :- maybeKmsClient
        .MapFailure(e => Types.ComAmazonawsKms(ComAmazonawsKms := e));
        kmsConstructedRegion := inferredRegion;
      } else {
        var maybeKmsClient := KMSOperations.KMSClient();
        kmsClient :- maybeKmsClient
        .MapFailure(e => Types.ComAmazonawsKms(ComAmazonawsKms := e));
        kmsConstructedRegion := None;
      }
    }
    // This just asserts that kmsClient is assigned
    // Any assignment after this a mistake
    assert allocated(kmsClient);

    var logicalKeyStoreNameUtf8 :- UTF8.Encode(config.logicalKeyStoreName)
    .MapFailure(e => Types.KeyStoreException(message := "logicalKeyStoreName can not be encoded to UTF8" + e));

    var storage: Types.IKeyStorageInterface;
    if
      && config.storage.Some?
      && config.storage.value.custom?
    {
      storage := config.storage.value.custom;
      ddbConstructedRegion := None;
    } else if
      && config.storage.Some?
      && config.storage.value.ddb.ddbClient.Some?
    {
      assert config.storage.value.ddb?;

      var ddbTableNameUtf8 :- UTF8.Encode(config.storage.value.ddb.ddbTableName)
      .MapFailure(e => Types.KeyStoreException(message := "ddbTableName can not be encoded to UTF8" + e));

      storage := new DefaultKeyStorageInterface.DynamoDBKeyStorageInterface(
        ddbTableName := config.storage.value.ddb.ddbTableName,
        ddbClient := config.storage.value.ddb.ddbClient.value,
        logicalKeyStoreName := config.logicalKeyStoreName,
        ddbTableNameUtf8 := ddbTableNameUtf8,
        logicalKeyStoreNameUtf8 := logicalKeyStoreNameUtf8
      );
      ddbConstructedRegion := None;
    } else if
      && config.ddbTableName.Some?
      && config.ddbClient.Some?
    {
      assert config.storage.None?;

      var ddbTableNameUtf8 :- UTF8.Encode(config.ddbTableName.value)
      .MapFailure(e => Types.KeyStoreException(message := "ddbTableName can not be encoded to UTF8" + e));

      storage := new DefaultKeyStorageInterface.DynamoDBKeyStorageInterface(
        ddbTableName := config.ddbTableName.value,
        ddbClient := config.ddbClient.value,
        logicalKeyStoreName := config.logicalKeyStoreName,
        ddbTableNameUtf8 := ddbTableNameUtf8,
        logicalKeyStoreNameUtf8 := logicalKeyStoreNameUtf8
      );
      ddbConstructedRegion := None;
    } else {

      var ddbTableName := if config.storage.Some? then
        config.storage.value.ddb.ddbTableName
      else
        config.ddbTableName.value;

      var ddbTableNameUtf8 :- UTF8.Encode(ddbTableName)
      .MapFailure(e => Types.KeyStoreException(message := "ddbTableName can not be encoded to UTF8" + e));

      var ddbClient;

      if inferredRegion.Some? {

        var maybeDdbClient := DDBOperations.DDBClientForRegion(inferredRegion.value);
        ddbClient :- maybeDdbClient
        .MapFailure(e => Types.ComAmazonawsDynamodb(ComAmazonawsDynamodb := e));
        ddbConstructedRegion := inferredRegion;
      } else {
        var maybeDdbClient := DDBOperations.DynamoDBClient();
        ddbClient :- maybeDdbClient
        .MapFailure(e => Types.ComAmazonawsDynamodb(ComAmazonawsDynamodb := e));
        ddbConstructedRegion := None;

      }
      storage := new DefaultKeyStorageInterface.DynamoDBKeyStorageInterface(
        ddbTableName := ddbTableName,
        ddbClient := ddbClient,
        logicalKeyStoreName := config.logicalKeyStoreName,
        ddbTableNameUtf8 := ddbTableNameUtf8,
        logicalKeyStoreNameUtf8 := logicalKeyStoreNameUtf8
      );
    }
    // This just asserts that storage is assigned
    // Any assignment after this a mistake
    assert allocated(storage);

    var internalConfig := Operations.Config(
      id := keyStoreId,
      ddbTableName := config.ddbTableName,
      logicalKeyStoreName := config.logicalKeyStoreName,
      kmsConfiguration := config.kmsConfiguration,
      grantTokens := grantTokens.value,
      kmsClient := kmsClient,
      ddbClient := if config.ddbTableName.Some?
      then
        Some((storage as DefaultKeyStorageInterface.DynamoDBKeyStorageInterface).ddbClient)
      else None,
      storage := storage,
      kmsConstructedRegion := kmsConstructedRegion,
      ddbConstructedRegion := ddbConstructedRegion
    );

    // This is true but to prove it requires changes to smithy-dafny.
    assume {:axiom} internalConfig.storage.Modifies !! internalConfig.kmsClient.Modifies;
    assume {:axiom} (internalConfig.ddbClient.Some? ==> internalConfig.ddbClient.value.Modifies !! internalConfig.kmsClient.Modifies);

      // Dafny points out that this is possible
      // Right now, this would require getting a storage instance from one key store
      // and using that to construct a new key store.
    :- Need(
      (internalConfig.storage is DefaultKeyStorageInterface.DynamoDBKeyStorageInterface
       ==>
         internalConfig.logicalKeyStoreName == (internalConfig.storage as DefaultKeyStorageInterface.DynamoDBKeyStorageInterface).logicalKeyStoreName)
    , Types.KeyStoreException(
        message := "Storage DynamoDBKeyStorageInterface logical key store name does not key store's configured logical key store name")
    );

    assert Operations.ValidInternalConfig?(internalConfig);
    var client := new KeyStoreClient(internalConfig);

    assume {:axiom} fresh(client.Modifies
                          - ( if config.ddbClient.Some? then config.ddbClient.value.Modifies else {})
                          - ( if config.kmsClient.Some? then config.kmsClient.value.Modifies else {})
                          - ( if (config.storage.Some? && config.storage.value.custom?) then config.storage.value.custom.Modifies else {})
                          - ( if (config.keyManagement.Some? && config.keyManagement.value.kms? && config.keyManagement.value.kms.kmsClient.Some?) then config.keyManagement.value.kms.kmsClient.value.Modifies else {})
                          - ( if (config.storage.Some? && config.storage.value.ddb? && config.storage.value.ddb.ddbClient.Some?) then config.storage.value.ddb.ddbClient.value.Modifies else {}));

    return Success(client);
  }

  class KeyStoreClient... {

    predicate {:vcs_split_on_every_assert} {:rlimit 3000} ValidState() {
      && Operations.ValidInternalConfig?(config)
      && History !in Operations.ModifiesInternalConfig(config)
      && Modifies == Operations.ModifiesInternalConfig(config) + {History}
    }

    constructor(config: Operations.InternalConfig)
    {
      this.config := config;
      History := new IKeyStoreClientCallHistory();
      Modifies := Operations.ModifiesInternalConfig(config) + {History};
    }
  }
}
