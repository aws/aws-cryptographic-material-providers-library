// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../../src/Index.dfy"
include "../TestUtils.dfy"
include "../../src/ErrorMessages.dfy"

module TestRawRSAKeying {
  import opened Wrappers
  import TestUtils
  import AtomicPrimitives
  import AwsCryptographyPrimitivesTypes
  import MaterialProviders
  import Types = AwsCryptographyMaterialProvidersTypes
  import ErrorMessages

  method {:test} TestOnEncryptOnDecryptSuppliedDataKey()
  {

    var mpl :- expect MaterialProviders.MaterialProviders();

    var namespace, name := TestUtils.NamespaceAndName(0);
    var keys := GenerateKeyPair(2048 as AwsCryptographyPrimitivesTypes.RSAModulusLengthBits);
    var rawRSAKeyring :- expect mpl.CreateRawRsaKeyring(Types.CreateRawRsaKeyringInput(
                                                          keyNamespace := namespace,
                                                          keyName := name,
                                                          paddingScheme := Types.PaddingScheme.OAEP_SHA1_MGF1,
                                                          publicKey := Option.Some(keys.publicKey.pem),
                                                          privateKey := Option.Some(keys.privateKey.pem)
                                                        ));

    var encryptionContext := TestUtils.SmallEncryptionContext(
      TestUtils.SmallEncryptionContextVariation.A
    );

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

    var encryptionMaterialsOut :- expect rawRSAKeyring.OnEncrypt(
      Types.OnEncryptInput(materials:=encryptionMaterialsIn)
    );
    var _ :- expect mpl.EncryptionMaterialsHasPlaintextDataKey(encryptionMaterialsOut.materials);

    var edk := encryptionMaterialsOut.materials.encryptedDataKeys[0];

    var decryptionMaterialsIn :- expect mpl.InitializeDecryptionMaterials(
      Types.InitializeDecryptionMaterialsInput(
        algorithmSuiteId := algorithmSuiteId,
        encryptionContext := encryptionContext,
        requiredEncryptionContextKeys := []
      )
    );

    var decryptionMaterialsOut :- expect rawRSAKeyring.OnDecrypt(
      Types.OnDecryptInput(
        materials:=decryptionMaterialsIn,
        encryptedDataKeys:=[edk]
      )
    );

    //= aws-encryption-sdk-specification/framework/raw-rsa-keyring.md#onencrypt
    //= type=test
    //# The keyring MUST attempt to encrypt the plaintext data key in the
    //# [encryption materials](structures.md#encryption-materials) using RSA.
    // We demonstrate this by showing OnEncrypt then OnDecrypt gets us the same pdk back.
    expect decryptionMaterialsOut.materials.plaintextDataKey
        == encryptionMaterialsOut.materials.plaintextDataKey;
  }

  method {:test} TestOnDecryptKeyNameMismatch()
  {
    var mpl :- expect MaterialProviders.MaterialProviders();

    var namespace, name := TestUtils.NamespaceAndName(0);
    var keys := GenerateKeyPair(2048 as AwsCryptographyPrimitivesTypes.RSAModulusLengthBits);
    var rawRSAKeyring :- expect mpl.CreateRawRsaKeyring(Types.CreateRawRsaKeyringInput(
                                                          keyNamespace := namespace,
                                                          keyName := name,
                                                          paddingScheme := Types.PaddingScheme.OAEP_SHA1_MGF1,
                                                          publicKey := Option.Some(keys.publicKey.pem),
                                                          privateKey := Option.Some(keys.privateKey.pem)
                                                        ));

    var mismatchedRSAKeyring :- expect mpl.CreateRawRsaKeyring(Types.CreateRawRsaKeyringInput(
                                                                 keyNamespace := namespace,
                                                                 keyName := "mismatched",
                                                                 paddingScheme := Types.PaddingScheme.OAEP_SHA1_MGF1,
                                                                 publicKey := Option.Some(keys.publicKey.pem),
                                                                 privateKey := Option.Some(keys.privateKey.pem)
                                                               ));

    var encryptionContext := TestUtils.SmallEncryptionContext(
      TestUtils.SmallEncryptionContextVariation.A
    );

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
    var encryptionMaterialsOut :- expect rawRSAKeyring.OnEncrypt(
      Types.OnEncryptInput(materials:=encryptionMaterialsIn)
    );
    var _ :- expect mpl.EncryptionMaterialsHasPlaintextDataKey(encryptionMaterialsOut.materials);

    var edk := encryptionMaterialsOut.materials.encryptedDataKeys[0];

    var decryptionMaterialsIn :- expect mpl.InitializeDecryptionMaterials(
      Types.InitializeDecryptionMaterialsInput(
        algorithmSuiteId := algorithmSuiteId,
        encryptionContext := encryptionContext,
        requiredEncryptionContextKeys := []
      )
    );
    var decryptionMaterialsOut := mismatchedRSAKeyring.OnDecrypt(
      Types.OnDecryptInput(
        materials:=decryptionMaterialsIn,
        encryptedDataKeys:=[edk]
      )
    );

    expect decryptionMaterialsOut.IsFailure();
    expect decryptionMaterialsOut.error.CollectionOfErrors?;
    expect |decryptionMaterialsOut.error.list| == 1;
    expect decryptionMaterialsOut.error.list[0].AwsCryptographicMaterialProvidersException?;
    expect decryptionMaterialsOut.error.list[0].message == ErrorMessages.IncorrectRawDataKeys("0", "RSAKeyring", namespace);
  }

  method {:test} TestOnDecryptFailure()
  {

    var mpl :- expect MaterialProviders.MaterialProviders();

    var namespace, name := TestUtils.NamespaceAndName(0);

    // The keys are different, so the decrypt will fail
    var encryptKeys := GenerateKeyPair(2048 as AwsCryptographyPrimitivesTypes.RSAModulusLengthBits);
    var decryptKeys := GenerateKeyPair(2048 as AwsCryptographyPrimitivesTypes.RSAModulusLengthBits);

    var encryptKeyring :- expect mpl.CreateRawRsaKeyring(Types.CreateRawRsaKeyringInput(
                                                           keyNamespace := namespace,
                                                           keyName := name,
                                                           paddingScheme := Types.PaddingScheme.OAEP_SHA1_MGF1,
                                                           publicKey := Option.Some(encryptKeys.publicKey.pem),
                                                           privateKey := Option.Some(encryptKeys.privateKey.pem)
                                                         ));

    var decryptKeyring :- expect mpl.CreateRawRsaKeyring(Types.CreateRawRsaKeyringInput(
                                                           keyNamespace := namespace,
                                                           keyName := name,
                                                           paddingScheme := Types.PaddingScheme.OAEP_SHA1_MGF1,
                                                           publicKey := Option.Some(decryptKeys.publicKey.pem),
                                                           privateKey := Option.Some(decryptKeys.privateKey.pem)
                                                         ));

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
    var encryptionMaterialsOut :- expect encryptKeyring.OnEncrypt(
      Types.OnEncryptInput(materials:=encryptionMaterialsIn)
    );
    var _ :- expect mpl.EncryptionMaterialsHasPlaintextDataKey(encryptionMaterialsOut.materials);

    var edk := encryptionMaterialsOut.materials.encryptedDataKeys[0];

    var decryptionMaterialsIn :- expect mpl.InitializeDecryptionMaterials(
      Types.InitializeDecryptionMaterialsInput(
        algorithmSuiteId := algorithmSuiteId,
        encryptionContext := encryptionContext,
        requiredEncryptionContextKeys := []
      )
    );
    var decryptionMaterialsOut := decryptKeyring.OnDecrypt(
      Types.OnDecryptInput(
        materials:=decryptionMaterialsIn,
        encryptedDataKeys:=[edk]
      )
    );

    //= aws-encryption-sdk-specification/framework/raw-rsa-keyring.md#ondecrypt
    //= type=test
    //# If no decryption succeeds, the keyring MUST fail and MUST NOT modify
    //# the [decryption materials](structures.md#decryption-materials).
    expect decryptionMaterialsOut.IsFailure();
  }

  // The RSA Keyring should attempt to decrypt every EDK that matches its keyname
  // and namespace, until it succeeds.
  // Here, we generate a valid EDK that the keyring should decrypt
  // and create a fake EDK that it will not be able to decrypt.
  // The keyring should fail to decrypt the fake one, and then
  // succeed with the real EDK, and return the PDK.
  method {:test} TestOnDecryptBadAndGoodEdkSucceeds()
  {

    var mpl :- expect MaterialProviders.MaterialProviders();

    var namespace, name := TestUtils.NamespaceAndName(0);
    var keys := GenerateKeyPair(2048 as AwsCryptographyPrimitivesTypes.RSAModulusLengthBits);
    var rawRSAKeyring :- expect mpl.CreateRawRsaKeyring(Types.CreateRawRsaKeyringInput(
                                                          keyNamespace := namespace,
                                                          keyName := name,
                                                          paddingScheme := Types.PaddingScheme.OAEP_SHA1_MGF1,
                                                          publicKey := Option.Some(keys.publicKey.pem),
                                                          privateKey := Option.Some(keys.privateKey.pem)
                                                        ));

    var encryptionContext := TestUtils.SmallEncryptionContext(
      TestUtils.SmallEncryptionContextVariation.A
    );

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
    var encryptionMaterialsOut :- expect rawRSAKeyring.OnEncrypt(
      Types.OnEncryptInput(materials:=encryptionMaterialsIn)
    );
    var _ :- expect mpl.EncryptionMaterialsHasPlaintextDataKey(encryptionMaterialsOut.materials);

    var edk := encryptionMaterialsOut.materials.encryptedDataKeys[0];

    var decryptionMaterialsIn :- expect mpl.InitializeDecryptionMaterials(
      Types.InitializeDecryptionMaterialsInput(
        algorithmSuiteId := algorithmSuiteId,
        encryptionContext := encryptionContext,
        requiredEncryptionContextKeys := []
      )
    );
    var fakeEdk := Types.EncryptedDataKey(
      keyProviderId := edk.keyProviderId,
      keyProviderInfo := edk.keyProviderInfo,
      ciphertext := seq(|edk.ciphertext|, i => 0)
    );

    //= aws-encryption-sdk-specification/framework/raw-rsa-keyring.md#ondecrypt
    //= type=test
    //# The keyring MUST attempt to decrypt the input encrypted data keys, in
    //# list order, until it successfully decrypts one.
    var decryptionMaterialsOut :- expect rawRSAKeyring.OnDecrypt(
      Types.OnDecryptInput(
        materials:=decryptionMaterialsIn,
        encryptedDataKeys:=[fakeEdk, edk]
      )
    );
    //= aws-encryption-sdk-specification/framework/raw-rsa-keyring.md#ondecrypt
    //= type=test
    //# If any decryption succeeds, this keyring MUST immediately return the
    //# input [decryption materials](structures.md#decryption-materials),
    //# modified in the following ways:
    expect decryptionMaterialsOut.materials.plaintextDataKey
        == encryptionMaterialsOut.materials.plaintextDataKey;
  }

  method GenerateKeyPair( keyModulusLength: AwsCryptographyPrimitivesTypes.RSAModulusLengthBitsToGenerate )
    returns (keys: AwsCryptographyPrimitivesTypes.GenerateRSAKeyPairOutput)
  {
    var crypto :- expect AtomicPrimitives.AtomicPrimitives();

    keys :- expect crypto.GenerateRSAKeyPair(
      AwsCryptographyPrimitivesTypes.GenerateRSAKeyPairInput(
        lengthBits := keyModulusLength
      )
    );
  }

}
