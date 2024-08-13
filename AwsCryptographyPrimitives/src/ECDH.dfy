// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../Model/AwsCryptographyPrimitivesTypes.dfy"

module {:extern "ECDH"} ECDH {
  import opened Wrappers
  import opened UInt = StandardLibrary.UInt
  import Types = AwsCryptographyPrimitivesTypes

  datatype EccKeyPair = EccKeyPair(privateKey: seq<uint8>, publicKey: seq<uint8>)

  method GenerateEccKeyPair(
    input: Types.GenerateECCKeyPairInput
  ) returns (output: Result<Types.GenerateECCKeyPairOutput, Types.Error>)
  {
    var keyPair :- ExternEccKeyGen(input.eccCurve);

    return Success(Types.GenerateECCKeyPairOutput(
                     eccCurve := input.eccCurve,
                     privateKey := Types.ECCPrivateKey(pem := keyPair.privateKey),
                     publicKey := Types.ECCPublicKey(der := keyPair.publicKey)
                   ));
  }

  method GetPublicKeyFromPrivate(
    input: Types.GetPublicKeyFromPrivateKeyInput
  ) returns (output: Result<Types.GetPublicKeyFromPrivateKeyOutput, Types.Error>)
  {
    var publicKey :- ExternGetPublicKeyFromPrivate(
      input.eccCurve,
      input.privateKey
    );

    return Success(Types.GetPublicKeyFromPrivateKeyOutput(
                     eccCurve := input.eccCurve,
                     privateKey := input.privateKey,
                     publicKey := publicKey
                   ));
  }

  method ValidatePublicKey(
    input: Types.ValidatePublicKeyInput
  ) returns (output: Result<Types.ValidatePublicKeyOutput, Types.Error>)
  {
    var result :- ExternValidatePublicKey(
      input.eccCurve,
      input.publicKey
    );

    return Success(Types.ValidatePublicKeyOutput(
                     success := result
                   ));
  }

  method DeriveSharedSecret(
    input: Types.DeriveSharedSecretInput
  ) returns (output: Result<Types.DeriveSharedSecretOutput, Types.Error>)
  {
    var derivedSharedSecret :- ExternDeriveSharedSecret(
      input.eccCurve,
      input.privateKey,
      input.publicKey
    );

    return Success(Types.DeriveSharedSecretOutput(
                     sharedSecret := derivedSharedSecret));
  }

  method CompressPublicKey(
    input: Types.CompressPublicKeyInput
  ) returns (output: Result<Types.CompressPublicKeyOutput, Types.Error>)
  {
    var compressedPublicKey :- ExternCompressPublicKey(
      input.publicKey.der,
      input.eccCurve
    );

    return Success(Types.CompressPublicKeyOutput(
                     compressedPublicKey := compressedPublicKey
                   ));
  }

  method DecompressPublicKey(
    input: Types.DecompressPublicKeyInput
  ) returns (output: Result<Types.DecompressPublicKeyOutput, Types.Error>)
  {
    var decompressedPublicKey :- ExternDecompressPublicKey(
      input.compressedPublicKey,
      input.eccCurve
    );

    return Success(Types.DecompressPublicKeyOutput(
                     publicKey := Types.ECCPublicKey(der := decompressedPublicKey)
                   ));
  }

  method ParsePublicKey(
    input: Types.ParsePublicKeyInput
  ) returns (output: Result<Types.ParsePublicKeyOutput, Types.Error>)
  {
    var derPublicKey :- ExternParsePublicKey(
      input.publicKey
    );
    return Success(Types.ParsePublicKeyOutput(
                     publicKey := Types.ECCPublicKey(der := derPublicKey)
                   ));
  }

  // Generate an ECDH key pair
  // Return the private key as UTF8 of PEM of Rfc5915 Der format
  // Return the public key as UTF8 of PEM of X.509 SubjectPublicKeyInfo DER format
  method {:extern "ECDH.KeyGeneration", "GenerateKeyPair"} ExternEccKeyGen(
    s: Types.ECDHCurveSpec
  ) returns (res: Result<EccKeyPair, Types.Error>)
    ensures res.Success? ==> 1 < |res.value.publicKey| <= 8192

  // Given a private key, return the associated public key
  // Input private key is in PEM format
  // Output public key is X.509 SubjectPublicKeyInfo DER format, but not PEM formatted
  method {:extern "ECDH.ECCUtils", "GetPublicKey"} ExternGetPublicKeyFromPrivate(
    curveAlgorithm: Types.ECDHCurveSpec,
    privateKey: Types.ECCPrivateKey
  ) returns (res: Result<seq<uint8>, Types.Error>)

  // Ensure that this public key follows 5.6.2.3.3 ECC Full Public-Key Validation Routine from
  // https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-56Ar3.pdf#page=55
  // Input public key is X.509 SubjectPublicKeyInfo DER format, but not PEM formatted
  // Result is never Success(false), it's either Success(true) or Failure()
  method {:extern "ECDH.ECCUtils", "ValidatePublicKey"} ExternValidatePublicKey(
    curveAlgorithm: Types.ECDHCurveSpec,
    publicKey: seq<uint8>
  ) returns (res: Result<bool, Types.Error>)

  // Calculate a shared secret from the keys
  // Private key is PEM formatted UTF8
  // Input public key is X.509 SubjectPublicKeyInfo DER format, but not PEM formatted
  method {:extern "ECDH.DeriveSharedSecret", "CalculateSharedSecret"} ExternDeriveSharedSecret(
    curveAlgorithm: Types.ECDHCurveSpec,
    privateKey: Types.ECCPrivateKey,
    publicKey: Types.ECCPublicKey
  ) returns (res: Result<seq<uint8>, Types.Error>)

  // Convert X.509 encoded public key to compressed X9.62 format
  // input is not pem formatted
  method {:extern "ECDH.ECCUtils", "CompressPublicKey"} ExternCompressPublicKey(
    publicKey: seq<uint8>,
    curveAlgorithm: Types.ECDHCurveSpec
  ) returns (res: Result<seq<uint8>, Types.Error>)

  // Convert X9.62 encoded public key to X.509 format
  // input is not pem formatted
  method {:extern "ECDH.ECCUtils", "DecompressPublicKey"} ExternDecompressPublicKey(
    publicKey: seq<uint8>,
    curveAlgorithm: Types.ECDHCurveSpec
  ) returns (res: Result<seq<uint8>, Types.Error>)

  // Ensure that this public key is in X.509 SubjectPublicKeyInfo DER format
  // input is not pem formatted
  method {:extern "ECDH.ECCUtils", "ParsePublicKey"} ExternParsePublicKey(
    publicKey: seq<uint8>
  ) returns (res: Result<seq<uint8>, Types.Error>)

  function method CreateExternEccKeyGenSuccess(output: EccKeyPair): Result<EccKeyPair, Types.Error> {
    Success(output)
  }

  function method CreateExternEccKeyGenFailure(error: Types.Error): Result<EccKeyPair, Types.Error> {
    Failure(error)
  }

  function method CreateExternGetPublicKeyFromPrivateSuccess(output: seq<uint8>): Result<seq<uint8>, Types.Error> {
    Success(output)
  }

  function method CreateExternGetPublicKeyFromPrivateError(error: Types.Error): Result<seq<uint8>, Types.Error> {
    Failure(error)
  }

  function method CreateExternValidatePublicKeySuccess(output: bool): Result<bool, Types.Error> {
    Success(output)
  }

  function method CreateExternValidatePublicKeyError(error: Types.Error): Result<bool, Types.Error> {
    Failure(error)
  }

  function method CreateExternDerivesharedSecretSuccess(output: seq<uint8>): Result<seq<uint8>, Types.Error> {
    Success(output)
  }

  function method CreateExternDerivesharedSecretError(error: Types.Error): Result<seq<uint8>, Types.Error> {
    Failure(error)
  }

  function method CreateExternCompressPublicKeyError(error: Types.Error): Result<seq<uint8>, Types.Error> {
    Failure(error)
  }

  function method CreateExternCompressPublicKeySuccess(output: seq<uint8>): Result<seq<uint8>, Types.Error> {
    Success(output)
  }

  function method CreateExternDecompressPublicKeyError(error: Types.Error): Result<seq<uint8>, Types.Error> {
    Failure(error)
  }

  function method CreateExternDecompressPublicKeySuccess(output: seq<uint8>): Result<seq<uint8>, Types.Error> {
    Success(output)
  }

  function method CreateExternParsePublicKeyError(error: Types.Error): Result<seq<uint8>, Types.Error> {
    Failure(error)
  }

  function method CreateExternParsePublicKeySuccess(output: seq<uint8>): Result<seq<uint8>, Types.Error> {
    Success(output)
  }

  function method CreateGetInfinityPublicKeyError(error: Types.Error): Result<seq<uint8>, Types.Error> {
    Failure(error)
  }

  function method CreateGetInfinityPublicKeySuccess(output: seq<uint8>): Result<seq<uint8>, Types.Error> {
    Success(output)
  }

  function method CreateGetOutOfBoundsPublicKeyError(error: Types.Error): Result<seq<uint8>, Types.Error> {
    Failure(error)
  }

  function method CreateGetOutOfBoundsPublicKeySuccess(output: seq<uint8>): Result<seq<uint8>, Types.Error> {
    Success(output)
  }
}
