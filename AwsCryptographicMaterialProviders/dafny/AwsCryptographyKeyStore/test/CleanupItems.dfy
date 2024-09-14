// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/Index.dfy"
include "Fixtures.dfy"

module CleanupItems {
  import DDB = Com.Amazonaws.Dynamodb
  import opened Wrappers
  import opened Fixtures
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
        ],
        Expected := None,
        ConditionalOperator := None,
        ReturnValues := None,
        ReturnConsumedCapacity := None,
        ReturnItemCollectionMetrics := None,
        ConditionExpression := None,
        ExpressionAttributeNames := None,
        ExpressionAttributeValues := None

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
        ],
        Expected := None,
        ConditionalOperator := None,
        ReturnValues := None,
        ReturnConsumedCapacity := None,
        ReturnItemCollectionMetrics := None,
        ConditionExpression := None,
        ExpressionAttributeNames := None,
        ExpressionAttributeValues := None

      )
    );

    var _ := ddbClient.DeleteItem(
      DDB.Types.DeleteItemInput(
        TableName := branchKeyStoreName,
        Key := map[
          Structure.BRANCH_KEY_IDENTIFIER_FIELD := DDB.Types.AttributeValue.S(branchKeyIdentifier),
          Structure.TYPE_FIELD := DDB.Types.AttributeValue.S(Structure.BEACON_KEY_TYPE_VALUE)
        ],
        Expected := None,
        ConditionalOperator := None,
        ReturnValues := None,
        ReturnConsumedCapacity := None,
        ReturnItemCollectionMetrics := None,
        ConditionExpression := None,
        ExpressionAttributeNames := None,
        ExpressionAttributeValues := None

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


}
