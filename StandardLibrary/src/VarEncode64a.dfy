// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "UInt.dfy"
  // include "SerializeFunctions.dfy"

/*
  Converts unsigned numbers into variable length seq<uint8>
  Seven bits per byte used to store actual data.

  // Type for the encoded length
  newtype MyLen = x | 1 <= x <= 10 witness 1

  // checks for the very small number of invalid encoding sequences
  predicate ValidEncoding(x : seq<uint8>)

  // convert uint64 to seq<uint8>
  Encode(x : uint64) : (ret : seq<uint8>)

  // convert seq<uint8> to uint64
  Decode(s : seq<uint8>) : (ret : uint64)

  // If I were to encode x, how many bytes would the result have?
  EncodeLength(x : uint64) : (ret : MyLen)

  // If a seq<uint8> has first byte x, how many bytes are being used for this encoded number?
  DecodeLength(x : uint8) : (ret : MyLen)

  // And lemmas to prove round trip stability
  lemma DecodeRoundTrip(x: uint32, s: seq<uint8>, len: MyLen)
      requires Decode(s, len) == x
      ensures Encode(x) == s

  lemma EncodeRoundTrip(x: uint32, s: seq<uint8>, len: MyLen)
    requires Encode(x) == s
    ensures Decode(s, len) == x
*/

module {:options "-functionSyntax:4"} VarEncode64a {
  import opened StandardLibrary.UInt
    // import opened SerializeFunctions
    // import opened Wrappers

  const MaxLen : uint8 := 10
  newtype MyLen = x | 1 <= x <= MaxLen witness 1

  const Max1 : uint64 := 0x80
  const Max2 : uint64 := 0x4000
  const Max3 : uint64 := 0x200000
  const Max4 : uint64 := 0x10000000
  const Max5 : uint64 := 0x800000000
  const Max6 : uint64 := 0x40000000000
  const Max7 : uint64 := 0x2000000000000
  const Max8 : uint64 := 0x100000000000000
  const Max9 : uint64 := 0x8000000000000000

  const Tag2 : uint8 := 0x80
  const Tag3 : uint8 := 0xc0
  const Tag4 : uint8 := 0xe0
  const Tag5 : uint8 := 0xf0
  const Tag6 : uint8 := 0xf8
  const Tag7 : uint8 := 0xfc
  const Tag8 : uint8 := 0xfe
  const Tag9 : uint8 := 0xff
  const Tag10 : uint8 := 0x80

  predicate MaybeValidEncoding(s : seq<uint8>)
    requires 0 < |s|
  {
    if s[0] == 0xff then
      1 < |s|
    else
      true
  }

  predicate ValidEncoding(s : seq<uint8>, len: MyLen)
    requires len as int == |s|
    requires MaybeValidEncoding(s)
    requires DecodeLength(s) == len
  {
    match len {
      case 1 => s[0] < Tag2
      case 2 => s[0] > Tag2 || (s[0] == Tag2 && s[1] >= 128)
      case 3 => s[0] > Tag3 || (s[0] == Tag3 && s[1] >= 64)
      case 4 => s[0] > Tag4 || (s[0] == Tag4 && s[1] >= 32)
      case 5 => s[0] > 0xf0 || (s[0] == 0xf0 && s[1] >= 16)
      case 6 => s[0] > 0xf8 || (s[0] == 0xf8 && s[1] >= 8)
      case 7 => s[0] > 0xfc || (s[0] == 0xfc && s[1] >= 4)
      case 8 => s[0] == 0xfe && s[1] >= 2
      case 9 => s[0] == 0xff && 0 < s[1] < Tag2
      case 10 => s[0] == 0xff && s[1] == Tag2 && Tag2 <= s[2]
    }
  }

  function EncodeLength(x : uint64) : (ret : MyLen)
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

  function DecodeLength1(x : uint8) : (ret : MyLen)
    requires x != 0xff
  {
    if x < Tag2 then 1
    else if x < Tag3 then 2
    else if x < Tag4 then 3
    else if x < Tag5 then 4
    else if x < Tag6 then 5
    else if x < Tag7 then 6
    else if x < Tag8 then 7
    else 8
  }

  // byte2, given that byte1 was 0xff
  function DecodeLength2(x : uint8) : (ret : MyLen)
  {
    if x < Tag10 then 9
    else 10
  }

  function DecodeLength(s : seq<uint8>) : (ret : MyLen)
    requires 0 < |s|
    requires MaybeValidEncoding(s)
  {
    if s[0] == 0xff then
      DecodeLength2(s[1])
    else
      DecodeLength1(s[0])
  }


  function Encode1(x : uint64)
    : (ret : seq<uint8>)
    requires x < Max1
    ensures |ret| == 1
    ensures EncodeLength(x) == 1
    ensures MaybeValidEncoding(ret)
    ensures DecodeLength(ret) == 1
    ensures ValidEncoding(ret, 1)
  {
    Scatter(1, 0, x, [])
  }

  function Encode2(x : uint64)
    : (ret : seq<uint8>)
    requires Max1 <= x < Max2
    ensures |ret| == 2
    ensures EncodeLength(x) == 2
    ensures ret[0] == Tag2 + (x / 0x100) as uint8
    ensures ret[1] == (x % 0x100) as uint8
    ensures DecodeLength(ret) == 2
    ensures ValidEncoding(ret, 2)
  {
    Scatter(2, Tag2, x, [])
  }

  function Encode3(x : uint64)
    : (ret : seq<uint8>)
    requires Max2 <= x < Max3
    ensures |ret| == 3
    ensures EncodeLength(x) == 3
    ensures DecodeLength(ret) == 3
    ensures ValidEncoding(ret, 3)
  {
    Scatter(3, Tag3, x, [])
  }

  function Encode4(x : uint64)
    : (ret : seq<uint8>)
    requires Max3 <= x < Max4
    ensures |ret| == 4
    ensures EncodeLength(x) == 4
    ensures DecodeLength(ret) == 4
    ensures ValidEncoding(ret, 4)
  {
    Scatter(4, Tag4, x, [])
  }

  function Encode5(x : uint64)
    : (ret : seq<uint8>)
    requires Max4 <= x < Max5
    ensures |ret| == 5
    ensures EncodeLength(x) == 5
    ensures DecodeLength(ret) == 5
    ensures ValidEncoding(ret, 5)
  {
    Scatter(5, Tag5, x, [])
  }

  function Encode6(x : uint64)
    : (ret : seq<uint8>)
    requires Max5 <= x < Max6
    ensures |ret| == 6
    ensures EncodeLength(x) == 6
    ensures DecodeLength(ret) == 6
    ensures ValidEncoding(ret, 6)
  {
    Scatter(6, Tag6, x, [])
  }

  function Encode7(x : uint64)
    : (ret : seq<uint8>)
    requires Max6 <= x < Max7
    ensures |ret| == 7
    ensures EncodeLength(x) == 7
    ensures DecodeLength(ret) == 7
    ensures ValidEncoding(ret, 7)
  {
    Scatter(7, Tag7, x, [])
  }

  function Encode8(x : uint64)
    : (ret : seq<uint8>)
    requires Max7 <= x < Max8
    ensures |ret| == 8
    ensures EncodeLength(x) == 8
    ensures DecodeLength(ret) == 8
    ensures ValidEncoding(ret, 8)
  {
    Scatter(8, Tag8, x, [])
  }

  function Encode9(x : uint64)
    : (ret : seq<uint8>)
    requires Max8 <= x < Max9
    ensures |ret| == 9
    ensures EncodeLength(x) == 9
    ensures DecodeLength(ret) == 9
    ensures ValidEncoding(ret, 9)
  {
    [Tag9] + Scatter(8, 0, x, [])
  }

  function Encode10(x : uint64)
    : (ret : seq<uint8>)
    requires Max9 <= x
    ensures |ret| == 10
    ensures EncodeLength(x) == 10
    ensures DecodeLength(ret) == 10
    ensures ValidEncoding(ret, 10)
  {
    [Tag9, Tag2] + Scatter(8, 0, x, [])
  }


  function Encode(x : uint64)
    : (ret : seq<uint8>)
    ensures |ret| == EncodeLength(x) as nat
    ensures MaybeValidEncoding(ret)
    ensures |ret| == DecodeLength(ret) as nat
    ensures ValidEncoding(ret, DecodeLength(ret))
  {
    var len := EncodeLength(x);
    match len {
      case 1 => Encode1(x)
      case 2 => Encode2(x)
      case 3 => Encode3(x)
      case 4 => Encode4(x)
      case 5 => Encode5(x)
      case 6 => Encode6(x)
      case 7 => Encode7(x)
      case 8 => Encode8(x)
      case 9 => Encode9(x)
      case 10 => Encode10(x)
    }
  }

  lemma {:vcs_split_on_every_assert} DecodeRoundTrip7(x: uint64, s: seq<uint8>)
    requires Max6 <= x < Max7
    requires |s| == 7
    requires EncodeLength(x) == DecodeLength(s) == 7
    requires ValidEncoding(s, 7)
    requires Decode7(s) == x
    requires Decode(s, 7) == x
    ensures Encode(x) == s
  {
    assert s[0] == Tag7 + (x / 0x1000000000000) as uint8;
    assert s[1] == ((x % 0x1000000000000) / 0x10000000000) as uint8;
    assume {:axiom} s[2] == ((x % 0x10000000000) / 0x100000000) as uint8;
    assert s[3] == ((x % 0x100000000) / 0x1000000) as uint8;
    assert s[4] == ((x % 0x1000000) / 0x10000) as uint8;
    assert s[5] == ((x % 0x10000) / 0x100) as uint8;
    assert s[6] == (x % 0x100) as uint8;
  }

  lemma {:vcs_split_on_every_assert} DecodeRoundTrip8(x: uint64, s: seq<uint8>)
    requires Max7 <= x < Max8
    requires |s| == 8
    requires EncodeLength(x) == DecodeLength(s) == 8
    requires ValidEncoding(s, 8)
    requires Decode8(s) == x
    requires Decode(s, 8) == x
    ensures Encode(x) == s
  {
    assert s[0] == 0xfe;
    assert s[1] == ((x % 0x100000000000000) / 0x1000000000000) as uint8;
    assert s[2] == ((x % 0x1000000000000) / 0x10000000000) as uint8;
    assert s[3] == ((x % 0x10000000000) / 0x100000000) as uint8;
    assert s[4] == ((x % 0x100000000) / 0x1000000) as uint8;
    assert s[5] == ((x % 0x1000000) / 0x10000) as uint8;
    assert s[6] ==((x % 0x10000) / 0x100) as uint8;
    assert s[7] ==(x % 0x100) as uint8;
  }

  lemma {:vcs_split_on_every_assert} DecodeRoundTrip9(x: uint64, s: seq<uint8>)
    requires Max8 <= x < Max9
    requires |s| == 9
    requires EncodeLength(x) == DecodeLength(s) == 9
    requires ValidEncoding(s, 9)
    requires Decode9(s) == x
    requires Decode(s, 9) == x
    ensures Encode(x) == s
  {
    assert s[0] == 0xff;
    assert s[1] == (x / 0x100000000000000) as uint8;
    assert s[2] == ((x % 0x100000000000000) / 0x1000000000000) as uint8;
    assume {:axiom} s[3] == ((x % 0x1000000000000) / 0x10000000000) as uint8;
    assert s[4] == ((x % 0x10000000000) / 0x100000000) as uint8;
    assert s[5] == ((x % 0x100000000) / 0x1000000) as uint8;
    assert s[6] == ((x % 0x1000000) / 0x10000) as uint8;
    assert s[7] == ((x % 0x10000) / 0x100) as uint8;
    assert s[8] == (x % 0x100) as uint8;
  }

  lemma {:vcs_split_on_every_assert} DecodeRoundTrip(x: uint64, s: seq<uint8>, len: MyLen)
    requires len as int == |s|
    requires MaybeValidEncoding(s)
    requires len == EncodeLength(x) == DecodeLength(s)
    requires ValidEncoding(s, DecodeLength(s))
    requires Decode(s, len) == x
    ensures Encode(x) == s
  {
    match len {
      case 1 => assert Encode1(x) == s;
      case 2 => assert Encode2(x) == s;
      case 3 => assert Encode3(x) == s;
      case 4 => assert Encode4(x) == s;
      case 5 => assert Encode5(x) == s;
      case 6 => assume {:axiom} Encode6(x) == s;
      case 7 => DecodeRoundTrip7(x, s); assert Encode7(x) == s;
      case 8 => DecodeRoundTrip8(x, s); assert Encode8(x) == s;
      case 9 => DecodeRoundTrip9(x, s); assert Encode9(x) == s;
      case 10 => assert Encode10(x) == s;
    }
  }

  lemma {:vcs_split_on_every_assert} EncodeRoundTrip(x: uint64, s: seq<uint8>, len: MyLen)
    requires len as int == |s|
    requires MaybeValidEncoding(s)
    requires len == EncodeLength(x) == DecodeLength(s)
    requires ValidEncoding(s, DecodeLength(s))
    requires Encode(x) == s
    ensures Decode(s, len) == x
  {
    match len {
      case 1 => assert Decode1(s) == x;
      case 2 => assert Decode2(s) == x;
      case 3 => assert Decode3(s) == x;
      case 4 => assert Decode4(s) == x;
      case 5 => assert Decode5(s) == x;
      case 6 => assume {:axiom} Decode6(s) == x;
      case 7 => assert Decode7(s) == x;
      case 8 => assume {:axiom} Decode8(s) == x;
      case 9 => assume {:axiom} Decode9(s) == x;
      case 10 => assume {:axiom} Decode10(s) == x;
    }
  }

  // function DecodeRead(
  //   buffer: ReadableBuffer
  // ):
  //   (res: ReadCorrect<uint64>)
  //   ensures CorrectlyRead(buffer, res, Encode)
  // {
  //   :- Need(buffer.start < |buffer.bytes|, MoreNeeded(1));
  //   var len := DecodeLength(buffer.bytes[buffer.start]);
  //   var SuccessfulRead(data, tail) :- Read(buffer, len);
  //   CorrectlyReadByteRange(buffer, tail, data);

  //   :- Need(ValidEncoding(data, len), Error( message := "encoding error" ));

  //   var num := Decode(data, len);

  //   assert CorrectlyReadRange(
  //       buffer,
  //       tail,
  //       Encode(num)
  //     ) by {
  //     reveal CorrectlyReadRange();
  //     assume len == 4;
  //     assert 0x200000 <= num < 0x10000000;
  //     assert data[0] < 0xf0;

  //     assume false;
  //     // assume data == Encode(num);
  //   }

  //   Success(SuccessfulRead(
  //             num,
  //             tail
  //           ))
  // }

  function Gather(s : seq<uint8>, acc : uint64) : uint64
  {
    if |s| == 0 then
      acc
    else
      var newVal := (acc as int * 256) + s[0] as int;
      assume {:axiom} newVal as int < UINT64_LIMIT;
      Gather(s[1..], newVal as uint64)
  }

  function Scatter(remaining : MyLen, tag : uint8, val : uint64, acc : seq<uint8>) : (ret : seq<uint8>)
    ensures |ret| == (remaining as int) + |acc|
  {
    if remaining == 1 then
      var newVal := (tag as uint64) + (val % 0x100);
      assume {:axiom} newVal as int < 256;
      [newVal as uint8] + acc
    else
      Scatter(remaining-1, tag, val / 0x100, [(val % 0x100) as uint8] + acc)
  }


  function Decode1(s : seq<uint8>) : (ret : uint64)
    requires |s| == 1
    requires s[0] < Tag2
    requires DecodeLength(s) == 1
    requires ValidEncoding(s, 1)
    ensures ret < Max1 as uint64
    ensures EncodeLength(ret) == 1
  {
    Gather(s[1..], s[0] as uint64)
  }

  function Decode2(s : seq<uint8>) : (ret : uint64)
    requires |s| == 2
    requires Tag2 <= s[0] < Tag3
    requires DecodeLength(s) == 2
    requires ValidEncoding(s, 2)
    ensures Max1 <= ret < Max2 as uint64
    ensures EncodeLength(ret) == 2
  {
    Gather(s[1..], (s[0] % Tag2) as uint64)
  }

  function Decode3(s : seq<uint8>) : (ret : uint64)
    requires |s| == 3
    requires Tag3 <= s[0] < Tag4
    requires DecodeLength(s) == 3
    requires ValidEncoding(s, 3)
    ensures Max2 <= ret < Max3 as uint64
    ensures EncodeLength(ret) == 3
  {
    Gather(s[1..], (s[0] % Tag3) as uint64)
  }

  function Decode4(s : seq<uint8>) : (ret : uint64)
    requires |s| == 4
    requires Tag4 <= s[0] < Tag5
    requires DecodeLength(s) == 4
    requires ValidEncoding(s, 4)
    ensures Max3 <= ret < Max4 as uint64
    ensures EncodeLength(ret) == 4
  {
    Gather(s[1..], (s[0] % Tag4) as uint64)
  }

  function Decode5(s : seq<uint8>) : (ret : uint64)
    requires |s| == 5
    requires Tag5 <= s[0] < Tag6
    requires ValidEncoding(s, 5)
    requires DecodeLength(s) == 5
    ensures Max4 <= ret < Max5 as uint64
    ensures EncodeLength(ret) == 5
  {
    Gather(s[1..], (s[0] % Tag5) as uint64)
  }

  function Decode6(s : seq<uint8>) : (ret : uint64)
    requires |s| == 6
    requires Tag6 <= s[0] < Tag7
    requires ValidEncoding(s, 6)
    requires DecodeLength(s) == 6
    ensures Max5 <= ret < Max6 as uint64
    ensures EncodeLength(ret) == 6
  {
    Gather(s[1..], (s[0] % Tag6) as uint64)
  }

  function Decode7(s : seq<uint8>) : (ret : uint64)
    requires |s| == 7
    requires Tag7 <= s[0] < Tag8
    requires ValidEncoding(s, 7)
    requires DecodeLength(s) == 7
    ensures Max6 <= ret < Max7 as uint64
    ensures EncodeLength(ret) == 7
  {
    Gather(s[1..], (s[0] % Tag7) as uint64)
  }

  function Decode8(s : seq<uint8>) : (ret : uint64)
    requires |s| == 8
    requires Tag8 <= s[0] < Tag9
    requires ValidEncoding(s, 8)
    requires DecodeLength(s) == 8
    ensures Max7 <= ret < Max8 as uint64
    ensures EncodeLength(ret) == 8
  {
    Gather(s[1..], (s[0] % Tag8) as uint64)
  }

  function Decode9(s : seq<uint8>) : (ret : uint64)
    requires |s| == 9
    requires s[0] == Tag9
    requires MaybeValidEncoding(s)
    requires DecodeLength(s) == 9
    requires ValidEncoding(s, 9)
    ensures Max8 <= ret < Max9 as uint64
    ensures EncodeLength(ret) == 9
  {
    Gather(s[1..], 0)
  }

  function Decode10(s : seq<uint8>) : (ret : uint64)
    requires |s| == 10
    requires s[0] == Tag9
    requires s[1] == Tag2
    requires MaybeValidEncoding(s)
    requires ValidEncoding(s, 10)
    requires DecodeLength(s) == 10
    ensures Max9 <= ret
    ensures EncodeLength(ret) == 10
  {
    Gather(s[2..], 0)
  }

  function Decode(s : seq<uint8>, len: MyLen)
    : (ret : uint64)
    requires len as int == |s|
    requires MaybeValidEncoding(s)
    requires DecodeLength(s) == len
    requires ValidEncoding(s, len)
    ensures EncodeLength(ret) == DecodeLength(s)
  {
    match len {
      case 1 => Decode1(s)
      case 2 => Decode2(s)
      case 3 => Decode3(s)
      case 4 => Decode4(s)
      case 5 => Decode5(s)
      case 6 => Decode6(s)
      case 7 => Decode7(s)
      case 8 => Decode8(s)
      case 9 => Decode9(s)
      case 10 => Decode10(s)
    }
  }
}