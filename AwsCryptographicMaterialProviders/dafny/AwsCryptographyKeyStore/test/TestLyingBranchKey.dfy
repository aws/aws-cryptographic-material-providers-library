// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/Index.dfy"
include "Fixtures.dfy"

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

  // Define the subset of KMS errors we care about
  type KmsTestError = e: ComAmazonawsKmsTypes.Error | (
        || e.IncorrectKeyException?
        || e.InvalidCiphertextException?
      ) witness *

  // Helper method to verify if an error matches the expected KMS error type
  method VerifyKMSError(
    actual: Types.Error,
    expected: KmsTestError
  ) {
    match actual {
      case ComAmazonawsKms(nestedError) =>
        match nestedError {
          case IncorrectKeyException(_) =>
            expect expected.IncorrectKeyException?;
          case InvalidCiphertextException(_) =>
            expect expected.InvalidCiphertextException?;
          case _ =>
            expect false, "Unexpected KMS error type";
        }
      case _ =>
        expect false, "Expected KMS error but got different error type";
    }
  }

  // These tests assert that a particular form of
  // illegal Branch Key is always correctly handled.
  // Creation of this particular illegal Branch Key `hierarchyV1InvalidKmsArnId` is detailed here:
  // `git rev-parse --show-toplevel`/cfn/lyingBranchKeyCreation.md
  // Test Case: KMS ARN Mismatch
  // The Branch Key's Item says it is protected by KMS-ARN Fixtures.dfy#postalHornKeyArn,
  // but the KMS requests were actually executed against KMS-ARN Fixtures.dfy#keyArn.
  // Thus, all Keystore Operations related to the Branch Key MUST fail with exceptions from KMS.
  // The branch key claims to be protected by KMS Arn (postalHornKeyArn)
  // but was actually encrypted using a different KMS key (keyArn)
  // Expected: KMS IncorrectKeyException
  method {:test} TestHv1GetKeysForLyingBranchKey() {
    var ddbClient :- expect ProvideDDBClient();
    var kmsClient :- expect ProvideKMSClient();
    var keyStore :- expect DefaultKeyStore(ddbClient?:=Some(ddbClient), kmsClient?:=Some(kmsClient), kmsId := postalHornKeyArn);

    TestBranchKeyOperationsExpectsException(
      id := hierarchyV1InvalidKmsArnId,
      version := hierarchyV1InvalidKmsArnVersion,
      expectedError := ComAmazonawsKmsTypes.Error.IncorrectKeyException,
      keyStore := keyStore
    );
  }

  // Test Case: KMS ARN Mismatch
  // The Branch Key's Item says it is protected by KMS-ARN Fixtures.dfy#postalHornKeyArn,
  // but the KMS requests were actually executed against KMS-ARN Fixtures.dfy#keyArn.
  // Thus, all Keystore Operations related to the Branch Key MUST fail with exceptions from KMS.
  // DDB Item KMS ARN:      Fixtures.dfy#postalHornKeyArn
  // Actual KMS ARN used:   Fixtures.dfy#keyArn
  // Expected: KMS.IncorrectKeyException
  method {:test} TestHv2GetKeysForLyingBranchKeyWrongKmsArn() {
    var ddbClient :- expect ProvideDDBClient();
    var kmsClient :- expect ProvideKMSClient();
    var keyStore :- expect DefaultKeyStore(ddbClient?:=Some(ddbClient), kmsClient?:=Some(kmsClient), kmsId := postalHornKeyArn);

    TestBranchKeyOperationsExpectsException(
      id := hierarchyV2InvalidKmsArnId,
      version := hierarchyV2InvalidKmsArnVersion,
      expectedError := ComAmazonawsKmsTypes.Error.IncorrectKeyException,
      keyStore := keyStore
    );
  }

  // Test Case: Mismatched Encryption Context
  // The Branch Key's encryption context in DDB: "TamperedKey:TamperedValue"
  // Actual encryption context used with KMS Requests: "ExampleContextKey:ExampleContextValue"
  // Expected: KMS.InvalidCiphertextException due to encryption context mismatch
  method {:test} TestHv2GetKeysForLyingBranchKeyWrongDigest() {
    var ddbClient :- expect ProvideDDBClient();
    var kmsClient :- expect ProvideKMSClient();
    var keyStore :- expect DefaultKeyStore(ddbClient?:=Some(ddbClient), kmsClient?:=Some(kmsClient));

    TestBranchKeyOperationsExpectsException(
      id := hierarchyV2InvalidDigestId,
      version := hierarchyV2InvalidDigestVersion,
      expectedError := ComAmazonawsKmsTypes.Error.InvalidCiphertextException,
      keyStore := keyStore
    );
  }

  // Test Case: Invalid Ciphertext Length
  // The Branch Key's Item contains ciphertext with incorrect length compared to the actual encrypted data.
  // Thus, all Keystore Operations related to the Branch Key MUST fail with KMS.InvalidCiphertextException.
  // Expected Error: KMS InvalidCiphertextException
  method {:test} TestHv2GetKeysForLyingBranchKeyWrongCiphertextLength() {
    var ddbClient :- expect ProvideDDBClient();
    var kmsClient :- expect ProvideKMSClient();
    var keyStore :- expect DefaultKeyStore(ddbClient?:=Some(ddbClient), kmsClient?:=Some(kmsClient));

    TestBranchKeyOperationsExpectsException(
      id := hierarchyV2InvalidCiphertextLengthId,
      version := hierarchyV2InvalidCiphertextLengthVersion,
      expectedError := ComAmazonawsKmsTypes.Error.InvalidCiphertextException,
      keyStore := keyStore
    );
  }

  // The Branch Key's operations (GetActiveBranchKey, GetBranchKeyVersion, GetBeaconKey)
  // MUST fail with the expected KMS error when the branch key is malformed or incorrectly configured.
  // This helper method verifies that each operation returns the appropriate KMS error
  // for invalid branch key configurations.
  method TestBranchKeyOperationsExpectsException(
    id: string,
    version : string,
    expectedError : KmsTestError,
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
    VerifyKMSError(actual:= activeOutput?.error, expected := expectedError);

    var versionOutput? := keyStore.GetBranchKeyVersion(
      Types.GetBranchKeyVersionInput(
        branchKeyIdentifier := id,
        branchKeyVersion := version
      ));
    expect versionOutput?.Failure?;
    VerifyKMSError(actual:= versionOutput?.error, expected := expectedError);

    var beaconOutput? := keyStore.GetBeaconKey(
      Types.GetBeaconKeyInput(
        branchKeyIdentifier := id
      ));
    expect beaconOutput?.Failure?;
    VerifyKMSError(actual := beaconOutput?.error, expected := expectedError);
  }
}
