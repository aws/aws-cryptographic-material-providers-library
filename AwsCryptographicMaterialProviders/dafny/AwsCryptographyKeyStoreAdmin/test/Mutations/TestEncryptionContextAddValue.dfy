// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../../src/Index.dfy"
include "../../../AwsCryptographyKeyStore/test/CleanupItems.dfy"
include "../../../AwsCryptographyKeyStore/test/Fixtures.dfy"
include "../../../AwsCryptographyKeyStore/Model/AwsCryptographyKeyStoreTypes.dfy"
include "../AdminFixtures.dfy"

// Tests that an Encryption Context only change:
// - Completes if there is no paging
// - Changes the Custom Encryption Context for all items
// - All items can be decrypted by KMS

module {:options "/functionSyntax:4" } TestMutationsEncryptionContextAddValue {
  import Types = AwsCryptographyKeyStoreAdminTypes
  import KeyStoreAdmin
  import KeyStore
  import KeyStoreTypes = AwsCryptographyKeyStoreTypes
  import opened Wrappers
  import Fixtures
  import AdminFixtures
  import UUID
  import CleanupItems
  import KMS = Com.Amazonaws.Kms
  import DDB = Com.Amazonaws.Dynamodb
  import DefaultKeyStorageInterface
  import Time
  import Structure
  import String = StandardLibrary.String
  import UTF8
  import opened StandardLibrary.UInt

  const happyCaseId := "test-mutations-encryption-context-key-value-out-side-of-expected"
  const customEC := "aws-crypto-ec:Koda"
  const kmsId: string := Fixtures.keyArn
  const physicalName: string := Fixtures.branchKeyStoreName
  const logicalName: string := Fixtures.logicalKeyStoreName
  const testLogPrefix := "\nTestMutationsEncryptionContextAddValue :: TestProofMutationsOverWritesUnModeldedAttributesCase :: "

  // This is evidence that the code behaves in the manner we DO NOT WANT
  method {:test} {:vcs_split_on_every_assert} TestProofMutationsOverWritesUnModeldedAttributesCase()
  {
    print " running";

    // expect false; // disable test till other investigation is done
    var ddbClient :- expect DDB.DynamoDBClient();
    var kmsClient :- expect KMS.KMSClient();

    var storage :- expect Fixtures.DefaultStorage();
    var keyStore :- expect Fixtures.DefaultKeyStore();
    var underTest :- expect AdminFixtures.DefaultAdmin(ddbClient?:=Some(ddbClient));
    var strategy :- expect AdminFixtures.DefaultKeyManagerStrategy(kmsClient?:=Some(kmsClient));

    var uuid :- expect UUID.GenerateUUID();
    var testId := happyCaseId + "-" + uuid;

    // var robbieBytes :- expect UTF8.Encode("Robbie");
    var kodaBytes :- expect UTF8.Encode("Koda");
    var isADogBytes :- expect UTF8.Encode("is a dog.");
    var originalEC := map[kodaBytes := isADogBytes];
    Fixtures.CreateHappyCaseId(id:=testId, versionCount:=0, customEC:=originalEC);

    print testLogPrefix + " Created the legit test items with 1 versions! testId: " + testId + "\n";

    var _ :- expect AdminFixtures.AddAttributeWithoutLibrary(id:=testId, alsoViolateBeacon? := true, ddbClient? := Some(ddbClient));

    print testLogPrefix + " Violated all three. testId: " + testId + "\n";

    var timestamp :- expect Time.GetCurrentTimeStamp();
    var newCustomEC: KeyStoreTypes.EncryptionContextString := map["Koda" := timestamp];
    var mutationsRequest := Types.Mutations(terminalEncryptionContext := Some(newCustomEC));
    var initInput := Types.InitializeMutationInput(
      branchKeyIdentifier := testId,
      mutations := mutationsRequest,
      strategy := Some(strategy));
    var initializeOutput :- expect underTest.InitializeMutation(initInput);
    var initializeToken := initializeOutput.mutationToken;

    print testLogPrefix + " Initialized Mutation. testId: " + testId + "\n";

    var testInput := Types.ApplyMutationInput(
      mutationToken := initializeToken,
      pageSize := Some(24),
      strategy := Some(strategy));
    var applyOutput :- expect underTest.ApplyMutation(testInput);

    print testLogPrefix + " Applied Mutation w/ pageSize 24. testId: " + testId + "\n";

    expect applyOutput.result.completeMutation?, "Apply Mutation output should not continue!";

    var versionQuery := KeyStoreTypes.QueryForVersionsInput(
      Identifier := testId,
      pageSize := 24
    );
    var queryOut :- expect storage.QueryForVersions(versionQuery);
    var items := queryOut.items;

    var itemIndex := 0;
    var inputV: KeyStoreTypes.GetBranchKeyVersionInput;
    while itemIndex < |items|
    {
      var item := items[itemIndex];
      expect
        customEC in item.EncryptionContext,
                    "Koda should be a Key in the Custom Encryption Context of all items for this test.";
      expect
        item.EncryptionContext[customEC] == timestamp,
        "Koda's value should be the test timestamp for all decrypt items for this test.";
      expect "type" in item.EncryptionContext, "Decrypt Only item is missing 'type' from EC!!";
      expect
        item.Type.HierarchicalSymmetricVersion?,
        "Query for Decrypt Only returned a non-Decrypt Only!";

      if ("Robbie" in item.EncryptionContext) {
        print testLogPrefix + "Robbie in " + item.EncryptionContext["type"] + "\n";
      }
      var versionUUID := item.Type.HierarchicalSymmetricVersion.Version;
      inputV := KeyStoreTypes.GetBranchKeyVersionInput(
        branchKeyIdentifier := testId,
        branchKeyVersion := versionUUID
      );
      var _ :- expect keyStore.GetBranchKeyVersion(inputV);

      // This is a best effort
      var _ := CleanupItems.DeleteTypeWithFailure(testId, item.EncryptionContext["type"], ddbClient);
      print testLogPrefix + " Validated Decrypt Only and tried to clean it up: " + item.EncryptionContext["type"] + "\n";
      itemIndex := 1 + itemIndex;
    }

    var lastActiveInput := KeyStoreTypes.GetEncryptedActiveBranchKeyInput(Identifier:=testId);
    var lastActive? :- expect storage.GetEncryptedActiveBranchKey(lastActiveInput);
    expect lastActive?.Item.Type.ActiveHierarchicalSymmetricVersion?;
    var lastActive := lastActive?.Item.Type.ActiveHierarchicalSymmetricVersion;
    expect
      customEC in lastActive?.Item.EncryptionContext,
                  "Koda should be a Key in the Custom Encryption Context for the ACTIVE.";
    expect
      lastActive?.Item.EncryptionContext[customEC] == timestamp,
      "Koda's value should be the test timestamp for the ACTIVE.";
    var _ :- expect keyStore.GetActiveBranchKey(KeyStoreTypes.GetActiveBranchKeyInput(branchKeyIdentifier := testId));
    print testLogPrefix + " Active Validated with KMS/KeyStore: " + testId + "\n";
    var _ := CleanupItems.DeleteTypeWithFailure(testId, Structure.BRANCH_KEY_ACTIVE_TYPE, ddbClient);

    var beaconInput := KeyStoreTypes.GetEncryptedBeaconKeyInput(Identifier:=testId);
    var beacon? :- expect storage.GetEncryptedBeaconKey(beaconInput);
    expect beacon?.Item.Type.ActiveHierarchicalSymmetricBeacon?;
    expect
      customEC in beacon?.Item.EncryptionContext,
                  "Koda should be a Key in the Custom Encryption Context for the Beacon.";
    expect
      beacon?.Item.EncryptionContext[customEC] == timestamp,
      "Koda's value should be the test timestamp for the Beacon.";
    var _ :- expect keyStore.GetBeaconKey(KeyStoreTypes.GetBeaconKeyInput(branchKeyIdentifier := testId));
    print testLogPrefix + " Beacon Validated with KMS/KeyStore: " + testId + "\n";
    var _ := CleanupItems.DeleteTypeWithFailure(testId, Structure.BEACON_KEY_TYPE_VALUE, ddbClient);
  }
}

// TestMutationsEncryptionContextAddValue :: TestHappyCase ::  Initialized Mutation. testId: test-mutations-encryption-context-add-value-2e2a4933-9a38-4bd7-9df4-5b6edf044646
// FAILED
        // dafny/AwsCryptographyKeyStoreAdmin/test/Mutations/TestEncryptionContextAddValue.dfy(96,23): Wrappers.Result.Failure(AwsCryptographyKeyStoreAdminTypes.Error.KeyStoreAdminException(WIP:test-mutations-encryption-context-add-value-2e2a4933-9a38-4bd7-9df4-5b6edf044646))
