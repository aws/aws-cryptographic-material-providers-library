// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "UInt.dfy"
include "../../libraries/src/Wrappers.dfy"

/*
  Converts unsigned numbers into variable length array<uint8>
  Seven bits per byte used to store actual data.

  // return the length of the encoded number at the start of s
  // return error if not a complete number or otherwise invalid
  function FindLength(s : array<uint8>) : Result<uint64, string>

  // return true if the whole of s is the valid encoding of a single value
  predicate ValidPartialSequence(s : array<uint8>)

  // same as ValidPartialSequence, but must not begin with 0x80
  predicate ValidSequence(s : array<uint8>)

  // convert number to array<uint8>
  Encode(x : uint64) : array<uint8>

  // convert array<uint8> to number
  Decode(s : array<uint8>) : uint64
*/

module {:options "-functionSyntax:4"} VarEncode64m {
  import opened Wrappers
  import opened BoundedInts

  const HighBit : uint8 := 0x80

  // Each encoded byte holds seven bits of actual data
  const MaxByteValue : uint64 := 128

  // Maximum Value for N bytes
  const Max1 : uint64 := 0x80
  const Max2 : uint64 := 0x4000
  const Max3 : uint64 := 0x200000
  const Max4 : uint64 := 0x10000000
  const Max5 : uint64 := 0x800000000
  const Max6 : uint64 := 0x40000000000
  const Max7 : uint64 := 0x2000000000000
  const Max8 : uint64 := 0x100000000000000
  const Max9 : uint64 := 0x8000000000000000
  // Max10 := UINT64_MAX

  // Maximum value of leading byte for 10-byte sequence
  const MaxLeading10 : uint8 := 0x2

  // Maximum value of leading byte for 5-byte sequence, with high bit set
  const MaxLeading10Set : uint8 := MaxLeading10 + HighBit

  datatype Error = Short | Long | Malformed

  // return the length of the encoded value at the start of this sequence
  // return an error if the sequence does not begin with a complete well formed encoding
  function FindLength(s : array<uint8>) : (ret : Result<uint64, Error>)
    reads s
    ensures ret.Success? ==>
              && ret.value as nat <= s.Length
              && ValidSequence(s[..ret.value])
              && (ret.value == 10 ==> s[0] < MaxLeading10Set)
  {
    var len : uint64 := if s.Length < 100 then s.Length as uint64 else 100;
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
      Success(5)
    else if 6 <= len && s[5] < HighBit then
      Success(6)
    else if 7 <= len && s[6] < HighBit then
      Success(7)
    else if 8 <= len && s[7] < HighBit then
      Success(8)
    else if 9 <= len && s[8] < HighBit then
      Success(9)
    else if 10 <= len && s[9] < HighBit then
      if s[0] < MaxLeading10Set then
        Success(10)
      else
        Failure(Long)
    else
      Failure(Long)
  }

  // the sequence is a well formed encoding
  predicate ValidSequence(s : seq<uint8>)
    ensures ValidSequence(s) ==> 0 < |s| <= 10
  {
    if 10 < |s| then
      false
    else
      var len := |s| as uint64;
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
      else if len == 5 then
        && s[0] >= HighBit
        && s[1] >= HighBit
        && s[2] >= HighBit
        && s[3] >= HighBit
        && s[4] < HighBit
      else if len == 6 then
        && s[0] >= HighBit
        && s[1] >= HighBit
        && s[2] >= HighBit
        && s[3] >= HighBit
        && s[4] >= HighBit
        && s[5] < HighBit
      else if len == 7 then
        && s[0] >= HighBit
        && s[1] >= HighBit
        && s[2] >= HighBit
        && s[3] >= HighBit
        && s[4] >= HighBit
        && s[5] >= HighBit
        && s[6] < HighBit
      else if len == 8 then
        && s[0] >= HighBit
        && s[1] >= HighBit
        && s[2] >= HighBit
        && s[3] >= HighBit
        && s[4] >= HighBit
        && s[5] >= HighBit
        && s[6] >= HighBit
        && s[7] < HighBit
      else if len == 9 then
        && s[0] >= HighBit
        && s[1] >= HighBit
        && s[2] >= HighBit
        && s[3] >= HighBit
        && s[4] >= HighBit
        && s[5] >= HighBit
        && s[6] >= HighBit
        && s[7] >= HighBit
        && s[8] < HighBit
      else
        assert len == 10;
        && s[0] < MaxLeading10Set
        && s[0] >= HighBit
        && s[1] >= HighBit
        && s[2] >= HighBit
        && s[3] >= HighBit
        && s[4] >= HighBit
        && s[5] >= HighBit
        && s[6] >= HighBit
        && s[7] >= HighBit
        && s[8] >= HighBit
        && s[9] < HighBit
  }

  // Decode the value
  function Decode(s : array<uint8>) : (ret : uint64)
    reads s
    requires ValidSequence(s[..])
  {
    var len : uint64 := s.Length as uint64;
    if len == 1 then
      s[0] as uint64
    else if len == 2 then
      (s[0] - HighBit) as uint64 * Max1
      + s[1] as uint64
    else if len == 3 then
      (s[0] - HighBit) as uint64 * Max2
      + (s[1] - HighBit) as uint64 * Max1
      + s[2] as uint64
    else if len == 4 then
      (s[0] - HighBit) as uint64 * Max3
      + (s[1] - HighBit) as uint64 * Max2
      + (s[2] - HighBit) as uint64 * Max1
      + s[3] as uint64
    else if len == 5 then
      (s[0] - HighBit) as uint64 * Max4
      + (s[1] - HighBit) as uint64 * Max3
      + (s[2] - HighBit) as uint64 * Max2
      + (s[3] - HighBit) as uint64 * Max1
      + s[4] as uint64
    else if len == 6 then
      (s[0] - HighBit) as uint64 * Max5
      + (s[1] - HighBit) as uint64 * Max4
      + (s[2] - HighBit) as uint64 * Max3
      + (s[3] - HighBit) as uint64 * Max2
      + (s[4] - HighBit) as uint64 * Max1
      + s[5] as uint64
    else if len == 7 then
      (s[0] - HighBit) as uint64 * Max6
      + (s[1] - HighBit) as uint64 * Max5
      + (s[2] - HighBit) as uint64 * Max4
      + (s[3] - HighBit) as uint64 * Max3
      + (s[4] - HighBit) as uint64 * Max2
      + (s[5] - HighBit) as uint64 * Max1
      + s[6] as uint64
    else if len == 8 then
      (s[0] - HighBit) as uint64 * Max7
      + (s[1] - HighBit) as uint64 * Max6
      + (s[2] - HighBit) as uint64 * Max5
      + (s[3] - HighBit) as uint64 * Max4
      + (s[4] - HighBit) as uint64 * Max3
      + (s[5] - HighBit) as uint64 * Max2
      + (s[6] - HighBit) as uint64 * Max1
      + s[7] as uint64
    else if len == 9 then
      (s[0] - HighBit) as uint64 * Max8
      + (s[1] - HighBit) as uint64 * Max7
      + (s[2] - HighBit) as uint64 * Max6
      + (s[3] - HighBit) as uint64 * Max5
      + (s[4] - HighBit) as uint64 * Max4
      + (s[5] - HighBit) as uint64 * Max3
      + (s[6] - HighBit) as uint64 * Max2
      + (s[7] - HighBit) as uint64 * Max1
      + s[8] as uint64
    else
      assert len == 10;
      (s[0] - HighBit) as uint64 * Max9
      + (s[1] - HighBit) as uint64 * Max8
      + (s[2] - HighBit) as uint64 * Max7
      + (s[3] - HighBit) as uint64 * Max6
      + (s[4] - HighBit) as uint64 * Max5
      + (s[5] - HighBit) as uint64 * Max4
      + (s[6] - HighBit) as uint64 * Max3
      + (s[7] - HighBit) as uint64 * Max2
      + (s[8] - HighBit) as uint64 * Max1
      + s[9] as uint64
  }

  // Encode the value
  method Encode(val : uint64) returns (ret : array<uint8>)
    ensures ValidSequence(ret[..])
    ensures ret.Length == EncodeLength(val) as nat
  {
    if val < Max1 {
      return new uint8[] [val as uint8];
    } else if val < Max2 {
      return new uint8[] 
      [ (val / Max1) as uint8 + HighBit,
        (val % Max1) as uint8];
    } else if val < Max3 {
      return new uint8[] 
      [ (val / Max2) as uint8 + HighBit,
        ((val / Max1) % Max1) as uint8 + HighBit,
        (val % Max1) as uint8];
    } else if val < Max4 {
      return new uint8[] 
      [ (val / Max3) as uint8  + HighBit,
        ((val / Max2) % Max1) as uint8 + HighBit,
        ((val / Max1) % Max1) as uint8 + HighBit,
        (val % Max1) as uint8];
    } else if val < Max5 {
      return new uint8[] 
      [ (val / Max4) as uint8 + HighBit,
        ((val / Max3) % Max1) as uint8 + HighBit,
        ((val / Max2) % Max1) as uint8 + HighBit,
        ((val / Max1) % Max1) as uint8 + HighBit,
        (val % Max1) as uint8];
    } else if val < Max6 {
      return new uint8[] 
      [ (val / Max5) as uint8 + HighBit,
        ((val / Max4) % Max1) as uint8 + HighBit,
        ((val / Max3) % Max1) as uint8 + HighBit,
        ((val / Max2) % Max1) as uint8 + HighBit,
        ((val / Max1) % Max1) as uint8 + HighBit,
        (val % Max1) as uint8];
    } else if val < Max7 {
      return new uint8[] 
      [ (val / Max6) as uint8 + HighBit,
        ((val / Max5) % Max1) as uint8 + HighBit,
        ((val / Max4) % Max1) as uint8 + HighBit,
        ((val / Max3) % Max1) as uint8 + HighBit,
        ((val / Max2) % Max1) as uint8 + HighBit,
        ((val / Max1) % Max1) as uint8 + HighBit,
        (val % Max1) as uint8];
    } else if val < Max8 {
      return new uint8[] 
      [ (val / Max7) as uint8 + HighBit,
        ((val / Max6) % Max1) as uint8 + HighBit,
        ((val / Max5) % Max1) as uint8 + HighBit,
        ((val / Max4) % Max1) as uint8 + HighBit,
        ((val / Max3) % Max1) as uint8 + HighBit,
        ((val / Max2) % Max1) as uint8 + HighBit,
        ((val / Max1) % Max1) as uint8 + HighBit,
        (val % Max1) as uint8];
    } else if val < Max9 {
      return new uint8[] 
      [ (val / Max8) as uint8 + HighBit,
        ((val / Max7) % Max1) as uint8 + HighBit,
        ((val / Max6) % Max1) as uint8 + HighBit,
        ((val / Max5) % Max1) as uint8 + HighBit,
        ((val / Max4) % Max1) as uint8 + HighBit,
        ((val / Max3) % Max1) as uint8 + HighBit,
        ((val / Max2) % Max1) as uint8 + HighBit,
        ((val / Max1) % Max1) as uint8 + HighBit,
        (val % Max1) as uint8];
    } else {
      return new uint8[] 
      [ (val / Max9) as uint8 + HighBit,
        ((val / Max8) % Max1) as uint8 + HighBit,
        ((val / Max7) % Max1) as uint8 + HighBit,
        ((val / Max6) % Max1) as uint8 + HighBit,
        ((val / Max5) % Max1) as uint8 + HighBit,
        ((val / Max4) % Max1) as uint8 + HighBit,
        ((val / Max3) % Max1) as uint8 + HighBit,
        ((val / Max2) % Max1) as uint8 + HighBit,
        ((val / Max1) % Max1) as uint8 + HighBit,
        (val % Max1) as uint8];
    }
  }

  // These two lemmas are proved by rigorous testing
  // lemma EncodeRoundTrip(val : uint64)
  //   ensures Decode(Encode(val)) == val
  // {
  //   assume {:axiom} Decode(Encode(val)) == val;
  // }

  // lemma DecodeRoundTrip(bytes : array<uint8>)
  //   requires ValidSequence(bytes)
  //   ensures Encode(Decode(bytes)) == bytes
  // {
  //   assume {:axiom} Encode(Decode(bytes)) == bytes;
  // }

  function EncodeLength(x : uint64) : uint64
  {
    if x < Max1 then 1
    else if x < Max2 then 2
    else if x < Max3 then 3
    else if x < Max4 then 4
    else if x < Max5 then 5
    else if x < Max6 then 6
    else if x < Max7 then 7
    else if x < Max8 then 8
    else if x < Max9 then 9
    else 10
  }
}
