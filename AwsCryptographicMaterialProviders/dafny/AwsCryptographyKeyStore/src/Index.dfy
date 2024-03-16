// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../Model/AwsCryptographyKeyStoreTypes.dfy"
include "AwsCryptographyKeyStoreOperations.dfy"
include "../../../dafny/AwsCryptographicMaterialProviders/src/AwsArnParsing.dfy"
include "../../AwsCryptographicMaterialProviders/src/Keyrings/AwsKms/AwsKmsUtils.dfy"
include "ErrorMessages.dfy"

module {:extern "software.amazon.cryptography.keystore.internaldafny"}
  KeyStore refines AbstractAwsCryptographyKeyStoreService
{
  import AAP = AwsArnParsing
  import opened AwsKmsUtils
  import Operations = AwsCryptographyKeyStoreOperations
  import KMSOperations = Com.Amazonaws.Kms
  import DDBOperations =  Com.Amazonaws.Dynamodb
  import KMS = ComAmazonawsKmsTypes
  import DDB = ComAmazonawsDynamodbTypes
  import UUID
  import ErrorMessages

  // There is no sensible default, so define something that passes verification but will fail at runtime
  function method DefaultKeyStoreConfig(): KeyStoreConfig
  {
    KeyStoreConfig(
      ddbTableName := "None",
      kmsConfiguration := KMSConfiguration.kmsKeyArn("a"),
      logicalKeyStoreName := "None",
      id := None,
      grantTokens := None,
      kmsClient := None,
      ddbClient := None
    )
  }

  method KeyStore(config: KeyStoreConfig)
    returns (res: Result<IKeyStoreClient, Error>)
    ensures res.Success? ==>
              && res.value is KeyStoreClient
              && var rconfig := (res.value as KeyStoreClient).config;
              && (rconfig.kmsConfiguration.kmsKeyArn? ==> Operations.ValidKmsArn?(rconfig.kmsConfiguration.kmsKeyArn))
              && DDB.IsValid_TableName(config.ddbTableName)
              && GetValidGrantTokens(config.grantTokens).Success?
              && (config.kmsClient.Some? ==> rconfig.kmsClient == config.kmsClient.value)
              && (config.ddbClient.Some? ==> rconfig.ddbClient == config.ddbClient.value
                                             && rconfig.kmsClient.ValidState()
                                             && rconfig.ddbClient.ValidState())
    ensures
      && !DDB.IsValid_TableName(config.ddbTableName)
      && !KMS.IsValid_KeyIdType(config.kmsConfiguration.kmsKeyArn)
      && AAP.ParseAwsKmsArn(config.kmsConfiguration.kmsKeyArn).Failure?
      ==>
        res.Failure?
  {
    var kmsClient: KMS.IKMSClient;
    var ddbClient: DDB.IDynamoDBClient;
    var inferredRegion: Option<string> := None;

    if config.kmsConfiguration.kmsKeyArn? {
      // var maybeParsedArn: Result<AAP.AwsKmsArn, string> :=
      //   AAP.ParseAwsKmsArn(config.kmsConfiguration.kmsKeyArn);
      // if maybeParsedArn.Failure? {
      //   return Failure(Types.KeyStoreException(message := ErrorMessages.KMS_KEY_ARN_INVALID + ". " + maybeParsedArn.error));
      // }
      // if maybeParsedArn.value.resource.resourceType != "key" {
      //   return Failure(Types.KeyStoreException(message := ErrorMessages.KMS_CONFIG_ALIAS_IS_NOT_ALLOWED));
    // }
      var parsedArn :- Operations.IsValidKmsKeyArn(config.kmsConfiguration.kmsKeyArn);
      // If KMS Configuration is a KMS Key ARN,
      // try to get KMS && DDB Clients for that Key's Region
      inferredRegion := Some(parsedArn.region);
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
      var maybeKmsClient := KMSOperations.KMSClientForRegion(inferredRegion.value);
      kmsClient :- maybeKmsClient
      .MapFailure(e => Types.ComAmazonawsKms(ComAmazonawsKms := e));
    } else {
      var maybeKmsClient := KMSOperations.KMSClient();
      kmsClient :- maybeKmsClient
      .MapFailure(e => Types.ComAmazonawsKms(ComAmazonawsKms := e));
    }

    if config.ddbClient.Some? {
      ddbClient := config.ddbClient.value;
    } else if config.ddbClient.None? && inferredRegion.Some? {
      var maybeDdbClient := DDBOperations.DDBClientForRegion(inferredRegion.value);
      ddbClient :- maybeDdbClient
      .MapFailure(e => Types.ComAmazonawsDynamodb(ComAmazonawsDynamodb := e));
    } else {
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
      ddbClient := ddbClient
      )
    );
    return Success(client as IKeyStoreClient);
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
