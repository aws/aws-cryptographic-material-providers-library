// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../Model/AwsCryptographyKeyStoreTypes.dfy"
include "AwsCryptographyKeyStoreOperations.dfy"

include "ErrorMessages.dfy"
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

  // There is no sensible default, so define something that passes verification but will fail at runtime
  function method DefaultKeyStoreConfig(): KeyStoreConfig
  {
    KeyStoreConfig(
      ddbTableName := "None",
      kmsConfiguration := KMSConfiguration.kmsKeyArn("arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"),
      logicalKeyStoreName := "None",
      id := None,
      grantTokens := None,
      kmsClient := None,
      ddbClient := None,
      requireConsistentReads := Some(false)
    )
  }

  method KeyStore(config: KeyStoreConfig)
    returns (res: Result<KeyStoreClient, Error>)
    ensures res.Success? ==>
              && res.value is KeyStoreClient
              && var rconfig := (res.value as KeyStoreClient).config;
              //= aws-encryption-sdk-specification/framework/branch-key-store.md#aws-kms-configuration
              //= type=implication
              //# This ARN MUST be a valid
              //# [AWS KMS Key ARN](./aws-kms/aws-kms-key-arn.md#a-valid-aws-kms-arn).
              && (rconfig.kmsConfiguration.kmsKeyArn? ==> KmsArn.ValidKmsArn?(rconfig.kmsConfiguration.kmsKeyArn))
              && (rconfig.kmsConfiguration.kmsMRKeyArn? ==> KmsArn.ValidKmsArn?(rconfig.kmsConfiguration.kmsMRKeyArn))
              && DDB.IsValid_TableName(config.ddbTableName)
              && GetValidGrantTokens(config.grantTokens).Success?
              && (config.kmsClient.Some? ==> rconfig.kmsClient == config.kmsClient.value)
              && (config.ddbClient.Some? ==> rconfig.ddbClient == config.ddbClient.value
                                             && rconfig.kmsClient.ValidState()
                                             && rconfig.ddbClient.ValidState())
    ensures
      && !DDB.IsValid_TableName(config.ddbTableName)
      && !KMS.IsValid_KeyIdType(config.kmsConfiguration.kmsKeyArn)
      ==>
        res.Failure?
  {
    var kmsClient: KMS.IKMSClient;
    var ddbClient: DDB.IDynamoDBClient;
    var inferredRegion: Option<string> := None;

    if KMSKeystoreOperations.HasKeyId(config.kmsConfiguration) {
      var parsedArn :- KmsArn.IsValidKeyArn(KMSKeystoreOperations.GetKeyId(config.kmsConfiguration));
      // If KMS Configuration is a KMS Key ARN,
      // try to get KMS && DDB Clients for that Key's Region
      inferredRegion := Some(parsedArn.region);

      //= aws-encryption-sdk-specification/framework/branch-key-store.md#dynamodb-client
      //# If the AWS KMS Configuration is MRDiscovery,
      //# and no DynamoDb Client is provided,
      //# a new DynamoDb Client MUST be created
      //# with the region configured in the MRDiscovery.

      //= aws-encryption-sdk-specification/framework/branch-key-store.md#kms-client
      //# If the AWS KMS Configuration is MRDiscovery,
      //# and no KMS Client is provided,
      //# a new KMS Client MUST be created
      //# with the region configured in the MRDiscovery.
    } else if config.kmsConfiguration.mrDiscovery? {
      inferredRegion := Some(config.kmsConfiguration.mrDiscovery.region);
    }

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#initialization
    //# The following inputs MAY be specified to create a KeyStore:
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

    if config.kmsClient.Some? {
      kmsClient := config.kmsClient.value;
    } else if config.kmsClient.None? && inferredRegion.Some? {
      //= aws-encryption-sdk-specification/framework/branch-key-store.md#kms-client
      //# If the AWS KMS Configuration is KMS Key ARN or KMS MRKey ARN,
      //# and no KMS Client is provided,
      //# a new KMS Client MUST be created
      //# with the region of the supplied KMS ARN.

      //= aws-encryption-sdk-specification/framework/branch-key-store.md#kms-client
      //# If the AWS KMS Configuration is MRDiscovery,
      //# and no KMS Client is provided,
      //# a new KMS Client MUST be created
      //# with the region configured in the MRDiscovery.
      var maybeKmsClient := KMSOperations.KMSClientForRegion(inferredRegion.value);
      kmsClient :- maybeKmsClient
      .MapFailure(e => Types.ComAmazonawsKms(ComAmazonawsKms := e));
    } else {
      //= aws-encryption-sdk-specification/framework/branch-key-store.md#kms-client
      //# If the AWS KMS Configuration is Discovery,
      //# and no KMS Client is provided,
      //# a new KMS Client MUST be created
      //# with the default configuration.
      var maybeKmsClient := KMSOperations.KMSClient();
      kmsClient :- maybeKmsClient
      .MapFailure(e => Types.ComAmazonawsKms(ComAmazonawsKms := e));
    }

    if config.ddbClient.Some? {
      ddbClient := config.ddbClient.value;
    } else if config.ddbClient.None? && inferredRegion.Some? {
      //= aws-encryption-sdk-specification/framework/branch-key-store.md#dynamodb-client
      //# If the AWS KMS Configuration is KMS Key ARN or KMS MRKey ARN,
      //# and no DynamoDb Client is provided,
      //# a new DynamoDb Client MUST be created
      //# with the region of the supplied KMS ARN.

      //= aws-encryption-sdk-specification/framework/branch-key-store.md#dynamodb-client
      //# If the AWS KMS Configuration is MRDiscovery,
      //# and no DynamoDb Client is provided,
      //# a new DynamoDb Client MUST be created
      //# with the region configured in the MRDiscovery.
      var maybeDdbClient := DDBOperations.DDBClientForRegion(inferredRegion.value);
      ddbClient :- maybeDdbClient
      .MapFailure(e => Types.ComAmazonawsDynamodb(ComAmazonawsDynamodb := e));
    } else {
      //= aws-encryption-sdk-specification/framework/branch-key-store.md#dynamodb-client
      //# If the AWS KMS Configuration is Discovery,
      //# and no DynamoDb Client is provided,
      //# a new DynamoDb Client MUST be created
      //# with the default configuration.
      var maybeDdbClient := DDBOperations.DynamoDBClient();
      ddbClient :- maybeDdbClient
      .MapFailure(e => Types.ComAmazonawsDynamodb(ComAmazonawsDynamodb := e));
    }

    // This is true but to prove it requires changes to smithy-dafny.
    assume {:axiom} ddbClient.Modifies !! kmsClient.Modifies;

      //= aws-encryption-sdk-specification/framework/branch-key-store.md#initialization
      //# The following inputs MUST be specified to create a KeyStore:
    :- Need(
      DDB.IsValid_TableName(config.ddbTableName),
      Types.KeyStoreException(
        message := "Invalid Amazon DynamoDB Table Name")
    );

    var client := new KeyStoreClient(
      Operations.Config(
      id := keyStoreId,
      ddbTableName := config.ddbTableName,
      logicalKeyStoreName := config.logicalKeyStoreName,
      kmsConfiguration := config.kmsConfiguration,
      grantTokens := grantTokens.value,
      kmsClient := kmsClient,
      ddbClient := ddbClient,
      requireConsistentReads := config.requireConsistentReads.UnwrapOr(false)
      )
    );
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
