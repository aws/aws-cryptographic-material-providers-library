// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/Index.dfy"
include "./Fixtures.dfy"
include "../src/Structure.dfy"
include "./CleanupItems.dfy"

module TestCreateKeysWithSpecialECKeys {
  import Types = AwsCryptographyKeyStoreTypes
  import ComAmazonawsKmsTypes
  import KMS = Com.Amazonaws.Kms
  import DDB = Com.Amazonaws.Dynamodb
  import KeyStore
  import opened Wrappers
  import opened Fixtures
  import Structure
  import UTF8
  import CleanupItems
  import UUID

  // Helper method for round-trip happy cases.
  // Creates a branch key with given encryption context, validates returned key materials after calling get keys.
  method HappyCaseRoundTrip(
    id : string,
    encryptionContext : Types.EncryptionContext
  )
    requires |id| > 0
  {
    // Initialize KeyStore
    var kmsClient :- expect KMS.KMSClient();
    var ddbClient :- expect DDB.DynamoDBClient();
    var kmsConfig := Types.KMSConfiguration.kmsKeyArn(keyArn);

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

    // Create key
    var branchKeyId :- expect keyStore.CreateKey(Types.CreateKeyInput(
                                                   branchKeyIdentifier := Some(id),
                                                   encryptionContext := Some(encryptionContext)
                                                 ));

    // Get keys
    var beaconKeyResult :- expect keyStore.GetBeaconKey(
      Types.GetBeaconKeyInput(
        branchKeyIdentifier := branchKeyId.branchKeyIdentifier
      ));

    var activeResult :- expect keyStore.GetActiveBranchKey(
      Types.GetActiveBranchKeyInput(
        branchKeyIdentifier := branchKeyId.branchKeyIdentifier
      ));

    var branchKeyVersion :- expect UTF8.Decode(activeResult.branchKeyMaterials.branchKeyVersion);
    var versionResult :- expect keyStore.GetBranchKeyVersion(
      Types.GetBranchKeyVersionInput(
        branchKeyIdentifier := branchKeyId.branchKeyIdentifier,
        branchKeyVersion := branchKeyVersion
      ));

    // Cleanup branch key
    var _ :- expect CleanupItems.DeleteBranchKey(Identifier := branchKeyId.branchKeyIdentifier, ddbClient := ddbClient);

    // Validate key materials
    expect id
        == versionResult.branchKeyMaterials.branchKeyIdentifier
        == activeResult.branchKeyMaterials.branchKeyIdentifier
        == beaconKeyResult.beaconKeyMaterials.beaconKeyIdentifier;

    expect encryptionContext
        == versionResult.branchKeyMaterials.encryptionContext
        == activeResult.branchKeyMaterials.encryptionContext
        == beaconKeyResult.beaconKeyMaterials.encryptionContext,
           "Failed to retrieve encryption context with branch key materials";
  }

  method {:test} TestCreateKeyWithEmptyKeyEC()
  {
    // Generate UUID for unique test run
    var uuid :- expect UUID.GenerateUUID();
    var id := "test-empty-string-key-ec-" + uuid;

    // Create encryption context
    var encryptionContext :- expect EncodeEncryptionContext(map[
                                                              "" := "encryption"
                                                            ]);

    // Test happy case
    HappyCaseRoundTrip(
      id,
      encryptionContext
    );
  }

  method {:test} TestCreateKeyWithWhiteSpaceEC()
  {
    // Generate UUID for unique test run
    var uuid :- expect UUID.GenerateUUID();
    var id := "test-white-space-key-ec-" + uuid;

    // Create encryption context
    var encryptionContext :- expect EncodeEncryptionContext(map[
                                                              " " := "encryption"
                                                            ]);

    // Test happy case
    HappyCaseRoundTrip(
      id,
      encryptionContext
    );
  }

  method {:test} TestCreateKeyWithAllSpecialCharsEC()
  {
    // Generate UUID for unique test run
    var uuid :- expect UUID.GenerateUUID();
    var id := "test-all-special-chars-ec-" + uuid;

    // Create encryption context with special characters
    var encryptionContext :- expect EncodeEncryptionContext(map[
                                                              "\n" := "newline",
                                                              "\t" := "tab",
                                                              "\r" := "carriage-return",
                                                              " " := "space",
                                                              "   " := "multiple-spaces",
                                                              "NormalKey" := "Value with\nspecial\rchars\t",
                                                              "\u0007" := "bell-unicode",
                                                              "\u0001" := "unicode"
                                                            ]);

    // Test happy case
    HappyCaseRoundTrip(
      id,
      encryptionContext
    );
  }
}
