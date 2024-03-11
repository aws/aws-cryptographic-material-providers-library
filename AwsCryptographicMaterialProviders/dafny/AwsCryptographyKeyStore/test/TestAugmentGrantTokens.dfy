// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/Index.dfy"
include "Fixtures.dfy"
include "CleanupItems.dfy"

module TestAugmentGrantTokens {
  import Types = AwsCryptographyKeyStoreTypes
  import KMSTypes = ComAmazonawsKmsTypes
  import ComAmazonawsDynamodbTypes
  import KMS = Com.Amazonaws.Kms
  import DDB = Com.Amazonaws.Dynamodb
  import KeyStore
  import opened Wrappers
  import opened StandardLibrary.String
  import opened Fixtures
  import Structure
  import UTF8
  import CleanupItems
  import DDBKeystoreOperations
  import UUID
  import ErrorMessages

  type GrantTokens = seq<KMSTypes.GrantTokenType>

  method GetNGrantTokens(
    n: int,
    start: int
  ) returns (
    grantTokens: GrantTokens
  )
    requires 0 < n < 8192
    requires 0 <= start < 8192
  {
    var index := 0;
    var numbers := seq(n, i => i + start);
    grantTokens := [];
    while index < |numbers|
    {
      var token: string := Base10Int2String(numbers[index]);
      assert KMSTypes.IsValid_GrantTokenType( token ) by {
        assume 0 < |token| < 5; //Not going to bother prooving this generates a list of strings all of whom's length is gt 0, lt 8219
      }
      grantTokens := grantTokens + [token];
      index := index + 1;
    }
  }

  // Assert that CreateKey Fails if sum of Grant Tokens in Request and Config exceed 10
  method {:test} TestCreateKeyRequestExceedTenGrantTokensFails()
  {
    var configGrantTokens := GetNGrantTokens(9, 0);
    var requestGrantTokens := GetNGrantTokens(9, 10);
    var kmsClient :- expect KMS.KMSClient();
    var ddbClient :- expect DDB.DynamoDBClient();
    var kmsConfig := Types.KMSConfiguration.kmsKeyArn(mrkRsaKeyArn); // See Note
    var keyStoreConfig := Types.KeyStoreConfig(
      id := None,
      kmsConfiguration := kmsConfig,
      logicalKeyStoreName := logicalKeyStoreName,
      grantTokens := Some(configGrantTokens),
      ddbTableName := branchKeyStoreName,
      ddbClient := Some(ddbClient),
      kmsClient := Some(kmsClient)
    );

    var keyStore :- expect KeyStore.KeyStore(keyStoreConfig);

    var actual := keyStore.CreateKey(Types.CreateKeyInput(
      branchKeyIdentifier := None,
      encryptionContext := None,
      arn := Some(mrkRsaKeyArn), // See Note
      grantTokens := Some(requestGrantTokens)
    ));
    // Note: the RSA Key ARN will make the KMS call fail.
    // We like this, as it means a behavior failure will not create
    // records we do not need.
    expect actual.Failure?;
    // KMS failure means we MUST assert the error message to proove that
    // we failed b/c of the Grant Token verification,
    // not RSA Key.
    expect actual.error == Types.KeyStoreException(message := ErrorMessages.AUGMENT_GRANT_TOKENS_EXCEEDS_TEN);
  }

  // Assert that VersionKey Fails if sum of Grant Tokens in Request and Config exceed 10 
  method {:test} TestVersionKeyRequestExceedTenGrantTokensFails()
  {
    var configGrantTokens := GetNGrantTokens(9, 0);
    var requestGrantTokens := GetNGrantTokens(9, 10);
    var kmsClient :- expect KMS.KMSClient();
    var ddbClient :- expect DDB.DynamoDBClient();
    var kmsConfig := Types.KMSConfiguration.kmsKeyArn(mrkRsaKeyArn); // See Note
    var keyStoreConfig := Types.KeyStoreConfig(
      id := None,
      kmsConfiguration := kmsConfig,
      logicalKeyStoreName := logicalKeyStoreName,
      grantTokens := Some(configGrantTokens),
      ddbTableName := branchKeyStoreName,
      ddbClient := Some(ddbClient),
      kmsClient := Some(kmsClient)
    );

    var keyStore :- expect KeyStore.KeyStore(keyStoreConfig);

    var actual := keyStore.VersionKey(Types.VersionKeyInput(
      branchKeyIdentifier := branchKeyId,
      grantTokens := Some(requestGrantTokens)
    ));
    // Note: the RSA Key ARN will make the KMS call fail.
    // We like this, as it means a behavior failure will not create
    // records we do not need.
    expect actual.Failure?;
    // KMS failure means we MUST assert the error message to proove that
    // we failed b/c of the Grant Token verification,
    // not RSA Key.
    expect actual.error == Types.KeyStoreException(message := ErrorMessages.AUGMENT_GRANT_TOKENS_EXCEEDS_TEN);
  }

  // Assert that CreateKey Fails if invalid Grant Tokens in Request
  method {:test} TestCreateKeyRequestInvalidGrantTokenFails()
  {
    var requestGrantTokens: seq<string> := [""];
    var kmsClient :- expect KMS.KMSClient();
    var ddbClient :- expect DDB.DynamoDBClient();
    var kmsConfig := Types.KMSConfiguration.kmsKeyArn(mrkRsaKeyArn); // See Note
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

    var actual := keyStore.CreateKey(Types.CreateKeyInput(
      branchKeyIdentifier := None,
      encryptionContext := None,
      arn := Some(mrkRsaKeyArn), // See Note
      grantTokens := Some(requestGrantTokens)
    ));
    // Note: the RSA Key ARN will make the KMS call fail.
    // We like this, as it means a behavior failure will not create
    // records we do not need.
    expect actual.Failure?;
    // KMS failure means we MUST assert the error message to proove that
    // we failed b/c of the Grant Token verification,
    // not RSA Key.
    expect actual.error == Types.KeyStoreException(message := "A Grant Token passed to CreateKey has invalid length");
  }

  // Assert that VersionKey Fails if invalid Grant Tokens in Request
  method {:test} TestVersionKeyRequestInvalidGrantTokensFails()
  {
    var requestGrantTokens: seq<string> := [""];
    var kmsClient :- expect KMS.KMSClient();
    var ddbClient :- expect DDB.DynamoDBClient();
    var kmsConfig := Types.KMSConfiguration.kmsKeyArn(mrkRsaKeyArn); // See Note
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

    var actual := keyStore.VersionKey(Types.VersionKeyInput(
      branchKeyIdentifier := branchKeyId,
      grantTokens := Some(requestGrantTokens)
    ));
    // Note: the RSA Key ARN will make the KMS call fail.
    // We like this, as it means a behavior failure will not create
    // records we do not need.
    expect actual.Failure?;
    // KMS failure means we MUST assert the error message to proove that
    // we failed b/c of the Grant Token verification,
    // not RSA Key.
    expect actual.error == Types.KeyStoreException(message := "A Grant Token passed to VersionKey has invalid length");
  }

  // TODO Postal Horn: Assert Grant Token Augmentation Happy Path (Post Pen Test Start)
}
