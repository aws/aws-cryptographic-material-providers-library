// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/Index.dfy"
include "Fixtures.dfy"

module CleanupItems {
  import DDB = Com.Amazonaws.Dynamodb
  import opened Wrappers
  import opened Fixtures
  import Structure
  import UTF8

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

  method DeleteBranchKeyWithOneVersion(
    Identifier: string,
    ddbClient: DDB.Types.IDynamoDBClient,
    tableName: string := branchKeyStoreName
  )
    returns (output: Result<bool, DDB.Types.Error>)
    requires
      && ddbClient.ValidState()
      && DDB.Types.IsValid_TableName(tableName)
      && UTF8.IsASCIIString(tableName)
    modifies ddbClient.Modifies
    ensures ddbClient.ValidState()
  {
    var storage :- expect Fixtures.DefaultStorage(
      physicalName := tableName,
      logicalName := tableName,
      ddbClient?:=Some(ddbClient));
    var lastActiveInput := Types.GetEncryptedActiveBranchKeyInput(Identifier:=Identifier);
    var lastActive? :- expect storage.GetEncryptedActiveBranchKey(lastActiveInput);
    expect lastActive?.Item.Type.ActiveHierarchicalSymmetricVersion?;
    var lastActive := lastActive?.Item.Type.ActiveHierarchicalSymmetricVersion.Version;
    var _ := DeleteTypeWithFailure(Identifier, Structure.BRANCH_KEY_ACTIVE_TYPE, ddbClient);
    var _ := DeleteTypeWithFailure(Identifier, Structure.BEACON_KEY_TYPE_VALUE, ddbClient);
    var _ := DeleteTypeWithFailure(Identifier, Structure.MUTATION_COMMITMENT_TYPE, ddbClient);
    var _ := DeleteTypeWithFailure(Identifier, Structure.MUTATION_INDEX_TYPE, ddbClient);
    var _ := DeleteTypeWithFailure(Identifier, Structure.BRANCH_KEY_TYPE_PREFIX + lastActive, ddbClient);
    return Success(true);
  }

}
