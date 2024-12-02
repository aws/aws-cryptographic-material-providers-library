// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../../src/Index.dfy"
include "../../../AwsCryptographyKeyStore/test/CleanupItems.dfy"
include "../../../AwsCryptographyKeyStore/test/Fixtures.dfy"
include "../../../AwsCryptographyKeyStore/Model/AwsCryptographyKeyStoreTypes.dfy"
include "../AdminFixtures.dfy"

// Tests that un-Modeled Encryption Context is Usable by:
// - Creating a Branch Key
// - "Manually" modifying the Branch Key's Beacon, ACTIVE, & only Version to have an un-modeled value
// - Use the Key Store to retrieve these Items normally
// If the Key Store retrievals are successful,
// the Items are useable
module {:options "/functionSyntax:4" } TestUnModeledEncryptionContextIsUsable {
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

  const happyCaseId := "test-un-modeled-encryption-context-is-usable"
  const customEC := "aws-crypto-ec:Koda"
  const kmsId: string := Fixtures.keyArn
  const physicalName: string := Fixtures.branchKeyStoreName
  const logicalName: string := Fixtures.logicalKeyStoreName
  const testLogPrefix := "\nTestUnModeledEncryptionContextIsUsable :: TestHappyCase? :: "

  method {:test} TestHappyCase()
  {
    // print " running";

    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var storage :- expect Fixtures.DefaultStorage(ddbClient?:=Some(ddbClient));
    var keyStore :- expect Fixtures.DefaultKeyStore(ddbClient?:=Some(ddbClient), kmsClient?:=Some(kmsClient));
    var strategy :- expect AdminFixtures.DefaultKeyManagerStrategy(kmsClient?:=Some(kmsClient));

    var uuid :- expect UUID.GenerateUUID();
    var testId := happyCaseId + "-" + uuid;

    var kodaBytes :- expect UTF8.Encode("Koda");
    var isADogBytes :- expect UTF8.Encode("is a dog.");
    var originalEC := map[kodaBytes := isADogBytes];
    Fixtures.CreateHappyCaseId(id:=testId, versionCount:=0, customEC:=originalEC);

    // print testLogPrefix + " Created the legit test items with 1 versions! testId: " + testId + "\n";

    var _ :- expect AdminFixtures.AddAttributeWithoutLibrary(id:=testId, alsoViolateBeacon? := true, ddbClient? := Some(ddbClient));

    // print testLogPrefix + " Violated all three. testId: " + testId + "\n";

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
      expect "type" in item.EncryptionContext, "Decrypt Only item is missing 'type' from EC!!";
      expect
        item.Type.HierarchicalSymmetricVersion?,
        "Query for Decrypt Only returned a non-Decrypt Only!";

      if ("Robbie" in item.EncryptionContext) {
        // print testLogPrefix + "Robbie in " + item.EncryptionContext["type"] + "\n";
      }
      var versionUUID := item.Type.HierarchicalSymmetricVersion.Version;
      inputV := KeyStoreTypes.GetBranchKeyVersionInput(
        branchKeyIdentifier := testId,
        branchKeyVersion := versionUUID
      );
      var _ :- expect keyStore.GetBranchKeyVersion(inputV);

      // print testLogPrefix + " Validated Decrypt Only and tried to clean it up: " + item.EncryptionContext["type"] + "\n";
      itemIndex := 1 + itemIndex;
    }

    var lastActiveInput := KeyStoreTypes.GetEncryptedActiveBranchKeyInput(Identifier:=testId);
    var lastActive? :- expect storage.GetEncryptedActiveBranchKey(lastActiveInput);
    expect lastActive?.Item.Type.ActiveHierarchicalSymmetricVersion?;
    var lastActive := lastActive?.Item.Type.ActiveHierarchicalSymmetricVersion;

    var _ :- expect keyStore.GetActiveBranchKey(KeyStoreTypes.GetActiveBranchKeyInput(branchKeyIdentifier := testId));
    // print testLogPrefix + " Active Validated with KMS/KeyStore: " + testId + "\n";

    var beaconInput := KeyStoreTypes.GetEncryptedBeaconKeyInput(Identifier:=testId);
    var beacon? :- expect storage.GetEncryptedBeaconKey(beaconInput);
    expect beacon?.Item.Type.ActiveHierarchicalSymmetricBeacon?;

    var _ :- expect keyStore.GetBeaconKey(KeyStoreTypes.GetBeaconKeyInput(branchKeyIdentifier := testId));
    // print testLogPrefix + " Beacon Validated with KMS/KeyStore: " + testId + "\n";
    var _ := CleanupItems.DeleteBranchKey(Identifier:=testId, ddbClient:=ddbClient);
  }
}
