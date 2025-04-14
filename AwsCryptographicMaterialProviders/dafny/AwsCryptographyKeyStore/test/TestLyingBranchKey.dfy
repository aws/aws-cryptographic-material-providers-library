// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/Index.dfy"
include "Fixtures.dfy"

// These tests assert that a particular form of
// illegal Branch Key is always correctly handled.
// Creation of this particular illegal Branch Key is detailed here:
// `git rev-parse --show-toplevel`/cfn/lyingBranchKeyCreation.md
// The Branch Key's Item says it is protected by KMS-ARN Fixtures.dfy#postalHornKeyArn,
// but the KMS requests were actually executed against KMS-ARN Fixtures.dfy#keyArn.
// Thus, all Keystore Operations related to the Branch Key MUST fail with exceptions from KMS.
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

  method {:test} TestGetActiveKeyForLyingBranchKey() {
    var kmsClient :- expect KMS.KMSClient();
    var ddbClient :- expect DDB.DynamoDBClient();
    var kmsConfig := Types.KMSConfiguration.kmsKeyArn(postalHornKeyArn);
    var keyStoreConfig := Types.KeyStoreConfig(
      id := None,
      kmsConfiguration := kmsConfig,
      logicalKeyStoreName := logicalKeyStoreName,
      grantTokens := None,
      ddbTableName := Some(branchKeyStoreName),
      ddbClient := Some(ddbClient),
      kmsClient := Some(kmsClient)
    );
    var keyStore :- expect KeyStore.KeyStore(keyStoreConfig);

    var result := keyStore.GetActiveBranchKey(
      Types.GetActiveBranchKeyInput(
        branchKeyIdentifier := lyingBranchKeyId
      ));
    expect result.Failure?;
    match result.error {
      case ComAmazonawsKms(nestedError) =>
        expect nestedError.IncorrectKeyException?;
      case _ => expect false, "Lying Branch Key SHOULD Fail with KMS IncorrectKeyException.";
    }
  }

  method {:test} TestGetBranchKeyVersionForLyingBranchKey() {
    var kmsClient :- expect KMS.KMSClient();
    var ddbClient :- expect DDB.DynamoDBClient();
    var kmsConfig := Types.KMSConfiguration.kmsKeyArn(postalHornKeyArn);
    var keyStoreConfig := Types.KeyStoreConfig(
      id := None,
      kmsConfiguration := kmsConfig,
      logicalKeyStoreName := logicalKeyStoreName,
      grantTokens := None,
      ddbTableName := Some(branchKeyStoreName),
      ddbClient := Some(ddbClient),
      kmsClient := Some(kmsClient)
    );
    var keyStore :- expect KeyStore.KeyStore(keyStoreConfig);

    var result := keyStore.GetBranchKeyVersion(
      Types.GetBranchKeyVersionInput(
        branchKeyIdentifier := lyingBranchKeyId,
        branchKeyVersion := lyingBranchKeyDecryptOnlyVersion
      ));
    expect result.Failure?;
    match result.error {
      case ComAmazonawsKms(nestedError) =>
        expect nestedError.IncorrectKeyException?;
      case _ => expect false, "Lying Branch Key SHOULD Fail with KMS IncorrectKeyException.";
    }
  }

  method {:test} TestGetBeaconKeyForLyingBranchKey() {
    var kmsClient :- expect KMS.KMSClient();
    var ddbClient :- expect DDB.DynamoDBClient();
    var kmsConfig := Types.KMSConfiguration.kmsKeyArn(postalHornKeyArn);
    var keyStoreConfig := Types.KeyStoreConfig(
      id := None,
      kmsConfiguration := kmsConfig,
      logicalKeyStoreName := logicalKeyStoreName,
      grantTokens := None,
      ddbTableName := Some(branchKeyStoreName),
      ddbClient := Some(ddbClient),
      kmsClient := Some(kmsClient)
    );
    var keyStore :- expect KeyStore.KeyStore(keyStoreConfig);

    var result := keyStore.GetBeaconKey(
      Types.GetBeaconKeyInput(
        branchKeyIdentifier := lyingBranchKeyId
      ));
    expect result.Failure?;
    match result.error {
      case ComAmazonawsKms(nestedError) =>
        expect nestedError.IncorrectKeyException?;
      case _ => expect false, "Lying Branch Key SHOULD Fail with KMS IncorrectKeyException.";
    }
  }

  method {:test} TestVersionKeyForLyingBranchKey() {
    var kmsClient :- expect KMS.KMSClient();
    var ddbClient :- expect DDB.DynamoDBClient();
    var kmsConfig := Types.KMSConfiguration.kmsKeyArn(postalHornKeyArn);
    var keyStoreConfig := Types.KeyStoreConfig(
      id := None,
      kmsConfiguration := kmsConfig,
      logicalKeyStoreName := logicalKeyStoreName,
      grantTokens := None,
      ddbTableName := Some(branchKeyStoreName),
      ddbClient := Some(ddbClient),
      kmsClient := Some(kmsClient)
    );
    var keyStore :- expect KeyStore.KeyStore(keyStoreConfig);

    var result := keyStore.VersionKey(
      Types.VersionKeyInput(
        branchKeyIdentifier := lyingBranchKeyId
      ));
    expect result.Failure?;
    match result.error {
      case ComAmazonawsKms(nestedError) =>
        expect nestedError.IncorrectKeyException?;
      case _ => expect false,   "Lying Branch Key SHOULD Fail with KMS IncorrectKeyException.";
    }
  }

  // Create a static HV-2 BK and tamper it; call Get* on it,
  // expect BKS.BranchKeyCiphertextException is thrown.
  method {:test} TestHV2GetKeyWrongDigest() {
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var keyStore :- expect Fixtures.DefaultKeyStore(ddbClient?:=Some(ddbClient), kmsClient?:=Some(kmsClient));

    var testId := "DO-NOT-DELETE-test-hv2-get-key-wrong-digest";

    // Call Get Active Key
    var activeOutput := keyStore.GetActiveBranchKey(
      Types.GetActiveBranchKeyInput(
        branchKeyIdentifier := testId
      )
    );
    expect activeOutput.Failure?;
    match activeOutput.error {
      case ComAmazonawsKms(nestedError) => 
        expect nestedError.InvalidCiphertextException?;
      case _ =>
        expect false, "Expected KMS InvalidCiphertextException";
    }
  }

  // Create a static HV-2 BK; replace enc with a blob that is the wrong length;
  // call Get* on it; expect a BKS.BranchKeyCiphertextException to be thrown.
  method {:test} TestHV2GetKeyWrongCiphertextLength() {
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var keyStore :- expect Fixtures.DefaultKeyStore(ddbClient?:=Some(ddbClient), kmsClient?:=Some(kmsClient));

    var testId := "DO-NOT-DELETE-test-hv2-get-key-wrong-ciphertext";

    // Call Get Active Key
    var activeOutput := keyStore.GetActiveBranchKey(
      Types.GetActiveBranchKeyInput(
        branchKeyIdentifier := testId
      )
    );
    expect activeOutput.Failure?;
    match activeOutput.error {
      case ComAmazonawsKms(nestedError) => 
        expect nestedError.InvalidCiphertextException?;
      case _ =>
        expect false, "Expected KMS InvalidCiphertextException";
    }
  }

  // Create a static HV-2 BK; carefully tamper it so only the KMS-ARN field
  // disagrees with the Humbolt Key ID embedded in the cipher-text;
  // call Get* on it; expect a reasonable BKS.BranchKeyCiphertextException is thrown.
  method {:test} TestHV2GetKeyWrongKmsArn() {
    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();

    // Configure Key Store with Key Arn with Branch key's tampered KMS Key ARN read from Dynamodb
    var keyStore :- expect Fixtures.DefaultKeyStore(ddbClient?:=Some(ddbClient), kmsClient?:=Some(kmsClient), kmsId := Fixtures.postalHornKeyArn);

    var testId := "DO-NOT-DELETE-test-hv2-get-key-wrong-kms-arn";

    // Call Get Active Key
    var activeOutput := keyStore.GetActiveBranchKey(
      Types.GetActiveBranchKeyInput(
        branchKeyIdentifier := testId
      )
    );
    expect activeOutput.Failure?;
    print activeOutput.error;
    match activeOutput.error {
      case ComAmazonawsKms(nestedError) => 
        expect nestedError.IncorrectKeyException?;
      case _ =>
        expect false, "Expected KMS InvalidCiphertextException";
    }
  }
}
