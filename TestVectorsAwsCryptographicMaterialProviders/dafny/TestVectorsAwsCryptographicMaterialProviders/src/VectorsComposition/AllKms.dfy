// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "AllAlgorithmSuites.dfy"
include "EncryptionContextUtils.dfy"

module {:options "-functionSyntax:4"} AllKms {
  import opened Wrappers
  import AllAlgorithmSuites
  import EncryptionContextUtils
  import TestVectors
  import KeyVectorsTypes = AwsCryptographyMaterialProvidersTestVectorKeysTypes
  import opened UTF8
  import opened UInt = StandardLibrary.UInt

  const AllAwsKMSKeys := [ "us-west-2-decryptable", "us-west-2-mrk" ]
  const KeyDescriptions :=
    set
      key <- AllAwsKMSKeys
      ::
        KeyVectorsTypes.Kms(KeyVectorsTypes.KMSInfo( keyId := key ))

  const TestsNoEc :=
    set
      keyDescription <- KeyDescriptions,
      algorithmSuite <- AllAlgorithmSuites.AllAlgorithmSuites,
      commitmentPolicy | commitmentPolicy == AllAlgorithmSuites.GetCompatibleCommitmentPolicy(algorithmSuite)
      ::
        TestVectors.PositiveEncryptKeyringVector(
          name := "Generated KMS No Encryption Context" + keyDescription.Kms.keyId,
          encryptionContext := map[],
          commitmentPolicy := commitmentPolicy,
          algorithmSuite := algorithmSuite,
          encryptDescription := keyDescription,
          decryptDescription := keyDescription
        )
  
  const TestsWitPsiEc :=
    set 
      keyDescription <- KeyDescriptions,
      algorithmSuite <- AllAlgorithmSuites.AllAlgorithmSuites,
      commitmentPolicy | commitmentPolicy == AllAlgorithmSuites.GetCompatibleCommitmentPolicy(algorithmSuite),
      encryptionContext <- EncryptionContextUtils.encryptionContextWitPsi
      ::
        TestVectors.PositiveEncryptKeyringVector(
          name := "Generated KMS Encryption Context With Psi " + keyDescription.Kms.keyId,
          encryptionContext := encryptionContext,
          commitmentPolicy := commitmentPolicy,
          algorithmSuite := algorithmSuite,
          encryptDescription := keyDescription,
          decryptDescription := keyDescription
        )
  
  const TestControlEc := 
    set 
      keyDescription <- KeyDescriptions,
      algorithmSuite <- AllAlgorithmSuites.AllAlgorithmSuites,
      commitmentPolicy | commitmentPolicy == AllAlgorithmSuites.GetCompatibleCommitmentPolicy(algorithmSuite),
      encryptionContext <- EncryptionContextUtils.encryptionContextControl
      ::
        TestVectors.PositiveEncryptKeyringVector(
          name := "Generated KMS Control Encryption Context " + keyDescription.Kms.keyId,
          encryptionContext := encryptionContext,
          commitmentPolicy := commitmentPolicy,
          algorithmSuite := algorithmSuite,
          encryptDescription := keyDescription,
          decryptDescription := keyDescription
        )
  
  const TestsBasicEc := 
    set 
      keyDescription <- KeyDescriptions,
      algorithmSuite <- AllAlgorithmSuites.AllAlgorithmSuites,
      commitmentPolicy | commitmentPolicy == AllAlgorithmSuites.GetCompatibleCommitmentPolicy(algorithmSuite),
      encryptionContext <- EncryptionContextUtils.encryptionContextBasic
      ::
        TestVectors.PositiveEncryptKeyringVector(
          name := "Generated KMS Basic Encryption Context " + keyDescription.Kms.keyId,
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
