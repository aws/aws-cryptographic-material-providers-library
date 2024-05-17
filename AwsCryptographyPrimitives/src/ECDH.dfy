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
                     privateKey := keyPair.privateKey,
                     publicKey := keyPair.publicKey
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
      input.privateKey,
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

  method {:extern "ECDH.KeyGeneration", "GenerateKeyPair"} ExternEccKeyGen(
    s: Types.ECDHCurveSpec
  ) returns (res: Result<EccKeyPair, Types.Error>)
    ensures res.Success? ==> 1 < |res.value.publicKey| <= 8192

  method {:extern "ECDH.ECCUtils", "GetPublicKey"} ExternGetPublicKeyFromPrivate(
    curveAlgorithm: Types.ECDHCurveSpec,
    privateKey: seq<uint8>
  ) returns (res: Result<seq<uint8>, Types.Error>)

  method {:extern "ECDH.ECCUtils", "ValidatePublicKey"} ExternValidatePublicKey(
    curveAlgorithm: Types.ECDHCurveSpec,
    privateKey: seq<uint8>,
    publicKey: seq<uint8>
  ) returns (res: Result<bool, Types.Error>)

  method {:extern "ECDH.DeriveSharedSecret", "CalculateSharedSecret"} ExternDeriveSharedSecret(
    curveAlgorithm: Types.ECDHCurveSpec,
    privateKey: seq<uint8>,
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

}
