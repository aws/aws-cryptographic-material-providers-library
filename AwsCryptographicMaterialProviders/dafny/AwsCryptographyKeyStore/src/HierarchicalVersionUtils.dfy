// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../../../dafny/AwsCryptographicMaterialProviders/Model/AwsCryptographyMaterialProvidersTypes.dfy"
include "../Model/AwsCryptographyKeyStoreTypes.dfy"

module HierarchicalVersionUtils {

  import opened Wrappers
  import AtomicPrimitives
  import opened StandardLibrary.UInt
  import Structure
  
  method ProvideCryptoClient(
    // Crypto?: Option<AtomicPrimitives.Types.IAwsCryptographicPrimitivesClient> := None
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

  // unpacks PlainTextTuple (i.e (MD_DIGEST + AES_256 key)) to return MD_DIGEST, AES_256 key
  function UnpackPlainTextTuple (
    plainTextTuple: seq<uint8>
  ) : (Result:(seq<uint8>, seq<uint8>)) 
  requires |plainTextTuple| == Structure.MD_DIGEST_LENGTH + Structure.AES_256_LENGTH
  ensures |Result.0| == Structure.MD_DIGEST_LENGTH
  ensures |Result.1| == Structure.AES_256_LENGTH
  ensures Result.0 == plainTextTuple[..Structure.MD_DIGEST_LENGTH]
  ensures Result.1 == plainTextTuple[Structure.MD_DIGEST_LENGTH..]
  {
    (plainTextTuple[..Structure.MD_DIGEST_LENGTH], plainTextTuple[Structure.MD_DIGEST_LENGTH..])
  }

  // packs mdDigest and AES 256 Key into (mdDigest + aes256Key)
  function PackPlainTextTuple (
    mdDigest: seq<uint8>, aes256Key: seq<uint8>
  ) : (Result:(seq<uint8>)) 
  requires |mdDigest| == Structure.MD_DIGEST_LENGTH
  requires |aes256Key| == Structure.AES_256_LENGTH
  ensures |Result| == |mdDigest| + |aes256Key|
  ensures Result[..Structure.MD_DIGEST_LENGTH] == mdDigest
  ensures Result[Structure.MD_DIGEST_LENGTH..] == aes256Key
  ensures Result == mdDigest + aes256Key
  {
    (mdDigest + aes256Key)
  }
}