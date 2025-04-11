// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
include "../../../../StandardLibrary/src/Index.dfy"
include "../../../../ComAmazonawsDynamodb/src/Index.dfy"
include "../../../../ComAmazonawsKms/src/Index.dfy"
module {:extern "software.amazon.cryptography.keystore.internaldafny.types" } AwsCryptographyKeyStoreTypes
{
  import opened Wrappers
  import opened StandardLibrary.UInt
  import opened UTF8
  import ComAmazonawsDynamodbTypes
  import ComAmazonawsKmsTypes
    // Generic helpers for verification of mock/unit tests.
  datatype DafnyCallEvent<I, O> = DafnyCallEvent(input: I, output: O)

  // Begin Generated Types

  datatype ActiveHierarchicalSymmetric = | ActiveHierarchicalSymmetric (
    nameonly Version: string
  )
  datatype ActiveHierarchicalSymmetricBeacon = | ActiveHierarchicalSymmetricBeacon (

                                               )
  datatype AwsKms = | AwsKms (
    nameonly grantTokens: Option<GrantTokenList> := Option.None ,
    nameonly kmsClient: Option<ComAmazonawsKmsTypes.IKMSClient> := Option.None
  )
  datatype BeaconKeyMaterials = | BeaconKeyMaterials (
    nameonly beaconKeyIdentifier: string ,
    nameonly encryptionContext: EncryptionContext ,
    nameonly beaconKey: Option<Secret> := Option.None ,
    nameonly hmacKeys: Option<HmacKeyMap> := Option.None
  )
  datatype BranchKeyMaterials = | BranchKeyMaterials (
    nameonly branchKeyIdentifier: string ,
    nameonly branchKeyVersion: Utf8Bytes ,
    nameonly encryptionContext: EncryptionContext ,
    nameonly branchKey: Secret
  )
  datatype CreateKeyInput = | CreateKeyInput (
    nameonly branchKeyIdentifier: Option<string> := Option.None ,
    nameonly encryptionContext: Option<EncryptionContext> := Option.None
  )
  datatype CreateKeyOutput = | CreateKeyOutput (
    nameonly branchKeyIdentifier: string
  )
  datatype CreateKeyStoreInput = | CreateKeyStoreInput (

                                 )
  datatype CreateKeyStoreOutput = | CreateKeyStoreOutput (
    nameonly tableArn: ComAmazonawsDynamodbTypes.TableArn
  )
  datatype DeleteMutationInput = | DeleteMutationInput (
    nameonly MutationCommitment: MutationCommitment
  )
  datatype DeleteMutationOutput = | DeleteMutationOutput (

                                  )
  datatype Discovery = | Discovery (

                       )
  datatype DynamoDBTable = | DynamoDBTable (
    nameonly ddbTableName: ComAmazonawsDynamodbTypes.TableName ,
    nameonly ddbClient: Option<ComAmazonawsDynamodbTypes.IDynamoDBClient> := Option.None
  )
  datatype EncryptedHierarchicalKey = | EncryptedHierarchicalKey (
    nameonly Identifier: string ,
    nameonly Type: HierarchicalKeyType ,
    nameonly CreateTime: string ,
    nameonly KmsArn: string ,
    nameonly EncryptionContext: EncryptionContextString ,
    nameonly CiphertextBlob: seq<uint8>
  )
  type EncryptedHierarchicalKeys = seq<EncryptedHierarchicalKey>
  type EncryptionContext = map<Utf8Bytes, Utf8Bytes>
  type EncryptionContextString = map<string, string>
  datatype GetActiveBranchKeyInput = | GetActiveBranchKeyInput (
    nameonly branchKeyIdentifier: string
  )
  datatype GetActiveBranchKeyOutput = | GetActiveBranchKeyOutput (
    nameonly branchKeyMaterials: BranchKeyMaterials
  )
  datatype GetBeaconKeyInput = | GetBeaconKeyInput (
    nameonly branchKeyIdentifier: string
  )
  datatype GetBeaconKeyOutput = | GetBeaconKeyOutput (
    nameonly beaconKeyMaterials: BeaconKeyMaterials
  )
  datatype GetBranchKeyVersionInput = | GetBranchKeyVersionInput (
    nameonly branchKeyIdentifier: string ,
    nameonly branchKeyVersion: string
  )
  datatype GetBranchKeyVersionOutput = | GetBranchKeyVersionOutput (
    nameonly branchKeyMaterials: BranchKeyMaterials
  )
  datatype GetEncryptedActiveBranchKeyInput = | GetEncryptedActiveBranchKeyInput (
    nameonly Identifier: string
  )
  datatype GetEncryptedActiveBranchKeyOutput = | GetEncryptedActiveBranchKeyOutput (
    nameonly Item: EncryptedHierarchicalKey
  )
  datatype GetEncryptedBeaconKeyInput = | GetEncryptedBeaconKeyInput (
    nameonly Identifier: string
  )
  datatype GetEncryptedBeaconKeyOutput = | GetEncryptedBeaconKeyOutput (
    nameonly Item: EncryptedHierarchicalKey
  )
  datatype GetEncryptedBranchKeyVersionInput = | GetEncryptedBranchKeyVersionInput (
    nameonly Identifier: string ,
    nameonly Version: string
  )
  datatype GetEncryptedBranchKeyVersionOutput = | GetEncryptedBranchKeyVersionOutput (
    nameonly Item: EncryptedHierarchicalKey
  )
  datatype GetItemsForInitializeMutationInput = | GetItemsForInitializeMutationInput (
    nameonly Identifier: string
  )
  datatype GetItemsForInitializeMutationOutput = | GetItemsForInitializeMutationOutput (
    nameonly ActiveItem: EncryptedHierarchicalKey ,
    nameonly BeaconItem: EncryptedHierarchicalKey ,
    nameonly MutationCommitment: Option<MutationCommitment> := Option.None ,
    nameonly MutationIndex: Option<MutationIndex> := Option.None
  )
  datatype GetKeyStorageInfoInput = | GetKeyStorageInfoInput (

                                    )
  datatype GetKeyStorageInfoOutput = | GetKeyStorageInfoOutput (
    nameonly Name: Utf8Bytes ,
    nameonly LogicalName: Utf8Bytes
  )
  datatype GetKeyStoreInfoOutput = | GetKeyStoreInfoOutput (
    nameonly keyStoreId: string ,
    nameonly keyStoreName: string ,
    nameonly logicalKeyStoreName: string ,
    nameonly grantTokens: GrantTokenList ,
    nameonly kmsConfiguration: KMSConfiguration
  )
  datatype GetMutationInput = | GetMutationInput (
    nameonly Identifier: string
  )
  datatype GetMutationOutput = | GetMutationOutput (
    nameonly MutationCommitment: Option<MutationCommitment> := Option.None ,
    nameonly MutationIndex: Option<MutationIndex> := Option.None
  )
  type GrantTokenList = seq<string>
  datatype HierarchicalKeyType =
    | ActiveHierarchicalSymmetricVersion(ActiveHierarchicalSymmetricVersion: ActiveHierarchicalSymmetric)
    | HierarchicalSymmetricVersion(HierarchicalSymmetricVersion: HierarchicalSymmetric)
    | ActiveHierarchicalSymmetricBeacon(ActiveHierarchicalSymmetricBeacon: ActiveHierarchicalSymmetricBeacon)
  datatype HierarchicalSymmetric = | HierarchicalSymmetric (
    nameonly Version: string
  )
  datatype HierarchyVersion =
    | v1
    | v2
  type HmacKeyMap = map<string, Secret>
  datatype KeyManagement =
    | kms(kms: AwsKms)
  class IKeyStorageInterfaceCallHistory {
    ghost constructor() {
      WriteNewEncryptedBranchKey := [];
      GetMutation := [];
      GetItemsForInitializeMutation := [];
      GetKeyStorageInfo := [];
      GetEncryptedBranchKeyVersion := [];
      WriteAtomicMutation := [];
      GetEncryptedBeaconKey := [];
      GetEncryptedActiveBranchKey := [];
      WriteMutatedVersions := [];
      WriteInitializeMutation := [];
      WriteNewEncryptedBranchKeyVersion := [];
      WriteMutationIndex := [];
      QueryForVersions := [];
      DeleteMutation := [];
    }
    ghost var WriteNewEncryptedBranchKey: seq<DafnyCallEvent<WriteNewEncryptedBranchKeyInput, Result<WriteNewEncryptedBranchKeyOutput, Error>>>
    ghost var GetMutation: seq<DafnyCallEvent<GetMutationInput, Result<GetMutationOutput, Error>>>
    ghost var GetItemsForInitializeMutation: seq<DafnyCallEvent<GetItemsForInitializeMutationInput, Result<GetItemsForInitializeMutationOutput, Error>>>
    ghost var GetKeyStorageInfo: seq<DafnyCallEvent<GetKeyStorageInfoInput, Result<GetKeyStorageInfoOutput, Error>>>
    ghost var GetEncryptedBranchKeyVersion: seq<DafnyCallEvent<GetEncryptedBranchKeyVersionInput, Result<GetEncryptedBranchKeyVersionOutput, Error>>>
    ghost var WriteAtomicMutation: seq<DafnyCallEvent<WriteAtomicMutationInput, Result<WriteAtomicMutationOutput, Error>>>
    ghost var GetEncryptedBeaconKey: seq<DafnyCallEvent<GetEncryptedBeaconKeyInput, Result<GetEncryptedBeaconKeyOutput, Error>>>
    ghost var GetEncryptedActiveBranchKey: seq<DafnyCallEvent<GetEncryptedActiveBranchKeyInput, Result<GetEncryptedActiveBranchKeyOutput, Error>>>
    ghost var WriteMutatedVersions: seq<DafnyCallEvent<WriteMutatedVersionsInput, Result<WriteMutatedVersionsOutput, Error>>>
    ghost var WriteInitializeMutation: seq<DafnyCallEvent<WriteInitializeMutationInput, Result<WriteInitializeMutationOutput, Error>>>
    ghost var WriteNewEncryptedBranchKeyVersion: seq<DafnyCallEvent<WriteNewEncryptedBranchKeyVersionInput, Result<WriteNewEncryptedBranchKeyVersionOutput, Error>>>
    ghost var WriteMutationIndex: seq<DafnyCallEvent<WriteMutationIndexInput, Result<WriteMutationIndexOutput, Error>>>
    ghost var QueryForVersions: seq<DafnyCallEvent<QueryForVersionsInput, Result<QueryForVersionsOutput, Error>>>
    ghost var DeleteMutation: seq<DafnyCallEvent<DeleteMutationInput, Result<DeleteMutationOutput, Error>>>
  }
  trait {:termination false} IKeyStorageInterface
  {
    // Helper to define any additional modifies/reads clauses.
    // If your operations need to mutate state,
    // add it in your constructor function:
    // Modifies := {your, fields, here, History};
    // If you do not need to mutate anything:
    // Modifies := {History};

    ghost const Modifies: set<object>
    // For an unassigned field defined in a trait,
    // Dafny can only assign a value in the constructor.
    // This means that for Dafny to reason about this value,
    // it needs some way to know (an invariant),
    // about the state of the object.
    // This builds on the Valid/Repr paradigm
    // To make this kind requires safe to add
    // to methods called from unverified code,
    // the predicate MUST NOT take any arguments.
    // This means that the correctness of this requires
    // MUST only be evaluated by the class itself.
    // If you require any additional mutation,
    // then you MUST ensure everything you need in ValidState.
    // You MUST also ensure ValidState in your constructor.
    predicate ValidState()
      ensures ValidState() ==> History in Modifies
    ghost const History: IKeyStorageInterfaceCallHistory
    predicate WriteNewEncryptedBranchKeyEnsuresPublicly(input: WriteNewEncryptedBranchKeyInput , output: Result<WriteNewEncryptedBranchKeyOutput, Error>)
    // The public method to be called by library consumers
    method WriteNewEncryptedBranchKey ( input: WriteNewEncryptedBranchKeyInput )
      returns (output: Result<WriteNewEncryptedBranchKeyOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`WriteNewEncryptedBranchKey
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures WriteNewEncryptedBranchKeyEnsuresPublicly(input, output)
      ensures History.WriteNewEncryptedBranchKey == old(History.WriteNewEncryptedBranchKey) + [DafnyCallEvent(input, output)]
    {
      output := WriteNewEncryptedBranchKey' (input);
      History.WriteNewEncryptedBranchKey := History.WriteNewEncryptedBranchKey + [DafnyCallEvent(input, output)];
    }
    // The method to implement in the concrete class.
    method WriteNewEncryptedBranchKey' ( input: WriteNewEncryptedBranchKeyInput )
      returns (output: Result<WriteNewEncryptedBranchKeyOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History}
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures WriteNewEncryptedBranchKeyEnsuresPublicly(input, output)
      ensures unchanged(History)

    predicate GetMutationEnsuresPublicly(input: GetMutationInput , output: Result<GetMutationOutput, Error>)
    // The public method to be called by library consumers
    method GetMutation ( input: GetMutationInput )
      returns (output: Result<GetMutationOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`GetMutation
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures GetMutationEnsuresPublicly(input, output)
      ensures History.GetMutation == old(History.GetMutation) + [DafnyCallEvent(input, output)]
    {
      output := GetMutation' (input);
      History.GetMutation := History.GetMutation + [DafnyCallEvent(input, output)];
    }
    // The method to implement in the concrete class.
    method GetMutation' ( input: GetMutationInput )
      returns (output: Result<GetMutationOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History}
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures GetMutationEnsuresPublicly(input, output)
      ensures unchanged(History)

    predicate GetItemsForInitializeMutationEnsuresPublicly(input: GetItemsForInitializeMutationInput , output: Result<GetItemsForInitializeMutationOutput, Error>)
    // The public method to be called by library consumers
    method GetItemsForInitializeMutation ( input: GetItemsForInitializeMutationInput )
      returns (output: Result<GetItemsForInitializeMutationOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`GetItemsForInitializeMutation
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures GetItemsForInitializeMutationEnsuresPublicly(input, output)
      ensures History.GetItemsForInitializeMutation == old(History.GetItemsForInitializeMutation) + [DafnyCallEvent(input, output)]
    {
      output := GetItemsForInitializeMutation' (input);
      History.GetItemsForInitializeMutation := History.GetItemsForInitializeMutation + [DafnyCallEvent(input, output)];
    }
    // The method to implement in the concrete class.
    method GetItemsForInitializeMutation' ( input: GetItemsForInitializeMutationInput )
      returns (output: Result<GetItemsForInitializeMutationOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History}
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures GetItemsForInitializeMutationEnsuresPublicly(input, output)
      ensures unchanged(History)

    predicate GetKeyStorageInfoEnsuresPublicly(input: GetKeyStorageInfoInput , output: Result<GetKeyStorageInfoOutput, Error>)
    // The public method to be called by library consumers
    method GetKeyStorageInfo ( input: GetKeyStorageInfoInput )
      returns (output: Result<GetKeyStorageInfoOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`GetKeyStorageInfo
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures GetKeyStorageInfoEnsuresPublicly(input, output)
      ensures History.GetKeyStorageInfo == old(History.GetKeyStorageInfo) + [DafnyCallEvent(input, output)]
    {
      output := GetKeyStorageInfo' (input);
      History.GetKeyStorageInfo := History.GetKeyStorageInfo + [DafnyCallEvent(input, output)];
    }
    // The method to implement in the concrete class.
    method GetKeyStorageInfo' ( input: GetKeyStorageInfoInput )
      returns (output: Result<GetKeyStorageInfoOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History}
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures GetKeyStorageInfoEnsuresPublicly(input, output)
      ensures unchanged(History)

    predicate GetEncryptedBranchKeyVersionEnsuresPublicly(input: GetEncryptedBranchKeyVersionInput , output: Result<GetEncryptedBranchKeyVersionOutput, Error>)
    // The public method to be called by library consumers
    method GetEncryptedBranchKeyVersion ( input: GetEncryptedBranchKeyVersionInput )
      returns (output: Result<GetEncryptedBranchKeyVersionOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`GetEncryptedBranchKeyVersion
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures GetEncryptedBranchKeyVersionEnsuresPublicly(input, output)
      ensures History.GetEncryptedBranchKeyVersion == old(History.GetEncryptedBranchKeyVersion) + [DafnyCallEvent(input, output)]
    {
      output := GetEncryptedBranchKeyVersion' (input);
      History.GetEncryptedBranchKeyVersion := History.GetEncryptedBranchKeyVersion + [DafnyCallEvent(input, output)];
    }
    // The method to implement in the concrete class.
    method GetEncryptedBranchKeyVersion' ( input: GetEncryptedBranchKeyVersionInput )
      returns (output: Result<GetEncryptedBranchKeyVersionOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History}
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures GetEncryptedBranchKeyVersionEnsuresPublicly(input, output)
      ensures unchanged(History)

    predicate WriteAtomicMutationEnsuresPublicly(input: WriteAtomicMutationInput , output: Result<WriteAtomicMutationOutput, Error>)
    // The public method to be called by library consumers
    method WriteAtomicMutation ( input: WriteAtomicMutationInput )
      returns (output: Result<WriteAtomicMutationOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`WriteAtomicMutation
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures WriteAtomicMutationEnsuresPublicly(input, output)
      ensures History.WriteAtomicMutation == old(History.WriteAtomicMutation) + [DafnyCallEvent(input, output)]
    {
      output := WriteAtomicMutation' (input);
      History.WriteAtomicMutation := History.WriteAtomicMutation + [DafnyCallEvent(input, output)];
    }
    // The method to implement in the concrete class.
    method WriteAtomicMutation' ( input: WriteAtomicMutationInput )
      returns (output: Result<WriteAtomicMutationOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History}
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures WriteAtomicMutationEnsuresPublicly(input, output)
      ensures unchanged(History)

    predicate GetEncryptedBeaconKeyEnsuresPublicly(input: GetEncryptedBeaconKeyInput , output: Result<GetEncryptedBeaconKeyOutput, Error>)
    // The public method to be called by library consumers
    method GetEncryptedBeaconKey ( input: GetEncryptedBeaconKeyInput )
      returns (output: Result<GetEncryptedBeaconKeyOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`GetEncryptedBeaconKey
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures GetEncryptedBeaconKeyEnsuresPublicly(input, output)
      ensures History.GetEncryptedBeaconKey == old(History.GetEncryptedBeaconKey) + [DafnyCallEvent(input, output)]
    {
      output := GetEncryptedBeaconKey' (input);
      History.GetEncryptedBeaconKey := History.GetEncryptedBeaconKey + [DafnyCallEvent(input, output)];
    }
    // The method to implement in the concrete class.
    method GetEncryptedBeaconKey' ( input: GetEncryptedBeaconKeyInput )
      returns (output: Result<GetEncryptedBeaconKeyOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History}
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures GetEncryptedBeaconKeyEnsuresPublicly(input, output)
      ensures unchanged(History)

    predicate GetEncryptedActiveBranchKeyEnsuresPublicly(input: GetEncryptedActiveBranchKeyInput , output: Result<GetEncryptedActiveBranchKeyOutput, Error>)
    // The public method to be called by library consumers
    method GetEncryptedActiveBranchKey ( input: GetEncryptedActiveBranchKeyInput )
      returns (output: Result<GetEncryptedActiveBranchKeyOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`GetEncryptedActiveBranchKey
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures GetEncryptedActiveBranchKeyEnsuresPublicly(input, output)
      ensures History.GetEncryptedActiveBranchKey == old(History.GetEncryptedActiveBranchKey) + [DafnyCallEvent(input, output)]
    {
      output := GetEncryptedActiveBranchKey' (input);
      History.GetEncryptedActiveBranchKey := History.GetEncryptedActiveBranchKey + [DafnyCallEvent(input, output)];
    }
    // The method to implement in the concrete class.
    method GetEncryptedActiveBranchKey' ( input: GetEncryptedActiveBranchKeyInput )
      returns (output: Result<GetEncryptedActiveBranchKeyOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History}
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures GetEncryptedActiveBranchKeyEnsuresPublicly(input, output)
      ensures unchanged(History)

    predicate WriteMutatedVersionsEnsuresPublicly(input: WriteMutatedVersionsInput , output: Result<WriteMutatedVersionsOutput, Error>)
    // The public method to be called by library consumers
    method WriteMutatedVersions ( input: WriteMutatedVersionsInput )
      returns (output: Result<WriteMutatedVersionsOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`WriteMutatedVersions
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures WriteMutatedVersionsEnsuresPublicly(input, output)
      ensures History.WriteMutatedVersions == old(History.WriteMutatedVersions) + [DafnyCallEvent(input, output)]
    {
      output := WriteMutatedVersions' (input);
      History.WriteMutatedVersions := History.WriteMutatedVersions + [DafnyCallEvent(input, output)];
    }
    // The method to implement in the concrete class.
    method WriteMutatedVersions' ( input: WriteMutatedVersionsInput )
      returns (output: Result<WriteMutatedVersionsOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History}
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures WriteMutatedVersionsEnsuresPublicly(input, output)
      ensures unchanged(History)

    predicate WriteInitializeMutationEnsuresPublicly(input: WriteInitializeMutationInput , output: Result<WriteInitializeMutationOutput, Error>)
    // The public method to be called by library consumers
    method WriteInitializeMutation ( input: WriteInitializeMutationInput )
      returns (output: Result<WriteInitializeMutationOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`WriteInitializeMutation
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures WriteInitializeMutationEnsuresPublicly(input, output)
      ensures History.WriteInitializeMutation == old(History.WriteInitializeMutation) + [DafnyCallEvent(input, output)]
    {
      output := WriteInitializeMutation' (input);
      History.WriteInitializeMutation := History.WriteInitializeMutation + [DafnyCallEvent(input, output)];
    }
    // The method to implement in the concrete class.
    method WriteInitializeMutation' ( input: WriteInitializeMutationInput )
      returns (output: Result<WriteInitializeMutationOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History}
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures WriteInitializeMutationEnsuresPublicly(input, output)
      ensures unchanged(History)

    predicate WriteNewEncryptedBranchKeyVersionEnsuresPublicly(input: WriteNewEncryptedBranchKeyVersionInput , output: Result<WriteNewEncryptedBranchKeyVersionOutput, Error>)
    // The public method to be called by library consumers
    method WriteNewEncryptedBranchKeyVersion ( input: WriteNewEncryptedBranchKeyVersionInput )
      returns (output: Result<WriteNewEncryptedBranchKeyVersionOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`WriteNewEncryptedBranchKeyVersion
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures WriteNewEncryptedBranchKeyVersionEnsuresPublicly(input, output)
      ensures History.WriteNewEncryptedBranchKeyVersion == old(History.WriteNewEncryptedBranchKeyVersion) + [DafnyCallEvent(input, output)]
    {
      output := WriteNewEncryptedBranchKeyVersion' (input);
      History.WriteNewEncryptedBranchKeyVersion := History.WriteNewEncryptedBranchKeyVersion + [DafnyCallEvent(input, output)];
    }
    // The method to implement in the concrete class.
    method WriteNewEncryptedBranchKeyVersion' ( input: WriteNewEncryptedBranchKeyVersionInput )
      returns (output: Result<WriteNewEncryptedBranchKeyVersionOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History}
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures WriteNewEncryptedBranchKeyVersionEnsuresPublicly(input, output)
      ensures unchanged(History)

    predicate WriteMutationIndexEnsuresPublicly(input: WriteMutationIndexInput , output: Result<WriteMutationIndexOutput, Error>)
    // The public method to be called by library consumers
    method WriteMutationIndex ( input: WriteMutationIndexInput )
      returns (output: Result<WriteMutationIndexOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`WriteMutationIndex
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures WriteMutationIndexEnsuresPublicly(input, output)
      ensures History.WriteMutationIndex == old(History.WriteMutationIndex) + [DafnyCallEvent(input, output)]
    {
      output := WriteMutationIndex' (input);
      History.WriteMutationIndex := History.WriteMutationIndex + [DafnyCallEvent(input, output)];
    }
    // The method to implement in the concrete class.
    method WriteMutationIndex' ( input: WriteMutationIndexInput )
      returns (output: Result<WriteMutationIndexOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History}
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures WriteMutationIndexEnsuresPublicly(input, output)
      ensures unchanged(History)

    predicate QueryForVersionsEnsuresPublicly(input: QueryForVersionsInput , output: Result<QueryForVersionsOutput, Error>)
    // The public method to be called by library consumers
    method QueryForVersions ( input: QueryForVersionsInput )
      returns (output: Result<QueryForVersionsOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`QueryForVersions
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures QueryForVersionsEnsuresPublicly(input, output)
      ensures History.QueryForVersions == old(History.QueryForVersions) + [DafnyCallEvent(input, output)]
    {
      output := QueryForVersions' (input);
      History.QueryForVersions := History.QueryForVersions + [DafnyCallEvent(input, output)];
    }
    // The method to implement in the concrete class.
    method QueryForVersions' ( input: QueryForVersionsInput )
      returns (output: Result<QueryForVersionsOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History}
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures QueryForVersionsEnsuresPublicly(input, output)
      ensures unchanged(History)

    predicate DeleteMutationEnsuresPublicly(input: DeleteMutationInput , output: Result<DeleteMutationOutput, Error>)
    // The public method to be called by library consumers
    method DeleteMutation ( input: DeleteMutationInput )
      returns (output: Result<DeleteMutationOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`DeleteMutation
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures DeleteMutationEnsuresPublicly(input, output)
      ensures History.DeleteMutation == old(History.DeleteMutation) + [DafnyCallEvent(input, output)]
    {
      output := DeleteMutation' (input);
      History.DeleteMutation := History.DeleteMutation + [DafnyCallEvent(input, output)];
    }
    // The method to implement in the concrete class.
    method DeleteMutation' ( input: DeleteMutationInput )
      returns (output: Result<DeleteMutationOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History}
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures DeleteMutationEnsuresPublicly(input, output)
      ensures unchanged(History)

  }
  class IKeyStoreClientCallHistory {
    ghost constructor() {
      GetKeyStoreInfo := [];
      CreateKeyStore := [];
      CreateKey := [];
      VersionKey := [];
      GetActiveBranchKey := [];
      GetBranchKeyVersion := [];
      GetBeaconKey := [];
    }
    ghost var GetKeyStoreInfo: seq<DafnyCallEvent<(), Result<GetKeyStoreInfoOutput, Error>>>
    ghost var CreateKeyStore: seq<DafnyCallEvent<CreateKeyStoreInput, Result<CreateKeyStoreOutput, Error>>>
    ghost var CreateKey: seq<DafnyCallEvent<CreateKeyInput, Result<CreateKeyOutput, Error>>>
    ghost var VersionKey: seq<DafnyCallEvent<VersionKeyInput, Result<VersionKeyOutput, Error>>>
    ghost var GetActiveBranchKey: seq<DafnyCallEvent<GetActiveBranchKeyInput, Result<GetActiveBranchKeyOutput, Error>>>
    ghost var GetBranchKeyVersion: seq<DafnyCallEvent<GetBranchKeyVersionInput, Result<GetBranchKeyVersionOutput, Error>>>
    ghost var GetBeaconKey: seq<DafnyCallEvent<GetBeaconKeyInput, Result<GetBeaconKeyOutput, Error>>>
  }
  trait {:termination false} IKeyStoreClient
  {
    // Helper to define any additional modifies/reads clauses.
    // If your operations need to mutate state,
    // add it in your constructor function:
    // Modifies := {your, fields, here, History};
    // If you do not need to mutate anything:
    // Modifies := {History};

    ghost const Modifies: set<object>
    // For an unassigned field defined in a trait,
    // Dafny can only assign a value in the constructor.
    // This means that for Dafny to reason about this value,
    // it needs some way to know (an invariant),
    // about the state of the object.
    // This builds on the Valid/Repr paradigm
    // To make this kind requires safe to add
    // to methods called from unverified code,
    // the predicate MUST NOT take any arguments.
    // This means that the correctness of this requires
    // MUST only be evaluated by the class itself.
    // If you require any additional mutation,
    // then you MUST ensure everything you need in ValidState.
    // You MUST also ensure ValidState in your constructor.
    predicate ValidState()
      ensures ValidState() ==> History in Modifies
    ghost const History: IKeyStoreClientCallHistory
    predicate GetKeyStoreInfoEnsuresPublicly(output: Result<GetKeyStoreInfoOutput, Error>)
    // The public method to be called by library consumers
    method GetKeyStoreInfo (  )
      returns (output: Result<GetKeyStoreInfoOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`GetKeyStoreInfo
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures GetKeyStoreInfoEnsuresPublicly(output)
      ensures History.GetKeyStoreInfo == old(History.GetKeyStoreInfo) + [DafnyCallEvent((), output)]

    predicate CreateKeyStoreEnsuresPublicly(input: CreateKeyStoreInput , output: Result<CreateKeyStoreOutput, Error>)
    // The public method to be called by library consumers
    method CreateKeyStore ( input: CreateKeyStoreInput )
      returns (output: Result<CreateKeyStoreOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`CreateKeyStore
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures CreateKeyStoreEnsuresPublicly(input, output)
      ensures History.CreateKeyStore == old(History.CreateKeyStore) + [DafnyCallEvent(input, output)]

    predicate CreateKeyEnsuresPublicly(input: CreateKeyInput , output: Result<CreateKeyOutput, Error>)
    // The public method to be called by library consumers
    method CreateKey ( input: CreateKeyInput )
      returns (output: Result<CreateKeyOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`CreateKey
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures CreateKeyEnsuresPublicly(input, output)
      ensures History.CreateKey == old(History.CreateKey) + [DafnyCallEvent(input, output)]

    predicate VersionKeyEnsuresPublicly(input: VersionKeyInput , output: Result<VersionKeyOutput, Error>)
    // The public method to be called by library consumers
    method VersionKey ( input: VersionKeyInput )
      returns (output: Result<VersionKeyOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`VersionKey
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures VersionKeyEnsuresPublicly(input, output)
      ensures History.VersionKey == old(History.VersionKey) + [DafnyCallEvent(input, output)]

    predicate GetActiveBranchKeyEnsuresPublicly(input: GetActiveBranchKeyInput , output: Result<GetActiveBranchKeyOutput, Error>)
    // The public method to be called by library consumers
    method GetActiveBranchKey ( input: GetActiveBranchKeyInput )
      returns (output: Result<GetActiveBranchKeyOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`GetActiveBranchKey
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures GetActiveBranchKeyEnsuresPublicly(input, output)
      ensures History.GetActiveBranchKey == old(History.GetActiveBranchKey) + [DafnyCallEvent(input, output)]

    predicate GetBranchKeyVersionEnsuresPublicly(input: GetBranchKeyVersionInput , output: Result<GetBranchKeyVersionOutput, Error>)
    // The public method to be called by library consumers
    method GetBranchKeyVersion ( input: GetBranchKeyVersionInput )
      returns (output: Result<GetBranchKeyVersionOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`GetBranchKeyVersion
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures GetBranchKeyVersionEnsuresPublicly(input, output)
      ensures History.GetBranchKeyVersion == old(History.GetBranchKeyVersion) + [DafnyCallEvent(input, output)]

    predicate GetBeaconKeyEnsuresPublicly(input: GetBeaconKeyInput , output: Result<GetBeaconKeyOutput, Error>)
    // The public method to be called by library consumers
    method GetBeaconKey ( input: GetBeaconKeyInput )
      returns (output: Result<GetBeaconKeyOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`GetBeaconKey
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures GetBeaconKeyEnsuresPublicly(input, output)
      ensures History.GetBeaconKey == old(History.GetBeaconKey) + [DafnyCallEvent(input, output)]

  }
  datatype KeyStoreConfig = | KeyStoreConfig (
    nameonly kmsConfiguration: KMSConfiguration ,
    nameonly logicalKeyStoreName: string ,
    nameonly keyManagement: Option<KeyManagement> := Option.None ,
    nameonly ddbTableName: Option<ComAmazonawsDynamodbTypes.TableName> := Option.None ,
    nameonly id: Option<string> := Option.None ,
    nameonly grantTokens: Option<GrantTokenList> := Option.None ,
    nameonly storage: Option<Storage> := Option.None ,
    nameonly ddbClient: Option<ComAmazonawsDynamodbTypes.IDynamoDBClient> := Option.None ,
    nameonly kmsClient: Option<ComAmazonawsKmsTypes.IKMSClient> := Option.None
  )
  datatype KMSConfiguration =
    | kmsKeyArn(kmsKeyArn: ComAmazonawsKmsTypes.KeyIdType)
    | kmsMRKeyArn(kmsMRKeyArn: ComAmazonawsKmsTypes.KeyIdType)
    | discovery(discovery: Discovery)
    | mrDiscovery(mrDiscovery: MRDiscovery)
  datatype MRDiscovery = | MRDiscovery (
    nameonly region: ComAmazonawsKmsTypes.RegionType
  )
  datatype MutationCommitment = | MutationCommitment (
    nameonly Identifier: string ,
    nameonly CreateTime: string ,
    nameonly UUID: string ,
    nameonly Original: seq<uint8> ,
    nameonly Terminal: seq<uint8> ,
    nameonly Input: seq<uint8> ,
    nameonly CiphertextBlob: seq<uint8>
  )
  datatype MutationIndex = | MutationIndex (
    nameonly Identifier: string ,
    nameonly CreateTime: string ,
    nameonly UUID: string ,
    nameonly PageIndex: seq<uint8> ,
    nameonly CiphertextBlob: seq<uint8>
  )
  datatype OverWriteEncryptedHierarchicalKey = | OverWriteEncryptedHierarchicalKey (
    nameonly Item: EncryptedHierarchicalKey ,
    nameonly Old: EncryptedHierarchicalKey
  )
  type OverWriteEncryptedHierarchicalKeys = seq<OverWriteEncryptedHierarchicalKey>
  datatype OverWriteMutationIndex = | OverWriteMutationIndex (
    nameonly Index: MutationIndex ,
    nameonly Old: MutationIndex
  )
  datatype QueryForVersionsInput = | QueryForVersionsInput (
    nameonly ExclusiveStartKey: Option<seq<uint8>> := Option.None ,
    nameonly Identifier: string ,
    nameonly PageSize: int32
  )
  datatype QueryForVersionsOutput = | QueryForVersionsOutput (
    nameonly ExclusiveStartKey: seq<uint8> ,
    nameonly Items: EncryptedHierarchicalKeys
  )
  type Secret = seq<uint8>
  datatype Storage =
    | ddb(ddb: DynamoDBTable)
    | custom(custom: IKeyStorageInterface)
  type Utf8Bytes = ValidUTF8Bytes
  datatype VersionKeyInput = | VersionKeyInput (
    nameonly branchKeyIdentifier: string
  )
  datatype VersionKeyOutput = | VersionKeyOutput (

                              )
  datatype WriteAtomicMutationInput = | WriteAtomicMutationInput (
    nameonly Active: OverWriteEncryptedHierarchicalKey ,
    nameonly Version: WriteInitializeMutationVersion ,
    nameonly Beacon: OverWriteEncryptedHierarchicalKey ,
    nameonly Items: OverWriteEncryptedHierarchicalKeys
  )
  datatype WriteAtomicMutationOutput = | WriteAtomicMutationOutput (

                                       )
  datatype WriteInitializeMutationInput = | WriteInitializeMutationInput (
    nameonly Active: OverWriteEncryptedHierarchicalKey ,
    nameonly Version: WriteInitializeMutationVersion ,
    nameonly Beacon: OverWriteEncryptedHierarchicalKey ,
    nameonly MutationCommitment: MutationCommitment ,
    nameonly MutationIndex: MutationIndex
  )
  datatype WriteInitializeMutationOutput = | WriteInitializeMutationOutput (

                                           )
  datatype WriteInitializeMutationVersion =
    | rotate(rotate: EncryptedHierarchicalKey)
    | mutate(mutate: OverWriteEncryptedHierarchicalKey)
  datatype WriteMutatedVersionsInput = | WriteMutatedVersionsInput (
    nameonly Items: OverWriteEncryptedHierarchicalKeys ,
    nameonly MutationCommitment: MutationCommitment ,
    nameonly MutationIndex: OverWriteMutationIndex ,
    nameonly EndMutation: bool
  )
  datatype WriteMutatedVersionsOutput = | WriteMutatedVersionsOutput (

                                        )
  datatype WriteMutationIndexInput = | WriteMutationIndexInput (
    nameonly MutationCommitment: MutationCommitment ,
    nameonly MutationIndex: MutationIndex
  )
  datatype WriteMutationIndexOutput = | WriteMutationIndexOutput (

                                      )
  datatype WriteNewEncryptedBranchKeyInput = | WriteNewEncryptedBranchKeyInput (
    nameonly Active: EncryptedHierarchicalKey ,
    nameonly Version: EncryptedHierarchicalKey ,
    nameonly Beacon: EncryptedHierarchicalKey
  )
  datatype WriteNewEncryptedBranchKeyOutput = | WriteNewEncryptedBranchKeyOutput (

                                              )
  datatype WriteNewEncryptedBranchKeyVersionInput = | WriteNewEncryptedBranchKeyVersionInput (
    nameonly Active: OverWriteEncryptedHierarchicalKey ,
    nameonly Version: EncryptedHierarchicalKey
  )
  datatype WriteNewEncryptedBranchKeyVersionOutput = | WriteNewEncryptedBranchKeyVersionOutput (

                                                     )
  datatype Error =
      // Local Error structures are listed here
    | AlreadyExistsConditionFailed (
        nameonly message: string
      )
    | BranchKeyCiphertextException (
        nameonly message: string
      )
    | HierarchyVersionException (
        nameonly message: string
      )
    | KeyManagementException (
        nameonly message: string
      )
    | KeyStorageException (
        nameonly message: string
      )
    | KeyStoreException (
        nameonly message: string
      )
    | MutationCommitmentConditionFailed (
        nameonly message: string
      )
    | NoLongerExistsConditionFailed (
        nameonly message: string
      )
    | OldEncConditionFailed (
        nameonly message: string
      )
    | VersionRaceException (
        nameonly message: string
      )
      // Any dependent models are listed here
    | ComAmazonawsDynamodb(ComAmazonawsDynamodb: ComAmazonawsDynamodbTypes.Error)
    | ComAmazonawsKms(ComAmazonawsKms: ComAmazonawsKmsTypes.Error)
      // The Collection error is used to collect several errors together
      // This is useful when composing OR logic.
      // Consider the following method:
      // 
      // method FN<I, O>(n:I)
      //   returns (res: Result<O, Types.Error>)
      //   ensures A(I).Success? ==> res.Success?
      //   ensures B(I).Success? ==> res.Success?
      //   ensures A(I).Failure? && B(I).Failure? ==> res.Failure?
      // 
      // If either A || B is successful then FN is successful.
      // And if A && B fail then FN will fail.
      // But what information should FN transmit back to the caller?
      // While it may be correct to hide these details from the caller,
      // this can not be the globally correct option.
      // Suppose that A and B can be blocked by different ACLs,
      // and that their representation of I is only eventually consistent.
      // How can the caller distinguish, at a minimum for logging,
      // the difference between the four failure modes?
    // || (!access(A(I)) && !access(B(I)))
    // || (!exit(A(I)) && !exit(B(I)))
    // || (!access(A(I)) && !exit(B(I)))
    // || (!exit(A(I)) && !access(B(I)))
    | CollectionOfErrors(list: seq<Error>, nameonly message: string)
      // The Opaque error, used for native, extern, wrapped or unknown errors
    | Opaque(obj: object)
      // A better Opaque, with a visible string representation.
    | OpaqueWithText(obj: object, objMessage : string)
  type OpaqueError = e: Error | e.Opaque? || e.OpaqueWithText? witness *
  // This dummy subset type is included to make sure Dafny
  // always generates a _ExternBase___default.java class.
  type DummySubsetType = x: int | IsDummySubsetType(x) witness 1
  predicate method IsDummySubsetType(x: int) {
    0 < x
  }

}
abstract module AbstractAwsCryptographyKeyStoreService
{
  import opened Wrappers
  import opened StandardLibrary.UInt
  import opened UTF8
  import opened Types = AwsCryptographyKeyStoreTypes
  import Operations : AbstractAwsCryptographyKeyStoreOperations
  function method DefaultKeyStoreConfig(): KeyStoreConfig
  method {:isoluate_asserations} {:resource_limit 94000000 } KeyStore(config: KeyStoreConfig := DefaultKeyStoreConfig())
    returns (res: Result<KeyStoreClient, Error>)
    requires config.ddbClient.Some? ==>
               config.ddbClient.value.ValidState()
    requires config.kmsClient.Some? ==>
               config.kmsClient.value.ValidState()
    requires config.storage.Some? ==>
               config.storage.value.custom? ==>
                 config.storage.value.custom.ValidState()
    requires config.keyManagement.Some? ==>
               config.keyManagement.value.kms? ==>
                 config.keyManagement.value.kms.kmsClient.Some? ==>
                   config.keyManagement.value.kms.kmsClient.value.ValidState()
    requires config.storage.Some? ==>
               config.storage.value.ddb? ==>
                 config.storage.value.ddb.ddbClient.Some? ==>
                   config.storage.value.ddb.ddbClient.value.ValidState()
    modifies if config.ddbClient.Some? then
               config.ddbClient.value.Modifies
             else {}
    modifies if config.kmsClient.Some? then
               config.kmsClient.value.Modifies
             else {}
    modifies if config.storage.Some? then
               if config.storage.value.custom? then
                 config.storage.value.custom.Modifies
               else {}
             else {}
    modifies if config.keyManagement.Some? then
               if config.keyManagement.value.kms? then
                 if config.keyManagement.value.kms.kmsClient.Some? then
                   config.keyManagement.value.kms.kmsClient.value.Modifies
                 else {}
               else {}
             else {}
    modifies if config.storage.Some? then
               if config.storage.value.ddb? then
                 if config.storage.value.ddb.ddbClient.Some? then
                   config.storage.value.ddb.ddbClient.value.Modifies
                 else {}
               else {}
             else {}
    ensures res.Success? ==>
              && fresh(res.value)
              && fresh(res.value.Modifies
                       - ( if config.ddbClient.Some? then
                             config.ddbClient.value.Modifies
                           else {}
                       ) - ( if config.kmsClient.Some? then
                               config.kmsClient.value.Modifies
                             else {}
                       ) - ( if config.storage.Some? then
                               if config.storage.value.custom? then
                                 config.storage.value.custom.Modifies
                               else {}
                             else {}
                       ) - ( if config.keyManagement.Some? then
                               if config.keyManagement.value.kms? then
                                 if config.keyManagement.value.kms.kmsClient.Some? then
                                   config.keyManagement.value.kms.kmsClient.value.Modifies
                                 else {}
                               else {}
                             else {}
                       ) - ( if config.storage.Some? then
                               if config.storage.value.ddb? then
                                 if config.storage.value.ddb.ddbClient.Some? then
                                   config.storage.value.ddb.ddbClient.value.Modifies
                                 else {}
                               else {}
                             else {}
                       ) )
              && fresh(res.value.History)
              && res.value.ValidState()
    ensures config.ddbClient.Some? ==>
              config.ddbClient.value.ValidState()
    ensures config.kmsClient.Some? ==>
              config.kmsClient.value.ValidState()
    ensures config.storage.Some? ==>
              config.storage.value.custom? ==>
                config.storage.value.custom.ValidState()
    ensures config.keyManagement.Some? ==>
              config.keyManagement.value.kms? ==>
                config.keyManagement.value.kms.kmsClient.Some? ==>
                  config.keyManagement.value.kms.kmsClient.value.ValidState()
    ensures config.storage.Some? ==>
              config.storage.value.ddb? ==>
                config.storage.value.ddb.ddbClient.Some? ==>
                  config.storage.value.ddb.ddbClient.value.ValidState()

  // Helper functions for the benefit of native code to create a Success(client) without referring to Dafny internals
  function method CreateSuccessOfClient(client: IKeyStoreClient): Result<IKeyStoreClient, Error> {
    Success(client)
  }
  function method CreateFailureOfError(error: Error): Result<IKeyStoreClient, Error> {
    Failure(error)
  }
  class KeyStoreClient extends IKeyStoreClient
  {
    constructor(config: Operations.InternalConfig)
      requires Operations.ValidInternalConfig?(config)
      ensures
        && ValidState()
        && fresh(History)
        && this.config == config
    const config: Operations.InternalConfig
    predicate ValidState()
      ensures ValidState() ==>
                && Operations.ValidInternalConfig?(config)
                && History !in Operations.ModifiesInternalConfig(config)
                && Modifies == Operations.ModifiesInternalConfig(config) + {History}
    predicate GetKeyStoreInfoEnsuresPublicly(output: Result<GetKeyStoreInfoOutput, Error>)
    {Operations.GetKeyStoreInfoEnsuresPublicly(output)}
    // The public method to be called by library consumers
    method GetKeyStoreInfo (  )
      returns (output: Result<GetKeyStoreInfoOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`GetKeyStoreInfo
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures GetKeyStoreInfoEnsuresPublicly(output)
      ensures History.GetKeyStoreInfo == old(History.GetKeyStoreInfo) + [DafnyCallEvent((), output)]
    {
      output := Operations.GetKeyStoreInfo(config);
      History.GetKeyStoreInfo := History.GetKeyStoreInfo + [DafnyCallEvent((), output)];
    }

    predicate CreateKeyStoreEnsuresPublicly(input: CreateKeyStoreInput , output: Result<CreateKeyStoreOutput, Error>)
    {Operations.CreateKeyStoreEnsuresPublicly(input, output)}
    // The public method to be called by library consumers
    method CreateKeyStore ( input: CreateKeyStoreInput )
      returns (output: Result<CreateKeyStoreOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`CreateKeyStore
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures CreateKeyStoreEnsuresPublicly(input, output)
      ensures History.CreateKeyStore == old(History.CreateKeyStore) + [DafnyCallEvent(input, output)]
    {
      output := Operations.CreateKeyStore(config, input);
      History.CreateKeyStore := History.CreateKeyStore + [DafnyCallEvent(input, output)];
    }

    predicate CreateKeyEnsuresPublicly(input: CreateKeyInput , output: Result<CreateKeyOutput, Error>)
    {Operations.CreateKeyEnsuresPublicly(input, output)}
    // The public method to be called by library consumers
    method CreateKey ( input: CreateKeyInput )
      returns (output: Result<CreateKeyOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`CreateKey
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures CreateKeyEnsuresPublicly(input, output)
      ensures History.CreateKey == old(History.CreateKey) + [DafnyCallEvent(input, output)]
    {
      output := Operations.CreateKey(config, input);
      History.CreateKey := History.CreateKey + [DafnyCallEvent(input, output)];
    }

    predicate VersionKeyEnsuresPublicly(input: VersionKeyInput , output: Result<VersionKeyOutput, Error>)
    {Operations.VersionKeyEnsuresPublicly(input, output)}
    // The public method to be called by library consumers
    method VersionKey ( input: VersionKeyInput )
      returns (output: Result<VersionKeyOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`VersionKey
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures VersionKeyEnsuresPublicly(input, output)
      ensures History.VersionKey == old(History.VersionKey) + [DafnyCallEvent(input, output)]
    {
      output := Operations.VersionKey(config, input);
      History.VersionKey := History.VersionKey + [DafnyCallEvent(input, output)];
    }

    predicate GetActiveBranchKeyEnsuresPublicly(input: GetActiveBranchKeyInput , output: Result<GetActiveBranchKeyOutput, Error>)
    {Operations.GetActiveBranchKeyEnsuresPublicly(input, output)}
    // The public method to be called by library consumers
    method GetActiveBranchKey ( input: GetActiveBranchKeyInput )
      returns (output: Result<GetActiveBranchKeyOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`GetActiveBranchKey
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures GetActiveBranchKeyEnsuresPublicly(input, output)
      ensures History.GetActiveBranchKey == old(History.GetActiveBranchKey) + [DafnyCallEvent(input, output)]
    {
      output := Operations.GetActiveBranchKey(config, input);
      History.GetActiveBranchKey := History.GetActiveBranchKey + [DafnyCallEvent(input, output)];
    }

    predicate GetBranchKeyVersionEnsuresPublicly(input: GetBranchKeyVersionInput , output: Result<GetBranchKeyVersionOutput, Error>)
    {Operations.GetBranchKeyVersionEnsuresPublicly(input, output)}
    // The public method to be called by library consumers
    method GetBranchKeyVersion ( input: GetBranchKeyVersionInput )
      returns (output: Result<GetBranchKeyVersionOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`GetBranchKeyVersion
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures GetBranchKeyVersionEnsuresPublicly(input, output)
      ensures History.GetBranchKeyVersion == old(History.GetBranchKeyVersion) + [DafnyCallEvent(input, output)]
    {
      output := Operations.GetBranchKeyVersion(config, input);
      History.GetBranchKeyVersion := History.GetBranchKeyVersion + [DafnyCallEvent(input, output)];
    }

    predicate GetBeaconKeyEnsuresPublicly(input: GetBeaconKeyInput , output: Result<GetBeaconKeyOutput, Error>)
    {Operations.GetBeaconKeyEnsuresPublicly(input, output)}
    // The public method to be called by library consumers
    method GetBeaconKey ( input: GetBeaconKeyInput )
      returns (output: Result<GetBeaconKeyOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`GetBeaconKey
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures GetBeaconKeyEnsuresPublicly(input, output)
      ensures History.GetBeaconKey == old(History.GetBeaconKey) + [DafnyCallEvent(input, output)]
    {
      output := Operations.GetBeaconKey(config, input);
      History.GetBeaconKey := History.GetBeaconKey + [DafnyCallEvent(input, output)];
    }

  }
}
abstract module AbstractAwsCryptographyKeyStoreOperations {
  import opened Wrappers
  import opened StandardLibrary.UInt
  import opened UTF8
  import opened Types = AwsCryptographyKeyStoreTypes
  type InternalConfig
  predicate ValidInternalConfig?(config: InternalConfig)
  function ModifiesInternalConfig(config: InternalConfig): set<object>
  predicate GetKeyStoreInfoEnsuresPublicly(output: Result<GetKeyStoreInfoOutput, Error>)
  // The private method to be refined by the library developer


  method GetKeyStoreInfo ( config: InternalConfig )
    returns (output: Result<GetKeyStoreInfoOutput, Error>)
    requires
      && ValidInternalConfig?(config)
    modifies ModifiesInternalConfig(config)
    // Dafny will skip type parameters when generating a default decreases clause.
    decreases ModifiesInternalConfig(config)
    ensures
      && ValidInternalConfig?(config)
    ensures GetKeyStoreInfoEnsuresPublicly(output)


  predicate CreateKeyStoreEnsuresPublicly(input: CreateKeyStoreInput , output: Result<CreateKeyStoreOutput, Error>)
  // The private method to be refined by the library developer


  method CreateKeyStore ( config: InternalConfig , input: CreateKeyStoreInput )
    returns (output: Result<CreateKeyStoreOutput, Error>)
    requires
      && ValidInternalConfig?(config)
    modifies ModifiesInternalConfig(config)
    // Dafny will skip type parameters when generating a default decreases clause.
    decreases ModifiesInternalConfig(config)
    ensures
      && ValidInternalConfig?(config)
    ensures CreateKeyStoreEnsuresPublicly(input, output)


  predicate CreateKeyEnsuresPublicly(input: CreateKeyInput , output: Result<CreateKeyOutput, Error>)
  // The private method to be refined by the library developer


  method CreateKey ( config: InternalConfig , input: CreateKeyInput )
    returns (output: Result<CreateKeyOutput, Error>)
    requires
      && ValidInternalConfig?(config)
    modifies ModifiesInternalConfig(config)
    // Dafny will skip type parameters when generating a default decreases clause.
    decreases ModifiesInternalConfig(config)
    ensures
      && ValidInternalConfig?(config)
    ensures CreateKeyEnsuresPublicly(input, output)


  predicate VersionKeyEnsuresPublicly(input: VersionKeyInput , output: Result<VersionKeyOutput, Error>)
  // The private method to be refined by the library developer


  method VersionKey ( config: InternalConfig , input: VersionKeyInput )
    returns (output: Result<VersionKeyOutput, Error>)
    requires
      && ValidInternalConfig?(config)
    modifies ModifiesInternalConfig(config)
    // Dafny will skip type parameters when generating a default decreases clause.
    decreases ModifiesInternalConfig(config)
    ensures
      && ValidInternalConfig?(config)
    ensures VersionKeyEnsuresPublicly(input, output)


  predicate GetActiveBranchKeyEnsuresPublicly(input: GetActiveBranchKeyInput , output: Result<GetActiveBranchKeyOutput, Error>)
  // The private method to be refined by the library developer


  method GetActiveBranchKey ( config: InternalConfig , input: GetActiveBranchKeyInput )
    returns (output: Result<GetActiveBranchKeyOutput, Error>)
    requires
      && ValidInternalConfig?(config)
    modifies ModifiesInternalConfig(config)
    // Dafny will skip type parameters when generating a default decreases clause.
    decreases ModifiesInternalConfig(config)
    ensures
      && ValidInternalConfig?(config)
    ensures GetActiveBranchKeyEnsuresPublicly(input, output)


  predicate GetBranchKeyVersionEnsuresPublicly(input: GetBranchKeyVersionInput , output: Result<GetBranchKeyVersionOutput, Error>)
  // The private method to be refined by the library developer


  method GetBranchKeyVersion ( config: InternalConfig , input: GetBranchKeyVersionInput )
    returns (output: Result<GetBranchKeyVersionOutput, Error>)
    requires
      && ValidInternalConfig?(config)
    modifies ModifiesInternalConfig(config)
    // Dafny will skip type parameters when generating a default decreases clause.
    decreases ModifiesInternalConfig(config)
    ensures
      && ValidInternalConfig?(config)
    ensures GetBranchKeyVersionEnsuresPublicly(input, output)


  predicate GetBeaconKeyEnsuresPublicly(input: GetBeaconKeyInput , output: Result<GetBeaconKeyOutput, Error>)
  // The private method to be refined by the library developer


  method GetBeaconKey ( config: InternalConfig , input: GetBeaconKeyInput )
    returns (output: Result<GetBeaconKeyOutput, Error>)
    requires
      && ValidInternalConfig?(config)
    modifies ModifiesInternalConfig(config)
    // Dafny will skip type parameters when generating a default decreases clause.
    decreases ModifiesInternalConfig(config)
    ensures
      && ValidInternalConfig?(config)
    ensures GetBeaconKeyEnsuresPublicly(input, output)
}
