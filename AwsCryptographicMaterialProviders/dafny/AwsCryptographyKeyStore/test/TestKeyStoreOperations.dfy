// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/Index.dfy"
include "Fixtures.dfy"
include "../src/Structure.dfy"
include "CleanupItems.dfy"
include "../src/ErrorMessages.dfy"

module TestKeyStoreOperations {
  import Types = AwsCryptographyKeyStoreTypes
  import ComAmazonawsKmsTypes
  import ComAmazonawsDynamodbTypes
  import KMS = Com.Amazonaws.Kms
  import DDB = Com.Amazonaws.Dynamodb
  import KeyStore
  import opened Wrappers
  import opened Fixtures
  import Structure
  import UTF8
  import CleanupItems
  import DDBKeystoreOperations
  import UUID
  import ErrorMessages
  
  method {:test} TestCreateKeyDiscoveryNoARNFails()
  {
    var kmsClient :- expect KMS.KMSClient();
    var ddbClient :- expect DDB.DynamoDBClient();
    var kmsConfig := Types.KMSConfiguration.discovery(Types.Discovery());
    var keyStoreConfig := Types.KeyStoreConfig(
      id := None,
      kmsConfiguration := kmsConfig,
      logicalKeyStoreName := logicalKeyStoreName,
      grantTokens := None,
      ddbTableName := branchKeyStoreName,
      ddbClient := Some(ddbClient),
      kmsClient := Some(kmsClient)
    );

    var keyStore :- expect KeyStore.KeyStore(keyStoreConfig);
    var actual := keyStore.CreateKey(
      Types.CreateKeyInput(
        branchKeyIdentifier := None,
        encryptionContext := None,
        arn := None
    ));
    expect actual.Failure?;
    expect actual.error == Types.KeyStoreException(message := ErrorMessages.DISCOVERY_CREATE_KEY_NO_ARN_ERROR_MSG);
  }

  method {:test} TestCreateKeyDisagreeARNsFails()
  {
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
    var keyStore :- expect KeyStore.KeyStore(keyStoreConfig);
    
    var actual := keyStore.CreateKey(
      Types.CreateKeyInput(
        branchKeyIdentifier := None,
        encryptionContext := None,
        arn := Some(mkrKeyArn)
    ));
    expect actual.Failure?;
    expect actual.error == Types.KeyStoreException(message := ErrorMessages.CREATE_KEY_KMS_ARN_DISAGREEMENT);
  }

  // TODO: refactor to method that takes kmsConfig
  method {:test} TestCreateKeyInvalidArn()
  {
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
    var keyStore :- expect KeyStore.KeyStore(keyStoreConfig);
    
    var actual := keyStore.CreateKey(
      Types.CreateKeyInput(
        branchKeyIdentifier := None,
        encryptionContext := None,
        arn := Some("robbie")
    ));
    expect actual.Failure?;
    expect actual.error == Types.KeyStoreException(message := ErrorMessages.CREATE_KEY_KMS_ARN_DISAGREEMENT);
    //expect actual.error == Types.KeyStoreException(message := ErrorMessages.KMS_KEY_ARN_INVALID);
    // Error Message could be 

    kmsConfig := Types.KMSConfiguration.discovery(Types.Discovery());
    keyStoreConfig := Types.KeyStoreConfig(
      id := None,
      kmsConfiguration := kmsConfig,
      logicalKeyStoreName := logicalKeyStoreName,
      grantTokens := None,
      ddbTableName := branchKeyStoreName,
      ddbClient := Some(ddbClient),
      kmsClient := Some(kmsClient)
    );
    keyStore :- expect KeyStore.KeyStore(keyStoreConfig);
    actual := keyStore.CreateKey(
      Types.CreateKeyInput(
        branchKeyIdentifier := None,
        encryptionContext := None,
        arn := Some("robbie")
    ));
    expect actual.Failure?;
    expect actual.error == Types.KeyStoreException(message := ErrorMessages.KMS_KEY_ARN_INVALID);
  }

  // method {:test} TestGetKey()
  // {
  //   var kmsClient :- expect KMS.KMSClient();
  //   var ddbClient :- expect DDB.DynamoDBClient();
  //   var kmsConfig := Types.KMSConfiguration.discovery(Types.Discovery());
  //   var keyStoreConfig := Types.KeyStoreConfig(
  //     id := None,
  //     kmsConfiguration := kmsConfig,
  //     logicalKeyStoreName := logicalKeyStoreName,
  //     grantTokens := None,
  //     ddbTableName := branchKeyStoreName,
  //     ddbClient := Some(ddbClient),
  //     kmsClient := Some(kmsClient)
  //   );

  //   var keyStore :- expect KeyStore.KeyStore(keyStoreConfig);
  //   var actual := keyStore.CreateKey(
  //     Types.CreateKeyInput(
  //       branchKeyIdentifier := None,
  //       encryptionContext := None,
  //       arn := None
  //   ));
  //   expect actual.Failure?;
  //   expect actual.error == Types.KeyStoreException(message := ErrorMessages.DISCOVERY_CREATE_KEY_NO_ARN_ERROR_MSG);
  // }


}
