// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/VarEncode32.dfy"

module {:options "-functionSyntax:4"} VarEncode32Test {
  import opened VarEncode32
  import opened StandardLibrary.UInt

  method CheckValue(val : uint32)
  {
    var enc := Encode(val);
    var encLen := |enc| as MyLen;
    expect Decode(enc, encLen) == val;
    expect ValidEncoding(enc, encLen);
    expect DecodeLength(enc[0]) == encLen;
    expect DecodeLength(enc[0]) == EncodeLength(val);
  }

  method {:test} TestEncodeSmallNumbers() {
    for i := 0 to 1000000 {
      CheckValue(i);
    }
  }

  method {:test} TestEncodePowersOfTwo() {
    var currPo2 := 1024;
    for p := 10 to 32
      invariant currPo2 >= 1024
    {
      for i := -10 to 10 {
        var val := currPo2 + i;
        if (val < UINT32_LIMIT) {
          CheckValue(val as uint32);
          currPo2 := currPo2 * 2;
          assert currPo2 >= 1024;
        }
      }
    }
  }
}