// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/VarEncode64b.dfy"

module {:options "-functionSyntax:4"} VarEncode64bTest {
  import opened VarEncode64b
  import opened StandardLibrary.UInt

  method CheckValue(val : nat)
  {
    var enc := Encode(val);
    expect ValidSequence(enc);
    if Decode(enc) != val {
      print "Decode : ", val, " ", |enc|, " ", enc, "\n";
    }
    expect Decode(enc) == val;
    if FindLength(enc) != |enc| {
      print "Length ", val, " ", FindLength(enc), " ", |enc|, " ", enc, "\n";
    }
    expect FindLength(enc) == |enc|;
    // if !ValidEncoding(enc, encLen) {
    //   print "ValidEncoding : ", val, " ", |enc|, " ", enc, "\n";
    // }
    // expect ValidEncoding(enc, encLen);
    // expect DecodeLength(enc) as int == |enc|;
    // expect DecodeLength(enc) == EncodeLength(val);
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
        CheckValue(val);
        assert currPo2 >= 1024;
      }
      currPo2 := currPo2 * 2;
    }
  }
}
