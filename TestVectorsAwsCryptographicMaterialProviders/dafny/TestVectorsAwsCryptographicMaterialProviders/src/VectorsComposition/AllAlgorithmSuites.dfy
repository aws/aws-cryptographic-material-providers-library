// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../TestVectors.dfy"

module {:options "-functionSyntax:4"} AllAlgorithmSuites {
  import Types = AwsCryptographyMaterialProvidersTypes
  import AlgorithmSuites
  import HexStrings

  function GetCompatibleCommitmentPolicy(algorithmSuite: Types.AlgorithmSuiteInfo)
    : (commitmentPolicy: Types.CommitmentPolicy)
  {
    match algorithmSuite.id
    case ESDK(_) =>
      if algorithmSuite.commitment.None? then
        Types.CommitmentPolicy.ESDK(Types.ESDKCommitmentPolicy.FORBID_ENCRYPT_ALLOW_DECRYPT)
      else
        Types.CommitmentPolicy.ESDK(Types.ESDKCommitmentPolicy.REQUIRE_ENCRYPT_REQUIRE_DECRYPT)
    case DBE(_) =>
      Types.CommitmentPolicy.DBE(Types.DBECommitmentPolicy.REQUIRE_ENCRYPT_REQUIRE_DECRYPT)
  }

// TODO: Add aes-192 after aws-lc-rs adds support
// To add AES192 tests, uncomment next line and remove the current value of ESDKAlgorithmSuites
//   const ESDKAlgorithmSuites := set id: Types.ESDKAlgorithmSuiteId :: AlgorithmSuites.GetESDKSuite(id)
  const ESDKAlgorithmSuites := set id: Types.ESDKAlgorithmSuiteId | 
    id != Types.ALG_AES_192_GCM_IV12_TAG16_NO_KDF &&
    id != Types.ALG_AES_192_GCM_IV12_TAG16_HKDF_SHA256 &&
    id != Types.ALG_AES_192_GCM_IV12_TAG16_HKDF_SHA384_ECDSA_P384 ::
    AlgorithmSuites.GetESDKSuite(id)
  const DBEAlgorithmSuites := set id: Types.DBEAlgorithmSuiteId :: AlgorithmSuites.GetDBESuite(id)

  const AllAlgorithmSuites := ESDKAlgorithmSuites + DBEAlgorithmSuites

// TODO: Add aes-192 after aws-lc-rs adds support
// To add AES192 tests, comment out AllAlgorithmSuitesIsCompleteExceptAES192
// and uncomment AllAlgorithmSuitesIsComplete
  lemma AllAlgorithmSuitesIsCompleteExceptAES192(id: Types.AlgorithmSuiteId)
  requires match id
    case ESDK(e) =>
      e != Types.ALG_AES_192_GCM_IV12_TAG16_NO_KDF &&
      e != Types.ALG_AES_192_GCM_IV12_TAG16_HKDF_SHA256 &&
      e != Types.ALG_AES_192_GCM_IV12_TAG16_HKDF_SHA384_ECDSA_P384
    case DBE(_) => true
  ensures AlgorithmSuites.GetSuite(id) in AllAlgorithmSuites
{}

  // lemma AllAlgorithmSuitesIsComplete(id: Types.AlgorithmSuiteId)
  //   ensures AlgorithmSuites.GetSuite(id) in AllAlgorithmSuites
  // {}

  function ToHex(algorithmSuite: Types.AlgorithmSuiteInfo)
    : string
  {
    HexStrings.ToHexString(algorithmSuite.binaryId)
  }

}
