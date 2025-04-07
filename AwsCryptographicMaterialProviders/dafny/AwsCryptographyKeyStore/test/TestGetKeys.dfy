// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/Index.dfy"
include "Fixtures.dfy"
include "CleanupItems.dfy"
include "../src/ErrorMessages.dfy"
include "BranchKeyValidators.dfy"

module {:options "/functionSyntax:4" } TestGetKeys {
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
  import BranchKeyValidators

  const incorrectLogicalName := "MySuperAwesomeTableName"

  method {:test} TestGetKeysHappyCase()
  {
    var ddbClient :- expect DDB.DynamoDBClient();
    var keyStore :- expect DefaultKeyStore(kmsId := keyArn, physicalName := branchKeyStoreName, logicalName := logicalKeyStoreName, ddbClient? := Some(ddbClient));
    var storage :- expect DefaultStorage(ddbClient? := Some(ddbClient));
    BranchKeyValidators.VerifyGetKeys(branchKeyId, keyStore, storage, versionUtf8Bytes?:=Some(branchKeyIdActiveVersionUtf8Bytes));
  }

  method {:test} TestGetKeysHV2HappyCase()
  {
    var ddbClient :- expect DDB.DynamoDBClient();
    var keyStore :- expect DefaultKeyStore(kmsId := keyArn, physicalName := branchKeyStoreName, logicalName := logicalKeyStoreName, ddbClient? := Some(ddbClient));
    var storage :- expect DefaultStorage(ddbClient? := Some(ddbClient));
    BranchKeyValidators.VerifyGetKeys(hv2BranchKeyId, keyStore, storage, versionUtf8Bytes?:=Some(hv2BranchKeyIdActiveVersionUtf8Bytes));
  }

  method {:test} TestGetMRKeySameRegionHappyCase()
  {
    var ddbClient :- expect DDB.DynamoDBClient();
    var keyStore :- expect KeyStoreWithOptionalClient(
      kmsId := MrkArnWest,
      physicalName := branchKeyStoreName,
      logicalName := logicalKeyStoreName,
      ddbClient? := Some(ddbClient)
    );
    var storage :- expect DefaultStorage(ddbClient? := Some(ddbClient));
    BranchKeyValidators.VerifyGetKeys(WestBranchKey, keyStore, storage, versionUtf8Bytes?:=Some(WestBranchKeyBranchKeyIdActiveVersionUtf8Bytes));
  }

  method {:test} TestGetMRKeyReplicatedRegionHappyCase()
  {
    var ddbClient :- expect DDB.DynamoDBClient();
    // Creating the KMS client puts it in the default region;
    // for our CI, that is us-west-2.
    var kmsClient :- expect KMS.KMSClient();
    var keyStore :- expect KeyStoreWithOptionalClient(
      kmsId := MrkArnEast,
      ddbClient? := Some(ddbClient),
      kmsClient? := Some(kmsClient),
      mrkKey := true,
      srkKey := false
    );
    var storage :- expect DefaultStorage(ddbClient? := Some(ddbClient));
    BranchKeyValidators.VerifyGetKeys(EastBranchKey, keyStore, storage, versionUtf8Bytes?:=Some(EastBranchKeyBranchKeyIdActiveVersionUtf8Bytes));
  }

  method {:test} TestGetMRKeyMrkNotReplicatedFails()
  {
    var ddbClient :- expect DDB.DynamoDBClient();
    var keyStore :- expect KeyStoreWithOptionalClient(
      kmsId := MrkArnAP,
      ddbClient? := Some(ddbClient),
      // By not creating KMS Client, we use the Index's create KMS Client logic, which creates the KMS Client for the region in KMS ARN
      // in this case, that is AP-south-1, for which the MRK is NOT replicated, so this fails
      mrkKey := true,
      srkKey := false
    );
    GetActiveKeyWithIncorrectKmsKeyArnHelper(keyStore, EastBranchKey);
    GetBeaconKeyWithIncorrectKmsKeyArnHelper(keyStore, EastBranchKey);
    GetBranchKeyVersionWithIncorrectKmsKeyArnHelper(keyStore, EastBranchKey, EastBranchKeyIdActiveVersion);
  }

  method {:test} TestGetSRKeyButKmsArnOutOfRegionFails()
  {
    // Creating the KMS client puts it in the default region; for our CI, that is us-west-2.
    // The BK's KMS-ARN is not us-east-?;
    var kmsClient :- expect KMS.KMSClient();
    var ddbClient :- expect DDB.DynamoDBClient();
    var keyStore :- expect KeyStoreWithOptionalClient(
      kmsId := MrkArnWest,
      ddbClient? := Some(ddbClient),
      // By not creating KMS Client, we use the Index's create KMS Client logic, which creates the KMS Client for the region in KMS ARN
      // in this case, that is us-west-2, for which the MRK is NOT replicated, so this fails
      mrkKey := false,
      srkKey := true
    );
    GetActiveKeyWithIncorrectKmsKeyArnHelper(keyStore, EastBranchKey);
    GetBeaconKeyWithIncorrectKmsKeyArnHelper(keyStore, EastBranchKey);
    GetBranchKeyVersionWithIncorrectKmsKeyArnHelper(keyStore, EastBranchKey, EastBranchKeyIdActiveVersion);
  }

  method {:test} TestKeyWithIncorrectKmsKeyArn() {
    var keyStore :- expect DefaultKeyStore(kmsId := postalHornKeyArn, physicalName := branchKeyStoreName, logicalName := logicalKeyStoreName);
    GetActiveKeyWithIncorrectKmsKeyArnHelper(keyStore, branchKeyId);
    GetBeaconKeyWithIncorrectKmsKeyArnHelper(keyStore, branchKeyId);
    GetBranchKeyVersionWithIncorrectKmsKeyArnHelper(keyStore, branchKeyId, branchKeyIdActiveVersion);
  }

  method {:test} TestKeyWithIncorrectKmsKeyArnHV2() {
    var keyStore :- expect DefaultKeyStore(kmsId := postalHornKeyArn, physicalName := branchKeyStoreName, logicalName := logicalKeyStoreName);
    GetActiveKeyWithIncorrectKmsKeyArnHelper(keyStore, hv2BranchKeyId);
    GetBeaconKeyWithIncorrectKmsKeyArnHelper(keyStore, hv2BranchKeyId);
    GetBranchKeyVersionWithIncorrectKmsKeyArnHelper(keyStore, hv2BranchKeyId, hv2BranchKeyVersion);
  }

  method {:test} TestGetActiveKeyWrongLogicalKeyStoreName() {
    var keyStore :- expect DefaultKeyStore(kmsId:=keyArn, physicalName := branchKeyStoreName, logicalName := incorrectLogicalName);
    GetActiveKeyWrongLogicalKeyStoreName(keyStore, branchKeyId, Types.HierarchyVersion.v1);
    GetBeaconKeyWrongLogicalKeyStoreName(keyStore, branchKeyId, Types.HierarchyVersion.v1);
    GetVersionKeyWrongLogicalKeyStoreName(keyStore, branchKeyId, branchKeyIdActiveVersion, Types.HierarchyVersion.v1);
  }


  method {:test} TestGetActiveKeyWrongLogicalKeyStoreNameHV2() {
    var keyStore :- expect DefaultKeyStore(kmsId:=keyArn, physicalName := branchKeyStoreName, logicalName := incorrectLogicalName);
    GetActiveKeyWrongLogicalKeyStoreName(keyStore, hv2BranchKeyId, Types.HierarchyVersion.v2);
    GetBeaconKeyWrongLogicalKeyStoreName(keyStore, hv2BranchKeyId, Types.HierarchyVersion.v2);
    GetVersionKeyWrongLogicalKeyStoreName(keyStore, hv2BranchKeyId, hv2BranchKeyVersion, Types.HierarchyVersion.v2);
  }

  // This test does not consider HV b/c it is really testing the storage layer
  method {:test} TestGetKeyDoesNotExistFails()
  {
    var keyStore :- expect DefaultKeyStore(kmsId := keyArn, physicalName := branchKeyStoreName, logicalName := logicalKeyStoreName);
    GetActiveKeyDoesNotExistFailsHelper(keyStore, "Robbie");
    GetBeaconKeyDoesNotExistFailsHelper(keyStore, "Robbie");
    GetBranchKeyVersionDoesNotExistFailsHelper(keyStore, "Robbie", branchKeyIdActiveVersion);
  }

  method GetActiveKeyWrongLogicalKeyStoreName(keyStore: Types.IKeyStoreClient, branchKeyId: string, hv: Types.HierarchyVersion)
    requires keyStore.ValidState()
    modifies keyStore.Modifies
    ensures keyStore.ValidState()
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
    ensures keyStore.ValidState()
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
    ensures keyStore.ValidState()
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
    ensures keyStore.ValidState()
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
    ensures keyStore.ValidState()
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
    ensures keyStore.ValidState()
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
    ensures keyStore.ValidState()
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
    ensures keyStore.ValidState()
  {
    var versionResult := keyStore.GetBranchKeyVersion(
      Types.GetBranchKeyVersionInput(
        branchKeyIdentifier := branchKeyId,
        branchKeyVersion := branchKeyIdActiveVersion
      ));

    expect versionResult.Failure?;
    expect versionResult.error == Types.KeyStoreException(message := ErrorMessages.GET_KEY_ARN_DISAGREEMENT);
  }

  method testActiveBranchKeyKMSFailureCase(keyStore: Types.IKeyStoreClient, branchKeyId: string)
    requires keyStore.ValidState()
    modifies keyStore.Modifies
    ensures keyStore.ValidState()
  {
    var branchKeyResult := keyStore.GetActiveBranchKey(
      Types.GetActiveBranchKeyInput(
        branchKeyIdentifier := branchKeyId
      ));
    expect branchKeyResult.Failure?;
    expect branchKeyResult.error.ComAmazonawsKms?;
    expect branchKeyResult.error.ComAmazonawsKms.OpaqueWithText?;
  }

  method testBranchKeyVersionKMSFailureCase(keyStore: Types.IKeyStoreClient, branchKeyId: string, branchKeyIdActiveVersion: string)
    requires keyStore.ValidState()
    modifies keyStore.Modifies
    ensures keyStore.ValidState()
  {
    var versionResult := keyStore.GetBranchKeyVersion(
      Types.GetBranchKeyVersionInput(
        branchKeyIdentifier := branchKeyId,
        branchKeyVersion := branchKeyIdActiveVersion
      ));
    expect versionResult.Failure?;
    expect versionResult.error.ComAmazonawsKms?;
    expect versionResult.error.ComAmazonawsKms.OpaqueWithText?;
  }

  method testBeaconKeyKMSFailureCase(keyStore: Types.IKeyStoreClient, branchKeyId: string)
    requires keyStore.ValidState()
    modifies keyStore.Modifies
  {
    var beaconKeyResult := keyStore.GetBeaconKey(
      Types.GetBeaconKeyInput(
        branchKeyIdentifier := branchKeyId
      ));
    expect beaconKeyResult.Failure?;
    expect beaconKeyResult.error.ComAmazonawsKms?;
    expect beaconKeyResult.error.ComAmazonawsKms.OpaqueWithText?;
  }
}
