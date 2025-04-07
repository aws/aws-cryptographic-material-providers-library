// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/Index.dfy"
include "Fixtures.dfy"
include "CleanupItems.dfy"
include "../src/ErrorMessages.dfy"
include "BranchKeyValidators.dfy"

// TODO-HV2-M1: add more HV2 tests.
// TODO-HV2-M1: Maybe rename this module to TestGetHv1Keys and create another TestGetHv2Keys
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
    var kmsClient :- expect KMS.KMSClient();
    var ddbClient :- expect DDB.DynamoDBClient();
    var keyStore :- expect DefaultKeyStore(kmsId := keyArn, physicalName := branchKeyStoreName, logicalName := logicalKeyStoreName, ddbClient? := Some(ddbClient), kmsClient? := Some(kmsClient));
    var storage :- expect DefaultStorage(ddbClient? := Some(ddbClient));
    BranchKeyValidators.VerifyGetKeys(branchKeyId, keyStore, storage, versionUtf8Bytes?:=Some(branchKeyIdActiveVersionUtf8Bytes));
  }

  method {:test} TestGetKeysHV2HappyCase()
  {
    var kmsClient :- expect KMS.KMSClient();
    var ddbClient :- expect DDB.DynamoDBClient();
    var keyStore :- expect DefaultKeyStore(kmsId := keyArn, physicalName := branchKeyStoreName, logicalName := logicalKeyStoreName, ddbClient? := Some(ddbClient), kmsClient? := Some(kmsClient));
    var storage :- expect DefaultStorage(ddbClient? := Some(ddbClient));
    BranchKeyValidators.VerifyGetKeys(hv2BranchKeyId, keyStore, storage, versionUtf8Bytes?:=Some(hv2BranchKeyIdActiveVersionUtf8Bytes));
  }

  method {:test} TestKeyWithIncorrectKmsKeyArn() {
    var kmsClient :- expect KMS.KMSClient();
    var ddbClient :- expect DDB.DynamoDBClient();
    var keyStore :- expect DefaultKeyStore(kmsId := postalHornKeyArn, physicalName := branchKeyStoreName, logicalName := logicalKeyStoreName, ddbClient? := Some(ddbClient), kmsClient? := Some(kmsClient));
    GetActiveKeyWithIncorrectKmsKeyArnHelper(keyStore, branchKeyId);
    GetBeaconKeyWithIncorrectKmsKeyArnHelper(keyStore, branchKeyId);
    GetBranchKeyVersionWithIncorrectKmsKeyArnHelper(keyStore, branchKeyId, branchKeyIdActiveVersion);
  }

  method {:test} TestKeyWithIncorrectKmsKeyArnHV2() {
    var kmsClient :- expect KMS.KMSClient();
    var ddbClient :- expect DDB.DynamoDBClient();
    var keyStore :- expect DefaultKeyStore(kmsId := postalHornKeyArn, physicalName := branchKeyStoreName, logicalName := logicalKeyStoreName, ddbClient? := Some(ddbClient), kmsClient? := Some(kmsClient));
    GetActiveKeyWithIncorrectKmsKeyArnHelper(keyStore, hv2BranchKeyId);
    GetBeaconKeyWithIncorrectKmsKeyArnHelper(keyStore, hv2BranchKeyId);
    GetBranchKeyVersionWithIncorrectKmsKeyArnHelper(keyStore, hv2BranchKeyId, hv2BranchKeyVersion);
  }

  method {:test} TestGetActiveKeyWrongLogicalKeyStoreName() {
    var kmsClient :- expect KMS.KMSClient();
    var ddbClient :- expect DDB.DynamoDBClient();
    var keyStore :- expect DefaultKeyStore(kmsId:=keyArn, physicalName := branchKeyStoreName, logicalName := incorrectLogicalName, ddbClient? := Some(ddbClient), kmsClient? := Some(kmsClient));
    GetActiveKeyWrongLogicalKeyStoreName(keyStore, branchKeyId, Types.HierarchyVersion.v1);
    GetBeaconKeyWrongLogicalKeyStoreName(keyStore, branchKeyId, Types.HierarchyVersion.v1);
    GetVersionKeyWrongLogicalKeyStoreName(keyStore, branchKeyId, branchKeyIdActiveVersion, Types.HierarchyVersion.v1);
  }


  method {:test} TestGetActiveKeyWrongLogicalKeyStoreNameHV2() {
    var kmsClient :- expect KMS.KMSClient();
    var ddbClient :- expect DDB.DynamoDBClient();
    var keyStore :- expect DefaultKeyStore(kmsId:=keyArn, physicalName := branchKeyStoreName, logicalName := incorrectLogicalName, ddbClient? := Some(ddbClient), kmsClient? := Some(kmsClient));
    GetActiveKeyWrongLogicalKeyStoreName(keyStore, hv2BranchKeyId, Types.HierarchyVersion.v2);
    GetBeaconKeyWrongLogicalKeyStoreName(keyStore, hv2BranchKeyId, Types.HierarchyVersion.v2);
    GetVersionKeyWrongLogicalKeyStoreName(keyStore, hv2BranchKeyId, hv2BranchKeyVersion, Types.HierarchyVersion.v2);
  }

  // These tests do not consider HV
  method {:test} TestGetKeyDoesNotExistFails()
  {
    var kmsClient :- expect KMS.KMSClient();
    var ddbClient :- expect DDB.DynamoDBClient();
    var keyStore :- expect DefaultKeyStore(kmsId := keyArn, physicalName := branchKeyStoreName, logicalName := logicalKeyStoreName, ddbClient? := Some(ddbClient), kmsClient? := Some(kmsClient));
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
