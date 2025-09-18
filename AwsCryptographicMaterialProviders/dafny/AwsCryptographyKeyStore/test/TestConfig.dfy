// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/Index.dfy"
include "Fixtures.dfy"

module TestConfig {
  import Types = AwsCryptographyKeyStoreTypes
  import ComAmazonawsKmsTypes
  import KMS = Com.Amazonaws.Kms
  import DDB = Com.Amazonaws.Dynamodb
  import KeyStore
  import opened Wrappers
  import opened Fixtures
  import UUID
  import ErrorMessages = KeyStoreErrorMessages

  method {:test} TestInvalidKmsKeyArnConfig() {
    var kmsClient :- expect KMS.KMSClient();
    var ddbClient :- expect DDB.DynamoDBClient();
    var kmsConfig := Types.KMSConfiguration.kmsKeyArn(keyId);

    var keyStoreConfig := Types.KeyStoreConfig(
      id := None,
      kmsConfiguration := kmsConfig,
      logicalKeyStoreName := logicalKeyStoreName,
      grantTokens := None,
      ddbTableName := branchKeyStoreName,
      ddbClient := Some(ddbClient),
      kmsClient := Some(kmsClient)
    );

    var keyStore := KeyStore.KeyStore(keyStoreConfig);
    expect keyStore.Failure?;
    match keyStore.error {
      case KeyStoreException(message) =>
        expect |message| > |ErrorMessages.KMS_CONFIG_KMS_ARN_INVALID|;
        expect message[..|ErrorMessages.KMS_CONFIG_KMS_ARN_INVALID|] == ErrorMessages.KMS_CONFIG_KMS_ARN_INVALID;
      case _ => expect false, "Invalid KMS Key ARN should fail Key Store Construction";
    }
  }

  //= aws-encryption-sdk-specification/framework/branch-key-store.md#aws-kms-configuration
  //= type=test
  //# This ARN MUST NOT be an Alias.
  method {:test} TestInvalidKmsKeyArnAliasConfig() {
    var kmsClient :- expect KMS.KMSClient();
    var ddbClient :- expect DDB.DynamoDBClient();
    var kmsConfig := Types.KMSConfiguration.kmsKeyArn(kmsKeyAlias);

    var keyStoreConfig := Types.KeyStoreConfig(
      id := None,
      kmsConfiguration := kmsConfig,
      logicalKeyStoreName := logicalKeyStoreName,
      grantTokens := None,
      ddbTableName := branchKeyStoreName,
      ddbClient := Some(ddbClient),
      kmsClient := Some(kmsClient)
    );

    var keyStore := KeyStore.KeyStore(keyStoreConfig);
    expect keyStore.Failure?;
    match keyStore.error {
      case KeyStoreException(message) =>
        expect |message| >= |ErrorMessages.ALIAS_NOT_ALLOWED|;
        expect message[..|ErrorMessages.ALIAS_NOT_ALLOWED|] == ErrorMessages.ALIAS_NOT_ALLOWED;
      case _ => expect false, "Alias should fail Key Store Construction";
    }
  }


  method {:test} TestValidConfig() {
    var kmsClient :- expect KMS.KMSClient();
    var ddbClient :- expect DDB.DynamoDBClient();
    var kmsConfig := Types.KMSConfiguration.kmsKeyArn(keyArn);

    var keyStoreConfig := Types.KeyStoreConfig(
      id := None,
      kmsConfiguration := kmsConfig,
      logicalKeyStoreName := logicalKeyStoreName,
      grantTokens := None,
      ddbTableName := branchKeyStoreName,
      ddbClient := Some(ddbClient),
      kmsClient := Some(kmsClient)
    );

    var keyStore := KeyStore.KeyStore(keyStoreConfig);
    expect keyStore.Success?;

    var conf :- expect keyStore.value.GetKeyStoreInfo();

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#keystore-id
    //= type=test
    //# If one is not supplied, then a [version 4 UUID](https://www.ietf.org/rfc/rfc4122.txt) MUST be used.
    var idByteUUID :- expect UUID.ToByteArray(conf.keyStoreId);
    var idRoundTrip :- expect UUID.FromByteArray(idByteUUID);
    expect idRoundTrip == conf.keyStoreId;

    expect conf.keyStoreName == branchKeyStoreName;
    expect conf.logicalKeyStoreName == logicalKeyStoreName;
    expect conf.kmsConfiguration == kmsConfig;

  }

  method {:test} TestValidConfigNoClients() {
    var kmsClient :- expect KMS.KMSClient();
    var ddbClient :- expect DDB.DynamoDBClient();
    var kmsConfig := Types.KMSConfiguration.kmsKeyArn(keyArn);

    // Test with no kms client supplied
    //= aws-encryption-sdk-specification/framework/branch-key-store.md#kms-client
    //= type=TODO
    //# If the AWS KMS Configuration is KMS Key ARN or KMS MRKey ARN,
    //# and no KMS Client is provided,
    //# a new KMS Client MUST be created
    //# with the region of the supplied KMS ARN.

    // create and use us-east-2 Keystore and Branch Key
    // Assert call to get Branch Key ID succeeds.
    // As long as tests are run NOT in us-east-2,
    // this proves that the DDB Client used the region
    // from the KMS Key ARN to initialize the DDB Client

    var keyStoreConfig := Types.KeyStoreConfig(
      id := None,
      kmsConfiguration := kmsConfig,
      logicalKeyStoreName := logicalKeyStoreName,
      grantTokens := None,
      ddbTableName := branchKeyStoreName,
      ddbClient := Some(ddbClient),
      kmsClient := None
    );
    var keyStore := KeyStore.KeyStore(keyStoreConfig);
    expect keyStore.Success?;

    // Test with no ddb client supplied

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#dynamodb-client
    //= type=TODO
    //# If the AWS KMS Configuration is KMS Key ARN or KMS MRKey ARN,
    //# and no DynamoDb Client is provided,
    //# a new DynamoDb Client MUST be created
    //# with the region of the supplied KMS ARN.

    // create and use us-east-2 Keystore and Branch Key
    // Assert call to get Branch Key ID succeeds.
    // As long as tests are run NOT in us-east-2,
    // this proves that the DDB Client used the region
    // from the KMS Key ARN to initialize the DDB Client
    keyStoreConfig := Types.KeyStoreConfig(
      id := None,
      kmsConfiguration := kmsConfig,
      logicalKeyStoreName := logicalKeyStoreName,
      grantTokens := None,
      ddbTableName := branchKeyStoreName,
      ddbClient := None,
      kmsClient := Some(kmsClient)
    );
    keyStore := KeyStore.KeyStore(keyStoreConfig);
    expect keyStore.Success?;

    // Test with no clients supplied

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#dynamodb-client
    //= type=TODO
    //# If the AWS KMS Configuration is Discovery,
    //# and no DynamoDb Client is provided,
    //# a new DynamoDb Client MUST be created
    //# with the default configuration.

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#kms-client
    //= type=TODO
    //# If the AWS KMS Configuration is Discovery,
    //# and no KMS Client is provided,
    //# a new KMS Client MUST be created
    //# with the default configuration.

    // create and use us-east-2 Keystore and Branch Key
    // Assert call to get Branch Key ID FAILS.
    // As long as tests are run NOT in us-east-2,
    // this proves that the DDB Client used the region
    // from the KMS Key ARN to initialize the DDB Client
    keyStoreConfig := Types.KeyStoreConfig(
      id := None,
      kmsConfiguration := kmsConfig,
      logicalKeyStoreName := logicalKeyStoreName,
      grantTokens := None,
      ddbTableName := branchKeyStoreName,
      ddbClient := None,
      kmsClient := None
    );
    keyStore := KeyStore.KeyStore(keyStoreConfig);
    expect keyStore.Success?;
  }
}
