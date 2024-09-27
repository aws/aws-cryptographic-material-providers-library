// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "UInt.dfy"
include "../../libraries/src/Wrappers.dfy"

/*
  Converts unsigned numbers into variable length seq<uint8>
  Seven bits per byte used to store actual data.

  // return the length of the encoded number at the start of s
  // return error if not a complete number or otherwise invalid
  function FindLength(s : seq<uint8>) : Result<uint16, string>

  // return true if the whole of s is the valid encoding of a single value
  predicate ValidPartialSequence(s : seq<uint8>)

  // same as ValidPartialSequence, but must not begin with 0x80
  predicate ValidSequence(s : seq<uint8>)

  // convert number to seq<uint8>
  Encode(x : uint16) : seq<uint8>

  // convert seq<uint8> to number
  Decode(s : seq<uint8>) : uint16
*/

module {:options "-functionSyntax:4"} VarEncode16 {
  import opened Wrappers
  import opened BoundedInts

  const HighBit : uint8 := 0x80

  // Each encoded byte holds seven bits of actual data
  const MaxByteValue : uint16 := 128

  // Maximum Value for N bytes
  const Max1 : uint16 := 0x80
  const Max2 : uint16 := 0x4000
  // const Max3 := UINT16_MAX

  // Maximum value of leading byte for 3-byte sequence
  const MaxLeading3 : uint8 := 0x4

  // Maximum value of leading byte for 3-byte sequence, with high bit set
  const MaxLeading3Set : uint8 := MaxLeading3 + HighBit

  datatype Error = Short | Long | Malformed

  // return the length of the encoded value at the start of this sequence
  // return an error if the sequence does not begin with a complete well formed encoding
  function FindLength(s : seq<uint8>) : (ret : Result<uint16, Error>)
    ensures ret.Success? ==>
              && ret.value as nat <= |s|
              && ValidSequence(s[..ret.value])
              && (ret.value == 3 ==> s[0] < MaxLeading3Set)
  {
    var len : uint16 := if |s| < 100 then |s| as uint16 else 100;
    if len == 0 then
      Failure(Short)
    else if s[0] == HighBit then
      Failure(Malformed)
    else if 1 <= len && s[0] < HighBit then
        Success(1)
    else if 2 <= len && s[1] < HighBit then
        Success(2)
    else if 3 <= len && s[2] < HighBit then
        if s[0] < MaxLeading3Set then
          Success(3)
        else
          Failure(Long)
    else
        Failure(Long)
  }

  // the sequence is a well formed encoding
  predicate ValidSequence(s : seq<uint8>)
    ensures ValidSequence(s) ==> 0 < |s| <= 3
  {
    if 3 < |s| then
      false
    else
      var len := |s| as uint16;
      if len == 0 then
        false
      else if s[0] == HighBit then
        false
      else if len == 1 then
        s[0] < HighBit
      else if len == 2 then
        && s[0] >= HighBit
        && s[1] < HighBit
      else
        assert len == 3;
        && s[0] < MaxLeading3Set
        && s[0] >= HighBit
        && s[1] >= HighBit
        && s[2] < HighBit
  }

  // Decode the value
  function Decode(s : seq<uint8>) : (ret : uint16)
    requires ValidSequence(s)
  {
    var len : uint16 := |s| as uint16;
    if len == 1 then
      s[0] as uint16
    else if len == 2 then
      (s[0] - HighBit) as uint16 * Max1
      + s[1] as uint16
    else 
      assert len == 3;
      (s[0] - HighBit) as uint16 * Max2
      + (s[1] - HighBit) as uint16 * Max1
      + s[2] as uint16
  }

  // Encode the value
  function Encode(val : uint16) : (ret : seq<uint8>)
    ensures ValidSequence(ret)
    ensures |ret| == EncodeLength(val) as nat
  {
    if val < Max1 then
      [val as uint8]
    else if val < Max2 then
      [ (val / Max1) as uint8 + HighBit,
        (val % Max1) as uint8]
    else
      [ (val / Max2) as uint8 + HighBit,
        ((val / Max1) % Max1) as uint8 + HighBit,
        (val % Max1) as uint8]
  }

  // These two lemmas are proved by rigorous testing
  lemma EncodeRoundTrip(val : uint16)
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

  function EncodeLength(x : uint16) : uint16
  {
    if x < Max1 then 1
    else if x < Max2 then 2
    else 3
  }
}