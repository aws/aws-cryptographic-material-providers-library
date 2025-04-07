// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/Index.dfy"
include "BranchKeyValidators.dfy"

// methods to validate a Get* Branch Key result from the Branch Key Store client given an MRK
module {:options "/functionSyntax:4" } TestGetKeysMRK {
  import opened Wrappers
  import opened StandardLibrary.UInt
  import UTF8
  import Types = AwsCryptographyKeyStoreTypes


  // This is a static test case to Get Branch Keys created with Mrk Keys
  // method {:test} TestGetActiveMrkKey()
  // {
  //   VerifyGetActiveMrkKey(
  //     KmsConfigEast := KmsConfigEast,
  //     KmsConfigWest := KmsConfigWest,
  //     KmsMrkConfigEast := KmsMrkConfigEast,
  //     KmsMrkConfigWest := KmsMrkConfigWest
  //   );
  // }

  // TODO-HV2-M1: Add MRK test for hv2
  // method {:isolate_assertions} VerifyGetActiveMrkKey(
  //   KmsConfigEast : Types.KMSConfiguration,
  //   KmsConfigWest : Types.KMSConfiguration,
  //   KmsMrkConfigEast : Types.KMSConfiguration,
  //   KmsMrkConfigWest : Types.KMSConfiguration
  // )
  // {
  //   var ddbClient :- expect DDB.DynamoDBClient();

  //   var westKeyStore :- expect KeyStoreWithOptionalClient(
  //     kmsId := MrkArnWest,
  //     physicalName := branchKeyStoreName,
  //     logicalName := logicalKeyStoreName,
  //     ddbClient? := Some(ddbClient)
  //   );

  //   var eastKeyStore :- expect KeyStoreWithOptionalClient(
  //     kmsId := MrkArnEast,
  //     physicalName := branchKeyStoreName,
  //     logicalName := logicalKeyStoreName,
  //     ddbClient? := Some(ddbClient)
  //   );

  //   var westMrkKeyStore :- expect KeyStoreWithOptionalClient(
  //     kmsId := MrkArnWest,
  //     physicalName := branchKeyStoreName,
  //     logicalName := logicalKeyStoreName,
  //     ddbClient? := Some(ddbClient),
  //     srkKey := false,
  //     mrkKey := true
  //   );

  //   var eastMrkKeyStore :- expect KeyStoreWithOptionalClient(
  //     kmsId := MrkArnEast,
  //     physicalName := branchKeyStoreName,
  //     logicalName := logicalKeyStoreName,
  //     ddbClient? := Some(ddbClient),
  //     srkKey := false,
  //     mrkKey := true
  //   );

  //   var apMrkKeyStore :- expect KeyStoreWithOptionalClient(
  //     kmsId := MrkArnAP,
  //     physicalName := branchKeyStoreName,
  //     logicalName := logicalKeyStoreName,
  //     ddbClient? := Some(ddbClient),
  //     srkKey := false,
  //     mrkKey := true
  //   );

  //   // All four set of keys (branch, beacon and version) should work when the regions match
  //   testActiveBranchKeyHappyCase(
  //     keyStore := westKeyStore,
  //     branchKeyId := WestBranchKey,
  //     branchKeyIdActiveVersionUtf8Bytes := WestBranchKeyBranchKeyIdActiveVersionUtf8Bytes,
  //     encryptionContext := KmsMrkEC
  //   );
  //   testBeaconKeyHappyCase(
  //     keyStore := westKeyStore,
  //     branchKeyId := WestBranchKey,
  //     encryptionContext := KmsMrkEC
  //   );
  //   testBranchKeyVersionHappyCase(
  //     keyStore := westKeyStore,
  //     branchKeyId := WestBranchKey,
  //     branchKeyIdActiveVersion := WestBranchKeyIdActiveVersion,
  //     branchKeyIdActiveVersionUtf8Bytes := WestBranchKeyBranchKeyIdActiveVersionUtf8Bytes,
  //     encryptionContext := KmsMrkEC
  //   );

  //   testActiveBranchKeyHappyCase(
  //     keyStore := eastKeyStore,
  //     branchKeyId := EastBranchKey,
  //     branchKeyIdActiveVersionUtf8Bytes := EastBranchKeyBranchKeyIdActiveVersionUtf8Bytes,
  //     encryptionContext := KmsMrkEC
  //   );
  //   testBeaconKeyHappyCase(
  //     keyStore := eastKeyStore,
  //     branchKeyId := EastBranchKey,
  //     encryptionContext := KmsMrkEC
  //   );
  //   testBranchKeyVersionHappyCase(
  //     keyStore := eastKeyStore,
  //     branchKeyId := EastBranchKey,
  //     branchKeyIdActiveVersion := EastBranchKeyIdActiveVersion,
  //     branchKeyIdActiveVersionUtf8Bytes := EastBranchKeyBranchKeyIdActiveVersionUtf8Bytes,
  //     encryptionContext := KmsMrkEC
  //   );

  //   testActiveBranchKeyHappyCase(
  //     keyStore := westMrkKeyStore,
  //     branchKeyId := WestBranchKey,
  //     branchKeyIdActiveVersionUtf8Bytes := WestBranchKeyBranchKeyIdActiveVersionUtf8Bytes,
  //     encryptionContext := KmsMrkEC
  //   );
  //   testBeaconKeyHappyCase(
  //     keyStore := westMrkKeyStore,
  //     branchKeyId := WestBranchKey,
  //     encryptionContext := KmsMrkEC
  //   );
  //   testBranchKeyVersionHappyCase(
  //     keyStore := westMrkKeyStore,
  //     branchKeyId := WestBranchKey,
  //     branchKeyIdActiveVersion := WestBranchKeyIdActiveVersion,
  //     branchKeyIdActiveVersionUtf8Bytes := WestBranchKeyBranchKeyIdActiveVersionUtf8Bytes,
  //     encryptionContext := KmsMrkEC
  //   );

  //   testActiveBranchKeyHappyCase(
  //     keyStore := eastMrkKeyStore,
  //     branchKeyId := EastBranchKey,
  //     branchKeyIdActiveVersionUtf8Bytes := EastBranchKeyBranchKeyIdActiveVersionUtf8Bytes,
  //     encryptionContext := KmsMrkEC
  //   );
  //   testBeaconKeyHappyCase(
  //     keyStore := eastMrkKeyStore,
  //     branchKeyId := EastBranchKey,
  //     encryptionContext := KmsMrkEC
  //   );
  //   testBranchKeyVersionHappyCase(
  //     keyStore := eastMrkKeyStore,
  //     branchKeyId := EastBranchKey,
  //     branchKeyIdActiveVersion := EastBranchKeyIdActiveVersion,
  //     branchKeyIdActiveVersionUtf8Bytes := EastBranchKeyBranchKeyIdActiveVersionUtf8Bytes,
  //     encryptionContext := KmsMrkEC
  //   );

  //   // MRK Configuration should work with the other region
  //   testActiveBranchKeyHappyCase(
  //     keyStore := westMrkKeyStore,
  //     branchKeyId := EastBranchKey,
  //     branchKeyIdActiveVersionUtf8Bytes := EastBranchKeyBranchKeyIdActiveVersionUtf8Bytes,
  //     encryptionContext := KmsMrkEC
  //   );
  //   testBeaconKeyHappyCase(
  //     keyStore := westMrkKeyStore,
  //     branchKeyId := EastBranchKey,
  //     encryptionContext := KmsMrkEC
  //   );
  //   testBranchKeyVersionHappyCase(
  //     keyStore := westMrkKeyStore,
  //     branchKeyId := EastBranchKey,
  //     branchKeyIdActiveVersion := EastBranchKeyIdActiveVersion,
  //     branchKeyIdActiveVersionUtf8Bytes := EastBranchKeyBranchKeyIdActiveVersionUtf8Bytes,
  //     encryptionContext := KmsMrkEC
  //   );

  //   testActiveBranchKeyHappyCase(
  //     keyStore := eastMrkKeyStore,
  //     branchKeyId := WestBranchKey,
  //     branchKeyIdActiveVersionUtf8Bytes := WestBranchKeyBranchKeyIdActiveVersionUtf8Bytes,
  //     encryptionContext := KmsMrkEC
  //   );
  //   testBeaconKeyHappyCase(
  //     keyStore := eastMrkKeyStore,
  //     branchKeyId := WestBranchKey,
  //     encryptionContext := KmsMrkEC
  //   );
  //   testBranchKeyVersionHappyCase(
  //     keyStore := eastMrkKeyStore,
  //     branchKeyId := WestBranchKey,
  //     branchKeyIdActiveVersion := WestBranchKeyIdActiveVersion,
  //     branchKeyIdActiveVersionUtf8Bytes := WestBranchKeyBranchKeyIdActiveVersionUtf8Bytes,
  //     encryptionContext := KmsMrkEC
  //   );

  //   // Plain Configuration should fail with the other region
  //   GetActiveKeyWithIncorrectKmsKeyArnHelper(
  //     keyStore := westKeyStore,
  //     branchKeyId := EastBranchKey
  //   );
  //   GetBeaconKeyWithIncorrectKmsKeyArnHelper(
  //     keyStore := westKeyStore,
  //     branchKeyId := EastBranchKey
  //   );
  //   GetBranchKeyVersionWithIncorrectKmsKeyArnHelper(
  //     keyStore := westKeyStore,
  //     branchKeyId := EastBranchKey,
  //     branchKeyIdActiveVersion := EastBranchKeyIdActiveVersion
  //   );

  //   GetActiveKeyWithIncorrectKmsKeyArnHelper(
  //     keyStore := eastKeyStore,
  //     branchKeyId := WestBranchKey
  //   );
  //   GetBeaconKeyWithIncorrectKmsKeyArnHelper(
  //     keyStore := eastKeyStore,
  //     branchKeyId := WestBranchKey
  //   );
  //   GetBranchKeyVersionWithIncorrectKmsKeyArnHelper(
  //     keyStore := eastKeyStore,
  //     branchKeyId := WestBranchKey,
  //     branchKeyIdActiveVersion := WestBranchKeyIdActiveVersion
  //   );

  //   // apMrkKeyStore should always fail
  //   testActiveBranchKeyKMSFailureCase(
  //     keyStore := apMrkKeyStore,
  //     branchKeyId := WestBranchKey
  //   );
  //   testBranchKeyVersionKMSFailureCase(
  //     keyStore := apMrkKeyStore,
  //     branchKeyId := WestBranchKey,
  //     branchKeyIdActiveVersion := WestBranchKeyIdActiveVersion
  //   );
  //   testBeaconKeyKMSFailureCase(
  //     keyStore := apMrkKeyStore,
  //     branchKeyId := WestBranchKey
  //   );
  // }

}