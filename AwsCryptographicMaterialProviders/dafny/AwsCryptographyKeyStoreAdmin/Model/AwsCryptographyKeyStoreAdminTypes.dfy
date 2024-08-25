// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
include "../../../../StandardLibrary/src/Index.dfy"
include "../../../../ComAmazonawsDynamodb/src/Index.dfy"
include "../../../../ComAmazonawsKms/src/Index.dfy"
include "../../../../AwsCryptographicMaterialProviders/dafny/AwsCryptographyKeyStore/src/Index.dfy"

module {:extern "software.amazon.cryptography.keystoreadmin.internaldafny.types" } AwsCryptographyKeyStoreAdminTypes
{
  import opened Wrappers
  import opened StandardLibrary.UInt
  import opened UTF8
  import AwsCryptographyKeyStoreTypes
  import ComAmazonawsDynamodbTypes
  import ComAmazonawsKmsTypes
    // Generic helpers for verification of mock/unit tests.
  datatype DafnyCallEvent<I, O> = DafnyCallEvent(input: I, output: O)

  // Begin Generated Types
  datatype CreateKeyInput = | CreateKeyInput (
    nameonly branchKeyIdentifier: Option<string> := Option.None ,
    nameonly encryptionContext: Option<AwsCryptographyKeyStoreTypes.EncryptionContext> := Option.None ,
    nameonly kmsArn: KMSIdentifier ,
    nameonly kms: KMSRelationship ,
    nameonly ReEncrypt: Option<ComAmazonawsKmsTypes.IKMSClient> := Option.None
  )
  datatype CreateKeyOutput = | CreateKeyOutput (
    nameonly branchKeyIdentifier: string
  )
  class IKeyStoreAdminClientCallHistory {
    ghost constructor() {
      CreateKey := [];
      VersionKey := [];
    }
    ghost var CreateKey: seq<DafnyCallEvent<CreateKeyInput, Result<CreateKeyOutput, Error>>>
    ghost var VersionKey: seq<DafnyCallEvent<VersionKeyInput, Result<VersionKeyOutput, Error>>>
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
        && ValidState() && ( input.ReEncrypt.Some? ==>
                               && input.ReEncrypt.value.ValidState()
                               && input.ReEncrypt.value.Modifies !! {History}
           )
      modifies Modifies - {History} ,
               (if input.ReEncrypt.Some? then input.ReEncrypt.value.Modifies else {}) ,
               History`CreateKey
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History} ,
                (if input.ReEncrypt.Some? then input.ReEncrypt.value.Modifies else {})
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
  }
  datatype KeyStoreAdminConfig = | KeyStoreAdminConfig (
    nameonly logicalKeyStoreName: string ,
    nameonly storage: AwsCryptographyKeyStoreTypes.Storage
  )
  datatype KMSIdentifier =
    | kmsKeyArn(kmsKeyArn: string)
    | kmsMRKeyArn(kmsMRKeyArn: string)
  datatype KMSRelationship =
    | ReEncrypt(ReEncrypt: ComAmazonawsKmsTypes.IKMSClient)
  type Utf8Bytes = ValidUTF8Bytes
  datatype VersionKeyInput = | VersionKeyInput (
    nameonly branchKeyIdentifier: string ,
    nameonly kmsArn: string ,
    nameonly kms: KMSRelationship
  )
  datatype VersionKeyOutput = | VersionKeyOutput (

                              )
  datatype Error =
      // Local Error structures are listed here
    | KeyStoreAdminException (
        nameonly message: string
      )
    | VersionRaceException (
        nameonly message: string
      )
      // Any dependent models are listed here
    | AwsCryptographyKeyStore(AwsCryptographyKeyStore: AwsCryptographyKeyStoreTypes.Error)
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
  type OpaqueError = e: Error | e.Opaque? witness *
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
        && ValidState() && ( input.ReEncrypt.Some? ==>
                               && input.ReEncrypt.value.ValidState()
                               && input.ReEncrypt.value.Modifies !! {History}
           )
      modifies Modifies - {History} ,
               (if input.ReEncrypt.Some? then input.ReEncrypt.value.Modifies else {}) ,
               History`CreateKey
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History} ,
                (if input.ReEncrypt.Some? then input.ReEncrypt.value.Modifies else {})
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
      && ValidInternalConfig?(config) && ( input.ReEncrypt.Some? ==>
                                             && input.ReEncrypt.value.ValidState()
         )
    modifies ModifiesInternalConfig(config) ,
             (if input.ReEncrypt.Some? then input.ReEncrypt.value.Modifies else {}),
              match input.kms
    case ReEncrypt(kmsClient) => kmsClient.Modifies
    // Dafny will skip type parameters when generating a default decreases clause.
    decreases ModifiesInternalConfig(config) ,
              (if input.ReEncrypt.Some? then input.ReEncrypt.value.Modifies else {})
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
}
