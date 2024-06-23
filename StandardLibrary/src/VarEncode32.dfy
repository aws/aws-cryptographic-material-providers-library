// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "UInt.dfy"
include "SerializeFunctions.dfy"

/*
  Converts unsigned numbers into variable length seq<uint8>
  Seven bits per byte used to store actual data.

  // Type for the encoded length
  newtype MyLen = x | 1 <= x <= 5 witness 1

  // checks for the very small number of invalid encoding sequences
  predicate ValidEncoding(x : seq<uint8>)

  // convert uint32 to seq<uint8>
  Encode(x : uint32) : (ret : seq<uint8>)

  // convert seq<uint8> to uint32
  Decode(x : seq<uint8>) : (ret : uint32)

  // If I were to encode x, how many bytes would the result have?
  EncodeLength(x : uint32) : (ret : MyLen)

  // If a seq<uint8> has first byte x, how many bytes are being used for this encoded number?
  DecodeLength(x : uint8) : (ret : MyLen)
*/

module {:options "-functionSyntax:4"} VarEncode32 {
  import opened StandardLibrary.UInt
  import opened SerializeFunctions
  import opened Wrappers

  newtype MyLen = x | 1 <= x <= 5 witness 1

  const Max1 : uint32 := 0x80
  const Max2 : uint32 := 0x4000
  const Max3 : uint32 := 0x200000
  const Max4 : uint32 := 0x10000000

  const Tag2 : uint8 := 0x80
  const Tag3 : uint8 := 0xc0
  const Tag4 : uint8 := 0xe0
  const Tag5 : uint8 := 0xf0
  const Tag6 : uint8 := 0xf8

  predicate ValidEncoding(x : seq<uint8>, len: MyLen)
    requires len as int == |x|
    requires DecodeLength(x[0]) == len
  {
    match len {
      case 1 => x[0] < Tag2
      case 2 => x[0] > Tag2 || (x[0] == Tag2 && x[1] >= 128)
      case 3 => x[0] > Tag3 || (x[0] == Tag3 && x[1] >= 64)
      case 4 => x[0] > Tag4 || (x[0] == Tag4 && x[1] >= 32)
      case 5 => x[0] == Tag5 && (x[1] >= 16)
    }
  }

  function EncodeLength(x : uint32) : (ret : MyLen)
  {
    if x < Max1 then
      1
    else if x < Max2 then
      2
    else if x < Max3 then
      3
    else if x < Max4 then
      4
    else
      5
  }

  function DecodeLength(x : uint8) : (ret : MyLen)
  {
    if x < Tag2 then
      1
    else if x < Tag3 then
      2
    else if x < Tag4 then
      3
    else if x < Tag5 then
      4
    else
      5
  }

  function Encode1(x : uint32)
    : (ret : seq<uint8>)
    requires x < Max1
    ensures |ret| == 1
    ensures EncodeLength(x) == 1
    ensures DecodeLength(ret[0]) == 1
    ensures ValidEncoding(ret, 1)
  {
    [x as uint8]
  }

  function Encode2(x : uint32)
    : (ret : seq<uint8>)
    requires Max1 <= x < Max2
    ensures |ret| == 2
    ensures EncodeLength(x) == 2
    ensures DecodeLength(ret[0]) == 2
    ensures ValidEncoding(ret, 2)
  {
    var byte1 := (x / 0x100) as uint8;
    var byte2 := (x % 0x100) as uint8;
    [Tag2 + byte1, byte2]
  }

  function Encode3(x : uint32)
    : (ret : seq<uint8>)
    requires Max2 <= x < Max3
    ensures |ret| == 3
    ensures EncodeLength(x) == 3
    ensures DecodeLength(ret[0]) == 3
    ensures ValidEncoding(ret, 3)
  {
    var byte1 := (x / 0x10000) as uint8;
    var byte2 := ((x % 0x10000) / 0x100) as uint8;
    var byte3 := (x % 0x100) as uint8;
    [Tag3 + byte1, byte2, byte3]
  }

  function Encode4(x : uint32)
    : (ret : seq<uint8>)
    requires Max3 <= x < Max4
    ensures |ret| == 4
    ensures EncodeLength(x) == 4
    ensures DecodeLength(ret[0]) == 4
    ensures ValidEncoding(ret, 4)
  {
    var byte1 := (x / 0x1000000) as uint8;
    var byte2 := ((x % 0x1000000) / 0x10000) as uint8;
    var byte3 := ((x % 0x10000) / 0x100) as uint8;
    var byte4 := (x % 0x100) as uint8;
    [Tag4 + byte1, byte2, byte3, byte4]
  }

  function Encode5(x : uint32)
    : (ret : seq<uint8>)
    requires Max4 <= x
    ensures |ret| == 5
    ensures EncodeLength(x) == 5
    ensures DecodeLength(ret[0]) == 5
    ensures ValidEncoding(ret, 5)
  {
    var byte2 := (x / 0x1000000) as uint8;
    var byte3 := ((x % 0x1000000) / 0x10000) as uint8;
    var byte4 := ((x % 0x10000) / 0x100) as uint8;
    var byte5 := (x % 0x100) as uint8;
    [Tag5, byte2, byte3, byte4, byte5]
  }

  function Encode(x : uint32)
    : (ret : seq<uint8>)
    ensures |ret| == EncodeLength(x) as nat
    ensures |ret| == DecodeLength(ret[0]) as nat
    ensures ValidEncoding(ret, DecodeLength(ret[0]))
  {
    var len := EncodeLength(x);
    match len {
      case 1 => Encode1(x)
      case 2 => Encode2(x)
      case 3 => Encode3(x)
      case 4 => Encode4(x)
      case 5 => Encode5(x)
    }
  }

  lemma {:vcs_split_on_every_assert} DecodeRoundTrip(x: uint32, s: seq<uint8>, len: MyLen)
    requires len as int == |s|
    requires len == EncodeLength(x) == DecodeLength(s[0])
    requires ValidEncoding(s, DecodeLength(s[0]))
    requires Decode(s, len) == x
    ensures Encode(x) == s
  {
    match len {
      case 1 => assert Encode1(x) == s;
      case 2 => assert Encode2(x) == s;
      case 3 => assert Encode3(x) == s;
      case 4 => assert Encode4(x) == s;
      case 5 => assert Encode5(x) == s;
    }
  }

  lemma {:vcs_split_on_every_assert} EncodeRoundTrip(x: uint32, s: seq<uint8>, len: MyLen)
    requires len as int == |s|
    requires len == EncodeLength(x) == DecodeLength(s[0])
    requires ValidEncoding(s, DecodeLength(s[0]))
    requires Encode(x) == s
    ensures Decode(s, len) == x
  {
    match len {
      case 1 => assert Decode1(s) == x;
      case 2 => assert Decode2(s) == x;
      case 3 => assert Decode3(s) == x;
      case 4 => assert Decode4(s) == x;
      case 5 => assert Decode5(s) == x;
    }
  }

  function DecodeRead(
    buffer: ReadableBuffer
  ):
    (res: ReadCorrect<uint32>)
    ensures CorrectlyRead(buffer, res, Encode)
  {
    :- Need(buffer.start < |buffer.bytes|, MoreNeeded(1));
    var len := DecodeLength(buffer.bytes[buffer.start]);
    var SuccessfulRead(data, tail) :- Read(buffer, len as int);
    CorrectlyReadByteRange(buffer, tail, data);

    :- Need(ValidEncoding(data, len), Error( message := "encoding error" ));

    var num := Decode(data, len);

    assert CorrectlyReadRange(
        buffer,
        tail,
        Encode(num)
      ) by {
      reveal CorrectlyReadRange();
      assume len == 4;
      assert 0x200000 <= num < 0x10000000;
      assert data[0] < 0xf0;
      
      assume false;
      // assume data == Encode(num);
    }

    Success(SuccessfulRead(
              num,
              tail
            ))
  }

  function Decode1(x : seq<uint8>) : (ret : uint32)
    requires |x| == 1
    requires x[0] < Tag2
    requires DecodeLength(x[0]) == 1
    requires ValidEncoding(x, 1)
    ensures EncodeLength(ret) == 1
  {
    x[0] as uint32
  }

  function Decode2(x : seq<uint8>) : (ret : uint32)
    requires |x| == 2
    requires Tag2 <= x[0] < Tag3
    requires DecodeLength(x[0]) == 2
    requires ValidEncoding(x, 2)
    ensures EncodeLength(ret) == 2
  {
        (x[0] % 0x80) as uint32 * 0x100
      + x[1] as uint32
  }

  function Decode3(x : seq<uint8>) : (ret : uint32)
    requires |x| == 3
    requires Tag3 <= x[0] < Tag4
    requires DecodeLength(x[0]) == 3
    requires ValidEncoding(x, 3)
    ensures EncodeLength(ret) == 3
  {
    (x[0] % 0xc0) as uint32 * 0x10000
    + x[1] as uint32 * 0x100
    + x[2] as uint32
  }

  function Decode4(x : seq<uint8>) : (ret : uint32)
    requires |x| == 4
    requires Tag4 <= x[0] < Tag5
    requires DecodeLength(x[0]) == 4
    requires ValidEncoding(x, 4)
    ensures EncodeLength(ret) == 4
  {
    (x[0] % 0xe0) as uint32 * 0x1000000
      + x[1] as uint32 * 0x10000
      + x[2] as uint32 * 0x100
      + x[3] as uint32
  }

  function Decode5(x : seq<uint8>) : (ret : uint32)
    requires |x| == 5
    requires Tag5 <= x[0] < Tag6
    requires ValidEncoding(x, 5)
    requires DecodeLength(x[0]) == 5
    ensures EncodeLength(ret) == 5
  {
      x[1] as uint32 * 0x1000000
      + x[2] as uint32 * 0x10000
      + x[3] as uint32 * 0x100
      + x[4] as uint32
  }

  function Decode(x : seq<uint8>, len: MyLen)
    : (ret : uint32)
    requires len as int == |x|
    requires DecodeLength(x[0]) == len
    requires ValidEncoding(x, len)
    ensures EncodeLength(ret) == DecodeLength(x[0])
  {
    match len {
      case 1 => Decode1(x)
      case 2 => Decode2(x)
      case 3 => Decode3(x)
      case 4 => Decode4(x)
      case 5 => Decode5(x)
    }
  }
}