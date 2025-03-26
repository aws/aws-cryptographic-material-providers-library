// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../../../dafny/AwsCryptographicMaterialProviders/Model/AwsCryptographyMaterialProvidersTypes.dfy"
include "../Model/AwsCryptographyKeyStoreTypes.dfy"

module HierarchicalVersionUtils {
  import opened Wrappers
  import AtomicPrimitives
  import opened StandardLibrary.UInt
  import Structure

  const AES_256_LENGTH: uint8 := 32
  // BKC => Branch Key Context
  const BKC_DIGEST_LENGTH: uint8 := 48
  type PlainTextTuple = s: seq<uint8> | |s| == 80 witness *

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
    var Crypto: AtomicPrimitives.AtomicPrimitivesClient;
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

  // unpacks PlainTextTuple (i.e (BKC_DIGEST + AES_256 key)) to return BKC_DIGEST, AES_256 key
  function UnpackPlainTextTuple (
    plainTextTuple: PlainTextTuple
  ) : (Result:(seq<uint8>, seq<uint8>))
    requires |plainTextTuple| == (BKC_DIGEST_LENGTH + AES_256_LENGTH) as int
    ensures |Result.0| == BKC_DIGEST_LENGTH as int
    ensures |Result.1| == AES_256_LENGTH as int
    ensures Result.0 == plainTextTuple[..BKC_DIGEST_LENGTH]
    ensures Result.1 == plainTextTuple[BKC_DIGEST_LENGTH..]
  {
    (plainTextTuple[..BKC_DIGEST_LENGTH], plainTextTuple[BKC_DIGEST_LENGTH..])
  }

  // packs BKCDigest and AES 256 Key into (bkcDigest + aes256Key)
  function PackPlainTextTuple (
    bkcDigest: seq<uint8>, aes256Key: seq<uint8>
  ) : (Result:(PlainTextTuple))
    requires |bkcDigest| == BKC_DIGEST_LENGTH as int
    requires |aes256Key| == AES_256_LENGTH as int
    ensures |Result| as uint8 == |bkcDigest| as uint8 + |aes256Key| as uint8
    ensures Result[..BKC_DIGEST_LENGTH] == bkcDigest
    ensures Result[BKC_DIGEST_LENGTH..] == aes256Key
    ensures Result == bkcDigest + aes256Key
  {
    (bkcDigest + aes256Key)
  }
}
