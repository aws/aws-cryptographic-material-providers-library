// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/Index.dfy"
include "../src/ECDH.dfy"

module TestECDH {
  import AtomicPrimitives
  import opened StandardLibrary.UInt
  import Types = AwsCryptographyPrimitivesTypes
  import UTF8
  import HexStrings
  import Base64
  import opened Wrappers
  import ECDH

  const P256 := Types.ECDHCurveSpec.ECC_NIST_P256
  const P384 := Types.ECDHCurveSpec.ECC_NIST_P384
  const P521 := Types.ECDHCurveSpec.ECC_NIST_P521
  // TODO SM2

  // THESE ARE TESTING RESOURCES; DO NOT USE IN A PROD ENVIRONMENT
  // RUN openssl ecparam -name secp256r1 -genkey -noout -out private.pem
  const ECC_P256_PRIVATE := "-----BEGIN PRIVATE KEY-----\n"
                            + "MIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQgw+7YSKEOEAh8/DFZ\n"
                            + "22oSTm/D3jo4nH5tN48IUp0WjyuhRANCAASnUgx7SrlHhPIn3McZfc3cEIs8+XFf\n"
                            + "7JvhcuV1wWELGZ8AjuwnKjE0ielEwSY5HYzWCF773FvJaWGYGYGhSba8\n"
                            + "-----END PRIVATE KEY-----"
  // HEX REPRESENATION OF THE PUBLIC KEY
  // RUN openssl ec -in public_key.der -pubin -outform DER | xxd -p -c 256
  const ECC_P256_PUBLIC := "3059301306072a8648ce3d020106082a8648ce3d03010703420004a7520c7b4ab9478"
                           + "4f227dcc7197dcddc108b3cf9715fec9be172e575c1610b199f008eec272a313489"
                           + "e944c126391d8cd6085efbdc5bc96961981981a149b6bc"

  const ECC_P256_PUBLIC_COMPRESSED :=
    "02a7520c7b4ab94784f227dcc7197dcddc108b3cf9715fec9be172e575c1610b19"

  const ECC_P384_PRIVATE := "-----BEGIN PRIVATE KEY-----\n"
                            + "MIG2AgEAMBAGByqGSM49AgEGBSuBBAAiBIGeMIGbAgEBBDAE/GcrZaGaZKKnWsbi\n"
                            + "6OiMB8HlhoyF1CQeaZHFdp1VFu7mSM2mUrSolCfpYRB50aahZANiAAQayPW6B3aV\n"
                            + "GKWFBbDH3SeuMhiY2GIPG+tBEHmMZ3QUaG6qNnQxXS+QpR95IWyQWZjInyDk2upe\n"
                            + "b1TivP0UYay+dIS8MrBFM7oLBsJIqxGiRQ1EPFIpBLv4mmteOma5qt8=\n"
                            + "-----END PRIVATE KEY-----"
  const ECC_384_PUBLIC := "3076301006072a8648ce3d020106052b81040022036200041ac8f5ba07769518a58505"
                          + "b0c7dd27ae321898d8620f1beb4110798c677414686eaa3674315d2f90a51f79216c"
                          + "905998c89f20e4daea5e6f54e2bcfd1461acbe7484bc32b04533ba0b06c248ab11a2"
                          + "450d443c522904bbf89a6b5e3a66b9aadf"

  const ECC_384_PUBLIC_COMPRESSED :=
    "031ac8f5ba07769518a58505b0c7dd27ae321898d8620f1beb4110798c677414686eaa3674315d2f90a51f79216c905998"

  const ECC_P521_PRIVATE := "-----BEGIN PRIVATE KEY-----\n"
                            + "MIHuAgEAMBAGByqGSM49AgEGBSuBBAAjBIHWMIHTAgEBBEIB3azBoPIuF7SY3Z7g\n"
                            + "xK/dEnSqoqBsHaoiI78Sfs9Ydxsd/3Ref4xZC0v58EwZjKxIMWwcqxSNzg8yLOAV\n"
                            + "oaRbwryhgYkDgYYABAHeMnMkadh2nketUTcDvKE4WCcdTdIFKaDqwtMIbq/y5N4E\n"
                            + "I77OxYwKP7IdGBC9n/GkcNIWx6R91zc3AId9a7VrOQF9+HitnblByL1u3N6kWhUf\n"
                            + "C3ury11T8dkNW+LbVkmX8B3+s6VaEQWKa+SYBemPV05aJhU0xaaF/MhsLGwKLpPp\n"
                            + "Qg==\n"
                            + "-----END PRIVATE KEY-----"
  const ECC_P521_PUBLIC := "30819b301006072a8648ce3d020106052b81040023038186000401de32732469d8769e"
                           + "47ad513703bca13858271d4dd20529a0eac2d3086eaff2e4de0423becec58c0a3fb2"
                           + "1d1810bd9ff1a470d216c7a47dd7373700877d6bb56b39017df878ad9db941c8bd6e"
                           + "dcdea45a151f0b7babcb5d53f1d90d5be2db564997f01dfeb3a55a11058a6be49805"
                           + "e98f574e5a261534c5a685fcc86c2c6c0a2e93e942"

  const ECC_P521_PUBLIC_COMPRESSED :=
    "0201de32732469d8769e47ad513703bca13858271d4dd20529a0eac2d3086eaff2e4de0423becec58c0a3fb21d1810bd9ff1a470d216c7a47dd7373700877d6bb56b39"

  // Known value infinity public keys.
  // These MUST fail with a known error message when loaded by the crypto provider.
  const ECC_256_PUBLIC_INF_FAIL_ON_LOAD := "3019301306072a8648ce3d020106082a8648ce3d03010703020000"
  const ECC_384_PUBLIC_INF_FAIL_ON_LOAD := "3016301006072a8648ce3d020106052b8104002203020000"
  const ECC_521_PUBLIC_INF_FAIL_ON_LOAD := "3016301006072a8648ce3d020106052b8104002303020000"

  // Known value out of bounds public keys.
  // These MUST fail with a known error message when loaded by the crypto provider.
  const ECC_P256_PUBLIC_GP_FAIL_ON_LOAD :=
    "3059301306072a8648ce3d020106082a8648ce3d03010703420004fffffffffffffffff"
    + "fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"
    + "ffffffffffffffffffffffffffffffffffffffffff"
  const ECC_P384_PUBLIC_GP_FAIL_ON_LOAD :=
    "3076301006072a8648ce3d020106052b8104002203620004fffffffffffffffffffffff"
    + "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"
    + "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"
    + "fffffffffffffffffffffffffffff"
  const ECC_P521_PUBLIC_GP_FAIL_ON_LOAD :=
    "30819b301006072a8648ce3d020106052b810400230381860004ffffffffffffffffffff"
    + "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"
    + "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"
    + "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"
    + "ffffffffffffffffffffffffffffffffff"

  // Known value infinity public keys.
  // These MUST fail when loaded by the crypto provider or when running extern NIST validation.
  const ECC_256_PUBLIC_INF := "3059301306072a864886f70d0106082a864886f70d03010703420004000000000000"
                              + "00000000000000000000000000000000000000000000000000000000000000000000"
                              + "00000000000000000000000000000000000000000000000000000000"
  const ECC_384_PUBLIC_INF := "3076301006072a864886f70d0106052b810400220362000400000000000000000000"
                              + "00000000000000000000000000000000000000000000000000000000000000000000"
                              + "00000000000000000000000000000000000000000000000000000000000000000000"
                              + "00000000000000"
  const ECC_521_PUBLIC_INF := "3081ee3010060772a8648ce3d02106052b81040023038186000400000000000000000"
                              + "000000000000000000000000000000000000000000000000000000000000000000000"
                              + "000000000000000000000000000000000000000000000000000000000000000000000"
                              + "000000000000000000000000000000000000000000000000000000000000000000000"
                              + "0000000000000000000000000000000000000000000000000000000000000000000000"
                              + "00000000000000000000000000000000000000000000"

  // Known value out of bounds public keys.
  // These MUST fail when loaded by the crypto provider or when running extern NIST validation.
  const ECC_P256_PUBLIC_GP := "3059301306072a864886f70d0106082a864886f70d03010703420004000000000000000"
                              + "00000000000000000000000000000000000000000000000000000000000000000000000"
                              + "00000000000000000000000000000000000000000000000000000000000000000000000"
                              + "000000001"
  const ECC_P384_PUBLIC_GP := "3076301006072a864886f70d0106052b810400220362000400000000000000000000000"
                              + "00000000000000000000000000000000000000000000000000000000000000000000000"
                              + "00000000000000000000000000000000000000000000000000000000000000000000000"
                              + "00000000000000000000000000000000000000000000000000000000000000000000000"
                              + "00000000000000000000000000000000000000000000000000000000000000000000000"
                              + "0000000000000000000000000000001"
  const ECC_P521_PUBLIC_GP := "3081ee3010060772a8648ce3d02106052b8104002303818600040000000000000000000"
                              + "00000000000000000000000000000000000000000000000000000000000000000000000"
                              + "00000000000000000000000000000000000000000000000000000000000000000000000"
                              + "00000000000000000000000000000000000000000000000000000000000000000000000"
                              + "00000000000000000000000000000000000000000000000000000000000000000000000"
                              + "00000000000000000000000000000000001"

  const INFINITY_POINT_ERR_MSG_JAVA := "encoded key spec not recognized: Point at infinity"
  const INFINITY_POINT_ERR_MSG_NET6 := "Point at infinity (Parameter 'q')"
  const INFINITY_POINT_ERR_MSG_NET48 := "Point at infinity\r\nParameter name: q"
  const INFINITY_POINT_ERR_MSG_PYTHON := "Cannot load an EC public key where the point is at infinity"

  const OUT_OF_BOUNDS_ERR_MSG_JAVA := "encoded key spec not recognized: x value invalid for"
  const OUT_OF_BOUNDS_ERR_MSG_NET6 := "value invalid for Fp field element (Parameter 'x')"
  const OUT_OF_BOUNDS_ERR_MSG_NE48 := "value invalid for Fp field element\r\nParameter name: x"
  const OUT_OF_BOUNDS_ERR_MSG_PYTHON := "Invalid key"

  // Rust does not provide a separate error message for infinity or out of bounds
  const BAD_X509_KEY_ERR_MSG_RUST := "Invalid X509 Public Key."
  const BAD_X509_KEY_ERR_MSG_GO := "x509: failed to unmarshal elliptic curve point"

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

  method {:test} TestGetPublicKeyFromPrivatePem()
  {
    var pemPrivateKeys := [ECC_P256_PRIVATE, ECC_P384_PRIVATE, ECC_P521_PRIVATE];
    var derPublicKeys := [ECC_P256_PUBLIC, ECC_384_PUBLIC, ECC_P521_PUBLIC];
    var supportedCurves := [P256, P384, P521];

    for i := 0 to |supportedCurves|
    {
      var curve := supportedCurves[i];
      var privateKey :- expect UTF8.Encode(pemPrivateKeys[i]);
      var looseHexPublicKey := expectLooseHexString(derPublicKeys[i]);
      var publicKeyBytes := HexStrings.FromHexString(looseHexPublicKey);

      var expectedPublicKey :- expect ECDH.ParsePublicKey(
        Types.ParsePublicKeyInput(
          publicKey := publicKeyBytes
        ));

      var publicKey :- expect ECDH.GetPublicKeyFromPrivate(
        Types.GetPublicKeyFromPrivateKeyInput(
          eccCurve := curve,
          privateKey := Types.ECCPrivateKey(pem := privateKey)
        )
      );

      expect publicKey.publicKey == expectedPublicKey.publicKey.der;
    }
  }

  method {:test} TestGetPublicKeyFromPrivateIncorrectCruve()
  {
    var curve := P384;
    var privateKey :- expect UTF8.Encode(ECC_P256_PRIVATE);
    var looseHexPublicKey := expectLooseHexString(ECC_P256_PUBLIC);
    var publicKeyBytes := HexStrings.FromHexString(looseHexPublicKey);

    var expectedPublicKey :- expect ECDH.ParsePublicKey(
      Types.ParsePublicKeyInput(
        publicKey := publicKeyBytes
      ));

    var publicKey := ECDH.GetPublicKeyFromPrivate(
      Types.GetPublicKeyFromPrivateKeyInput(
        eccCurve := curve,
        privateKey := Types.ECCPrivateKey(pem := privateKey)
      )
    );

    expect publicKey.Failure?;
  }

  method expectLooseHexString(s: string)
    returns (s2: HexStrings.LooseHexString)
  {
    expect HexStrings.IsLooseHexString(s);
    return s;
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
          publicKey := keypairB.publicKey.der
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
            publicKey := keypairB.publicKey.der
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

  method {:test} TestValidatePublicKeyFailurePointAtINFFailOnLoad()
  {
    var publicKeysWithPointsAtINF := [
      ECC_256_PUBLIC_INF_FAIL_ON_LOAD, ECC_384_PUBLIC_INF_FAIL_ON_LOAD, ECC_521_PUBLIC_INF_FAIL_ON_LOAD
    ];
    var supportedCurves := [P256, P384, P521];
    for i := 0 to |supportedCurves|
    {
      var looseHexPublicKey := expectLooseHexString(publicKeysWithPointsAtINF[i]);
      var publicKeyBytes := HexStrings.FromHexString(looseHexPublicKey);

      var validPublicKey:= ECDH.ValidatePublicKey(
        Types.ValidatePublicKeyInput(
          eccCurve := supportedCurves[i],
          publicKey := publicKeyBytes
        )
      );
      expect validPublicKey.Failure?;

      expect validPublicKey.error.AwsCryptographicPrimitivesError?;
      var errMsg := validPublicKey.error.message;

      expect (
          errMsg == BAD_X509_KEY_ERR_MSG_RUST ||
          errMsg == BAD_X509_KEY_ERR_MSG_GO ||
          errMsg == INFINITY_POINT_ERR_MSG_JAVA ||
          errMsg == INFINITY_POINT_ERR_MSG_NET6 ||
          errMsg == INFINITY_POINT_ERR_MSG_NET48 ||
          seq_contains(errMsg, INFINITY_POINT_ERR_MSG_PYTHON)
        );
    }
  }

  method {:test} TestValidatePublicKeyFailurePointAtINF()
  {
    var publicKeysWithPointsAtINF := [ECC_256_PUBLIC_INF, ECC_384_PUBLIC_INF, ECC_521_PUBLIC_INF];
    var supportedCurves := [P256, P384, P521];
    for i := 0 to |supportedCurves|
    {
      var looseHexPublicKey := expectLooseHexString(publicKeysWithPointsAtINF[i]);
      var publicKeyBytes := HexStrings.FromHexString(looseHexPublicKey);

      var validPublicKey:= ECDH.ValidatePublicKey(
        Types.ValidatePublicKeyInput(
          eccCurve := supportedCurves[i],
          publicKey := publicKeyBytes
        )
      );
      expect validPublicKey.Failure?;
    }
  }

  method {:test} TestValidatePublicKeyFailurePointGreaterThanPFailOnLoad()
  {
    var publicKeysWithPointsGreaterThanP := [
      ECC_P256_PUBLIC_GP_FAIL_ON_LOAD, ECC_P384_PUBLIC_GP_FAIL_ON_LOAD, ECC_P521_PUBLIC_GP_FAIL_ON_LOAD
    ];
    var supportedCurves := [P256, P384, P521];
    for i := 0 to |supportedCurves|
    {
      var looseHexPublicKey := expectLooseHexString(publicKeysWithPointsGreaterThanP[i]);
      var publicKeyBytes := HexStrings.FromHexString(looseHexPublicKey);

      var validPublicKey:= ECDH.ValidatePublicKey(
        Types.ValidatePublicKeyInput(
          eccCurve := supportedCurves[i],
          publicKey := publicKeyBytes
        )
      );
      expect validPublicKey.Failure?;

      expect validPublicKey.error.AwsCryptographicPrimitivesError?;
      var errMsg := validPublicKey.error.message;
      expect (
          seq_contains(errMsg, OUT_OF_BOUNDS_ERR_MSG_JAVA) ||
          errMsg == BAD_X509_KEY_ERR_MSG_RUST ||
          errMsg == BAD_X509_KEY_ERR_MSG_GO ||
          errMsg == OUT_OF_BOUNDS_ERR_MSG_NET6 ||
          errMsg == OUT_OF_BOUNDS_ERR_MSG_NE48 ||
          seq_contains(errMsg, OUT_OF_BOUNDS_ERR_MSG_PYTHON)
        );
    }
  }

  method {:test} TestValidatePublicKeyFailurePointGreaterThanP()
  {
    var publicKeysWithPointsGreaterThanP := [ECC_P256_PUBLIC_GP, ECC_P384_PUBLIC_GP, ECC_P521_PUBLIC_GP];
    var supportedCurves := [P256, P384, P521];
    for i := 0 to |supportedCurves|
    {
      var looseHexPublicKey := expectLooseHexString(publicKeysWithPointsGreaterThanP[i]);
      var publicKeyBytes := HexStrings.FromHexString(looseHexPublicKey);

      var validPublicKey:= ECDH.ValidatePublicKey(
        Types.ValidatePublicKeyInput(
          eccCurve := supportedCurves[i],
          publicKey := publicKeyBytes
        )
      );
      expect validPublicKey.Failure?;
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
          publicKey := keypairB.publicKey.der
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

  method {:test} TestCompressDecompressPublicKey() {
    var supportedCurves := [P256, P384, P521];
    for i := 0 to |supportedCurves|
    {
      var curve := supportedCurves[i];
      var keypair :- expect ECDH.GenerateEccKeyPair(
        Types.GenerateECCKeyPairInput(
          eccCurve := curve
        )
      );
      var originalPublicKey := keypair.publicKey;

      var compressedPublicKeyResult :- expect ECDH.CompressPublicKey(
        Types.CompressPublicKeyInput(
          publicKey := originalPublicKey,
          eccCurve := curve
        )
      );

      expect compressedPublicKeyResult.compressedPublicKey != originalPublicKey.der;

      var compressedPublicKey := compressedPublicKeyResult.compressedPublicKey;

      var decompressedPublicKeyResult :- expect ECDH.DecompressPublicKey(
        Types.DecompressPublicKeyInput(
          compressedPublicKey := compressedPublicKey,
          eccCurve := curve
        )
      );

      var decompressedPublicKey := decompressedPublicKeyResult.publicKey;

      expect originalPublicKey.der == decompressedPublicKey.der;
    }
  }

  method {:test} {:vcs_split_on_every_assert} TestCompressDecompressConstantPublicKeys() {
    var derX509PublicKeys := [ECC_P256_PUBLIC, ECC_384_PUBLIC, ECC_P521_PUBLIC];
    var compressedKeys := [ECC_P256_PUBLIC_COMPRESSED, ECC_384_PUBLIC_COMPRESSED, ECC_P521_PUBLIC_COMPRESSED];
    var curves := [P256, P384, P521];

    for i := 0 to |curves|
    {
      var curve := curves[i];
      var originalPublicKey := expectLooseHexString(derX509PublicKeys[i]);
      var publicKeyBytes := HexStrings.FromHexString(originalPublicKey);
      var compressedKey := expectLooseHexString(compressedKeys[i]);
      var compressedKeyBytes := HexStrings.FromHexString(compressedKey);

      var compressedPublicKeyResult :- expect ECDH.CompressPublicKey(
        Types.CompressPublicKeyInput(
          publicKey := Types.ECCPublicKey(der := publicKeyBytes),
          eccCurve := curve
        )
      );

      expect compressedPublicKeyResult.compressedPublicKey == compressedKeyBytes;

      var compressedPublicKey := compressedPublicKeyResult.compressedPublicKey;

      var decompressedPublicKeyResult :- expect ECDH.DecompressPublicKey(
        Types.DecompressPublicKeyInput(
          compressedPublicKey := compressedPublicKey,
          eccCurve := curve
        )
      );

      var decompressedPublicKey := decompressedPublicKeyResult.publicKey;

      expect publicKeyBytes == decompressedPublicKey.der;
    }
  }

  method {:test} TestPublicKeyValidationTestVectorsInfinity()
  {
    var curves := [P256, P384, P521];

    for i := 0 to |curves|
    {
      var der_ecc_inf :- expect GetInfinityPublicKey(curves[i]);

      var validPublicKeyB := ECDH.ValidatePublicKey(
        Types.ValidatePublicKeyInput(
          eccCurve := curves[i],
          publicKey := der_ecc_inf
        ));

      expect validPublicKeyB.Failure?;
      expect validPublicKeyB.error.AwsCryptographicPrimitivesError?;
      var errMsg := validPublicKeyB.error.message;

      expect (
          errMsg == INFINITY_POINT_ERR_MSG_JAVA ||
          errMsg == BAD_X509_KEY_ERR_MSG_RUST ||
          errMsg == BAD_X509_KEY_ERR_MSG_GO ||
          errMsg == INFINITY_POINT_ERR_MSG_NET6 ||
          errMsg == INFINITY_POINT_ERR_MSG_NET48 ||
          seq_contains(errMsg, INFINITY_POINT_ERR_MSG_PYTHON)
        );
    }
  }

  method {:test} TestPublicKeyValidationTestVectorsOutOfBounds()
  {
    var curves := [P256, P384, P521];

    for i := 0 to |curves|
    {
      var der_ecc_inf :- expect GetOutOfBoundsPublicKey(curves[i]);

      var validPublicKeyB := ECDH.ValidatePublicKey(
        Types.ValidatePublicKeyInput(
          eccCurve := curves[i],
          publicKey := der_ecc_inf
        ));

      expect validPublicKeyB.Failure?;
      expect validPublicKeyB.error.AwsCryptographicPrimitivesError?;
      var errMsg := validPublicKeyB.error.message;

      expect (
          seq_contains(errMsg, OUT_OF_BOUNDS_ERR_MSG_JAVA) ||
          errMsg == BAD_X509_KEY_ERR_MSG_RUST ||
          errMsg == BAD_X509_KEY_ERR_MSG_GO ||
          errMsg == OUT_OF_BOUNDS_ERR_MSG_NET6 ||
          errMsg == OUT_OF_BOUNDS_ERR_MSG_NE48 ||
          seq_contains(errMsg, OUT_OF_BOUNDS_ERR_MSG_PYTHON)
        );
    }

  }

  predicate method  {:tailrecursion} seq_contains<T(==)>(haystack : seq<T>, needle : seq<T>)
  {
    if |needle| == 0 then
      true
    else if |haystack| == 0 then
      false
    else if |haystack| < |needle|  then
      false
    else if needle[0] == haystack[0] && needle[1..] <= haystack[1..] then
      true
    else
      seq_contains(haystack[1..], needle)
  }

  method {:extern "ECDH.ECCUtils", "GetInfinityPublicKey" } GetInfinityPublicKey(curve: Types.ECDHCurveSpec)
    returns (res: Result<seq<uint8>, Types.Error>)

  method {:extern "ECDH.ECCUtils", "GetOutOfBoundsPublicKey" } GetOutOfBoundsPublicKey(curve: Types.ECDHCurveSpec)
    returns (res: Result<seq<uint8>, Types.Error>)

}
