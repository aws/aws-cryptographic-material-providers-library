// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/Index.dfy"
include "Fixtures.dfy"
include "../src/ErrorMessages.dfy"

module TestGetKeys {
  import Types = AwsCryptographyKeyStoreTypes
  import ComAmazonawsKmsTypes
  import KMS = Com.Amazonaws.Kms
  import DDB = Com.Amazonaws.Dynamodb
  import KeyStore
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
      grantTokens := None,
      ddbTableName := branchKeyStoreName,
      ddbClient := Some(ddbClient),
      kmsClient := Some(kmsClient)
    );

    var keyStore :- expect KeyStore.KeyStore(keyStoreConfig);

    var beaconKeyResult :- expect keyStore.GetBeaconKey(
      Types.GetBeaconKeyInput(
        branchKeyIdentifier := branchKeyId
      ));
    expect beaconKeyResult.beaconKeyMaterials.beaconKeyIdentifier == branchKeyId;
    expect beaconKeyResult.beaconKeyMaterials.beaconKey.Some?;
    expect |beaconKeyResult.beaconKeyMaterials.beaconKey.value| == 32;
  }

  method {:test} TestGetActiveKey()
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

    var activeResult :- expect keyStore.GetActiveBranchKey(
      Types.GetActiveBranchKeyInput(
        branchKeyIdentifier := branchKeyId
      ));

    expect activeResult.branchKeyMaterials.branchKeyIdentifier == branchKeyId;
    expect activeResult.branchKeyMaterials.branchKeyVersion == branchKeyIdActiveVersionUtf8Bytes;
    expect |activeResult.branchKeyMaterials.branchKey| == 32;
  }

  method {:test} TestGetActiveMrkKey()
  {
    var ddbClient :- expect DDB.DynamoDBClient();

    var eastKeyStoreConfig := Types.KeyStoreConfig(
      id := None,
      kmsConfiguration := KmsConfigEast,
      logicalKeyStoreName := logicalKeyStoreName,
      grantTokens := None,
      ddbTableName := branchKeyStoreName,
      ddbClient := Some(ddbClient)
    );

    var westKeyStoreConfig := Types.KeyStoreConfig(
      id := None,
      kmsConfiguration := KmsConfigWest,
      logicalKeyStoreName := logicalKeyStoreName,
      grantTokens := None,
      ddbTableName := branchKeyStoreName,
      ddbClient := Some(ddbClient)
    );

    var eastMrkKeyStoreConfig := Types.KeyStoreConfig(
      id := None,
      kmsConfiguration := KmsMrkConfigEast,
      logicalKeyStoreName := logicalKeyStoreName,
      grantTokens := None,
      ddbTableName := branchKeyStoreName,
      ddbClient := Some(ddbClient)
    );

    var westMrkKeyStoreConfig := Types.KeyStoreConfig(
      id := None,
      kmsConfiguration := KmsMrkConfigWest,
      logicalKeyStoreName := logicalKeyStoreName,
      grantTokens := None,
      ddbTableName := branchKeyStoreName,
      ddbClient := Some(ddbClient)
    );

    // KmsMrkConfigAP is NOT created
    var apMrkKeyStoreConfig := Types.KeyStoreConfig(
      id := None,
      kmsConfiguration := KmsMrkConfigAP,
      logicalKeyStoreName := logicalKeyStoreName,
      grantTokens := None,
      ddbTableName := branchKeyStoreName,
      ddbClient := Some(ddbClient)
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

    var versionResult :- expect keyStore.GetBranchKeyVersion(
      Types.GetBranchKeyVersionInput(
        branchKeyIdentifier := branchKeyId,
        branchKeyVersion := branchKeyIdActiveVersion
      ));

    var testBytes :- expect UTF8.Encode(branchKeyIdActiveVersion);

    expect versionResult.branchKeyMaterials.branchKeyIdentifier == branchKeyId;
    expect versionResult.branchKeyMaterials.branchKeyVersion == branchKeyIdActiveVersionUtf8Bytes == testBytes;
    expect |versionResult.branchKeyMaterials.branchKey| == 32;
  }


  method {:test} TestGetActiveKeyWithIncorrectKmsKeyArn() {
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
      grantTokens := None,
      ddbTableName := branchKeyStoreName,
      ddbClient := Some(ddbClient),
      kmsClient := Some(kmsClient)
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
      grantTokens := None,
      ddbTableName := branchKeyStoreName,
      ddbClient := Some(ddbClient),
      kmsClient := Some(kmsClient)
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
      grantTokens := None,
      ddbTableName := branchKeyStoreName,
      ddbClient := None,
      kmsClient := None
    );

    var keyStore :- expect KeyStore.KeyStore(keyStoreConfig);

    var activeResult :- expect keyStore.GetActiveBranchKey(
      Types.GetActiveBranchKeyInput(
        branchKeyIdentifier := branchKeyId
      ));

    expect |activeResult.branchKeyMaterials.branchKey| == 32;
  }

  method {:test} TestGetActiveBranchKeyFromNativeRustWrite() {
    var kmsConfig := Types.KMSConfiguration.kmsKeyArn(keyArn);

    var keyStoreConfig := Types.KeyStoreConfig(
      id := None,
      kmsConfiguration := kmsConfig,
      logicalKeyStoreName := logicalKeyStoreName,
      grantTokens := None,
      ddbTableName := branchKeyStoreName,
      ddbClient := None,
      kmsClient := None
    );

    var keyStore :- expect KeyStore.KeyStore(keyStoreConfig);

    var activeResult :- expect keyStore.GetActiveBranchKey(
      Types.GetActiveBranchKeyInput(
        branchKeyIdentifier := nativeRustBranchKey
      ));
    
    var versionResult :- expect keyStore.GetBranchKeyVersion(
      Types.GetBranchKeyVersionInput(
        branchKeyIdentifier := nativeRustBranchKey,
        branchKeyVersion := nativeRustBranchKeyVersion
      )
    );

    // length checks  
    expect |versionResult.branchKeyMaterials.branchKey| == 32;
    expect |activeResult.branchKeyMaterials.branchKey| == 32;
    
    // check version on active materials is the same as the version
    // in the version materials
    expect activeResult.branchKeyMaterials.branchKeyVersion == 
      versionResult.branchKeyMaterials.branchKeyVersion;
    
    // check that the branch key material is the same on both
    expect activeResult.branchKeyMaterials.branchKey ==
      versionResult.branchKeyMaterials.branchKey;

  }

  method {:test} TestVersionedActiveBranchKeyFromNativeRustWrite() {

    var kmsConfig := Types.KMSConfiguration.kmsKeyArn(keyArn);

    var keyStoreConfig := Types.KeyStoreConfig(
      id := None,
      kmsConfiguration := kmsConfig,
      logicalKeyStoreName := logicalKeyStoreName,
      grantTokens := None,
      ddbTableName := branchKeyStoreName,
      ddbClient := None,
      kmsClient := None
    );

    var keyStore :- expect KeyStore.KeyStore(keyStoreConfig);
    
    var versionActiveResult :- expect keyStore.GetActiveBranchKey(
      Types.GetActiveBranchKeyInput(
        branchKeyIdentifier := rotatedNativeRustBranchKey
      ));
    
    var versionActiveVersionResult :- expect keyStore.GetBranchKeyVersion(
      Types.GetBranchKeyVersionInput(
        branchKeyIdentifier := rotatedNativeRustBranchKey,
        branchKeyVersion := rotatedNativeRustBranchKeyActiveVersion
      )
    );

    var oldVersionResult :- expect keyStore.GetBranchKeyVersion(
      Types.GetBranchKeyVersionInput(
        branchKeyIdentifier := rotatedNativeRustBranchKey,
        branchKeyVersion := rotatedNativeRustBranchKeyOldVersion
      )
    );

    // check all three branch key materials have the same branch key id
    expect rotatedNativeRustBranchKey
      ==  versionActiveResult.branchKeyMaterials.branchKeyIdentifier 
      == versionActiveVersionResult.branchKeyMaterials.branchKeyIdentifier 
      == oldVersionResult.branchKeyMaterials.branchKeyIdentifier;

    // check that the branch key materials from the current active and its version are the same
    expect versionActiveResult.branchKeyMaterials.branchKey ==
      versionActiveVersionResult.branchKeyMaterials.branchKey;

    // check that branch key materials from the current active and the old version are NOT the same
    expect versionActiveResult.branchKeyMaterials.branchKey !=
      oldVersionResult.branchKeyMaterials.branchKey;

    // check that the version from the current active and its version are the same
    expect versionActiveResult.branchKeyMaterials.branchKeyVersion ==
      versionActiveVersionResult.branchKeyMaterials.branchKeyVersion;
    
    // check that the version from the current active and the old version are NOT the same
    expect versionActiveResult.branchKeyMaterials.branchKeyVersion !=
      versionActiveVersionResult.branchKeyMaterials.branchKeyVersion;
  }

  method {:test} TestGetCustomEncryptionContextBranchKeyFromNativeRustWrite() {
    var kmsConfig := Types.KMSConfiguration.kmsKeyArn(keyArn);

    var keyStoreConfig := Types.KeyStoreConfig(
      id := None,
      kmsConfiguration := kmsConfig,
      logicalKeyStoreName := logicalKeyStoreName,
      grantTokens := None,
      ddbTableName := branchKeyStoreName,
      ddbClient := None,
      kmsClient := None
    );

    var keyStore :- expect KeyStore.KeyStore(keyStoreConfig);

    var activeResult :- expect keyStore.GetActiveBranchKey(
      Types.GetActiveBranchKeyInput(
        branchKeyIdentifier := customECNativeRustBranchKey 
      ));
    
    var versionResult :- expect keyStore.GetBranchKeyVersion(
      Types.GetBranchKeyVersionInput(
        branchKeyIdentifier := customECNativeRustBranchKey,
        branchKeyVersion := customECNativeRustBranchKeyVersion
      )
    );

    // length checks  
    expect |versionResult.branchKeyMaterials.branchKey| == 32;
    expect |activeResult.branchKeyMaterials.branchKey| == 32;
    
    // check version on active materials is the same as the version
    // in the version materials
    expect activeResult.branchKeyMaterials.branchKeyVersion == 
      versionResult.branchKeyMaterials.branchKeyVersion;
    
    // check that the branch key material is the same on both
    expect activeResult.branchKeyMaterials.branchKey ==
      versionResult.branchKeyMaterials.branchKey;
    
    // check that the ec on the materials matches the one we expect
    var encryptionContext :- expect EncodeEncryptionContext(map[
                                                              "koda" := "is a dog"
                                                            ]);
    expect encryptionContext
      == activeResult.branchKeyMaterials.encryptionContext
      == versionResult.branchKeyMaterials.encryptionContext;
  }
}
