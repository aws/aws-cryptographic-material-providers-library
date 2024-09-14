// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../Fixtures.dfy"
include "../CleanupItems.dfy"
include "TestGetItemsForInitializeMutation.dfy"

/** Tests WriteItemsForInitializeMutation and WriteCompleteMutation */
module {:options "/functionSyntax:4"} TestWriteAndDeleteMutationLock {
  import UInt = Fixtures.UInt
  import Types = Fixtures.Types
  import UTF8 = Fixtures.UTF8
  import opened Wrappers
  import DefaultEncryptedKeyStore
  import DDB = Types.ComAmazonawsDynamodbTypes
  import Fixtures
  import Structure
  import DDBOperations = Com.Amazonaws.Dynamodb
  import KMSOperations = Com.Amazonaws.Kms
  import KeyStore
  import TestGetItemsForInitializeMutation
  import Time
  import CleanupItems

  const ddbTableName: DDB.TableName := Fixtures.branchKeyStoreName
  const logicalKeyStoreName := Fixtures.logicalKeyStoreName
  // The Key Store will consider this mutation lock invalid
  // The Storage layer will not.
  const alreadyLocked := TestGetItemsForInitializeMutation.mLockedId //"test-get-items-for-initialize-mutation"
  const happyCaseId := "test-write-and-delete-m-lock"
  const happyCaseVersion := "ced9948e-fd0c-46e9-98a0-e774649e3844"
  // const happyCaseVersion := "b5cb82e2-87cc-4fdf-9b21-99da3511f20f"

  /** Happy Case :: No Lock exists. Decryt Only, Active, Beacon, & lock are "storage-valid".*/
  /** Lock is successfully written and then removed */
  method {:test} TestHappyCase()
  {
    print " running";
    var ddbClient :- expect DDBOperations.DynamoDBClient();
    var underTest :- expect Fixtures.defaultStorage(ddbClient?:=Some(ddbClient));
    var allThree :- expect Fixtures.getItems(id:=happyCaseId, version:=happyCaseVersion, underTest:=underTest);

    // Because the new Version is written with "BRANCH_KEY_NOT_EXIST // The new Decryt Only MUST not exist"
    // We need to create a new Version
    // Or... we can delete the current one we just read... and trust that we will recreate it!
    var cleanedVersion? :- expect CleanupItems.DeleteTypeWithFailure(
      happyCaseId, Structure.BRANCH_KEY_TYPE_PREFIX + happyCaseVersion, ddbClient);

    // If you ever need to remove the lock manually
    // var cleanedVersion? :- expect CleanupItems.DeleteTypeWithFailure(happyCaseId, "MUTATION_LOCK", ddbClient);

    var timestamp :- expect Time.GetCurrentTimeStamp();
    var mLock := Types.MutationLock(
      Identifier := happyCaseId,
      CreateTime := timestamp,
      UUID := "not-a-real-uuid-but-storage-does-not-care",
      Original := UTF8.EncodeAscii("storage-does-not-validate-original-only-that-is-binary"),
      Terminal := UTF8.EncodeAscii("storage-does-not-validate-terminal-only-that-is-binary")
    );

    var inputInit := Types.WriteItemsForInitializeMutationInput(
      active := allThree.active,
      oldActive := allThree.active,
      version := allThree.decrypt,
      beacon := allThree.beacon,
      mutationLock := mLock
    );

    var writeInit :- expect underTest.WriteItemsForInitializeMutation(inputInit);

    print "\nTestWriteAndDeleteMutationLock :: TestHappyCase :: WriteInit PASS\n";

    var inputComplete := Types.WriteCompleteMutationInput(
      Identifier := happyCaseId,
      Original := mLock.Original,
      Terminal := mLock.Terminal
    );

    var writeCompl :- expect underTest.WriteCompleteMutation(inputComplete);

    print "\nTestWriteAndDeleteMutationLock :: TestHappyCase :: WriteComplete PASS\n";
    // This last print makes the Dafny Test runner look normal for this module
    print "TestWriteAndDeleteMutationLock.TestHappyCase: ";
  }

}
