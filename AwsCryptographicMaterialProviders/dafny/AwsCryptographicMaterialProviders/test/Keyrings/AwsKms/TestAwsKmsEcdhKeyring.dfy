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
  import Aws.Cryptography.Primitives
  import PrimitiveTypes = AwsCryptographyPrimitivesTypes
  import Com.Amazonaws.Kms
  import AwsKmsRsaKeyring
  import TestUtils
  import ComAmazonawsKmsTypes
  import AwsCryptographyPrimitivesTypes
  import AlgorithmSuites
  import UTF8
  import ErrorMessages

  const P256 := PrimitiveTypes.ECDHCurveSpec.ECC_NIST_P256
  const TEST_DBE_ALG_SUITE_ID := Types.AlgorithmSuiteId.DBE(Types.ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY_SYMSIG_HMAC_SHA384)

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

    var kmsClient :- expect Kms.GammaKmsClient();

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

    var kmsClient :- expect Kms.GammaKmsClient();

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

      print "\nTest with sender: " + senderArns[i] + " and recipient: " + recipientArns[i] + "\n";
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

    var kmsClient :- expect Kms.GammaKmsClient();

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

      print "\nTest with sender: " + senderArns[i] + " and recipient: " + recipientArns[i] + "\n";
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

    var kmsClient :- expect Kms.GammaKmsClient();

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
      print "\nDiscovery Test for: " + recipientArns[i] + "\n";
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

  method {:test} TestKmsEcdhKeyringRecipientRawKeyEncryptDecryptSuccessSetSenderPublicKey() {
    var mpl :- expect MaterialProviders.MaterialProviders();
    var primitives :- expect Primitives.AtomicPrimitives();

    var recipientKeypair :- expect primitives.GenerateECCKeyPair(
      PrimitiveTypes.GenerateECCKeyPairInput(
        eccCurve := P256
      )
    );

    var kmsClient :- expect Kms.GammaKmsClient();
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

}