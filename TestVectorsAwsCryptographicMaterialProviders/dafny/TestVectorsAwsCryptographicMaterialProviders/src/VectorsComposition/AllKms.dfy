// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "AllAlgorithmSuites.dfy"

module {:options "-functionSyntax:4"} AllKms {
  import opened Wrappers
  import AllAlgorithmSuites
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
  
  const normal : seq<uint8> := [0x6e, 0x6f, 0x72, 0x6d, 0x61, 0x6c, 0xed, 0x80, 0x80] // "normal퀀" as utf8
  const psi : seq<uint8> := [0xf0, 0x90, 0x80, 0x82] // "𐀂" as utf8
  const a := UTF8.Encode("a").value

  const encryptionContextWithPsiMap := map[normal := normal, psi := psi]
  const encryptionContextWitPsi := {encryptionContextWithPsiMap}

  // const encryptionContextWithSurrogateMap := map[]
  // const encryptionContextWithSurrogate :={encryptionContextWithSurrogateMap}

  const encryptionContextControlMap := map[normal:= normal]
  const encryptionContextControl := {encryptionContextControlMap}
  
  const encryptionContextBasicMap := map[a := a]
  const encryptionContextBasic := {encryptionContextBasicMap}

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
      encryptionContext <- encryptionContextWitPsi
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
      encryptionContext <- encryptionContextControl
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
      encryptionContext <- encryptionContextBasic
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
