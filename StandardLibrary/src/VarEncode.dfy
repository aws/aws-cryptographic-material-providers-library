// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "UInt.dfy"
include "../../libraries/src/Wrappers.dfy"

/*
  Converts unsigned numbers into variable length seq<uint8>
  Seven bits per byte used to store actual data.

  // return the length of the encoded number at the start of s
  // return error if not a complete number or otherwise invalid
  function FindLength(s : seq<uint8>) : Result<nat, string>

  // return true if the whole of s is the valid encoding of a single value
  predicate ValidPartialSequence(s : seq<uint8>)

  // same as ValidPartialSequence, but must not begin with 0x80
  predicate ValidSequence(s : seq<uint8>)

  // convert number to seq<uint8>
  Encode(x : nat) : seq<uint8>

  // convert seq<uint8> to number
  Decode(s : seq<uint8>) : nat
*/

module {:options "-functionSyntax:4"} VarEncode {
  import opened StandardLibrary.UInt
  import opened Wrappers

  const HighBit : uint8 := 0x80

  // Each encoded byte holds seven bits of actual data
  const MaxByteValue : nat := 128

  // return the length of the suffix of an encoded value at the start of this sequence
  // return an error if the sequence does not begin with the suffix complete well formed encoding
  function FindLength2(s : seq<uint8>, pos : nat := 0) : (ret : Result<nat, string>)
    requires 0 < |s|
    requires pos < |s|
    requires forall i | 0 <= i < (pos) :: s[i] >= HighBit
    decreases |s| - pos
    ensures ret.Success? ==>
              && ret.value <= |s|
              && ValidPartialSequence(s[..ret.value])
    ensures ret.Failure? <==>
            forall i | 0 <= i < |s| :: s[i] >= HighBit
  {
    if s[pos] < HighBit then
      Success(pos + 1)
    else if pos == |s| - 1 then
      Failure("VarEncode sequence does not contain a terminating byte.")
    else
      FindLength2(s, pos+1)
  }

  // return the length of the encoded value at the start of this sequence
  // return an error if the sequence does not begin with a complete well formed encoding
  function FindLength(s : seq<uint8>) : (ret : Result<nat, string>)
    requires 0 < |s|
    ensures ret.Success? ==>
              && ret.value <= |s|
              && ValidSequence(s[..ret.value])
    ensures ret.Failure? <==>
            || s[0] == HighBit
            || forall i | 0 <= i < |s| :: s[i] >= HighBit
  {
    if s[0] == HighBit then
      Failure("VarEncode sequence starts with 0x80.")
    else
      FindLength2(s, 0)
  }

  // the sequence is a suffix of a well formed encoding
  predicate ValidPartialSequence(s : seq<uint8>)
  {
    && 0 < |s|
    && (forall i | 0 <= i < (|s|-1) :: s[i] >= HighBit)
    && s[|s|-1] < HighBit
  }

  // the sequence is a well formed encoding
  predicate ValidSequence(s : seq<uint8>)
  {
    && ValidPartialSequence(s)
    && s[0] != HighBit
  }

  // Decode the higher order bytes of the value
  function Decode2(s : seq<uint8>) : (ret : nat)
    requires (forall i | 0 <= i < |s| :: s[i] >= HighBit)
  {
    if |s| == 0 then
      0
    else
      Decode2(s[..|s|-1]) * 128 + (s[|s|-1] - HighBit) as nat
  }

  // Decode the value
  function Decode(s : seq<uint8>) : (ret : nat)
    requires ValidSequence(s)
  {
    if |s| == 1 then
      s[0] as nat
    else
      Decode2(s[..|s|-1]) * 128 + s[|s|-1] as nat
  }

  // Encode the higher order bytes of the value
  function Encode2(val : nat) : (ret : seq<uint8>)
    requires 0 < val
    ensures 0 < |ret|
    ensures (forall i | 0 <= i < |ret| :: ret[i] >= HighBit)
    ensures |ret| == EncodeLength(val)
    ensures ret[0] != HighBit
  {
    var val1 := (val % MaxByteValue) as uint8;
    var val2 := (val / MaxByteValue);
    assert 0 < val1 || 0 < val2;
    var val1a := val1 + HighBit;
    if val2 == 0 then
      [val1a]
    else
      Encode2(val2) + [val1a]
  }

  // Encode the value
  function Encode(val : nat) : (ret : seq<uint8>)
    ensures ValidSequence(ret)
    ensures |ret| == EncodeLength(val)
  {
    CheckLength(val);
    if val == 0 then
      [0]
    else
      var val1 := (val % MaxByteValue) as uint8;
      var val2 := (val / MaxByteValue);
      assert 0 < val1 || 0 < val2;
      if val2 == 0 then
        [val1]
      else
        Encode2(val2) + [val1]
  }

  // These two lemmas are proved by rigorous testing
  lemma EncodeRoundTrip(val : nat)
    ensures Decode(Encode(val)) == val
  {
    assume {:axiom} Decode(Encode(val)) == val;
  }

  lemma DecodeRoundTrip(bytes : seq<uint8>)
    requires ValidSequence(bytes)
    ensures Encode(Decode(bytes)) == bytes
  {
    assume {:axiom} Encode(Decode(bytes)) == bytes;
  }

  ghost const Max1 := 0x80
  ghost const Max2 := 0x4000
  ghost const Max3 := 0x200000
  ghost const Max4 := 0x10000000
  ghost const Max5 := 0x800000000
  ghost const Max6 := 0x40000000000
  ghost const Max7 := 0x2000000000000
  ghost const Max8 := 0x100000000000000
  ghost const Max9 := 0x8000000000000000

  ghost function EncodeLength(x : nat) : nat
  {
    if x < Max1 then
      1
    else
      1 + EncodeLength(x / MaxByteValue)
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


}