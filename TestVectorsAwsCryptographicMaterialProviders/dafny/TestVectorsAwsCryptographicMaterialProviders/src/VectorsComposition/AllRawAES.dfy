// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "AllAlgorithmSuites.dfy"
include "EncryptionContextUtils.dfy"

module {:options "-functionSyntax:4"} AllRawAES {
  import opened Wrappers
  import TestVectors
  import EncryptionContextUtils
  import AllAlgorithmSuites
  import KeyVectorsTypes = AwsCryptographyMaterialProvidersTestVectorKeysTypes
  import opened UTF8
  import opened UInt = StandardLibrary.UInt

  // These are all the PositiveKeyDescription for the RawAESKeyring

  // TODO: Add aes-192 after aws-lc-rs adds support
  // const aesPersistentKeyNames := [ "aes-128", "aes-192", "aes-256", "\ud835\udfc1-nonascii-\ud800\udc02-aes-256-\ud835\udfc1"]
  // UTF-8 (JSON) -> UTF-16 (Dafny source code) substitution:
  // 𝟁 -> "\ud835\udfc1"
  // 𐀂 -> "\ud800\udc02"
  const aesPersistentKeyNames := ["aes-128", "aes-256", "\uD835\uDfc1-nonascii-\uD800\uDC02-aes-256-\uD835\uDFC1-with-\uFFFD"]
  const KeyDescriptionsWithPsi :=
    set
      key <- aesPersistentKeyNames
      ::
        KeyVectorsTypes.AES(KeyVectorsTypes.RawAES(
                              keyId := key,
                              providerId := "aws-raw-vectors-persistent-" + key + "-\uD835\uDFC1"
                            ))
  const KeyDescriptions :=
    set
      key <- aesPersistentKeyNames
      ::
        KeyVectorsTypes.AES(KeyVectorsTypes.RawAES(
                              keyId := key,
                              providerId := "aws-raw-vectors-persistent-" + key
                            ))

  const TestsNoEc :=
    set
      keyDescription <- KeyDescriptions + KeyDescriptionsWithPsi,
      algorithmSuite <- AllAlgorithmSuites.AllAlgorithmSuites,
      commitmentPolicy | commitmentPolicy == AllAlgorithmSuites.GetCompatibleCommitmentPolicy(algorithmSuite)
      ::
        TestVectors.PositiveEncryptKeyringVector(
          name := "Generated RawAES No Encryption Context " + keyDescription.AES.keyId,
          encryptionContext := map[],
          commitmentPolicy := commitmentPolicy,
          algorithmSuite := algorithmSuite,
          encryptDescription := keyDescription,
          decryptDescription := keyDescription
        )

  const TestsWitPsiEc :=
    set
      keyDescription <- KeyDescriptions + KeyDescriptionsWithPsi,
      algorithmSuite <- AllAlgorithmSuites.AllAlgorithmSuites,
      commitmentPolicy | commitmentPolicy == AllAlgorithmSuites.GetCompatibleCommitmentPolicy(algorithmSuite),
      encryptionContext <- EncryptionContextUtils.encryptionContextWitPsi
      ::
        TestVectors.PositiveEncryptKeyringVector(
          name := "Generated RawAES Encryption Context With Psi " + keyDescription.AES.keyId,
          encryptionContext := encryptionContext,
          commitmentPolicy := commitmentPolicy,
          algorithmSuite := algorithmSuite,
          encryptDescription := keyDescription,
          decryptDescription := keyDescription
        )

  const TestsWitReplacementCharEc :=
    set
      keyDescription <- KeyDescriptions + KeyDescriptionsWithPsi,
      algorithmSuite <- AllAlgorithmSuites.AllAlgorithmSuites,
      commitmentPolicy | commitmentPolicy == AllAlgorithmSuites.GetCompatibleCommitmentPolicy(algorithmSuite),
      encryptionContext <- EncryptionContextUtils.encryptionContextWitReplacementChar
      ::
        TestVectors.PositiveEncryptKeyringVector(
          name := "Generated RawAES Encryption Context With Psi " + keyDescription.AES.keyId,
          encryptionContext := encryptionContext,
          commitmentPolicy := commitmentPolicy,
          algorithmSuite := algorithmSuite,
          encryptDescription := keyDescription,
          decryptDescription := keyDescription
        )

  const TestControlEc :=
    set
      keyDescription <- KeyDescriptions + KeyDescriptionsWithPsi,
      algorithmSuite <- AllAlgorithmSuites.AllAlgorithmSuites,
      commitmentPolicy | commitmentPolicy == AllAlgorithmSuites.GetCompatibleCommitmentPolicy(algorithmSuite),
      encryptionContext <- EncryptionContextUtils.encryptionContextControl
      ::
        TestVectors.PositiveEncryptKeyringVector(
          name := "Generated RawAES Control Encryption Context " + keyDescription.AES.keyId,
          encryptionContext := encryptionContext,
          commitmentPolicy := commitmentPolicy,
          algorithmSuite := algorithmSuite,
          encryptDescription := keyDescription,
          decryptDescription := keyDescription
        )

  const TestsBasicEc :=
    set
      keyDescription <- KeyDescriptions + KeyDescriptionsWithPsi,
      algorithmSuite <- AllAlgorithmSuites.AllAlgorithmSuites,
      commitmentPolicy | commitmentPolicy == AllAlgorithmSuites.GetCompatibleCommitmentPolicy(algorithmSuite),
      encryptionContext <- EncryptionContextUtils.encryptionContextBasic
      ::
        TestVectors.PositiveEncryptKeyringVector(
          name := "Generated RawAES Basic Encryption Context " + keyDescription.AES.keyId,
          encryptionContext := encryptionContext,
          commitmentPolicy := commitmentPolicy,
          algorithmSuite := algorithmSuite,
          encryptDescription := keyDescription,
          decryptDescription := keyDescription
        )

  const TestsWithDiffUTF8Ec :=
    set
      keyDescription <- KeyDescriptions + KeyDescriptionsWithPsi,
      algorithmSuite <- AllAlgorithmSuites.AllAlgorithmSuites,
      commitmentPolicy | commitmentPolicy == AllAlgorithmSuites.GetCompatibleCommitmentPolicy(algorithmSuite),
      encryptionContext <- EncryptionContextUtils.variedUTF8EncryptionContext
      ::
        TestVectors.PositiveEncryptKeyringVector(
          name := "Generated RawAES UTF8 Representative values " + keyDescription.AES.keyId,
          encryptionContext := encryptionContext,
          commitmentPolicy := commitmentPolicy,
          algorithmSuite := algorithmSuite,
          encryptDescription := keyDescription,
          decryptDescription := keyDescription
        )

  const TestsWithOnePairOfHighCodePointUtf8ValuesInEc :=
    set
      keyDescription <- KeyDescriptions + KeyDescriptionsWithPsi,
      algorithmSuite <- AllAlgorithmSuites.AllAlgorithmSuites,
      commitmentPolicy | commitmentPolicy == AllAlgorithmSuites.GetCompatibleCommitmentPolicy(algorithmSuite),
      key, value | key in EncryptionContextUtils.representativeEncryptionContextUtf8Values && value in EncryptionContextUtils.representativeEncryptionContextUtf8Values
      ::
        TestVectors.PositiveEncryptKeyringVector(
          name := "Generated RawAES Mix and Match UTF8 Key Values " + keyDescription.AES.keyId,
          encryptionContext := map[key := value],
          commitmentPolicy := commitmentPolicy,
          algorithmSuite := algorithmSuite,
          encryptDescription := keyDescription,
          decryptDescription := keyDescription
        )

  const TestsWithMultipleUTF8Ec :=
    set
      keyDescription <- KeyDescriptions + KeyDescriptionsWithPsi,
      algorithmSuite <- AllAlgorithmSuites.AllAlgorithmSuites,
      commitmentPolicy | commitmentPolicy == AllAlgorithmSuites.GetCompatibleCommitmentPolicy(algorithmSuite),
      encryptionContext <- EncryptionContextUtils.multipleEntriesUTF8EncryptionContext
      ::
        TestVectors.PositiveEncryptKeyringVector(
          name := "Generated RawAES Multiple UTF8 Entries EC " + keyDescription.AES.keyId,
          encryptionContext := encryptionContext,
          commitmentPolicy := commitmentPolicy,
          algorithmSuite := algorithmSuite,
          encryptDescription := keyDescription,
          decryptDescription := keyDescription
        )

  const Tests :=
    {}
    + TestsNoEc
    + TestsWitPsiEc
    + TestsBasicEc
    + TestControlEc
    + TestsWitReplacementCharEc
    + TestsWithMultipleUTF8Ec
}
