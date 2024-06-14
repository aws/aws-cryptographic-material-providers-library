// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../../src/Index.dfy"
include "../TestUtils.dfy"
include "../../src/ErrorMessages.dfy"

module {:options "/functionSyntax:4" } TestRawECDHKeyring {
  import opened Wrappers
  import TestUtils
  import UTF8
  import ComAmazonawsKmsTypes
  import Com.Amazonaws.Kms
  import Aws.Cryptography.Primitives
  import AwsCryptographyPrimitivesTypes
  import MaterialProviders
  import Types = AwsCryptographyMaterialProvidersTypes
  import ErrorMessages
  import AlgorithmSuites
  import PrimitiveTypes = AwsCryptographyPrimitivesTypes

  const P256 := PrimitiveTypes.ECDHCurveSpec.ECC_NIST_P256
  const P384 := PrimitiveTypes.ECDHCurveSpec.ECC_NIST_P384
  const P521 := PrimitiveTypes.ECDHCurveSpec.ECC_NIST_P521

  const TEST_DBE_ALG_SUITE_ID := Types.AlgorithmSuiteId.DBE(Types.ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY_SYMSIG_HMAC_SHA384)

  method {:test} TestRawEcdhDiscoveryOnEncryptFailure() {
    var mpl :- expect MaterialProviders.MaterialProviders();
    var primitives :- expect Primitives.AtomicPrimitives();

    var keypair :- expect primitives.GenerateECCKeyPair(
      PrimitiveTypes.GenerateECCKeyPairInput(
        eccCurve := P256
      )
    );

    var keyring :- expect mpl.CreateRawEcdhKeyring(
      Types.CreateRawEcdhKeyringInput(
        KeyAgreementScheme := Types.PublicKeyDiscovery(
          Types.PublicKeyDiscoveryInput(recipientStaticPrivateKey := keypair.privateKey.pem)
        ),
        curveSpec := AwsCryptographyPrimitivesTypes.ECC_NIST_P256
      )
    );

    var encryptionContext := TestUtils.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation.A);

    var algorithmSuiteId := Types.AlgorithmSuiteId.ESDK(Types.ALG_AES_256_GCM_IV12_TAG16_NO_KDF);
    var encryptionMaterialsIn :- expect mpl.InitializeEncryptionMaterials(
      Types.InitializeEncryptionMaterialsInput(
        algorithmSuiteId := algorithmSuiteId,
        encryptionContext := encryptionContext,
        signingKey := None,
        verificationKey := None,
        requiredEncryptionContextKeys := []
      )
    );

    var encryptionMaterialsOut := keyring.OnEncrypt(
      Types.OnEncryptInput(materials:=encryptionMaterialsIn)
    );

    expect encryptionMaterialsOut.IsFailure();
    expect encryptionMaterialsOut.error.AwsCryptographicMaterialProvidersException?;

    var expectedErrorMessage := ErrorMessages.RAW_ECDH_DISCOVERY_ENCRYPT_ERROR;
    expect encryptionMaterialsOut.error.message == expectedErrorMessage;
  }

  method {:test} TestRawEcdhEphemeralOnDecryptFailure() {
    var mpl :- expect MaterialProviders.MaterialProviders();
    var primitives :- expect Primitives.AtomicPrimitives();

    var keypair :- expect primitives.GenerateECCKeyPair(
      PrimitiveTypes.GenerateECCKeyPairInput(
        eccCurve := P256
      )
    );

    var keyring :- expect mpl.CreateRawEcdhKeyring(
      Types.CreateRawEcdhKeyringInput(
        KeyAgreementScheme := Types.EphemeralPrivateKeyToStaticPublicKey(
          Types.EphemeralPrivateKeyToStaticPublicKeyInput(
            recipientPublicKey := keypair.publicKey.der
          )
        ),
        curveSpec := AwsCryptographyPrimitivesTypes.ECC_NIST_P256
      )
    );

    var encryptionContext := TestUtils.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation.A);

    var algorithmSuiteId := Types.AlgorithmSuiteId.ESDK(Types.ALG_AES_256_GCM_IV12_TAG16_NO_KDF);
    var decryptionMaterialsIn :- expect mpl.InitializeDecryptionMaterials(
      Types.InitializeDecryptionMaterialsInput(
        algorithmSuiteId := algorithmSuiteId,
        encryptionContext := map[],
        requiredEncryptionContextKeys := []
      )
    );

    var decryptionMaterialsOutRes := keyring.OnDecrypt(
      Types.OnDecryptInput(
        materials:=decryptionMaterialsIn,
        encryptedDataKeys:=[]
      )
    );
    expect decryptionMaterialsOutRes.Failure?;
    expect decryptionMaterialsOutRes.error.AwsCryptographicMaterialProvidersException?;

    expect decryptionMaterialsOutRes.error.message == ErrorMessages.RAW_ECDH_EPHEMERAL_DECRYPT_ERROR;
  }

  method {:test} TestRawEcdhKeyringEphemeralDecryptOwnMessageFailure() {
    var mpl :- expect MaterialProviders.MaterialProviders();
    var primitives :- expect Primitives.AtomicPrimitives();

    var keypair :- expect primitives.GenerateECCKeyPair(
      PrimitiveTypes.GenerateECCKeyPairInput(
        eccCurve := P256
      )
    );

    var keyring :- expect mpl.CreateRawEcdhKeyring(
      Types.CreateRawEcdhKeyringInput(
        KeyAgreementScheme := Types.EphemeralPrivateKeyToStaticPublicKey(
          Types.EphemeralPrivateKeyToStaticPublicKeyInput(
            recipientPublicKey := keypair.publicKey.der
          )
        ),
        curveSpec := AwsCryptographyPrimitivesTypes.ECC_NIST_P256
      )
    );

    var encryptionContext := TestUtils.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation.A);

    var algorithmSuiteId := Types.AlgorithmSuiteId.ESDK(Types.ALG_AES_256_GCM_IV12_TAG16_NO_KDF);
    var encryptionMaterialsIn :- expect mpl.InitializeEncryptionMaterials(
      Types.InitializeEncryptionMaterialsInput(
        algorithmSuiteId := algorithmSuiteId,
        encryptionContext := encryptionContext,
        signingKey := None,
        verificationKey := None,
        requiredEncryptionContextKeys := []
      )
    );

    var encryptionMaterialsOut :- expect keyring.OnEncrypt(
      Types.OnEncryptInput(materials:=encryptionMaterialsIn)
    );

    var _ :- expect mpl.EncryptionMaterialsHasPlaintextDataKey(encryptionMaterialsOut.materials);

    expect |encryptionMaterialsOut.materials.encryptedDataKeys| == 1;
    var edk := encryptionMaterialsOut.materials.encryptedDataKeys[0];

    var decryptionMaterialsIn :- expect mpl.InitializeDecryptionMaterials(
      Types.InitializeDecryptionMaterialsInput(
        algorithmSuiteId := algorithmSuiteId,
        encryptionContext := encryptionContext,
        requiredEncryptionContextKeys := []
      )
    );
    var decryptionMaterialsOut := keyring.OnDecrypt(
      Types.OnDecryptInput(
        materials:=decryptionMaterialsIn,
        encryptedDataKeys:=[edk]
      )
    );

    expect decryptionMaterialsOut.Failure?;
    expect decryptionMaterialsOut.error.AwsCryptographicMaterialProvidersException?;

    var expectedErrorMessage := ErrorMessages.RAW_ECDH_EPHEMERAL_DECRYPT_ERROR;
    expect decryptionMaterialsOut.error.message == expectedErrorMessage;
  }

  method {:test} TestRawEcdhKeyringStaticSuccess() {
    var mpl :- expect MaterialProviders.MaterialProviders();
    var primitives :- expect Primitives.AtomicPrimitives();

    var senderKeypair :- expect primitives.GenerateECCKeyPair(
      PrimitiveTypes.GenerateECCKeyPairInput(
        eccCurve := P256
      )
    );

    var recipientKeypair :- expect primitives.GenerateECCKeyPair(
      PrimitiveTypes.GenerateECCKeyPairInput(
        eccCurve := P256
      )
    );

    var keyring :- expect mpl.CreateRawEcdhKeyring(
      Types.CreateRawEcdhKeyringInput(
        KeyAgreementScheme := Types.RawPrivateKeyToStaticPublicKey(
          Types.RawPrivateKeyToStaticPublicKeyInput(
            senderStaticPrivateKey := senderKeypair.privateKey.pem,
            recipientPublicKey := recipientKeypair.publicKey.der
          )
        ),
        curveSpec := AwsCryptographyPrimitivesTypes.ECC_NIST_P256
      )
    );

    var encryptionContext := TestUtils.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation.A);

    var algorithmSuiteId := Types.AlgorithmSuiteId.ESDK(Types.ALG_AES_256_GCM_IV12_TAG16_NO_KDF);
    var encryptionMaterialsIn :- expect mpl.InitializeEncryptionMaterials(
      Types.InitializeEncryptionMaterialsInput(
        algorithmSuiteId := algorithmSuiteId,
        encryptionContext := encryptionContext,
        signingKey := None,
        verificationKey := None,
        requiredEncryptionContextKeys := []
      )
    );

    var encryptionMaterialsOut :- expect keyring.OnEncrypt(
      Types.OnEncryptInput(materials:=encryptionMaterialsIn)
    );

    var _ :- expect mpl.EncryptionMaterialsHasPlaintextDataKey(encryptionMaterialsOut.materials);

    expect |encryptionMaterialsOut.materials.encryptedDataKeys| == 1;
    var edk := encryptionMaterialsOut.materials.encryptedDataKeys[0];

    var decryptionMaterialsIn :- expect mpl.InitializeDecryptionMaterials(
      Types.InitializeDecryptionMaterialsInput(
        algorithmSuiteId := algorithmSuiteId,
        encryptionContext := encryptionContext,
        requiredEncryptionContextKeys := []
      )
    );
    var decryptionMaterialsOut :- expect keyring.OnDecrypt(
      Types.OnDecryptInput(
        materials:=decryptionMaterialsIn,
        encryptedDataKeys:=[edk]
      )
    );

    expect encryptionMaterialsOut.materials.plaintextDataKey
        == decryptionMaterialsOut.materials.plaintextDataKey;

  }

  method {:test} TestTwoRawEcdhKeyringStaticSuccess() {
    var mpl :- expect MaterialProviders.MaterialProviders();
    var primitives :- expect Primitives.AtomicPrimitives();

    var senderKeypair :- expect primitives.GenerateECCKeyPair(
      PrimitiveTypes.GenerateECCKeyPairInput(
        eccCurve := P256
      )
    );

    var recipientKeypair :- expect primitives.GenerateECCKeyPair(
      PrimitiveTypes.GenerateECCKeyPairInput(
        eccCurve := P256
      )
    );

    var senderKeyring :- expect mpl.CreateRawEcdhKeyring(
      Types.CreateRawEcdhKeyringInput(
        KeyAgreementScheme := Types.RawPrivateKeyToStaticPublicKey(
          Types.RawPrivateKeyToStaticPublicKeyInput(
            senderStaticPrivateKey := senderKeypair.privateKey.pem,
            recipientPublicKey := recipientKeypair.publicKey.der
          )
        ),
        curveSpec := AwsCryptographyPrimitivesTypes.ECC_NIST_P256
      )
    );

    var recipientKeyring :- expect mpl.CreateRawEcdhKeyring(
      Types.CreateRawEcdhKeyringInput(
        KeyAgreementScheme := Types.RawPrivateKeyToStaticPublicKey(
          Types.RawPrivateKeyToStaticPublicKeyInput(
            senderStaticPrivateKey := recipientKeypair.privateKey.pem,
            recipientPublicKey := senderKeypair.publicKey.der
          )
        ),
        curveSpec := AwsCryptographyPrimitivesTypes.ECC_NIST_P256
      )
    );

    var encryptionContext := TestUtils.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation.A);

    var algorithmSuiteId := Types.AlgorithmSuiteId.ESDK(Types.ALG_AES_256_GCM_IV12_TAG16_NO_KDF);
    var encryptionMaterialsIn :- expect mpl.InitializeEncryptionMaterials(
      Types.InitializeEncryptionMaterialsInput(
        algorithmSuiteId := algorithmSuiteId,
        encryptionContext := encryptionContext,
        signingKey := None,
        verificationKey := None,
        requiredEncryptionContextKeys := []
      )
    );

    var encryptionMaterialsOut :- expect senderKeyring.OnEncrypt(
      Types.OnEncryptInput(materials:=encryptionMaterialsIn)
    );

    var _ :- expect mpl.EncryptionMaterialsHasPlaintextDataKey(encryptionMaterialsOut.materials);

    expect |encryptionMaterialsOut.materials.encryptedDataKeys| == 1;
    var edk := encryptionMaterialsOut.materials.encryptedDataKeys[0];

    var decryptionMaterialsIn :- expect mpl.InitializeDecryptionMaterials(
      Types.InitializeDecryptionMaterialsInput(
        algorithmSuiteId := algorithmSuiteId,
        encryptionContext := encryptionContext,
        requiredEncryptionContextKeys := []
      )
    );
    var decryptionMaterialsOut :- expect recipientKeyring.OnDecrypt(
      Types.OnDecryptInput(
        materials:=decryptionMaterialsIn,
        encryptedDataKeys:=[edk]
      )
    );

    expect encryptionMaterialsOut.materials.plaintextDataKey
        == decryptionMaterialsOut.materials.plaintextDataKey;

  }

  method {:test} TestTwoEcdhKeyringStaticSuccess() {
    var mpl :- expect MaterialProviders.MaterialProviders();
    var primitives :- expect Primitives.AtomicPrimitives();

    var senderKeypair :- expect primitives.GenerateECCKeyPair(
      PrimitiveTypes.GenerateECCKeyPairInput(
        eccCurve := P256
      )
    );

    var kmsClient :- expect Kms.GammaKmsClient();
    var publicKeyResponse := kmsClient.GetPublicKey(
      Kms.Types.GetPublicKeyRequest(
        KeyId := TestUtils.KMS_ECC_256_KEY_ARN_R,
        GrantTokens := None
      )
    );
    expect(publicKeyResponse.Success?);

    var GetPublicKeyResponse(_,PublicKey,_,_,_,_,_,_) := publicKeyResponse.value;
    expect PublicKey.Some?;

    var senderKeyring :- expect mpl.CreateRawEcdhKeyring(
      Types.CreateRawEcdhKeyringInput(
        KeyAgreementScheme := Types.RawPrivateKeyToStaticPublicKey(
          Types.RawPrivateKeyToStaticPublicKeyInput(
            senderStaticPrivateKey := senderKeypair.privateKey.pem,
            recipientPublicKey := PublicKey.value
          )
        ),
        curveSpec := AwsCryptographyPrimitivesTypes.ECC_NIST_P256
      )
    );

    var recipientKmsEcdhKeyring :- expect mpl.CreateAwsKmsEcdhKeyring(
      Types.CreateAwsKmsEcdhKeyringInput(
        KeyAgreementScheme := Types.KmsEcdhStaticConfigurations.KmsPrivateKeyToStaticPublicKey(
          Types.KmsPrivateKeyToStaticPublicKeyInput(
            senderKmsIdentifier := TestUtils.KMS_ECC_256_KEY_ARN_R,
            recipientPublicKey := senderKeypair.publicKey.der
          )
        ),
        curveSpec := AwsCryptographyPrimitivesTypes.ECC_NIST_P256,
        kmsClient := kmsClient,
        grantTokens := None()
      )
    );

    var encryptionContext := TestUtils.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation.A);

    var algorithmSuiteId := Types.AlgorithmSuiteId.ESDK(Types.ALG_AES_256_GCM_IV12_TAG16_NO_KDF);
    var encryptionMaterialsIn :- expect mpl.InitializeEncryptionMaterials(
      Types.InitializeEncryptionMaterialsInput(
        algorithmSuiteId := algorithmSuiteId,
        encryptionContext := encryptionContext,
        signingKey := None,
        verificationKey := None,
        requiredEncryptionContextKeys := []
      )
    );

    var encryptionMaterialsOut :- expect senderKeyring.OnEncrypt(
      Types.OnEncryptInput(materials:=encryptionMaterialsIn)
    );

    var _ :- expect mpl.EncryptionMaterialsHasPlaintextDataKey(encryptionMaterialsOut.materials);

    expect |encryptionMaterialsOut.materials.encryptedDataKeys| == 1;
    var edk := encryptionMaterialsOut.materials.encryptedDataKeys[0];

    var decryptionMaterialsIn :- expect mpl.InitializeDecryptionMaterials(
      Types.InitializeDecryptionMaterialsInput(
        algorithmSuiteId := algorithmSuiteId,
        encryptionContext := encryptionContext,
        requiredEncryptionContextKeys := []
      )
    );
    var decryptionMaterialsOut :- expect recipientKmsEcdhKeyring.OnDecrypt(
      Types.OnDecryptInput(
        materials:=decryptionMaterialsIn,
        encryptedDataKeys:=[edk]
      )
    );

    expect encryptionMaterialsOut.materials.plaintextDataKey
        == decryptionMaterialsOut.materials.plaintextDataKey;

  }

  method {:test} TestRawEcdhKeyringEncryptDecryptSuccessDBESDKSuite() {
    var mpl :- expect MaterialProviders.MaterialProviders();
    var primitives :- expect Primitives.AtomicPrimitives();

    var senderKeypair :- expect primitives.GenerateECCKeyPair(
      PrimitiveTypes.GenerateECCKeyPairInput(
        eccCurve := P256
      )
    );

    var recipientKeypair :- expect primitives.GenerateECCKeyPair(
      PrimitiveTypes.GenerateECCKeyPairInput(
        eccCurve := P256
      )
    );

    var senderKeyring :- expect mpl.CreateRawEcdhKeyring(
      Types.CreateRawEcdhKeyringInput(
        KeyAgreementScheme := Types.RawPrivateKeyToStaticPublicKey(
          Types.RawPrivateKeyToStaticPublicKeyInput(
            senderStaticPrivateKey := senderKeypair.privateKey.pem,
            recipientPublicKey := recipientKeypair.publicKey.der
          )
        ),
        curveSpec := AwsCryptographyPrimitivesTypes.ECC_NIST_P256
      )
    );

    var recipientKeyring :- expect mpl.CreateRawEcdhKeyring(
      Types.CreateRawEcdhKeyringInput(
        KeyAgreementScheme := Types.RawPrivateKeyToStaticPublicKey(
          Types.RawPrivateKeyToStaticPublicKeyInput(
            senderStaticPrivateKey := recipientKeypair.privateKey.pem,
            recipientPublicKey := senderKeypair.publicKey.der
          )
        ),
        curveSpec := AwsCryptographyPrimitivesTypes.ECC_NIST_P256
      )
    );

    var encryptionContext := TestUtils.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation.A);
    var materials := GetTestMaterials(TEST_DBE_ALG_SUITE_ID);


    var encryptionMaterialsOut :- expect senderKeyring.OnEncrypt(
      Types.OnEncryptInput(materials:=materials)
    );

    var _ :- expect mpl.EncryptionMaterialsHasPlaintextDataKey(encryptionMaterialsOut.materials);

    expect |encryptionMaterialsOut.materials.encryptedDataKeys| == 1;
    var edk := encryptionMaterialsOut.materials.encryptedDataKeys[0];

    var decryptionMaterialsIn :- expect mpl.InitializeDecryptionMaterials(
      Types.InitializeDecryptionMaterialsInput(
        algorithmSuiteId := TEST_DBE_ALG_SUITE_ID,
        encryptionContext := encryptionContext,
        requiredEncryptionContextKeys := []
      )
    );
    var decryptionMaterialsOut :- expect recipientKeyring.OnDecrypt(
      Types.OnDecryptInput(
        materials:=decryptionMaterialsIn,
        encryptedDataKeys:=[edk]
      )
    );

    expect encryptionMaterialsOut.materials.plaintextDataKey
        == decryptionMaterialsOut.materials.plaintextDataKey;



  }

  method GetTestMaterials(suiteId: Types.AlgorithmSuiteId) returns (out: Types.EncryptionMaterials)
  {
    var mpl :- expect MaterialProviders.MaterialProviders();

    var encryptionContext := TestUtils.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation.A);
    var suite := AlgorithmSuites.GetSuite(suiteId);
    // Add data key to test the case where i have a pdk
    var encryptionMaterialsIn :- expect mpl.InitializeEncryptionMaterials(
      Types.InitializeEncryptionMaterialsInput(
        algorithmSuiteId := suiteId,
        encryptionContext := encryptionContext,
        requiredEncryptionContextKeys := [],
        signingKey := None,
        verificationKey := None
      )
    );

    return encryptionMaterialsIn;
  }
}
