// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../Fixtures.dfy"
include "../CleanupItems.dfy"

module {:options "/functionSyntax:4"} TestWriteAtomicMutation {
  import Fixtures
  import UInt = Fixtures.UInt
  import Types = Fixtures.Types
  import UTF8 = Fixtures.UTF8
  import DDB = Com.Amazonaws.Dynamodb
  import KMS = Com.Amazonaws.Kms
  import Time
  import CleanupItems
  import opened Wrappers
  import String = StandardLibrary.String
  import opened Seq
  import Structure
  import KeyStore
  import UUID

  const ddbTableName: DDB.Types.TableName := Fixtures.branchKeyStoreName
  const logicalKeyStoreName := Fixtures.logicalKeyStoreName
  const happyCaseId := "test-write-atomic-mutation"

  method {:test} TestHappyCaseMutate()
  {
    // print " running";
    var ddbClient :- expect DDB.DynamoDBClient();
    var underTest :- expect Fixtures.DefaultStorage(ddbClient?:=Some(ddbClient));
    var uuid :- expect UUID.GenerateUUID();
    var testId := happyCaseId + "-mutate-version-" + uuid;

    // Create initial test data
    CreateHappyCaseId(testId);
    // print "\nTestWriteAtomicMutation :: TestHappyCaseMutate :: Created the test items! testId: " + testId + "\n";

    // Get all three items (active, beacon, decrypt)
    var activeInput := Types.GetEncryptedActiveBranchKeyInput(
      Identifier := testId
    );
    var active? :- expect underTest.GetEncryptedActiveBranchKey(activeInput);
    var active := active?.Item;

    var beaconInput := Types.GetEncryptedBeaconKeyInput(
      Identifier := testId
    );
    var beacon? :- expect underTest.GetEncryptedBeaconKey(beaconInput);
    var beacon := beacon?.Item;

    // we retrieved Active version becuase we are only Mutating the version.
    expect active.Type.ActiveHierarchicalSymmetricVersion?;
    var decryptInput := Types.GetEncryptedBranchKeyVersionInput(
      Identifier := testId,
      Version := active.Type.ActiveHierarchicalSymmetricVersion.Version
    );
    var decrypt? :- expect underTest.GetEncryptedBranchKeyVersion(decryptInput);
    var decrypt := decrypt?.Item;
    // print "\nTestWriteAtomicMutation :: TestHappyCaseMutate :: Retrieved test items! testId: " + testId + "\n";

    // Create modified versions with custom EC "aws-crypto-ec:Robbie":timestamp
    var timestamp :- expect Time.GetCurrentTimeStamp();

    // Modify Active key
    var newActiveEC := active.EncryptionContext;
    expect
      "aws-crypto-ec:Robbie" in newActiveEC
      && newActiveEC["aws-crypto-ec:Robbie"] == "Is a dog.",
      "Robbie should be a Key in the Custom Encryption Context";
    newActiveEC := newActiveEC["aws-crypto-ec:Robbie" := timestamp];
    expect Structure.BranchKeyContext?(newActiveEC);
    var newActive := Structure.ConstructEncryptedHierarchicalKey(newActiveEC, active.CiphertextBlob);
    var activeOverwrite := Types.OverWriteEncryptedHierarchicalKey(
      Item := newActive,
      Old := active
    );

    // Modify Beacon key
    var newBeaconEC := beacon.EncryptionContext;
    expect
      "aws-crypto-ec:Robbie" in newBeaconEC
      && newBeaconEC["aws-crypto-ec:Robbie"] == "Is a dog.",
      "Robbie should be a Key in the Custom Encryption Context";
    newBeaconEC := newBeaconEC["aws-crypto-ec:Robbie" := timestamp];
    expect Structure.BranchKeyContext?(newBeaconEC);
    var newBeacon := Structure.ConstructEncryptedHierarchicalKey(newBeaconEC, beacon.CiphertextBlob);
    var beaconOverwrite := Types.OverWriteEncryptedHierarchicalKey(
      Item := newBeacon,
      Old := beacon
    );

    // Modify Version key
    var newDecryptEC := decrypt.EncryptionContext;
    expect
      "aws-crypto-ec:Robbie" in newDecryptEC &&
      newDecryptEC["aws-crypto-ec:Robbie"] == "Is a dog.",
      "Robbie should be a Key in the Custom Encryption Context";
    newDecryptEC := newDecryptEC["aws-crypto-ec:Robbie" := timestamp];
    expect Structure.BranchKeyContext?(newDecryptEC);
    var newDecrypt := Structure.ConstructEncryptedHierarchicalKey(newDecryptEC, decrypt.CiphertextBlob);
    var decryptOverwrite := Types.OverWriteEncryptedHierarchicalKey(
      Item := newDecrypt,
      Old := decrypt
    );

    // Query for Decrypt Only Versions
    var inputQuery := Types.QueryForVersionsInput(
      Identifier := testId,
      PageSize := 24
    );

    var queryOut :- expect underTest.QueryForVersions(inputQuery);
    var items := queryOut.Items;
    expect
      |items| == 6,
      "Test expects there to be 6 Decrypt Only items! Found: " + String.Base10Int2String(|items|);
    // print "\nTestWriteAtomicMutation :: TestHappyCaseMutate :: Read the test items! testId: "
    //       + testId  +  "\n";

    // WriteAtomicMutation should handle Transaction request
    // to not include two write operations on active decrypt-only version
    var mutatedItems: Types.OverWriteEncryptedHierarchicalKeys := [];
    var itemIndex := 0;
    while itemIndex < |items|
    {
      var item := items[itemIndex];
      expect
        "aws-crypto-ec:Robbie" in item.EncryptionContext,
                                  "Robbie should be a Key in the Custom Encryption Context of all items for this test.";
      var temp := item.EncryptionContext["aws-crypto-ec:Robbie" := timestamp];
      expect Structure.BranchKeyContext?(temp);
      var newItem := Structure.ConstructEncryptedHierarchicalKey(temp, item.CiphertextBlob);
      var overWriteItem := Types.OverWriteEncryptedHierarchicalKey(
        Item:=newItem,
        Old:=item);
      mutatedItems := mutatedItems + [overWriteItem];
      itemIndex := 1 + itemIndex;
    }

    // Prepare and execute WriteAtomicMutation
    var input := Types.WriteAtomicMutationInput(
      Active := activeOverwrite,
      Version := Types.WriteInitializeMutationVersion.mutate(mutate := decryptOverwrite),
      Beacon := beaconOverwrite,
      Items := mutatedItems
    );

    var output :- expect underTest.WriteAtomicMutation(input);
    // print "\nTestWriteAtomicMutation :: TestHappyCaseMutate :: Executed atomic mutation! testId: " + testId + "\n";

    // Verify changes
    var verifyActive? :- expect underTest.GetEncryptedActiveBranchKey(
      Types.GetEncryptedActiveBranchKeyInput(Identifier := testId)
    );
    var verifyActiveEC := verifyActive?.Item.EncryptionContext;
    expect Structure.BranchKeyContext?(verifyActiveEC);
    expect "aws-crypto-ec:Robbie" in verifyActiveEC
           && verifyActiveEC["aws-crypto-ec:Robbie"] == timestamp,
           "Active key EC was not updated";

    var verifyBeacon? :- expect underTest.GetEncryptedBeaconKey(
      Types.GetEncryptedBeaconKeyInput(Identifier := testId)
    );
    var verifyBeaconEC := verifyBeacon?.Item.EncryptionContext;
    expect Structure.BranchKeyContext?(verifyBeaconEC);
    expect "aws-crypto-ec:Robbie" in verifyBeaconEC
           && verifyBeaconEC["aws-crypto-ec:Robbie"] == timestamp,
           "Beacon key EC was not updated";

    // Cleanup: Delete the branch key
    var _ := CleanupItems.DeleteBranchKey(Identifier:=testId, ddbClient:=ddbClient);
    // print "TestWriteAtomicMutation.TestHappyCaseMutate: ";
  }

  method {:test} TestHappyCaseRotate()
  {
    // print " running";
    var ddbClient :- expect DDB.DynamoDBClient();
    var underTest :- expect Fixtures.DefaultStorage(ddbClient?:=Some(ddbClient));
    var uuid :- expect UUID.GenerateUUID();
    var testId := happyCaseId + "-rotate-version-" + uuid;

    // Create initial test data
    CreateHappyCaseId(testId);
    // print "\nTestWriteAtomicMutation :: TestHappyCaseRotate :: Created the test items! testId: " + testId + "\n";

    // Get active and beacon items (we don't need decrypt for rotation)
    var activeInput := Types.GetEncryptedActiveBranchKeyInput(
      Identifier := testId
    );
    var active? :- expect underTest.GetEncryptedActiveBranchKey(activeInput);
    var active := active?.Item;

    var beaconInput := Types.GetEncryptedBeaconKeyInput(
      Identifier := testId
    );
    var beacon? :- expect underTest.GetEncryptedBeaconKey(beaconInput);
    var beacon := beacon?.Item;

    // print "\nTestWriteAtomicMutation :: TestHappyCaseRotate :: Retrieved test items! testId: " + testId + "\n";

    // Create modified versions with timestamp
    var timestamp :- expect Time.GetCurrentTimeStamp();

    // Construct the EC and Create new version for rotation
    var newVersionEC := map[
      Structure.BRANCH_KEY_IDENTIFIER_FIELD := active.Identifier,
      Structure.TYPE_FIELD:= Structure.BRANCH_KEY_TYPE_PREFIX + uuid,
      Structure.KEY_CREATE_TIME := timestamp,
      Structure.HIERARCHY_VERSION := Structure.HIERARCHY_VERSION_VALUE,
      Structure.KMS_FIELD := active.KmsArn,
      Structure.TABLE_FIELD := ddbTableName
    ];
    newVersionEC := newVersionEC["aws-crypto-ec:Robbie" := timestamp];
    expect Structure.BranchKeyContext?(newVersionEC);
    var newVersion := Structure.ConstructEncryptedHierarchicalKey(newVersionEC, active.CiphertextBlob);

    // Modify Active key
    var newActiveEC := active.EncryptionContext;
    expect "aws-crypto-ec:Robbie" in newActiveEC &&
           newActiveEC["aws-crypto-ec:Robbie"] == "Is a dog.", "Robbie should be a Key in the Custom Encryption Context";
    newActiveEC := newActiveEC["aws-crypto-ec:Robbie" := timestamp];
    newActiveEC := newActiveEC[Structure.BRANCH_KEY_ACTIVE_VERSION_FIELD := Structure.BRANCH_KEY_TYPE_PREFIX + uuid];
    expect Structure.BranchKeyContext?(newActiveEC);
    var newActive := Structure.ConstructEncryptedHierarchicalKey(newActiveEC, active.CiphertextBlob);
    var activeOverwrite := Types.OverWriteEncryptedHierarchicalKey(
      Item := newActive,
      Old := active
    );

    // Modify Beacon key
    var newBeaconEC := beacon.EncryptionContext;
    expect "aws-crypto-ec:Robbie" in newBeaconEC &&
           newBeaconEC["aws-crypto-ec:Robbie"] == "Is a dog.", "Robbie should be a Key in the Custom Encryption Context";
    newBeaconEC := newBeaconEC["aws-crypto-ec:Robbie" := timestamp];
    expect Structure.BranchKeyContext?(newBeaconEC);
    var newBeacon := Structure.ConstructEncryptedHierarchicalKey(newBeaconEC, beacon.CiphertextBlob);
    var beaconOverwrite := Types.OverWriteEncryptedHierarchicalKey(
      Item := newBeacon,
      Old := beacon
    );

    // Query for Decrypt Only Versions
    var inputQuery := Types.QueryForVersionsInput(
      Identifier := testId,
      PageSize := 24
    );

    var queryOut :- expect underTest.QueryForVersions(inputQuery);
    var items := queryOut.Items;
    expect
      |items| == 6,
      "Test expects there to be 6 Decrypt Only items! Found: " + String.Base10Int2String(|items|);
    // print "\nTestWriteAtomicMutation :: TestHappyCaseRotate :: Read the test items! testId: "
    //       + testId  +  "\n";

    // Modify EC for Decrypt Only Versions
    var mutatedItems: Types.OverWriteEncryptedHierarchicalKeys := [];
    var itemIndex := 0;
    while itemIndex < |items|
    {
      var item := items[itemIndex];
      expect
        "aws-crypto-ec:Robbie" in item.EncryptionContext,
                                  "Robbie should be a Key in the Custom Encryption Context of all items for this test.";
      var temp := item.EncryptionContext["aws-crypto-ec:Robbie" := timestamp];
      expect Structure.BranchKeyContext?(temp);
      var newItem := Structure.ConstructEncryptedHierarchicalKey(temp, item.CiphertextBlob);
      var overWriteItem := Types.OverWriteEncryptedHierarchicalKey(
        Item:=newItem,
        Old:=item);
      mutatedItems := mutatedItems + [overWriteItem];
      itemIndex := 1 + itemIndex;
    }

    // Prepare and execute WriteAtomicMutation with rotate
    var input := Types.WriteAtomicMutationInput(
      Active := activeOverwrite,
      Version := Types.WriteInitializeMutationVersion.rotate(rotate := newVersion),
      Beacon := beaconOverwrite,
      Items := mutatedItems
    );

    var output :- expect underTest.WriteAtomicMutation(input);
    // print "\nTestWriteAtomicMutation :: TestHappyCaseRotate :: Executed atomic mutation! testId: " + testId + "\n";

    // Verify changes
    var verifyActive? :- expect underTest.GetEncryptedActiveBranchKey(
      Types.GetEncryptedActiveBranchKeyInput(Identifier := testId)
    );
    var verifyActiveEC := verifyActive?.Item.EncryptionContext;
    expect "aws-crypto-ec:Robbie" in verifyActiveEC &&
           verifyActiveEC["aws-crypto-ec:Robbie"] == timestamp,
           "Active key EC was not updated";
    expect Structure.BRANCH_KEY_ACTIVE_VERSION_FIELD in verifyActiveEC &&
           verifyActiveEC[Structure.BRANCH_KEY_ACTIVE_VERSION_FIELD] == Structure.BRANCH_KEY_TYPE_PREFIX + uuid, "Active version should be " + Structure.BRANCH_KEY_TYPE_PREFIX + uuid;
    expect Structure.BranchKeyContext?(verifyActiveEC);
    var verifyBeacon? :- expect underTest.GetEncryptedBeaconKey(
      Types.GetEncryptedBeaconKeyInput(Identifier := testId)
    );

    var verifyBeaconEC := verifyBeacon?.Item.EncryptionContext;
    expect "aws-crypto-ec:Robbie" in verifyBeaconEC &&
           verifyBeaconEC["aws-crypto-ec:Robbie"] == timestamp,
           "Beacon key EC was not updated";
    expect Structure.BranchKeyContext?(verifyBeaconEC);

    // Verify new version was created
    var verifyVersion? :- expect underTest.GetEncryptedBranchKeyVersion(
      Types.GetEncryptedBranchKeyVersionInput(
        Identifier := testId,
        Version := uuid
      )
    );
    var verifyVersionEC := verifyVersion?.Item.EncryptionContext;
    expect Structure.BranchKeyContext?(verifyVersionEC);
    expect "aws-crypto-ec:Robbie" in verifyVersionEC
           && verifyVersionEC["aws-crypto-ec:Robbie"] == timestamp,
           "New version key EC was not set correctly";

    // Cleanup: Delete the branch key
    var _ := CleanupItems.DeleteBranchKey(Identifier:=testId, ddbClient:=ddbClient);
    // print "TestWriteAtomicMutation.TestHappyCaseRotate: ";
  }

  method CreateHappyCaseId(
    id: string,
    ddbClient?: Option<DDB.Types.IDynamoDBClient> := None
  )
    requires ddbClient?.Some? ==> ddbClient?.value.ValidState()
    modifies (if ddbClient?.Some? then ddbClient?.value.Modifies else {})
    ensures ddbClient?.Some? ==> ddbClient?.value.ValidState()
  {
    var ddbClient :- expect Fixtures.ProvideDDBClient(ddbClient?);
    Fixtures.CreateHappyCaseId(id:=id, versionCount:=5);
  }
}
