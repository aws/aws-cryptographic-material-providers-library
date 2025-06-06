// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../Model/AwsCryptographyPrimitivesTypes.dfy"

module Digest {
  import opened Wrappers
  import opened UInt = StandardLibrary.UInt
  import opened StandardLibrary.MemoryMath
  import Types = AwsCryptographyPrimitivesTypes
  import ExternDigest

  // Hash length in octets (bytes), e.g. GetHashLength(SHA_256) ==> 256 bits = 32 bytes ==> n = 32
  function method Length(digestAlgorithm: Types.DigestAlgorithm): uint64
  {
    match digestAlgorithm
    case SHA_512() => 64
    case SHA_384() => 48
    case SHA_256() => 32
  }

  method Digest(input: Types.DigestInput)
    returns (res: Result<seq<uint8>, Types.Error>)
    ensures res.Success? ==> |res.value| == Length(input.digestAlgorithm) as nat
  {
    var DigestInput(digestAlgorithm, message) := input;
    var value :- ExternDigest.Digest(digestAlgorithm, message);
    SequenceIsSafeBecauseItIsInMemory(value);
    :- Need(
      |value| as uint64 == Length(digestAlgorithm),
      Types.AwsCryptographicPrimitivesError(message := "Incorrect length digest from ExternDigest.")
    );
    return Success(value);
  }
}

module {:extern "ExternDigest" } ExternDigest {
  import opened Wrappers
  import opened UInt = StandardLibrary.UInt
  import Types = AwsCryptographyPrimitivesTypes

  method {:extern } Digest(alg: Types.DigestAlgorithm, msg: seq<uint8>)
    returns (res: Result<seq<uint8>, Types.Error>)

  // The next two functions are for the benefit of the extern implementation to call,
  // avoiding direct references to generic datatype constructors
  // since their calling pattern is different between different versions of Dafny
  // (i.e. after 4.2, explicit type descriptors are required).

  function method CreateDigestSuccess(bytes: seq<uint8>): Result<seq<uint8>, Types.Error> {
    Success(bytes)
  }

  function method CreateDigestFailure(error: Types.Error): Result<seq<uint8>, Types.Error> {
    Failure(error)
  }
}
