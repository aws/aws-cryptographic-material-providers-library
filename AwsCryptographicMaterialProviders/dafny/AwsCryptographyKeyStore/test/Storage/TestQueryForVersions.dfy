// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../Fixtures.dfy"
include "../CleanupItems.dfy"

module {:options "/functionSyntax:4"} TestQueryForVersions {
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
  import Structure

  const ddbTableName: DDB.Types.TableName := Fixtures.branchKeyStoreName
  const logicalKeyStoreName := Fixtures.logicalKeyStoreName
  const happyCaseId := "test-query-for-versions"

  method {:test} TestHappyCase()
  {
    print " running";
    var ddbClient :- expect DDB.DynamoDBClient();
    var underTest :- expect Fixtures.DefaultStorage(ddbClient?:=Some(ddbClient));
    // TODO-Mutations-GA restore tests once done refactoring storage
    // var inputQuery: Types.QueryForVersionsInput;
    // var items: Types.EncryptedHierarchicalKeys;
    // var startKey: seq<UInt.uint8>;
    // var queryOut : Types.QueryForVersionsOutput;
    // var strStartKey: string;

    // inputQuery := Types.QueryForVersionsInput(
    //   Identifier := happyCaseId,
    //   PageSize := 2
    // );

    // var pageLimit := 3;
    // var pageIndex := 0;
    // var queryCount := 0;
    // while pageIndex < pageLimit
    // {

    //   print "\nTestQueryForVersions :: TestHappyCase :: pre-Query "
    //         + String.Base10Int2String(queryCount+1)  +
    //         " :: Input Start Key is None? :: " +
    //         (if inputQuery.ExclusiveStartKey.None? then "True" else "False")
    //         + "\n";
    //   assume {:axiom} underTest.Modifies == {}; // Turns off verification
    //   queryOut :- expect underTest.QueryForVersions(inputQuery);
    //   queryCount := queryCount + 1;
    //   items := queryOut.Items;
    //   startKey := queryOut.ExclusiveStartKey;
    //   strStartKey := "";

    //   if (|items| > 0) {
    //     expect
    //       |items| == 2,
    //       "Query returned items but not 2 of them? Size of items: " + String.Base10Int2String(|items|);
    //     var strItems: seq<string> := seq(|items|, (i: nat) requires i < |items| => items[i].EncryptionContext[Structure.TYPE_FIELD]);
    //     print "\nTestQueryForVersions :: TestHappyCase :: Query "
    //           + String.Base10Int2String(queryCount)  +  " :: Items :: "
    //           + strItems[0] + " , " + strItems[1] + "\n";
    //   }

    //   if (|startKey| > 0) {
    //     strStartKey :- expect UTF8.Decode(startKey);
    //     print "\nTestQueryForVersions :: TestHappyCase :: Query "
    //           + String.Base10Int2String(queryCount)  +  " :: Start Key :: " + strStartKey + "\n";
    //   } else {
    //     strStartKey := "";
    //     print "\nTestQueryForVersions :: TestHappyCase :: Query "
    //           + String.Base10Int2String(queryCount)  +  " :: Did not have a start key.\n";
    //     pageIndex := 10; // Short cut
    //   }

    //   inputQuery := Types.QueryForVersionsInput(
    //     Identifier := inputQuery.Identifier,
    //     PageSize := inputQuery.PageSize,
    //     ExclusiveStartKey := if |startKey| > 0 then Some(startKey) else None()
    //   );
    //   pageIndex := pageIndex + 1;
    // }

    // expect
    //   queryCount == 2,
    //   "It should have take 2 queries to fetch all versions, but it did not!";
    print "TestQueryForVersions.TestHappyCase: ";
  }
}
