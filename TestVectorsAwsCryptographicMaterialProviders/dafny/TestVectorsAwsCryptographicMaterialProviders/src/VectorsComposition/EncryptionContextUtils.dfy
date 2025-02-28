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

  // UTF8 use 16, 32, and 64 bit encodings. So, valid
  // UTF8 can be represented within 4 bytes.
  // We can separate these in 4 bins
  // ASCII characters can be represented in 1 byte
  // 2-byte UTF8 in 2 bytes
  // 3-byte UTF8 in 3 bytes
  // 4-byte UTF8 in 4 bytes
  // To make sure we are covering enough ground in our EC testing
  // we will select three random characters within each bin and 
  // treat those as the representative test cases. In addition
  // we will also select the lowest and highest values within those bins.
  // In total, each "bin" will have 5 representative test cases.
  
  const ascii1 : seq<uint8> := [0x31] // 1 as UTF8 
  const ascii2 : seq<uint8> := [0xc2, 0xa0] // Â as UTF8
  const ascii3 : seq<uint8> := [0x55] // U as UTF8
  const ascii4 : seq<uint8> := [0xc2, 0xb6] // ¶ as UTF8
  const ascii5 : seq<uint8> := [0xc3, 0xbf] // ÿ  as UTF8
  const asciiSet := {ascii1, ascii2, ascii3, ascii4, ascii5}
  const encryptionContextAsciiMap := 
    map[
      ascii1 := ascii1,
      ascii2 := ascii2,
      ascii3 := ascii3,
      ascii4 := ascii4,
      ascii5 := ascii5
    ]
  const encryptionContextAscii := {encryptionContextAsciiMap}

  const utf8_2_1: seq<uint8> := [0xc4, 0x80] // Ä as UTF8
  const utf8_2_2: seq<uint8> := [0xd4, 0x98] // Ԙ as UTF8
  const utf8_2_3: seq<uint8> := [0xd4, 0x88] // Ԉ as UTF8
  const utf8_2_4: seq<uint8> := [0xdf, 0x9f] // ߟ as UTF8
  const utf8_2_5: seq<uint8> := [0xdf, 0x9f] // ߟ as UTF8
  const utf8_2Set := {utf8_2_1, utf8_2_2, utf8_2_3, utf8_2_4, utf8_2_5} 
  const encryptionContextUTF82Map :=
    map[
      utf8_2_1 := utf8_2_1,
      utf8_2_2 := utf8_2_2,
      utf8_2_3 := utf8_2_3,
      utf8_2_4 := utf8_2_4,
      utf8_2_5 := utf8_2_5
    ]
  const encryptionContextUTF82 := {encryptionContextUTF82Map}

  const utf8_3_1: seq<uint8> := [0xe0, 0xa0, 0x80] // ࠀ as UTF8
  const utf8_3_2: seq<uint8> := [0xe0, 0xb7, 0xb4] // ෴ as UTF8
  const utf8_3_3: seq<uint8> := [0xe2, 0x88, 0xb0] // ∰ as UTF8
  const utf8_3_4: seq<uint8> := [0xef, 0xa3, 0xbf] //  as UTF8
  const utf8_3_5: seq<uint8> := [0xef, 0xbf, 0xbf] // ￿ as UTF8
  const utf8_3Set := {utf8_3_1, utf8_3_2, utf8_3_3, utf8_3_4, utf8_3_5}
  const encryptionContextUTF83Map :=
    map[
      utf8_3_1 := utf8_3_1,
      utf8_3_2 := utf8_3_2,
      utf8_3_3 := utf8_3_3,
      utf8_3_4 := utf8_3_4,
      utf8_3_5 := utf8_3_5
    ]
  const encryptionContextUTF83 := {encryptionContextUTF83Map}

  const utf8_4_1: seq<uint8> := [0xf0, 0x92, 0x80, 0x80] // 𒀀 as UTF8
  const utf8_4_2: seq<uint8> := [0xf0, 0x93, 0x80, 0xa3] // 𓀣  as UTF8
  const utf8_4_3: seq<uint8> := [0xf0, 0x93, 0x89, 0xa9] // 𓉩  as UTF8
  const utf8_4_4: seq<uint8> := [0xf0, 0x9d, 0x84, 0xa2] // 𝄢 as UTF8
  const utf8_4_5: seq<uint8> := [0xf0, 0x9f, 0xa7, 0xbf] // 🧿 as UTF8
  const utf8_4Set := {utf8_4_1, utf8_4_2, utf8_4_3, utf8_4_4, utf8_4_5}
  const encryptionContextUTF84Map :=
    map[
      utf8_4_1 := utf8_4_1,
      utf8_4_2 := utf8_4_2,
      utf8_4_3 := utf8_4_3,
      utf8_4_4 := utf8_4_4,
      utf8_4_5 := utf8_4_5
    ]
  const encryptionContextUTF84 := {encryptionContextUTF84Map}

  const variedUTF8EncryptionContext := 
   {}
   + encryptionContextAscii
   + encryptionContextUTF82
   + encryptionContextUTF83
   + encryptionContextUTF84

  const encryptionContextValues :=
  {}
    + asciiSet
    + utf8_2Set
    + utf8_3Set
    + utf8_4Set
}
