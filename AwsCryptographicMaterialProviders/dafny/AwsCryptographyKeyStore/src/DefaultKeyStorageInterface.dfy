// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../Model/AwsCryptographyKeyStoreTypes.dfy"
include "Structure.dfy"
include "ErrorMessages.dfy"

module DefaultKeyStorageInterface {
  import opened Wrappers
  import ComAmazonawsDynamodbTypes
  import Seq
  import Types = AwsCryptographyKeyStoreTypes
  import DDB = ComAmazonawsDynamodbTypes
  import UTF8
  import Structure

  const ToAttributeMap := Structure.ToAttributeMap
  const ToEncryptedHierarchicalKey := Structure.ToEncryptedHierarchicalKey
  import ErrorMessages = KeyStoreErrorMessages

  const BRANCH_KEY_EXISTS_EXPRESSION_ATTRIBUTE_NAME := "#BranchKeyIdentifierField"
  const BRANCH_KEY_EXISTS_EXPRESSION_ATTRIBUTE_NAMES
    := map[
         BRANCH_KEY_EXISTS_EXPRESSION_ATTRIBUTE_NAME := Structure.BRANCH_KEY_IDENTIFIER_FIELD
       ]
  const BRANCH_KEY_NOT_EXIST_CONDITION := "attribute_not_exists(" + BRANCH_KEY_EXISTS_EXPRESSION_ATTRIBUTE_NAME + ")"
  const BRANCH_KEY_EXISTS_CONDITION := "attribute_exists(" + BRANCH_KEY_EXISTS_EXPRESSION_ATTRIBUTE_NAME + ")"

  datatype ConditionExpression =
    | BRANCH_KEY_NOT_EXIST
    | BRANCH_KEY_EXISTS

  class {:termination false} DynamoDBKeyStorageInterface
    //= aws-encryption-sdk-specification/framework/key-store/dynamodb-key-storage.md#operations
    //= type=implication
    //# The Dynamodb Key Storage Interface MUST implement the [key storage interface](./key-storage.md#interface).
    extends Types.IKeyStorageInterface
  {

    const ddbTableName: ComAmazonawsDynamodbTypes.TableName
    const ddbTableNameUtf8: UTF8.ValidUTF8Bytes
    const logicalKeyStoreName: string
    const logicalKeyStoreNameUtf8: UTF8.ValidUTF8Bytes
    const ddbClient: ComAmazonawsDynamodbTypes.IDynamoDBClient

    predicate ValidState()
      ensures ValidState() ==> History in Modifies
    {
      && History in Modifies
      && ddbClient.ValidState()
      && ddbClient.Modifies < Modifies
      && History !in ddbClient.Modifies
      && UTF8.Encode(ddbTableName).Success?
      && ddbTableNameUtf8 == UTF8.Encode(ddbTableName).value
      && UTF8.Encode(logicalKeyStoreName).Success?
      && logicalKeyStoreNameUtf8 == UTF8.Encode(logicalKeyStoreName).value
    }

    predicate WriteNewEncryptedBranchKeyEnsuresPublicly(
      input: Types.WriteNewEncryptedBranchKeyInput ,
      output: Result<Types.WriteNewEncryptedBranchKeyOutput, Types.Error>
    )
    {true}
    predicate WriteNewEncryptedBranchKeyVersionEnsuresPublicly(
      input: Types.WriteNewEncryptedBranchKeyVersionInput ,
      output: Result<Types.WriteNewEncryptedBranchKeyVersionOutput, Types.Error>
    )
    {true}

    predicate GetEncryptedActiveBranchKeyEnsuresPublicly(
      input: Types.GetEncryptedActiveBranchKeyInput ,
      output: Result<Types.GetEncryptedActiveBranchKeyOutput, Types.Error>
    )
    {
      && (output.Success? ==>
            //= aws-encryption-sdk-specification/framework/key-store/dynamodb-key-storage.md#getencryptedactivebranchkey
            //= type=implication
            //# The returned EncryptedHierarchicalKey MUST have the same identifier as the input.
            && output.value.Item.Identifier == input.Identifier
               //= aws-encryption-sdk-specification/framework/key-store/dynamodb-key-storage.md#getencryptedactivebranchkey
               //= type=implication
               //# The returned EncryptedHierarchicalKey MUST have a type of ActiveHierarchicalSymmetricVersion.
            && Structure.ActiveHierarchicalSymmetricKey?(output.value.Item)
               //= aws-encryption-sdk-specification/framework/key-store/dynamodb-key-storage.md#logical-keystore-name
               //= type=implication
               //# It is not stored on the items in the so it MUST be added
               //# to items retrieved from the table.
            && output.value.Item.EncryptionContext[Structure.TABLE_FIELD] == logicalKeyStoreName
      )
    }
    predicate GetEncryptedBranchKeyVersionEnsuresPublicly(
      input: Types.GetEncryptedBranchKeyVersionInput ,
      output: Result<Types.GetEncryptedBranchKeyVersionOutput, Types.Error>
    )
    {
      && (output.Success? ==>
            //= aws-encryption-sdk-specification/framework/key-store/dynamodb-key-storage.md#getencryptedbranchkeyversion
            //= type=implication
            //# The returned EncryptedHierarchicalKey MUST have the same identifier as the input.
            && output.value.Item.Identifier == input.Identifier
               //= aws-encryption-sdk-specification/framework/key-store/dynamodb-key-storage.md#getencryptedbranchkeyversion
               //= type=implication
               //# The returned EncryptedHierarchicalKey MUST have a type of HierarchicalSymmetricVersion.
            && Structure.DecryptOnlyHierarchicalSymmetricKey?(output.value.Item)
            && output.value.Item.Type == Types.HierarchicalSymmetricVersion(
                                           //= aws-encryption-sdk-specification/framework/key-store/dynamodb-key-storage.md#getencryptedbranchkeyversion
                                           //= type=implication
                                           //# The returned EncryptedHierarchicalKey MUST have the same version as the input.
                                           Types.HierarchicalSymmetric( Version := input.Version )
                                         )
               //= aws-encryption-sdk-specification/framework/key-store/dynamodb-key-storage.md#logical-keystore-name
               //= type=implication
               //# It is not stored on the items in the so it MUST be added
               //# to items retrieved from the table.
            && output.value.Item.EncryptionContext[Structure.TABLE_FIELD] == logicalKeyStoreName
      )


    }
    predicate GetEncryptedBeaconKeyEnsuresPublicly(
      input: Types.GetEncryptedBeaconKeyInput ,
      output: Result<Types.GetEncryptedBeaconKeyOutput, Types.Error>
    )
    {
      && (output.Success? ==>
            //= aws-encryption-sdk-specification/framework/key-store/dynamodb-key-storage.md#getencryptedbeaconkey
            //= type=implication
            //# The returned EncryptedHierarchicalKey MUST have the same identifier as the input.
            && output.value.Item.Identifier == input.Identifier
               //= aws-encryption-sdk-specification/framework/key-store/dynamodb-key-storage.md#getencryptedbeaconkey
               //= type=implication
               //# The returned EncryptedHierarchicalKey MUST have a type of ActiveHierarchicalSymmetricBeacon.
            && Structure.ActiveHierarchicalSymmetricBeaconKey?(output.value.Item)
               //= aws-encryption-sdk-specification/framework/key-store/dynamodb-key-storage.md#logical-keystore-name
               //= type=implication
               //# It is not stored on the items in the so it MUST be added
               //# to items retrieved from the table.
            && output.value.Item.EncryptionContext[Structure.TABLE_FIELD] == logicalKeyStoreName
      )
    }
    predicate GetKeyStorageInfoEnsuresPublicly(
      input: Types.GetKeyStorageInfoInput ,
      output: Result<Types.GetKeyStorageInfoOutput, Types.Error>
    )
    {true}

    //= aws-encryption-sdk-specification/framework/key-store/dynamodb-key-storage.md#initialization
    //= type=implication
    //# The following inputs MUST be specified to create a Dynamodb Key Storage Interface:
    //#
    //#- [DynamoDb Client](#dynamodb-client)
    //#- [Table Name](#table-name)
    //#- [Logical KeyStore Name](#logical-keystore-name)
    constructor (
      nameonly ddbTableName: ComAmazonawsDynamodbTypes.TableName ,
      nameonly ddbClient: ComAmazonawsDynamodbTypes.IDynamoDBClient,
      nameonly logicalKeyStoreName: string,
      nameonly ddbTableNameUtf8: UTF8.ValidUTF8Bytes,
      nameonly logicalKeyStoreNameUtf8: UTF8.ValidUTF8Bytes
    )
      requires ddbClient.ValidState()
      requires
        && UTF8.Encode(ddbTableName).Success?
        && UTF8.Encode(logicalKeyStoreName).Success?
        && ddbTableNameUtf8 == UTF8.Encode(ddbTableName).value
        && logicalKeyStoreNameUtf8 == UTF8.Encode(logicalKeyStoreName).value
      ensures
        && this.ddbClient == ddbClient
        && this.ddbTableName == ddbTableName
        && this.logicalKeyStoreName == logicalKeyStoreName
      ensures ValidState()

      ensures fresh(Modifies - ddbClient.Modifies)
    {
      History := new Types.IKeyStorageInterfaceCallHistory();
      Modifies := {History} + ddbClient.Modifies;

      this.ddbClient := ddbClient;
      this.ddbTableName := ddbTableName;
      this.logicalKeyStoreName := logicalKeyStoreName;
      this.ddbTableNameUtf8 := ddbTableNameUtf8;
      this.logicalKeyStoreNameUtf8 := logicalKeyStoreNameUtf8;
    }

    method WriteNewEncryptedBranchKey' ( input: Types.WriteNewEncryptedBranchKeyInput )
      returns (output: Result<Types.WriteNewEncryptedBranchKeyOutput, Types.Error>)
      requires
        && ValidState()
      modifies Modifies - {History}
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures WriteNewEncryptedBranchKeyEnsuresPublicly(input, output)
      ensures unchanged(History)

      ensures
        && (forall k <- input.Version.EncryptionContext.Keys :: DDB.IsValid_AttributeName(k))
        && (forall k <- input.Active.EncryptionContext.Keys :: DDB.IsValid_AttributeName(k))
        && (forall k <- input.Beacon.EncryptionContext.Keys :: DDB.IsValid_AttributeName(k))
        ==>
          //= aws-encryption-sdk-specification/framework/key-store/dynamodb-key-storage.md#writenewencryptedbranchkey
          //= type=implication
          //# The call to Amazon DynamoDB TransactWriteItems MUST use the configured Amazon DynamoDB Client to make the call.
          && |ddbClient.History.TransactWriteItems| == |old(ddbClient.History.TransactWriteItems)| + 1

      ensures
        output.Success?
        ==>
          && (forall k <- input.Version.EncryptionContext.Keys :: DDB.IsValid_AttributeName(k))
          && (forall k <- input.Active.EncryptionContext.Keys :: DDB.IsValid_AttributeName(k))
          && (forall k <- input.Beacon.EncryptionContext.Keys :: DDB.IsValid_AttributeName(k))

          //= aws-encryption-sdk-specification/framework/key-store/dynamodb-key-storage.md#writenewencryptedbranchkey
          //= type=implication
          //# To add the branch keys and a beacon key to the keystore the
          //# operation MUST call [Amazon DynamoDB API TransactWriteItems](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_TransactWriteItems.html).
          && Seq.Last(ddbClient.History.TransactWriteItems).input
             //= aws-encryption-sdk-specification/framework/key-store/dynamodb-key-storage.md#writenewencryptedbranchkey
             //= type=implication
             //# The operation MUST call Amazon DynamoDB TransactWriteItems with a request constructed as follows:
             == DDB.TransactWriteItemsInput(
                  TransactItems := [
                    //= aws-encryption-sdk-specification/framework/key-store/dynamodb-key-storage.md#writenewencryptedbranchkey
                    //= type=implication
                    //#- PUT:
                    //#  - Item: A [record formatted item](#record-format) constructed from the version input
                    //#  - ConditionExpression: `attribute_not_exists(branch-key-id)`
                    //#  - TableName: the configured Table Name
                    CreateTransactWritePutItem(
                      input.Version,
                      ddbTableName,
                      BRANCH_KEY_NOT_EXIST
                    ),
                    //= aws-encryption-sdk-specification/framework/key-store/dynamodb-key-storage.md#writenewencryptedbranchkey
                    //= type=implication
                    //#- PUT:
                    //#  - Item: A [record formatted item](#record-format) constructed from the active input
                    //#  - ConditionExpression: `attribute_not_exists(branch-key-id)`
                    //#  - TableName: the configured Table Name
                    CreateTransactWritePutItem(
                      input.Active,
                      ddbTableName,
                      BRANCH_KEY_NOT_EXIST
                    ),
                    //= aws-encryption-sdk-specification/framework/key-store/dynamodb-key-storage.md#writenewencryptedbranchkey
                    //= type=implication
                    //#- PUT:
                    //#  - Item: A [record formatted item](#record-format) constructed from the beacon input
                    //#  - ConditionExpression: `attribute_not_exists(branch-key-id)`
                    //#  - TableName is the configured Table Name
                    CreateTransactWritePutItem(
                      input.Beacon,
                      ddbTableName,
                      BRANCH_KEY_NOT_EXIST
                    )
                  ]
                )
          && old(ddbClient.History.TransactWriteItems) < ddbClient.History.TransactWriteItems

      //= aws-encryption-sdk-specification/framework/key-store/dynamodb-key-storage.md#writenewencryptedbranchkey
      //= type=implication
      //# If DDB TransactWriteItems is successful, this operation MUST return a successful response containing no additional data.
      ensures
        && (forall k <- input.Version.EncryptionContext.Keys :: DDB.IsValid_AttributeName(k))
        && (forall k <- input.Active.EncryptionContext.Keys :: DDB.IsValid_AttributeName(k))
        && (forall k <- input.Beacon.EncryptionContext.Keys :: DDB.IsValid_AttributeName(k))
        && Seq.Last(ddbClient.History.TransactWriteItems).output.Success?
        ==> output.Success?
      //= aws-encryption-sdk-specification/framework/key-store/dynamodb-key-storage.md#writenewencryptedbranchkey
      //= type=implication
      //# Otherwise, this operation MUST yield an error.
      ensures
        && (forall k <- input.Version.EncryptionContext.Keys :: DDB.IsValid_AttributeName(k))
        && (forall k <- input.Active.EncryptionContext.Keys :: DDB.IsValid_AttributeName(k))
        && (forall k <- input.Beacon.EncryptionContext.Keys :: DDB.IsValid_AttributeName(k))
        && Seq.Last(ddbClient.History.TransactWriteItems).output.Failure?
        ==> output.Failure?
    {

      :- Need(
        && (forall k <- input.Version.EncryptionContext.Keys :: DDB.IsValid_AttributeName(k))
        && (forall k <- input.Active.EncryptionContext.Keys :: DDB.IsValid_AttributeName(k))
        && (forall k <- input.Beacon.EncryptionContext.Keys :: DDB.IsValid_AttributeName(k))
      , Types.KeyStoreException( message := ErrorMessages.ENCRYPTION_CONTEXT_EXCEEDS_DDB_LIMIT)
      );

      var items: DDB.TransactWriteItemList := [
        CreateTransactWritePutItem(
          input.Version,
          ddbTableName,
          BRANCH_KEY_NOT_EXIST
        ),
        CreateTransactWritePutItem(
          input.Active,
          ddbTableName,
          BRANCH_KEY_NOT_EXIST
        ),
        CreateTransactWritePutItem(
          input.Beacon,
          ddbTableName,
          BRANCH_KEY_NOT_EXIST
        )
      ];

      var transactRequest := DDB.TransactWriteItemsInput(
        TransactItems := items,
        ReturnConsumedCapacity := None,
        ReturnItemCollectionMetrics := None,
        ClientRequestToken := None
      );

      var transactWriteItemsResponse? := ddbClient.TransactWriteItems(transactRequest);
      var _ :- transactWriteItemsResponse?
      .MapFailure(e => Types.ComAmazonawsDynamodb(ComAmazonawsDynamodb := e));

      output := Success(Types.WriteNewEncryptedBranchKeyOutput);
    }

    method WriteNewEncryptedBranchKeyVersion' ( input: Types.WriteNewEncryptedBranchKeyVersionInput )
      returns (output: Result<Types.WriteNewEncryptedBranchKeyVersionOutput, Types.Error>)
      requires
        && ValidState()
      modifies Modifies - {History}
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures WriteNewEncryptedBranchKeyVersionEnsuresPublicly(input, output)
      ensures unchanged(History)

      //= aws-encryption-sdk-specification/framework/key-store/dynamodb-key-storage.md#writenewencryptedbranchkeyversion
      //= type=implication
      //# The call to Amazon DynamoDB TransactWriteItems MUST use the configured Amazon DynamoDB Client to make the call.
      ensures
        && (forall k <- input.Version.EncryptionContext.Keys :: DDB.IsValid_AttributeName(k))
        && (forall k <- input.Active.EncryptionContext.Keys :: DDB.IsValid_AttributeName(k))
        ==>
          && |ddbClient.History.TransactWriteItems| == |old(ddbClient.History.TransactWriteItems)| + 1
          && old(ddbClient.History.TransactWriteItems) < ddbClient.History.TransactWriteItems
          && (output.Success? ==> Seq.Last(ddbClient.History.TransactWriteItems).output.Success?)
          && (Seq.Last(ddbClient.History.TransactWriteItems).output.Failure? ==> output.Failure?)

      ensures
        output.Success?
        ==>
          && (forall k <- input.Version.EncryptionContext.Keys :: DDB.IsValid_AttributeName(k))
          && (forall k <- input.Active.EncryptionContext.Keys :: DDB.IsValid_AttributeName(k))
             //= aws-encryption-sdk-specification/framework/key-store/dynamodb-key-storage.md#writenewencryptedbranchkeyversion
             //= type=implication
             //# To add the new branch key to the keystore,
             //# the operation MUST call [Amazon DynamoDB API TransactWriteItems](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_TransactWriteItems.html).
          && Seq.Last(ddbClient.History.TransactWriteItems).input
             //= aws-encryption-sdk-specification/framework/key-store/dynamodb-key-storage.md#writenewencryptedbranchkeyversion
             //= type=implication
             //# The operation MUST call Amazon DynamoDB TransactWriteItems with a request constructed as follows:
             == DDB.TransactWriteItemsInput(
                  TransactItems := [
                    //= aws-encryption-sdk-specification/framework/key-store/dynamodb-key-storage.md#writenewencryptedbranchkeyversion
                    //= type=implication
                    //#- PUT:
                    //#  - Item: A [record formatted item](#record-format) constructed from the version input
                    //#  - ConditionExpression: `attribute_not_exists(branch-key-id)`
                    //#  - TableName: the configured Table Name
                    CreateTransactWritePutItem(
                      input.Version,
                      ddbTableName,
                      BRANCH_KEY_NOT_EXIST
                    ),
                    //= aws-encryption-sdk-specification/framework/key-store/dynamodb-key-storage.md#writenewencryptedbranchkeyversion
                    //= type=implication
                    //#- PUT:
                    //#  - Item: A [record formatted item](#record-format) constructed from the active input
                    //#  - ConditionExpression: `attribute_exists(branch-key-id)`
                    //#  - TableName: the configured Table Name
                    CreateTransactWritePutItem(
                      input.Active,
                      ddbTableName,
                      BRANCH_KEY_EXISTS
                    )
                  ]
                )
    {

      :- Need(
        && (forall k <- input.Version.EncryptionContext.Keys :: DDB.IsValid_AttributeName(k))
        && (forall k <- input.Active.EncryptionContext.Keys :: DDB.IsValid_AttributeName(k))
      , Types.KeyStoreException( message := ErrorMessages.ENCRYPTION_CONTEXT_EXCEEDS_DDB_LIMIT)
      );

      var items: DDB.TransactWriteItemList := [
        CreateTransactWritePutItem(
          input.Version,
          ddbTableName,
          BRANCH_KEY_NOT_EXIST
        ),
        CreateTransactWritePutItem(
          input.Active,
          ddbTableName,
          BRANCH_KEY_EXISTS
        )
      ];

      var transactRequest := DDB.TransactWriteItemsInput(
        TransactItems := items,
        ReturnConsumedCapacity := None,
        ReturnItemCollectionMetrics := None,
        ClientRequestToken := None
      );

      var transactWriteItemsResponse? := ddbClient.TransactWriteItems(transactRequest);
      var _ :- transactWriteItemsResponse?
      .MapFailure(e => Types.ComAmazonawsDynamodb(ComAmazonawsDynamodb := e));

      output := Success(Types.WriteNewEncryptedBranchKeyVersionOutput);

    }

    method GetEncryptedActiveBranchKey' ( input: Types.GetEncryptedActiveBranchKeyInput )
      returns (output: Result<Types.GetEncryptedActiveBranchKeyOutput, Types.Error>)
      requires
        && ValidState()
      modifies Modifies - {History}
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures GetEncryptedActiveBranchKeyEnsuresPublicly(input, output)
      ensures unchanged(History)

      ensures |ddbClient.History.GetItem| == |old(ddbClient.History.GetItem)| + 1
      ensures
        //= aws-encryption-sdk-specification/framework/key-store/dynamodb-key-storage.md#getencryptedactivebranchkey
        //= type=implication
        //# To get the active version for the branch key id from the keystore
        //# this operation MUST call AWS DDB `GetItem`
        //# using the `branch-key-id` as the Partition Key and `"branch:ACTIVE"` value as the Sort Key.
        && Seq.Last(ddbClient.History.GetItem).input.Key
           == map[
                Structure.BRANCH_KEY_IDENTIFIER_FIELD := DDB.AttributeValue.S(input.Identifier),
                Structure.TYPE_FIELD := DDB.AttributeValue.S(Structure.BRANCH_KEY_ACTIVE_TYPE)
              ]

      ensures output.Success?
              ==>
                && Seq.Last(ddbClient.History.GetItem).output.Success?
                && Seq.Last(ddbClient.History.GetItem).output.value.Item.Some?
                   //= aws-encryption-sdk-specification/framework/key-store/dynamodb-key-storage.md#getencryptedactivebranchkey
                   //= type=implication
                   //# The AWS DDB response MUST contain the fields defined in the [branch keystore record format](#record-format).
                && Structure.BranchKeyItem?(Seq.Last(ddbClient.History.GetItem).output.value.Item.value)

      ensures
        && old(ddbClient.History.GetItem) < ddbClient.History.GetItem
        && old(ddbClient.History.TransactWriteItems) == ddbClient.History.TransactWriteItems

      ensures
        && Seq.Last(ddbClient.History.GetItem).output.Success?
        && Seq.Last(ddbClient.History.GetItem).output.value.Item.Some?
           //= aws-encryption-sdk-specification/framework/key-store/dynamodb-key-storage.md#getencryptedactivebranchkey
           //= type=implication
           //# If the record does not contain the defined fields, this operation MUST fail.
        && !Structure.BranchKeyItem?(Seq.Last(ddbClient.History.GetItem).output.value.Item.value)
        ==> output.Failure?
    {

      var dynamoDbKey: DDB.Key := map[
        Structure.BRANCH_KEY_IDENTIFIER_FIELD := DDB.AttributeValue.S(input.Identifier),
        Structure.TYPE_FIELD := DDB.AttributeValue.S(Structure.BRANCH_KEY_ACTIVE_TYPE)
      ];
      var ItemRequest := DDB.GetItemInput(
        Key := dynamoDbKey,
        TableName := ddbTableName,
        AttributesToGet := None,
        ConsistentRead :=  None,
        ReturnConsumedCapacity := None,
        ProjectionExpression := None,
        ExpressionAttributeNames := None
      );

      var getItemResponse? := ddbClient.GetItem(ItemRequest);
      var getItemResponse :- getItemResponse?
      .MapFailure(e => Types.ComAmazonawsDynamodb(ComAmazonawsDynamodb := e));

      :- Need(
        getItemResponse.Item.Some? && |getItemResponse.Item.value| >= 1,
        Types.KeyStoreException( message := ErrorMessages.NO_CORRESPONDING_BRANCH_KEY)
      );

      :- Need(
        Structure.BranchKeyItem?(getItemResponse.Item.value),
        Types.KeyStoreException( message := ErrorMessages.INVALID_ACTIVE_BRANCH_KEY_FROM_STORAGE)
      );

      var activeItem := ToEncryptedHierarchicalKey(getItemResponse.Item.value, logicalKeyStoreName);

      :- Need(
        && activeItem.Type.ActiveHierarchicalSymmetricVersion?
        && activeItem.Identifier == input.Identifier,
        Types.KeyStoreException( message := ErrorMessages.INVALID_ACTIVE_BRANCH_KEY_FROM_STORAGE)
      );

      // This is a simplification of the above checks.
      // The goal is that the record is well constructed,
      // but this way all the checks can be done only once.
      assert Structure.ActiveHierarchicalSymmetricKey?(activeItem);

      output := Success(
        Types.GetEncryptedActiveBranchKeyOutput(
          Item := activeItem
        ));
    }

    method GetEncryptedBranchKeyVersion' ( input: Types.GetEncryptedBranchKeyVersionInput )
      returns (output: Result<Types.GetEncryptedBranchKeyVersionOutput, Types.Error>)
      requires
        && ValidState()
      modifies Modifies - {History}
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures GetEncryptedBranchKeyVersionEnsuresPublicly(input, output)
      ensures unchanged(History)

      ensures |ddbClient.History.GetItem| == |old(ddbClient.History.GetItem)| + 1

      ensures
        //= aws-encryption-sdk-specification/framework/key-store/dynamodb-key-storage.md#getencryptedbranchkeyversion
        //= type=implication
        //# To get a branch key from the keystore this operation MUST call AWS DDB `GetItem`
        //# using the `branch-key-id` as the Partition Key and "branch:version:" + `branchKeyVersion` value as the Sort Key.
        && Seq.Last(ddbClient.History.GetItem).input.Key
           == map[
                Structure.BRANCH_KEY_IDENTIFIER_FIELD := DDB.AttributeValue.S(input.Identifier),
                Structure.TYPE_FIELD := DDB.AttributeValue.S(Structure.BRANCH_KEY_TYPE_PREFIX + input.Version)
              ]

      ensures output.Success?
              ==>
                && Seq.Last(ddbClient.History.GetItem).output.Success?
                && Seq.Last(ddbClient.History.GetItem).output.value.Item.Some?
                   //= aws-encryption-sdk-specification/framework/key-store/dynamodb-key-storage.md#getencryptedbranchkeyversion
                   //= type=implication
                   //# The AWS DDB response MUST contain the fields defined in the [branch keystore record format](#record-format).
                && Structure.BranchKeyItem?(Seq.Last(ddbClient.History.GetItem).output.value.Item.value)

      ensures
        && |ddbClient.History.GetItem| == |old(ddbClient.History.GetItem)| + 1
        && Seq.Last(ddbClient.History.GetItem).output.Success?
        && Seq.Last(ddbClient.History.GetItem).output.value.Item.Some?
           //= aws-encryption-sdk-specification/framework/key-store/dynamodb-key-storage.md#getencryptedbranchkeyversion
           //= type=implication
           //# If the record does not contain the defined fields, this operation MUST fail.
        && !Structure.BranchKeyItem?(Seq.Last(ddbClient.History.GetItem).output.value.Item.value)
        ==> output.Failure?
    {

      var dynamoDbKey: DDB.Key := map[
        Structure.BRANCH_KEY_IDENTIFIER_FIELD := DDB.AttributeValue.S(input.Identifier),
        Structure.TYPE_FIELD := DDB.AttributeValue.S(Structure.BRANCH_KEY_TYPE_PREFIX + input.Version)
      ];
      var ItemRequest := DDB.GetItemInput(
        Key := dynamoDbKey,
        TableName := ddbTableName
      );


      var getItemResponse? := ddbClient.GetItem(ItemRequest);
      var getItemResponse :- getItemResponse?
      .MapFailure(e => Types.ComAmazonawsDynamodb(ComAmazonawsDynamodb := e));

      :- Need(
        getItemResponse.Item.Some? && |getItemResponse.Item.value| >= 1,
        Types.KeyStoreException( message := ErrorMessages.NO_CORRESPONDING_BRANCH_KEY)
      );

      :- Need(
        Structure.BranchKeyItem?(getItemResponse.Item.value),
        Types.KeyStoreException( message := ErrorMessages.INVALID_BRANCH_KEY_VERSION_FROM_STORAGE)
      );

      var versionItem := ToEncryptedHierarchicalKey(getItemResponse.Item.value, logicalKeyStoreName);

      :- Need(
        && versionItem.Type.HierarchicalSymmetricVersion?
        && versionItem.Identifier == input.Identifier
        && versionItem.Type == Types.HierarchicalSymmetricVersion(Types.HierarchicalSymmetric( Version := input.Version )),
        Types.KeyStoreException( message := ErrorMessages.INVALID_BRANCH_KEY_VERSION_FROM_STORAGE)
      );

      // This is a simplification of the above checks.
      // The goal is that the record is well constructed,
      // but this way all the checks can be done only once.
      assert Structure.DecryptOnlyHierarchicalSymmetricKey?(versionItem);

      output := Success(
        Types.GetEncryptedBranchKeyVersionOutput(
          Item := versionItem
        ));
    }

    method GetEncryptedBeaconKey' ( input: Types.GetEncryptedBeaconKeyInput )
      returns (output: Result<Types.GetEncryptedBeaconKeyOutput, Types.Error>)
      requires
        && ValidState()
      modifies Modifies - {History}
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures GetEncryptedBeaconKeyEnsuresPublicly(input, output)
      ensures unchanged(History)

      ensures |ddbClient.History.GetItem| == |old(ddbClient.History.GetItem)| + 1

      ensures
        //= aws-encryption-sdk-specification/framework/key-store/dynamodb-key-storage.md#getencryptedbeaconkey
        //= type=implication
        //# To get a branch key from the keystore this operation MUST call AWS DDB `GetItem`
        //# using the `branch-key-id` as the Partition Key and "beacon:ACTIVE" value as the Sort Key.
        && Seq.Last(ddbClient.History.GetItem).input.Key
           == map[
                Structure.BRANCH_KEY_IDENTIFIER_FIELD := DDB.AttributeValue.S(input.Identifier),
                Structure.TYPE_FIELD := DDB.AttributeValue.S(Structure.BEACON_KEY_TYPE_VALUE)
              ]

      ensures output.Success?
              ==>
                && Seq.Last(ddbClient.History.GetItem).output.Success?
                && Seq.Last(ddbClient.History.GetItem).output.value.Item.Some?
                   //= aws-encryption-sdk-specification/framework/key-store/dynamodb-key-storage.md#getencryptedbeaconkey
                   //= type=implication
                   //# The AWS DDB response MUST contain the fields defined in the [branch keystore record format](#record-format).
                && Structure.BranchKeyItem?(Seq.Last(ddbClient.History.GetItem).output.value.Item.value)

      ensures
        && Seq.Last(ddbClient.History.GetItem).output.Success?
        && Seq.Last(ddbClient.History.GetItem).output.value.Item.Some?
           //= aws-encryption-sdk-specification/framework/key-store/dynamodb-key-storage.md#getencryptedbeaconkey
           //= type=implication
           //# If the record does not contain the defined fields, this operation MUST fail.
        && !Structure.BranchKeyItem?(Seq.Last(ddbClient.History.GetItem).output.value.Item.value)
        ==> output.Failure?
    {
      var dynamoDbKey: DDB.Key := map[
        Structure.BRANCH_KEY_IDENTIFIER_FIELD := DDB.AttributeValue.S(input.Identifier),
        Structure.TYPE_FIELD := DDB.AttributeValue.S(Structure.BEACON_KEY_TYPE_VALUE)
      ];
      var ItemRequest := DDB.GetItemInput(
        Key := dynamoDbKey,
        TableName := ddbTableName,
        AttributesToGet := None,
        ConsistentRead :=  None,
        ReturnConsumedCapacity := None,
        ProjectionExpression := None,
        ExpressionAttributeNames := None
      );

      var maybeGetItem := ddbClient.GetItem(ItemRequest);
      var getItemResponse :- maybeGetItem
      .MapFailure(e => Types.ComAmazonawsDynamodb(ComAmazonawsDynamodb := e));

      :- Need(
        getItemResponse.Item.Some? && |getItemResponse.Item.value| >= 1,
        Types.KeyStoreException( message := ErrorMessages.NO_CORRESPONDING_BRANCH_KEY)
      );

      :- Need(
        Structure.BranchKeyItem?(getItemResponse.Item.value),
        Types.KeyStoreException( message := ErrorMessages.INVALID_BEACON_KEY_FROM_STORAGE)
      );

      var beaconItem := ToEncryptedHierarchicalKey(getItemResponse.Item.value, logicalKeyStoreName);

      :- Need(
        && beaconItem.Type.ActiveHierarchicalSymmetricBeacon?
        && beaconItem.Identifier == input.Identifier,
        Types.KeyStoreException( message := ErrorMessages.INVALID_BEACON_KEY_FROM_STORAGE)
      );

      // This is a simplification of the above checks.
      // The goal is that the record is well constructed,
      // but this way all the checks can be done only once.
      assert Structure.ActiveHierarchicalSymmetricBeaconKey?(beaconItem);

      output := Success(
        Types.GetEncryptedBeaconKeyOutput(
          Item := beaconItem
        ));
    }


    method GetKeyStorageInfo' ( input: Types.GetKeyStorageInfoInput )
      returns (output: Result<Types.GetKeyStorageInfoOutput, Types.Error>)
      requires
        && ValidState()
      modifies Modifies - {History}
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures GetKeyStorageInfoEnsuresPublicly(input, output)
      ensures unchanged(History)
    {
      return Success(
          Types.GetKeyStorageInfoOutput(
            Name := ddbTableNameUtf8,
            LogicalName := logicalKeyStoreNameUtf8
          ));
    }
  }

  function method CreateTransactWritePutItem(
    encryptedKey: Types.EncryptedHierarchicalKey,
    tableName: DDB.TableName,
    ConditionExpression: ConditionExpression
  ): (output: DDB.TransactWriteItem)
    requires (forall k <- encryptedKey.EncryptionContext.Keys :: DDB.IsValid_AttributeName(k))
  {
    DDB.TransactWriteItem(
      Put := Some(
        DDB.Put(
          Item := ToAttributeMap(encryptedKey),
          TableName := tableName,
          ConditionExpression := Some(
            match ConditionExpression
            case BRANCH_KEY_NOT_EXIST() => BRANCH_KEY_NOT_EXIST_CONDITION
            case BRANCH_KEY_EXISTS() => BRANCH_KEY_EXISTS_CONDITION
          ),
          ExpressionAttributeNames := Some(BRANCH_KEY_EXISTS_EXPRESSION_ATTRIBUTE_NAMES)))
    )
  }
}
