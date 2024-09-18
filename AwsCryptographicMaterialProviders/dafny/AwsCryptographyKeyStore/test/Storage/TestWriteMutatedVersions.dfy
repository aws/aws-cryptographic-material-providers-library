// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../Fixtures.dfy"
include "../CleanupItems.dfy"

module {:options "/functionSyntax:4"} TestWriteMutatedVersions {
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
  const happyCaseId := "test-write-mutated-items"
  const original := Fixtures.ORIGINAL_BYTES
  const terminal := Fixtures.TERMINAL_BYTES

  method {:test} TestHappyCase()
  {
    print " running";
    // TODO-Mutations-GA restore tests once done refactoring storage
    // var ddbClient :- expect DDB.DynamoDBClient();
    // var underTest :- expect Fixtures.DefaultStorage(ddbClient?:=Some(ddbClient));
    // var uuid :- expect UUID.GenerateUUID();
    // var testId := happyCaseId + "-" + uuid;
    // CreateHappyCaseId(testId);

    // print "\nTestWriteMutatedVersions :: TestHappyCase :: Created the test items! testId: "
    //       + testId  +  "\n";
    // var inputQuery := Types.QueryForVersionsInput(
    //   Identifier := testId,
    //   PageSize := 24
    // );

    // var queryOut :- expect underTest.QueryForVersions(inputQuery);
    // var items := queryOut.Items;
    // expect
    //   |items| == 4,
    //   "Test expects there to be 4 Decrypt Only items! Found: " + String.Base10Int2String(|items|);
    // print "\nTestWriteMutatedVersions :: TestHappyCase :: Read the test items! testId: "
    //       + testId  +  "\n";

    // var timestamp :- expect Time.GetCurrentTimeStamp();
    // var mutatedItems: Types.EncryptedHierarchicalKeys := [];
    // var itemIndex := 0;
    // while itemIndex < |items|
    // {
    //   var item := items[itemIndex];
    //   expect
    //     "aws-crypto-ec:Robbie" in item.EncryptionContext,
    //                               "Robbie should be a Key in the Custom Encryption Context of all items for this test.";
    //   var temp := item.EncryptionContext["aws-crypto-ec:Robbie" := timestamp];
    //   expect Structure.BranchKeyContext?(temp);
    //   var newItem := Structure.ConstructEncryptedHierarchicalKey(temp, item.CiphertextBlob);
    //   mutatedItems := mutatedItems + [newItem];
    //   itemIndex := 1 + itemIndex;
    // }

    // var input := Types.WriteMutatedVersionsInput(
    //   Items := mutatedItems,
    //   Identifier := testId,
    //   Original := original,
    //   Terminal := terminal,
    //   CompleteMutation := false
    // );

    // var output :- expect underTest.WriteMutatedVersions(input);
    // print "\nTestWriteMutatedVersions :: TestHappyCase :: Wrote the \"mutated\" test items! testId: "
    //       + testId  +  "\n";

    // queryOut :- expect underTest.QueryForVersions(inputQuery);
    // items := queryOut.Items;
    // print "\nTestWriteMutatedVersions :: TestHappyCase :: Read the \"mutated\" test items! testId: "
    //       + testId  +  "\n";
    // itemIndex := 0;
    // while itemIndex < |items|
    // {
    //   var item := items[itemIndex];
    //   expect
    //     "aws-crypto-ec:Robbie" in item.EncryptionContext,
    //                               "Robbie should be a Key in the Custom Encryption Context of all items for this test.";
    //   expect
    //     item.EncryptionContext["aws-crypto-ec:Robbie"] == timestamp,
    //     "Robbie should be a Key in the Custom Encryption Context of all items for this test.";
    //   // This is a best effort
    //   expect Structure.TYPE_FIELD in item.EncryptionContext;
    //   var _ := CleanupItems.DeleteTypeWithFailure(testId, item.EncryptionContext[Structure.TYPE_FIELD], ddbClient);
    //   itemIndex := 1 + itemIndex;
    // }
    // expect
    //   itemIndex == 4,
    //   "There should have been 4 mutated items!";
    // print "\nTestWriteMutatedVersions :: TestHappyCase :: Validated and tried to delete the read \"mutated\" test items! testId: "
    //       + testId  +  "\n";
    // // This is all a best effort; let's hope we don't run out of UUIDs!
    // var _ := CleanupItems.DeleteTypeWithFailure(testId, Structure.BRANCH_KEY_ACTIVE_TYPE, ddbClient);
    // var _ := CleanupItems.DeleteTypeWithFailure(testId, Structure.BEACON_KEY_TYPE_VALUE, ddbClient);
    // var _ := CleanupItems.DeleteTypeWithFailure(testId, Structure.MUTATION_LOCK_TYPE, ddbClient);
    // print "\nTestWriteMutatedVersions :: TestHappyCase :: Tried to Delete the other items. testId: "
    //       + testId  +  "\n";
    // print "TestWriteMutatedVersions.TestHappyCase: ";
  }

  // method CreateHappyCaseId(
  //   id: string,
  //   ddbClient?: Option<DDB.Types.IDynamoDBClient> := None
  // )
  //   requires ddbClient?.Some? ==> ddbClient?.value.ValidState()
  //   modifies (if ddbClient?.Some? then ddbClient?.value.Modifies else {})
  //   ensures ddbClient?.Some? ==> ddbClient?.value.ValidState()
  // {
  //   var ddbClient :- expect Fixtures.ProvideDDBClient(ddbClient?);
  //   Fixtures.CreateHappyCaseId(id:=id, versionCount:=3);
  //   var item: DDB.Types.PutItemInputAttributeMap :=
  //     map[
  //       "type":=DDB.Types.AttributeValue.S(Structure.MUTATION_COMMITMENT_TYPE),
  //       Structure.HIERARCHY_VERSION := DDB.Types.AttributeValue.N("1"),
  //       Structure.BRANCH_KEY_IDENTIFIER_FIELD := DDB.Types.AttributeValue.S(id),
  //       Structure.KEY_CREATE_TIME :=  DDB.Types.AttributeValue.S("now!"),
  //       Structure.M_UUID := DDB.Types.AttributeValue.S("this-is-not-a-uuid-but-storage-does-not-validate-this"),
  //       Structure.M_ORIGINAL := DDB.Types.AttributeValue.B(UTF8.EncodeAscii("storage-does-not-validate-original-only-that-is-binary")),
  //       Structure.M_TERMINAL := DDB.Types.AttributeValue.B(UTF8.EncodeAscii("storage-does-not-validate-terminal-only-that-is-binary")),
  //       Structure.ENC_FIELD := DDB.Types.AttributeValue.B(UTF8.EncodeAscii("storage-does-not-validate-enc-only-that-is-binary"))
  //     ];
  //   var inputPut := DDB.Types.PutItemInput(TableName := ddbTableName, Item := item);
  //   var _ :- expect ddbClient.PutItem(inputPut);
  // }

}
