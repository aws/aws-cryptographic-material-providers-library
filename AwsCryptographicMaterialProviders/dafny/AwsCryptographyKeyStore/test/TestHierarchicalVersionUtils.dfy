// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/HierarchicalVersionUtils.dfy"

module {:options "/functionSyntax:4" } TestHierarchicalVersionUtils {
  import HVUtils = HierarchicalVersionUtils
  import Structure = HVUtils.Structure

  const NEWLINE := "\n"
  const SPACE := " "
  const TAB := "\t"
  const SLASH_R := "\r"
  const BLANKISH: seq<string> := [NEWLINE, SPACE, TAB, SLASH_R]
  const BLANK := ""
  const JOHN := "john"
  const VALID_PREFIXED: seq<string> := [Structure.ENCRYPTION_CONTEXT_PREFIX + JOHN]

  const EMPTYISH_PREFIXED: seq<string> :=
    seq(|BLANKISH|-1, n requires 0 <= n <= |BLANKISH|-1 => Structure.ENCRYPTION_CONTEXT_PREFIX + BLANKISH[n])
    + [Structure.ENCRYPTION_CONTEXT_PREFIX + BLANK]

  const TERMINAL_EMPTYISH_PREFIXED: seq<string> :=
    seq(
    |BLANKISH|-1,
    n requires 0 <= n <= |BLANKISH|-1 => Structure.ENCRYPTION_CONTEXT_PREFIX + JOHN + BLANKISH[n])

  const START_EMPTYISH_PREFIX: seq<string> :=
    seq(
    |BLANKISH|-1,
    n requires 0 <= n <= |BLANKISH|-1 => Structure.ENCRYPTION_CONTEXT_PREFIX + BLANKISH[n] + JOHN)

  method {:test} /* {:verify false} */ TestRemovePrefix() {
    expect BLANK == HVUtils.RemovePrefix(Structure.ENCRYPTION_CONTEXT_PREFIX + BLANK);
    expect JOHN == HVUtils.RemovePrefix(Structure.ENCRYPTION_CONTEXT_PREFIX + JOHN);
    var i := 0;
    while i < |BLANKISH|-1 {
      expect HVUtils.HasPrefix(TERMINAL_EMPTYISH_PREFIXED[i]),
        "(EC Prefix + John + a blankish) should count as prefixed.";
      expect HVUtils.HasPrefix(START_EMPTYISH_PREFIX[i]),
        "(EC Prefix + a blankish + John) should count as prefixed.";
      expect JOHN + BLANKISH[i] == HVUtils.RemovePrefix(TERMINAL_EMPTYISH_PREFIXED[i]),
        "removing Prefix from (EC Prefix + John + a blankish) should return (john + a blankish).";
      expect BLANKISH[i] + JOHN == HVUtils.RemovePrefix(START_EMPTYISH_PREFIX[i]),
        "removing Prefix from (EC Prefix + a blankish + John) should return (a blankish + John).";
      i := i + 1;
    }
  }
}