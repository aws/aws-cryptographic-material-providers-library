// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../../../src/Index.dfy"
include "../../TestUtils.dfy"
include "../../../../../../ComAmazonawsKms/src/Index.dfy"
include "../../../src/ErrorMessages.dfy"

module {:options "/functionSyntax:4" } TestAwsKmsEcdhKeyring {
  import opened Wrappers
  import opened UInt = StandardLibrary.UInt
  import MaterialProviders
  import Types = AwsCryptographyMaterialProvidersTypes
  import AtomicPrimitives
  import PrimitiveTypes = AwsCryptographyPrimitivesTypes
  import Com.Amazonaws.Kms
  import AwsKmsRsaKeyring
  import TestUtils
  import Base64
  import ComAmazonawsKmsTypes
  import AwsCryptographyPrimitivesTypes
  import AlgorithmSuites
  import UTF8
  import ErrorMessages

  const TEST_DBE_ALG_SUITE_ID := Types.AlgorithmSuiteId.DBE(Types.ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY_SYMSIG_HMAC_SHA384)

  const derKmsSenderPublicKeyStrings := [TestUtils.KMS_ECC_256_PUBLIC_KEY_S, TestUtils.KMS_ECC_384_PUBLIC_KEY_S, TestUtils.KMS_ECC_521_PUBLIC_KEY_S]
  const senderKmsKeys := [TestUtils.KMS_ECC_256_KEY_ARN_S, TestUtils.KMS_ECC_384_KEY_ARN_S, TestUtils.KMS_ECC_521_KEY_ARN_S]
  const derKmsRecipientPublicKeyStrings := [TestUtils.KMS_ECC_256_PUBLIC_KEY_R, TestUtils.KMS_ECC_384_PUBLIC_KEY_R, TestUtils.KMS_ECC_521_PUBLIC_KEY_R]
  const recipientKmsKeys := [TestUtils.KMS_ECC_256_KEY_ARN_R, TestUtils.KMS_ECC_384_KEY_ARN_R, TestUtils.KMS_ECC_521_KEY_ARN_R]

  const rawEccPrivateKeys := [TestUtils.ECC_P256_PRIVATE, TestUtils.ECC_P384_PRIVATE, TestUtils.ECC_P521_PRIVATE]
  const rawEccPublicKeysB64der := [TestUtils.ECC_P256_PUBLIC, TestUtils.ECC_P384_PUBLIC, TestUtils.ECC_P521_PUBLIC]

  const P256 := PrimitiveTypes.ECDHCurveSpec.ECC_NIST_P256
  const P384 := PrimitiveTypes.ECDHCurveSpec.ECC_NIST_P384
  const P521 := PrimitiveTypes.ECDHCurveSpec.ECC_NIST_P521

  const CURVES := [P256, P384, P521]

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

  method {:test} TestKmsEcdhConfigurationFailure() {
    var mpl :- expect MaterialProviders.MaterialProviders();

    var kmsClient :- expect Kms.KMSClient();

    var kmsEcdhKeyringDiscoveryConfiguration :- expect mpl.CreateAwsKmsEcdhKeyring(
      Types.CreateAwsKmsEcdhKeyringInput(
        KeyAgreementScheme := Types.KmsEcdhStaticConfigurations.KmsPublicKeyDiscovery(
          Types.KmsPublicKeyDiscoveryInput(
            recipientKmsIdentifier := TestUtils.KMS_ECC_256_KEY_ARN_R
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

    var encryptionMaterialsOut := kmsEcdhKeyringDiscoveryConfiguration.OnEncrypt(
      Types.OnEncryptInput(materials:=encryptionMaterialsIn)
    );

    expect encryptionMaterialsOut.IsFailure();
    expect encryptionMaterialsOut.error.AwsCryptographicMaterialProvidersException?;

    var expectedErrorMessage := ErrorMessages.KMS_ECDH_DISCOVERY_ENCRYPT_ERROR;
    expect encryptionMaterialsOut.error.message == expectedErrorMessage;
  }

  method {:test} TestKmsEcdhKeyringRecipientKmsKeyEncryptDecryptSuccess() {
    var mpl :- expect MaterialProviders.MaterialProviders();

    var kmsClient :- expect Kms.KMSClient();

    var senderArns := [TestUtils.KMS_ECC_256_KEY_ARN_S, TestUtils.KMS_ECC_384_KEY_ARN_S, TestUtils.KMS_ECC_521_KEY_ARN_S];
    var recipientArns := [TestUtils.KMS_ECC_256_KEY_ARN_R, TestUtils.KMS_ECC_384_KEY_ARN_R, TestUtils.KMS_ECC_521_KEY_ARN_R];
    var curveSpecs := [AwsCryptographyPrimitivesTypes.ECC_NIST_P256, AwsCryptographyPrimitivesTypes.ECC_NIST_P384, AwsCryptographyPrimitivesTypes.ECC_NIST_P521];

    for i := 0 to |senderArns|
    {
      var publicKeyResponse := kmsClient.GetPublicKey(
        Kms.Types.GetPublicKeyRequest(
          KeyId := recipientArns[i],
          GrantTokens := None
        )
      );
      expect(publicKeyResponse.Success?);
      var GetPublicKeyResponse(_,PublicKey,_,_,_,_,_,_) := publicKeyResponse.value;
      expect PublicKey.Some?;

      // print "\nTest with sender: " + senderArns[i] + " and recipient: " + recipientArns[i] + "\n";
      var kmsEcdhKeyring :- expect mpl.CreateAwsKmsEcdhKeyring(
        Types.CreateAwsKmsEcdhKeyringInput(
          KeyAgreementScheme := Types.KmsEcdhStaticConfigurations.KmsPrivateKeyToStaticPublicKey(
            Types.KmsPrivateKeyToStaticPublicKeyInput(
              senderKmsIdentifier := senderArns[i],
              recipientPublicKey := PublicKey.value
            )
          ),
          curveSpec := curveSpecs[i],
          kmsClient := kmsClient,
          grantTokens := None()
        )
      );

      var encryptionContext := TestUtils.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation.A);

      var algorithmSuiteId := Types.AlgorithmSuiteId.ESDK(Types.ALG_AES_256_GCM_IV12_TAG16_NO_KDF);
      var suite := AlgorithmSuites.GetSuite(algorithmSuiteId);
      var encryptionMaterialsIn :- expect mpl.InitializeEncryptionMaterials(
        Types.InitializeEncryptionMaterialsInput(
          algorithmSuiteId := algorithmSuiteId,
          encryptionContext := encryptionContext,
          requiredEncryptionContextKeys := [],
          signingKey := None,
          verificationKey := None
        )
      );

      var encryptionMaterialsOut :- expect kmsEcdhKeyring.OnEncrypt(
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
      var decryptionMaterialsOut :- expect kmsEcdhKeyring.OnDecrypt(
        Types.OnDecryptInput(
          materials:=decryptionMaterialsIn,
          encryptedDataKeys:=[edk]
        )
      );

      expect encryptionMaterialsOut.materials.plaintextDataKey
          == decryptionMaterialsOut.materials.plaintextDataKey;
    }
  }

  method {:test} TestKmsEcdhKeyringRecipientKmsKeyEncryptDecryptSuccessDBESDKSuite() {
    var mpl :- expect MaterialProviders.MaterialProviders();

    var kmsClient :- expect Kms.KMSClient();

    var senderArns := [TestUtils.KMS_ECC_256_KEY_ARN_S, TestUtils.KMS_ECC_384_KEY_ARN_S, TestUtils.KMS_ECC_521_KEY_ARN_S];
    var recipientArns := [TestUtils.KMS_ECC_256_KEY_ARN_R, TestUtils.KMS_ECC_384_KEY_ARN_R, TestUtils.KMS_ECC_521_KEY_ARN_R];
    var curveSpecs := [AwsCryptographyPrimitivesTypes.ECC_NIST_P256, AwsCryptographyPrimitivesTypes.ECC_NIST_P384, AwsCryptographyPrimitivesTypes.ECC_NIST_P521];

    for i := 0 to |senderArns|
    {
      var publicKeyResponse := kmsClient.GetPublicKey(
        Kms.Types.GetPublicKeyRequest(
          KeyId := recipientArns[i],
          GrantTokens := None
        )
      );
      expect(publicKeyResponse.Success?);
      var GetPublicKeyResponse(_,PublicKey,_,_,_,_,_,_) := publicKeyResponse.value;
      expect PublicKey.Some?;

      // print "\nTest with sender: " + senderArns[i] + " and recipient: " + recipientArns[i] + "\n";
      var kmsEcdhKeyring :- expect mpl.CreateAwsKmsEcdhKeyring(
        Types.CreateAwsKmsEcdhKeyringInput(
          KeyAgreementScheme := Types.KmsEcdhStaticConfigurations.KmsPrivateKeyToStaticPublicKey(
            Types.KmsPrivateKeyToStaticPublicKeyInput(
              senderKmsIdentifier := senderArns[i],
              recipientPublicKey := PublicKey.value
            )
          ),
          curveSpec := curveSpecs[i],
          kmsClient := kmsClient,
          grantTokens := None()
        )
      );

      var encryptionContext := TestUtils.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation.A);
      var materials := GetTestMaterials(TEST_DBE_ALG_SUITE_ID);

      var encryptionMaterialsOut :- expect kmsEcdhKeyring.OnEncrypt(
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
      var decryptionMaterialsOut :- expect kmsEcdhKeyring.OnDecrypt(
        Types.OnDecryptInput(
          materials:=decryptionMaterialsIn,
          encryptedDataKeys:=[edk]
        )
      );

      expect encryptionMaterialsOut.materials.plaintextDataKey
          == decryptionMaterialsOut.materials.plaintextDataKey;
    }

  }

  method {:test} TestKmsEcdhKeyringDiscoverySuccess() {
    var mpl :- expect MaterialProviders.MaterialProviders();

    var kmsClient :- expect Kms.KMSClient();

    var senderArns := [TestUtils.KMS_ECC_256_KEY_ARN_S, TestUtils.KMS_ECC_384_KEY_ARN_S, TestUtils.KMS_ECC_521_KEY_ARN_S];
    var recipientArns := [TestUtils.KMS_ECC_256_KEY_ARN_R, TestUtils.KMS_ECC_384_KEY_ARN_R, TestUtils.KMS_ECC_521_KEY_ARN_R];
    var curveSpecs := [AwsCryptographyPrimitivesTypes.ECC_NIST_P256, AwsCryptographyPrimitivesTypes.ECC_NIST_P384, AwsCryptographyPrimitivesTypes.ECC_NIST_P521];

    for i := 0 to |senderArns|
    {
      var publicKeyResponse := kmsClient.GetPublicKey(
        Kms.Types.GetPublicKeyRequest(
          KeyId := recipientArns[i],
          GrantTokens := None
        )
      );
      expect(publicKeyResponse.Success?);
      var GetPublicKeyResponse(_,PublicKey,_,_,_,_,_,_) := publicKeyResponse.value;
      expect PublicKey.Some?;

      var kmsEcdhKeyring :- expect mpl.CreateAwsKmsEcdhKeyring(
        Types.CreateAwsKmsEcdhKeyringInput(
          KeyAgreementScheme := Types.KmsEcdhStaticConfigurations.KmsPrivateKeyToStaticPublicKey(
            Types.KmsPrivateKeyToStaticPublicKeyInput(
              senderKmsIdentifier := senderArns[i],
              recipientPublicKey := PublicKey.value
            )
          ),
          curveSpec := curveSpecs[i],
          kmsClient := kmsClient,
          grantTokens := None()
        )
      );

      var kmsEcdhKeyringDiscovery :- expect mpl.CreateAwsKmsEcdhKeyring(
        Types.CreateAwsKmsEcdhKeyringInput(
          KeyAgreementScheme := Types.KmsEcdhStaticConfigurations.KmsPublicKeyDiscovery(
            Types.KmsPublicKeyDiscoveryInput(
              recipientKmsIdentifier := recipientArns[i]
            )
          ),
          curveSpec := curveSpecs[i],
          kmsClient := kmsClient,
          grantTokens := None()
        )
      );

      var encryptionContext := TestUtils.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation.A);

      var algorithmSuiteId := Types.AlgorithmSuiteId.ESDK(Types.ALG_AES_256_GCM_IV12_TAG16_NO_KDF);
      var suite := AlgorithmSuites.GetSuite(algorithmSuiteId);
      var encryptionMaterialsIn :- expect mpl.InitializeEncryptionMaterials(
        Types.InitializeEncryptionMaterialsInput(
          algorithmSuiteId := algorithmSuiteId,
          encryptionContext := encryptionContext,
          requiredEncryptionContextKeys := [],
          signingKey := None,
          verificationKey := None
        )
      );

      var encryptionMaterialsOut :- expect kmsEcdhKeyring.OnEncrypt(
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
      // print "\nDiscovery Test for: " + recipientArns[i] + "\n";
      var decryptionMaterialsOut :- expect kmsEcdhKeyringDiscovery.OnDecrypt(
        Types.OnDecryptInput(
          materials:=decryptionMaterialsIn,
          encryptedDataKeys:=[edk]
        )
      );

      expect encryptionMaterialsOut.materials.plaintextDataKey
          == decryptionMaterialsOut.materials.plaintextDataKey;
    }
  }

  method {:test} TestKmsEcdhKeyringRecipientRawKeyEncryptDecryptSuccessSetSenderPublicKey()
  {
    var mpl :- expect MaterialProviders.MaterialProviders();
    var primitives :- expect AtomicPrimitives.AtomicPrimitives();

    var recipientKeypair :- expect primitives.GenerateECCKeyPair(
      PrimitiveTypes.GenerateECCKeyPairInput(
        eccCurve := P256
      )
    );

    var kmsClient :- expect Kms.KMSClient();
    var publicKeyResponse := kmsClient.GetPublicKey(
      Kms.Types.GetPublicKeyRequest(
        KeyId := TestUtils.KMS_ECC_256_KEY_ARN_S,
        GrantTokens := None
      )
    );
    expect(publicKeyResponse.Success?);

    var GetPublicKeyResponse(_,PublicKey,_,_,_,_,_,_) := publicKeyResponse.value;
    expect PublicKey.Some?;

    var kmsEcdhKeyring :- expect mpl.CreateAwsKmsEcdhKeyring(
      Types.CreateAwsKmsEcdhKeyringInput(
        KeyAgreementScheme := Types.KmsEcdhStaticConfigurations.KmsPrivateKeyToStaticPublicKey(
          Types.KmsPrivateKeyToStaticPublicKeyInput(
            senderKmsIdentifier := TestUtils.KMS_ECC_256_KEY_ARN_S,
            senderPublicKey := Some(PublicKey.value),
            recipientPublicKey := recipientKeypair.publicKey.der
          )
        ),
        curveSpec := AwsCryptographyPrimitivesTypes.ECC_NIST_P256,
        kmsClient := kmsClient,
        grantTokens := None()
      )
    );

    var recipientKeyring :- expect mpl.CreateRawEcdhKeyring(
      Types.CreateRawEcdhKeyringInput(
        KeyAgreementScheme := Types.RawPrivateKeyToStaticPublicKey(
          Types.RawPrivateKeyToStaticPublicKeyInput(
            senderStaticPrivateKey := recipientKeypair.privateKey.pem,
            recipientPublicKey := PublicKey.value
          )
        ),
        curveSpec := AwsCryptographyPrimitivesTypes.ECC_NIST_P256
      )
    );

    var encryptionContext := TestUtils.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation.A);

    var algorithmSuiteId := Types.AlgorithmSuiteId.ESDK(Types.ALG_AES_256_GCM_IV12_TAG16_NO_KDF);
    var suite := AlgorithmSuites.GetSuite(algorithmSuiteId);
    var encryptionMaterialsIn :- expect mpl.InitializeEncryptionMaterials(
      Types.InitializeEncryptionMaterialsInput(
        algorithmSuiteId := algorithmSuiteId,
        encryptionContext := encryptionContext,
        requiredEncryptionContextKeys := [],
        signingKey := None,
        verificationKey := None
      )
    );

    var encryptionMaterialsOut :- expect kmsEcdhKeyring.OnEncrypt(
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

  method {:test} TestKmsEcdhKeyringWithDerPublicKeys()
  {
    var mpl :- expect MaterialProviders.MaterialProviders();

    var kmsClient :- expect Kms.KMSClient();

    for i := 0 to |CURVES|
    {
      var senderPublicKey :- expect Base64.Decode(derKmsSenderPublicKeyStrings[i]);
      var recipientPublicKey :- expect Base64.Decode(derKmsRecipientPublicKeyStrings[i]);

      var senderKmsEcdhKeyring :- expect mpl.CreateAwsKmsEcdhKeyring(
        Types.CreateAwsKmsEcdhKeyringInput(
          KeyAgreementScheme := Types.KmsEcdhStaticConfigurations.KmsPrivateKeyToStaticPublicKey(
            Types.KmsPrivateKeyToStaticPublicKeyInput(
              senderKmsIdentifier := senderKmsKeys[i],
              senderPublicKey := Some(senderPublicKey),
              recipientPublicKey := recipientPublicKey
            )
          ),
          curveSpec := CURVES[i],
          kmsClient := kmsClient,
          grantTokens := None()
        )
      );

      var recipientKmsEcdhKeyring :- expect mpl.CreateAwsKmsEcdhKeyring(
        Types.CreateAwsKmsEcdhKeyringInput(
          KeyAgreementScheme := Types.KmsEcdhStaticConfigurations.KmsPrivateKeyToStaticPublicKey(
            Types.KmsPrivateKeyToStaticPublicKeyInput(
              senderKmsIdentifier := recipientKmsKeys[i],
              senderPublicKey := Some(recipientPublicKey),
              recipientPublicKey := senderPublicKey
            )
          ),
          curveSpec := CURVES[i],
          kmsClient := kmsClient,
          grantTokens := None()
        )
      );

      var encryptionContext := TestUtils.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation.A);

      var algorithmSuiteId := Types.AlgorithmSuiteId.ESDK(Types.ALG_AES_256_GCM_IV12_TAG16_NO_KDF);
      var suite := AlgorithmSuites.GetSuite(algorithmSuiteId);
      var encryptionMaterialsIn :- expect mpl.InitializeEncryptionMaterials(
        Types.InitializeEncryptionMaterialsInput(
          algorithmSuiteId := algorithmSuiteId,
          encryptionContext := encryptionContext,
          requiredEncryptionContextKeys := [],
          signingKey := None,
          verificationKey := None
        )
      );

      var encryptionMaterialsOut :- expect senderKmsEcdhKeyring.OnEncrypt(
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
  }

  method {:test} TestKmsEcdhRawEcdhKeyringWithDerPublicKeys()
  {
    var mpl :- expect MaterialProviders.MaterialProviders();

    var kmsClient :- expect Kms.KMSClient();

    for i := 0 to |CURVES|
    {
      var senderKmsKey := senderKmsKeys[i];
      var senderPublicKey :- expect Base64.Decode(derKmsSenderPublicKeyStrings[i]);
      var recipientPrivateKey :- expect UTF8.Encode(rawEccPrivateKeys[i]);
      var recipientPublicKey :- expect Base64.Decode(rawEccPublicKeysB64der[i]);
      var curve := CURVES[i];

      var senderKmsEcdhKeyring :- expect mpl.CreateAwsKmsEcdhKeyring(
        Types.CreateAwsKmsEcdhKeyringInput(
          KeyAgreementScheme := Types.KmsEcdhStaticConfigurations.KmsPrivateKeyToStaticPublicKey(
            Types.KmsPrivateKeyToStaticPublicKeyInput(
              senderKmsIdentifier := senderKmsKey,
              senderPublicKey := Some(senderPublicKey),
              recipientPublicKey := recipientPublicKey
            )
          ),
          curveSpec := curve,
          kmsClient := kmsClient,
          grantTokens := None()
        )
      );

      var recipientRawKeyring :- expect mpl.CreateRawEcdhKeyring(
        Types.CreateRawEcdhKeyringInput(
          KeyAgreementScheme := Types.RawPrivateKeyToStaticPublicKey(
            Types.RawPrivateKeyToStaticPublicKeyInput(
              senderStaticPrivateKey := recipientPrivateKey,
              recipientPublicKey := senderPublicKey
            )
          ),
          curveSpec := curve
        )
      );

      var encryptionContext := TestUtils.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation.A);

      var algorithmSuiteId := Types.AlgorithmSuiteId.ESDK(Types.ALG_AES_256_GCM_IV12_TAG16_NO_KDF);
      var suite := AlgorithmSuites.GetSuite(algorithmSuiteId);
      var encryptionMaterialsIn :- expect mpl.InitializeEncryptionMaterials(
        Types.InitializeEncryptionMaterialsInput(
          algorithmSuiteId := algorithmSuiteId,
          encryptionContext := encryptionContext,
          requiredEncryptionContextKeys := [],
          signingKey := None,
          verificationKey := None
        )
      );

      var encryptionMaterialsOut :- expect senderKmsEcdhKeyring.OnEncrypt(
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
      var decryptionMaterialsOut :- expect recipientRawKeyring.OnDecrypt(
        Types.OnDecryptInput(
          materials:=decryptionMaterialsIn,
          encryptedDataKeys:=[edk]
        )
      );

      expect encryptionMaterialsOut.materials.plaintextDataKey
          == decryptionMaterialsOut.materials.plaintextDataKey;

    }

  }

  method {:test} TestKmsEcdhKeyringWithIncorrectCurveConfigurationFailure()
  {
    var mpl :- expect MaterialProviders.MaterialProviders();

    var kmsClient :- expect Kms.KMSClient();

    var senderPublicKey :- expect Base64.Decode(TestUtils.KMS_ECC_256_PUBLIC_KEY_S);
    var recipientPublicKey :- expect Base64.Decode(TestUtils.KMS_ECC_256_PUBLIC_KEY_R);

    var senderKmsEcdhKeyring := mpl.CreateAwsKmsEcdhKeyring(
      Types.CreateAwsKmsEcdhKeyringInput(
        KeyAgreementScheme := Types.KmsEcdhStaticConfigurations.KmsPrivateKeyToStaticPublicKey(
          Types.KmsPrivateKeyToStaticPublicKeyInput(
            senderKmsIdentifier := TestUtils.KMS_ECC_256_KEY_ARN_S,
            senderPublicKey := Some(senderPublicKey),
            recipientPublicKey := recipientPublicKey
          )
        ),
        curveSpec := P384,
        kmsClient := kmsClient,
        grantTokens := None()
      )
    );

    expect senderKmsEcdhKeyring.Failure?;
  }

  method {:test} TestKmsEcdhKeyringWithIncorrectCurveConfigurationCombinationsFailure()
  {
    var mpl :- expect MaterialProviders.MaterialProviders();

    var kmsClient :- expect Kms.KMSClient();

    var senderKmsKey256       := TestUtils.KMS_ECC_256_KEY_ARN_S;
    var senderPublicKey256    :- expect Base64.Decode(TestUtils.KMS_ECC_256_PUBLIC_KEY_S);
    var recipientPublicKey256 :- expect Base64.Decode(TestUtils.ECC_P256_PUBLIC_R);

    var senderKmsKey384       := TestUtils.KMS_ECC_384_KEY_ARN_S;
    var senderPublicKey384    :- expect Base64.Decode(TestUtils.KMS_ECC_384_PUBLIC_KEY_S);
    var recipientPublicKey384 :- expect Base64.Decode(TestUtils.ECC_P384_PUBLIC_R);

    var senderKmsKey521       := TestUtils.KMS_ECC_521_KEY_ARN_S;
    var senderPublicKey521    :- expect Base64.Decode(TestUtils.KMS_ECC_521_PUBLIC_KEY_S);
    var recipientPublicKey521 :- expect Base64.Decode(TestUtils.ECC_P521_PUBLIC_R);

    // 1. Test that if keys are the same but if curvespec is diff construction MUST fail.
/// P256 tests
    var senderKmsEcdhKeyring := mpl.CreateAwsKmsEcdhKeyring(
      Types.CreateAwsKmsEcdhKeyringInput(
        KeyAgreementScheme := Types.KmsEcdhStaticConfigurations.KmsPrivateKeyToStaticPublicKey(
          Types.KmsPrivateKeyToStaticPublicKeyInput(
            senderKmsIdentifier := senderKmsKey256,
            senderPublicKey := Some(senderPublicKey256),
            recipientPublicKey := recipientPublicKey256
          )
        ),
        curveSpec := P384,
        kmsClient := kmsClient,
        grantTokens := None()
      )
    );
    expect senderKmsEcdhKeyring.Failure?;

    senderKmsEcdhKeyring := mpl.CreateAwsKmsEcdhKeyring(
      Types.CreateAwsKmsEcdhKeyringInput(
        KeyAgreementScheme := Types.KmsEcdhStaticConfigurations.KmsPrivateKeyToStaticPublicKey(
          Types.KmsPrivateKeyToStaticPublicKeyInput(
            senderKmsIdentifier := senderKmsKey256,
            senderPublicKey := Some(senderPublicKey256),
            recipientPublicKey := recipientPublicKey256
          )
        ),
        curveSpec := P521,
        kmsClient := kmsClient,
        grantTokens := None()
      )
    );

    //P384 Tests
    senderKmsEcdhKeyring := mpl.CreateAwsKmsEcdhKeyring(
      Types.CreateAwsKmsEcdhKeyringInput(
        KeyAgreementScheme := Types.KmsEcdhStaticConfigurations.KmsPrivateKeyToStaticPublicKey(
          Types.KmsPrivateKeyToStaticPublicKeyInput(
            senderKmsIdentifier := senderKmsKey384,
            senderPublicKey := Some(senderPublicKey384),
            recipientPublicKey := recipientPublicKey384
          )
        ),
        curveSpec := P256,
        kmsClient := kmsClient,
        grantTokens := None()
      )
    );
    expect senderKmsEcdhKeyring.Failure?;

    senderKmsEcdhKeyring := mpl.CreateAwsKmsEcdhKeyring(
      Types.CreateAwsKmsEcdhKeyringInput(
        KeyAgreementScheme := Types.KmsEcdhStaticConfigurations.KmsPrivateKeyToStaticPublicKey(
          Types.KmsPrivateKeyToStaticPublicKeyInput(
            senderKmsIdentifier := senderKmsKey384,
            senderPublicKey := Some(senderPublicKey384),
            recipientPublicKey := recipientPublicKey384
          )
        ),
        curveSpec := P521,
        kmsClient := kmsClient,
        grantTokens := None()
      )
    );

    //P521
    senderKmsEcdhKeyring := mpl.CreateAwsKmsEcdhKeyring(
      Types.CreateAwsKmsEcdhKeyringInput(
        KeyAgreementScheme := Types.KmsEcdhStaticConfigurations.KmsPrivateKeyToStaticPublicKey(
          Types.KmsPrivateKeyToStaticPublicKeyInput(
            senderKmsIdentifier := senderKmsKey521,
            senderPublicKey := Some(senderPublicKey521),
            recipientPublicKey := recipientPublicKey521
          )
        ),
        curveSpec := P256,
        kmsClient := kmsClient,
        grantTokens := None()
      )
    );
    expect senderKmsEcdhKeyring.Failure?;

    senderKmsEcdhKeyring := mpl.CreateAwsKmsEcdhKeyring(
      Types.CreateAwsKmsEcdhKeyringInput(
        KeyAgreementScheme := Types.KmsEcdhStaticConfigurations.KmsPrivateKeyToStaticPublicKey(
          Types.KmsPrivateKeyToStaticPublicKeyInput(
            senderKmsIdentifier := senderKmsKey521,
            senderPublicKey := Some(senderPublicKey521),
            recipientPublicKey := recipientPublicKey521
          )
        ),
        curveSpec := P384,
        kmsClient := kmsClient,
        grantTokens := None()
      )
    );

    // 2. Test that if sender and curve spec are the same but public key diff, construction MUST fail
    //P256
    senderKmsEcdhKeyring := mpl.CreateAwsKmsEcdhKeyring(
      Types.CreateAwsKmsEcdhKeyringInput(
        KeyAgreementScheme := Types.KmsEcdhStaticConfigurations.KmsPrivateKeyToStaticPublicKey(
          Types.KmsPrivateKeyToStaticPublicKeyInput(
            senderKmsIdentifier := senderKmsKey256,
            senderPublicKey := Some(senderPublicKey256),
            recipientPublicKey := recipientPublicKey384
          )
        ),
        curveSpec := P256,
        kmsClient := kmsClient,
        grantTokens := None()
      )
    );
    expect senderKmsEcdhKeyring.Failure?;

    senderKmsEcdhKeyring := mpl.CreateAwsKmsEcdhKeyring(
      Types.CreateAwsKmsEcdhKeyringInput(
        KeyAgreementScheme := Types.KmsEcdhStaticConfigurations.KmsPrivateKeyToStaticPublicKey(
          Types.KmsPrivateKeyToStaticPublicKeyInput(
            senderKmsIdentifier := senderKmsKey256,
            senderPublicKey := Some(senderPublicKey256),
            recipientPublicKey := recipientPublicKey521
          )
        ),
        curveSpec := P256,
        kmsClient := kmsClient,
        grantTokens := None()
      )
    );
    expect senderKmsEcdhKeyring.Failure?;

    //P384
    senderKmsEcdhKeyring := mpl.CreateAwsKmsEcdhKeyring(
      Types.CreateAwsKmsEcdhKeyringInput(
        KeyAgreementScheme := Types.KmsEcdhStaticConfigurations.KmsPrivateKeyToStaticPublicKey(
          Types.KmsPrivateKeyToStaticPublicKeyInput(
            senderKmsIdentifier := senderKmsKey384,
            senderPublicKey := Some(senderPublicKey384),
            recipientPublicKey := recipientPublicKey256
          )
        ),
        curveSpec := P384,
        kmsClient := kmsClient,
        grantTokens := None()
      )
    );
    expect senderKmsEcdhKeyring.Failure?;

    senderKmsEcdhKeyring := mpl.CreateAwsKmsEcdhKeyring(
      Types.CreateAwsKmsEcdhKeyringInput(
        KeyAgreementScheme := Types.KmsEcdhStaticConfigurations.KmsPrivateKeyToStaticPublicKey(
          Types.KmsPrivateKeyToStaticPublicKeyInput(
            senderKmsIdentifier := senderKmsKey384,
            senderPublicKey := Some(senderPublicKey384),
            recipientPublicKey := recipientPublicKey521
          )
        ),
        curveSpec := P384,
        kmsClient := kmsClient,
        grantTokens := None()
      )
    );
    expect senderKmsEcdhKeyring.Failure?;

    //P521
    senderKmsEcdhKeyring := mpl.CreateAwsKmsEcdhKeyring(
      Types.CreateAwsKmsEcdhKeyringInput(
        KeyAgreementScheme := Types.KmsEcdhStaticConfigurations.KmsPrivateKeyToStaticPublicKey(
          Types.KmsPrivateKeyToStaticPublicKeyInput(
            senderKmsIdentifier := senderKmsKey521,
            senderPublicKey := Some(senderPublicKey521),
            recipientPublicKey := recipientPublicKey256
          )
        ),
        curveSpec := P521,
        kmsClient := kmsClient,
        grantTokens := None()
      )
    );
    expect senderKmsEcdhKeyring.Failure?;

    senderKmsEcdhKeyring := mpl.CreateAwsKmsEcdhKeyring(
      Types.CreateAwsKmsEcdhKeyringInput(
        KeyAgreementScheme := Types.KmsEcdhStaticConfigurations.KmsPrivateKeyToStaticPublicKey(
          Types.KmsPrivateKeyToStaticPublicKeyInput(
            senderKmsIdentifier := senderKmsKey521,
            senderPublicKey := Some(senderPublicKey521),
            recipientPublicKey := recipientPublicKey384
          )
        ),
        curveSpec := P521,
        kmsClient := kmsClient,
        grantTokens := None()
      )
    );
    expect senderKmsEcdhKeyring.Failure?;

    // 3. Test that if recipient public key and curve spec are the same BUT if private
    // is on different curve, construction MUST fail
    //P256
    senderKmsEcdhKeyring := mpl.CreateAwsKmsEcdhKeyring(
      Types.CreateAwsKmsEcdhKeyringInput(
        KeyAgreementScheme := Types.KmsEcdhStaticConfigurations.KmsPrivateKeyToStaticPublicKey(
          Types.KmsPrivateKeyToStaticPublicKeyInput(
            senderKmsIdentifier := senderKmsKey384,
            senderPublicKey := Some(senderPublicKey384),
            recipientPublicKey := recipientPublicKey256
          )
        ),
        curveSpec := P256,
        kmsClient := kmsClient,
        grantTokens := None()
      )
    );
    expect senderKmsEcdhKeyring.Failure?;

    senderKmsEcdhKeyring := mpl.CreateAwsKmsEcdhKeyring(
      Types.CreateAwsKmsEcdhKeyringInput(
        KeyAgreementScheme := Types.KmsEcdhStaticConfigurations.KmsPrivateKeyToStaticPublicKey(
          Types.KmsPrivateKeyToStaticPublicKeyInput(
            senderKmsIdentifier := senderKmsKey521,
            senderPublicKey := Some(senderPublicKey521),
            recipientPublicKey := recipientPublicKey256
          )
        ),
        curveSpec := P256,
        kmsClient := kmsClient,
        grantTokens := None()
      )
    );
    expect senderKmsEcdhKeyring.Failure?;

    //P384
    senderKmsEcdhKeyring := mpl.CreateAwsKmsEcdhKeyring(
      Types.CreateAwsKmsEcdhKeyringInput(
        KeyAgreementScheme := Types.KmsEcdhStaticConfigurations.KmsPrivateKeyToStaticPublicKey(
          Types.KmsPrivateKeyToStaticPublicKeyInput(
            senderKmsIdentifier := senderKmsKey256,
            senderPublicKey := Some(senderPublicKey256),
            recipientPublicKey := recipientPublicKey384
          )
        ),
        curveSpec := P384,
        kmsClient := kmsClient,
        grantTokens := None()
      )
    );
    expect senderKmsEcdhKeyring.Failure?;

    senderKmsEcdhKeyring := mpl.CreateAwsKmsEcdhKeyring(
      Types.CreateAwsKmsEcdhKeyringInput(
        KeyAgreementScheme := Types.KmsEcdhStaticConfigurations.KmsPrivateKeyToStaticPublicKey(
          Types.KmsPrivateKeyToStaticPublicKeyInput(
            senderKmsIdentifier := senderKmsKey521,
            senderPublicKey := Some(senderPublicKey521),
            recipientPublicKey := recipientPublicKey384
          )
        ),
        curveSpec := P384,
        kmsClient := kmsClient,
        grantTokens := None()
      )
    );
    expect senderKmsEcdhKeyring.Failure?;

    //P521
    senderKmsEcdhKeyring := mpl.CreateAwsKmsEcdhKeyring(
      Types.CreateAwsKmsEcdhKeyringInput(
        KeyAgreementScheme := Types.KmsEcdhStaticConfigurations.KmsPrivateKeyToStaticPublicKey(
          Types.KmsPrivateKeyToStaticPublicKeyInput(
            senderKmsIdentifier := senderKmsKey256,
            senderPublicKey := Some(senderPublicKey256),
            recipientPublicKey := recipientPublicKey521
          )
        ),
        curveSpec := P521,
        kmsClient := kmsClient,
        grantTokens := None()
      )
    );
    expect senderKmsEcdhKeyring.Failure?;

    senderKmsEcdhKeyring := mpl.CreateAwsKmsEcdhKeyring(
      Types.CreateAwsKmsEcdhKeyringInput(
        KeyAgreementScheme := Types.KmsEcdhStaticConfigurations.KmsPrivateKeyToStaticPublicKey(
          Types.KmsPrivateKeyToStaticPublicKeyInput(
            senderKmsIdentifier := senderKmsKey384,
            senderPublicKey := Some(senderPublicKey384),
            recipientPublicKey := recipientPublicKey521
          )
        ),
        curveSpec := P521,
        kmsClient := kmsClient,
        grantTokens := None()
      )
    );
    expect senderKmsEcdhKeyring.Failure?;
  }

  method {:test} TestLyingKmsKey()
  {
    var senderKmsKey256       := TestUtils.KMS_ECC_256_KEY_ARN_S;
    var senderPublicKey256    :- expect Base64.Decode(TestUtils.KMS_ECC_256_PUBLIC_KEY_S);
    var recipientPublicKey256 :- expect Base64.Decode(TestUtils.ECC_P256_PUBLIC_R);

    var senderKmsKey384       := TestUtils.KMS_ECC_384_KEY_ARN_S;
    var senderPublicKey384    :- expect Base64.Decode(TestUtils.KMS_ECC_384_PUBLIC_KEY_S);
    var recipientPublicKey384 :- expect Base64.Decode(TestUtils.ECC_P384_PUBLIC_R);

    var senderKmsKey521       := TestUtils.KMS_ECC_521_KEY_ARN_S;
    var senderPublicKey521    :- expect Base64.Decode(TestUtils.KMS_ECC_521_PUBLIC_KEY_S);
    var recipientPublicKey521 :- expect Base64.Decode(TestUtils.ECC_P521_PUBLIC_R);

    var mpl :- expect MaterialProviders.MaterialProviders();

    var kmsClient :- expect Kms.KMSClient();

    var encryptionContext := TestUtils.SmallEncryptionContext(TestUtils.SmallEncryptionContextVariation.A);

    var algorithmSuiteId := Types.AlgorithmSuiteId.ESDK(Types.ALG_AES_256_GCM_IV12_TAG16_NO_KDF);
    var suite := AlgorithmSuites.GetSuite(algorithmSuiteId);
    var encryptionMaterialsIn :- expect mpl.InitializeEncryptionMaterials(
      Types.InitializeEncryptionMaterialsInput(
        algorithmSuiteId := algorithmSuiteId,
        encryptionContext := encryptionContext,
        requiredEncryptionContextKeys := [],
        signingKey := None,
        verificationKey := None
      )
    );

    // In the AWS KMS ECDH Keyring, we only have control of the 3/4 keys
    // since the private sender key is in KMS.
    // If someone constructs a keyring in such a way that the kms key is different
    // than the rest of the keys, then construction should succeed but there
    // will be a failure on encrypt as KMS will not allow a key in a different curve than
    // the private key.

    //P256
    var kmsEcdhKeyring :- expect mpl.CreateAwsKmsEcdhKeyring(
      Types.CreateAwsKmsEcdhKeyringInput(
        KeyAgreementScheme := Types.KmsEcdhStaticConfigurations.KmsPrivateKeyToStaticPublicKey(
          Types.KmsPrivateKeyToStaticPublicKeyInput(
            senderKmsIdentifier := senderKmsKey384,
            senderPublicKey := Some(senderPublicKey256),
            recipientPublicKey := recipientPublicKey256
          )
        ),
        curveSpec := P256,
        kmsClient := kmsClient,
        grantTokens := None()
      )
    );
    var encryptionMaterialsOut := kmsEcdhKeyring.OnEncrypt(
      Types.OnEncryptInput(materials:=encryptionMaterialsIn)
    );
    expect encryptionMaterialsOut.Failure?;

    kmsEcdhKeyring :- expect mpl.CreateAwsKmsEcdhKeyring(
      Types.CreateAwsKmsEcdhKeyringInput(
        KeyAgreementScheme := Types.KmsEcdhStaticConfigurations.KmsPrivateKeyToStaticPublicKey(
          Types.KmsPrivateKeyToStaticPublicKeyInput(
            senderKmsIdentifier := senderKmsKey521,
            senderPublicKey := Some(senderPublicKey256),
            recipientPublicKey := recipientPublicKey256
          )
        ),
        curveSpec := P256,
        kmsClient := kmsClient,
        grantTokens := None()
      )
    );
    encryptionMaterialsOut := kmsEcdhKeyring.OnEncrypt(
      Types.OnEncryptInput(materials:=encryptionMaterialsIn)
    );
    expect encryptionMaterialsOut.Failure?;

    //P384
    kmsEcdhKeyring :- expect mpl.CreateAwsKmsEcdhKeyring(
      Types.CreateAwsKmsEcdhKeyringInput(
        KeyAgreementScheme := Types.KmsEcdhStaticConfigurations.KmsPrivateKeyToStaticPublicKey(
          Types.KmsPrivateKeyToStaticPublicKeyInput(
            senderKmsIdentifier := senderKmsKey256,
            senderPublicKey := Some(senderPublicKey384),
            recipientPublicKey := recipientPublicKey384
          )
        ),
        curveSpec := P384,
        kmsClient := kmsClient,
        grantTokens := None()
      )
    );
    encryptionMaterialsOut := kmsEcdhKeyring.OnEncrypt(
      Types.OnEncryptInput(materials:=encryptionMaterialsIn)
    );
    expect encryptionMaterialsOut.Failure?;

    kmsEcdhKeyring :- expect mpl.CreateAwsKmsEcdhKeyring(
      Types.CreateAwsKmsEcdhKeyringInput(
        KeyAgreementScheme := Types.KmsEcdhStaticConfigurations.KmsPrivateKeyToStaticPublicKey(
          Types.KmsPrivateKeyToStaticPublicKeyInput(
            senderKmsIdentifier := senderKmsKey521,
            senderPublicKey := Some(senderPublicKey384),
            recipientPublicKey := recipientPublicKey384
          )
        ),
        curveSpec := P384,
        kmsClient := kmsClient,
        grantTokens := None()
      )
    );
    encryptionMaterialsOut := kmsEcdhKeyring.OnEncrypt(
      Types.OnEncryptInput(materials:=encryptionMaterialsIn)
    );
    expect encryptionMaterialsOut.Failure?;

    //P521
    kmsEcdhKeyring :- expect mpl.CreateAwsKmsEcdhKeyring(
      Types.CreateAwsKmsEcdhKeyringInput(
        KeyAgreementScheme := Types.KmsEcdhStaticConfigurations.KmsPrivateKeyToStaticPublicKey(
          Types.KmsPrivateKeyToStaticPublicKeyInput(
            senderKmsIdentifier := senderKmsKey256,
            senderPublicKey := Some(senderPublicKey521),
            recipientPublicKey := recipientPublicKey521
          )
        ),
        curveSpec := P521,
        kmsClient := kmsClient,
        grantTokens := None()
      )
    );
    encryptionMaterialsOut := kmsEcdhKeyring.OnEncrypt(
      Types.OnEncryptInput(materials:=encryptionMaterialsIn)
    );
    expect encryptionMaterialsOut.Failure?;

    kmsEcdhKeyring :- expect mpl.CreateAwsKmsEcdhKeyring(
      Types.CreateAwsKmsEcdhKeyringInput(
        KeyAgreementScheme := Types.KmsEcdhStaticConfigurations.KmsPrivateKeyToStaticPublicKey(
          Types.KmsPrivateKeyToStaticPublicKeyInput(
            senderKmsIdentifier := senderKmsKey384,
            senderPublicKey := Some(senderPublicKey521),
            recipientPublicKey := recipientPublicKey521
          )
        ),
        curveSpec := P521,
        kmsClient := kmsClient,
        grantTokens := None()
      )
    );
    encryptionMaterialsOut := kmsEcdhKeyring.OnEncrypt(
      Types.OnEncryptInput(materials:=encryptionMaterialsIn)
    );
    expect encryptionMaterialsOut.Failure?;
  }
}
