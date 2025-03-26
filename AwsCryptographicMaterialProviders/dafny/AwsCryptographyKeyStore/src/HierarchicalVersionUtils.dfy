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
}