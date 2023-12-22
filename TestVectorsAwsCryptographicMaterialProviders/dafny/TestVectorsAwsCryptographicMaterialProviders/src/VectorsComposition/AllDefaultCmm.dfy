// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "AllAlgorithmSuites.dfy"
include "AllRawAES.dfy"

module {:options "-functionSyntax:4"} AllDefaultCmm {
  import opened JSON.Values
  import opened Wrappers
  import AllAlgorithmSuites
  import AllRawAES
  import SortedSets
  import StandardLibrary

  import opened UTF8
  import TestVectors
  import KeyVectorsTypes = AwsCryptographyMaterialProvidersTestVectorKeysTypes
  import Types = AwsCryptographyMaterialProvidersTypes

  const StaticNotPlaintextDataKey
    := KeyVectorsTypes.Static(KeyVectorsTypes.StaticKeyring(
                                keyId := "no-plaintext-data-key"
                              ))

  const StaticPlaintextDataKey
    := KeyVectorsTypes.Static(KeyVectorsTypes.StaticKeyring(
                                keyId := "static-plaintext-data-key"
                              ))

  const StaticAlgorithmSuite := AllAlgorithmSuites.AlgorithmSuites.GetESDKSuite(
                                  AllAlgorithmSuites.Types.ALG_AES_128_GCM_IV12_TAG16_NO_KDF)

  const AesKey := AllRawAES.aesPersistentKeyNames[|AllRawAES.aesPersistentKeyNames| - 1]
  const RawAesKeyring
    := KeyVectorsTypes.AES(KeyVectorsTypes.RawAES(
                             keyId := AesKey,
                             providerId := "aws-raw-vectors-persistent-" + AesKey
                           ))

  const Tests
  := {}
  + {
    TestVectors.PositiveEncryptKeyringVector(
      name := "Simplest possible happy path",
      commitmentPolicy := AllAlgorithmSuites.GetCompatibleCommitmentPolicy(StaticAlgorithmSuite),
      algorithmSuite := StaticAlgorithmSuite,
      encryptDescription := StaticPlaintextDataKey,
      decryptDescription := StaticPlaintextDataKey,
      encryptionContext := map[]
    ),
    TestVectors.NegativeEncryptKeyringVector(
      name := "Missing plaintext data key on decrypt",
      errorDescription := "No plaintext data key on encrypt fails",
      commitmentPolicy := AllAlgorithmSuites.GetCompatibleCommitmentPolicy(StaticAlgorithmSuite),
      algorithmSuite := StaticAlgorithmSuite,
      keyDescription := StaticNotPlaintextDataKey,
      encryptionContext := map[]

    ),
    TestVectors.PositiveEncryptNegativeDecryptKeyringVector(
      name := "Missing plaintext data key on decrypt",
      decryptErrorDescription := "No plaintext data key on encrypt fails",
      commitmentPolicy := AllAlgorithmSuites.GetCompatibleCommitmentPolicy(StaticAlgorithmSuite),
      algorithmSuite := StaticAlgorithmSuite,
      encryptDescription := StaticPlaintextDataKey,
      decryptDescription := StaticNotPlaintextDataKey,
      encryptionContext := map[]
    )
  }

}
