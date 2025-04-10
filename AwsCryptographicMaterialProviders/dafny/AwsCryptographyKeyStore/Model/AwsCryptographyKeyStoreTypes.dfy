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
  datatype Discovery = | Discovery (

                       )
  type EncryptionContext = map<Utf8Bytes, Utf8Bytes>
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
  datatype GetKeyStoreInfoOutput = | GetKeyStoreInfoOutput (
    nameonly keyStoreId: string ,
    nameonly keyStoreName: ComAmazonawsDynamodbTypes.TableName ,
    nameonly logicalKeyStoreName: string ,
    nameonly grantTokens: GrantTokenList ,
    nameonly kmsConfiguration: KMSConfiguration
  )
  type GrantTokenList = seq<string>
  type HmacKeyMap = map<string, Secret>
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
    nameonly ddbTableName: ComAmazonawsDynamodbTypes.TableName ,
    nameonly kmsConfiguration: KMSConfiguration ,
    nameonly logicalKeyStoreName: string ,
    nameonly id: Option<string> := Option.None ,
    nameonly grantTokens: Option<GrantTokenList> := Option.None ,
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
  type Secret = seq<uint8>
  type Utf8Bytes = ValidUTF8Bytes
  datatype VersionKeyInput = | VersionKeyInput (
    nameonly branchKeyIdentifier: string
  )
  datatype VersionKeyOutput = | VersionKeyOutput (

                              )
  datatype Error =
      // Local Error structures are listed here
    | KeyStoreException (
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
  method KeyStore(config: KeyStoreConfig := DefaultKeyStoreConfig())
    returns (res: Result<KeyStoreClient, Error>)
    requires config.ddbClient.Some? ==>
               config.ddbClient.value.ValidState()
    requires config.kmsClient.Some? ==>
               config.kmsClient.value.ValidState()
    modifies if config.ddbClient.Some? then
               config.ddbClient.value.Modifies
             else {}
    modifies if config.kmsClient.Some? then
               config.kmsClient.value.Modifies
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
                       ) )
              && fresh(res.value.History)
              && res.value.ValidState()
    ensures config.ddbClient.Some? ==>
              config.ddbClient.value.ValidState()
    ensures config.kmsClient.Some? ==>
              config.kmsClient.value.ValidState()

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
