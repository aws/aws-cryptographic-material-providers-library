// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/VarEncode.dfy"

module {:options "-functionSyntax:4"} VarEncodeTest {
  import opened VarEncode
  import opened StandardLibrary.UInt

  method CheckValue(val : uint64)
  {
    var enc := Encode(val);
    expect Decode(enc) == val;
    expect ValidEncoding(enc);
    expect DecodeLength(enc[0]) as int == |enc|;
    expect DecodeLength(enc[0]) == EncodeLength(val);
  }

  method {:test} TestEncodeSmallNumbers() {
    for i := 0 to 1000000 {
      CheckValue(i);
    }
  }

  method {:test} TestEncodePowersOfTwo() {
    var currPo2 := 1024;
    for p := 10 to 63
      invariant currPo2 >= 1024
    {
      for i := -10 to 10 {
        var val := currPo2 + i;
        if (val < UINT64_LIMIT) {
          CheckValue(val as uint64);
          currPo2 := currPo2 * 2;
          assert currPo2 >= 1024;
        }
      }
    }
  }
}