// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../Model/AwsCryptographyKeyStoreTypes.dfy"
include "Structure.dfy"
include "KmsArn.dfy"

module {:options "/functionSyntax:4"} StorageHelpers {
  import opened Wrappers
  import Seq
  import Types = AwsCryptographyKeyStoreTypes
  import UTF8
  import Structure
  import String = StandardLibrary.String
  import DDB = Com.Amazonaws.Dynamodb
  import KmsArn

  const ToAttributeMap := Structure.ToAttributeMap
  const ToEncryptedHierarchicalKey := Structure.ToEncryptedHierarchicalKey

  function MutationCommitmentFromOptionalItem(
    item?: Option<DDB.Types.AttributeMap>,
    identifier: string,
    ddbTableName: string
  ): (output: Result<Option<Types.MutationCommitment>, Types.Error>)
    ensures output.Success? && output.value.Some? ==>
              (output.value.value.Identifier == identifier)
  {
    if (item?.None? || (|item?.value| == 0))
    then Success(None)
    else
      var mLock :- MutationCommitmentFromItem(item?.value, identifier, ddbTableName);
      Success(Some(mLock))
  }

  function MutationCommitmentFromItem(
    item: DDB.Types.AttributeMap,
    identifier: string,
    ddbTableName: string
  ): (output: Result<Types.MutationCommitment, Types.Error>)
    ensures output.Success? ==>
              && (output.value.Identifier == identifier)
              && Structure.MutationCommitmentAttribute?(item)
              && output.value == Structure.ToMutationCommitment(item)
    ensures !Structure.MutationCommitmentAttribute?(item) ==> output.Failure?
  {
    :- Need(
         Structure.MutationCommitmentAttribute?(item),
         Types.KeyStorageException(
           message:="Malformed Mutation Lock encountered. TableName: "
           + ddbTableName + "\tBranch Key ID: " + identifier)
       );
    var mLock := Structure.ToMutationCommitment(item);
    :- Need(
         mLock.Identifier == identifier,
         Types.KeyStorageException(
           message:=
             "Mutation Lock returned by DDB is for wrong Branch Key ID. "
             + "TableName: " + ddbTableName
             + "\tRequested Branch Key ID: " + identifier
             + "\tReturned Branch Key ID: " + mLock.Identifier)
       );
    Success(mLock)
  }

  function MutationIndexFromOptionalItem(
    item?: Option<DDB.Types.AttributeMap>,
    identifier: string,
    ddbTableName: string
  ): (output: Result<Option<Types.MutationIndex>, Types.Error>)
    ensures output.Success? && output.value.Some? ==>
              (output.value.value.Identifier == identifier)
  {
    if (item?.None? || (|item?.value| == 0))
    then Success(None)
    else
      var mIndex :- MutationIndexFromItem(item?.value, identifier, ddbTableName);
      Success(Some(mIndex))
  }

  function MutationIndexFromItem(
    item: DDB.Types.AttributeMap,
    identifier: string,
    ddbTableName: string
  ): (output: Result<Types.MutationIndex, Types.Error>)
    ensures output.Success? ==>
              && (output.value.Identifier == identifier)
              && Structure.MutationIndexAttribute?(item)
              && output.value == Structure.ToMutationIndex(item)
    ensures !Structure.MutationIndexAttribute?(item) ==> output.Failure?
  {
    :- Need(
         Structure.MutationIndexAttribute?(item),
         Types.KeyStorageException(
           message:="Malformed Mutation Index encountered. TableName: "
           + ddbTableName + "\tBranch Key ID: " + identifier)
       );
    var mIndex := Structure.ToMutationIndex(item);
    :- Need(
         mIndex.Identifier == identifier,
         Types.KeyStorageException(
           message:=
             "Mutation Index returned by DDB is for wrong Branch Key ID. "
             + "TableName: " + ddbTableName
             + "\tRequested Branch Key ID: " + identifier
             + "\tReturned Branch Key ID: " + mIndex.Identifier)
       );
    Success(mIndex)
  }

  function EncryptedHierarchicalKeyFromItem(
    item: DDB.Types.AttributeMap,
    logicalKeyStoreName: string,
    identifier: string,
    ddbTableName: string
  ): (output: Result<Types.EncryptedHierarchicalKey, Types.Error>)
    ensures output.Success?
            ==>
              && Structure.EncryptedHierarchicalKeyFromStorage?(output.value)
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
    var branchKey := ToEncryptedHierarchicalKey(item, logicalKeyStoreName);
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

  function BlobToExclusiveStartKey(
    blob: seq<Types.UInt.uint8>,
    identifier: string
  ): (output: Result<DDB.Types.Key,Types.Error>)
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
    var exclusiveStartKey: DDB.Types.Key :=
      map[
        Structure.BRANCH_KEY_IDENTIFIER_FIELD := DDB.Types.AttributeValue.S(identifier),
        Structure.TYPE_FIELD := DDB.Types.AttributeValue.S(versionStr)
      ];
    Success(exclusiveStartKey)
  }

  function LastEvaluatedKeyToBlob(lastKey: DDB.Types.Key): (output: Result<seq<Types.UInt.uint8>, Types.Error>)
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
}
