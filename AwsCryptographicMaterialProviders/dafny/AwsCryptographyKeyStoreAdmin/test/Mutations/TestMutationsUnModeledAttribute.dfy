// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../../src/Index.dfy"
include "../../../AwsCryptographyKeyStore/test/CleanupItems.dfy"
include "../../../AwsCryptographyKeyStore/test/Fixtures.dfy"
include "../../../AwsCryptographyKeyStore/Model/AwsCryptographyKeyStoreTypes.dfy"
include "../AdminFixtures.dfy"

// Tests that an Encryption Context only change:
// - Completes, without paging, since it is annoying to violate the items
// - Changes the Custom Encryption Context for all items
// - All items can be decrypted by KMS
// - maintains un-modeled attributes in exsisting items
// - projects un-modeled attributes to new items

module {:options "/functionSyntax:4" } TestMutationsUnModeledAttribute {
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
  const testLogPrefix := "\nTestMutationsUnModeledAttribute :: TestHappyCase :: "

  method {:test} TestHappyCase()
  {
    // print " running";

    var ddbClient :- expect DDB.DynamoDBClient();
    var kmsClient :- expect KMS.KMSClient();

    var storage :- expect Fixtures.DefaultStorage();
    var keyStore :- expect Fixtures.DefaultKeyStore();
    var underTest :- expect AdminFixtures.DefaultAdmin(ddbClient?:=Some(ddbClient));
    var strategy :- expect AdminFixtures.DefaultKeyManagerStrategy(kmsClient?:=Some(kmsClient));

    var uuid :- expect UUID.GenerateUUID();
    var testId := happyCaseId + "-" + uuid;

    var kodaBytes :- expect UTF8.Encode("Koda");
    var isADogBytes :- expect UTF8.Encode("is a dog.");
    var originalEC := map[kodaBytes := isADogBytes];
    Fixtures.CreateHappyCaseId(id:=testId, versionCount:=0, customEC:=originalEC);

    // print testLogPrefix + " Created the legit test items with 1 versions! testId: " + testId + "\n";
    var unModeledAttri := AdminFixtures.KeyValue(key:="Robbie", value:="Is a dog.");
    var _ :- expect AdminFixtures.AddAttributeWithoutLibrary(
      id:=testId,
      alsoViolateBeacon? := true,
      ddbClient? := Some(ddbClient),
      keyValue := unModeledAttri);

    // print testLogPrefix + " Violated all three. testId: " + testId + "\n";

    var timestamp :- expect Time.GetCurrentTimeStamp();
    var newCustomEC: KeyStoreTypes.EncryptionContextString := map["Koda" := timestamp];
    var mutationsRequest := Types.Mutations(TerminalEncryptionContext := Some(newCustomEC));
    var initInput := Types.InitializeMutationInput(
      Identifier := testId,
      Mutations := mutationsRequest,
      Strategy := Some(strategy),
      SystemKey := Some(Types.SystemKey.trustStorage(trustStorage := Types.TrustStorage())),
      DoNotVersion := Some(false));
    var initializeOutput :- expect underTest.InitializeMutation(initInput);
    var initializeToken := initializeOutput.MutationToken;

    // print testLogPrefix + " Initialized Mutation. testId: " + testId + "\n";

    var testInput := Types.ApplyMutationInput(
      MutationToken := initializeToken,
      PageSize := Some(24),
      Strategy := Some(strategy),
      SystemKey := Some(Types.SystemKey.trustStorage(trustStorage := Types.TrustStorage())));
    var applyOutput :- expect underTest.ApplyMutation(testInput);

    // print testLogPrefix + " Applied Mutation w/ pageSize 24. testId: " + testId + "\n";

    expect applyOutput.MutationResult.CompleteMutation?, "Apply Mutation output should not continue!";

    var versionQuery := KeyStoreTypes.QueryForVersionsInput(
      Identifier := testId,
      PageSize := 24
    );
    var queryOut :- expect storage.QueryForVersions(versionQuery);
    var items := queryOut.Items;

    var itemIndex := 0;
    var inputV: KeyStoreTypes.GetBranchKeyVersionInput;
    while itemIndex < |items|
    {
      var item := items[itemIndex];
      expect
        item.Type.HierarchicalSymmetricVersion?,
        "Query for Decrypt Only returned a non-Decrypt Only!";
      var _ := itemExpectations(item, timestamp, unModeledAttri);
      var versionUUID := item.Type.HierarchicalSymmetricVersion.Version;
      inputV := KeyStoreTypes.GetBranchKeyVersionInput(
        branchKeyIdentifier := testId,
        branchKeyVersion := versionUUID
      );
      var _ :- expect keyStore.GetBranchKeyVersion(inputV);

      // print testLogPrefix + " Validated Decrypt Only and tried to clean it up: " + Structure.BRANCH_KEY_TYPE_PREFIX + versionUUID + "\n";
      itemIndex := 1 + itemIndex;
    }

    var lastActiveInput := KeyStoreTypes.GetEncryptedActiveBranchKeyInput(Identifier:=testId);
    var lastActive? :- expect storage.GetEncryptedActiveBranchKey(lastActiveInput);
    expect lastActive?.Item.Type.ActiveHierarchicalSymmetricVersion?;
    var lastActive := lastActive?.Item.Type.ActiveHierarchicalSymmetricVersion;
    var _ := itemExpectations(lastActive?.Item, timestamp, unModeledAttri);
    var _ :- expect keyStore.GetActiveBranchKey(KeyStoreTypes.GetActiveBranchKeyInput(branchKeyIdentifier := testId));
    // print testLogPrefix + " Active Validated with KMS/KeyStore: " + testId + "\n";

    var beaconInput := KeyStoreTypes.GetEncryptedBeaconKeyInput(Identifier:=testId);
    var beacon? :- expect storage.GetEncryptedBeaconKey(beaconInput);
    expect beacon?.Item.Type.ActiveHierarchicalSymmetricBeacon?;
    var _ := itemExpectations(beacon?.Item, timestamp, unModeledAttri);
    var _ :- expect keyStore.GetBeaconKey(KeyStoreTypes.GetBeaconKeyInput(branchKeyIdentifier := testId));
    // print testLogPrefix + " Beacon Validated with KMS/KeyStore: " + testId + "\n";
    var _ := CleanupItems.DeleteBranchKey(Identifier:=testId, ddbClient:=ddbClient);
  }

  method itemExpectations(
    item: KeyStoreTypes.EncryptedHierarchicalKey,
    timestamp : string,
    unModeledAttri : AdminFixtures.KeyValue
  )
    returns (output: bool)
    ensures output ==> "type" in item.EncryptionContext
  {
    expect
      customEC in item.EncryptionContext,
                  "Koda should be a Key in the Custom Encryption Context of all items for this test.";
    expect
      item.EncryptionContext[customEC] == timestamp,
      "Koda's value should be the test timestamp for all items for this test.";
    expect "type" in item.EncryptionContext, "item is missing 'type' from EC!!";
    expect unModeledAttri.key in item.EncryptionContext,
                                 "un-modeled attribute was dropped!";
    expect item.EncryptionContext[unModeledAttri.key] == unModeledAttri.value,
      "un-modeled attribute value is incorrect";
    return true;
  }
}
