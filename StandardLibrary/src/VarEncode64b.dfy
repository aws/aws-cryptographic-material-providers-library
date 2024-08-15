// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "UInt.dfy"
  // include "SerializeFunctions.dfy"

/*
  Converts unsigned numbers into variable length seq<uint8>
  Seven bits per byte used to store actual data.

  // return the length of the encoded number at the start of s
  // return -1 if not a complete number
  function FindLength(s : seq<uint8>) : int

  // return true if the whole of s is a valid encoding
  predicate ValidSequence(s : seq<uint8>)

  // same as ValidSequence, but must not begin with 0x80
  predicate ValidFullSequence(s : seq<uint8>)

  // convert number to seq<uint8>
  Encode(x : nat) : seq<uint8>

  // convert seq<uint8> to number
  Decode(s : seq<uint8>) : nat

*/

module {:options "-functionSyntax:4"} VarEncode64b {
  import opened StandardLibrary.UInt
    // import opened SerializeFunctions
    // import opened Wrappers

  const HighBit : uint8 := 0x80

  function FindLength(s : seq<uint8>, pos : nat := 0) : (ret : int)
    requires 0 < |s|
    requires pos < |s|
    requires forall i | 0 <= i < (pos) :: s[i] >= HighBit
    decreases |s| - pos
    ensures ret != 0
    ensures ret > 0 ==> 
      && ret <= |s|
      && (forall i | 0 <= i < (ret-1) :: s[i] >= HighBit)
      && s[ret-1] < HighBit
      && ValidSequence(s[..ret])
    ensures ret < 0 <==>
      forall i | 0 <= i < ret :: s[i] >= HighBit
  {
    if s[pos] < HighBit then
      pos + 1
    else if pos == |s| - 1 then
      -1
    else
      FindLength(s, pos+1)
  }

  predicate ValidSequence(s : seq<uint8>)
  {
    && 0 < |s|
    && (forall i | 0 <= i < (|s|-1) :: s[i] >= HighBit)
    && s[|s|-1] < HighBit
  }

  predicate ValidFullSequence(s : seq<uint8>)
  {
    && ValidSequence(s)
    && s[0] != HighBit
  }

  lemma Foo3(s : seq<uint8>)
    requires ValidSequence(s)
    ensures exists i | 0 <= i < |s| :: s[i] < HighBit
{

}

//   lemma Foo(s : seq<uint8>)
//     requires ValidFullSequence(s)
//     ensures FindLength(s) == |s|
// {  
//   if |s| == 1 {
//     assert FindLength(s) == |s|;
//   } else if |s| == 2 {
//     assert FindLength(s) == |s|;
//   } else if |s| == 3 {
//     assert FindLength(s) == |s|;
//   } else if |s| == 4 {
//     assert FindLength(s) == |s|;
//   } else {
//     assert FindLength(s) == |s|;
//   }
// }

  function Decode(s : seq<uint8>, acc : nat := 0) : nat
    requires ValidSequence(s)
  {
    if |s| == 1 then
      (acc * 128) + (s[0] as nat)
    else
      var newVal := (acc * 128) + (s[0] - HighBit) as nat;
      Decode(s[1..], newVal)
  }

  function Encode(val : nat, acc : seq<uint8> := []) : (ret : seq<uint8>)
    requires |acc| == 0 || ValidSequence(acc)
    ensures ValidSequence(ret)
  {
    if val == 0 then
      if |acc| == 0 then
        [0]
      else
        acc
    else
      var val1 := (val % 0x80) as uint8;
      var val2 := (val / 0x80);
      assert 0 < val1 || 0 < val2;
      if |acc| == 0 then
        Encode(val2, [val1])
      else
        var val1a := val1 + HighBit;
        assert HighBit <= val1a <= 0xff;
        Encode(val2, [val1a] + acc)
  }

  // lemma XXX(val: uint64, enc : seq<uint8>, encLen : int)
  //   requires Encode(val) == enc
  //   requires |Encode(val)| == encLen
  //   ensures ValidSequence(enc)
  //   ensures Decode(enc) == val
  // {
  //   if val <= 127 {
  //     assert Decode(enc) == val;
  //   } else if val == 1 {
  //     assert Decode(enc) == val;
  //   } else if val == 127 {
  //     assert Decode(enc) == val;
  //   } else if encLen == 1 {
  //     assert Decode(enc) == val;
  //   } else if encLen == 2 {
  //     assert Decode(enc) == val;
  //   } else {
  //     assert Decode(enc) == val;
  //   }
  // }

  // lemma YYY(val: uint64, enc : seq<uint8>)
  //   requires ValidSequence(enc)
  //   requires Decode(enc) == val
  //   ensures Encode(val) == enc
  // {}
  
}