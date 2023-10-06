// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../JSONHelpers.dfy"
include "AllAlgorithmSuites.dfy"

module {:options "-functionSyntax:4"} KeyDescriptionJson {
  import opened JSON.Values
  import AllAlgorithmSuites
  import AllAlgorithmSuites.Types
  import opened Wrappers
  import SortedSets
  import Seq
  import StandardLibrary

  datatype KeyDescriptionJSON =
    | PositiveKeyDescriptionJSON(
        description: string,
        encrypt: JSON,
        decrypt: JSON
      )
    | NegativeDecryptKeyDescriptionJSON(
        description: string,
        decryptErrorDescription: string,
        encrypt: JSON,
        decrypt: JSON
      )
    | NegativeEncryptKeyDescriptionJSON(
        description: string,
        errorDescription: string,
        encrypt: JSON
      )

  function ToJson(
    nameonly keyDescription: KeyDescriptionJSON,
    nameonly algorithmSuite: Types.AlgorithmSuiteInfo,
    nameonly encryptionContext: map<string, string> := map[],
    nameonly requiredEncryptionContextKeys: set<string> := {},
    nameonly reproducedEncryptionContext: Option<map<string, string>> := None,
    nameonly maxPlaintextLength: Option<nat> := None
  )
    : JSON
    requires keyDescription.NegativeEncryptKeyDescriptionJSON? ==> reproducedEncryptionContext.None?
  {
    var id := AllAlgorithmSuites.ToHex(algorithmSuite);
    var reproducedEc
      := if reproducedEncryptionContext.Some? then
           [("reproducedEncryptionContext",
             EncryptionContextToJson(reproducedEncryptionContext.value))]
         else
           [];

    var maxPlaintextL
      := if maxPlaintextLength.Some? then
           [("maxPlaintextLength",
             Number(Int(maxPlaintextLength.value)))]
         else
           [];
    match keyDescription
    case PositiveKeyDescriptionJSON(description, encrypt, decrypt) =>
      Object([
               ("type", String("positive-keyring")),
               ("description", String(description + " " + id)),
               ("algorithmSuiteId", String(id)),
               ("encryptionContext", EncryptionContextToJson(encryptionContext)),
               ("requiredEncryptionContextKeys", EncryptionContextKeysToJson(requiredEncryptionContextKeys)),
               ("encryptKeyDescription", encrypt),
               ("decryptKeyDescription", decrypt)
             ] + reproducedEc + maxPlaintextL)
    case NegativeEncryptKeyDescriptionJSON(description, errorDescription, encrypt) =>
      Object([
               ("type", String("negative-encrypt-keyring")),
               ("description", String(description + " " + id)),
               ("errorDescription", String(errorDescription)),
               ("algorithmSuiteId", String(id)),
               ("encryptionContext", EncryptionContextToJson(encryptionContext)),
               ("requiredEncryptionContextKeys", EncryptionContextKeysToJson(requiredEncryptionContextKeys)),
               ("keyDescription", encrypt)
             ] + maxPlaintextL)
    case NegativeDecryptKeyDescriptionJSON(description, errorDescription, encrypt, decrypt) =>
      Object([
               ("type", String("negative-decrypt-keyring")),
               ("description", String(description + " " + id)),
               ("decryptErrorDescription", String(errorDescription)),
               ("algorithmSuiteId", String(id)),
               ("encryptionContext", EncryptionContextToJson(encryptionContext)),
               ("requiredEncryptionContextKeys", EncryptionContextKeysToJson(requiredEncryptionContextKeys)),
               ("encryptKeyDescription", encrypt),
               ("decryptKeyDescription", decrypt)
             ] + reproducedEc + maxPlaintextL)
  }

  function EncryptionContextKeysToJson(keys: set<string>)
    : JSON
  {
    var k := SortedSets.ComputeSetToSequence(keys);
    Array(seq(|k|, i requires 0 <= i < |k| => String(k[i])))
  }

  function EncryptionContextToJson(m: map<string, string>)
    : JSON
  {
    var keys := SortedSets.ComputeSetToSequence(m.Keys);
    var pairsBytes := Seq.Map(k requires k in m.Keys => (k, String(m[k])), keys);
    Object(pairsBytes)
  }

}
