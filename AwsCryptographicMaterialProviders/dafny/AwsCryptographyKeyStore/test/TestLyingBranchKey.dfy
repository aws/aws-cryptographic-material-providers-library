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
  //
  // Test Case: HV1 KMS ARN Mismatch
  // Branch Key Creation Properties:
  //   - Hierarchy Version: 1
  //   - Encrypted with: keyArn
  // Tampered Properties:
  //   - DDB record modified to claim protection by postalHornKeyArn
  // Expected Error: KMS.IncorrectKeyException
  //   - KMS detects key mismatch during decryption attempt
  //   - Thus, all Keystore Operations related to the Branch Key MUST fail with exceptions from KMS.
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

  // Test Case: HV2 KMS ARN Mismatch
  // Branch Key Creation Properties:
  //   - Hierarchy Version: 2
  //   - Encrypted with: keyArn
  // Tampered Properties:
  //   - DDB record modified to claim protection by postalHornKeyArn
  // Expected Error: KMS.IncorrectKeyException
  //   - KMS detects key mismatch during decryption attempt
  //   - Thus, all Keystore Operations related to the Branch Key MUST fail with exceptions from KMS.
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


  // Test Case: HV2 Creation Time Tampering
  // Branch Key Creation Properties:
  //   - Hierarchy Version: 2
  //   - Original creation time: "2025-04-17T19:11:28.000676Z"
  //   - Digest calculated using original creation time
  // Tampered Properties:
  //   - Creation timestamp in DDB changed to "1970-01-01T00:00:00.000000Z"
  // Expected Error: BranchKeyCiphertextException (MD_DIGEST_SHA_NOT_MATCHED)
  //   - KeyStore able to decrypt the ciphertext however
  //   - Digest validation fails due to wrong BKC digest because creation time is part of the authenticated data
  //   - Thus, all Keystore Operations related to the Branch Key MUST fail with BKS.BranchKeyCiphertextException.
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

  // Test Case: HV2 Invalid Ciphertext
  // Branch Key Creation Properties:
  //   - Hierarchy Version: 2
  //   - Valid KMS ciphertext
  // Tampered Properties:
  //   - Ciphertext in DDB is truncated to wrong length
  // Expected Error: KMS.InvalidCiphertextException
  //   - KMS fails to decrypt the ciphertext with incorrect length compared to the actual encrypted data.
  //   - Thus, all Keystore Operations related to the Branch Key MUST fail with KMS.InvalidCiphertextException.
  method {:test} TestHv2GetKeysForLyingBranchKeyWrongCiphertextLength() {
    var ddbClient :- expect ProvideDDBClient();
    var kmsClient :- expect ProvideKMSClient();
    var keyStore :- expect StaticKeyStore(ddbClient?:=Some(ddbClient), kmsClient?:=Some(kmsClient));

    TestBranchKeyOperationsExpectsException(
      id := hierarchyV2InvalidCiphertextId,
      version := hierarchyV2InvalidCiphertextVersion,
      expectedError := Types.Error.ComAmazonawsKms(ComAmazonawsKmsTypes.Error.InvalidCiphertextException),
      keyStore := keyStore
    );
  }

  // Test Case: HV2 Invalid Plaintext Length
  // Branch Key Creation Properties:
  //   - Hierarchy Version: 2
  //   - Plaintext Tuple of valid length: 80 bytes
  //   - Encrypted with KMS and stored in DDB
  // Tampered Properties:
  //   - ReEcnrypts the Protected Data Key (PDK) with incorrect length (not 80 bytes) before calling KMS Encrypt Request and stores the new ciphertext in DDB
  // Expected Error: BranchKeyCiphertextException (KMS_DECRYPT_INVALID_KEY_LENGTH_HV2)
  //   - KeyStore able to decrypt the ciphertext stored in DDB however
  //   - KeyStore fails to validate decrypted plaintext length after KMS decryption with the expected plaintext length(80 bytes) for a HV-2 branch key
  //   - Thus, all Keystore Operations related to the Branch Key MUST fail with BKS.BranchKeyCiphertextException.
  method {:test} TestHv2GetKeysForLyingBranchKeyWrongPlaintextLength() {
    var ddbClient :- expect ProvideDDBClient();
    var kmsClient :- expect ProvideKMSClient();
    var keyStore :- expect StaticKeyStore(ddbClient?:=Some(ddbClient), kmsClient?:=Some(kmsClient));

    TestBranchKeyOperationsExpectsException(
      id := hierarchyV2InvalidPlaintextLengthId,
      version := hierarchyV2InvalidPlaintextLengthVersion,
      expectedError := Types.Error.BranchKeyCiphertextException(message := ErrorMessages.KMS_DECRYPT_INVALID_KEY_LENGTH_HV2),
      keyStore := keyStore
    );
  }

  // Test Case: HV2 Missing Encryption Context
  // Branch Key Creation Properties:
  //   - Hierarchy Version: 2
  //   - Encrypted with context: "ExampleContextKey:ExampleContextValue"
  // Tampered Properties:
  //   - Encryption context in DDB changed to "TamperedKey:TamperedValue"
  // Expected Error: KMS.InvalidCiphertextException
  //   - KMS fails to decrypt due to encryption context mismatch
  //   - Thus, all Keystore Operations related to the Branch Key MUST fail with KMS.InvalidCiphertextException.
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

  // Test Case: HV2 Unexpected Encryption Context
  // Branch Key Creation Properties:
  //   - Hierarchy Version: 2
  //   - Encrypted with specific encryption context key-value pairs
  // Tampered Properties:
  //   - Additional pair "unexpected-key:unexpected-value" added to DDB record
  // Expected Error: KMS.InvalidCiphertextException
  //   - KMS fails to decrypt due to encryption context mismatch
  //   - Thus, all Keystore Operations related to the Branch Key MUST fail with KMS.InvalidCiphertextException.
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
