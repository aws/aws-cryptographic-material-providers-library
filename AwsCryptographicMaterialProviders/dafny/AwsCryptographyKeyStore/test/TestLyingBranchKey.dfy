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
}
