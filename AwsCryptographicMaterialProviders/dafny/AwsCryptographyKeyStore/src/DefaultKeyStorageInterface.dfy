// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../Model/AwsCryptographyKeyStoreTypes.dfy"
include "Structure.dfy"
include "ErrorMessages.dfy"
include "KmsArn.dfy"

module DefaultKeyStorageInterface {
  import opened Wrappers
  import ComAmazonawsDynamodbTypes
  import Seq
  import Types = AwsCryptographyKeyStoreTypes
  import DDB = ComAmazonawsDynamodbTypes
  import UTF8
  import Structure
  import String = StandardLibrary.String
  import KmsArn

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

  // To use these values in a match Dafny needs to match these as local variables.
  // This means that Dafny can not use `Structure.MUTATION_LOCK_TYPE`
  // in the case statement to evaluate a literal.
  const MUTATION_LOCK_TYPE := "branch:MUTATION_LOCK" // Structure.MUTATION_LOCK_TYPE
  const BRANCH_KEY_ACTIVE_TYPE := "branch:ACTIVE" // Structure.BRANCH_KEY_ACTIVE_TYPE
  const BEACON_KEY_TYPE_VALUE :=  "beacon:ACTIVE" // Structure.BEACON_KEY_TYPE_VALUE
  const VERSION_TYPE_PREFIX := "branch:version:" // Structure.BRANCH_KEY_TYPE_PREFIX

  lemma TypesAreCorrect()
    ensures
      && MUTATION_LOCK_TYPE == Structure.MUTATION_LOCK_TYPE
      && BRANCH_KEY_ACTIVE_TYPE == Structure.BRANCH_KEY_ACTIVE_TYPE
      && BEACON_KEY_TYPE_VALUE == Structure.BEACON_KEY_TYPE_VALUE
      && VERSION_TYPE_PREFIX == Structure.BRANCH_KEY_TYPE_PREFIX
  {}

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

    predicate GetItemsForInitializeMutationEnsuresPublicly(
      input: Types.GetItemsForInitializeMutationInput ,
      output: Result<Types.GetItemsForInitializeMutationOutput, Types.Error>
    )
    {
      && (output.Success? ==>
            && output.value.activeItem.Identifier == input.Identifier
            && Structure.ActiveHierarchicalSymmetricKey?(output.value.activeItem)
            && output.value.activeItem.EncryptionContext[Structure.TABLE_FIELD] == logicalKeyStoreName
            && KmsArn.ValidKmsArn?(output.value.activeItem.KmsArn)
            && output.value.beaconItem.Identifier == input.Identifier
            && Structure.ActiveHierarchicalSymmetricBeaconKey?(output.value.beaconItem)
            && output.value.beaconItem.EncryptionContext[Structure.TABLE_FIELD] == logicalKeyStoreName
            && KmsArn.ValidKmsArn?(output.value.beaconItem.KmsArn)
      )
    }

    predicate WriteInitializeMutationEnsuresPublicly(
      input: Types.WriteInitializeMutationInput ,
      output: Result<Types.WriteInitializeMutationOutput, Types.Error>
    )
    {true}

    predicate QueryForVersionsEnsuresPublicly(
      input: Types.QueryForVersionsInput ,
      output: Result<Types.QueryForVersionsOutput, Types.Error>
    )
    {
      && (output.Success? && |output.value.items| > 0 ==>
            forall item <- output.value.items ::
              && item.Identifier == input.Identifier
              && Structure.DecryptOnlyHierarchicalSymmetricKey?(item)
              && item.Type.HierarchicalSymmetricVersion?
              && item.EncryptionContext[Structure.TABLE_FIELD] == logicalKeyStoreName
              && KmsArn.ValidKmsArn?(item.KmsArn)
      )
    }

    predicate WriteMutatedVersionsEnsuresPublicly(
      input: Types.WriteMutatedVersionsInput ,
      output: Result<Types.WriteMutatedVersionsOutput, Types.Error>
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
                    CreateTransactOverwriteActive(
                      input.Active,
                      input.oldActive,
                      ddbTableName
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
        CreateTransactOverwriteActive(
          input.Active,
          input.oldActive,
          ddbTableName
        )
      ];

      var transactRequest := DDB.TransactWriteItemsInput(
        TransactItems := items,
        ReturnConsumedCapacity := None,
        ReturnItemCollectionMetrics := None,
        ClientRequestToken := None
      );

      var transactWriteItemsResponse? := ddbClient.TransactWriteItems(transactRequest);
      // TODO: A mitigation to the threat model requires that we know if write requests fail due to a race.
      // But, from DDB Docs: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_TransactWriteItems.html#API_TransactWriteItems_Errors
      // > If using Java, DynamoDB lists the cancellation reasons on the CancellationReasons property.
      // > This property is not set for other languages.
      // Thus, we MAY only be able to detect why a DDB Transact Request Failed in Java...
      // Tony will talk to our Security Engineer... maybe we benerate some logic
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

    // This a Get for 3 items, with ConsistentRead
    // From DDB Docs: "If a requested item does not exist, it is not returned in the result."
    // Thus, if Mutation Lock is not returned, than it does not exist.
    method GetItemsForInitializeMutation' ( input: Types.GetItemsForInitializeMutationInput )
      returns (output: Result<Types.GetItemsForInitializeMutationOutput, Types.Error>)
      requires  ValidState()
      modifies Modifies - {History}
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures ValidState()
      ensures GetItemsForInitializeMutationEnsuresPublicly(input, output)
      ensures unchanged(History)
    {
      /** Construct & Issue DDB Request */
      var mLockKey: DDB.Key := map[
        Structure.BRANCH_KEY_IDENTIFIER_FIELD := DDB.AttributeValue.S(input.Identifier),
        Structure.TYPE_FIELD := DDB.AttributeValue.S(Structure.MUTATION_LOCK_TYPE)
      ];
      var activeKey: DDB.Key := map[
        Structure.BRANCH_KEY_IDENTIFIER_FIELD := DDB.AttributeValue.S(input.Identifier),
        Structure.TYPE_FIELD := DDB.AttributeValue.S(Structure.BRANCH_KEY_ACTIVE_TYPE)
      ];
      var beaconKey: DDB.Key := map[
        Structure.BRANCH_KEY_IDENTIFIER_FIELD := DDB.AttributeValue.S(input.Identifier),
        Structure.TYPE_FIELD := DDB.AttributeValue.S(Structure.BEACON_KEY_TYPE_VALUE)
      ];
      var keysList := [mLockKey, activeKey, beaconKey];
      var keysAndAttributes := DDB.KeysAndAttributes(
        Keys := keysList,
        ConsistentRead := Some(true));
      var ddbRequest := DDB.BatchGetItemInput(RequestItems := map[ddbTableName := keysAndAttributes]);
      var ddbResponse? := ddbClient.BatchGetItem(ddbRequest);
      /** Handle DDB Error */
      // TODO Benerate KeyStorageException to have a message field and an Error field
      // that can hold either Opaque or DDB Error
      var ddbResponse :- ddbResponse?
      .MapFailure((e: DDB.Error) =>
                    wrapDdbException(
                      e:=e,
                      storageOperation:="GetItemForInitializeMutation",
                      ddbOperation:="BatchGetItem",
                      identifier:=input.Identifier,
                      tableName:=ddbTableName));

        /** Handle nonsensical DDB Responses */
        // We could debate weather it is good to conflate
        // no response with response from more than one table
        // with response from one table but it's the wrong table...
        // but the only real error case we expect is no response.
      :- Need(
        ddbResponse.Responses.Some? && (|ddbResponse.Responses.value| == 1) && (ddbResponse.Responses.value.Keys == {ddbTableName}),
        Types.KeyStorageException(
          message:="DDB returned no items from table: " + ddbTableName));

        // SDKs/Smithy-Dafny/Custom Implementations of Storage MAY respond with None or an Empty Map.
        // .NET returns an empty map, Java returns None.
      :- Need(
        ddbResponse.UnprocessedKeys.None? || |ddbResponse.UnprocessedKeys.value| == 0,
        Types.KeyStorageException(
          message:=
            "DDB returned UnprocessedKeys for a BatchGetItem request of 3 items"
            + ", which is indicative a DDB Read error due to some conflicting activity." +
            "Table Name: " + ddbTableName + "\tBranch Key ID: " + input.Identifier));
      var itemList: DDB.ItemList := ddbResponse.Responses.value[ddbTableName];
      :- Need(
        2 <= |itemList| <= 3,
        Types.KeyStorageException(
          message:="DDB returned the wrong number of Items;"
          + " 2 or 3 are expected. Received: " + String.Base10Int2String(|itemList|)));

      /** Process sensical DDB Response */
      var itemIndex := 0;
      var beaconItem: Option<Types.EncryptedHierarchicalKey> := None;
      var activeItem: Option<Types.EncryptedHierarchicalKey> := None;
      var lockItem: Option<Types.MutationLock> := None;
      while itemIndex < |itemList|
      {
        var item := itemList[itemIndex];
        :- Need(
          Structure.TYPE_FIELD in item.Keys,
          Types.KeyStorageException(
            message:=
              "Malformed Branch Key Store Item encountered. Missing TYPE Attribute. "
              + "TableName: " + ddbTableName +
              "\tBranch Key ID: " + input.Identifier
          ));
        var itemType := item[Structure.TYPE_FIELD];
        :- Need(
          itemType.S?,
          Types.KeyStorageException(
            message:=
              "Malformed Branch Key Store Item encountered. TYPE Attribute MUST be String but is not. " +
              "TableName: " + ddbTableName + "\tBranch Key ID: " + input.Identifier
          ));
        var typeStr: string := itemType.S;
        var id: string := input.Identifier; // Tony did this solely so lines would not wrap
        match typeStr {
          case MUTATION_LOCK_TYPE =>
            var lockItem? := mutationLockFromItem(item, id);
            if (lockItem?.Success?) { lockItem := Some(lockItem?.value); } else { return Failure(lockItem?.error); }
          case BRANCH_KEY_ACTIVE_TYPE => var activeItem? := encryptedHierarchicalKeyFromItem(item, logicalKeyStoreName, id);
          if (activeItem?.Success?) { activeItem := Some(activeItem?.value); } else { return Failure(activeItem?.error); }
          case BEACON_KEY_TYPE_VALUE => var beaconItem? := encryptedHierarchicalKeyFromItem(item, logicalKeyStoreName, id);
          if (beaconItem?.Success?) { beaconItem := Some(beaconItem?.value); } else { return Failure(beaconItem?.error); }
          case _ => return Failure(
              Types.KeyStorageException(
                message:=
                  "Unexpected item returned by DDB. TableName: "
                  + ddbTableName + "\tBranch Key ID: " + input.Identifier));
        }
        itemIndex := 1 + itemIndex;
      }

        /** Validate DDB Responses */
      :- Need(
        activeItem.Some?,
        Types.KeyStorageException(
          message:=
            "Could not find the ACTIVE Item. TableName: " + ddbTableName + "\tBranch Key ID: " + input.Identifier
        ));
      :- Need(
        && Structure.ActiveHierarchicalSymmetricKey?(activeItem.value)
        && activeItem.value.Identifier == input.Identifier
        && activeItem.value.EncryptionContext[Structure.TABLE_FIELD] == logicalKeyStoreName
        && KmsArn.ValidKmsArn?(activeItem.value.KmsArn),
        Types.KeyStorageException(
          message:=
            "Item returned for the ACTIVE is malformed. TableName: " + ddbTableName + "\tBranch Key ID: " + input.Identifier
        ));

      :- Need(beaconItem.Some?,
              Types.KeyStorageException(
                message:=
                  "Could not find the Beacon Key. TableName: " + ddbTableName + "\tBranch Key ID: " + input.Identifier
              ));
      :- Need(
        && Structure.ActiveHierarchicalSymmetricBeaconKey?(beaconItem.value)
        && beaconItem.value.Identifier == input.Identifier
        && beaconItem.value.EncryptionContext[Structure.TABLE_FIELD] == logicalKeyStoreName
        && KmsArn.ValidKmsArn?(beaconItem.value.KmsArn),
        Types.KeyStorageException(
          message:=
            "Item returned for Beacon Key is malformed. TableName: " + ddbTableName + "\tBranch Key ID: " + input.Identifier
        ));

      if (lockItem.Some?) {
        :- Need(
          && lockItem.value.Identifier == input.Identifier,
          Types.KeyStorageException(
            message:=
              "Item returned for Mutation Lock is malformed. TableName: " + ddbTableName + "\tBranch Key ID: " + input.Identifier
          ));
      }

      return Success(
          Types.GetItemsForInitializeMutationOutput(
            activeItem := activeItem.value,
            beaconItem := beaconItem.value,
            mutationLock := lockItem
          ));
    }

    function method mutationLockFromItem(
      item: DDB.AttributeMap,
      identifier: string
    ): (output: Result<Types.MutationLock, Types.Error>)
    {
      :- Need(
           Structure.MutationLockAttribute?(item),
           Types.KeyStorageException(
             message:="Malformed Branch Key Store Item encountered. TableName: "
             + ddbTableName + "\tBranch Key ID: " + identifier)
         );
      Success(Structure.ToMutationLock(item))
    }


    function method encryptedHierarchicalKeyFromItem(
      item: DDB.AttributeMap,
      logicalKeyStoreName: string,
      identifier: string
    ): (output: Result<Types.EncryptedHierarchicalKey, Types.Error>)
      ensures output.Success?
              ==>
                && Structure.EncryptedHierarchicalKey?(output.value)
                && output.value.Identifier == identifier
                && output.value.EncryptionContext[Structure.TABLE_FIELD] == logicalKeyStoreName
                && KmsArn.ValidKmsArn?(output.value.KmsArn)
    {
      :- Need(
           Structure.BranchKeyItem?(item),
           Types.KeyStorageException(
             message:="Malformed Branch Key Store Item encountered. TableName: "
             + ddbTableName + "\tBranch Key ID: " + identifier)
         );
      var branchKey := ToEncryptedHierarchicalKey(branchKey, logicalKeyStoreName);

      assert branchKey.EncryptionContext[Structure.TABLE_FIELD] == logicalKeyStoreName;
      :- Need(
           && branchKey.Identifier == identifier
           && branchKey.EncryptionContext[Structure.TABLE_FIELD] == logicalKeyStoreName
           && KmsArn.ValidKmsArn?(branchKey.KmsArn),
           Types.KeyStorageException(
             message:="Malformed Branch Key Store BranchKey encountered. TableName: "
             + ddbTableName + "\tBranch Key ID: " + identifier)
         );
      Success(branchKey)
    }

    /** A transaction write for 4 items, conditioned on No Mutation Lock exsisting for Identifier.*/
    /** One of the items is a new Active; it is conditioned on the oldActive's enc still being present at write time.*/
    method WriteInitializeMutation' ( input: Types.WriteInitializeMutationInput )
      returns (output: Result<Types.WriteInitializeMutationOutput, Types.Error>)
      requires
        && ValidState()
      modifies Modifies - {History}
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures WriteInitializeMutationEnsuresPublicly(input, output)
      ensures unchanged(History)
    {

      :- Need(
        Structure.MutationLock?(input.mutationLock)
      , Types.KeyStorageException(
          message := "Invalid mutation lock."
        )
      );

        /** Validate Inputs can be mapped to DDB Items */
      :- Need(
        && (forall k <- input.version.EncryptionContext.Keys :: DDB.IsValid_AttributeName(k))
        && (forall k <- input.active.EncryptionContext.Keys :: DDB.IsValid_AttributeName(k))
        && (forall k <- input.beacon.EncryptionContext.Keys :: DDB.IsValid_AttributeName(k))
      , Types.KeyStorageException( message := ErrorMessages.ENCRYPTION_CONTEXT_EXCEEDS_DDB_LIMIT)
      );
      /** Convert Inputs to DDB Items.*/
      var items: DDB.TransactWriteItemList := [
        CreateTransactWritePutItem(
          input.version,
          ddbTableName,
          BRANCH_KEY_NOT_EXIST // The new Decrypt Only MUST not exist
        ),
        CreateTransactOverwriteActive(
          input.active,
          input.oldActive,
          ddbTableName
        ),
        CreateTransactWritePutItem(
          input.beacon,
          ddbTableName,
          BRANCH_KEY_EXISTS // The Beacon MUST exist
        ),
        CreateTransactWriteMLock(
          input.mutationLock,
          ddbTableName,
          BRANCH_KEY_NOT_EXIST // The M-LOCK MUST not exist
        )
      ];
      var transactRequest := DDB.TransactWriteItemsInput(
        TransactItems := items,
        ReturnConsumedCapacity := None,
        ReturnItemCollectionMetrics := None,
        ClientRequestToken := None
      );

      var transactWriteItemsResponse? := ddbClient.TransactWriteItems(transactRequest);
      // TODO-Mutations-FF: we need to check the cancellation reason for
      // ConditionalCheckFailed on the Active item (VersionRaceException)
      // OR the Mutation Lock (MutationLockException)
      // OR something else.
      var _ :- transactWriteItemsResponse?
      .MapFailure(e => wrapDdbException(
                      e:=e,
                      storageOperation:="WriteInitializeMutation",
                      ddbOperation:="TransactWriteItems",
                      identifier:=input.active.Identifier,
                      tableName:=ddbTableName));
      // This is a Smithy Modeled Operation; the output MUST be a Structure
      output := Success(Types.WriteInitializeMutationOutput());
    }

    static const queryForVersionsKeyExpression: DDB.KeyExpression := "#pk = :pk AND begins_with( #sk, :decryptOnlyPrefix )"
    static const queryForVersionsExpAttNames: DDB.ExpressionAttributeNameMap :=
      map[
        "#pk" := Structure.BRANCH_KEY_IDENTIFIER_FIELD,
        "#sk" := Structure.TYPE_FIELD]

    method QueryForVersions' ( input: Types.QueryForVersionsInput )
      returns (output: Result<Types.QueryForVersionsOutput, Types.Error>)
      requires
        && ValidState()
      modifies Modifies - {History}
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures QueryForVersionsEnsuresPublicly(input, output)
      ensures unchanged(History)
    {
      /** Construct & Issue DDB Request */
      var exclusiveStartKey: Option<DDB.Key> := None;
      if (input.exclusiveStartKey.Some?) {
        var decodedLastKey :- blobToExclusiveStartKey(
          input.exclusiveStartKey.value,
          input.Identifier);
        exclusiveStartKey := Some(decodedLastKey);
      }
      :- Need(0 < input.pageSize,
              Types.KeyStorageException(message:="DynamoDB Encrypted Key Storage will not Query for page size of 0."));
      var exprAttributeValues: DDB.ExpressionAttributeValueMap := map[
        ":pk" := DDB.AttributeValue.S(input.Identifier),
        ":decryptOnlyPrefix" := DDB.AttributeValue.S("branch:version:")];
      var ddbRequest := DDB.QueryInput(
        TableName := ddbTableName,
        Limit := Some(input.pageSize),
        ConsistentRead := Some(true),
        ExclusiveStartKey := exclusiveStartKey,
        KeyConditionExpression := Some(queryForVersionsKeyExpression),
        ExpressionAttributeNames := Some(queryForVersionsExpAttNames),
        ExpressionAttributeValues := Some(exprAttributeValues)
      );
      var ddbResponse? := ddbClient.Query(ddbRequest);

      /** Handle DDB Error */
      var ddbResponse :- ddbResponse?
      .MapFailure(
        (e: DDB.Error) => wrapDdbException(
            e:=e,
            storageOperation:="QueryForVersions",
            ddbOperation:="Query",
            identifier:=input.Identifier,
            tableName:=ddbTableName));

      /** Process sensical DDB Response */
      var lastKeyBlob: seq<Types.UInt.uint8> := [];
      var lastKeyEmpty: bool :=
        // It is not clear if SDKs/Smithy-Dafny/Custom Implementations of Storage will respond with None or an Empty Map.
        ddbResponse.LastEvaluatedKey.None? || (ddbResponse.LastEvaluatedKey.Some? && |ddbResponse.LastEvaluatedKey.value| == 0);

      if (!lastKeyEmpty) {
        lastKeyBlob :- lastEvaluatedKeyToBlob(ddbResponse.LastEvaluatedKey.value);
      }
      if (ddbResponse.Items.None? || ( |ddbResponse.Items.value| == 0) ) {
        return Success(Types.QueryForVersionsOutput(
                         exclusiveStartKey := lastKeyBlob,
                         items := []
                       ));
      }

      /* Map DDB items to Branch Keys.*/
      var branchKeys: seq<Types.EncryptedHierarchicalKey> :- Seq.MapWithResult(
        // Dafny requires the type of the element being mapped over, or it feaks out.
        (item: DDB.AttributeMap)
        =>
          /* Convert DDB Item to Branch Key. */
          var branchKey :- encryptedHierarchicalKeyFromItem(item, logicalKeyStoreName, input.Identifier);
          /* Validate that Branch Key is a Version, or Decrypt Only, Branch Key Type. */
          :- Need(
               branchKey.Type.HierarchicalSymmetricVersion?,
               Types.KeyStorageException(
                 message:="Unexpected item returned by DDB. TableName: " + ddbTableName + "\tBranch Key ID: " + input.Identifier
               ));
          Success(branchKey),
        ddbResponse.Items.value
      );

      return Success(
          Types.QueryForVersionsOutput(
            exclusiveStartKey := lastKeyBlob,
            items := branchKeys
          ));
    }

    function method blobToExclusiveStartKey(
      blob: seq<Types.UInt.uint8>,
      identifier: string
    ): (output: Result<DDB.Key,Types.Error>)
    {
      // From DDB's Docs:
      // https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Query.html#API_Query_RequestSyntax
      // > The primary key of the first item that this
      // > operation will evaluate. Use the value that was returned for LastEvaluatedKey in the previous operation.
      // > The data type for ExclusiveStartKey must be String, Number, or Binary. No set data types are allowed.
      // From that, we can infer that Partition Key is just going to be the Identifier.
      // Thus, we only need to store the Type value.
      // This will be the full "branch:version:<uuidv4>"
      var versionStr :- UTF8.Decode(blob).MapFailure(
                          eString => Types.KeyStorageException(
                              message:="Could not UTF8 Decode Exclusive Start Key. " + eString));
      :- Need(
           // I elected to require len > 15, rather than len == 51, in case we or someone else ever uses not-UUIDv4 for version.
           && 15 < |versionStr| && versionStr[0 .. 15] == "branch:version:",
           Types.KeyStorageException(
             message:=
               "Exclusive Start Key does not appear to be applicable to the DynamoDB Encrypted Key Storage."
               + " It should start with 'branch:version:'. Passed Value: " + versionStr));
      var exclusiveStartKey: DDB.Key :=
        map[
          Structure.BRANCH_KEY_IDENTIFIER_FIELD := DDB.AttributeValue.S(identifier),
          Structure.TYPE_FIELD := DDB.AttributeValue.S(versionStr)
        ];
      Success(exclusiveStartKey)
    }

    function method lastEvaluatedKeyToBlob(lastKey: DDB.Key): (output: Result<seq<Types.UInt.uint8>, Types.Error>)
    {
      :- Need(
           Structure.TYPE_FIELD in lastKey && lastKey[Structure.TYPE_FIELD].S?,
           Types.KeyStorageException(
             message:=
               "Last Evaluated Key does not appear to be applicable to the DynamoDB Encrypted Key Storage."
               + " It should contain 'type' as key with a DDB String as the value."));
      :- Need(
           |lastKey[Structure.TYPE_FIELD].S| > 15 && lastKey[Structure.TYPE_FIELD].S[0 .. 15] == "branch:version:",
           Types.KeyStorageException(
             message:=
               "Last Evaluated Key does not appear to be applicable to the DynamoDB Encrypted Key Storage."
               + " The value for 'type' should be a string that starts with 'branch:version'."));
      var blob :- UTF8.Encode(lastKey[Structure.TYPE_FIELD].S)
                  .MapFailure(
                    eString
                    =>
                      Types.KeyStorageException(
                        message
                        :=
                          "Could not UTF8 Encode Last Evaluated Key. " + eString));
      Success(blob)
    }

    /** Transaction OverWrite up to 24 Decryt Only Items, with a Global Condition on the M-Lock.*/
    method WriteMutatedVersions' ( input: Types.WriteMutatedVersionsInput )
      returns (output: Result<Types.WriteMutatedVersionsOutput, Types.Error>)
      requires
        && ValidState()
      modifies Modifies - {History}
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures WriteMutatedVersionsEnsuresPublicly(input, output)
      ensures unchanged(History)
    {
      /** Validate Input */
      :- Need(
        |input.items| < 99,
        Types.KeyStorageException(message:="DynamoDB Encrypted Key Storage can only write page sizes less than 99."
        ));
      :- Need(
        0 < |input.Original|,
        Types.KeyStorageException(message:="Original State MUST NOT be empty."
        ));
      :- Need(
        0 < |input.Terminal|,
        Types.KeyStorageException(message:="Terminal State MUST NOT be empty."
        ));

      /** Convert Items to DDB */
      var items?: seq<DDB.TransactWriteItem> :- Seq.MapWithResult(
        (branchKey: Types.EncryptedHierarchicalKey)
        =>
          /* All Attribute Names MUST comply with DDB's limits.*/
          /* Attribute Names are the "keys" of the Encryption Context.*/
          :- Need(
               && (forall k <- branchKey.EncryptionContext.Keys :: DDB.IsValid_AttributeName(k)),
               Types.KeyStorageException( message := ErrorMessages.ENCRYPTION_CONTEXT_EXCEEDS_DDB_LIMIT)
             );
          /* Only Version, or Decrypt Only, items are permitted.*/
          :- Need(
               branchKey.Type.HierarchicalSymmetricVersion?,
               Types.KeyStorageException(
                 message :=
                   "WriteMutatedVersions of DynamoDB Encrypted Key Storage ONLY writes Decrypt Only Items to Storage. "
                   + "Encountered a non-Decrypt Only Item."
               ));
          /* The branch key is valid for DDB; create a Put request.*/
          var item := CreateTransactWritePutItem(
                        branchKey,
                        ddbTableName,
                        BRANCH_KEY_EXISTS); // The Branch Key Item already exists in the table.
          Success(item),
        input.items);

      var mLockAction :=
        if (input.CompleteMutation)
        then CreateTransactDeleteMutationLock(input.Identifier, input.Original, input.Terminal, ddbTableName)
        else conditionalCheckOnMutationLock(input.Identifier, input.Original, input.Terminal, ddbTableName);
      var items: DDB.TransactWriteItemList := [mLockAction] + items?;

      /** Construct & Issue DDB Request */
      var ddbRequest := DDB.TransactWriteItemsInput(
        TransactItems := items
      );
      var ddbResponse? := ddbClient.TransactWriteItems(ddbRequest);

      /** Handle DDB Error */
      // TODO: Wherever we write a Transaction, to explain race failure, we MUST do something like this:
      if (ddbResponse?.Failure? && ddbResponse?.error.TransactionCanceledException?) {
        return Failure(
            Types.KeyStorageException(
              message :=
                "DDB request to Write Mutated Versions was failed by DDB with TransactionCanceledException. "
                + "This MAY be caused by a race between hosts mutating the same Branch Key ID. "
                + "The Mutation has NOT completed. "
                + "Table Name: "+ ddbTableName
                + "\tBranch Key ID: " + input.Identifier
                // TODO: If we cannot benerate logic to store the exception obj,
                // we MUST write logic that completely serializes all the components of
                // the TransactionCanceledException
                + "\tDDB Exception Message: \n" + ddbResponse?.error.Message.UnwrapOr("")));
      }
      var ddbResponse :- ddbResponse?
      .MapFailure(
        (e: DDB.Error) => wrapDdbException(
            e:=e,
            storageOperation:="WriteMutatedVersions",
            ddbOperation:="TransactionWriteItems",
            identifier:=input.Identifier,
            tableName:=ddbTableName));

      return Success(Types.WriteMutatedVersionsOutput());
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

  function method CreateTransactWriteMLock(
    mutationLock: Types.MutationLock,
    tableName: DDB.TableName,
    ConditionExpression: ConditionExpression
  ): (output: DDB.TransactWriteItem)
    requires Structure.MutationLock?(mutationLock)
  {
    DDB.TransactWriteItem(
      Put := Some(
        DDB.Put(
          Item := Structure.MutationLockToAttributeMap(mutationLock),
          TableName := tableName,
          ConditionExpression := Some(
            match ConditionExpression
            case BRANCH_KEY_NOT_EXIST() => BRANCH_KEY_NOT_EXIST_CONDITION
            case BRANCH_KEY_EXISTS() => BRANCH_KEY_EXISTS_CONDITION
          ),
          ExpressionAttributeNames := Some(BRANCH_KEY_EXISTS_EXPRESSION_ATTRIBUTE_NAMES)))
    )
  }

  function method CreateTransactDeleteMutationLock(
    branchKeyIdentifier: string,
    original: seq<Types.UInt.uint8> ,
    terminal: seq<Types.UInt.uint8> ,
    tableName: DDB.TableName
  ): (output: DDB.TransactWriteItem)
  {
    var check := checkForMutationLock(branchKeyIdentifier, original, terminal);
    DDB.TransactWriteItem(
      Delete := Some(
        DDB.Delete(
          Key :=
            map[
              Structure.BRANCH_KEY_IDENTIFIER_FIELD := DDB.AttributeValue.S(branchKeyIdentifier),
              Structure.TYPE_FIELD := DDB.AttributeValue.S(Structure.MUTATION_LOCK_TYPE)
            ],
          TableName := tableName,
          ConditionExpression := Some(check.ConditionExpression),
          ExpressionAttributeNames := Some(check.ExpressionAttributeNames),
          ExpressionAttributeValues := Some(check.ExpressionAttributeValues)
        )))
  }

  function method CreateTransactOverwriteActive(
    active: Types.EncryptedHierarchicalKey,
    oldActive: Types.EncryptedHierarchicalKey,
    tableName: DDB.TableName
  ): (output: DDB.TransactWriteItem)
    requires (forall k <- active.EncryptionContext.Keys :: DDB.IsValid_AttributeName(k))
  {
    var check := checkForOldActive(oldActive);
    DDB.TransactWriteItem(
      Put := Some(
        DDB.Put(
          Item := ToAttributeMap(active),
          TableName := tableName,
          ConditionExpression := Some(check.ConditionExpression),
          ExpressionAttributeNames := Some(check.ExpressionAttributeNames),
          ExpressionAttributeValues := Some(check.ExpressionAttributeValues)
        )))
  }

  datatype check = | check(
    nameonly ConditionExpression: DDB.ConditionExpression ,
    nameonly ExpressionAttributeNames: DDB.ExpressionAttributeNameMap ,
    nameonly ExpressionAttributeValues: DDB.ExpressionAttributeValueMap)

  /** Assert the cipherText of the Active Item has not changed since it was read.*/
  function method checkForOldActive(
    oldActive: Types.EncryptedHierarchicalKey
  ): (output: check)
  {
    check(
      ConditionExpression := "attribute_exists(#pk) AND enc = :encOld",
      ExpressionAttributeNames := map["#pk" := Structure.BRANCH_KEY_IDENTIFIER_FIELD],
      ExpressionAttributeValues := map[":encOld" := DDB.AttributeValue.B(oldActive.CiphertextBlob)])
  }

  function method checkForMutationLock(
    branchKeyIdentifier: string,
    original: seq<Types.UInt.uint8> ,
    terminal: seq<Types.UInt.uint8>
  ): (output: check)
  {
    check(
      ConditionExpression := "attribute_exists(#pk) AND original = :original AND terminal = :terminal",
      ExpressionAttributeNames := map["#pk" := Structure.BRANCH_KEY_IDENTIFIER_FIELD], // "#pk":="branch-key-id"
      ExpressionAttributeValues :=
        map[
          ":original" := DDB.AttributeValue.B(original),
          ":terminal" := DDB.AttributeValue.B(terminal)
        ]
    )
  }

  /** Assert a Mutation Lock exists for Branch Key ID, with Original and Terminal as expected.*/
  /** For use with WriteMutatedVersions. */
  function method conditionalCheckOnMutationLock(
    branchKeyIdentifier: string,
    original: seq<Types.UInt.uint8> ,
    terminal: seq<Types.UInt.uint8> ,
    tableName: DDB.TableName
  ): (output: DDB.TransactWriteItem)
  {
    var check := checkForMutationLock(branchKeyIdentifier, original, terminal);
    var conditionCheck
      :=
      DDB.ConditionCheck(
        Key := map[
          Structure.BRANCH_KEY_IDENTIFIER_FIELD := DDB.AttributeValue.S(branchKeyIdentifier),
          Structure.TYPE_FIELD := DDB.AttributeValue.S(Structure.MUTATION_LOCK_TYPE)
        ],
        TableName := tableName,
        ConditionExpression := check.ConditionExpression,
        ExpressionAttributeNames := Some(check.ExpressionAttributeNames),
        ExpressionAttributeValues := Some(check.ExpressionAttributeValues)
      );
    DDB.TransactWriteItem(ConditionCheck := Some(conditionCheck))
  }

  /** It is a BREAKING CHANGE to use this for Key Store Operations released in MPL v1.0.2. */
  function method wrapDdbException(
    nameonly e: DDB.Error,
    nameonly storageOperation: string,
    nameonly ddbOperation: string,
    nameonly identifier: string,
    nameonly tableName: string
  ): (storageException: Types.Error)
  {
    // TODO Benerate KeyStorageException to have a message field and an Error field
    // that can hold either Opaque or DDB Error
    match e {
      case Opaque(obj) => Types.Opaque(obj) //https://github.com/smithy-lang/smithy-dafny/issues/450#issuecomment-2322149920
      case IdempotentParameterMismatchException(Message) => Types.KeyStorageException(
        message :=
          "DDB through an exception for " +  storageOperation + "'s " + ddbOperation + ". Table Name: "
          + tableName
          + "\tBranch Key ID: " + identifier
          + "\tDDB Message: " + Message.UnwrapOr(""))
      case InvalidEndpointException(Message) => Types.KeyStorageException(
        message :=
          "DDB through an exception for " +  storageOperation + "'s " + ddbOperation + ". Table Name: "
          + tableName
          + "\tBranch Key ID: " + identifier
          + "\tDDB Message: " + Message.UnwrapOr(""))
      case TransactionInProgressException(Message) => Types.KeyStorageException(
        message :=
          "DDB through an exception for " +  storageOperation + "'s " + ddbOperation + ". Table Name: "
          + tableName
          + "\tBranch Key ID: " + identifier
          + "\tDDB Message: " + Message.UnwrapOr(""))
      case TransactionCanceledException(Message, _) => Types.KeyStorageException(
        message :=
          "DDB through an exception for " +  storageOperation + "'s " + ddbOperation + ". Table Name: "
          + tableName
          + "\tBranch Key ID: " + identifier
          + "\tDDB Message: " + Message.UnwrapOr(""))
      case _ => Types.KeyStorageException(
        message :=
          "DDB through an exception for " +  storageOperation + "'s " + ddbOperation + ". Table Name: "
          + tableName
          + "\tBranch Key ID: " + identifier
          + "\tDDB Message: " + e.message.UnwrapOr(""))
    }
  }
}
