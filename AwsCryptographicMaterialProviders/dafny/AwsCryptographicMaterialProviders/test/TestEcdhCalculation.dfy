// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/Index.dfy"
include "../src/Keyrings/AwsKms/AwsKmsDiscoveryKeyring.dfy"
include "./TestUtils.dfy"
include "../../../../ComAmazonawsKms/src/Index.dfy"

module TestEcdhCalculation {
  import opened Wrappers
  import opened UInt = StandardLibrary.UInt
  import MaterialProviders
  import Types = AwsCryptographyMaterialProvidersTypes
  import AtomicPrimitives
  import Com.Amazonaws.Kms
  import TestUtils
  import PrimitiveTypes = AwsCryptographyPrimitivesTypes
  import ComAmazonawsKmsTypes
  import UTF8
  import Base64

  // ECC Curve P256 Keys
  const senderKmsKey    := "arn:aws:kms:us-west-2:370957321024:key/eabdf483-6be2-4d2d-8ee4-8c2583d416e9"
  const recipientKmsKey := "arn:aws:kms:us-west-2:370957321024:key/0265c8e9-5b6a-4055-8f70-63719e09fda5"
  const senderArns := [TestUtils.KMS_ECC_256_KEY_ARN_S, TestUtils.KMS_ECC_384_KEY_ARN_S, TestUtils.KMS_ECC_521_KEY_ARN_S]
  const senderArnPublicKeys := [TestUtils.KMS_ECC_256_PUBLIC_KEY_S, TestUtils.KMS_ECC_384_PUBLIC_KEY_S, TestUtils.KMS_ECC_521_PUBLIC_KEY_S]
  const privateKeyReceivers := [TestUtils.ECC_P256_PRIVATE, TestUtils.ECC_P384_PRIVATE, TestUtils.ECC_P521_PRIVATE]
  const publicKeyReceivers := [TestUtils.ECC_P256_PUBLIC, TestUtils.ECC_P384_PUBLIC, TestUtils.ECC_P521_PUBLIC]
  const curveSpecs := [PrimitiveTypes.ECC_NIST_P256, PrimitiveTypes.ECC_NIST_P384, PrimitiveTypes.ECC_NIST_P521]

  method {:test} TestKmsDeriveSharedSecretOfflineCalculation() {
    var kmsClient :- expect Kms.KMSClient();
    var primitives :- expect AtomicPrimitives.AtomicPrimitives();

    var keyPair :- expect primitives.GenerateECCKeyPair(
      PrimitiveTypes.GenerateECCKeyPairInput(
        eccCurve := PrimitiveTypes.ECDHCurveSpec.ECC_NIST_P256
      )
    );

    expect 1 <= |keyPair.publicKey.der| <= 8192;

    var kmsSharedSecret := kmsClient.DeriveSharedSecret(
      input := Kms.Types.DeriveSharedSecretRequest(
        KeyId := senderKmsKey,
        KeyAgreementAlgorithm := Kms.Types.KeyAgreementAlgorithmSpec.ECDH,
        PublicKey := keyPair.publicKey.der
      )
    );
    expect kmsSharedSecret.Success?;
    expect kmsSharedSecret.value.SharedSecret.Some?;

    var publicKeyResponse := kmsClient.GetPublicKey(
      Kms.Types.GetPublicKeyRequest(
        KeyId := senderKmsKey,
        GrantTokens := None
      )
    );
    expect(publicKeyResponse.Success?);

    var GetPublicKeyResponse(_,PublicKey,_,_,_,_,_,_) := publicKeyResponse.value;
    expect PublicKey.Some?;

    var offlineSharedSecret :- expect primitives.DeriveSharedSecret(
      PrimitiveTypes.DeriveSharedSecretInput(
        eccCurve := PrimitiveTypes.ECDHCurveSpec.ECC_NIST_P256,
        privateKey := keyPair.privateKey,
        publicKey := PrimitiveTypes.ECCPublicKey(der := PublicKey.value)
      )
    );

    expect kmsSharedSecret.value.SharedSecret.value == offlineSharedSecret.sharedSecret;

  }

  method {:test} TestKmsDeriveSharedSecretOfflineCalculationCurves() {
    var kmsClient :- expect Kms.KMSClient();
    var primitives :- expect AtomicPrimitives.AtomicPrimitives();

    for i := 0 to |senderArns|
    {
      var keyPair :- expect primitives.GenerateECCKeyPair(
        PrimitiveTypes.GenerateECCKeyPairInput(
          eccCurve := curveSpecs[i]
        )
      );
      expect 1 <= |keyPair.publicKey.der| <= 8192;

      var kmsSharedSecret := kmsClient.DeriveSharedSecret(
        input := Kms.Types.DeriveSharedSecretRequest(
          KeyId := senderArns[i],
          KeyAgreementAlgorithm := Kms.Types.KeyAgreementAlgorithmSpec.ECDH,
          PublicKey := keyPair.publicKey.der
        )
      );
      expect kmsSharedSecret.Success?;
      expect kmsSharedSecret.value.SharedSecret.Some?;

      var publicKeyResponse := kmsClient.GetPublicKey(
        Kms.Types.GetPublicKeyRequest(
          KeyId := senderArns[i],
          GrantTokens := None
        )
      );
      expect(publicKeyResponse.Success?);

      var GetPublicKeyResponse(_,PublicKey,_,_,_,_,_,_) := publicKeyResponse.value;
      expect PublicKey.Some?;

      var offlineSharedSecret :- expect primitives.DeriveSharedSecret(
        PrimitiveTypes.DeriveSharedSecretInput(
          eccCurve := curveSpecs[i],
          privateKey := keyPair.privateKey,
          publicKey := PrimitiveTypes.ECCPublicKey(der := PublicKey.value)
        )
      );

      expect kmsSharedSecret.value.SharedSecret.value == offlineSharedSecret.sharedSecret;

    }
  }

  method {:test} TestOfflineDeriveSharedSecretStaticKeys()
  {
    var kmsClient :- expect Kms.KMSClient();
    var primitives :- expect AtomicPrimitives.AtomicPrimitives();

    for i := 0 to |curveSpecs|
    {
      var curve := curveSpecs[i];
      var senderArn := senderArns[i];
      var senderPublicKey :- expect Base64.Decode(senderArnPublicKeys[i]);
      var recipientPrivateKey :- expect UTF8.Encode(privateKeyReceivers[i]);
      var recipientPublicKey :- expect Base64.Decode(publicKeyReceivers[i]);

      var kmsSharedSecret := kmsClient.DeriveSharedSecret(
        input := Kms.Types.DeriveSharedSecretRequest(
          KeyId := senderArn,
          KeyAgreementAlgorithm := Kms.Types.KeyAgreementAlgorithmSpec.ECDH,
          PublicKey := recipientPublicKey
        )
      );
      expect kmsSharedSecret.Success?;
      expect kmsSharedSecret.value.SharedSecret.Some?;

      var offlineSharedSecret :- expect primitives.DeriveSharedSecret(
        PrimitiveTypes.DeriveSharedSecretInput(
          eccCurve := curveSpecs[i],
          privateKey := PrimitiveTypes.ECCPrivateKey(pem := recipientPrivateKey),
          publicKey := PrimitiveTypes.ECCPublicKey(der := senderPublicKey)
        )
      );


      expect kmsSharedSecret.value.SharedSecret.value == offlineSharedSecret.sharedSecret;
    }
  }

}
