// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/VarEncode64a.dfy"

module {:options "-functionSyntax:4"} VarEncode64aTest {
  import opened VarEncode64a
  import opened StandardLibrary.UInt

  method CheckValue(val : uint64)
  {
    var enc := Encode(val);
    var encLen := |enc| as MyLen;
    if Decode(enc, encLen) != val {
      print "Decode : ", val, " ", |enc|, " ", enc, "\n";
    }
    expect Decode(enc, encLen) == val;
    if !ValidEncoding(enc, encLen) {
      print "ValidEncoding : ", val, " ", |enc|, " ", enc, "\n";
    }
    expect ValidEncoding(enc, encLen);
    expect DecodeLength(enc) as int == |enc|;
    expect DecodeLength(enc) == EncodeLength(val);
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
      for i : int := -100 to 100 {
        var val := currPo2 + i;
        if (val < UINT64_LIMIT) {
          CheckValue(val as uint64);
          assert currPo2 >= 1024;
        }
      }
      currPo2 := currPo2 * 2;
    }
  }
}