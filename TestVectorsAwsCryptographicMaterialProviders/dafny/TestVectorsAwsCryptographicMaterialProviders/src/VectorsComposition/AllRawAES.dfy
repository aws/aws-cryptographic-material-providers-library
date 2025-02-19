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
  // const aesPersistentKeyNames := [ "aes-128", "aes-192", "aes-256"]
  const aesPersistentKeyNames := ["aes-128", "aes-256"]
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
  
  const Tests := 
  {}
    + TestsNoEc
    + TestsWitPsiEc
    + TestsBasicEc
    + TestControlEc
}
