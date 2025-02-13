// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/VarEncode64.dfy"
include "../src/Time.dfy"

module {:options "-functionSyntax:4"} VarEncode64Test {
  import opened VarEncode64
  import opened BoundedInts
  import opened Wrappers
  import Time

  method CheckValue(val : uint64)
  {
    var enc := Encode(val);
    if !ValidSequence(enc) {
      print "Invalid Sequence from : ", val, " ", |enc|, " ", enc, "\n";
    }
    expect ValidSequence(enc);
    if Decode(enc) != val {
      print "Decode : ", val, " ", Decode(enc), " ", |enc|, " ", enc, "\n";
    }
    expect Decode(enc) == val;
    if FindLength(enc) != Success(|enc| as uint64) {
      print "Length ", val, " ", FindLength(enc), " ", |enc|, " ", enc, "\n";
    }
    expect FindLength(enc) == Success(|enc| as uint64);
    expect EncodeLength(val) == |enc| as uint64;
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
        if val < TWO_TO_THE_64 {
          CheckValue(val as uint64);
        }
      }
      currPo2 := currPo2 * 2;
    }
  }

  method CheckSeq(bytes : seq<uint8>)
  {
    var result := FindLength(bytes);
    if result.Success? {
      var new_bytes := bytes[0..result.value];
      if bytes != new_bytes {
        expect !ValidSequence(bytes);
      }
      expect ValidSequence(new_bytes);
      var value := Decode(new_bytes);
      expect EncodeLength(value) == |new_bytes| as uint64;
      expect Encode(value) == new_bytes;
    } else {
      expect !ValidSequence(bytes);
    }
  }

  method {:test} TestDecode() {
    var start := Time.GetCurrentMilli();

    for i : uint32 := 0 to 256 {
      var bytes : seq<uint8> := [i as uint8];
      CheckSeq(bytes);
    }

    for i : uint32 := 0 to 256 {
      for j : uint32 := 0 to 256 {
        var bytes : seq<uint8> := [i as uint8, j as uint8];
        CheckSeq(bytes);
      }
    }

    for i : uint32 := 0 to 256 {
      for j : uint32 := 0 to 256 {
        for k : uint32 := 0 to 256 {
          var bytes : seq<uint8> := [i as uint8, j as uint8, k as uint8];
          CheckSeq(bytes);
        }
      }
    }

    var end := Time.GetCurrentMilli();
    print Time.FormatMilliDiff(start, end), " ";
  }
}
