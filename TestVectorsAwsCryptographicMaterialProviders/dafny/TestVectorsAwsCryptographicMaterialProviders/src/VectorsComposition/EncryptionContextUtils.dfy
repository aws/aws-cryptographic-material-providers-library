// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "AllAlgorithmSuites.dfy"

module {:options "-functionSyntax:4"} EncryptionContextUtils {
  import opened UTF8
  import opened UInt = StandardLibrary.UInt
  
  const normal : seq<uint8> := [0x6e, 0x6f, 0x72, 0x6d, 0x61, 0x6c, 0xed, 0x80, 0x80] // "normal퀀" as utf8
  const psi : seq<uint8> := [0xf0, 0x90, 0x80, 0x82] // "𐀂" as utf8
  const a := UTF8.Encode("a").value

  const encryptionContextWithPsiMap := map[normal := normal, psi := psi]
  const encryptionContextWitPsi := {encryptionContextWithPsiMap}

  const encryptionContextControlMap := map[normal:= normal]
  const encryptionContextControl := {encryptionContextControlMap}
  
  const encryptionContextBasicMap := map[a := a]
  const encryptionContextBasic := {encryptionContextBasicMap}

  const encryptionContextEmptyMap: map<seq<uint8>, seq<uint8>> := map[]
  const encryptionContextEmpty := {encryptionContextEmptyMap}

}
