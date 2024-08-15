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
  const HighNat : nat := 0x80

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

  function Decode2(s : seq<uint8>) : (ret : nat)
    requires (forall i | 0 <= i < |s| :: s[i] >= HighBit)
    // ensures |s| == EncodeLength(ret)
  {
    if |s| == 0 then
      0
    else
      Decode2(s[..|s|-1]) * 128 + (s[|s|-1] - HighBit) as nat
  }

  function Decode(s : seq<uint8>) : (ret : nat)
    requires ValidFullSequence(s)
    // ensures |s| == EncodeLength(ret)
  {
    if |s| == 1 then
      s[0] as nat
    else
      Decode2(s[..|s|-1]) * 128 + s[|s|-1] as nat
  }

  function Encode2(val : nat) : (ret : seq<uint8>)
    requires 0 < val
    ensures 0 < |ret|
    ensures (forall i | 0 <= i < |ret| :: ret[i] >= HighBit)
    ensures |ret| == EncodeLength(val)
    ensures ret[0] != HighBit
  {
      var val1 := (val % HighNat) as uint8;
      var val2 := (val / HighNat);
      assert 0 < val1 || 0 < val2;
      var val1a := val1 + HighBit;
      if val2 == 0 then
        [val1a]
      else
        Encode2(val2) + [val1a]
  }

  function Encode(val : nat) : (ret : seq<uint8>)
    ensures ValidFullSequence(ret)
    ensures |ret| == EncodeLength(val)
  {
    CheckLength(val);
    if val == 0 then
        [0]
    else
      var val1 := (val % HighNat) as uint8;
      var val2 := (val / HighNat);
      assert 0 < val1 || 0 < val2;
      if val2 == 0 then
        [val1]
      else
        Encode2(val2) + [val1]
  }

  const Max1 := 0x80
  const Max2 := 0x4000
  const Max3 := 0x200000
  const Max4 := 0x10000000
  const Max5 := 0x800000000
  const Max6 := 0x40000000000
  const Max7 := 0x2000000000000
  const Max8 := 0x100000000000000
  const Max9 := 0x8000000000000000

  function EncodeLength(x : nat) : nat
  {
    if x < Max1 then
      1
    else
      1 + EncodeLength(x / HighNat)
  }

  lemma CheckLength(x : nat)
    ensures x < Max1 ==> EncodeLength(x) == 1
    ensures Max1 <= x < Max2 ==> EncodeLength(x) == 2
    ensures Max2 <= x < Max3 ==> EncodeLength(x) == 3
    ensures Max3 <= x < Max4 ==> EncodeLength(x) == 4
    ensures Max4 <= x < Max5 ==> EncodeLength(x) == 5
    ensures Max5 <= x < Max6 ==> EncodeLength(x) == 6
    ensures Max6 <= x < Max7 ==> EncodeLength(x) == 7
    ensures Max7 <= x < Max8 ==> EncodeLength(x) == 8
    ensures Max8 <= x < Max9 ==> EncodeLength(x) == 9
  {}

  lemma EncodeDecode1(val: nat, enc : seq<uint8>)
    requires val < Max1
    requires Encode(val) == enc
    ensures |Encode(val)| == 1
    ensures ValidFullSequence(enc)
    ensures Decode(enc) == val
  {}
  lemma DecodeEncode1(val: nat, enc : seq<uint8>)
    requires val < Max1
    requires ValidFullSequence(enc)
    requires Decode(enc) == val
    ensures Encode(val) == enc
  {}

  lemma EncodeDecode2(val: nat, enc : seq<uint8>)
    requires Max1 <= val < Max2
    requires Encode(val) == enc
    ensures |Encode(val)| == 2
    ensures ValidFullSequence(enc)
    ensures Decode(enc) == val
  {}
  lemma EncodeDecode(val: nat, enc : seq<uint8>)
    requires Encode(val) == enc
    ensures ValidFullSequence(enc)
    ensures Decode(enc) == val
  {}

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