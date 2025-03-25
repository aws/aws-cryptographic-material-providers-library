// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../../../dafny/AwsCryptographicMaterialProviders/Model/AwsCryptographyMaterialProvidersTypes.dfy"
include "../Model/AwsCryptographyKeyStoreTypes.dfy"
include "../../AwsCryptographicMaterialProviders/src/CanonicalEncryptionContext.dfy"

module HierarchicalVersionUtils {

  import opened Wrappers
  import AtomicPrimitives
  import opened StandardLibrary.UInt
  import opened Seq
  import Structure

  import Types = AwsCryptographyKeyStoreTypes
  import CanonicalEncryptionContext
  // TODO: Remove UTF8 import while removing UnstringifyEncryptionContext
  import opened UTF8

  method ProvideCryptoClient(
    Crypto?: Option<AtomicPrimitives.AtomicPrimitivesClient> := None
  )
    returns (output: Result<AtomicPrimitives.AtomicPrimitivesClient, AtomicPrimitives.Types.Error>)
    requires Crypto?.Some? ==> Crypto?.value.ValidState()
    modifies (if Crypto?.Some? then Crypto?.value.Modifies else {})
    ensures output.Success?
            ==>
              && output.value.ValidState()
              && fresh(output.value)
              && fresh(output.value.Modifies)
  {
    var Crypto: AtomicPrimitives.AtomicPrimitivesClient; //AtomicPrimitives.Types.IAwsCryptographicPrimitivesClient;
    if (Crypto?.None?) {
      Crypto :- AtomicPrimitives.AtomicPrimitives();
    } else {
      Crypto := Crypto?.value;
    }
    // If the customer gave us the Crypto Client, it is fresh
    // If we create the Crypto Client, it is fresh
    assume {:axiom} fresh(Crypto) && fresh(Crypto.Modifies);
    return Success(Crypto);
  }

  method createMdDigest (
    branchKeyContext: map<string, string>,
    cryptoClient: AtomicPrimitives.AtomicPrimitivesClient
  ) returns (output: Result<seq<uint8>, Types.Error>) 
    requires Structure.BranchKeyContext?(branchKeyContext)
    requires cryptoClient.ValidState()
    modifies cryptoClient.Modifies
    ensures cryptoClient.ValidState()
    ensures output.Success? ==>
              && 0 < |cryptoClient.History.Digest|
              && Seq.Last(cryptoClient.History.Digest).output.Success?
              && var DigestInput := Seq.Last(cryptoClient.History.Digest).input;
              && var DigestOutput := Seq.Last(cryptoClient.History.Digest).output;
              && DigestInput.digestAlgorithm == AtomicPrimitives.Types.SHA_384
              && DigestOutput.value == output.value
  {
    var utf8MDDigest :- UnstringifyEncryptionContext(branchKeyContext);
    var digestResult := CanonicalEncryptionContext.EncryptionContextDigest(cryptoClient, utf8MDDigest);
    if (digestResult.Failure?) {
      var error: Types.Error;
      error := match digestResult.error {
        case AwsCryptographyPrimitives(e) =>
          // we cannot reliably serialize a Primitive error without work
          Types.KeyStoreException(message:="Could not SHA-384 Content.")
        case AwsCryptographicMaterialProvidersException(e) =>
          Types.KeyStoreException(message:="Could not SHA-384 Content. " + e)
      };
      return Failure(error);
    }
    return Success(digestResult.value);
  }

  // If you are reviewing this code, then you can STOP. Darwin will add UnstringifyEncryptionContext and UnstringifyEncryptionContextPair. So, these func below are temporary.
  function method UnstringifyEncryptionContext(stringEncCtx: Types.EncryptionContextString) : (res: Result<Types.EncryptionContext, Types.Error>)
  {
    if |stringEncCtx| == 0 then
      Success(map[])
    else
      var parseResults: map<string, Result<(UTF8.ValidUTF8Bytes, UTF8.ValidUTF8Bytes), Types.Error>> :=
        map strKey | strKey in stringEncCtx.Keys :: strKey := UnstringifyEncryptionContextPair(strKey, stringEncCtx[strKey]);
      if exists r | r in parseResults.Values :: r.Failure?
      then Failure(
             Types.KeyStoreException(message := "Encryption context contains invalid UTF8")
           )
      else
        assert forall r | r in parseResults.Values :: r.Success?;
        var utf8KeysUnique := forall k, k' | k in parseResults && k' in parseResults
                                :: k != k' ==> parseResults[k].value.0 != parseResults[k'].value.0;
        if !utf8KeysUnique then Failure(Types.KeyStoreException(
                                          message := "Encryption context keys are not unique"))  // this should never happen...
        else Success(map r | r in parseResults.Values :: r.value.0 := r.value.1)
  }

  function method UnstringifyEncryptionContextPair(strKey: string, strValue: string) : (res: Result<(UTF8.ValidUTF8Bytes, UTF8.ValidUTF8Bytes), Types.Error>)
    ensures (UTF8.Encode(strKey).Success? && UTF8.Encode(strValue).Success?) <==> res.Success?
  {
    var key :- UTF8
               .Encode(strKey)
               .MapFailure(WrapStringToError);
    var value :- UTF8
                 .Encode(strValue)
                 .MapFailure(WrapStringToError);

    Success((key, value))
  }

  function method WrapStringToError(e: string)
    :(ret: Types.Error)
  {
    Types.KeyStoreException( message := e )
  }
}