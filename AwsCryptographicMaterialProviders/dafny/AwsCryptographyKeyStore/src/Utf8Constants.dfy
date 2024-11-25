// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../Model/AwsCryptographyKeyStoreTypes.dfy"
include "./Structure.dfy"

module {:options "/functionSyntax:4" } Utf8Constants {
  import UTF8
  import Structure

  const CREATE_TIME_UTF8_BYTES : UTF8.ValidUTF8Bytes :=
    var s := [0x63, 0x72, 0x65, 0x61, 0x74, 0x65, 0x2d, 0x74, 0x69, 0x6d, 0x65];
    assert s == UTF8.EncodeAscii(Structure.KEY_CREATE_TIME);
    s

  const ORIGINAL_UTF8_BYTES : UTF8.ValidUTF8Bytes :=
    var s := [0x6f, 0x72, 0x69, 0x67, 0x69, 0x6e, 0x61, 0x6c];
    assert s == UTF8.EncodeAscii(Structure.M_ORIGINAL);
    s

  const TERMINAL_UTF8_BYTES : UTF8.ValidUTF8Bytes :=
    var s := [0x74, 0x65, 0x72, 0x6d, 0x69, 0x6e, 0x61, 0x6c];
    assert s == UTF8.EncodeAscii(Structure.M_TERMINAL);
    s

  const INPUT_UTF8_BYTES : UTF8.ValidUTF8Bytes :=
    var s := [0x69, 0x6e, 0x70, 0x75, 0x74];
    assert s == UTF8.EncodeAscii(Structure.M_INPUT);
    s

  const PAGE_INDEX_UTF8_BYTES : UTF8.ValidUTF8Bytes :=
    var s := [0x70, 0x61, 0x67, 0x65, 0x49, 0x6e, 0x64, 0x65, 0x78];
    assert s == UTF8.EncodeAscii(Structure.M_PAGE_INDEX);
    s

  const COMMITMENT_TYPE_UTF8_BYTES : UTF8.ValidUTF8Bytes :=
    var s := [0x62, 0x72, 0x61, 0x6e, 0x63, 0x68, 0x3a, 0x4d, 0x55, 0x54, 0x41, 0x54, 0x49, 0x4f, 0x4e, 0x5f, 0x43, 0x4f, 0x4d, 0x4d, 0x49, 0x54, 0x4d, 0x45, 0x4e, 0x54];
    assert s == UTF8.EncodeAscii(Structure.MUTATION_COMMITMENT_TYPE);
    s

  const INDEX_TYPE_UTF8_BYTES : UTF8.ValidUTF8Bytes :=
    var s := [0x62, 0x72, 0x61, 0x6e, 0x63, 0x68, 0x3a, 0x4d, 0x55, 0x54, 0x41, 0x54, 0x49, 0x4f, 0x4e, 0x5f, 0x49, 0x4e, 0x44, 0x45, 0x58];
    assert s == UTF8.EncodeAscii(Structure.MUTATION_INDEX_TYPE);
    s

  const TRUST_STORAGE_UTF8_BYTES : UTF8.ValidUTF8Bytes :=
    var s := [0x74, 0x72, 0x75, 0x73, 0x74, 0x53, 0x74, 0x6f, 0x72, 0x61, 0x67, 0x65];
    assert s == UTF8.EncodeAscii("trustStorage");
    s

  const HIERARCHY_VERSION_UTF8_BYTES : UTF8.ValidUTF8Bytes :=
    var s := [0x68, 0x69, 0x65, 0x72, 0x61, 0x72, 0x63, 0x68, 0x79, 0x2d, 0x76, 0x65, 0x72, 0x73, 0x69, 0x6f, 0x6e];
    assert s == UTF8.EncodeAscii(Structure.HIERARCHY_VERSION);
    s

  const HIERARCHY_VERSION_VALUE_UTF8_BYTES : UTF8.ValidUTF8Bytes :=
    var s := [0x31];
    assert s == UTF8.EncodeAscii(Structure.HIERARCHY_VERSION_VALUE);
    s
}