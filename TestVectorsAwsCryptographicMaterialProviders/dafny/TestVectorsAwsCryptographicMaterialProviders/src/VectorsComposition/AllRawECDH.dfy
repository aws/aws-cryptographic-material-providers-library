// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "AllAlgorithmSuites.dfy"

module {:options "-functionSyntax:4"} AllRawECDH {
  import opened Wrappers
  import TestVectors
  import AllAlgorithmSuites
  import KeyVectorsTypes = AwsCryptographyMaterialProvidersTestVectorKeysTypes
  import AwsCryptographyPrimitivesTypes

  // These are all the PositiveKeydescription for the RawEcdhKeyring
  const ecdhCurveNames := ["ecc-256", "ecc-384", "ecc-521"]

  const EphemeralKeyDescriptionsEncrypt :=
    set
      key  <- ecdhCurveNames
      ::
        KeyVectorsTypes.ECDH(KeyVectorsTypes.RawEcdh(
                               senderKeyId := "ephemeral",
                               recipientKeyId := key + "-private",
                               providerId := "aws-raw-vectors-persistent-ephemeral " + key,
                               keyAgreementScheme := "ephemeral",
                               curveSpec := key
                             ))

  const DiscoveryKeyDescriptionsDecrypt :=
    set
      key  <- ecdhCurveNames
      ::
        KeyVectorsTypes.ECDH(KeyVectorsTypes.RawEcdh(
                               senderKeyId := "discovery",
                               recipientKeyId := key + "-private",
                               providerId := "aws-raw-vectors-persistent-discovery " + key,
                               keyAgreementScheme := "discovery",
                               curveSpec := key
                             ))

  const SenderKeyDescriptions :=
    set
      key  <- ecdhCurveNames
      ::
        KeyVectorsTypes.ECDH(KeyVectorsTypes.RawEcdh(
                               senderKeyId := key + "-private",
                               recipientKeyId := key + "-private",
                               providerId := "aws-raw-vectors-persistent-static " + key,
                               keyAgreementScheme := "static",
                               curveSpec := key
                             ))

  const RecipientKeyDescriptions :=
    set
      key  <- ecdhCurveNames
      ::
        KeyVectorsTypes.ECDH(KeyVectorsTypes.RawEcdh(
                               senderKeyId := key + "-private",
                               recipientKeyId := key + "-private",
                               providerId := "aws-raw-vectors-persistent-static " + key,
                               keyAgreementScheme := "static",
                               curveSpec := key
                             ))

  const EphemeralDiscoveryTests :=
    set
      encryptKeyDescription <- EphemeralKeyDescriptionsEncrypt,
      decryptKeyDescription <- DiscoveryKeyDescriptionsDecrypt | decryptKeyDescription.ECDH.curveSpec == encryptKeyDescription.ECDH.curveSpec,
      algorithmSuite <- AllAlgorithmSuites.AllAlgorithmSuites,
      commitmentPolicy | commitmentPolicy == AllAlgorithmSuites.GetCompatibleCommitmentPolicy(algorithmSuite)
      ::
        TestVectors.PositiveEncryptKeyringVector(
          name := "Generated RawECDH Ephemeral-Discovery " + encryptKeyDescription.ECDH.senderKeyId + " " + decryptKeyDescription.ECDH.recipientKeyId,
          encryptionContext := map[],
          commitmentPolicy := commitmentPolicy,
          algorithmSuite := algorithmSuite,
          encryptDescription := encryptKeyDescription,
          decryptDescription := decryptKeyDescription
        )

  const StaticSenderDiscoveryRecipientTests :=
    set
      encryptKeyDescription <- SenderKeyDescriptions,
      decryptKeyDescription <- DiscoveryKeyDescriptionsDecrypt | decryptKeyDescription.ECDH.curveSpec == encryptKeyDescription.ECDH.curveSpec,
      algorithmSuite <- AllAlgorithmSuites.AllAlgorithmSuites,
      commitmentPolicy | commitmentPolicy == AllAlgorithmSuites.GetCompatibleCommitmentPolicy(algorithmSuite)
      ::
        TestVectors.PositiveEncryptKeyringVector(
          name := "Generated RawECDH Static " + encryptKeyDescription.ECDH.senderKeyId + " Discovery " + decryptKeyDescription.ECDH.recipientKeyId,
          encryptionContext := map[],
          commitmentPolicy := commitmentPolicy,
          algorithmSuite := algorithmSuite,
          encryptDescription := encryptKeyDescription,
          decryptDescription := decryptKeyDescription
        )

  const StaticSenderRecipientTests :=
    set
      encryptKeyDescription <- SenderKeyDescriptions,
      decryptKeyDescription <- RecipientKeyDescriptions | decryptKeyDescription.ECDH.curveSpec == encryptKeyDescription.ECDH.curveSpec,
      algorithmSuite <- AllAlgorithmSuites.AllAlgorithmSuites,
      commitmentPolicy | commitmentPolicy == AllAlgorithmSuites.GetCompatibleCommitmentPolicy(algorithmSuite)
      ::
        TestVectors.PositiveEncryptKeyringVector(
          name := "Generated RawECDH Static " + encryptKeyDescription.ECDH.senderKeyId + " " + decryptKeyDescription.ECDH.senderKeyId,
          encryptionContext := map[],
          commitmentPolicy := commitmentPolicy,
          algorithmSuite := algorithmSuite,
          encryptDescription := encryptKeyDescription,
          decryptDescription := decryptKeyDescription
        )

  const Tests := EphemeralDiscoveryTests + StaticSenderRecipientTests + StaticSenderDiscoveryRecipientTests

}