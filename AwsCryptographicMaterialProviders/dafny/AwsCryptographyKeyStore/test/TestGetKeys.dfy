// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/Index.dfy"
include "Fixtures.dfy"
include "CleanupItems.dfy"
include "../src/ErrorMessages.dfy"

// TODO-HV2-M1: add more HV2 tests.
// TODO-HV2-M1: Maybe rename this module to TestGetHv1Keys and create another TestGetHv2Keys
module TestGetKeys {
  import Types = AwsCryptographyKeyStoreTypes
  import ComAmazonawsKmsTypes
  import KMS = Com.Amazonaws.Kms
  import DDB = Com.Amazonaws.Dynamodb
  import KeyStore
  import ComAmazonawsDynamodbTypes
  import opened Wrappers
  import opened Fixtures
  import opened StandardLibrary.UInt
  import UTF8
  import ErrorMessages = KeyStoreErrorMessages
  import UUID

  const incorrectLogicalName := "MySuperAwesomeTableName"

  method VerifyGetKeys(
    identifier : string,
    keyStore : Types.IKeyStoreClient,
    storage : Types.IKeyStorageInterface
  )
    requires
      keyStore.ValidState() && storage.ValidState()
    modifies
      keyStore.Modifies, storage.Modifies
    ensures
      keyStore.ValidState() && storage.ValidState()

  {
    testBeaconKeyHappyCase(keyStore, identifier);

    var activeResult := testAndGetActiveBranchKeyHappyCase(keyStore, identifier);
    var branchKeyVersion :- expect UTF8.Decode(activeResult.branchKeyMaterials.branchKeyVersion);

    testBranchKeyVersionHappyCase(keyStore, identifier, branchKeyVersion, activeResult.branchKeyMaterials.branchKeyVersion);
    VerifyGetKeysFromStorage(identifier, storage);
    
    //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-and-beacon-key-creation
    //= type=test
    //# This guid MUST be [version 4 UUID](https://www.ietf.org/rfc/rfc4122.txt)
    var versionString :- expect UTF8.Decode(activeResult.branchKeyMaterials.branchKeyVersion);
    var versionByteUUID :- expect UUID.ToByteArray(versionString);
    var versionRoundTrip :- expect UUID.FromByteArray(versionByteUUID);
    expect versionRoundTrip == versionString;
  }

  method {:test} TestGetKeysHappyCase()
  {
    var kmsClient :- expect KMS.KMSClient();
    var ddbClient :- expect DDB.DynamoDBClient();
    var kmsConfig := Types.KMSConfiguration.kmsKeyArn(keyArn);

    var keyStore :- expect DefaultKeyStore(kmsId := keyArn, physicalName := branchKeyStoreName, logicalName := logicalKeyStoreName, ddbClient? := Some(ddbClient), kmsClient? := Some(kmsClient));

    testBeaconKeyHappyCase(keyStore, branchKeyId);
    testBeaconKeyHappyCase(keyStore, hv2BranchKeyId);

    testActiveBranchKeyHappyCase(keyStore, branchKeyId, branchKeyIdActiveVersionUtf8Bytes);
    testActiveBranchKeyHappyCase(keyStore, hv2BranchKeyId, hv2BranchKeyIdActiveVersionUtf8Bytes);

    testBranchKeyVersionHappyCase(keyStore, branchKeyId, branchKeyIdActiveVersion, branchKeyIdActiveVersionUtf8Bytes);
    testBranchKeyVersionHappyCase(keyStore, hv2BranchKeyId, hv2BranchKeyVersion, hv2BranchKeyIdActiveVersionUtf8Bytes);
  }

  // TODO-HV2-M1: Add MRK test for hv2
  method {:test} {:isolate_assertions} TestGetActiveMrkKey()
  {
    var ddbClient :- expect DDB.DynamoDBClient();

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

  method {:test} TestKeyWithIncorrectKmsKeyArn() {
    var kmsClient :- expect KMS.KMSClient();
    var ddbClient :- expect DDB.DynamoDBClient();

    var keyStore :- expect DefaultKeyStore(kmsId := postalHornKeyArn, physicalName := branchKeyStoreName, logicalName := logicalKeyStoreName, ddbClient? := Some(ddbClient), kmsClient? := Some(kmsClient));

    GetActiveKeyWithIncorrectKmsKeyArnHelper(keyStore, branchKeyId);
    GetActiveKeyWithIncorrectKmsKeyArnHelper(keyStore, hv2BranchKeyId);

    GetBeaconKeyWithIncorrectKmsKeyArnHelper(keyStore, branchKeyId);
    GetBeaconKeyWithIncorrectKmsKeyArnHelper(keyStore, hv2BranchKeyId);

    GetBranchKeyVersionWithIncorrectKmsKeyArnHelper(keyStore, branchKeyId, branchKeyIdActiveVersion);
    GetBranchKeyVersionWithIncorrectKmsKeyArnHelper(keyStore, hv2BranchKeyId, hv2BranchKeyVersion);
  }

  method {:test} TestGetActiveKeyWrongLogicalKeyStoreName() {
    var kmsClient :- expect KMS.KMSClient();
    var ddbClient :- expect DDB.DynamoDBClient();

    var keyStore :- expect DefaultKeyStore(kmsId:=keyArn, physicalName := branchKeyStoreName, logicalName := incorrectLogicalName, ddbClient? := Some(ddbClient), kmsClient? := Some(kmsClient));
    GetActiveKeyWrongLogicalKeyStoreName(keyStore, branchKeyId, Types.HierarchyVersion.v1);
    GetActiveKeyWrongLogicalKeyStoreName(keyStore, hv2BranchKeyId, Types.HierarchyVersion.v2);

    GetBeaconKeyWrongLogicalKeyStoreName(keyStore, branchKeyId, Types.HierarchyVersion.v1);
    GetBeaconKeyWrongLogicalKeyStoreName(keyStore, hv2BranchKeyId, Types.HierarchyVersion.v2);

    GetVersionKeyWrongLogicalKeyStoreName(keyStore, branchKeyId, branchKeyIdActiveVersion, Types.HierarchyVersion.v1);
    GetVersionKeyWrongLogicalKeyStoreName(keyStore, hv2BranchKeyId, hv2BranchKeyVersion, Types.HierarchyVersion.v2);
  }

  method {:test} TestGetKeyDoesNotExistFails()
  {
    var kmsClient :- expect KMS.KMSClient();
    var ddbClient :- expect DDB.DynamoDBClient();

    var keyStore :- expect DefaultKeyStore(kmsId := keyArn, physicalName := branchKeyStoreName, logicalName := logicalKeyStoreName, ddbClient? := Some(ddbClient), kmsClient? := Some(kmsClient));
    GetActiveKeyDoesNotExistFailsHelper(keyStore, "Robbie");
    GetBeaconKeyDoesNotExistFailsHelper(keyStore, "Robbie");
    GetBranchKeyVersionDoesNotExistFailsHelper(keyStore, "Robbie", branchKeyIdActiveVersion);
  }

  method {:test} TestGetKeysWithNoClients() {
    var kmsConfig := Types.KMSConfiguration.kmsKeyArn(keyArn);

    var keyStore :- expect KeyStoreWithNoClient(kmsId:=keyArn, physicalName:=branchKeyStoreName, logicalName := logicalKeyStoreName);

    testActiveBranchKeyHappyCase(keyStore, branchKeyId, branchKeyIdActiveVersionUtf8Bytes);
    testActiveBranchKeyHappyCase(keyStore, hv2BranchKeyId, hv2BranchKeyIdActiveVersionUtf8Bytes);

    testBeaconKeyHappyCase(keyStore, branchKeyId);
    testBeaconKeyHappyCase(keyStore, hv2BranchKeyId);

    testBranchKeyVersionHappyCase(keyStore, branchKeyId, branchKeyIdActiveVersion, branchKeyIdActiveVersionUtf8Bytes);
    testBranchKeyVersionHappyCase(keyStore, hv2BranchKeyId, hv2BranchKeyVersion, hv2BranchKeyIdActiveVersionUtf8Bytes);
  }

  method GetActiveKeyWrongLogicalKeyStoreName(keyStore: Types.IKeyStoreClient, branchKeyId: string, hv: Types.HierarchyVersion)
    requires keyStore.ValidState()
    modifies keyStore.Modifies
  {
    var activeResult := keyStore.GetActiveBranchKey(
      Types.GetActiveBranchKeyInput(
        branchKeyIdentifier := branchKeyId
      ));
    expect activeResult.Failure?;
    match hv {
      case v1 =>
        match activeResult.error {
          case ComAmazonawsKms(nestedError) =>
            expect nestedError.InvalidCiphertextException?;
          case _ => expect false, "Wrong Logical Keystore Name SHOULD Fail with KMS InvalidCiphertextException for HV-1.";
        }
      case v2 => expect activeResult.error == Types.Error.BranchKeyCiphertextException(message := ErrorMessages.MD_DIGEST_SHA_NOT_MATCHED), "Wrong Logical Keystore Name SHOULD Fail with BranchKeyCiphertextException for HV-2.";
    }
  }

  method GetBeaconKeyWrongLogicalKeyStoreName(keyStore: Types.IKeyStoreClient, branchKeyId: string, hv: Types.HierarchyVersion)
    requires keyStore.ValidState()
    modifies keyStore.Modifies
  {
    var beaconKeyResult := keyStore.GetBeaconKey(
      Types.GetBeaconKeyInput(
        branchKeyIdentifier := branchKeyId
      ));
    expect beaconKeyResult.Failure?;
    match hv {
      case v1 =>
        match beaconKeyResult.error {
          case ComAmazonawsKms(nestedError) =>
            expect nestedError.InvalidCiphertextException?;
          case _ => expect false, "Wrong Logical Keystore Name SHOULD Fail with KMS InvalidCiphertextException for HV-1.";
        }
      case v2 => expect beaconKeyResult.error == Types.Error.BranchKeyCiphertextException(message := ErrorMessages.MD_DIGEST_SHA_NOT_MATCHED), "Wrong Logical Keystore Name SHOULD Fail with BranchKeyCiphertextException for HV-2.";
    }
  }

  method GetVersionKeyWrongLogicalKeyStoreName(keyStore: Types.IKeyStoreClient, branchKeyId: string, branchKeyIdActiveVersion: string, hv: Types.HierarchyVersion)
    requires keyStore.ValidState()
    modifies keyStore.Modifies
  {
    var versionResult := keyStore.GetBranchKeyVersion(
      Types.GetBranchKeyVersionInput(
        branchKeyIdentifier := branchKeyId,
        branchKeyVersion := branchKeyIdActiveVersion
      ));
    expect versionResult.Failure?;
    match hv {
      case v1 =>
        match versionResult.error {
          case ComAmazonawsKms(nestedError) =>
            expect nestedError.InvalidCiphertextException?;
          case _ => expect false, "Wrong Logical Keystore Name SHOULD Fail with KMS InvalidCiphertextException for HV-1.";
        }
      case v2 => expect versionResult.error == Types.Error.BranchKeyCiphertextException(message := ErrorMessages.MD_DIGEST_SHA_NOT_MATCHED), "Wrong Logical Keystore Name SHOULD Fail with BranchKeyCiphertextException for HV-2.";
    }
  }

  method GetActiveKeyDoesNotExistFailsHelper(keyStore: Types.IKeyStoreClient, branchKeyId: string)
    requires keyStore.ValidState()
    modifies keyStore.Modifies
  {
    var activeResult := keyStore.GetActiveBranchKey(
      Types.GetActiveBranchKeyInput(
        branchKeyIdentifier := branchKeyId
      ));
    expect activeResult.Failure?;
    expect activeResult.error == Types.KeyStoreException(message := ErrorMessages.NO_CORRESPONDING_BRANCH_KEY);
  }

  method GetBeaconKeyDoesNotExistFailsHelper(keyStore: Types.IKeyStoreClient, branchKeyId: string)
    requires keyStore.ValidState()
    modifies keyStore.Modifies
  {
    var beaconKeyResult := keyStore.GetBeaconKey(
      Types.GetBeaconKeyInput(
        branchKeyIdentifier := branchKeyId
      ));
    expect beaconKeyResult.Failure?;
    expect beaconKeyResult.error == Types.KeyStoreException(message := ErrorMessages.NO_CORRESPONDING_BRANCH_KEY);
  }

  method GetBranchKeyVersionDoesNotExistFailsHelper(keyStore: Types.IKeyStoreClient, branchKeyId: string, branchKeyIdActiveVersion: string)
    requires keyStore.ValidState()
    modifies keyStore.Modifies
  {
    var versionResult := keyStore.GetBranchKeyVersion(
      Types.GetBranchKeyVersionInput(
        branchKeyIdentifier := branchKeyId,
        branchKeyVersion := branchKeyIdActiveVersion
      ));
    expect versionResult.Failure?;
    expect versionResult.error == Types.KeyStoreException(message := ErrorMessages.NO_CORRESPONDING_BRANCH_KEY);
  }

  method GetActiveKeyWithIncorrectKmsKeyArnHelper(keyStore: Types.IKeyStoreClient, branchKeyId: string)
    requires keyStore.ValidState()
    modifies keyStore.Modifies
  {
    var activeResult := keyStore.GetActiveBranchKey(
      Types.GetActiveBranchKeyInput(
        branchKeyIdentifier := branchKeyId
      ));
    expect activeResult.Failure?;
    expect activeResult.error == Types.KeyStoreException(message := ErrorMessages.GET_KEY_ARN_DISAGREEMENT);
  }

  method GetBeaconKeyWithIncorrectKmsKeyArnHelper(keyStore: Types.IKeyStoreClient, branchKeyId: string)
    requires keyStore.ValidState()
    modifies keyStore.Modifies
  {
    var beaconKeyResult := keyStore.GetBeaconKey(
      Types.GetBeaconKeyInput(
        branchKeyIdentifier := branchKeyId
      ));

    expect beaconKeyResult.Failure?;
    expect beaconKeyResult.error == Types.KeyStoreException(message := ErrorMessages.GET_KEY_ARN_DISAGREEMENT);
  }

  method GetBranchKeyVersionWithIncorrectKmsKeyArnHelper(keyStore: Types.IKeyStoreClient, branchKeyId: string, branchKeyIdActiveVersion: string)
    requires keyStore.ValidState()
    modifies keyStore.Modifies
  {
    var versionResult := keyStore.GetBranchKeyVersion(
      Types.GetBranchKeyVersionInput(
        branchKeyIdentifier := branchKeyId,
        branchKeyVersion := branchKeyIdActiveVersion
      ));

    expect versionResult.Failure?;
    expect versionResult.error == Types.KeyStoreException(message := ErrorMessages.GET_KEY_ARN_DISAGREEMENT);
  }

  method testBeaconKeyHappyCase(keyStore: Types.IKeyStoreClient, branchKeyId: string)
    requires keyStore.ValidState()
    modifies keyStore.Modifies
  {
    var beaconKeyResult :- expect keyStore.GetBeaconKey(
      Types.GetBeaconKeyInput(
        branchKeyIdentifier := branchKeyId
      ));
    expect isValidBeaconResult?(beaconKeyResult, branchKeyId);
  }

  predicate method isValidBeaconResult?(beaconKeyResult: Types.GetBeaconKeyOutput, branchKeyId: string) {
    && beaconKeyResult.beaconKeyMaterials.beaconKeyIdentifier == branchKeyId
    && beaconKeyResult.beaconKeyMaterials.beaconKey.Some?
    && |beaconKeyResult.beaconKeyMaterials.beaconKey.value| == 32
  }

  method testActiveBranchKeyHappyCase(keyStore: Types.IKeyStoreClient, branchKeyId: string, branchKeyIdActiveVersionUtf8Bytes: seq<uint8>)
    requires keyStore.ValidState()
    modifies keyStore.Modifies
  {
    var branchKeyResult :- expect keyStore.GetActiveBranchKey(
      Types.GetActiveBranchKeyInput(
        branchKeyIdentifier := branchKeyId
      ));
    expect isValidActiveBranchKeyResult?(branchKeyResult, branchKeyId, Some(branchKeyIdActiveVersionUtf8Bytes));
  }

  method testAndGetActiveBranchKeyHappyCase(keyStore: Types.IKeyStoreClient, branchKeyId: string, nameonly branchKeyIdActiveVersionUtf8Bytes: Option<seq<uint8>> := None)
    returns (output: Types.GetActiveBranchKeyOutput)
    requires keyStore.ValidState()
    modifies keyStore.Modifies
  {
    var branchKeyResult :- expect keyStore.GetActiveBranchKey(
      Types.GetActiveBranchKeyInput(
        branchKeyIdentifier := branchKeyId
      ));
    expect isValidActiveBranchKeyResult?(branchKeyResult, branchKeyId, branchKeyIdActiveVersionUtf8Bytes);
    return branchKeyResult;
  }

  predicate method isValidActiveBranchKeyResult?(branchKeyResult: Types.GetActiveBranchKeyOutput, branchKeyId: string, branchKeyIdActiveVersionUtf8Bytes: Option<seq<uint8>>) {
    && branchKeyResult.branchKeyMaterials.branchKeyIdentifier == branchKeyId
    && (branchKeyIdActiveVersionUtf8Bytes.None? || 
        branchKeyResult.branchKeyMaterials.branchKeyVersion == branchKeyIdActiveVersionUtf8Bytes.value)
    && |branchKeyResult.branchKeyMaterials.branchKey| == 32
  }

  method testBranchKeyVersionHappyCase(keyStore: Types.IKeyStoreClient, branchKeyId: string, branchKeyIdActiveVersion: string, branchKeyIdActiveVersionUtf8Bytes: seq<uint8>)
    requires keyStore.ValidState()
    modifies keyStore.Modifies
  {
    var versionResult :- expect keyStore.GetBranchKeyVersion(
      Types.GetBranchKeyVersionInput(
        branchKeyIdentifier := branchKeyId,
        branchKeyVersion := branchKeyIdActiveVersion
      ));
    var testBytes :- expect UTF8.Encode(branchKeyIdActiveVersion);
    expect isValidBranchKeyVersionResult?(versionResult, branchKeyId, branchKeyIdActiveVersionUtf8Bytes, testBytes);
  }

  predicate method isValidBranchKeyVersionResult?(versionResult: Types.GetBranchKeyVersionOutput, branchKeyId: string, branchKeyIdActiveVersionUtf8Bytes: seq<uint8>, testBytes: UTF8.ValidUTF8Bytes) {
    && versionResult.branchKeyMaterials.branchKeyIdentifier == branchKeyId
    && versionResult.branchKeyMaterials.branchKeyVersion == branchKeyIdActiveVersionUtf8Bytes == testBytes
    && |versionResult.branchKeyMaterials.branchKey| == 32
  }

  method VerifyGetKeysFromStorage(
    identifier : string,
    storage : Types.IKeyStorageInterface
  )
    requires storage.ValidState()
    modifies storage.Modifies
    ensures storage.ValidState()
  {
    var encryptedActiveFromStorage :- expect storage.GetEncryptedActiveBranchKey(
      Types.GetEncryptedActiveBranchKeyInput(
        Identifier := identifier
      )
    );

    var encryptedBeaconFromStorage :- expect storage.GetEncryptedBeaconKey(
      Types.GetEncryptedBeaconKeyInput(
        Identifier := identifier
      )
    );

    expect encryptedActiveFromStorage.Item.Type.ActiveHierarchicalSymmetricVersion?;

    var encryptedVersionFromStorage :- expect storage.GetEncryptedBranchKeyVersion(
      Types.GetEncryptedBranchKeyVersionInput(
        Identifier := identifier,
        Version := encryptedActiveFromStorage.Item.Type.ActiveHierarchicalSymmetricVersion.Version
      )
    );

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#branch-key-and-beacon-key-creation
    //= type=test
    //# This timestamp MUST be in ISO 8601 format in UTC, to microsecond precision (e.g. “YYYY-MM-DDTHH:mm:ss.ssssssZ“)
    expect ISO8601?(encryptedActiveFromStorage.Item.CreateTime);
    expect ISO8601?(encryptedBeaconFromStorage.Item.CreateTime);
    expect ISO8601?(encryptedVersionFromStorage.Item.CreateTime);
  }

  lemma ISO8601Test()
  {
    assert ISO8601?("2024-08-06T17:23:25.000874Z");
  }

  predicate method ISO8601?(
    CreateTime: string
  )
  {
    // “YYYY-MM-DDTHH:mm:ss.ssssssZ“
    && |CreateTime| == 27
    && CreateTime[4] == '-'
    && CreateTime[7] == '-'
    && CreateTime[10] == 'T'
    && CreateTime[13] == ':'
    && CreateTime[16] == ':'
    && CreateTime[19] == '.'
    && CreateTime[26] == 'Z'
  }
}
