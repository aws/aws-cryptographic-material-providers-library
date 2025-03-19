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
      storage := Some(
        Types.ddb(
          Types.DynamoDBTable(
            ddbTableName := branchKeyStoreName,
            ddbClient := Some(ddbClient)
          ))),
      keyManagement := Some(
        Types.kms(
          Types.AwsKms(
            kmsClient := Some(kmsClient)
          )))
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
      storage := Some(
        Types.ddb(
          Types.DynamoDBTable(
            ddbTableName := branchKeyStoreName,
            ddbClient := Some(ddbClient)
          ))),
      keyManagement := Some(
        Types.kms(
          Types.AwsKms(
            kmsClient := Some(kmsClient)
          )))
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


  method {:vcs_split_on_every_assert} {:test} TestValidConfig() {
    var kmsClient :- expect ProvideKMSClient();
    var ddbClient :- expect ProvideDDBClient();
    var kmsConfig := Types.KMSConfiguration.kmsKeyArn(keyArn);

    var keyStoreConfig := Types.KeyStoreConfig(
      id := None,
      kmsConfiguration := kmsConfig,
      logicalKeyStoreName := logicalKeyStoreName,
      storage := Some(
        Types.ddb(
          Types.DynamoDBTable(
            ddbTableName := branchKeyStoreName,
            ddbClient := Some(ddbClient)
          ))),
      keyManagement := Some(
        Types.kms(
          Types.AwsKms(
            kmsClient := Some(kmsClient)
          )))
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
      ddbTableName := Some(branchKeyStoreName),
      ddbClient := Some(ddbClient),
      kmsClient := None
    );
    var keyStore := KeyStore.KeyStore(keyStoreConfig);
    expect keyStore.Success?;

    // Test with no ddb client supplied

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#dynamodb-client

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
      ddbTableName := Some(branchKeyStoreName),
      ddbClient := None,
      kmsClient := Some(kmsClient)
    );
    keyStore := KeyStore.KeyStore(keyStoreConfig);
    expect keyStore.Success?;

    // Test with no clients supplied

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
      ddbTableName := Some(branchKeyStoreName),
      ddbClient := None,
      kmsClient := None
    );
    keyStore := KeyStore.KeyStore(keyStoreConfig);
    expect keyStore.Success?;
  }

  method {:test} TestGenerateRandom() {
    var kmsClient :- expect KMS.KMSClient();

      // Test Case 1: Happy Path
    {
      var response := GenerateRandom(kmsClient);
      expect response.Success?;
      expect response.value.Plaintext.Some?;
      expect |response.value.Plaintext.value| == 32;
      expect |kmsClient.History.GenerateRandom| == 1;
      print response.value.Plaintext.value;
    }

      // Test Case 2: Verify History Modification
    {
      var oldGenerateRandomHistory := kmsClient.History.GenerateRandom;
      var oldEncryptHistory := kmsClient.History.Encrypt;
      var oldDecryptHistory := kmsClient.History.Decrypt;

      var result := GenerateRandom([], kmsClient);

      expect |kmsClient.History.GenerateRandom| == |oldGenerateRandomHistory| + 1;
      expect kmsClient.History.Encrypt == oldEncryptHistory;
      expect kmsClient.History.Decrypt == oldDecryptHistory;
    }

      // Test Case 3: Verify Request Format
    {
      var result := GenerateRandom(kmsClient);
      var lastRequest := Seq.Last(kmsClient.History.GenerateRandom).input;

      expect lastRequest == KMS.GenerateRandomRequest(
                              NumberOfBytes := Some(32),
                              CustomKeyStoreId := None,
                              Recipient := None
                            );
    }

      // Test Case 4: Verify Response Matching
    {
      var result := GenerateRandom([], kmsClient);
      expect result.Success?;
      var lastOperation := Seq.Last(kmsClient.History.GenerateRandom).output;
      expect lastOperation.Success?;
      expect lastOperation.value == result.value;
    }
  }
}
