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
  import Aws.Cryptography.Primitives
  import Com.Amazonaws.Kms
  import PrimitiveTypes = AwsCryptographyPrimitivesTypes
  import ComAmazonawsKmsTypes
  import UTF8

  // ECC Curve P256 Keys - only available in gamma stack
  const senderKmsKey := "arn:aws:kms:us-east-1:370957321024:key/ab0f5ab2-82a6-4bd3-aa5f-87336cbf38bd";
  const recipientKmsKey := "arn:aws:kms:us-east-1:370957321024:key/672ec393-86fb-4581-adc2-8cdb5b3d65ba";

  method {:test} TestKmsDeriveSharedSecretOfflineCalculation() {
    var kmsClient :- expect Kms.GammaKmsClient();
    var primitives :- expect Primitives.AtomicPrimitives();

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

}
