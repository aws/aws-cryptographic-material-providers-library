// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/Index.dfy"
include "Fixtures.dfy"

// These tests assert that a Key Store with KMSConfiguration
// Discovery can get Branch Key Material for at least two different KMS
// Key ARNs as long as it has access.
// They are largely identical to the tests in TestGetKeys.dfy,
// but executed against Discovery.
module TestDiscoveryGetKeys {
  import Types = AwsCryptographyKeyStoreTypes
  import KMS = Com.Amazonaws.Kms
  import DDB = Com.Amazonaws.Dynamodb
  import KeyStore
  import opened Wrappers
  import opened Fixtures
  import UTF8

  method {:test} TestGetBeaconKeyForTwoKmsArnsSuccess()
  {
    var kmsClient :- expect KMS.KMSClient();
    var ddbClient :- expect DDB.DynamoDBClient();
    var kmsConfig := Types.KMSConfiguration.discovery(Types.Discovery());

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

    beaconKeyResult :- expect keyStore.GetBeaconKey(
      Types.GetBeaconKeyInput(
        branchKeyIdentifier := postalHornBranchKeyId
      ));

    expect beaconKeyResult.beaconKeyMaterials.beaconKeyIdentifier == postalHornBranchKeyId;
  }


  method {:test} TestGetActiveKeyForTwoKmsArnsSuccess()
  {
    var kmsClient :- expect KMS.KMSClient();
    var ddbClient :- expect DDB.DynamoDBClient();
    var kmsConfig := Types.KMSConfiguration.discovery(Types.Discovery());

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

    activeResult :- expect keyStore.GetActiveBranchKey(
      Types.GetActiveBranchKeyInput(
        branchKeyIdentifier := postalHornBranchKeyId
      ));

    expect activeResult.branchKeyMaterials.branchKeyIdentifier == postalHornBranchKeyId;
  }

  method {:test} TestGetBranchKeyVersionForTwoKmsArnsSuccess()
  {
    var kmsClient :- expect KMS.KMSClient();
    var ddbClient :- expect DDB.DynamoDBClient();
    var kmsConfig := Types.KMSConfiguration.discovery(Types.Discovery());

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

    versionResult :- expect keyStore.GetBranchKeyVersion(
      Types.GetBranchKeyVersionInput(
        branchKeyIdentifier := postalHornBranchKeyId,
        branchKeyVersion := postalHornBranchKeyActiveVersion
      ));
    testBytes :- expect UTF8.Encode(postalHornBranchKeyActiveVersion);
    expect versionResult.branchKeyMaterials.branchKeyIdentifier == postalHornBranchKeyId;
    expect versionResult.branchKeyMaterials.branchKeyVersion == testBytes;
  }

}
