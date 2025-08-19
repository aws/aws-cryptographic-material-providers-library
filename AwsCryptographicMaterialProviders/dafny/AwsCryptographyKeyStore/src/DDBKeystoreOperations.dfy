// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../Model/AwsCryptographyKeyStoreTypes.dfy"
include "Structure.dfy"
include "ErrorMessages.dfy"

module DDBKeystoreOperations {
  import opened Wrappers
  import opened UInt = StandardLibrary.UInt
  import opened StandardLibrary.MemoryMath
  import Seq
  import Types = AwsCryptographyKeyStoreTypes
  import DDB = ComAmazonawsDynamodbTypes
  import UTF8
  import Structure
  import ErrorMessages = KeyStoreErrorMessages

  const BRANCH_KEY_NOT_EXISTS_EXPRESSION_ATTRIBUTE_NAME := "#BranchKeyIdentifierField"
  const BRANCH_KEY_EXISTS_EXPRESSION_ATTRIBUTE_NAME := "#EncField"
  const BRANCH_KEY_EXISTS_EXPRESSION_ATTRIBUTE_VALUE_NAME := ":enc"
  const BRANCH_KEY_NOT_EXISTS_EXPRESSION_ATTRIBUTE_NAMES
    := map[
         BRANCH_KEY_NOT_EXISTS_EXPRESSION_ATTRIBUTE_NAME := Structure.BRANCH_KEY_IDENTIFIER_FIELD
       ]
  const BRANCH_KEY_EXISTS_EXPRESSION_ATTRIBUTE_NAMES
    := map[
         BRANCH_KEY_EXISTS_EXPRESSION_ATTRIBUTE_NAME := Structure.BRANCH_KEY_FIELD
       ]
  function method GetBranchKeyExistsAttributeValues(val : DDB.AttributeValue) : DDB.ExpressionAttributeValueMap
  {
    map[
      BRANCH_KEY_EXISTS_EXPRESSION_ATTRIBUTE_VALUE_NAME := val
    ]
  }
  const BRANCH_KEY_NOT_EXIST_CONDITION := "attribute_not_exists(" + BRANCH_KEY_NOT_EXISTS_EXPRESSION_ATTRIBUTE_NAME + ")"
  const BRANCH_KEY_EXISTS_CONDITION := BRANCH_KEY_EXISTS_EXPRESSION_ATTRIBUTE_NAME + " = " + BRANCH_KEY_EXISTS_EXPRESSION_ATTRIBUTE_VALUE_NAME

  method WriteNewKeyToStore(
    versionBranchKeyItem: Structure.VersionBranchKeyItem,
    activeBranchKeyItem: Structure.ActiveBranchKeyItem,
    beaconKeyItem: Structure.BeaconKeyItem,
    tableName: DDB.TableName,
    ddbClient: DDB.IDynamoDBClient
  )
    returns (output: Result<DDB.TransactWriteItemsOutput, Types.Error>)
    requires
      && activeBranchKeyItem[Structure.BRANCH_KEY_IDENTIFIER_FIELD]
      == versionBranchKeyItem[Structure.BRANCH_KEY_IDENTIFIER_FIELD]
      == beaconKeyItem[Structure.BRANCH_KEY_IDENTIFIER_FIELD]
      && activeBranchKeyItem[Structure.BRANCH_KEY_ACTIVE_VERSION_FIELD] == versionBranchKeyItem[Structure.TYPE_FIELD]
    requires ddbClient.ValidState()
    modifies ddbClient.Modifies
    ensures ddbClient.ValidState()

    ensures
      && |ddbClient.History.TransactWriteItems| == |old(ddbClient.History.TransactWriteItems)| + 1
      && DDB.TransactWriteItemsInput(
           TransactItems := [
             CreateTransactWritePutItemNotExist(versionBranchKeyItem, tableName),
             CreateTransactWritePutItemNotExist(activeBranchKeyItem, tableName),
             CreateTransactWritePutItemNotExist(beaconKeyItem, tableName)
           ],
           ReturnConsumedCapacity := None,
           ReturnItemCollectionMetrics := None,
           ClientRequestToken := None
         )
         == Seq.Last(ddbClient.History.TransactWriteItems).input
      && old(ddbClient.History.TransactWriteItems) < ddbClient.History.TransactWriteItems

    //= aws-encryption-sdk-specification/framework/branch-key-store.md#writing-branch-key-and-beacon-key-to-branch-key-store-table
    //= type=implication
    //# If DDB TransactWriteItems is successful, this operation MUST return a successful response containing no additional data.
    ensures output.Success? ==> Seq.Last(ddbClient.History.TransactWriteItems).output.Success?
    //= aws-encryption-sdk-specification/framework/branch-key-store.md#writing-branch-key-and-beacon-key-to-branch-key-store-table
    //= type=implication
    //# Otherwise, this operation MUST yield an error.
    ensures Seq.Last(ddbClient.History.TransactWriteItems).output.Failure? ==> output.Failure?

  {
    var items: DDB.TransactWriteItemList := [
      CreateTransactWritePutItemNotExist(versionBranchKeyItem, tableName),
      CreateTransactWritePutItemNotExist(activeBranchKeyItem, tableName),
      CreateTransactWritePutItemNotExist(beaconKeyItem, tableName)
    ];

    var transactRequest := DDB.TransactWriteItemsInput(
      TransactItems := items,
      ReturnConsumedCapacity := None,
      ReturnItemCollectionMetrics := None,
      ClientRequestToken := None
    );

    var maybeTransactWriteResponse := ddbClient.TransactWriteItems(transactRequest);
    var transactWriteItemsResponse :- maybeTransactWriteResponse
    .MapFailure(e => Types.ComAmazonawsDynamodb(ComAmazonawsDynamodb := e));

    output := Success(transactWriteItemsResponse);
  }

  method WriteNewBranchKeyVersionToKeystore(
    versionBranchKeyItem: Structure.VersionBranchKeyItem,
    activeBranchKeyItem: Structure.ActiveBranchKeyItem,
    tableName: DDB.TableName,
    ddbClient: DDB.IDynamoDBClient,
    enc : DDB.AttributeValue
  )
    returns (output: Result<DDB.TransactWriteItemsOutput, Types.Error>)
    requires
      && activeBranchKeyItem[Structure.BRANCH_KEY_IDENTIFIER_FIELD] == versionBranchKeyItem[Structure.BRANCH_KEY_IDENTIFIER_FIELD]
      && activeBranchKeyItem[Structure.BRANCH_KEY_ACTIVE_VERSION_FIELD] == versionBranchKeyItem[Structure.TYPE_FIELD]
    requires ddbClient.ValidState()
    modifies ddbClient.Modifies
    ensures ddbClient.ValidState()

    ensures
      && |ddbClient.History.TransactWriteItems| == |old(ddbClient.History.TransactWriteItems)| + 1
      && DDB.TransactWriteItemsInput(
           TransactItems := [
             CreateTransactWritePutItemNotExist(versionBranchKeyItem, tableName),
             CreateTransactWritePutItemExists(activeBranchKeyItem, tableName, enc)
           ],
           ReturnConsumedCapacity := None,
           ReturnItemCollectionMetrics := None,
           ClientRequestToken := None
         )
         == Seq.Last(ddbClient.History.TransactWriteItems).input

    ensures output.Success? ==> Seq.Last(ddbClient.History.TransactWriteItems).output.Success?
    ensures Seq.Last(ddbClient.History.TransactWriteItems).output.Failure? ==> output.Failure?

    ensures
      && old(ddbClient.History.TransactWriteItems) < ddbClient.History.TransactWriteItems
      && old(ddbClient.History.GetItem) == ddbClient.History.GetItem
  {
    var items: DDB.TransactWriteItemList := [
      CreateTransactWritePutItemNotExist(versionBranchKeyItem, tableName),
      CreateTransactWritePutItemExists(activeBranchKeyItem, tableName, enc)
    ];

    var transactRequest := DDB.TransactWriteItemsInput(
      TransactItems := items,
      ReturnConsumedCapacity := None,
      ReturnItemCollectionMetrics := None,
      ClientRequestToken := None
    );

    var maybeTransactWriteResponse := ddbClient.TransactWriteItems(transactRequest);
    var transactWriteItemsResponse :- maybeTransactWriteResponse
    .MapFailure(e => Types.ComAmazonawsDynamodb(ComAmazonawsDynamodb := e));

    output := Success(transactWriteItemsResponse);
  }


  method GetActiveBranchKeyItem(
    branchKeyIdentifier: string,
    tableName: DDB.TableName,
    ddbClient: DDB.IDynamoDBClient
  )
    returns (output: Result<Structure.ActiveBranchKeyItem, Types.Error>)
    requires DDB.IsValid_TableName(tableName)
    requires ddbClient.ValidState()
    modifies ddbClient.Modifies
    ensures ddbClient.ValidState()

    ensures
      //= aws-encryption-sdk-specification/framework/branch-key-store.md#versionkey
      //= type=implication
      //# VersionKey MUST first get the active version for the branch key from the keystore
      //# by calling AWS DDB `GetItem`
      //# using the `branch-key-id` as the Partition Key and `"branch:ACTIVE"` value as the Sort Key.
      && |ddbClient.History.GetItem| == |old(ddbClient.History.GetItem)| + 1
      && Seq.Last(ddbClient.History.GetItem).input.Key
         == map[
              Structure.BRANCH_KEY_IDENTIFIER_FIELD := DDB.AttributeValue.S(branchKeyIdentifier),
              Structure.TYPE_FIELD := DDB.AttributeValue.S(Structure.BRANCH_KEY_ACTIVE_TYPE)
            ]

    ensures output.Success?
            ==>
              && output.value[Structure.BRANCH_KEY_IDENTIFIER_FIELD].S == branchKeyIdentifier
              && Seq.Last(ddbClient.History.GetItem).output.Success?
              && Seq.Last(ddbClient.History.GetItem).output.value.Item.Some?
              && output == Success(Seq.Last(ddbClient.History.GetItem).output.value.Item.value)

    ensures
      && old(ddbClient.History.GetItem) < ddbClient.History.GetItem
      && old(ddbClient.History.TransactWriteItems) == ddbClient.History.TransactWriteItems

    ensures
      && |ddbClient.History.GetItem| == |old(ddbClient.History.GetItem)| + 1
      && Seq.Last(ddbClient.History.GetItem).output.Success?
      && Seq.Last(ddbClient.History.GetItem).output.value.Item.Some?
      && !Structure.ActiveBranchKeyItem?(Seq.Last(ddbClient.History.GetItem).output.value.Item.value)
      ==> output.Failure?
  {
    var dynamoDbKey: DDB.Key := map[
      Structure.BRANCH_KEY_IDENTIFIER_FIELD := DDB.AttributeValue.S(branchKeyIdentifier),
      Structure.TYPE_FIELD := DDB.AttributeValue.S(Structure.BRANCH_KEY_ACTIVE_TYPE)
    ];
    var ItemRequest := DDB.GetItemInput(
      Key := dynamoDbKey,
      TableName := tableName,
      AttributesToGet := None,
      ConsistentRead :=  None,
      ReturnConsumedCapacity := None,
      ProjectionExpression := None,
      ExpressionAttributeNames := None
    );

    var maybeGetItem := ddbClient.GetItem(ItemRequest);
    var getItemResponse :- maybeGetItem
    .MapFailure(e => Types.ComAmazonawsDynamodb(ComAmazonawsDynamodb := e));

    OptionalMapIsSafeBecauseItIsInMemory(getItemResponse.Item);
    :- Need(
      getItemResponse.Item.Some? && |getItemResponse.Item.value| as uint64 >= 1,
      Types.KeyStoreException( message := ErrorMessages.NO_CORRESPONDING_BRANCH_KEY)
    );

    :- Need(
      && Structure.ActiveBranchKeyItem?(getItemResponse.Item.value)
      && getItemResponse.Item.value[Structure.BRANCH_KEY_IDENTIFIER_FIELD].S == branchKeyIdentifier,
      Types.KeyStoreException( message := "Item found is not a valid active branch key.")
    );

    output := Success(getItemResponse.Item.value);
  }

  method GetVersionBranchKeyItem(
    branchKeyIdentifier: string,
    branchKeyVersion: string,
    tableName: DDB.TableName,
    ddbClient: DDB.IDynamoDBClient
  )
    returns (output: Result<Structure.VersionBranchKeyItem, Types.Error>)
    requires DDB.IsValid_TableName(tableName)
    requires ddbClient.ValidState()
    modifies ddbClient.Modifies
    ensures ddbClient.ValidState()

    ensures
      && |ddbClient.History.GetItem| == |old(ddbClient.History.GetItem)| + 1
      && Seq.Last(ddbClient.History.GetItem).input.Key
         == map[
              Structure.BRANCH_KEY_IDENTIFIER_FIELD := DDB.AttributeValue.S(branchKeyIdentifier),
              Structure.TYPE_FIELD := DDB.AttributeValue.S(Structure.BRANCH_KEY_TYPE_PREFIX + branchKeyVersion)
            ]

    ensures output.Success?
            ==>
              && output.value[Structure.BRANCH_KEY_IDENTIFIER_FIELD].S == branchKeyIdentifier
              && output.value[Structure.TYPE_FIELD].S == Structure.BRANCH_KEY_TYPE_PREFIX + branchKeyVersion
              && Seq.Last(ddbClient.History.GetItem).output.Success?
              && Seq.Last(ddbClient.History.GetItem).output.value.Item.Some?
              && output == Success(Seq.Last(ddbClient.History.GetItem).output.value.Item.value)

    ensures
      && |ddbClient.History.GetItem| == |old(ddbClient.History.GetItem)| + 1
      && Seq.Last(ddbClient.History.GetItem).output.Success?
      && Seq.Last(ddbClient.History.GetItem).output.value.Item.Some?
      && !Structure.VersionBranchKeyItem?(Seq.Last(ddbClient.History.GetItem).output.value.Item.value)
      ==> output.Failure?
  {
    var dynamoDbKey: DDB.Key := map[
      Structure.BRANCH_KEY_IDENTIFIER_FIELD := DDB.AttributeValue.S(branchKeyIdentifier),
      Structure.TYPE_FIELD := DDB.AttributeValue.S(Structure.BRANCH_KEY_TYPE_PREFIX + branchKeyVersion)
    ];
    var ItemRequest := DDB.GetItemInput(
      Key := dynamoDbKey,
      TableName := tableName,
      AttributesToGet := None,
      ConsistentRead :=  None,
      ReturnConsumedCapacity := None,
      ProjectionExpression := None,
      ExpressionAttributeNames := None
    );

    var maybeGetItem := ddbClient.GetItem(ItemRequest);
    var getItemResponse :- maybeGetItem
    .MapFailure(e => Types.ComAmazonawsDynamodb(ComAmazonawsDynamodb := e));

    OptionalMapIsSafeBecauseItIsInMemory(getItemResponse.Item);
    :- Need(
      getItemResponse.Item.Some? && |getItemResponse.Item.value| as uint64  >= 1,
      Types.KeyStoreException( message := ErrorMessages.NO_CORRESPONDING_BRANCH_KEY)
    );

    :- Need(
      && Structure.VersionBranchKeyItem?(getItemResponse.Item.value)
      && getItemResponse.Item.value[Structure.BRANCH_KEY_IDENTIFIER_FIELD].S == branchKeyIdentifier
      && getItemResponse.Item.value[Structure.TYPE_FIELD].S == Structure.BRANCH_KEY_TYPE_PREFIX + branchKeyVersion,
      Types.KeyStoreException( message := "Item found is not a valid branch key version.")
    );

    output := Success(getItemResponse.Item.value);
  }

  method GetBeaconKeyItem(
    branchKeyIdentifier: string,
    tableName: DDB.TableName,
    ddbClient: DDB.IDynamoDBClient
  )
    returns (output: Result<Structure.BeaconKeyItem, Types.Error>)
    requires DDB.IsValid_TableName(tableName)
    requires ddbClient.ValidState()
    modifies ddbClient.Modifies
    ensures ddbClient.ValidState()
    ensures output.Success?
            ==>
              output.value[Structure.BRANCH_KEY_IDENTIFIER_FIELD].S == branchKeyIdentifier

    ensures
      && |ddbClient.History.GetItem| == |old(ddbClient.History.GetItem)| + 1
      && Seq.Last(ddbClient.History.GetItem).input.Key
         == map[
              Structure.BRANCH_KEY_IDENTIFIER_FIELD := DDB.AttributeValue.S(branchKeyIdentifier),
              Structure.TYPE_FIELD := DDB.AttributeValue.S(Structure.BEACON_KEY_TYPE_VALUE)
            ]

    ensures output.Success?
            ==>
              && output.value[Structure.BRANCH_KEY_IDENTIFIER_FIELD].S == branchKeyIdentifier
              && output.value[Structure.TYPE_FIELD].S == Structure.BEACON_KEY_TYPE_VALUE
              && Seq.Last(ddbClient.History.GetItem).output.Success?
              && Seq.Last(ddbClient.History.GetItem).output.value.Item.Some?
              && output == Success(Seq.Last(ddbClient.History.GetItem).output.value.Item.value)

    ensures
      && |ddbClient.History.GetItem| == |old(ddbClient.History.GetItem)| + 1
      && Seq.Last(ddbClient.History.GetItem).output.Success?
      && Seq.Last(ddbClient.History.GetItem).output.value.Item.Some?
      && !Structure.BeaconKeyItem?(Seq.Last(ddbClient.History.GetItem).output.value.Item.value)
      ==> output.Failure?
  {
    var dynamoDbKey: DDB.Key := map[
      Structure.BRANCH_KEY_IDENTIFIER_FIELD := DDB.AttributeValue.S(branchKeyIdentifier),
      Structure.TYPE_FIELD := DDB.AttributeValue.S(Structure.BEACON_KEY_TYPE_VALUE)
    ];
    var ItemRequest := DDB.GetItemInput(
      Key := dynamoDbKey,
      TableName := tableName,
      AttributesToGet := None,
      ConsistentRead :=  None,
      ReturnConsumedCapacity := None,
      ProjectionExpression := None,
      ExpressionAttributeNames := None
    );

    var maybeGetItem := ddbClient.GetItem(ItemRequest);
    var getItemResponse :- maybeGetItem
    .MapFailure(e => Types.ComAmazonawsDynamodb(ComAmazonawsDynamodb := e));

    OptionalMapIsSafeBecauseItIsInMemory(getItemResponse.Item);
    :- Need(
      getItemResponse.Item.Some? && |getItemResponse.Item.value| as uint64 >= 1,
      Types.KeyStoreException( message := ErrorMessages.NO_CORRESPONDING_BRANCH_KEY)
    );

    :- Need(
      && Structure.BeaconKeyItem?(getItemResponse.Item.value)
      && getItemResponse.Item.value[Structure.BRANCH_KEY_IDENTIFIER_FIELD].S == branchKeyIdentifier,
      Types.KeyStoreException( message := "Item found is not a valid beacon key.")
    );

    output := Success(getItemResponse.Item.value);
  }

  function method CreateTransactWritePutItemNotExist(
    item: DDB.AttributeMap,
    tableName: DDB.TableName
  ): (output: DDB.TransactWriteItem)
  {

    DDB.TransactWriteItem(
      ConditionCheck := None,
      Put := Some(
        DDB.Put(
          Item := item,
          TableName := tableName,
          ConditionExpression := Some(BRANCH_KEY_NOT_EXIST_CONDITION),
          ExpressionAttributeNames := Some(BRANCH_KEY_NOT_EXISTS_EXPRESSION_ATTRIBUTE_NAMES),
          ExpressionAttributeValues := None,
          ReturnValuesOnConditionCheckFailure := None)),
      Delete := None,
      Update := None
    )
  }
  function method CreateTransactWritePutItemExists(
    item: DDB.AttributeMap,
    tableName: DDB.TableName,
    enc : DDB.AttributeValue
  ): (output: DDB.TransactWriteItem)
  {

    DDB.TransactWriteItem(
      ConditionCheck := None,
      Put := Some(
        DDB.Put(
          Item := item,
          TableName := tableName,
          ConditionExpression := Some(BRANCH_KEY_EXISTS_CONDITION),
          ExpressionAttributeNames := Some(BRANCH_KEY_EXISTS_EXPRESSION_ATTRIBUTE_NAMES),
          ExpressionAttributeValues := Some(GetBranchKeyExistsAttributeValues(enc)),
          ReturnValuesOnConditionCheckFailure := None)),
      Delete := None,
      Update := None
    )
  }

}
