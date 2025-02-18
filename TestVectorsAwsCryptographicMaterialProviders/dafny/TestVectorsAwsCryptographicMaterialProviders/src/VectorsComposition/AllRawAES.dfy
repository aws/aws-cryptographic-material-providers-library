// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "AllAlgorithmSuites.dfy"

module {:options "-functionSyntax:4"} AllRawAES {
  import opened Wrappers
  import TestVectors
  import AllAlgorithmSuites
  import KeyVectorsTypes = AwsCryptographyMaterialProvidersTestVectorKeysTypes
  import opened UTF8
  import opened UInt = StandardLibrary.UInt

  // These are all the PositiveKeyDescription for the RawAESKeyring

  // TODO: Add aes-192 after aws-lc-rs adds support
  // const aesPersistentKeyNames := [ "aes-128", "aes-192", "aes-256"]
  const aesPersistentKeyNames := [ "aes-128", "aes-256"]
  const KeyDescriptions :=
    set
      key <- aesPersistentKeyNames
      ::
        KeyVectorsTypes.AES(KeyVectorsTypes.RawAES(
                              keyId := key,  
                              providerId := "aws-raw-vectors-persistent-" + key + "\uD835\uDFC1"
                            ))

  const normal : seq<uint8> := [0x6e, 0x6f, 0x72, 0x6d, 0x61, 0x6c, 0xed, 0x80, 0x80] // "normal퀀" as utf8
  const psi : seq<uint8> := [0xf0, 0x90, 0x80, 0x82] // "𐀂" as utf8

  const controlEncryptionContext := map[normal := normal]
  const encryptionContextPsi := map[psi := psi]
  const ecToTest := {controlEncryptionContext, encryptionContextPsi}

  const TestsNoEc :=
    set
      keyDescription <- KeyDescriptions,
      algorithmSuite <- AllAlgorithmSuites.AllAlgorithmSuites,
      commitmentPolicy | commitmentPolicy == AllAlgorithmSuites.GetCompatibleCommitmentPolicy(algorithmSuite)
      ::
        TestVectors.PositiveEncryptKeyringVector(
          name := "Generated RawAES " + keyDescription.AES.keyId,
          encryptionContext := map[],
          commitmentPolicy := commitmentPolicy,
          algorithmSuite := algorithmSuite,
          encryptDescription := keyDescription,
          decryptDescription := keyDescription
        )

  const TestsWithEc :=
    set
      keyDescription <- KeyDescriptions,
      algorithmSuite <- AllAlgorithmSuites.AllAlgorithmSuites,
      ec <- ecToTest,
      commitmentPolicy | commitmentPolicy == AllAlgorithmSuites.GetCompatibleCommitmentPolicy(algorithmSuite)
      ::
        TestVectors.PositiveEncryptKeyringVector(
          name := "Generated RawAES " + keyDescription.AES.keyId,
          commitmentPolicy := commitmentPolicy,
          algorithmSuite := algorithmSuite,
          encryptDescription := keyDescription,
          decryptDescription := keyDescription,
          encryptionContext := ec
        )
  
  const Tests := 
    {} 
    + TestsNoEc
    + TestsWithEc

}
