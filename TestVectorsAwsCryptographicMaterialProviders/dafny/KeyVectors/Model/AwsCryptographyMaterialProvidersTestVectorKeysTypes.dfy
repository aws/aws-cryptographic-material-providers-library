// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
include "../../../../StandardLibrary/src/Index.dfy"
include "../../../../AwsCryptographicMaterialProviders/dafny/AwsCryptographicMaterialProviders/src/Index.dfy"
include "../../../../ComAmazonawsKms/src/Index.dfy"
module {:extern "software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types" } AwsCryptographyMaterialProvidersTestVectorKeysTypes
{
  import opened Wrappers
  import opened StandardLibrary.UInt
  import opened UTF8
  import AwsCryptographyMaterialProvidersTypes
  import ComAmazonawsKmsTypes
    // Generic helpers for verification of mock/unit tests.
  datatype DafnyCallEvent<I, O> = DafnyCallEvent(input: I, output: O)

  // Begin Generated Types

  datatype CmmOperation =
    | ENCRYPT
    | DECRYPT
  datatype GetKeyDescriptionInput = | GetKeyDescriptionInput (
    nameonly json: seq<uint8>
  )
  datatype GetKeyDescriptionOutput = | GetKeyDescriptionOutput (
    nameonly keyDescription: KeyDescription
  )
  datatype HierarchyKeyring = | HierarchyKeyring (
    nameonly keyId: string
  )
  datatype KeyDescription =
    | Kms(Kms: KMSInfo)
    | KmsMrk(KmsMrk: KmsMrkAware)
    | KmsMrkDiscovery(KmsMrkDiscovery: KmsMrkAwareDiscovery)
    | RSA(RSA: RawRSA)
    | AES(AES: RawAES)
    | ECDH(ECDH: RawEcdh)
    | Static(Static: StaticKeyring)
    | KmsRsa(KmsRsa: KmsRsaKeyring)
    | KmsECDH(KmsECDH: KmsEcdhKeyring)
    | Hierarchy(Hierarchy: HierarchyKeyring)
    | Multi(Multi: MultiKeyring)
    | RequiredEncryptionContext(RequiredEncryptionContext: RequiredEncryptionContextCMM)
  type KeyDescriptionList = seq<KeyDescription>
  class IKeyVectorsClientCallHistory {
    ghost constructor() {
      CreateTestVectorKeyring := [];
      CreateWrappedTestVectorKeyring := [];
      CreateWrappedTestVectorCmm := [];
      GetKeyDescription := [];
      SerializeKeyDescription := [];
    }
    ghost var CreateTestVectorKeyring: seq<DafnyCallEvent<TestVectorKeyringInput, Result<AwsCryptographyMaterialProvidersTypes.IKeyring, Error>>>
    ghost var CreateWrappedTestVectorKeyring: seq<DafnyCallEvent<TestVectorKeyringInput, Result<AwsCryptographyMaterialProvidersTypes.IKeyring, Error>>>
    ghost var CreateWrappedTestVectorCmm: seq<DafnyCallEvent<TestVectorCmmInput, Result<AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsManager, Error>>>
    ghost var GetKeyDescription: seq<DafnyCallEvent<GetKeyDescriptionInput, Result<GetKeyDescriptionOutput, Error>>>
    ghost var SerializeKeyDescription: seq<DafnyCallEvent<SerializeKeyDescriptionInput, Result<SerializeKeyDescriptionOutput, Error>>>
  }
  trait {:termination false} IKeyVectorsClient
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
    ghost const History: IKeyVectorsClientCallHistory
    predicate CreateTestVectorKeyringEnsuresPublicly(input: TestVectorKeyringInput , output: Result<AwsCryptographyMaterialProvidersTypes.IKeyring, Error>)
    // The public method to be called by library consumers
    method CreateTestVectorKeyring ( input: TestVectorKeyringInput )
      returns (output: Result<AwsCryptographyMaterialProvidersTypes.IKeyring, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`CreateTestVectorKeyring
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
        && ( output.Success? ==>
               && output.value.ValidState()
               && output.value.Modifies !! {History}
               && fresh(output.value)
               && fresh ( output.value.Modifies
                          - Modifies - {History} ) )
      ensures CreateTestVectorKeyringEnsuresPublicly(input, output)
      ensures History.CreateTestVectorKeyring == old(History.CreateTestVectorKeyring) + [DafnyCallEvent(input, output)]

    predicate CreateWrappedTestVectorKeyringEnsuresPublicly(input: TestVectorKeyringInput , output: Result<AwsCryptographyMaterialProvidersTypes.IKeyring, Error>)
    // The public method to be called by library consumers
    method CreateWrappedTestVectorKeyring ( input: TestVectorKeyringInput )
      returns (output: Result<AwsCryptographyMaterialProvidersTypes.IKeyring, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`CreateWrappedTestVectorKeyring
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
        && ( output.Success? ==>
               && output.value.ValidState()
               && output.value.Modifies !! {History}
               && fresh(output.value)
               && fresh ( output.value.Modifies
                          - Modifies - {History} ) )
      ensures CreateWrappedTestVectorKeyringEnsuresPublicly(input, output)
      ensures History.CreateWrappedTestVectorKeyring == old(History.CreateWrappedTestVectorKeyring) + [DafnyCallEvent(input, output)]

    predicate CreateWrappedTestVectorCmmEnsuresPublicly(input: TestVectorCmmInput , output: Result<AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsManager, Error>)
    // The public method to be called by library consumers
    method CreateWrappedTestVectorCmm ( input: TestVectorCmmInput )
      returns (output: Result<AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsManager, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`CreateWrappedTestVectorCmm
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
        && ( output.Success? ==>
               && output.value.ValidState()
               && output.value.Modifies !! {History}
               && fresh(output.value)
               && fresh ( output.value.Modifies
                          - Modifies - {History} ) )
      ensures CreateWrappedTestVectorCmmEnsuresPublicly(input, output)
      ensures History.CreateWrappedTestVectorCmm == old(History.CreateWrappedTestVectorCmm) + [DafnyCallEvent(input, output)]

    // Functions are deterministic, no need for historical call events or ensures indirection
    // The public method to be called by library consumers
    function method GetKeyDescription ( input: GetKeyDescriptionInput )
      : (output: Result<GetKeyDescriptionOutput, Error>)
    // Functions that are transparent do not need ensures

    // Functions are deterministic, no need for historical call events or ensures indirection
    // The public method to be called by library consumers
    function method SerializeKeyDescription ( input: SerializeKeyDescriptionInput )
      : (output: Result<SerializeKeyDescriptionOutput, Error>)
    // Functions that are transparent do not need ensures

  }
  datatype KeyVectorsConfig = | KeyVectorsConfig (
    nameonly keyManifestPath: string
  )
  datatype KmsEcdhKeyring = | KmsEcdhKeyring (
    nameonly senderKeyId: string ,
    nameonly recipientKeyId: string ,
    nameonly senderPublicKey: string ,
    nameonly recipientPublicKey: string ,
    nameonly curveSpec: string ,
    nameonly keyAgreementScheme: string
  )
  datatype KMSInfo = | KMSInfo (
    nameonly keyId: string
  )
  datatype KmsMrkAware = | KmsMrkAware (
    nameonly keyId: string
  )
  datatype KmsMrkAwareDiscovery = | KmsMrkAwareDiscovery (
    nameonly keyId: string ,
    nameonly defaultMrkRegion: string ,
    nameonly awsKmsDiscoveryFilter: Option<AwsCryptographyMaterialProvidersTypes.DiscoveryFilter> := Option.None
  )
  datatype KmsRsaKeyring = | KmsRsaKeyring (
    nameonly keyId: string ,
    nameonly encryptionAlgorithm: ComAmazonawsKmsTypes.EncryptionAlgorithmSpec
  )
  datatype MultiKeyring = | MultiKeyring (
    nameonly generator: Option<KeyDescription> := Option.None ,
    nameonly childKeyrings: KeyDescriptionList
  )
  datatype RawAES = | RawAES (
    nameonly keyId: string ,
    nameonly providerId: string
  )
  datatype RawEcdh = | RawEcdh (
    nameonly senderKeyId: string ,
    nameonly recipientKeyId: string ,
    nameonly senderPublicKey: string ,
    nameonly recipientPublicKey: string ,
    nameonly providerId: string ,
    nameonly curveSpec: string ,
    nameonly keyAgreementScheme: string
  )
  datatype RawRSA = | RawRSA (
    nameonly keyId: string ,
    nameonly providerId: string ,
    nameonly padding: AwsCryptographyMaterialProvidersTypes.PaddingScheme
  )
  datatype RequiredEncryptionContextCMM = | RequiredEncryptionContextCMM (
    nameonly underlying: KeyDescription ,
    nameonly requiredEncryptionContextKeys: AwsCryptographyMaterialProvidersTypes.EncryptionContextKeys
  )
  datatype SerializeKeyDescriptionInput = | SerializeKeyDescriptionInput (
    nameonly keyDescription: KeyDescription
  )
  datatype SerializeKeyDescriptionOutput = | SerializeKeyDescriptionOutput (
    nameonly json: seq<uint8>
  )
  datatype StaticKeyring = | StaticKeyring (
    nameonly keyId: string
  )
  datatype TestVectorCmmInput = | TestVectorCmmInput (
    nameonly keyDescription: KeyDescription ,
    nameonly forOperation: CmmOperation
  )
  datatype TestVectorKeyringInput = | TestVectorKeyringInput (
    nameonly keyDescription: KeyDescription
  )
  datatype Error =
      // Local Error structures are listed here
    | KeyVectorException (
        nameonly message: string
      )
      // Any dependent models are listed here
    | AwsCryptographyMaterialProviders(AwsCryptographyMaterialProviders: AwsCryptographyMaterialProvidersTypes.Error)
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
abstract module AbstractAwsCryptographyMaterialProvidersTestVectorKeysService
{
  import opened Wrappers
  import opened StandardLibrary.UInt
  import opened UTF8
  import opened Types = AwsCryptographyMaterialProvidersTestVectorKeysTypes
  import Operations : AbstractAwsCryptographyMaterialProvidersTestVectorKeysOperations
  function method DefaultKeyVectorsConfig(): KeyVectorsConfig
  method KeyVectors(config: KeyVectorsConfig := DefaultKeyVectorsConfig())
    returns (res: Result<KeyVectorsClient, Error>)
    ensures res.Success? ==>
              && fresh(res.value)
              && fresh(res.value.Modifies)
              && fresh(res.value.History)
              && res.value.ValidState()

  // Helper functions for the benefit of native code to create a Success(client) without referring to Dafny internals
  function method CreateSuccessOfClient(client: IKeyVectorsClient): Result<IKeyVectorsClient, Error> {
    Success(client)
  }
  function method CreateFailureOfError(error: Error): Result<IKeyVectorsClient, Error> {
    Failure(error)
  }
  class KeyVectorsClient extends IKeyVectorsClient
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
    predicate CreateTestVectorKeyringEnsuresPublicly(input: TestVectorKeyringInput , output: Result<AwsCryptographyMaterialProvidersTypes.IKeyring, Error>)
    {Operations.CreateTestVectorKeyringEnsuresPublicly(input, output)}
    // The public method to be called by library consumers
    method CreateTestVectorKeyring ( input: TestVectorKeyringInput )
      returns (output: Result<AwsCryptographyMaterialProvidersTypes.IKeyring, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`CreateTestVectorKeyring
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
        && ( output.Success? ==>
               && output.value.ValidState()
               && output.value.Modifies !! {History}
               && fresh(output.value)
               && fresh ( output.value.Modifies
                          - Modifies - {History} ) )
      ensures CreateTestVectorKeyringEnsuresPublicly(input, output)
      ensures History.CreateTestVectorKeyring == old(History.CreateTestVectorKeyring) + [DafnyCallEvent(input, output)]
    {
      output := Operations.CreateTestVectorKeyring(config, input);
      History.CreateTestVectorKeyring := History.CreateTestVectorKeyring + [DafnyCallEvent(input, output)];
    }

    predicate CreateWrappedTestVectorKeyringEnsuresPublicly(input: TestVectorKeyringInput , output: Result<AwsCryptographyMaterialProvidersTypes.IKeyring, Error>)
    {Operations.CreateWrappedTestVectorKeyringEnsuresPublicly(input, output)}
    // The public method to be called by library consumers
    method CreateWrappedTestVectorKeyring ( input: TestVectorKeyringInput )
      returns (output: Result<AwsCryptographyMaterialProvidersTypes.IKeyring, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`CreateWrappedTestVectorKeyring
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
        && ( output.Success? ==>
               && output.value.ValidState()
               && output.value.Modifies !! {History}
               && fresh(output.value)
               && fresh ( output.value.Modifies
                          - Modifies - {History} ) )
      ensures CreateWrappedTestVectorKeyringEnsuresPublicly(input, output)
      ensures History.CreateWrappedTestVectorKeyring == old(History.CreateWrappedTestVectorKeyring) + [DafnyCallEvent(input, output)]
    {
      output := Operations.CreateWrappedTestVectorKeyring(config, input);
      History.CreateWrappedTestVectorKeyring := History.CreateWrappedTestVectorKeyring + [DafnyCallEvent(input, output)];
    }

    predicate CreateWrappedTestVectorCmmEnsuresPublicly(input: TestVectorCmmInput , output: Result<AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsManager, Error>)
    {Operations.CreateWrappedTestVectorCmmEnsuresPublicly(input, output)}
    // The public method to be called by library consumers
    method CreateWrappedTestVectorCmm ( input: TestVectorCmmInput )
      returns (output: Result<AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsManager, Error>)
      requires
        && ValidState()
      modifies Modifies - {History} ,
               History`CreateWrappedTestVectorCmm
      // Dafny will skip type parameters when generating a default decreases clause.
      decreases Modifies - {History}
      ensures
        && ValidState()
        && ( output.Success? ==>
               && output.value.ValidState()
               && output.value.Modifies !! {History}
               && fresh(output.value)
               && fresh ( output.value.Modifies
                          - Modifies - {History} ) )
      ensures CreateWrappedTestVectorCmmEnsuresPublicly(input, output)
      ensures History.CreateWrappedTestVectorCmm == old(History.CreateWrappedTestVectorCmm) + [DafnyCallEvent(input, output)]
    {
      output := Operations.CreateWrappedTestVectorCmm(config, input);
      History.CreateWrappedTestVectorCmm := History.CreateWrappedTestVectorCmm + [DafnyCallEvent(input, output)];
    }


    // The public method to be called by library consumers
    function method GetKeyDescription ( input: GetKeyDescriptionInput )
      : (output: Result<GetKeyDescriptionOutput, Error>)
      // Functions that are transparent do not need ensures
    {
      Operations.GetKeyDescription(config, input)
    }


    // The public method to be called by library consumers
    function method SerializeKeyDescription ( input: SerializeKeyDescriptionInput )
      : (output: Result<SerializeKeyDescriptionOutput, Error>)
      // Functions that are transparent do not need ensures
    {
      Operations.SerializeKeyDescription(config, input)
    }

  }
}
abstract module AbstractAwsCryptographyMaterialProvidersTestVectorKeysOperations {
  import opened Wrappers
  import opened StandardLibrary.UInt
  import opened UTF8
  import opened Types = AwsCryptographyMaterialProvidersTestVectorKeysTypes
  type InternalConfig
  predicate ValidInternalConfig?(config: InternalConfig)
  function ModifiesInternalConfig(config: InternalConfig): set<object>
  predicate CreateTestVectorKeyringEnsuresPublicly(input: TestVectorKeyringInput , output: Result<AwsCryptographyMaterialProvidersTypes.IKeyring, Error>)
  // The private method to be refined by the library developer


  method CreateTestVectorKeyring ( config: InternalConfig , input: TestVectorKeyringInput )
    returns (output: Result<AwsCryptographyMaterialProvidersTypes.IKeyring, Error>)
    requires
      && ValidInternalConfig?(config)
    modifies ModifiesInternalConfig(config)
    // Dafny will skip type parameters when generating a default decreases clause.
    decreases ModifiesInternalConfig(config)
    ensures
      && ValidInternalConfig?(config)
      && ( output.Success? ==>
             && output.value.ValidState()
             && fresh(output.value)
             && fresh ( output.value.Modifies
                        - ModifiesInternalConfig(config) ) )
    ensures CreateTestVectorKeyringEnsuresPublicly(input, output)


  predicate CreateWrappedTestVectorKeyringEnsuresPublicly(input: TestVectorKeyringInput , output: Result<AwsCryptographyMaterialProvidersTypes.IKeyring, Error>)
  // The private method to be refined by the library developer


  method CreateWrappedTestVectorKeyring ( config: InternalConfig , input: TestVectorKeyringInput )
    returns (output: Result<AwsCryptographyMaterialProvidersTypes.IKeyring, Error>)
    requires
      && ValidInternalConfig?(config)
    modifies ModifiesInternalConfig(config)
    // Dafny will skip type parameters when generating a default decreases clause.
    decreases ModifiesInternalConfig(config)
    ensures
      && ValidInternalConfig?(config)
      && ( output.Success? ==>
             && output.value.ValidState()
             && fresh(output.value)
             && fresh ( output.value.Modifies
                        - ModifiesInternalConfig(config) ) )
    ensures CreateWrappedTestVectorKeyringEnsuresPublicly(input, output)


  predicate CreateWrappedTestVectorCmmEnsuresPublicly(input: TestVectorCmmInput , output: Result<AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsManager, Error>)
  // The private method to be refined by the library developer


  method CreateWrappedTestVectorCmm ( config: InternalConfig , input: TestVectorCmmInput )
    returns (output: Result<AwsCryptographyMaterialProvidersTypes.ICryptographicMaterialsManager, Error>)
    requires
      && ValidInternalConfig?(config)
    modifies ModifiesInternalConfig(config)
    // Dafny will skip type parameters when generating a default decreases clause.
    decreases ModifiesInternalConfig(config)
    ensures
      && ValidInternalConfig?(config)
      && ( output.Success? ==>
             && output.value.ValidState()
             && fresh(output.value)
             && fresh ( output.value.Modifies
                        - ModifiesInternalConfig(config) ) )
    ensures CreateWrappedTestVectorCmmEnsuresPublicly(input, output)


  // Functions are deterministic, no need for historical call events or ensures indirection
  // The private method to be refined by the library developer


  function method GetKeyDescription ( config: InternalConfig , input: GetKeyDescriptionInput )
    : (output: Result<GetKeyDescriptionOutput, Error>)
  // Functions that are transparent do not need ensures


  // Functions are deterministic, no need for historical call events or ensures indirection
  // The private method to be refined by the library developer


  function method SerializeKeyDescription ( config: InternalConfig , input: SerializeKeyDescriptionInput )
    : (output: Result<SerializeKeyDescriptionOutput, Error>)
  // Functions that are transparent do not need ensures
}
