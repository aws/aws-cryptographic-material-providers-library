// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/VarEncode.dfy"
include "../src/Time.dfy"

module {:options "-functionSyntax:4"} VarEncodeTest {
  import opened VarEncode
  import opened StandardLibrary.UInt
  import opened Wrappers
  import Time

  method CheckValue(val : nat)
  {
    var enc := Encode(val);
    expect ValidSequence(enc);
    if Decode(enc) != val {
      print "Decode : ", val, " ", Decode(enc), " ", |enc|, " ", enc, "\n";
    }
    expect Decode(enc) == val;
    if FindLength(enc) != Success(|enc|) {
      print "Length ", val, " ", FindLength(enc), " ", |enc|, " ", enc, "\n";
    }
    expect FindLength(enc) == Success(|enc|);
    expect EncodeLength(val) == |enc|;
    expect ValidSequence(enc);
  }

  method {:test} TestEncodeSmallNumbers() {
    for i := 0 to 1000000 {
      CheckValue(i);
    }
  }

  method {:test} TestEncodePowersOfTwo() {
    var currPo2 : nat := 1024;
    for p := 10 to 80
      invariant currPo2 >= 1024
    {
      for i : int := -100 to 100 {
        var val := currPo2 + i;
        CheckValue(val);
      }
      currPo2 := currPo2 * 2;
    }
  }

  method CheckSeq(bytes : seq<uint8>)
    requires 0 < |bytes|
  {
    var result := FindLength(bytes);
    if result.Success? {
      var new_bytes := bytes[0..result.value];
      if bytes != new_bytes {
        expect !ValidSequence(bytes);
      }
      expect ValidSequence(new_bytes);
      var value := Decode(new_bytes);
      expect EncodeLength(value) == |new_bytes|;
      expect Encode(value) == new_bytes;
    } else {
      expect !ValidSequence(bytes);
    }
  }

  method {:test} TestDecode() {
    var start := Time.GetCurrentMilli();

    for i : nat := 0 to 256 {
      var bytes : seq<uint8> := [i as uint8];
      CheckSeq(bytes);
    }

    for i : nat := 0 to 256 {
      for j : nat := 0 to 256 {
        var bytes : seq<uint8> := [i as uint8, j as uint8];
        CheckSeq(bytes);
      }
    }

    for i : nat := 0 to 256 {
      for j : nat := 0 to 256 {
        for k : nat := 0 to 256 {
          var bytes : seq<uint8> := [i as uint8, j as uint8, k as uint8];
          CheckSeq(bytes);
        }
      }
    }
    var end := Time.GetCurrentMilli();
    print Time.FormatMilliDiff(start, end), " ";
  }

}
