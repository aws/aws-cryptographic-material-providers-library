// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "KeyDescriptionJson.dfy"
include "AllRawAES.dfy"

module {:options "-functionSyntax:4"} AllDefaultCmm {
  import opened JSON.Values
  import opened KeyDescriptionJson
  import opened Wrappers
  import AllAlgorithmSuites
  import AllRawAES
  import SortedSets
  import StandardLibrary

  const StaticNotPlaintextDataKey
    := Object([
                ("type", String("static-material-keyring")),
                ("key", String("no-plaintext-data-key"))
              ])
  const StaticPlaintextDataKey
    := Object([
                ("type", String("static-material-keyring")),
                ("key", String("static-plaintext-data-key"))
              ])
  const StaticAlgorithmSuite := AllAlgorithmSuites.AlgorithmSuites.GetESDKSuite(
                                  AllAlgorithmSuites.Types.ALG_AES_128_GCM_IV12_TAG16_NO_KDF)

  const AesKey := AllRawAES.aesPersistentKeyNames[|AllRawAES.aesPersistentKeyNames| - 1]
  const RawAesKeyring
    := Object([
                ("type", String("raw")),
                ("encryption-algorithm", String("aes")),
                ("provider-id", String("aws-raw-vectors-persistent-" + AesKey)),
                ("key", String(AesKey))
              ])

  function SubSets(ec: map<string, string>, keys: seq<string>)
    : set<map<string, string>>
    requires keys == SortedSets.ComputeSetToOrderedSequence2(ec.Keys, (a, b) => a < b)
  {
    if |ec| == 0 then
      {map[]}
    else
      var subsets := SubSets(ec - {keys[0]}, keys[1..]);
      subsets
      + (set
           s <- subsets
           ::
             s + map[keys[0] := ec[keys[0]]])
  }

  const SuccessTestingRequiredEncryptionContextKeysReproducedEncryptionContext :=
    set
      encryptionContext <- {map["a" := "a", "b" := "b"]},
      requiredEncryptionContextKeys
      <- set
           s <- SubSets(
                  encryptionContext,
                  SortedSets.ComputeSetToOrderedSequence2(encryptionContext.Keys, (a, b) => a < b))
           :: s.Keys,
      reproducedEncryptionContext
      <- set
           s <- SubSets(
                  encryptionContext,
                  SortedSets.ComputeSetToOrderedSequence2(encryptionContext.Keys, (a, b) => a < b))
           | s.Keys * requiredEncryptionContextKeys == requiredEncryptionContextKeys
           :: s
      ::
        ToJson(
          keyDescription := PositiveKeyDescriptionJSON(
            description := "Success testing requiredEncryptionContextKeys/reproducedEncryptionContext",
            encrypt := RawAesKeyring,
            decrypt := RawAesKeyring
          ),
          algorithmSuite := StaticAlgorithmSuite,
          encryptionContext := encryptionContext,
          requiredEncryptionContextKeys := requiredEncryptionContextKeys,
          reproducedEncryptionContext := Some(reproducedEncryptionContext)
        )

  const FailureBadReproducedEncryptionContext :=
    set
      encryptionContext <- {map["a" := "a", "b" := "b"]},
      requiredEncryptionContextKeys
      <- set
           s <- SubSets(
                  encryptionContext,
                  SortedSets.ComputeSetToOrderedSequence2(encryptionContext.Keys, (a, b) => a < b))
           :: s.Keys,
      incorrectEncryptionContext
      <- set
           s <- SubSets(
                  map["a" := "c", "b" := "c", "c" := "c"],
                  SortedSets.ComputeSetToOrderedSequence2(map["a" := "c", "b" := "c", "c" := "c"].Keys, (a, b) => a < b))
           | s != map[]
           :: s,
      reproducedEncryptionContext
      <- set
           s <- SubSets(
                  encryptionContext,
                  SortedSets.ComputeSetToOrderedSequence2(encryptionContext.Keys, (a, b) => a < b))
           :: s + incorrectEncryptionContext
      ::
        ToJson(
          keyDescription := NegativeDecryptKeyDescriptionJSON(
            description := "Failure of reproducedEncryptionContext",
            decryptErrorDescription := "The reproducedEncryptionContext is never correct",
            encrypt := RawAesKeyring,
            decrypt := RawAesKeyring
          ),
          algorithmSuite := StaticAlgorithmSuite,
          encryptionContext := encryptionContext,
          requiredEncryptionContextKeys := requiredEncryptionContextKeys,
          reproducedEncryptionContext := Some(reproducedEncryptionContext)
        )

  const Tests :=
    {
      ToJson(
        keyDescription := PositiveKeyDescriptionJSON(
          description := "Simplest possible happy path",
          encrypt := StaticPlaintextDataKey,
          decrypt := StaticPlaintextDataKey
        ),
        algorithmSuite := StaticAlgorithmSuite
      ),
      ToJson(
        keyDescription := NegativeEncryptKeyDescriptionJSON(
          description := "Missing plaintext data key on encrypt",
          errorDescription := "No plaintext data key on encrypt fails",
          encrypt := StaticNotPlaintextDataKey
        ),
        algorithmSuite := StaticAlgorithmSuite
      ),
      ToJson(
        keyDescription := NegativeDecryptKeyDescriptionJSON(
          description := "Missing plaintext data key on decrypt",
          decryptErrorDescription := "No plaintext data key on encrypt fails",
          encrypt := StaticPlaintextDataKey,
          decrypt := StaticNotPlaintextDataKey
        ),
        algorithmSuite := StaticAlgorithmSuite
      ),
      ToJson(
        keyDescription := NegativeEncryptKeyDescriptionJSON(
          description := "Missing plaintext data key on encrypt",
          errorDescription := "No plaintext data key on encrypt fails",
          encrypt := StaticPlaintextDataKey
        ),
        algorithmSuite := StaticAlgorithmSuite,
        encryptionContext := map["a" := "a", "b" := "b"],
        requiredEncryptionContextKeys := {"c"}
      )
    }
    + FailureBadReproducedEncryptionContext
    + SuccessTestingRequiredEncryptionContextKeysReproducedEncryptionContext

}
