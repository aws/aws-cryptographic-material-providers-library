// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "HKDF/HKDF.dfy"
include "HKDF/HMAC.dfy"
include "Digest.dfy"
include "../Model/AwsCryptographyPrimitivesTypes.dfy"

/*
 * Implementation of the https://tools.ietf.org/html/rfc5869 HMAC-based key derivation function
 */
module WrappedHKDF {
  import opened Wrappers
  import opened UInt = StandardLibrary.UInt
  import opened StandardLibrary.MemoryMath
  import StandardLibrary
  import Types = AwsCryptographyPrimitivesTypes
  import HMAC
  import HKDF
  import Digest

  method Extract(input: Types.HkdfExtractInput)
    returns (output: Result<seq<uint8>, Types.Error>)
  {
    SequenceIsSafeBecauseItIsInMemory(input.ikm);
    OptionalSequenceIsSafeBecauseItIsInMemory(input.salt);
    :- Need(
      && (input.salt.None? || |input.salt.value| as uint64 != 0)
      && |input.ikm| as uint64 < INT32_MAX_LIMIT as uint64,
      Types.AwsCryptographicPrimitivesError(message := "HKDF Extract needs a salt and reasonable ikm.")
    );

    var HkdfExtractInput(digestAlgorithm, salt, ikm) := input;

    var hmac :- HMAC.HMac.Build(digestAlgorithm);
    var prk := HKDF.Extract(
      hmac,
      salt.UnwrapOr(StandardLibrary.Fill(0, Digest.Length(digestAlgorithm))),
      ikm,
      digestAlgorithm
    );

    return Success(prk);
  }

  method Expand(input: Types.HkdfExpandInput)
    returns (output: Result<seq<uint8>, Types.Error>)
    ensures output.Success? ==> |output.value| == input.expectedLength as nat
  {
    SequenceIsSafeBecauseItIsInMemory(input.info);
    SequenceIsSafeBecauseItIsInMemory(input.prk);
    :- Need(
      && 1 <= input.expectedLength as uint64 <= 255 * Digest.Length(input.digestAlgorithm) as uint64
      && |input.info| as uint64 < INT32_MAX_LIMIT as uint64
      && Digest.Length(input.digestAlgorithm) as uint64 == |input.prk| as uint64,
      Types.AwsCryptographicPrimitivesError(message := "HKDF Expand needs valid input.")
    );
    var HkdfExpandInput(digestAlgorithm, prk, info, expectedLength) := input;

    var hmac :- HMAC.HMac.Build(digestAlgorithm);
    var omk, _ := HKDF.Expand(
      hmac,
      prk,
      info,
      expectedLength as uint64,
      digestAlgorithm
    );

    return Success(omk);
  }

  /*
   * The RFC 5869 KDF. Outputs L bytes of output key material.
   */
  method Hkdf(input: Types.HkdfInput)
    returns (output: Result<seq<uint8>, Types.Error>)
    ensures output.Success? ==> |output.value| == input.expectedLength as nat
  {
    SequenceIsSafeBecauseItIsInMemory(input.ikm);
    SequenceIsSafeBecauseItIsInMemory(input.info);
    OptionalSequenceIsSafeBecauseItIsInMemory(input.salt);
    :- Need(
      && 1 <= input.expectedLength as uint64 <= 255 * Digest.Length(input.digestAlgorithm) as uint64
      && (input.salt.None? || |input.salt.value| as uint64 != 0)
      && |input.info| as uint64 < INT32_MAX_LIMIT as uint64
      && |input.ikm| as uint64 < INT32_MAX_LIMIT as uint64,
      Types.AwsCryptographicPrimitivesError(message := "Wrapped Hkdf input is invalid.")
    );
    var HkdfInput(digest, salt, ikm, info, expectedLength) := input;

    var okm := HKDF.Hkdf(
      digest,
      salt,
      ikm,
      info,
      expectedLength as uint64
    );

    return Success(okm);
  }
}
