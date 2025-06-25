// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/VarEncode64m.dfy"
include "../src/Time.dfy"

module {:options "-functionSyntax:4"} VarEncode64mTest {
  import opened VarEncode64m
  import opened BoundedInts
  import opened Wrappers
  import Time

  method CheckValue(val : uint64)
  {
    var enc := Encode(val);
    if !ValidSequence(enc[..]) {
      print "Invalid Sequence from : ", val, " ", enc.Length, " ", enc, "\n";
    }
    expect ValidSequence(enc[..]);
    if Decode(enc) != val {
      print "Decode : ", val, " ", Decode(enc), " ", enc.Length, " ", enc, "\n";
    }
    expect Decode(enc) == val;
    if FindLength(enc) != Success(enc.Length as uint64) {
      print "Length ", val, " ", FindLength(enc), " ", enc.Length, " ", enc, "\n";
    }
    expect FindLength(enc) == Success(enc.Length as uint64);
    expect EncodeLength(val) == enc.Length as uint64;
    expect ValidSequence(enc[..]);
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

  /* Converts a sequence to an array. */
  method ToArray<T>(xs: seq<T>) returns (a: array<T>)
    ensures fresh(a)
    ensures a.Length == |xs|
    ensures forall i :: 0 <= i < |xs| ==> a[i] == xs[i]
  {
    a := new T[|xs|](i requires 0 <= i < |xs| => xs[i]);
  }

  method EqualArray(x : array<uint8>, y : array<uint8>) returns (ret : bool)
  {
    if x.Length != y.Length {
      return false;
    }
    for i := 0 to x.Length {
      if x[i] != y[i] {
        return false;
      }
    }
    return true;
  }

  method CheckSeq(bytes : array<uint8>)
  {
    var result := FindLength(bytes);
    if result.Success? {
      var new_bytes_seq := bytes[0..result.value];
      var new_bytes_arr := ToArray(new_bytes_seq);
      if new_bytes_arr.Length != bytes.Length {
        expect !ValidSequence(bytes[..]);
      }
      expect ValidSequence(new_bytes_seq);
      var value := Decode(new_bytes_arr);
      expect EncodeLength(value) == |new_bytes_seq| as uint64;
      var enc := Encode(value);
      var equal := EqualArray(enc, new_bytes_arr);
      expect equal;
    } else {
      expect !ValidSequence(bytes[..]);
    }
  }

  method {:test} TestDecode() {
    var start := Time.GetCurrentMilli();

    for i : nat := 0 to 256 {
      var bytes := new uint8[] [i as uint8];
      CheckSeq(bytes);
    }

    for i : nat := 0 to 256 {
      for j : nat := 0 to 256 {
        var bytes :=  new uint8[] [i as uint8, j as uint8];
        CheckSeq(bytes);
      }
    }

    for i : nat := 0 to 256 {
      for j : nat := 0 to 256 {
        for k : nat := 0 to 256 {
          var bytes :=  new uint8[] [i as uint8, j as uint8, k as uint8];
          CheckSeq(bytes);
        }
      }
    }

    var end := Time.GetCurrentMilli();
    print Time.FormatMilliDiff(start, end), " ";
  }
}
