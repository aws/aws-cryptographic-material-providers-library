// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../Fixtures.dfy"
include "../CleanupItems.dfy"
include "TestGetItemsForInitializeMutation.dfy"

/** Tests WriteInitializeMutation and WriteCompleteMutation */
module {:options "/functionSyntax:4"} TestWriteAndDeleteMutationLock {
  import UInt = Fixtures.UInt
  import Types = Fixtures.Types
  import UTF8 = Fixtures.UTF8
  import opened Wrappers
  import DefaultKeyStorageInterface
  import Fixtures
  import Structure
  import DDB = Com.Amazonaws.Dynamodb
  import KMS = Com.Amazonaws.Kms
  import KeyStore
  import TestGetItemsForInitializeMutation
  import Time
  import CleanupItems
  import UUID

  const ddbTableName: DDB.Types.TableName := Fixtures.branchKeyStoreName
  const logicalKeyStoreName := Fixtures.logicalKeyStoreName
  const happyCaseId := "test-write-and-delete-m-lock"
  const original := UTF8.EncodeAscii("storage-does-not-validate-original-only-that-is-binary")
  const terminal := UTF8.EncodeAscii("storage-does-not-validate-terminal-only-that-is-binary")
  const inputJson := UTF8.EncodeAscii("storage-does-not-validate-input-only-that-is-binary")
  const enc := UTF8.EncodeAscii("storage-does-not-validate-enc-only-that-is-binary")
  const lock_uuid := "not-a-real-uuid-but-storage-does-not-care"

  /** Happy Case :: No Lock exists. Decryt Only, Active, Beacon, & lock are "storage-valid".*/
  /** Lock is successfully written and then removed */
  method {:test} TestHappyCase()
  {
    print " running";
    // TODO-Mutations-GA restore tests once done refactoring storage
    //   var uuid :- expect UUID.GenerateUUID();
    //   var testId := happyCaseId + "-" + uuid;
    //   print "\nTestWriteAndDeleteMutationLock :: TestHappyCase :: testId: " + testId + "\n";
    //   Fixtures.CreateHappyCaseId(id:=testId, versionCount:=0);
    //   print "\nTestWriteAndDeleteMutationLock :: TestHappyCase :: created Test Items: " + testId + "\n";
    //   var ddbClient :- expect Fixtures.ProvideDDBClient();
    //   var underTest :- expect Fixtures.DefaultStorage();


    //   var allThree? := Fixtures.getItems(id:=testId, underTest:=underTest);
    //   var allThree: Fixtures.allThree;
    //   if (allThree?.Success?) {
    //     allThree := allThree?.value;
    //   } else {
    //     expect false, "Could not retrieve testId";
    //   }
    //   print "\nTestWriteAndDeleteMutationLock :: TestHappyCase :: retrieved Test Items: " + testId + "\n";

    //   // Because the new Version is written with "BRANCH_KEY_NOT_EXIST // The new Decryt Only MUST not exist"
    //   // We need to create a new Version
    //   // Or... we can delete the current one we just read... and trust that we will recreate it!
    //   var decryptItem := allThree.decrypt;
    //   expect Structure.TYPE_FIELD in decryptItem.EncryptionContext;
    //   var cleanedVersion? :- expect CleanupItems.DeleteTypeWithFailure(
    //     testId, decryptItem.EncryptionContext[Structure.TYPE_FIELD], ddbClient);

    //   var timestamp :- expect Time.GetCurrentTimeStamp();
    //   var mLock := Types.MutationCommitment(
    //     Identifier := testId,
    //     CreateTime := timestamp,
    //     UUID := lock_uuid,
    //     Original := original,
    //     Terminal := terminal,
    //     Input := inputJson,
    //     CiphertextBlob := enc
    //   );

    //   var inputInit := Types.WriteInitializeMutationInput(
    //     Active := Some(Types.OverWriteEncryptedHierarchicalKey(Item:=allThree.active, Old:=allThree.active)),
    //     Version := Some(allThree.decrypt),
    //     Beacon := Types.OverWriteEncryptedHierarchicalKey(Item:=allThree.beacon, Old:=allThree.beacon),
    //     MutationCommitment := mLock,

    //   );

    //   var writeInit :- expect underTest.WriteInitializeMutation(inputInit);

    //   var actualLock :- expect Fixtures.GetItemFromDDB(id:=testId, typeStr:=Structure.MUTATION_LOCK_TYPE, ddbClient?:=Some(ddbClient));
    //   expect Structure.M_LOCK_ORIGINAL in actualLock;
    //   expect actualLock[Structure.M_LOCK_ORIGINAL] == DDB.Types.AttributeValue.B(original);
    //   expect Structure.M_LOCK_TERMINAL in actualLock;
    //   expect actualLock[Structure.M_LOCK_TERMINAL] == DDB.Types.AttributeValue.B(terminal);
    //   expect Structure.M_LOCK_UUID in actualLock;
    //   expect actualLock[Structure.M_LOCK_UUID] == DDB.Types.AttributeValue.S(lock_uuid);
    //   expect Structure.KEY_CREATE_TIME in actualLock;
    //   expect actualLock[Structure.KEY_CREATE_TIME] == DDB.Types.AttributeValue.S(timestamp);
    //   // Type and Identifier of M_LOCK are asserted by GetItemFromDDB

    //   print "\nTestWriteAndDeleteMutationLock :: TestHappyCase :: WriteInit PASS\n";

    //   var writeCompl := Types.WriteMutatedVersionsInput(
    //     Items := [],
    //     Identifier := testId,
    //     Original := original,
    //     Terminal := terminal,
    //     CompleteMutation := true
    //   );

    //   var output :- expect underTest.WriteMutatedVersions(writeCompl);

    //   var noLock? := Fixtures.GetItemFromDDB(id:=testId, typeStr:=Structure.MUTATION_LOCK_TYPE, ddbClient?:=Some(ddbClient));
    //   expect noLock?.Failure?, "Mutation Lock was not deleted!!";

    //   print "\nTestWriteAndDeleteMutationLock :: TestHappyCase :: WriteCompl PASS\n";
    //   // Clean up.
    //   var _ := CleanupItems.DeleteTypeWithFailure(testId, decryptItem.EncryptionContext[Structure.TYPE_FIELD], ddbClient);
    //   var _ := CleanupItems.DeleteTypeWithFailure(testId, Structure.BRANCH_KEY_ACTIVE_TYPE, ddbClient);
    //   var _ := CleanupItems.DeleteTypeWithFailure(testId, Structure.BEACON_KEY_TYPE_VALUE, ddbClient);
    //   var _ := CleanupItems.DeleteTypeWithFailure(testId, Structure.MUTATION_COMMITMENT_TYPE, ddbClient);
    //   var _ := CleanupItems.DeleteTypeWithFailure(testId, Structure.MUTATION_INDEX_TYPE, ddbClient);

    //   // This last print makes the Dafny Test runner look normal for this module
    //   print "TestWriteAndDeleteMutationLock.TestHappyCase: ";
  }

}
