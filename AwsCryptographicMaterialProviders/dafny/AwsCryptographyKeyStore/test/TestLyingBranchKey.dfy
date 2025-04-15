// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/Index.dfy"
include "Fixtures.dfy"

// These tests assert that a particular form of
// illegal Branch Key is always correctly handled.
// Creation of this particular illegal Branch Key is detailed here:
// `git rev-parse --show-toplevel`/cfn/lyingBranchKeyCreation.md
module TestLyingBranchKey {
  import Types = AwsCryptographyKeyStoreTypes
  import KMS = Com.Amazonaws.Kms
  import DDB = Com.Amazonaws.Dynamodb
  import ComAmazonawsKmsTypes
  import KeyStore
  import opened Wrappers
  import opened Fixtures
  import UTF8
  import ErrorMessages = KeyStoreErrorMessages

  // The Branch Key's Item says it is protected by KMS-ARN Fixtures.dfy#postalHornKeyArn,
  // but the KMS requests were actually executed against KMS-ARN Fixtures.dfy#keyArn.
  // Thus, all Keystore Operations related to the Branch Key MUST fail with exceptions from KMS.
  method {:test} TestHv1GetKeysForLyingBranchKey() {
    var keyStore :- expect DefaultKeyStore(kmsId := postalHornKeyArn);

    GetKeysForLyingBranchKeyExpectsIncorrectKeyException(
      id := hierarchyV1InvalidKmsArnId,
      version := hierarchyV1InvalidKmsArnVersion,
      keyStore := keyStore
    );
  }

  // The Branch Key's Item says it is protected by KMS-ARN Fixtures.dfy#postalHornKeyArn,
  // but the KMS requests were actually executed against KMS-ARN Fixtures.dfy#keyArn.
  // Thus, all Keystore Operations related to the Branch Key MUST fail with exceptions from KMS.
  method {:test} TestHv2GetKeysForLyingBranchKey() {
    var keyStore :- expect DefaultKeyStore(kmsId := postalHornKeyArn);

    TestBranchKeyExpectsException(
      id := hierarchyV2InvalidKmsArnId,
      version := hierarchyV2InvalidKmsArnVersion,
      expectedError := ComAmazonawsKmsTypes.Error.IncorrectKeyException,
      keyStore := keyStore
    );
  }

  method {:isolate_assertions} TestBranchKeyExpectsException(
    id: string,
    version : string,
    expectedError : ComAmazonawsKmsTypes.Error,
    keyStore: Types.IKeyStoreClient
  )
    requires keyStore.ValidState()
    modifies keyStore.Modifies
    ensures keyStore.ValidState()
  {
    var activeOutput? := keyStore.GetActiveBranchKey(
      Types.GetActiveBranchKeyInput(
        branchKeyIdentifier := id
      ));
    expect activeOutput?.Failure?;
    expect activeOutput.Error == Types.Error.ComAmazonawsKms(expectedError);
    match activeOutput?.error {
      case ComAmazonawsKms(nestedError) =>
        expect nestedError.IncorrectKeyException?;
      case _ => expect false, "Lying Branch Key SHOULD Fail with KMS IncorrectKeyException.";
    }

    var versionOutput? := keyStore.GetBranchKeyVersion(
      Types.GetBranchKeyVersionInput(
        branchKeyIdentifier := id,
        branchKeyVersion := version
      ));
    expect versionOutput?.Failure?;
    match versionOutput?.error {
      case ComAmazonawsKms(nestedError) =>
        expect nestedError.IncorrectKeyException?;
      case _ => expect false, "Lying Branch Key SHOULD Fail with KMS IncorrectKeyException.";
    }

    var beaconOutput? := keyStore.GetBeaconKey(
      Types.GetBeaconKeyInput(
        branchKeyIdentifier := id
      ));
    expect beaconOutput?.Failure?;
    match beaconOutput?.error {
      case ComAmazonawsKms(nestedError) =>
        expect nestedError.IncorrectKeyException?;
      case _ => expect false, "Lying Branch Key SHOULD Fail with KMS IncorrectKeyException.";
    }
  }

  // The Branch Key's Item says it has encryption context "TamperedKey:TamperedValue",
  // but the KMS Requests were actually executed with encryption context "ExampleContextKey:ExampleContextValue".
  // Thus, all Keystore Operations related to the Branch Key MUST fail with KMS.InvalidCiphertextException.
  method {:test} TestHV2GetKeyWrongDigest() {
    var ddbClient :- expect ProvideDDBClient();
    var kmsClient :- expect ProvideKMSClient();
    var keyStore :- expect DefaultKeyStore(ddbClient?:=Some(ddbClient), kmsClient?:=Some(kmsClient));

    GetKeysForLyingBranchKeyExpectsInvalidCiphertextException(
      id := hierarchyV2InvalidDigestId,
      version := hierarchyV2InvalidDigestVersion,
      keyStore := keyStore
    );
  }

  // The Branch Key's Item contains ciphertext with incorrect length compared to the actual encrypted data.
  // Thus, all Keystore Operations related to the Branch Key MUST fail with KMS.InvalidCiphertextException.
  method {:test} TestHV2GetKeyWrongCiphertextLength() {
    var ddbClient :- expect ProvideDDBClient();
    var kmsClient :- expect ProvideKMSClient();
    var keyStore :- expect DefaultKeyStore(ddbClient?:=Some(ddbClient), kmsClient?:=Some(kmsClient));

    GetKeysForLyingBranchKeyExpectsInvalidCiphertextException(
      id := hierarchyV2InvalidCiphertextLengthId,
      version := hierarchyV2InvalidCiphertextLengthVersion,
      keyStore := keyStore
    );
  }


  method {:isolate_assertions} GetKeysForLyingBranchKeyExpectsInvalidCiphertextException(
    id: string,
    version : string,
    keyStore: Types.IKeyStoreClient
  )
    requires keyStore.ValidState()
    modifies keyStore.Modifies
    ensures keyStore.ValidState()
  {
    var activeOutput? := keyStore.GetActiveBranchKey(
      Types.GetActiveBranchKeyInput(
        branchKeyIdentifier := id
      ));
    expect activeOutput?.Failure?;
    match activeOutput?.error {
      case ComAmazonawsKms(nestedError) =>
        expect nestedError.InvalidCiphertextException?;
      case _ => expect false, "Lying Branch Key SHOULD Fail with KMS InvalidCiphertextException.";
    }

    var versionOutput? := keyStore.GetBranchKeyVersion(
      Types.GetBranchKeyVersionInput(
        branchKeyIdentifier := id,
        branchKeyVersion := version
      ));
    expect versionOutput?.Failure?;
    match versionOutput?.error {
      case ComAmazonawsKms(nestedError) =>
        expect nestedError.InvalidCiphertextException?;
      case _ => expect false, "Lying Branch Key SHOULD Fail with KMS InvalidCiphertextException.";
    }

    var beaconOutput? := keyStore.GetBeaconKey(
      Types.GetBeaconKeyInput(
        branchKeyIdentifier := id
      ));
    expect beaconOutput?.Failure?;
    match beaconOutput?.error {
      case ComAmazonawsKms(nestedError) =>
        expect nestedError.InvalidCiphertextException?;
      case _ => expect false, "Lying Branch Key SHOULD Fail with KMS InvalidCiphertextException.";
    }
  }
}
