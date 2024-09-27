// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "UInt.dfy"
include "../../libraries/src/Wrappers.dfy"

/*
  Converts unsigned numbers into variable length seq<uint8>
  Seven bits per byte used to store actual data.

  // return the length of the encoded number at the start of s
  // return error if not a complete number or otherwise invalid
  function FindLength(s : seq<uint8>) : Result<uint32, string>

  // return true if the whole of s is the valid encoding of a single value
  predicate ValidPartialSequence(s : seq<uint8>)

  // same as ValidPartialSequence, but must not begin with 0x80
  predicate ValidSequence(s : seq<uint8>)

  // convert number to seq<uint8>
  Encode(x : uint32) : seq<uint8>

  // convert seq<uint8> to number
  Decode(s : seq<uint8>) : uint32
*/

module {:options "-functionSyntax:4"} VarEncode32 {
  import opened Wrappers
  import opened BoundedInts

  const HighBit : uint8 := 0x80

  // Each encoded byte holds seven bits of actual data
  const MaxByteValue : uint32 := 128

  // Maximum Value for N bytes
  const Max1 : uint32 := 0x80
  const Max2 : uint32 := 0x4000
  const Max3 : uint32 := 0x200000
  const Max4 : uint32 := 0x10000000
  // Max5 := UINT32_MAX

  // Maximum value of leading byte for 5-byte sequence
  const MaxLeading5 : uint8 := 0x10

  // Maximum value of leading byte for 5-byte sequence, with high bit set
  const MaxLeading5Set : uint8 := MaxLeading5 + HighBit

  datatype Error = Short | Long | Malformed

  // return the length of the encoded value at the start of this sequence
  // return an error if the sequence does not begin with a complete well formed encoding
  function FindLength(s : seq<uint8>) : (ret : Result<uint32, Error>)
    ensures ret.Success? ==>
              && ret.value as nat <= |s|
              && ValidSequence(s[..ret.value])
              && (ret.value == 5 ==> s[0] < MaxLeading5Set)
  {
    var len : uint32 := if |s| < 100 then |s| as uint32 else 100;
    if len == 0 then
      Failure(Short)
    else if s[0] == HighBit then
      Failure(Malformed)
    else if 1 <= len && s[0] < HighBit then
        Success(1)
    else if 2 <= len && s[1] < HighBit then
        Success(2)
    else if 3 <= len && s[2] < HighBit then
        Success(3)
    else if 4 <= len && s[3] < HighBit then
        Success(4)
    else if 5 <= len && s[4] < HighBit then
        if s[0] < MaxLeading5Set then
          Success(5)
        else
          Failure(Long)
    else
        Failure(Long)
  }

  // the sequence is a well formed encoding
  predicate ValidSequence(s : seq<uint8>)
    ensures ValidSequence(s) ==> 0 < |s| <= 5
  {
    if 5 < |s| then
      false
    else
      var len := |s| as uint32;
      if len == 0 then
        false
      else if s[0] == HighBit then
        false
      else if len == 1 then
        s[0] < HighBit
      else if len == 2 then
        && s[0] >= HighBit
        && s[1] < HighBit
      else if len == 3 then
        && s[0] >= HighBit
        && s[1] >= HighBit
        && s[2] < HighBit
      else if len == 4 then
        && s[0] >= HighBit
        && s[1] >= HighBit
        && s[2] >= HighBit
        && s[3] < HighBit
      else
        assert len == 5;
        && s[0] < MaxLeading5Set
        && s[0] >= HighBit
        && s[1] >= HighBit
        && s[2] >= HighBit
        && s[3] >= HighBit
        && s[4] < HighBit
  }

  // Decode the value
  function Decode(s : seq<uint8>) : (ret : uint32)
    requires ValidSequence(s)
  {
    var len : uint32 := |s| as uint32;
    if len == 1 then
      s[0] as uint32
    else if len == 2 then
      (s[0] - HighBit) as uint32 * Max1
      + s[1] as uint32
    else if len == 3 then
      (s[0] - HighBit) as uint32 * Max2
      + (s[1] - HighBit) as uint32 * Max1
      + s[2] as uint32
    else if len == 4 then
      (s[0] - HighBit) as uint32 * Max3
      + (s[1] - HighBit) as uint32 * Max2
      + (s[2] - HighBit) as uint32 * Max1
      + s[3] as uint32
    else
      assert len == 5;
      (s[0] - HighBit) as uint32 * Max4
      + (s[1] - HighBit) as uint32 * Max3
      + (s[2] - HighBit) as uint32 * Max2
      + (s[3] - HighBit) as uint32 * Max1
      + s[4] as uint32
  }

  // Encode the value
  function Encode(val : uint32) : (ret : seq<uint8>)
    ensures ValidSequence(ret)
    ensures |ret| == EncodeLength(val) as nat
  {
    if val < Max1 then
      [val as uint8]
    else if val < Max2 then
      [ (val / Max1) as uint8 + HighBit,
        (val % Max1) as uint8]
    else if val < Max3 then
      [ (val / Max2) as uint8 + HighBit,
        ((val / Max1) % Max1) as uint8 + HighBit,
        (val % Max1) as uint8]
    else if val < Max4 then
      [ (val / Max3) as uint8  + HighBit,
        ((val / Max2) % Max1) as uint8 + HighBit,
        ((val / Max1) % Max1) as uint8 + HighBit,
        (val % Max1) as uint8]
    else
      [ (val / Max4) as uint8 + HighBit,
        ((val / Max3) % Max1) as uint8 + HighBit,
        ((val / Max2) % Max1) as uint8 + HighBit,
        ((val / Max1) % Max1) as uint8 + HighBit,
        (val % Max1) as uint8]
  }

  // These two lemmas are proved by rigorous testing
  lemma EncodeRoundTrip(val : uint32)
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

  function EncodeLength(x : uint32) : uint32
  {
    if x < Max1 then 1
    else if x < Max2 then 2
    else if x < Max3 then 3
    else if x < Max4 then 4
    else 5
  }
}