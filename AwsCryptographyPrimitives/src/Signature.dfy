// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../Model/AwsCryptographyPrimitivesTypes.dfy"

module {:extern "Signature"} Signature {

  import opened Wrappers
  import opened UInt = StandardLibrary.UInt
  import opened StandardLibrary.MemoryMath
  import Types = AwsCryptographyPrimitivesTypes

  datatype SignatureKeyPair = SignatureKeyPair(verificationKey: seq<uint8>, signingKey: seq<uint8>)

  predicate {:axiom} IsSigned(key: seq<uint8>, msg: seq<uint8>, signature: seq<uint8>)

  function method SignatureLength(signatureAlgorithm: Types.ECDSASignatureAlgorithm): uint16 {
    match signatureAlgorithm
    case ECDSA_P256 => 71
    case ECDSA_P384 => 103
  }

  function method FieldSize(signatureAlgorithm: Types.ECDSASignatureAlgorithm): uint64 {
    match signatureAlgorithm
    case ECDSA_P256 => assert 1 + (256 + 7) / 8 == 33; 33
    case ECDSA_P384 => assert 1 + (384 + 7) / 8 == 49; 49
  }

  predicate {:axiom} IsValidSignatureKeyPair(sigKeyPair: SignatureKeyPair)

  method KeyGen(
    input: Types.GenerateECDSASignatureKeyInput
  ) returns (res: Result<Types.GenerateECDSASignatureKeyOutput, Types.Error>)
    ensures match res
            case Success(sigKeyPair) =>
              //= aws-encryption-sdk-specification/framework/structures.md#2.3.3.2.5
              //= type=implication
              //# The signing key MUST fit the specification described by the signature
              //# algorithm (algorithm-suites.md#signature-algorithm) included in this
              //# encryption material's algorithm suite (Section 2.3.3.2.1).
              && |sigKeyPair.verificationKey| == FieldSize(input.signatureAlgorithm) as nat
            // && IsValidSignatureKeyPair(sigKeyPair)
            case Failure(_) => true
  {
    var sigKeyPair :- ExternKeyGen(input.signatureAlgorithm);
    SequenceIsSafeBecauseItIsInMemory(sigKeyPair.verificationKey);

    :- Need(|sigKeyPair.verificationKey| as uint64 == FieldSize(input.signatureAlgorithm) as uint64,
            Types.AwsCryptographicPrimitivesError(
              message := "Incorrect verification-key length from ExternKeyGen."
            ));

    return Success(Types.GenerateECDSASignatureKeyOutput(
                     signatureAlgorithm := input.signatureAlgorithm,
                     verificationKey := sigKeyPair.verificationKey,
                     signingKey := sigKeyPair.signingKey
                   ));
  }

  // Generate an ECDSA key pair
  // Verification key, a.k.a public key, is in X9.62 compressed format
  // Signing Key, a.k.a private key, is in DER-encoded
  method {:extern "Signature.ECDSA", "ExternKeyGen"} {:axiom} ExternKeyGen(
    s: Types.ECDSASignatureAlgorithm
  ) returns (res: Result<SignatureKeyPair, Types.Error>)
    ensures res.Success? ==> IsValidSignatureKeyPair(res.value)

  // sign the message with the private key
  // private signing key is DER-encoded
  method {:extern "Signature.ECDSA", "Sign"} {:axiom} Sign(
    s: Types.ECDSASignatureAlgorithm,
    key: seq<uint8>,
    msg: seq<uint8>
  ) returns (sig: Result<seq<uint8>, Types.Error>)
    ensures sig.Success? ==> IsSigned(key, msg, sig.value)

  // Verify that these bytes created this signature
  // Public verification key is DER-encoded X9.62 format
  // If signature does not match Success(false) is returned
  // This is a valid function
  // because the same inputs will result in the same outputs.
  function method {:extern "Signature.ECDSA", "Verify"} Verify(
    s: Types.ECDSASignatureAlgorithm, key: seq<uint8>,
    msg: seq<uint8>,
    sig: seq<uint8>
  ): (res: Result<bool, Types.Error>)

  // The next six functions are for the benefit of the extern implementation to call,
  // avoiding direct references to generic datatype constructors
  // since their calling pattern is different between different versions of Dafny
  // (i.e. after 4.2, explicit type descriptors are required).

  function method CreateExternKeyGenSuccess(output: SignatureKeyPair): Result<SignatureKeyPair, Types.Error> {
    Success(output)
  }

  function method CreateExternKeyGenFailure(error: Types.Error): Result<SignatureKeyPair, Types.Error> {
    Failure(error)
  }

  function method CreateSignSuccess(bytes: seq<uint8>): Result<seq<uint8>, Types.Error> {
    Success(bytes)
  }

  function method CreateSignFailure(error: Types.Error): Result<seq<uint8>, Types.Error> {
    Failure(error)
  }

  function method CreateVerifySuccess(b: bool): Result<bool, Types.Error> {
    Success(b)
  }

  function method CreateVerifyFailure(error: Types.Error): Result<bool, Types.Error> {
    Failure(error)
  }
}
