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
  import UTF8

  type PageIndex = UTF8.ValidUTF8Bytes
  type ExclusiveStartKey = Option<UTF8.ValidUTF8Bytes>

  // TODO: Investigate if allocating constant is more efficient than ASCII Encode.
  // UTF-8 encoded "Not Started"
  // https://cyberchef.infosec.amazon.dev/#recipe=Encode_text('UTF-8%20(65001)')To_Hex('0x%20with%20comma',0)&input=Tm90IFN0YXJ0ZWQ&oenc=65001&oeol=CR
  const NOT_STARTED_UTF8_BYTES: UTF8.ValidUTF8Bytes :=
    var s :=
      [0x4e,0x6f,0x74,0x20,0x53,0x74,0x61,0x72,0x74,0x65,0x64];
    assert UTF8.ValidUTF8Seq(s) by {
      assert UTF8.EncodeAscii("Not Started") == s;
    }
    s

  // UTF-8 encoded "Done"
  // https://cyberchef.infosec.amazon.dev/#recipe=Encode_text('UTF-8%20(65001)')To_Hex('0x%20with%20comma',0)&input=RG9uZQ&oenc=65001&oeol=CR
  const DONE_UTF8_BYTES: UTF8.ValidUTF8Bytes :=
    var s := [0x44,0x6f,0x6e,0x65];
    assert UTF8.ValidUTF8Seq(s) by {
      assert UTF8.EncodeAscii("Done") == s;
    }
    s

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
