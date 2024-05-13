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

  method {:extern "ECDH.KeyGeneration", "GenerateKeyPair"} ExternEccKeyGen(
    s: Types.ECDHCurveSpec
  ) returns (res: Result<EccKeyPair, Types.Error>)

  function method CreateExternEccKeyGenSuccess(output: EccKeyPair): Result<EccKeyPair, Types.Error> {
    Success(output)
  }

  function method CreateExternEccKeyGenFailure(error: Types.Error): Result<EccKeyPair, Types.Error> {
    Failure(error)
  }
} 