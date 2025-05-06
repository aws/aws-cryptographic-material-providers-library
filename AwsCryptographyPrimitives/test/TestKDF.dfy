// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/Index.dfy"
include "../src/Digest.dfy"
include "../src/KDF/KdfCtr.dfy"

module TestKDF {
  import AtomicPrimitives
  import opened Wrappers
  import opened StandardLibrary.UInt
  import Digest
  import KdfCtr

  method KdfRawDeriveTest(
    ikm: seq<uint8>,
    info: seq<uint8>,
    L: AtomicPrimitives.Types.PositiveInteger,
    expectedOKM: seq<uint8>,
    digestAlgorithm: AtomicPrimitives.Types.DigestAlgorithm
  )
    requires
      && |ikm| >= 32
      && L > 0
      && 4 + |info| < INT32_MAX_LIMIT
      && L as int + Digest.Length(AtomicPrimitives.Types.DigestAlgorithm.SHA_256) as nat < INT32_MAX_LIMIT - 1
      && L as int + Digest.Length(AtomicPrimitives.Types.DigestAlgorithm.SHA_384) as nat < INT32_MAX_LIMIT - 1
      && (digestAlgorithm == AtomicPrimitives.Types.DigestAlgorithm.SHA_256
          || digestAlgorithm == AtomicPrimitives.Types.DigestAlgorithm.SHA_384)
  {

    var output := KdfCtr.RawDerive(ikm, info, L, 0, digestAlgorithm);

    if output.Success? {
      expect |output.value| == L as nat;
      expect output.value == expectedOKM;
    }
  }

  method KdfTest(
    input: AtomicPrimitives.Types.KdfCtrInput,
    expectedOKM: seq<uint8>
  )
  {
    var client :- expect AtomicPrimitives.AtomicPrimitives();

    var output :- expect client.KdfCounterMode(input);
    expect |output| == input.expectedLength as nat;
    expect output == expectedOKM;
  }
}
