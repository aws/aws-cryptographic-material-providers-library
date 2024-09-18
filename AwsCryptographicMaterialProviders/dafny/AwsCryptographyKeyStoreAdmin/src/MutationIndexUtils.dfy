// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../Model/AwsCryptographyKeyStoreAdminTypes.dfy"

// A PageIndex can be a Branch Key Verision, Not Started, or Done.
// Let's just represent Not Started as "Not Started", and Done as "Done".

// Storage, in QueryForVersions, treats it as either:
// - Set, and non-empty, MUST be branch:version:UUID
// - Not Set, MUST be Not Started
// - Set and empty, MUST Be Done

// The problem is that we cannot persit Opitional to DDB.
// Thus, we need to refactor the mapping.

// PageIndex is what we put IN TO DynamoDB as a MutationIndex.
// ExclusiveStartKey is what we work with.

module {:options "/functionSyntax:4" } MutationIndexUtils {
  import opened Wrappers
  import opened StandardLibrary.UInt
  import UTF8

  type PageIndex = seq<uint8>
  type ExclusiveStartKey = Option<seq<uint8>>

  const NOT_STARTED_UTF8_BYTES: seq<uint8> := [78,111,116,32,83,116,97,114,116,101,100]
  // https://cyberchef.infosec.amazon.dev/#recipe=Encode_text('UTF-8%20(65001)')To_Decimal('Comma',false)&input=Tm90IFN0YXJ0ZWQ&oenc=65001&oeol=CR
  const DONE_UTF8_BYTES: seq<uint8> := [68,111,110,101]
  // https://cyberchef.infosec.amazon.dev/#recipe=Encode_text('UTF-8%20(65001)')To_Decimal('Comma',false)&input=RG9uZQ&oenc=65001&oeol=CR

  function PageIndexToExclusiveStartKey(
    pageIndex: PageIndex
  ): (exclusiveStartKey: ExclusiveStartKey)
  {
    if pageIndex == NOT_STARTED_UTF8_BYTES then None
    else if pageIndex == DONE_UTF8_BYTES then Some([])
    else Some(pageIndex)
  }

  function ExclusiveStartKeyToPageIndex(
    exclusiveStartKey: ExclusiveStartKey
  ): (pageIndex: PageIndex)
  {
    if exclusiveStartKey.None? then NOT_STARTED_UTF8_BYTES
    else if exclusiveStartKey.value == [] then DONE_UTF8_BYTES
    else exclusiveStartKey.value
  }
}
