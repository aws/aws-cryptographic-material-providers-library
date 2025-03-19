// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
include "../../../../StandardLibrary/src/Index.dfy"
include "../../AwsCryptographyKeyStore/src/Index.dfy"
include "../../../../AwsCryptographyPrimitives/src/Index.dfy"
include "../../../../ComAmazonawsDynamodb/src/Index.dfy"
include "../../../../ComAmazonawsKms/src/Index.dfy"
module {:extern "software.amazon.cryptography.keystoreadmin.internaldafny.types" } AwsCryptographyKeyStoreAdminTypes
{
  import opened Wrappers
  import opened StandardLibrary.UInt
  import opened UTF8
  import AwsCryptographyKeyStoreTypes
  import AwsCryptographyPrimitivesTypes
  import ComAmazonawsDynamodbTypes
  import ComAmazonawsKmsTypes
    // Generic helpers for verification of mock/unit tests.
  datatype DafnyCallEvent<I, O> = DafnyCallEvent(input: I, output: O)

  // Begin Generated Types

  datatype ApplyMutationInput = | ApplyMutationInput (
    nameonly MutationToken: MutationToken ,
    nameonly PageSize: Option<int32> := Option.None ,
    nameonly Strategy: Option<KeyManagementStrategy> := Option.None ,
    nameonly SystemKey: SystemKey
  )
  datatype ApplyMutationOutput = | ApplyMutationOutput (
    nameonly MutationResult: ApplyMutationResult ,
    nameonly MutatedBranchKeyItems: MutatedBranchKeyItems
  )
  datatype ApplyMutationResult =
    | ContinueMutation(ContinueMutation: MutationToken)
    | CompleteMutation(CompleteMutation: MutationComplete)
  datatype AwsKmsDecryptEncrypt = | AwsKmsDecryptEncrypt (
    nameonly decrypt: Option<AwsCryptographyKeyStoreTypes.AwsKms> := Option.None ,
    nameonly encrypt: Option<AwsCryptographyKeyStoreTypes.AwsKms> := Option.None
  )
  datatype AwsKmsForHierarchyVersionTwo = | AwsKmsForHierarchyVersionTwo (
    nameonly generateRandom: Option<AwsCryptographyKeyStoreTypes.AwsKms> := Option.None ,
    nameonly encrypt: Option<AwsCryptographyKeyStoreTypes.AwsKms> := Option.None ,
    nameonly decrypt: Option<AwsCryptographyKeyStoreTypes.AwsKms> := Option.None
  )
  datatype CreateKeyInput = | CreateKeyInput (
    nameonly Identifier: Option<string> := Option.None ,
    nameonly EncryptionContext: Option<AwsCryptographyKeyStoreTypes.EncryptionContext> := Option.None ,
    nameonly KmsArn: KmsSymmetricKeyArn ,
    nameonly Strategy: Option<KeyManagementStrategy> := Option.None ,
    nameonly HierarchyVersion: Option<AwsCryptographyKeyStoreTypes.HierarchyVersion> := Option.None
  )
  datatype CreateKeyOutput = | CreateKeyOutput (
    nameonly Identifier: string
  )
  datatype DescribeMutationInput = | DescribeMutationInput (
    nameonly Identifier: string
  )
  datatype DescribeMutationOutput = | DescribeMutationOutput (
    nameonly MutationInFlight: MutationInFlight
  )
  datatype InitializeMutationFlag =
    | Created
    | Resumed
    | ResumedWithoutIndex
  datatype InitializeMutationInput = | InitializeMutationInput (
    nameonly Identifier: string ,
    nameonly Mutations: Mutations ,
    nameonly Strategy: Option<KeyManagementStrategy> := Option.None ,
    nameonly SystemKey: SystemKey ,
    nameonly DoNotVersion: Option<bool> := Option.None
  )
  datatype InitializeMutationOutput = | InitializeMutationOutput (
    nameonly MutationToken: MutationToken ,
    nameonly MutatedBranchKeyItems: MutatedBranchKeyItems ,
    nameonly InitializeMutationFlag: InitializeMutationFlag
  )
  datatype KeyManagementStrategy =
    | AwsKmsReEncrypt(AwsKmsReEncrypt: AwsCryptographyKeyStoreTypes.AwsKms)
    | AwsKmsDecryptEncrypt(AwsKmsDecryptEncrypt: AwsKmsDecryptEncrypt)
    | AwsKmsForHierarchyVersionTwo(AwsKmsForHierarchyVersionTwo: AwsKmsForHierarchyVersionTwo)
  class IKeyStoreAdminClientCallHistory {
    ghost constructor() {
      CreateKey := [];
      VersionKey := [];
      InitializeMutation := [];
      ApplyMutation := [];
      DescribeMutation := [];
    }
    ghost var CreateKey: seq<DafnyCallEvent<CreateKeyInput, Result<CreateKeyOutput, Error>>>
    ghost var VersionKey: seq<DafnyCallEvent<VersionKeyInput, Result<VersionKeyOutput, Error>>>
    ghost var InitializeMutation: seq<DafnyCallEvent<InitializeMutationInput, Result<InitializeMutationOutput, Error>>>
    ghost var ApplyMutation: seq<DafnyCallEvent<ApplyMutationInput, Result<ApplyMutationOutput, Error>>>
    ghost var DescribeMutation: seq<DafnyCallEvent<DescribeMutationInput, Result<DescribeMutationOutput, Error>>>
  }
  trait {:termination false} IKeyStoreAdminClient
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
    ghost const History: IKeyStoreAdminClientCallHistory
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

    predicate InitializeMutationEnsuresPublicly(input: InitializeMutationInput , output: Result<InitializeMutationOutput, Error>)
    // The public method to be called by library consumers
    method InitializeMutation ( input: InitializeMutationInput )
      returns (output: Result<InitializeMutationOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`InitializeMutation
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures InitializeMutationEnsuresPublicly(input, output)
      ensures History.InitializeMutation == old(History.InitializeMutation) + [DafnyCallEvent(input, output)]

    predicate ApplyMutationEnsuresPublicly(input: ApplyMutationInput , output: Result<ApplyMutationOutput, Error>)
    // The public method to be called by library consumers
    method ApplyMutation ( input: ApplyMutationInput )
      returns (output: Result<ApplyMutationOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`ApplyMutation
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures ApplyMutationEnsuresPublicly(input, output)
      ensures History.ApplyMutation == old(History.ApplyMutation) + [DafnyCallEvent(input, output)]

    predicate DescribeMutationEnsuresPublicly(input: DescribeMutationInput , output: Result<DescribeMutationOutput, Error>)
    // The public method to be called by library consumers
    method DescribeMutation ( input: DescribeMutationInput )
      returns (output: Result<DescribeMutationOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`DescribeMutation
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures DescribeMutationEnsuresPublicly(input, output)
      ensures History.DescribeMutation == old(History.DescribeMutation) + [DafnyCallEvent(input, output)]

  }
  datatype KeyStoreAdminConfig = | KeyStoreAdminConfig (
    nameonly logicalKeyStoreName: string ,
    nameonly storage: AwsCryptographyKeyStoreTypes.Storage
  )
  datatype KmsSymmetricEncryption = | KmsSymmetricEncryption (
    nameonly KmsArn: ComAmazonawsKmsTypes.KeyIdType ,
    nameonly AwsKms: AwsCryptographyKeyStoreTypes.AwsKms
  )
  datatype KmsSymmetricKeyArn =
    | KmsKeyArn(KmsKeyArn: string)
    | KmsMRKeyArn(KmsMRKeyArn: string)
  datatype MutableBranchKeyProperties = | MutableBranchKeyProperties (
    nameonly KmsArn: string ,
    nameonly CustomEncryptionContext: AwsCryptographyKeyStoreTypes.EncryptionContextString ,
    nameonly HierarchyVersion: AwsCryptographyKeyStoreTypes.HierarchyVersion
  )
  datatype MutatedBranchKeyItem = | MutatedBranchKeyItem (
    nameonly ItemType: string ,
    nameonly Description: string
  )
  type MutatedBranchKeyItems = seq<MutatedBranchKeyItem>
  datatype MutationComplete = | MutationComplete (

                              )
  datatype MutationDescription = | MutationDescription (
    nameonly MutationDetails: MutationDetails ,
    nameonly MutationToken: MutationToken
  )
  datatype MutationDetails = | MutationDetails (
    nameonly Original: MutableBranchKeyProperties ,
    nameonly Terminal: MutableBranchKeyProperties ,
    nameonly Input: Mutations ,
    nameonly SystemKey: string ,
    nameonly CreateTime: string ,
    nameonly UUID: string
  )
  datatype MutationInFlight =
    | Yes(Yes: MutationDescription)
    | No(No: string)
  datatype Mutations = | Mutations (
    nameonly TerminalKmsArn: Option<string> := Option.None ,
    nameonly TerminalEncryptionContext: Option<AwsCryptographyKeyStoreTypes.EncryptionContextString> := Option.None ,
    nameonly TerminalHierarchyVersion: Option<AwsCryptographyKeyStoreTypes.HierarchyVersion> := Option.None
  )
  datatype MutationToken = | MutationToken (
    nameonly Identifier: string ,
    nameonly UUID: string ,
    nameonly CreateTime: string
  )
  datatype SystemKey =
    | kmsSymmetricEncryption(kmsSymmetricEncryption: KmsSymmetricEncryption)
    | trustStorage(trustStorage: TrustStorage)
  datatype TrustStorage = | TrustStorage (

                          )
  datatype VersionKeyInput = | VersionKeyInput (
    nameonly Identifier: string ,
    nameonly KmsArn: KmsSymmetricKeyArn ,
    nameonly Strategy: Option<KeyManagementStrategy> := Option.None ,
    nameonly hierarchyVersion: Option<AwsCryptographyKeyStoreTypes.HierarchyVersion> := Option.None
  )
  datatype VersionKeyOutput = | VersionKeyOutput (

                              )
  datatype Error =
      // Local Error structures are listed here
    | KeyStoreAdminException (
        nameonly message: string
      )
    | MutationConflictException (
        nameonly message: string
      )
    | MutationFromException (
        nameonly message: string
      )
    | MutationInvalidException (
        nameonly message: string
      )
    | MutationToException (
        nameonly message: string
      )
    | MutationVerificationException (
        nameonly message: string
      )
    | UnexpectedStateException (
        nameonly message: string
      )
    | UnsupportedFeatureException (
        nameonly message: string
      )
      // Any dependent models are listed here
    | AwsCryptographyKeyStore(AwsCryptographyKeyStore: AwsCryptographyKeyStoreTypes.Error)
    | AwsCryptographyPrimitives(AwsCryptographyPrimitives: AwsCryptographyPrimitivesTypes.Error)
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
abstract module AbstractAwsCryptographyKeyStoreAdminService
{
  import opened Wrappers
  import opened StandardLibrary.UInt
  import opened UTF8
  import opened Types = AwsCryptographyKeyStoreAdminTypes
  import Operations : AbstractAwsCryptographyKeyStoreAdminOperations
  function method DefaultKeyStoreAdminConfig(): KeyStoreAdminConfig
  method KeyStoreAdmin(config: KeyStoreAdminConfig := DefaultKeyStoreAdminConfig())
    returns (res: Result<KeyStoreAdminClient, Error>)
    requires config.storage.custom? ==>
               config.storage.custom.ValidState()
    requires config.storage.ddb? ==>
               config.storage.ddb.ddbClient.Some? ==>
                 config.storage.ddb.ddbClient.value.ValidState()
    modifies if config.storage.custom? then
               config.storage.custom.Modifies
             else {}
    modifies if config.storage.ddb? then
               if config.storage.ddb.ddbClient.Some? then
                 config.storage.ddb.ddbClient.value.Modifies
               else {}
             else {}
    ensures res.Success? ==>
              && fresh(res.value)
              && fresh(res.value.Modifies
                       - ( if config.storage.custom? then
                             config.storage.custom.Modifies
                           else {}
                       ) - ( if config.storage.ddb? then
                               if config.storage.ddb.ddbClient.Some? then
                                 config.storage.ddb.ddbClient.value.Modifies
                               else {}
                             else {}
                       ) )
              && fresh(res.value.History)
              && res.value.ValidState()
    ensures config.storage.custom? ==>
              config.storage.custom.ValidState()
    ensures config.storage.ddb? ==>
              config.storage.ddb.ddbClient.Some? ==>
                config.storage.ddb.ddbClient.value.ValidState()

  // Helper functions for the benefit of native code to create a Success(client) without referring to Dafny internals
  function method CreateSuccessOfClient(client: IKeyStoreAdminClient): Result<IKeyStoreAdminClient, Error> {
    Success(client)
  }
  function method CreateFailureOfError(error: Error): Result<IKeyStoreAdminClient, Error> {
    Failure(error)
  }
  class KeyStoreAdminClient extends IKeyStoreAdminClient
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

    predicate InitializeMutationEnsuresPublicly(input: InitializeMutationInput , output: Result<InitializeMutationOutput, Error>)
    {Operations.InitializeMutationEnsuresPublicly(input, output)}
    // The public method to be called by library consumers
    method InitializeMutation ( input: InitializeMutationInput )
      returns (output: Result<InitializeMutationOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`InitializeMutation
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures InitializeMutationEnsuresPublicly(input, output)
      ensures History.InitializeMutation == old(History.InitializeMutation) + [DafnyCallEvent(input, output)]
    {
      output := Operations.InitializeMutation(config, input);
      History.InitializeMutation := History.InitializeMutation + [DafnyCallEvent(input, output)];
    }

    predicate ApplyMutationEnsuresPublicly(input: ApplyMutationInput , output: Result<ApplyMutationOutput, Error>)
    {Operations.ApplyMutationEnsuresPublicly(input, output)}
    // The public method to be called by library consumers
    method ApplyMutation ( input: ApplyMutationInput )
      returns (output: Result<ApplyMutationOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`ApplyMutation
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures ApplyMutationEnsuresPublicly(input, output)
      ensures History.ApplyMutation == old(History.ApplyMutation) + [DafnyCallEvent(input, output)]
    {
      output := Operations.ApplyMutation(config, input);
      History.ApplyMutation := History.ApplyMutation + [DafnyCallEvent(input, output)];
    }

    predicate DescribeMutationEnsuresPublicly(input: DescribeMutationInput , output: Result<DescribeMutationOutput, Error>)
    {Operations.DescribeMutationEnsuresPublicly(input, output)}
    // The public method to be called by library consumers
    method DescribeMutation ( input: DescribeMutationInput )
      returns (output: Result<DescribeMutationOutput, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`DescribeMutation
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
      ensures DescribeMutationEnsuresPublicly(input, output)
      ensures History.DescribeMutation == old(History.DescribeMutation) + [DafnyCallEvent(input, output)]
    {
      output := Operations.DescribeMutation(config, input);
      History.DescribeMutation := History.DescribeMutation + [DafnyCallEvent(input, output)];
    }

  }
}
abstract module AbstractAwsCryptographyKeyStoreAdminOperations {
  import opened Wrappers
  import opened StandardLibrary.UInt
  import opened UTF8
  import opened Types = AwsCryptographyKeyStoreAdminTypes
  type InternalConfig
  predicate ValidInternalConfig?(config: InternalConfig)
  function ModifiesInternalConfig(config: InternalConfig): set<object>
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


  predicate InitializeMutationEnsuresPublicly(input: InitializeMutationInput , output: Result<InitializeMutationOutput, Error>)
  // The private method to be refined by the library developer


  method InitializeMutation ( config: InternalConfig , input: InitializeMutationInput )
    returns (output: Result<InitializeMutationOutput, Error>)
    requires
      && ValidInternalConfig?(config)
    modifies ModifiesInternalConfig(config)
    // Dafny will skip type parameters when generating a default decreases clause.
    decreases ModifiesInternalConfig(config)
    ensures
      && ValidInternalConfig?(config)
    ensures InitializeMutationEnsuresPublicly(input, output)


  predicate ApplyMutationEnsuresPublicly(input: ApplyMutationInput , output: Result<ApplyMutationOutput, Error>)
  // The private method to be refined by the library developer


  method ApplyMutation ( config: InternalConfig , input: ApplyMutationInput )
    returns (output: Result<ApplyMutationOutput, Error>)
    requires
      && ValidInternalConfig?(config)
    modifies ModifiesInternalConfig(config)
    // Dafny will skip type parameters when generating a default decreases clause.
    decreases ModifiesInternalConfig(config)
    ensures
      && ValidInternalConfig?(config)
    ensures ApplyMutationEnsuresPublicly(input, output)


  predicate DescribeMutationEnsuresPublicly(input: DescribeMutationInput , output: Result<DescribeMutationOutput, Error>)
  // The private method to be refined by the library developer


  method DescribeMutation ( config: InternalConfig , input: DescribeMutationInput )
    returns (output: Result<DescribeMutationOutput, Error>)
    requires
      && ValidInternalConfig?(config)
    modifies ModifiesInternalConfig(config)
    // Dafny will skip type parameters when generating a default decreases clause.
    decreases ModifiesInternalConfig(config)
    ensures
      && ValidInternalConfig?(config)
    ensures DescribeMutationEnsuresPublicly(input, output)
}
