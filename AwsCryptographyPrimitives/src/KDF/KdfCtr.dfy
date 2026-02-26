// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../HKDF/HMAC.dfy"
include "../Digest.dfy"
include "../../Model/AwsCryptographyPrimitivesTypes.dfy"

/*
 * Implementation of the https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-108r1.pdf
 * Key Derivation in Counter Mode Using Pseudorandom Functions
 */
module KdfCtr {
  import opened StandardLibrary
  import opened Wrappers
  import opened UInt = StandardLibrary.UInt
  import opened StandardLibrary.MemoryMath
  import UTF8
  import Types = AwsCryptographyPrimitivesTypes
  import HMAC
  import Digest

  const SEPARATION_INDICATOR: seq<uint8> := [0x00]
  const COUNTER_START_VALUE: uint32 := 1

  // This implementation of te spec is restricted to only deriving
  // 32 bytes of key material. We will have to consider the effect of allowing different
  // key length to the hierarchy keyring.
  method KdfCounterMode(input: Types.KdfCtrInput)
    returns (output: Result<seq<uint8>, Types.Error>)
    ensures output.Success? ==> |output.value| == input.expectedLength as nat
  {
    // currently only SHA 256 and SHA 384 are allowed
    SequenceIsSafeBecauseItIsInMemory(input.ikm);
    OptionalSequenceIsSafeBecauseItIsInMemory(input.nonce);
    :- Need(
      && (input.digestAlgorithm == Types.DigestAlgorithm.SHA_256 || input.digestAlgorithm == Types.DigestAlgorithm.SHA_384)
      && (|input.ikm| as uint64 == 32 || |input.ikm| as uint64 == 48 || |input.ikm| as uint64 == 66)
      && input.nonce.Some?
      && (|input.nonce.value| as uint64 == 16 || |input.nonce.value| as uint64 == 32)
      && (input.expectedLength == 32 || input.expectedLength == 64)
      && 0 < (input.expectedLength * 8) as uint64 < INT32_MAX_LIMIT as uint64,
      Types.AwsCryptographicPrimitivesError(message := "Kdf in Counter Mode input is invalid.")
    );

    var ikm := input.ikm;
    var label_ := input.purpose.UnwrapOr([]);
    var info := input.nonce.UnwrapOr([]);
    var okm := [];

    // Compute length in bits of the input going into the PRF.
    var internalLength : uint32 := (4 + |SEPARATION_INDICATOR| as uint64 + 4) as uint32;
    SequenceIsSafeBecauseItIsInMemory(label_);
    SequenceIsSafeBecauseItIsInMemory(info);
    :- Need(
      && Add3(internalLength as uint64,|label_| as uint64, |info| as uint64)  < INT32_MAX_LIMIT  as uint64 ,
      Types.AwsCryptographicPrimitivesError(message:= "Input Length exceeds INT32_MAX_LIMIT")
    );

    // Compute length in bits of the output from the PRF. "L" in SP800-108.
    var lengthBits : seq<uint8> := UInt.UInt32ToSeq((input.expectedLength * 8) as uint32);
    var explicitInfo := label_ + SEPARATION_INDICATOR + info + lengthBits;

    SequenceIsSafeBecauseItIsInMemory(explicitInfo);
    :- Need(
      4 + |explicitInfo| as uint64 < INT32_MAX_LIMIT as uint64,
      Types.AwsCryptographicPrimitivesError(message := "PRF input length exceeds INT32_MAX_LIMIT.")
    );

    okm :- RawDerive(ikm, explicitInfo, input.expectedLength, 0, input.digestAlgorithm);

    return Success(okm);
  }

  method RawDerive(ikm: seq<uint8>, explicitInfo: seq<uint8>, length: int32, offset: int32, digestAlgorithm: Types.DigestAlgorithm)
    returns (output: Result<seq<uint8>, Types.Error>)
    requires
      && |ikm| >= 32
      && length > 0
      && 4 + |explicitInfo| < INT32_MAX_LIMIT
      && (digestAlgorithm == Types.DigestAlgorithm.SHA_256 || digestAlgorithm == Types.DigestAlgorithm.SHA_384)
      && length as int + Digest.Length(Types.DigestAlgorithm.SHA_256) as int < INT32_MAX_LIMIT - 1
      && length as int + Digest.Length(Types.DigestAlgorithm.SHA_384) as int < INT32_MAX_LIMIT - 1
    ensures output.Success? ==> |output.value| == length as int
  {
    var hmac :- HMAC.HMac.Build(digestAlgorithm);
    hmac.Init(key := ikm);

    var macLengthBytes := Digest.Length(digestAlgorithm) as int32; // "h" in SP800-108
    // Number of iterations required to compose output of required length.
    var iterations := (length + macLengthBytes - 1) / macLengthBytes; // "n" in SP800-108
    var buffer := [];

    // Counter "i"
    var i : seq<uint8> := UInt.UInt32ToSeq(COUNTER_START_VALUE);

    for iteration : uint64 := 1 to Add(iterations as uint64, 1)
      invariant |i| == 4
      invariant hmac.GetKey() == ikm
    {
      /*
       * SP800-108 defines PRF(s,x), the "x" variable is prfInput below.
       */
      // i || label || 0x00 || context (info) || L
      hmac.Update(i);
      hmac.Update(explicitInfo);
      var tmp := hmac.GetResult();
      buffer := buffer + tmp;

      i :- Increment(i);
    }

    SequenceIsSafeBecauseItIsInMemory(buffer);
    :- Need(
      |buffer| as uint64 >= length as uint64,
      Types.AwsCryptographicPrimitivesError(message := "Failed to derive key of requested length")
    );

    return Success(buffer[..length]);
  }

  function method Increment(x : seq<uint8>) : (ret : Result<seq<uint8>, Types.Error>)
    requires |x| == 4
    ensures ret.Success? ==> |ret.value| == 4
  {
    // increments the counter x which represents the number of iterations
    // as a bit sequence
    if x[3 as uint32] < 255 then
      Success([x[0 as uint32], x[1 as uint32], x[2 as uint32], x[3 as uint32]+1])
    else if x[2 as uint32] < 255 then
      Success([x[0 as uint32], x[1 as uint32], x[2 as uint32]+1, 0])
    else if x[1 as uint32] < 255 then
      Success([x[0 as uint32], x[1 as uint32]+1, 0, 0])
    else if x[0 as uint32] < 255 then
      Success([x[0 as uint32]+1, 0, 0, 0])
    else
      Failure(Types.AwsCryptographicPrimitivesError(message := "Unable to derive key material; may have exceeded limit."))
  }

}
