// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/VarEncode16.dfy"
include "../src/Time.dfy"

module {:options "-functionSyntax:4"} VarEncode16Test {
  import opened VarEncode16
  import opened BoundedInts
  import opened Wrappers
  import Time

  method CheckValue(val : uint16)
  {
    var enc := Encode(val);
    expect ValidSequence(enc);
    if Decode(enc) != val {
      print "Decode : ", val, " ", Decode(enc), " ", |enc|, " ", enc, "\n";
    }
    expect Decode(enc) == val;
    if FindLength(enc) != Success(|enc| as uint16) {
      print "Length ", val, " ", FindLength(enc), " ", |enc|, " ", enc, "\n";
    }
    expect FindLength(enc) == Success(|enc| as uint16);
    expect EncodeLength(val) == |enc| as uint16;
    expect ValidSequence(enc);
  }

  method {:test} TestEncodeSmallNumbers() {
    for i := 0 to UINT16_MAX {
      CheckValue(i as uint16);
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
      expect EncodeLength(value) == |new_bytes| as uint16;
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
