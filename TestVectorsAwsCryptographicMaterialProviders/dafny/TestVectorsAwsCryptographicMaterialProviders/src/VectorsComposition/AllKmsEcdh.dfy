// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "AllAlgorithmSuites.dfy"

module {:options "-functionSyntax:4"} AllKmsEcdh {
  import opened Wrappers
  import TestVectors
  import AllAlgorithmSuites
  import KeyVectorsTypes = AwsCryptographyMaterialProvidersTestVectorKeysTypes
  import AwsCryptographyPrimitivesTypes

  // These are all the PositiveKeydescription for the RawEcdhKeyring
  const kmsKeys := ["us-west-2-256-ecc", "us-west-2-384-ecc", "us-west-2-521-ecc"]

  const StaticKmsDescriptionsEncryptSender :=
    set
      key  <- kmsKeys
      ::
        KeyVectorsTypes.KmsECDH(KeyVectorsTypes.KmsEcdhKeyring(
                                  senderKeyId := key,
                                  senderPublicKey := "sender-material-public-key",
                                  recipientKeyId := key,
                                  recipientPublicKey := "recipient-material-public-key",
                                  curveSpec := key,
                                  keyAgreementScheme :=  "static"
                                ))
  const DiscoveryKeyDescriptionsDecrypt :=
    set
      key  <- kmsKeys
      ::
        KeyVectorsTypes.KmsECDH(KeyVectorsTypes.KmsEcdhKeyring(
                                  senderKeyId := "discovery",
                                  senderPublicKey := "discovery",
                                  recipientKeyId := key,
                                  recipientPublicKey := "recipient-material-public-key",
                                  curveSpec := key,
                                  keyAgreementScheme :=  "discovery"
                                ))

  const StaticKmsDescriptionsEncryptRecipient := StaticKmsDescriptionsEncryptSender

  const StaticKmsSenderRecipientTests :=
    set
      encryptKeyDescription <- StaticKmsDescriptionsEncryptSender,
      decryptKeyDescription <- StaticKmsDescriptionsEncryptRecipient | decryptKeyDescription.KmsECDH.curveSpec == encryptKeyDescription.KmsECDH.curveSpec,
      algorithmSuite <- AllAlgorithmSuites.AllAlgorithmSuites,
      commitmentPolicy | commitmentPolicy == AllAlgorithmSuites.GetCompatibleCommitmentPolicy(algorithmSuite)
      ::
        TestVectors.PositiveEncryptKeyringVector(
          name := "AWS KMS ECDH Static " + encryptKeyDescription.KmsECDH.senderKeyId + " " + decryptKeyDescription.KmsECDH.senderKeyId,
          encryptionContext := map[],
          commitmentPolicy := commitmentPolicy,
          algorithmSuite := algorithmSuite,
          encryptDescription := encryptKeyDescription,
          decryptDescription := decryptKeyDescription
        )

  const DiscoveryKmsTests :=
    set
      encryptKeyDescription <- StaticKmsDescriptionsEncryptSender,
      decryptKeyDescription <- DiscoveryKeyDescriptionsDecrypt | decryptKeyDescription.KmsECDH.curveSpec == encryptKeyDescription.KmsECDH.curveSpec,
      algorithmSuite <- AllAlgorithmSuites.AllAlgorithmSuites,
      commitmentPolicy | commitmentPolicy == AllAlgorithmSuites.GetCompatibleCommitmentPolicy(algorithmSuite)
      ::
        TestVectors.PositiveEncryptKeyringVector(
          name := "AWS KMS ECDH Discovery " + encryptKeyDescription.KmsECDH.senderKeyId + " " + decryptKeyDescription.KmsECDH.senderKeyId,
          encryptionContext := map[],
          commitmentPolicy := commitmentPolicy,
          algorithmSuite := algorithmSuite,
          encryptDescription := encryptKeyDescription,
          decryptDescription := decryptKeyDescription
        )

  const Tests := StaticKmsSenderRecipientTests + DiscoveryKmsTests
}