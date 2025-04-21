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
  import ComAmazonawsKmsTypes
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
      storage := Some(
        Types.ddb(
          Types.DynamoDBTable(
            ddbTableName := staticBranchKeyStoreName,
            ddbClient := Some(ddbClient)
          ))),
      keyManagement := Some(
        Types.kms(
          Types.AwsKms(
            kmsClient := Some(kmsClient)
          )))
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
      storage := Some(
        Types.ddb(
          Types.DynamoDBTable(
            ddbTableName := staticBranchKeyStoreName,
            ddbClient := Some(ddbClient)
          ))),
      keyManagement := Some(
        Types.kms(
          Types.AwsKms(
            kmsClient := Some(kmsClient)
          )))
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
      storage := Some(
        Types.ddb(
          Types.DynamoDBTable(
            ddbTableName := staticBranchKeyStoreName,
            ddbClient := Some(ddbClient)
          ))),
      keyManagement := Some(
        Types.kms(
          Types.AwsKms(
            kmsClient := Some(kmsClient)
          )))
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

  method {:test} TestGetKeysForMrk()
  {
    var kmsClient :- expect KMS.KMSClient();
    var ddbClient :- expect DDB.DynamoDBClient();
    var kmsConfigMr := Types.KMSConfiguration.mrDiscovery(Types.MRDiscovery(region := "us-west-2"));
    var kmsConfigSr := Types.KMSConfiguration.discovery(Types.Discovery());

    var keyStoreConfigMr := Types.KeyStoreConfig(
      id := None,
      kmsConfiguration := kmsConfigMr,
      logicalKeyStoreName := logicalKeyStoreName,
      storage := Some(
        Types.ddb(
          Types.DynamoDBTable(
            ddbTableName := branchKeyStoreName,
            ddbClient := Some(ddbClient)
          ))),
      keyManagement := Some(
        Types.kms(
          Types.AwsKms(
            kmsClient := Some(kmsClient)
          )))
    );

    var keyStoreConfigSr := keyStoreConfigMr.(kmsConfiguration := kmsConfigSr);

    var keyStoreMr :- expect KeyStore.KeyStore(keyStoreConfigMr);
    var keyStoreSr :- expect KeyStore.KeyStore(keyStoreConfigSr);

    var beaconInput := Types.GetBeaconKeyInput(branchKeyIdentifier := EastBranchKey);
    var beaconKeyResultMr :- expect keyStoreMr.GetBeaconKey(beaconInput);
    expect beaconKeyResultMr.beaconKeyMaterials.beaconKeyIdentifier == EastBranchKey;

    var beaconKeyResultSr := keyStoreSr.GetBeaconKey(beaconInput);
    expect beaconKeyResultSr.Failure?;
    expect beaconKeyResultSr.error.ComAmazonawsKms?;
    match beaconKeyResultSr.error {
      case ComAmazonawsKms(nestedError) =>
        expect nestedError.IncorrectKeyException?;
      case _ => expect false, "Request for Branch Key's Beacon Key protected by us-east-1 KMS Key, issued from us-west-2, without MR logic, MUST fail with KMS IncorrectKeyException.";
    }

    var branchInput := Types.GetActiveBranchKeyInput(branchKeyIdentifier := EastBranchKey);
    var branchKeyResultMr :- expect keyStoreMr.GetActiveBranchKey(branchInput);
    expect branchKeyResultMr.branchKeyMaterials.branchKeyIdentifier == EastBranchKey;

    var branchKeyResultSr := keyStoreSr.GetActiveBranchKey(branchInput);
    expect branchKeyResultSr.Failure?;
    expect branchKeyResultSr.error.ComAmazonawsKms?;

    match branchKeyResultSr.error {
      case ComAmazonawsKms(nestedError) =>
        expect nestedError.IncorrectKeyException?;
      case _ => expect false, "Request for Branch Key Active Version protected by us-east-1 KMS Key, issued from us-west-2, without MR logic, MUST fail with KMS IncorrectKeyException.";
    }
  }



}
