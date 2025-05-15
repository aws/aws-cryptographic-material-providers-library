// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/Index.dfy"
include "Fixtures.dfy"

module CleanupItems {
  import opened Wrappers
  import opened Fixtures
  import Seq
  import UTF8
  import DDB = Com.Amazonaws.Dynamodb
  import Structure

  method DeleteVersion(
    branchKeyIdentifier: string,
    branchKeyVersion: string,
    ddbClient: DDB.Types.IDynamoDBClient
  )
    requires ddbClient.ValidState()
    modifies ddbClient.Modifies
    ensures ddbClient.ValidState()
  {

    // This is a best effort to remove these items.
    var _ := ddbClient.DeleteItem(
      DDB.Types.DeleteItemInput(
        TableName := branchKeyStoreName,
        Key := map[
          Structure.BRANCH_KEY_IDENTIFIER_FIELD := DDB.Types.AttributeValue.S(branchKeyIdentifier),
          Structure.TYPE_FIELD := DDB.Types.AttributeValue.S(Structure.BRANCH_KEY_TYPE_PREFIX + branchKeyVersion)
        ]
      )
    );
  }

  method DeleteActive(
    branchKeyIdentifier: string,
    ddbClient: DDB.Types.IDynamoDBClient
  )
    requires ddbClient.ValidState()
    modifies ddbClient.Modifies
    ensures ddbClient.ValidState()
  {

    // This is a best effort to remove these items.
    var _ := ddbClient.DeleteItem(
      DDB.Types.DeleteItemInput(
        TableName := branchKeyStoreName,
        Key := map[
          Structure.BRANCH_KEY_IDENTIFIER_FIELD := DDB.Types.AttributeValue.S(branchKeyIdentifier),
          Structure.TYPE_FIELD := DDB.Types.AttributeValue.S(Structure.BRANCH_KEY_ACTIVE_TYPE)
        ]
      )
    );

    var _ := ddbClient.DeleteItem(
      DDB.Types.DeleteItemInput(
        TableName := branchKeyStoreName,
        Key := map[
          Structure.BRANCH_KEY_IDENTIFIER_FIELD := DDB.Types.AttributeValue.S(branchKeyIdentifier),
          Structure.TYPE_FIELD := DDB.Types.AttributeValue.S(Structure.BEACON_KEY_TYPE_VALUE)
        ]
      )
    );
  }

  method DeleteTypeWithFailure(
    branchKeyIdentifier: string,
    typeStr: string,
    ddbClient: DDB.Types.IDynamoDBClient
  )
    returns (output: Result<bool, DDB.Types.Error>)
    requires ddbClient.ValidState()
    modifies ddbClient.Modifies
    ensures ddbClient.ValidState()
  {
    var _ :- ddbClient.DeleteItem(
      DDB.Types.DeleteItemInput(
        TableName := branchKeyStoreName,
        Key := map[
          Structure.BRANCH_KEY_IDENTIFIER_FIELD := DDB.Types.AttributeValue.S(branchKeyIdentifier),
          Structure.TYPE_FIELD := DDB.Types.AttributeValue.S(typeStr)
        ]
      )
    );
    return Success(true);
  }

  const NOT_BK_ERR_MSG
    :=
    "NOT a DDB Internal Server Error, but an MPL Testing error."
    + " DDB query to gather and delete a BK returned a non-BK item."

  method DeleteBranchKey(
    nameonly Identifier: string,
    nameonly tableName: string := branchKeyStoreName,
    nameonly ddbClient: DDB.Types.IDynamoDBClient
  )
    returns (output: Result<bool, DDB.Types.Error>)
    requires
      && ddbClient.ValidState()
      && DDB.Types.IsValid_TableName(tableName)
    modifies ddbClient.Modifies
    ensures ddbClient.ValidState()
  {
    var ExpressionAttributeNames := map[
      "#pk" := Structure.BRANCH_KEY_IDENTIFIER_FIELD
    ];
    var ExpressionAttributeValues := map[
      ":pk" := DDB.Types.AttributeValue.S(Identifier)
    ];
    var queryReq := DDB.Types.QueryInput(
      TableName := tableName,
      KeyConditionExpression := Some("#pk = :pk"),
      ExpressionAttributeNames := Some(ExpressionAttributeNames),
      ExpressionAttributeValues := Some(ExpressionAttributeValues)
    );
    var queryRes :- ddbClient.Query(queryReq);
    if (queryRes.Items.None?) {
      return Success(true);
    }
    var deleteItems: seq<DDB.Types.TransactWriteItem> :- Seq.MapWithResult(
      (item: DDB.Types.AttributeMap)
      =>
        :- Need(
             Structure.TYPE_FIELD in item,
             DDB.Types.Error.InternalServerError(message := Some(NOT_BK_ERR_MSG))
           );
        Success(
          DDB.Types.TransactWriteItem(
            Delete := Some(
              DDB.Types.Delete(
                Key :=
                  map[
                    Structure.BRANCH_KEY_IDENTIFIER_FIELD := DDB.Types.AttributeValue.S(Identifier),
                    Structure.TYPE_FIELD := item[Structure.TYPE_FIELD]
                  ],
                TableName := tableName
              )))),
      queryRes.Items.value);

    if (0 == |deleteItems|) {
      return Success(true);
    }
    if (100 < |deleteItems|) {
      // eh, we are going to return false, and delete 100 items
      deleteItems := deleteItems[..100];
    }
    var deleteReq := DDB.Types.TransactWriteItemsInput(TransactItems := deleteItems);
    var _ :- ddbClient.TransactWriteItems(deleteReq);
    return Success(if 100 < |queryRes.Items.value| then false else true);
  }
}