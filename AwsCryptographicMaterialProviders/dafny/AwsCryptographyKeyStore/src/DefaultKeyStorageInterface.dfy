// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../Model/AwsCryptographyKeyStoreTypes.dfy"
include "Structure.dfy"
include "KeyStoreErrorMessages.dfy"
include "KmsArn.dfy"
include "StorageHelpers.dfy"

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
  import StorageHelpers

  const ToAttributeMap := StorageHelpers.ToAttributeMap
  const ToEncryptedHierarchicalKey := StorageHelpers.ToEncryptedHierarchicalKey
  const MutationCommitmentFromOptionalItem := StorageHelpers.MutationCommitmentFromOptionalItem
  const MutationIndexFromOptionalItem := StorageHelpers.MutationIndexFromOptionalItem
  const EncryptedHierarchicalKeyFromItem := StorageHelpers.EncryptedHierarchicalKeyFromItem
  const BlobToExclusiveStartKey := StorageHelpers.BlobToExclusiveStartKey
  const LastEvaluatedKeyToBlob := StorageHelpers.LastEvaluatedKeyToBlob
  import ErrorMessages = KeyStoreErrorMessages

  const BRANCH_KEY_EXISTS_EXPRESSION_ATTRIBUTE_NAME := "#BranchKeyIdentifierField"
  const BRANCH_KEY_EXISTS_EXPRESSION_ATTRIBUTE_NAMES
    := map[
         BRANCH_KEY_EXISTS_EXPRESSION_ATTRIBUTE_NAME := Structure.BRANCH_KEY_IDENTIFIER_FIELD
       ]
  const BRANCH_KEY_NOT_EXIST_CONDITION := "attribute_not_exists(" + BRANCH_KEY_EXISTS_EXPRESSION_ATTRIBUTE_NAME + ")"
  const BRANCH_KEY_EXISTS_CONDITION := "attribute_exists(" + BRANCH_KEY_EXISTS_EXPRESSION_ATTRIBUTE_NAME + ")"
  // The Table's Index is BRANCH_KEY_IDENTIFIER_FIELD & TYPE_FIELD
  const INDEX_EXP_ATT_NAMES: DDB.ExpressionAttributeNameMap :=
    map[
      "#pk" := Structure.BRANCH_KEY_IDENTIFIER_FIELD,
      "#sk" := Structure.TYPE_FIELD]
  // Ideally, MAX_PAGE would be Types.UInt.uint8, but the size of sequence is always an int
  const DDB_MAX_MUTATION_WRITE_PAGE_SIZE: int := 98
  const DDB_MAX_MUTATION_WRITE_PAGE_SIZE_str: string := "98"

  datatype ConditionExpression =
    | BRANCH_KEY_NOT_EXIST
    | BRANCH_KEY_EXISTS

  // To use these values in a match Dafny needs to match these as local variables.
  // This means that Dafny can not use `Structure.MUTATION_COMMITMENT_TYPE`
  // in the case statement to evaluate a literal.
  const MUTATION_COMMITMENT_TYPE := "branch:MUTATION_COMMITMENT" // Structure.MUTATION_COMMITMENT_TYPE
  const MUTATION_INDEX_TYPE := "branch:MUTATION_INDEX" // Structure.MUTATION_INDEX_TYPE

  lemma TypesAreCorrect()
    ensures
      && MUTATION_COMMITMENT_TYPE == Structure.MUTATION_COMMITMENT_TYPE
      && MUTATION_INDEX_TYPE == Structure.MUTATION_INDEX_TYPE
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

    predicate WriteMutationIndexEnsuresPublicly(
      input: Types.WriteMutationIndexInput,
      output: Result<Types.WriteMutationIndexOutput, Types.Error>
    )
    {true}

    predicate GetMutationEnsuresPublicly(
      input: Types.GetMutationInput,
      output: Result<Types.GetMutationOutput, Types.Error>
    )
    {
      && (output.Success? ==>
            // Conditions for M-Lock
            && (output.value.MutationCommitment.Some? ==>
                  && output.value.MutationCommitment.value.Identifier == input.Identifier
                  && Structure.MutationCommitment?(output.value.MutationCommitment.value))
               // Conditions for M-Index
            && (output.value.MutationIndex.Some? ==>
                  && output.value.MutationIndex.value.Identifier == input.Identifier
                  && Structure.MutationIndex?(output.value.MutationIndex.value) )
      )
    }

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

    predicate WriteAtomicMutationEnsuresPublicly(
      input: Types.WriteAtomicMutationInput,
      output: Result<Types.WriteAtomicMutationOutput, Types.Error>
    )
    {true}

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

    predicate DeleteMutationEnsuresPublicly(
      input: Types.DeleteMutationInput,
      output: Result<Types.DeleteMutationOutput, Types.Error>
    )
    {true}

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
            // Conditions for Active
            && output.value.ActiveItem.Identifier == input.Identifier
            && Structure.ActiveHierarchicalSymmetricKey?(output.value.ActiveItem)
            && output.value.ActiveItem.EncryptionContext[Structure.TABLE_FIELD] == logicalKeyStoreName
            && KmsArn.ValidKmsArn?(output.value.ActiveItem.KmsArn)
               // Conditions for Beacon
            && output.value.BeaconItem.Identifier == input.Identifier
            && Structure.ActiveHierarchicalSymmetricBeaconKey?(output.value.BeaconItem)
            && output.value.BeaconItem.EncryptionContext[Structure.TABLE_FIELD] == logicalKeyStoreName
            && KmsArn.ValidKmsArn?(output.value.BeaconItem.KmsArn)
               // Conditions for M-Lock
            && (output.value.MutationCommitment.Some? ==>
                  && output.value.MutationCommitment.value.Identifier == input.Identifier
                  && Structure.MutationCommitment?(output.value.MutationCommitment.value))
               // Conditions for M-Index
            && (output.value.MutationIndex.Some? ==>
                  && output.value.MutationIndex.value.Identifier == input.Identifier
                  && Structure.MutationIndex?(output.value.MutationIndex.value) )
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
      && (output.Success? && |output.value.Items| > 0 ==>
            forall item <- output.value.Items ::
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
                    TransactCreateHKey(
                      input.Version,
                      ddbTableName
                    ),
                    //= aws-encryption-sdk-specification/framework/key-store/dynamodb-key-storage.md#writenewencryptedbranchkey
                    //= type=implication
                    //#- PUT:
                    //#  - Item: A [record formatted item](#record-format) constructed from the active input
                    //#  - ConditionExpression: `attribute_not_exists(branch-key-id)`
                    //#  - TableName: the configured Table Name
                    TransactCreateHKey(
                      input.Active,
                      ddbTableName
                    ),
                    //= aws-encryption-sdk-specification/framework/key-store/dynamodb-key-storage.md#writenewencryptedbranchkey
                    //= type=implication
                    //#- PUT:
                    //#  - Item: A [record formatted item](#record-format) constructed from the beacon input
                    //#  - ConditionExpression: `attribute_not_exists(branch-key-id)`
                    //#  - TableName is the configured Table Name
                    TransactCreateHKey(
                      input.Beacon,
                      ddbTableName
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
        TransactCreateHKey(
          input.Version,
          ddbTableName
        ),
        TransactCreateHKey(
          input.Active,
          ddbTableName
        ),
        TransactCreateHKey(
          input.Beacon,
          ddbTableName
        )
      ];

      var transactRequest := DDB.TransactWriteItemsInput(
        TransactItems := items
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
        && (forall k <- input.Active.Item.EncryptionContext.Keys :: DDB.IsValid_AttributeName(k))
        ==>
          && |ddbClient.History.TransactWriteItems| == |old(ddbClient.History.TransactWriteItems)| + 1
          && old(ddbClient.History.TransactWriteItems) < ddbClient.History.TransactWriteItems
          && (output.Success? ==> Seq.Last(ddbClient.History.TransactWriteItems).output.Success?)
          && (Seq.Last(ddbClient.History.TransactWriteItems).output.Failure? ==> output.Failure?)

      ensures
        output.Success?
        ==>
          && (forall k <- input.Version.EncryptionContext.Keys :: DDB.IsValid_AttributeName(k))
          && (forall k <- input.Active.Item.EncryptionContext.Keys :: DDB.IsValid_AttributeName(k))
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
                    TransactCreateHKey(
                      input.Version,
                      ddbTableName
                    ),
                    //= aws-encryption-sdk-specification/framework/key-store/dynamodb-key-storage.md#writenewencryptedbranchkeyversion
                    //= type=implication
                    //#- PUT:
                    //#  - Item: A [record formatted item](#record-format) constructed from the active input
                    //#  - ConditionExpression: `attribute_exists(branch-key-id)`
                    //#  - TableName: the configured Table Name
                    TransactOverwriteHKey(
                      input.Active.Item,
                      input.Active.Old,
                      ddbTableName
                    )
                  ]
                )
    {

      :- Need(
        && (forall k <- input.Version.EncryptionContext.Keys :: DDB.IsValid_AttributeName(k))
        && (forall k <- input.Active.Item.EncryptionContext.Keys :: DDB.IsValid_AttributeName(k))
      , Types.KeyStoreException( message := ErrorMessages.ENCRYPTION_CONTEXT_EXCEEDS_DDB_LIMIT)
      );

      var items: DDB.TransactWriteItemList := [
        TransactCreateHKey(
          input.Version,
          ddbTableName
        ),
        TransactOverwriteHKey(
          input.Active.Item,
          input.Active.Old,
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
      var _ :- transactWriteItemsResponse?
      .MapFailure(e => Types.ComAmazonawsDynamodb(ComAmazonawsDynamodb := e));
      output := Success(Types.WriteNewEncryptedBranchKeyVersionOutput);
    }

    method WriteMutationIndex'(input: Types.WriteMutationIndexInput)
      returns (output: Result<Types.WriteMutationIndexOutput, Types.Error>)
      requires ValidState()
      modifies Modifies - {History}
      decreases Modifies - {History}
      ensures ValidState() && unchanged(History)
      ensures WriteMutationIndexEnsuresPublicly(input, output)
    {
      /** Validate Input */
      :- Need(
        Structure.MutationCommitment?(input.MutationCommitment),
        Types.KeyStorageException(
          message := "Invalid mutation commitment."
        ));
      :- Need(
        Structure.MutationIndex?(input.MutationIndex),
        Types.KeyStorageException(
          message := "Invalid mutation index."
        ));
      /** Construct & Issue DDB Request */
      var ddbRequest := DDB.TransactWriteItemsInput(
        TransactItems :=
          [
            TransactConditionCheckOnMutationCommitment(input.MutationCommitment, ddbTableName),
            TransactCreateMutationIndex(input.MutationIndex, ddbTableName)
          ]
      );
      var ddbResponse? := ddbClient.TransactWriteItems(ddbRequest);

      /** Handle DDB Error */
      // TODO: Wherever we write a Transaction, to explain race failure, we MUST do something like this:
      if (ddbResponse?.Failure? && ddbResponse?.error.TransactionCanceledException?) {
        return Failure(
            Types.KeyStorageException(
              message :=
                "DDB request to Write Mutated Versions failed with DynamoDB's TransactionCanceledException. "
                + "This MAY be caused by a race between hosts mutating the same Branch Key ID. "
                + "The Mutation has NOT completed. "
                + "Table Name: "+ ddbTableName
                + "\tBranch Key ID: " + input.MutationCommitment.Identifier
                + "\tDynamoDB Exception Message: \n" + ddbResponse?.error.Message.UnwrapOr("")));
      }
      var ddbResponse :- ddbResponse?
      .MapFailure(
        (e: DDB.Error) => wrapDdbException(
            e:=e,
            storageOperation:="WriteMutationIndex",
            ddbOperation:="TransactionWriteItems",
            identifier:=input.MutationCommitment.Identifier,
            tableName:=ddbTableName));

      return Success(Types.WriteMutationIndexOutput());
    }


    method GetMutation' ( input: Types.GetMutationInput )
      returns (output: Result<Types.GetMutationOutput, Types.Error>)
      requires ValidState()
      modifies Modifies - {History}
      decreases Modifies - {History}
      ensures ValidState()
      ensures GetMutationEnsuresPublicly(input, output)
      ensures unchanged(History)
      ensures |ddbClient.History.TransactGetItems| == |old(ddbClient.History.TransactGetItems)| + 1
      ensures
        output.Success?
        ==>
          && var tgi := Seq.Last(ddbClient.History.TransactGetItems);
          && tgi.output.Success?
          && tgi.output.value.Responses.Some?
          && var responses := tgi.output.value.Responses.value;
          && |responses| == 2
          && var commitment? := MutationCommitmentFromOptionalItem(responses[0].Item, input.Identifier, ddbTableName);
          && commitment?.Success?
          && var index? := MutationIndexFromOptionalItem(responses[1].Item, input.Identifier, ddbTableName);
          && index?.Success?
          && output.value.MutationCommitment == commitment?.value
          && output.value.MutationIndex == index?.value
      ensures
        && old(ddbClient.History.TransactGetItems) < ddbClient.History.TransactGetItems
    {
      var transactItems: DDB.TransactGetItemList
        := Seq.Map(
        (typeStr: string)
        =>
          // The DDB request is a list of TransactGetItems
          DDB.TransactGetItem(
            Get := DDB.Get(
              Key := DDBKeyForType(typeStr, input.Identifier),
              TableName := ddbTableName)),

        // This is the seq we are mapping over. The DDB Result will be in this order!
        [Structure.MUTATION_COMMITMENT_TYPE, Structure.MUTATION_INDEX_TYPE]);

      var ddbRequest := DDB.TransactGetItemsInput(TransactItems := transactItems);
      var ddbResponse? := ddbClient.TransactGetItems(ddbRequest);

      /** Handle DDB Error */
      var ddbResponse :- ddbResponse?
      .MapFailure((e: DDB.Error) =>
                    wrapDdbException(
                      e:=e,
                      storageOperation:="GetMutation",
                      ddbOperation:="TransactGetItems",
                      identifier:=input.Identifier,
                      tableName:=ddbTableName));

        // SDKs/Smithy-Dafny/Custom Implementations of Storage MAY respond with None or an Empty Map.
        // .NET returns an empty map, Java returns None.
      :- Need(
        ddbResponse.Responses.Some? && (2 == |ddbResponse.Responses.value|),
        Types.KeyStorageException(
          message:=
            "GetMutation: No items returned. "
            + "Branch Key ID: " + input.Identifier
            + "\tTable Name: " + ddbTableName));

      /** Process sensical DDB Response */
      var lockCanidate := ddbResponse.Responses.value[0].Item;
      var lockItem: Option<Types.MutationCommitment> :-
        MutationCommitmentFromOptionalItem(lockCanidate, input.Identifier, ddbTableName);

      var indexCanidate := ddbResponse.Responses.value[1].Item;
      var indexItem: Option<Types.MutationIndex> :-
        MutationIndexFromOptionalItem(indexCanidate, input.Identifier, ddbTableName);

      return Success(
          Types.GetMutationOutput(
            MutationCommitment := lockItem,
            MutationIndex := indexItem));
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
      // @seebees what is this second line about? How can a GetItem have a Write in it's history
      // && old(ddbClient.History.TransactWriteItems) == ddbClient.History.TransactWriteItems

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

    method WriteAtomicMutation'(input: Types.WriteAtomicMutationInput)
      returns (output: Result<Types.WriteAtomicMutationOutput, Types.Error>)
      requires ValidState()
      modifies Modifies - {History}
      decreases Modifies - {History}
      ensures ValidState() && unchanged(History)
      ensures WriteAtomicMutationEnsuresPublicly(input, output)

      ensures output.Failure?
    {
      return Failure(
          Types.KeyStorageException(
            message := "At this time, WriteAtomicMutation is not supported."
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

    function method DDBKeyForType(
      typeStr: string,
      identifier: string
    ): (key: DDB.Key)
    {
      map[
        Structure.BRANCH_KEY_IDENTIFIER_FIELD := DDB.AttributeValue.S(identifier),
        Structure.TYPE_FIELD := DDB.AttributeValue.S(typeStr)
      ]
    }

    // This a TransactGetItems for 5 items
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
      var transactItems: DDB.TransactGetItemList
        := Seq.Map(
        (typeStr: string)
        =>
          // The DDB request is a list of TransactGetItems
          DDB.TransactGetItem(
            Get := DDB.Get(
              Key := DDBKeyForType(typeStr, input.Identifier),
              TableName := ddbTableName)),

        // This is the seq we are mapping over. The DDB Result will be in this order!
        [Structure.MUTATION_COMMITMENT_TYPE, Structure.BRANCH_KEY_ACTIVE_TYPE,
         Structure.BEACON_KEY_TYPE_VALUE, Structure.MUTATION_INDEX_TYPE]);

      var ddbRequest := DDB.TransactGetItemsInput(TransactItems := transactItems);
      var ddbResponse? := ddbClient.TransactGetItems(ddbRequest);

      /** Handle DDB Error */
      var ddbResponse :- ddbResponse?
      .MapFailure((e: DDB.Error) =>
                    wrapDdbException(
                      e:=e,
                      storageOperation:="GetItemsForInitializeMutation",
                      ddbOperation:="TransactGetItems",
                      identifier:=input.Identifier,
                      tableName:=ddbTableName));

        // SDKs/Smithy-Dafny/Custom Implementations of Storage MAY respond with None or an Empty Map.
        // .NET returns an empty map, Java returns None.
      :- Need(
        ddbResponse.Responses.Some? && (4 == |ddbResponse.Responses.value|),
        Types.KeyStorageException(
          message:=
            "GetItemsForInitializeMutation: No items returned. "
            + "Branch Key ID: " + input.Identifier
            + "\tTable Name: " + ddbTableName));

      /** Process sensical DDB Response */
      var lockItem: Option<Types.MutationCommitment> :-
        MutationCommitmentFromOptionalItem(ddbResponse.Responses.value[0].Item, input.Identifier, ddbTableName);

      :- Need(
        ddbResponse.Responses.value[1].Item.Some? && (0 < |ddbResponse.Responses.value[1].Item.value|),
        Types.KeyStorageException(
          message:=
            "GetItemsForInitializeMutation: Could not find the ACTIVE Item. "
            + "Branch Key ID: " + input.Identifier
            + "\tTable Name: " + ddbTableName));
      var activeItem: Types.EncryptedHierarchicalKey :-
        EncryptedHierarchicalKeyFromItem(
          ddbResponse.Responses.value[1].Item.value, logicalKeyStoreName, input.Identifier, ddbTableName);

      :- Need(
        ddbResponse.Responses.value[2].Item.Some?  && (0 < |ddbResponse.Responses.value[2].Item.value|),
        Types.KeyStorageException(
          message:=
            "GetItemsForInitializeMutation: Could not find the Beacon Item. "
            + "Branch Key ID: " + input.Identifier
            + "\tTable Name: " + ddbTableName));
      var beaconItem: Types.EncryptedHierarchicalKey :-
        EncryptedHierarchicalKeyFromItem(
          ddbResponse.Responses.value[2].Item.value, logicalKeyStoreName, input.Identifier, ddbTableName);

      var indexItem: Option<Types.MutationIndex> :-
        MutationIndexFromOptionalItem(ddbResponse.Responses.value[3].Item, input.Identifier, ddbTableName);

        /** Validate DDB Responses */
      :- Need(
        && Structure.ActiveHierarchicalSymmetricKey?(activeItem),
        Types.KeyStorageException(
          message:=
            "Item returned for the ACTIVE is malformed. TableName: " + ddbTableName + "\tBranch Key ID: " + input.Identifier
        ));

      :- Need(
        && Structure.ActiveHierarchicalSymmetricBeaconKey?(beaconItem),
        Types.KeyStorageException(
          message:=
            "Item returned for Beacon Key is malformed. TableName: " + ddbTableName + "\tBranch Key ID: " + input.Identifier
        ));

      return Success(
          Types.GetItemsForInitializeMutationOutput(
            ActiveItem := activeItem,
            BeaconItem := beaconItem,
            MutationCommitment := lockItem,
            MutationIndex := indexItem
          ));
    }

    /** A transaction write for 5 items, conditioned on No Mutation Lock Or Index exsisting for Identifier.*/
    /** One of the items is a new Active; it is conditioned on the oldActive's enc still being present at write time.*/
    method WriteInitializeMutation' ( input: Types.WriteInitializeMutationInput )
      returns (output: Result<Types.WriteInitializeMutationOutput, Types.Error>)
      requires ValidState()
      modifies Modifies - {History}
      decreases Modifies - {History}
      ensures ValidState() && unchanged(History)
      ensures WriteInitializeMutationEnsuresPublicly(input, output)

    {
      :- Need(
        Structure.MutationCommitment?(input.MutationCommitment),
        Types.KeyStorageException(
          message := "Invalid mutation commitment."
        ));
      :- Need(
        Structure.MutationIndex?(input.MutationIndex),
        Types.KeyStorageException(
          message := "Invalid mutation index."
        ));

        /** Validate Inputs can be mapped to DDB Items */
      :- Need(
        && (forall k <- input.Active.Item.EncryptionContext.Keys :: DDB.IsValid_AttributeName(k)),
        Types.KeyStorageException( message := ErrorMessages.ENCRYPTION_CONTEXT_EXCEEDS_DDB_LIMIT)
      );
      :- Need(
        && (forall k <- input.Beacon.Item.EncryptionContext.Keys :: DDB.IsValid_AttributeName(k)),
        Types.KeyStorageException( message := ErrorMessages.ENCRYPTION_CONTEXT_EXCEEDS_DDB_LIMIT)
      );

      :- Need(
        match input.Version {
          case rotate(item) => (forall k <- item.EncryptionContext.Keys :: DDB.IsValid_AttributeName(k))
          case mutate(overWrite) => (forall k <- overWrite.Item.EncryptionContext.Keys :: DDB.IsValid_AttributeName(k))
        },
        Types.KeyStorageException( message := ErrorMessages.ENCRYPTION_CONTEXT_EXCEEDS_DDB_LIMIT)
      );

      /** Convert Inputs to DDB Items.*/
      var items: DDB.TransactWriteItemList := [
        TransactOverwriteHKey(
          input.Active.Item,
          input.Active.Old,
          ddbTableName
        ),
        TransactOverwriteHKey(
          input.Beacon.Item,
          input.Beacon.Old,
          ddbTableName
        ),
        TransactCreateMutationCommitment(
          input.MutationCommitment,
          ddbTableName
        ),
        TransactCreateMutationIndex(
          input.MutationIndex,
          ddbTableName),
        if input.Version.rotate?
        then TransactCreateHKey(
               input.Version.rotate,
               ddbTableName
             )
        else TransactOverwriteHKey(
            input.Version.mutate.Item,
            input.Version.mutate.Old,
            ddbTableName
          )
      ];
      var transactRequest := DDB.TransactWriteItemsInput(
        TransactItems := items
      );

      var transactWriteItemsResponse? := ddbClient.TransactWriteItems(transactRequest);
      // TODO-Mutations-FF: we need to check the cancellation reason for
      // ConditionalCheckFailed on the Active item (VersionRaceException)
      // OR the Mutation Lock (MutationCommitmentException)
      // OR something else.
      var _ :- transactWriteItemsResponse?
      .MapFailure(e => wrapDdbException(
                      e:=e,
                      storageOperation:="WriteInitializeMutation",
                      ddbOperation:="TransactWriteItems",
                      identifier:=input.Active.Item.Identifier,
                      tableName:=ddbTableName));
      // This is a Smithy Modeled Operation; the output MUST be a Structure
      output := Success(Types.WriteInitializeMutationOutput());
    }

    static const queryForVersionsKeyExpression: DDB.KeyExpression := "#pk = :pk AND begins_with( #sk, :decryptOnlyPrefix )"

    method QueryForVersions' ( input: Types.QueryForVersionsInput )
      returns (output: Result<Types.QueryForVersionsOutput, Types.Error>)
      requires ValidState()
      modifies Modifies - {History}
      decreases Modifies - {History}
      ensures ValidState() && unchanged(History)
      ensures QueryForVersionsEnsuresPublicly(input, output)
    {
      /** Construct & Issue DDB Request */
      var exclusiveStartKey: Option<DDB.Key> := None;
      if (input.ExclusiveStartKey.Some?) {
        var decodedLastKey :- BlobToExclusiveStartKey(
          input.ExclusiveStartKey.value,
          input.Identifier);
        exclusiveStartKey := Some(decodedLastKey);
      }
      :- Need(0 < input.PageSize,
              Types.KeyStorageException(message:="DynamoDB Encrypted Key Storage will not Query for page size of 0."));
      var exprAttributeValues: DDB.ExpressionAttributeValueMap := map[
        ":pk" := DDB.AttributeValue.S(input.Identifier),
        ":decryptOnlyPrefix" := DDB.AttributeValue.S("branch:version:")];
      var ddbRequest := DDB.QueryInput(
        TableName := ddbTableName,
        Limit := Some(input.PageSize),
        ConsistentRead := Some(true),
        ExclusiveStartKey := exclusiveStartKey,
        KeyConditionExpression := Some(queryForVersionsKeyExpression),
        ExpressionAttributeNames := Some(INDEX_EXP_ATT_NAMES),
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
        lastKeyBlob :- LastEvaluatedKeyToBlob(ddbResponse.LastEvaluatedKey.value);
      }
      if (ddbResponse.Items.None? || ( |ddbResponse.Items.value| == 0) ) {
        return Success(Types.QueryForVersionsOutput(
                         ExclusiveStartKey := lastKeyBlob,
                         Items := []
                       ));
      }

      /* Map DDB items to Branch Keys.*/
      var branchKeys: seq<Types.EncryptedHierarchicalKey> :- Seq.MapWithResult(
        // Dafny requires the type of the element being mapped over, or it feaks out.
        (item: DDB.AttributeMap)
        =>
          /* Convert DDB Item to Branch Key. */
          var branchKey :- EncryptedHierarchicalKeyFromItem(item, logicalKeyStoreName, input.Identifier, ddbTableName);
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
            ExclusiveStartKey := lastKeyBlob,
            Items := branchKeys
          ));
    }

    /** Transaction OverWrite up to 98 Decryt Only Items,
       with a Global Condition on the M-Commitment.
       The Mutation Index is also updated via an Optimistic Lock.
       If the mutation is complete, the M-Commitment & M-Index are deleted.
     */
    method WriteMutatedVersions' ( input: Types.WriteMutatedVersionsInput )
      returns (output: Result<Types.WriteMutatedVersionsOutput, Types.Error>)
      requires && ValidState()
      modifies Modifies - {History}
      decreases Modifies - {History}
      ensures unchanged(History) && ValidState()
      ensures WriteMutatedVersionsEnsuresPublicly(input, output)
    {
      /** Validate Input */
      :- Need(
        |input.Items| < DDB_MAX_MUTATION_WRITE_PAGE_SIZE,
        Types.KeyStorageException(message:="DynamoDB Encrypted Key Storage can only write page sizes less than " + DDB_MAX_MUTATION_WRITE_PAGE_SIZE_str + "."
        ));
      :- Need(
        0 < |input.MutationCommitment.Original|,
        Types.KeyStorageException(message:="Original State MUST NOT be empty."
        ));
      :- Need(
        0 < |input.MutationCommitment.Terminal|,
        Types.KeyStorageException(message:="Terminal State MUST NOT be empty."
        ));
      :- Need(
        Structure.MutationIndex?(input.MutationIndex.Index),
        Types.KeyStorageException(message:="Mutation Index MUST be valid."
        ));

      /** Convert Items to DDB */
      var items: seq<DDB.TransactWriteItem> :- Seq.MapWithResult(
        (branchKey: Types.OverWriteEncryptedHierarchicalKey)
        =>
          /* All Attribute Names MUST comply with DDB's limits.*/
          /* Attribute Names are the "keys" of the Encryption Context.*/
          :- Need(
               && (forall k <- branchKey.Item.EncryptionContext.Keys :: DDB.IsValid_AttributeName(k)),
               Types.KeyStorageException( message := ErrorMessages.ENCRYPTION_CONTEXT_EXCEEDS_DDB_LIMIT)
             );
          /* Only Version, or Decrypt Only, items are permitted.*/
          :- Need(
               branchKey.Item.Type.HierarchicalSymmetricVersion?,
               Types.KeyStorageException(
                 message :=
                   "WriteMutatedVersions of DynamoDB Encrypted Key Storage ONLY writes Decrypt Only Items to Storage. "
                   + "Encountered a non-Decrypt Only Item."
               ));
          /* The branch key is valid for DDB; create a Put request.*/
          var overWrite := TransactOverwriteHKey(
                             branchKey.Item,
                             branchKey.Old,
                             ddbTableName);
          Success(overWrite),
        input.Items);

      var mLock := input.MutationCommitment;
      var mLockAction := if input.EndMutation
      then TransactConditionalDeleteMutationCommitment(mLock, ddbTableName)
      else TransactConditionCheckOnMutationCommitment(mLock, ddbTableName);
      var mIndex := input.MutationIndex;
      var mIndexAction :=
        if input.EndMutation
        then TransactConditionalDeleteMutationIndex(mIndex.Index, mIndex.Old, ddbTableName)
        else TransactOverwriteMutationIndex(mIndex.Index, mIndex.Old, ddbTableName);
      /** Construct & Issue DDB Request */
      var ddbRequest := DDB.TransactWriteItemsInput(
        TransactItems := [mLockAction,  mIndexAction] + items
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
                + "\tBranch Key ID: " + mLock.Identifier
                + "\tDDB Exception Message: \n" + ddbResponse?.error.Message.UnwrapOr("")));
      }
      var ddbResponse :- ddbResponse?
      .MapFailure(
        (e: DDB.Error) => wrapDdbException(
            e:=e,
            storageOperation:="WriteMutatedVersions",
            ddbOperation:="TransactionWriteItems",
            identifier:=mLock.Identifier,
            tableName:=ddbTableName));

      return Success(Types.WriteMutatedVersionsOutput());
    }

    method DeleteMutation' ( input: Types.DeleteMutationInput )
      returns (output: Result<Types.DeleteMutationOutput, Types.Error>)
      requires ValidState()
      modifies Modifies - {History}
      decreases Modifies - {History}
      ensures ValidState() && unchanged(History)
      ensures DeleteMutationEnsuresPublicly(input, output)

      ensures !Structure.MutationCommitment?(input.MutationCommitment) ==> output.Failure?
      ensures
        && Structure.MutationCommitment?(input.MutationCommitment) ==>(
            && |ddbClient.History.TransactWriteItems| == |old(ddbClient.History.TransactWriteItems)| + 1
            && old(ddbClient.History.TransactWriteItems) < ddbClient.History.TransactWriteItems
            && (output.Success? ==> Seq.Last(ddbClient.History.TransactWriteItems).output.Success?)
            && (Seq.Last(ddbClient.History.TransactWriteItems).output.Failure? ==> output.Failure?))

      ensures
        output.Success?
        ==>
          && Seq.Last(ddbClient.History.TransactWriteItems).input
             == DDB.TransactWriteItemsInput(
                  TransactItems := [
                    TransactConditionalDeleteMutationCommitment(
                      input.MutationCommitment,
                      ddbTableName),
                    TransactNoConditionDeleteMutationIndex(
                      input.MutationCommitment.Identifier,
                      ddbTableName
                    )
                  ]
                )
    {
      /** Validate Input */
      :- Need(
        Structure.MutationCommitment?(input.MutationCommitment),
        Types.KeyStorageException(message:="Mutation Index must be valid."));

      var items: DDB.TransactWriteItemList := [
        TransactConditionalDeleteMutationCommitment(
          input.MutationCommitment,
          ddbTableName),
        TransactNoConditionDeleteMutationIndex(
          input.MutationCommitment.Identifier,
          ddbTableName
        )
      ];

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
                "DDB request to Delete Mutation Lock & Index was failed by DDB with TransactionCanceledException. "
                + "This MAY be caused by a race between hosts mutating the same Branch Key ID. "
                + "The Mutation has NOT completed. "
                + "Table Name: "+ ddbTableName
                + "\tBranch Key ID: " + input.MutationCommitment.Identifier
                + "\tDDB Exception Message: \n" + ddbResponse?.error.Message.UnwrapOr("")));
      }
      var ddbResponse :- ddbResponse?
      .MapFailure(
        (e: DDB.Error) => wrapDdbException(
            e:=e,
            storageOperation:="DeleteMutation",
            ddbOperation:="TransactionWriteItems",
            identifier:=input.MutationCommitment.Identifier,
            tableName:=ddbTableName));
      return Success(Types.DeleteMutationOutput());
    }
  }

  function method TransactCreateHKey(
    encryptedKey: Types.EncryptedHierarchicalKey,
    tableName: DDB.TableName
  ): (output: DDB.TransactWriteItem)
    requires (forall k <- encryptedKey.EncryptionContext.Keys :: DDB.IsValid_AttributeName(k))
  {
    DDB.TransactWriteItem(
      Put := Some(
        DDB.Put(
          Item := ToAttributeMap(encryptedKey),
          TableName := tableName,
          ConditionExpression := Some(BRANCH_KEY_NOT_EXIST_CONDITION),
          ExpressionAttributeNames := Some(BRANCH_KEY_EXISTS_EXPRESSION_ATTRIBUTE_NAMES)))
    )
  }

  function method TransactCreateMutationCommitment(
    mutationLock: Types.MutationCommitment,
    tableName: DDB.TableName
  ): (output: DDB.TransactWriteItem)
    requires Structure.MutationCommitment?(mutationLock)
  {
    DDB.TransactWriteItem(
      Put := Some(
        DDB.Put(
          Item := Structure.MutationCommitmentToAttributeMap(mutationLock),
          TableName := tableName,
          ConditionExpression := Some(BRANCH_KEY_NOT_EXIST_CONDITION),
          ExpressionAttributeNames := Some(BRANCH_KEY_EXISTS_EXPRESSION_ATTRIBUTE_NAMES)))
    )
  }

  function method TransactCreateMutationIndex(
    mutationIndex: Types.MutationIndex,
    tableName: DDB.TableName
  ): (output: DDB.TransactWriteItem)
    requires Structure.MutationIndex?(mutationIndex)
  {
    DDB.TransactWriteItem(
      Put := Some(
        DDB.Put(
          Item := Structure.MutationIndexToAttributeMap(mutationIndex),
          TableName := tableName,
          ConditionExpression := Some(BRANCH_KEY_NOT_EXIST_CONDITION),
          ExpressionAttributeNames := Some(BRANCH_KEY_EXISTS_EXPRESSION_ATTRIBUTE_NAMES)))
    )
  }

  function method TransactConditionalDeleteMutationCommitment(
    mLock: Types.MutationCommitment,
    tableName: DDB.TableName
  ): (output: DDB.TransactWriteItem)
  {
    var check := checkForMutationCommitment(mLock);
    DDB.TransactWriteItem(
      Delete := Some(
        DDB.Delete(
          Key :=
            map[
              Structure.BRANCH_KEY_IDENTIFIER_FIELD := DDB.AttributeValue.S(mLock.Identifier),
              Structure.TYPE_FIELD := DDB.AttributeValue.S(Structure.MUTATION_COMMITMENT_TYPE)
            ],
          TableName := tableName,
          ConditionExpression := Some(check.ConditionExpression),
          ExpressionAttributeNames := Some(check.ExpressionAttributeNames),
          ExpressionAttributeValues := Some(check.ExpressionAttributeValues)
        )))
  }

  function method TransactOverwriteHKey(
    item: Types.EncryptedHierarchicalKey,
    oldItem: Types.EncryptedHierarchicalKey,
    tableName: DDB.TableName
  ): (output: DDB.TransactWriteItem)
    requires (forall k <- item.EncryptionContext.Keys :: DDB.IsValid_AttributeName(k))
  {
    var check := checkForOldEnc(oldItem.CiphertextBlob);
    DDB.TransactWriteItem(
      Put := Some(
        DDB.Put(
          Item := ToAttributeMap(item),
          TableName := tableName,
          ConditionExpression := Some(check.ConditionExpression),
          ExpressionAttributeNames := Some(check.ExpressionAttributeNames),
          ExpressionAttributeValues := Some(check.ExpressionAttributeValues)
        )))
  }

  function method TransactOverwriteMutationIndex(
    index: Types.MutationIndex,
    oldIndex: Types.MutationIndex,
    tableName: DDB.TableName
  ): (output: DDB.TransactWriteItem)
    requires Structure.MutationIndex?(index)
  {
    var check := ConditionForMutationIndex(oldIndex);
    DDB.TransactWriteItem(
      Put := Some(
        DDB.Put(
          Item := Structure.MutationIndexToAttributeMap(index),
          TableName := tableName,
          ConditionExpression := Some(check.ConditionExpression),
          ExpressionAttributeNames := Some(check.ExpressionAttributeNames),
          ExpressionAttributeValues := Some(check.ExpressionAttributeValues)
        )))
  }

  function method TransactConditionalDeleteMutationIndex(
    index: Types.MutationIndex,
    oldIndex: Types.MutationIndex,
    tableName: DDB.TableName
  ): (output: DDB.TransactWriteItem)
    requires Structure.MutationIndex?(index)
  {
    var check := ConditionForMutationIndex(oldIndex);
    DDB.TransactWriteItem(
      Delete := Some(
        DDB.Delete(
          Key :=
            map[
              Structure.BRANCH_KEY_IDENTIFIER_FIELD := DDB.AttributeValue.S(index.Identifier),
              Structure.TYPE_FIELD := DDB.AttributeValue.S(Structure.MUTATION_INDEX_TYPE)
            ],
          TableName := tableName,
          ConditionExpression := Some(check.ConditionExpression),
          ExpressionAttributeNames := Some(check.ExpressionAttributeNames),
          ExpressionAttributeValues := Some(check.ExpressionAttributeValues)
        )))
  }

  function method TransactNoConditionDeleteMutationIndex(
    identifier: string,
    tableName: DDB.TableName
  ): (output: DDB.TransactWriteItem)
  {
    DDB.TransactWriteItem(
      Delete := Some(
        DDB.Delete(
          Key :=
            map[
              Structure.BRANCH_KEY_IDENTIFIER_FIELD := DDB.AttributeValue.S(identifier),
              Structure.TYPE_FIELD := DDB.AttributeValue.S(Structure.MUTATION_INDEX_TYPE)
            ],
          TableName := tableName
        )))
  }

  datatype check = | check(
    nameonly ConditionExpression: DDB.ConditionExpression ,
    nameonly ExpressionAttributeNames: DDB.ExpressionAttributeNameMap ,
    nameonly ExpressionAttributeValues: DDB.ExpressionAttributeValueMap)

  /** Assert the cipherText of the Active Item has not changed since it was read.*/
  function method checkForOldEnc(
    oldCiphertextBlob: seq<Types.UInt.uint8>
  ): (output: check)
  {
    check(
      ConditionExpression := "attribute_exists(#pk) AND " + Structure.ENC_FIELD + " = :encOld",
      ExpressionAttributeNames := map["#pk" := Structure.BRANCH_KEY_IDENTIFIER_FIELD],
      ExpressionAttributeValues := map[":encOld" := DDB.AttributeValue.B(oldCiphertextBlob)])
  }

  function method checkForMutationCommitment(
    mLock: Types.MutationCommitment
  ): (output: check)
  {
    check(
      ConditionExpression :=
        "attribute_exists(#pk)"
        + " AND original = :original"
        + " AND terminal = :terminal"
        + " AND " + Structure.ENC_FIELD + " = :encOld"
        + " AND #uuid = :" + Structure.M_UUID,
      ExpressionAttributeNames := map[
        "#pk" := Structure.BRANCH_KEY_IDENTIFIER_FIELD, // "#pk":="branch-key-id"
        "#uuid" := Structure.M_UUID // "#uuid" := "uuid"
      ],
      ExpressionAttributeValues :=
        map[
          ":original" := DDB.AttributeValue.B(mLock.Original),
          ":terminal" := DDB.AttributeValue.B(mLock.Terminal),
          ":encOld" := DDB.AttributeValue.B(mLock.CiphertextBlob),
          ":" + Structure.M_UUID := DDB.AttributeValue.S(mLock.UUID)
        ]
    )
  }

  /** Assert a Mutation Lock exists for Branch Key ID, with Original and Terminal as expected.*/
  /** For use with WriteMutatedVersions. */
  function method TransactConditionCheckOnMutationCommitment(
    mLock: Types.MutationCommitment,
    tableName: DDB.TableName
  ): (output: DDB.TransactWriteItem)
  {
    var check := checkForMutationCommitment(mLock);
    var conditionCheck
      :=
      DDB.ConditionCheck(
        Key := map[
          Structure.BRANCH_KEY_IDENTIFIER_FIELD := DDB.AttributeValue.S(mLock.Identifier),
          Structure.TYPE_FIELD := DDB.AttributeValue.S(Structure.MUTATION_COMMITMENT_TYPE)
        ],
        TableName := tableName,
        ConditionExpression := check.ConditionExpression,
        ExpressionAttributeNames := Some(check.ExpressionAttributeNames),
        ExpressionAttributeValues := Some(check.ExpressionAttributeValues)
      );
    DDB.TransactWriteItem(ConditionCheck := Some(conditionCheck))
  }

  function method ConditionForMutationIndex(
    oldIndex: Types.MutationIndex
  ): (output: check)
  {
    check(
      ConditionExpression :=
        "attribute_exists(#pk)"
        + " AND " + Structure.M_PAGE_INDEX + " = :" + Structure.M_PAGE_INDEX + "Old"
        + " AND " + Structure.ENC_FIELD + " = :" + Structure.ENC_FIELD + "Old"
        + " AND #uuid = :" + Structure.M_UUID,
      ExpressionAttributeNames := map[
        "#pk" := Structure.BRANCH_KEY_IDENTIFIER_FIELD, // "#pk":="branch-key-id"
        "#uuid" := Structure.M_UUID // "#uuid" := "uuid"
      ],
      ExpressionAttributeValues :=
        map[
          ":" + Structure.M_PAGE_INDEX + "Old" := DDB.AttributeValue.B(oldIndex.PageIndex),
          ":" + Structure.ENC_FIELD + "Old" := DDB.AttributeValue.B(oldIndex.CiphertextBlob),
          ":" + Structure.M_UUID := DDB.AttributeValue.S(oldIndex.UUID)
        ]
    )
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
      case OpaqueWithText(obj, objMessage) => Types.OpaqueWithText(obj, objMessage)
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
