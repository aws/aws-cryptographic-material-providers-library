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

  // Helper method to verify if an error matches the expected KMS error type
  method VerifyKMSError(
    actual: Types.Error,
    expected: Types.Error
  ) {
    match actual {
      case ComAmazonawsKms(nestedError) =>
        expect expected.ComAmazonawsKms?;
        match nestedError {
          case IncorrectKeyException(_) =>
            expect expected.ComAmazonawsKms.IncorrectKeyException?;
          case InvalidCiphertextException(_) =>
            expect expected.ComAmazonawsKms.InvalidCiphertextException?;
          case _ =>
            expect false, "Unexpected KMS error type";
        }
      case BranchKeyCiphertextException(_) =>
        expect expected.BranchKeyCiphertextException?;
      case _ =>
        expect false, "Expected KMS error or BranchKeyCiphertextException, but got different error type";
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
  // Expected Error: KMS IncorrectKeyException
  method {:test} TestHv1GetKeysForLyingBranchKey() {
    var ddbClient :- expect ProvideDDBClient();
    var kmsClient :- expect ProvideKMSClient();
    var keyStore :- expect StaticKeyStore(ddbClient?:=Some(ddbClient), kmsClient?:=Some(kmsClient), kmsId := postalHornKeyArn);

    TestBranchKeyOperationsExpectsException(
      id := hierarchyV1InvalidKmsArnId,
      version := hierarchyV1InvalidKmsArnVersion,
      expectedError := Types.Error.ComAmazonawsKms(ComAmazonawsKmsTypes.Error.IncorrectKeyException),
      keyStore := keyStore
    );
  }

  // Test Case: KMS ARN Mismatch
  // The Branch Key's Item says it is protected by KMS-ARN Fixtures.dfy#postalHornKeyArn,
  // but the KMS requests were actually executed against KMS-ARN Fixtures.dfy#keyArn.
  // Thus, all Keystore Operations related to the Branch Key MUST fail with exceptions from KMS.
  // DDB Item KMS ARN:      Fixtures.dfy#postalHornKeyArn
  // Actual KMS ARN used:   Fixtures.dfy#keyArn
  // Expected Error: KMS.IncorrectKeyException
  method {:test} TestHv2GetKeysForLyingBranchKeyWrongKmsArn() {
    var ddbClient :- expect ProvideDDBClient();
    var kmsClient :- expect ProvideKMSClient();
    var keyStore :- expect StaticKeyStore(ddbClient?:=Some(ddbClient), kmsClient?:=Some(kmsClient), kmsId := postalHornKeyArn);

    TestBranchKeyOperationsExpectsException(
      id := hierarchyV2InvalidKmsArnId,
      version := hierarchyV2InvalidKmsArnVersion,
      expectedError := Types.Error.ComAmazonawsKms(ComAmazonawsKmsTypes.Error.IncorrectKeyException),
      keyStore := keyStore
    );
  }

  // Test Case: Create Time Tampering
  // The Branch Key's creation time in DDB: "1970-01-01T00:00:00.000000Z"
  // Actual creation time when Branch Key was created: "2025-04-17T19:11:28.000676Z"
  // Expected: BranchKeyCiphertextException due to wrong BKC digest
  method {:test} TestHv2GetKeysForLyingBranchKeyWrongDigest() {
    var ddbClient :- expect ProvideDDBClient();
    var kmsClient :- expect ProvideKMSClient();
    var keyStore :- expect StaticKeyStore(ddbClient?:=Some(ddbClient), kmsClient?:=Some(kmsClient));

    TestBranchKeyOperationsExpectsException(
      id := hierarchyV2InvalidDigestId,
      version := hierarchyV2InvalidDigestVersion,
      expectedError := Types.Error.BranchKeyCiphertextException(message := ErrorMessages.MD_DIGEST_SHA_NOT_MATCHED),
      keyStore := keyStore
    );
  }

  // Test Case: Invalid Ciphertext Length
  // The Branch Key's Item contains ciphertext with incorrect length compared to the actual encrypted data.
  // Thus, all Keystore Operations related to the Branch Key MUST fail with KMS.InvalidCiphertextException.
  // Expected Error: BranchKeyCiphertextException due to wrong plaintext length after decrypt
  method {:test} TestHv2GetKeysForLyingBranchKeyWrongCiphertextLength() {
    var ddbClient :- expect ProvideDDBClient();
    var kmsClient :- expect ProvideKMSClient();
    var keyStore :- expect StaticKeyStore(ddbClient?:=Some(ddbClient), kmsClient?:=Some(kmsClient));

    TestBranchKeyOperationsExpectsException(
      id := hierarchyV2InvalidCiphertextLengthId,
      version := hierarchyV2InvalidCiphertextLengthVersion,
      expectedError := Types.Error.BranchKeyCiphertextException(message := ErrorMessages.KMS_DECRYPT_INVALID_KEY_LENGTH_HV2),
      keyStore := keyStore
    );
  }

  // Test Case: Missing Encryption Context
  // The Branch Key's encryption context in DDB: "TamperedKey:TamperedValue"
  // Actual encryption context used with KMS Requests: "ExampleContextKey:ExampleContextValue"
  // Expected Error: KMS.InvalidCiphertextException due to encryption context mismatch
  method {:test} TestHv2GetKeysForLyingBranchKeyMissingPrefixedEC() {
    var ddbClient :- expect ProvideDDBClient();
    var kmsClient :- expect ProvideKMSClient();
    var keyStore :- expect StaticKeyStore(ddbClient?:=Some(ddbClient), kmsClient?:=Some(kmsClient));

    TestBranchKeyOperationsExpectsException(
      id := hierarchyV2MissingPrefixedECId,
      version := hierarchyV2MissingPrefixedECVersion,
      expectedError := Types.Error.ComAmazonawsKms(ComAmazonawsKmsTypes.Error.InvalidCiphertextException),
      keyStore := keyStore
    );
  }

  // Test Case: Unexpected Encryption Context
  // The Branch Key's encryption context in DDB includes additional unmodeled EC: "unexpected-key:unexpected-value"
  // Expected Error: KMS.InvalidCiphertextException due to unexpected encryption context
  method {:test} TestHv2GetKeysForLyingBranchKeyUnexpectedEC() {
    var ddbClient :- expect ProvideDDBClient();
    var kmsClient :- expect ProvideKMSClient();
    var keyStore :- expect StaticKeyStore(ddbClient?:=Some(ddbClient), kmsClient?:=Some(kmsClient));

    TestBranchKeyOperationsExpectsException(
      id := hierarchyV2UnexpectedECId,
      version := hierarchyV2UnexpectedECVersion,
      expectedError := Types.Error.ComAmazonawsKms(ComAmazonawsKmsTypes.Error.InvalidCiphertextException),
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
    expectedError : Types.Error,
    keyStore: Types.IKeyStoreClient
  )
    requires keyStore.ValidState()
    modifies keyStore.Modifies
    ensures keyStore.ValidState()
  {
    var versionKeyOutput? := keyStore.VersionKey(
      Types.VersionKeyInput(
        branchKeyIdentifier := id
      )
    );
    expect versionKeyOutput?.Failure?;
    VerifyKMSError(actual:= versionKeyOutput?.error, expected := expectedError);

    var activeOutput? := keyStore.GetActiveBranchKey(
      Types.GetActiveBranchKeyInput(
        branchKeyIdentifier := id
      ));
    expect activeOutput?.Failure?;
    VerifyKMSError(actual:= activeOutput?.error, expected := expectedError);

    var decryptOnlyOutput? := keyStore.GetBranchKeyVersion(
      Types.GetBranchKeyVersionInput(
        branchKeyIdentifier := id,
        branchKeyVersion := version
      ));
    expect decryptOnlyOutput?.Failure?;
    VerifyKMSError(actual:= decryptOnlyOutput?.error, expected := expectedError);

    var beaconOutput? := keyStore.GetBeaconKey(
      Types.GetBeaconKeyInput(
        branchKeyIdentifier := id
      ));
    expect beaconOutput?.Failure?;
    VerifyKMSError(actual := beaconOutput?.error, expected := expectedError);
  }
}
