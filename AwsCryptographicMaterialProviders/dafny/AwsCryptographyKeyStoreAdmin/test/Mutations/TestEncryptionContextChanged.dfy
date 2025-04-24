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

module {:options "/functionSyntax:4" } TestEncryptionContextChanged {
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

  const happyCaseId := "test-mutate-encryption-context-only"
  const customEC := "aws-crypto-ec:Robbie"
  const kmsId: string := Fixtures.keyArn
  const physicalName: string := Fixtures.branchKeyStoreName
  const logicalName: string := Fixtures.logicalKeyStoreName
  const testLogPrefix := "\nTestEncryptionContextChanged :: TestHappyCase :: "

  method {:test} TestHappyCase()
  {
    // print " running";

    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var storage :- expect Fixtures.DefaultStorage(ddbClient?:=Some(ddbClient));
    var keyStore :- expect Fixtures.DefaultKeyStore(ddbClient?:=Some(ddbClient), kmsClient?:=Some(kmsClient));
    var strategy :- expect AdminFixtures.DefaultKeyManagerStrategy(kmsClient?:=Some(kmsClient));
    var underTest :- expect AdminFixtures.DefaultAdmin(ddbClient?:=Some(ddbClient));

    var uuid :- expect UUID.GenerateUUID();
    var testId := happyCaseId + "-" + uuid;

    Fixtures.CreateHappyCaseId(id:=testId, versionCount:=1);

    // print testLogPrefix + " Created the test items with 2 versions! testId: " + testId + "\n";

    var activeOneInput := KeyStoreTypes.GetEncryptedActiveBranchKeyInput(Identifier:=testId);
    var activeOne? :- expect storage.GetEncryptedActiveBranchKey(activeOneInput);
    expect customEC in activeOne?.Item.EncryptionContext;
    expect activeOne?.Item.Type.ActiveHierarchicalSymmetricVersion?;
    var activeOne := activeOne?.Item.Type.ActiveHierarchicalSymmetricVersion.Version;
    var robbieOne := activeOne?.Item.EncryptionContext[customEC];

    // print testLogPrefix + " Established ActiveOne: " + activeOne + "\n";

    var timestamp :- expect Time.GetCurrentTimeStamp();
    var newCustomEC: KeyStoreTypes.EncryptionContextString := map["Robbie" := timestamp];
    var mutationsRequest := Types.Mutations(TerminalEncryptionContext := Some(newCustomEC));
    var initInput := Types.InitializeMutationInput(
      Identifier := testId,
      Mutations := mutationsRequest,
      Strategy := Some(strategy),
      SystemKey := Types.SystemKey.trustStorage(trustStorage := Types.TrustStorage()),
      // TODO-HV-2-Version
      // DoNotVersion := Some(false));
      DoNotVersion := Some(true));
    var initializeOutput :- expect underTest.InitializeMutation(initInput);
    var initializeToken := initializeOutput.MutationToken;

    // print testLogPrefix + " Initialized Mutation. M-Lock UUID " + initializeToken.UUID + "\n";

    var testInput := Types.ApplyMutationInput(
      MutationToken := initializeToken,
      PageSize := Some(24),
      Strategy := Some(strategy),
      SystemKey := Types.SystemKey.trustStorage(trustStorage := Types.TrustStorage()));
    var applyOutput :- expect underTest.ApplyMutation(testInput);

    // print testLogPrefix + " Applied Mutation w/ pageSize 1. testId: " + testId + "\n";

    expect applyOutput.MutationResult.CompleteMutation?, "Apply Mutation output should not continue!";

    var versionQuery := KeyStoreTypes.QueryForVersionsInput(
      Identifier := testId,
      PageSize := 24
    );
    var queryOut :- expect storage.QueryForVersions(versionQuery);
    var items := queryOut.Items;
    expect
      // TODO-HV-2-Version
      // |items| == 3,
      |items| == 2,
      "Test expects there to be 3 Decrypt Only items! Found: " + String.Base10Int2String(|items|);
    // print testLogPrefix + " Read the 3 Decrypt Only items! testId: " + testId + "\n";

    var itemIndex := 0;
    var inputV: KeyStoreTypes.GetBranchKeyVersionInput;
    while itemIndex < |items|
    {
      var item := items[itemIndex];
      expect
        customEC in item.EncryptionContext,
                    "Robbie should be a Key in the Custom Encryption Context of all items for this test.";
      expect
        item.EncryptionContext[customEC] == timestamp,
        "Robbie's value should be the test timestamp for all decrypt items for this test.";
      expect "type" in item.EncryptionContext, "Decrypt Only item is missing 'type' from EC!!";
      expect
        item.Type.HierarchicalSymmetricVersion?,
        "Query for Decrypt Only returned a non-Decrypt Only!";
      var versionUUID := item.Type.HierarchicalSymmetricVersion.Version;
      inputV := KeyStoreTypes.GetBranchKeyVersionInput(
        branchKeyIdentifier := testId,
        branchKeyVersion := versionUUID
      );
      var _ :- expect keyStore.GetBranchKeyVersion(inputV);

      // This is a best effort
      var _ := CleanupItems.DeleteTypeWithFailure(testId, item.EncryptionContext["type"], ddbClient);
      // print testLogPrefix + " Validated Decrypt Only and tried to clean it up: " + item.EncryptionContext["type"] + "\n";
      itemIndex := 1 + itemIndex;
    }

    var lastActiveInput := KeyStoreTypes.GetEncryptedActiveBranchKeyInput(Identifier:=testId);
    var lastActive? :- expect storage.GetEncryptedActiveBranchKey(lastActiveInput);
    expect lastActive?.Item.Type.ActiveHierarchicalSymmetricVersion?;
    var lastActive := lastActive?.Item.Type.ActiveHierarchicalSymmetricVersion;
    expect
      customEC in lastActive?.Item.EncryptionContext,
                  "Robbie should be a Key in the Custom Encryption Context for the ACTIVE.";
    expect
      lastActive?.Item.EncryptionContext[customEC] == timestamp,
      "Robbie's value should be the test timestamp for the ACTIVE.";
    var _ :- expect keyStore.GetActiveBranchKey(KeyStoreTypes.GetActiveBranchKeyInput(branchKeyIdentifier := testId));
    // print testLogPrefix + " Active Validated with KMS/KeyStore: " + testId + "\n";

    var beaconInput := KeyStoreTypes.GetEncryptedBeaconKeyInput(Identifier:=testId);
    var beacon? :- expect storage.GetEncryptedBeaconKey(beaconInput);
    expect beacon?.Item.Type.ActiveHierarchicalSymmetricBeacon?;
    expect
      customEC in beacon?.Item.EncryptionContext,
                  "Robbie should be a Key in the Custom Encryption Context for the Beacon.";
    expect
      beacon?.Item.EncryptionContext[customEC] == timestamp,
      "Robbie's value should be the test timestamp for the Beacon.";
    var _ :- expect keyStore.GetBeaconKey(KeyStoreTypes.GetBeaconKeyInput(branchKeyIdentifier := testId));
    // print testLogPrefix + " Beacon Validated with KMS/KeyStore: " + testId + "\n";

    var _ := CleanupItems.DeleteBranchKey(Identifier:=testId, ddbClient:=ddbClient);
    // print "TestEncryptionContextChanged.TestHappyCase: ";
  }
}
