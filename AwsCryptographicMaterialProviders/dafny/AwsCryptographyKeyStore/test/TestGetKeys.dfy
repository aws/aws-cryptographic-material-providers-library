// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/Index.dfy"
include "Fixtures.dfy"
include "../src/ErrorMessages.dfy"

// TODO-HV2-M1: add more HV2 tests.
// TODO-HV2-M1: Maybe refactor this module to TestGetHv1Keys and create another TestGetHv2Keys
module TestGetKeys {
  import Types = AwsCryptographyKeyStoreTypes
  import ComAmazonawsKmsTypes
  import KMS = Com.Amazonaws.Kms
  import DDB = Com.Amazonaws.Dynamodb
  import KeyStore
  import ComAmazonawsDynamodbTypes
  import opened Wrappers
  import opened Fixtures
  import UTF8
  import ErrorMessages = KeyStoreErrorMessages

  const incorrectLogicalName := "MySuperAwesomeTableName"

  method {:test} TestGetBeaconKey()
  {
    var kmsClient :- expect KMS.KMSClient();
    var ddbClient :- expect DDB.DynamoDBClient();
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

    var keyStore :- expect KeyStore.KeyStore(keyStoreConfig);

    var beaconKeyResult :- expect keyStore.GetBeaconKey(
      Types.GetBeaconKeyInput(
        branchKeyIdentifier := branchKeyId
      ));
    expect beaconKeyResult.beaconKeyMaterials.beaconKeyIdentifier == branchKeyId;
    expect beaconKeyResult.beaconKeyMaterials.beaconKey.Some?;
    expect |beaconKeyResult.beaconKeyMaterials.beaconKey.value| == 32;

    var hv2ActiveResult :- expect keyStore.GetBeaconKey(
      Types.GetBeaconKeyInput(
        branchKeyIdentifier := hv2BranchKeyId
      ));

    expect hv2ActiveResult.beaconKeyMaterials.beaconKeyIdentifier == hv2BranchKeyId;
    expect hv2ActiveResult.beaconKeyMaterials.beaconKey.Some?;
    expect |hv2ActiveResult.beaconKeyMaterials.beaconKey.value| == 32;
  }

  method {:test} {:isolate_assertions} TestGetActiveKey()
  {
    var kmsClient :- expect KMS.KMSClient();
    var ddbClient :- expect DDB.DynamoDBClient();
    var kmsConfig := Types.KMSConfiguration.kmsKeyArn(keyArn);
    assume {:axiom} ddbClient.Modifies == {}; // Turns off verification
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

    var keyStore :- expect KeyStore.KeyStore(keyStoreConfig);

    var activeResult :- expect keyStore.GetActiveBranchKey(
      Types.GetActiveBranchKeyInput(
        branchKeyIdentifier := branchKeyId
      ));

    expect activeResult.branchKeyMaterials.branchKeyIdentifier == branchKeyId;
    expect activeResult.branchKeyMaterials.branchKeyVersion == branchKeyIdActiveVersionUtf8Bytes;
    expect |activeResult.branchKeyMaterials.branchKey| == 32;

    var hv2ActiveResult :- expect keyStore.GetActiveBranchKey(
      Types.GetActiveBranchKeyInput(
        branchKeyIdentifier := hv2BranchKeyId
      ));

    expect hv2ActiveResult.branchKeyMaterials.branchKeyIdentifier == hv2BranchKeyId;
    expect hv2ActiveResult.branchKeyMaterials.branchKeyVersion == hv2BranchKeyIdActiveVersionUtf8Bytes;
    expect |hv2ActiveResult.branchKeyMaterials.branchKey| == 32;
  }

  method {:test} {:isolate_assertions} TestGetActiveMrkKey()
  {
    var ddbClient :- expect DDB.DynamoDBClient();
    assume {:axiom} ddbClient.Modifies == {}; // Turns off verification, but allows calling underTest
    var eastKeyStoreConfig := Types.KeyStoreConfig(
      id := None,
      kmsConfiguration := KmsConfigEast,
      logicalKeyStoreName := logicalKeyStoreName,
      storage := Some(
        Types.ddb(
          Types.DynamoDBTable(
            ddbTableName := branchKeyStoreName,
            ddbClient := Some(ddbClient)
          )))
    );

    var westKeyStoreConfig := Types.KeyStoreConfig(
      id := None,
      kmsConfiguration := KmsConfigWest,
      logicalKeyStoreName := logicalKeyStoreName,
      storage := Some(
        Types.ddb(
          Types.DynamoDBTable(
            ddbTableName := branchKeyStoreName,
            ddbClient := Some(ddbClient)
          )))
    );

    var eastMrkKeyStoreConfig := Types.KeyStoreConfig(
      id := None,
      kmsConfiguration := KmsMrkConfigEast,
      logicalKeyStoreName := logicalKeyStoreName,
      storage := Some(
        Types.ddb(
          Types.DynamoDBTable(
            ddbTableName := branchKeyStoreName,
            ddbClient := Some(ddbClient)
          )))
    );

    var westMrkKeyStoreConfig := Types.KeyStoreConfig(
      id := None,
      kmsConfiguration := KmsMrkConfigWest,
      logicalKeyStoreName := logicalKeyStoreName,
      storage := Some(
        Types.ddb(
          Types.DynamoDBTable(
            ddbTableName := branchKeyStoreName,
            ddbClient := Some(ddbClient)
          )))
    );

    // KmsMrkConfigAP is NOT created
    var apMrkKeyStoreConfig := Types.KeyStoreConfig(
      id := None,
      kmsConfiguration := KmsMrkConfigAP,
      logicalKeyStoreName := logicalKeyStoreName,
      storage := Some(
        Types.ddb(
          Types.DynamoDBTable(
            ddbTableName := branchKeyStoreName,
            ddbClient := Some(ddbClient)
          )))
    );


    var westKeyStore :- expect KeyStore.KeyStore(westKeyStoreConfig);
    var eastKeyStore :- expect KeyStore.KeyStore(eastKeyStoreConfig);
    var westMrkKeyStore :- expect KeyStore.KeyStore(westMrkKeyStoreConfig);
    var eastMrkKeyStore :- expect KeyStore.KeyStore(eastMrkKeyStoreConfig);
    var apMrkKeyStore :- expect KeyStore.KeyStore(apMrkKeyStoreConfig);

    // All four should work when the regions match

    var activeResult :- expect westKeyStore.GetActiveBranchKey(
      Types.GetActiveBranchKeyInput(branchKeyIdentifier := WestBranchKey));
    expect activeResult.branchKeyMaterials.branchKeyIdentifier == WestBranchKey;
    expect |activeResult.branchKeyMaterials.branchKey| == 32;

    activeResult :- expect eastKeyStore.GetActiveBranchKey(
      Types.GetActiveBranchKeyInput(branchKeyIdentifier := EastBranchKey));
    expect activeResult.branchKeyMaterials.branchKeyIdentifier == EastBranchKey;
    expect |activeResult.branchKeyMaterials.branchKey| == 32;

    activeResult :- expect westMrkKeyStore.GetActiveBranchKey(
      Types.GetActiveBranchKeyInput(branchKeyIdentifier := WestBranchKey));
    expect activeResult.branchKeyMaterials.branchKeyIdentifier == WestBranchKey;
    expect |activeResult.branchKeyMaterials.branchKey| == 32;

    activeResult :- expect eastMrkKeyStore.GetActiveBranchKey(
      Types.GetActiveBranchKeyInput(branchKeyIdentifier := EastBranchKey));
    expect activeResult.branchKeyMaterials.branchKeyIdentifier == EastBranchKey;
    expect |activeResult.branchKeyMaterials.branchKey| == 32;

    // MRK Configuration should work with the other region

    activeResult :- expect westMrkKeyStore.GetActiveBranchKey(
      Types.GetActiveBranchKeyInput(branchKeyIdentifier := EastBranchKey));
    expect activeResult.branchKeyMaterials.branchKeyIdentifier == EastBranchKey;
    expect |activeResult.branchKeyMaterials.branchKey| == 32;

    activeResult :- expect eastMrkKeyStore.GetActiveBranchKey(
      Types.GetActiveBranchKeyInput(branchKeyIdentifier := WestBranchKey));
    expect activeResult.branchKeyMaterials.branchKeyIdentifier == WestBranchKey;
    expect |activeResult.branchKeyMaterials.branchKey| == 32;

    // Plain Configuration should fail with the other region

    var badResult := westKeyStore.GetActiveBranchKey(
      Types.GetActiveBranchKeyInput(branchKeyIdentifier := EastBranchKey));
    expect badResult.Failure?;
    expect badResult.error == Types.Error.KeyStoreException(message := ErrorMessages.GET_KEY_ARN_DISAGREEMENT);

    badResult := eastKeyStore.GetActiveBranchKey(
      Types.GetActiveBranchKeyInput(branchKeyIdentifier := WestBranchKey));
    expect badResult.Failure?;
    expect badResult.error == Types.Error.KeyStoreException(message := ErrorMessages.GET_KEY_ARN_DISAGREEMENT);

    // apMrkKeyStore should always fail

    badResult := apMrkKeyStore.GetActiveBranchKey(
      Types.GetActiveBranchKeyInput(branchKeyIdentifier := WestBranchKey));
    expect badResult.Failure?;
    expect badResult.error.ComAmazonawsKms?;
    expect badResult.error.ComAmazonawsKms.OpaqueWithText?;
    // it's an opaque error, so I can't test its contents
  }

  method {:test} TestGetBranchKeyVersion()
  {
    var keyStore :- expect DefaultKeyStore();

    var versionResult :- expect keyStore.GetBranchKeyVersion(
      Types.GetBranchKeyVersionInput(
        branchKeyIdentifier := branchKeyId,
        branchKeyVersion := branchKeyIdActiveVersion
      ));

    var testBytes :- expect UTF8.Encode(branchKeyIdActiveVersion);

    expect versionResult.branchKeyMaterials.branchKeyIdentifier == branchKeyId;
    expect versionResult.branchKeyMaterials.branchKeyVersion == branchKeyIdActiveVersionUtf8Bytes == testBytes;
    expect |versionResult.branchKeyMaterials.branchKey| == 32;

    var hv2versionResult :- expect keyStore.GetBranchKeyVersion(
      Types.GetBranchKeyVersionInput(
        branchKeyIdentifier := hv2BranchKeyId,
        branchKeyVersion := hv2BranchKeyIdWithEC
      ));

    var hv2testBytes :- expect UTF8.Encode(hv2BranchKeyIdWithEC);

    expect hv2versionResult.branchKeyMaterials.branchKeyIdentifier == hv2BranchKeyId;
    expect hv2versionResult.branchKeyMaterials.branchKeyVersion == hv2BranchKeyIdActiveVersionUtf8Bytes == hv2testBytes;
    expect |hv2versionResult.branchKeyMaterials.branchKey| == 32;
  }


  method {:test} TestGetActiveKeyWithIncorrectKmsKeyArn() {
    var kmsClient :- expect KMS.KMSClient();
    var ddbClient :- expect DDB.DynamoDBClient();
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

    var keyStore :- expect KeyStore.KeyStore(keyStoreConfig);

    var activeResult := keyStore.GetActiveBranchKey(
      Types.GetActiveBranchKeyInput(
        branchKeyIdentifier := postalHornBranchKeyId
      ));
    expect activeResult.Failure?;
    expect activeResult.error == Types.KeyStoreException(message := ErrorMessages.GET_KEY_ARN_DISAGREEMENT);
  }

  method {:test} TestGetActiveKeyWrongLogicalKeyStoreName() {
    var kmsClient :- expect KMS.KMSClient();
    var ddbClient :- expect DDB.DynamoDBClient();
    var kmsConfig := Types.KMSConfiguration.kmsKeyArn(keyArn);

    var keyStoreConfig := Types.KeyStoreConfig(
      id := None,
      kmsConfiguration := kmsConfig,
      logicalKeyStoreName := incorrectLogicalName,
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

    var keyStore :- expect KeyStore.KeyStore(keyStoreConfig);

    var activeResult := keyStore.GetActiveBranchKey(
      Types.GetActiveBranchKeyInput(
        branchKeyIdentifier := branchKeyId
      ));

    expect activeResult.Failure?;
    match activeResult.error {
      case ComAmazonawsKms(nestedError) =>
        expect nestedError.InvalidCiphertextException?;
      case _ => expect false, "Wrong Logical Keystore Name SHOULD Fail with KMS InvalidCiphertextException.";
    }
  }

  method {:test} TestGetActiveKeyDoesNotExistFails()
  {
    var kmsClient :- expect KMS.KMSClient();
    var ddbClient :- expect DDB.DynamoDBClient();
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

    var keyStore :- expect KeyStore.KeyStore(keyStoreConfig);

    var activeResult := keyStore.GetActiveBranchKey(
      Types.GetActiveBranchKeyInput(
        branchKeyIdentifier := "Robbie"
      ));

    expect activeResult.Failure?;
    expect activeResult.error == Types.KeyStoreException(message := ErrorMessages.NO_CORRESPONDING_BRANCH_KEY);
    //AwsCryptographyKeyStoreTypes.Error.KeyStoreException(No item found for corresponding branch key identifier.)
  }

  method {:test} TestGetActiveKeyWithNoClients() {
    var kmsConfig := Types.KMSConfiguration.kmsKeyArn(keyArn);

    var keyStoreConfig := Types.KeyStoreConfig(
      id := None,
      kmsConfiguration := kmsConfig,
      logicalKeyStoreName := logicalKeyStoreName,
      storage := Some(
        Types.ddb(
          Types.DynamoDBTable(
            ddbTableName := branchKeyStoreName
          )))
    );

    var keyStore :- expect KeyStore.KeyStore(keyStoreConfig);

    var activeResult :- expect keyStore.GetActiveBranchKey(
      Types.GetActiveBranchKeyInput(
        branchKeyIdentifier := branchKeyId
      ));

    expect |activeResult.branchKeyMaterials.branchKey| == 32;
  }
}
