// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../../Model/AwsCryptographyMaterialProvidersTypes.dfy"

module CacheConstants {
  import opened StandardLibrary.UInt
  import Seq

  // Constants defined for cache identifier formulae

  // Null Byte
  const NULL_BYTE : seq<uint8> := [0x00]

  // Resource Id
  const RESOURCE_ID_CACHING_CMM: seq<uint8> := [0x01]
  const RESOURCE_ID_HIERARCHICAL_KEYRING: seq<uint8> := [0x02]

  // Scope Id
  const SCOPE_ID_ENCRYPT: seq<uint8> := [0x01]
  const SCOPE_ID_DECRYPT: seq<uint8> := [0x02]
  const SCOPE_ID_SEARCHABLE_ENCRYPTION: seq<uint8> := [0x03]
}
