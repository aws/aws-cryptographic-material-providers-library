// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/Index.dfy"
include "../src/ECDH.dfy"

module TestECDH {
  import Aws.Cryptography.Primitives
  import opened StandardLibrary.UInt
  import Types = Aws.Cryptography.Primitives.Types
  import UTF8
  import opened Wrappers
  import ECDH

  const P256 := Types.ECDHCurveSpec.ECC_NIST_P256
  const P384 := Types.ECDHCurveSpec.ECC_NIST_P384
  const P521 := Types.ECDHCurveSpec.ECC_NIST_P521
  // TODO SM2

  method {:test} TestKeyGen()
  {
    var supportedCurves := [P256, P384, P521];
    for i := 0 to |supportedCurves|
    {
      var curve := supportedCurves[i];
      var keypair :- expect ECDH.GenerateEccKeyPair(
        Types.GenerateECCKeyPairInput(
          eccCurve := curve
        )
      );
    }
  }

  method {:test} TestGetPublicKeyFromPrivate()
  {
    var supportedCurves := [P256, P384, P521];
    for i := 0 to |supportedCurves|
    {
      var curve := supportedCurves[i];
      var keypair :- expect ECDH.GenerateEccKeyPair(
        Types.GenerateECCKeyPairInput(
          eccCurve := curve
        )
      );

      var publicKey :- expect ECDH.GetPublicKeyFromPrivate(
        Types.GetPublicKeyFromPrivateKeyInput(
          eccCurve := curve,
          privateKey := keypair.privateKey
        )
      );

      expect
        && keypair.eccCurve == publicKey.eccCurve
        && keypair.privateKey == publicKey.privateKey
        && keypair.publicKey == publicKey.publicKey;
    }
  }

  method {:test} TestValidatePublicKeySuccess()
  {
    var supportedCurves := [P256, P384, P521];
    for i := 0 to |supportedCurves|
    {
      var curve := supportedCurves[i];
      var keypairA :- expect ECDH.GenerateEccKeyPair(
        Types.GenerateECCKeyPairInput(
          eccCurve := curve
        )
      );
      var keypairB :- expect ECDH.GenerateEccKeyPair(
        Types.GenerateECCKeyPairInput(
          eccCurve := curve
        )
      );

      var validPublicKeyB :- expect ECDH.ValidatePublicKey(
        Types.ValidatePublicKeyInput(
          eccCurve := curve,
          privateKey := keypairA.privateKey,
          publicKey := keypairB.publicKey
        )
      );
    }

  }

  method {:test} TestValidatePublicKeyFailure()
  {
    var supportedCurves := [P256, P384, P521];
    for i := 0 to |supportedCurves|
    {
      for j := 0 to |supportedCurves|
      {
        var curve_i := supportedCurves[i];
        var curve_j := supportedCurves[j];

        var keypairA :- expect ECDH.GenerateEccKeyPair(
          Types.GenerateECCKeyPairInput(
            eccCurve := curve_i
          )
        );
        var keypairB :- expect ECDH.GenerateEccKeyPair(
          Types.GenerateECCKeyPairInput(
            eccCurve := curve_j
          )
        );

        var validPublicKeyB := ECDH.ValidatePublicKey(
          Types.ValidatePublicKeyInput(
            eccCurve := curve_i,
            privateKey := keypairA.privateKey,
            publicKey := keypairB.publicKey
          )
        );

        if curve_i != curve_j {
          expect validPublicKeyB.Failure?;
        } else {
          expect validPublicKeyB.Success?;
        }

      }
    }
  }

  method {:test} TestGenerateSharedSecret()
  {
    var supportedCurves := [P256, P384, P521];
    for i := 0 to |supportedCurves|
    {
      var curve := supportedCurves[i];
      var keypairA :- expect ECDH.GenerateEccKeyPair(
        Types.GenerateECCKeyPairInput(
          eccCurve := curve
        )
      );
      var keypairB :- expect ECDH.GenerateEccKeyPair(
        Types.GenerateECCKeyPairInput(
          eccCurve := curve
        )
      );

      expect
        && keypairA.privateKey != keypairB.privateKey
        && keypairA.publicKey != keypairB.publicKey;


      var validPublicKeyB :- expect ECDH.ValidatePublicKey(
        Types.ValidatePublicKeyInput(
          eccCurve := curve,
          privateKey := keypairA.privateKey,
          publicKey := keypairB.publicKey
        )
      );

      var sharedSecretA :- expect ECDH.DeriveSharedSecret(
        Types.DeriveSharedSecretInput(
          eccCurve := curve,
          privateKey := keypairA.privateKey,
          publicKey := keypairB.publicKey
        )
      );

      var sharedSecretB :- expect ECDH.DeriveSharedSecret(
        Types.DeriveSharedSecretInput(
          eccCurve := curve,
          privateKey := keypairB.privateKey,
          publicKey := keypairA.publicKey
        )
      );

      expect sharedSecretA == sharedSecretB;
    }
  }
}