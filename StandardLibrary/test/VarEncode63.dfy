// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/VarEncode63.dfy"

module {:options "-functionSyntax:4"} VarEncode63Test {
  import opened VarEncode63
  import opened StandardLibrary.UInt

  method CheckValue(val : uint64)
    requires val < Max9
  {
    var enc := Encode(val);
    var encLen := |enc| as MyLen;
    expect Decode(enc, encLen) == val;
    expect ValidEncoding(enc, encLen);
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
    for p := 10 to 64
      invariant currPo2 >= 1024
    {
      for i : int := -10 to 10 {
        var val := currPo2 + i;
        if (val < Max9 as int) {
          CheckValue(val as uint64);
          currPo2 := currPo2 * 2;
          assert currPo2 >= 1024;
        }
      }
    }
  }
}