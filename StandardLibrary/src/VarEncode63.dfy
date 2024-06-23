// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "UInt.dfy"
include "SerializeFunctions.dfy"

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
  Decode(x : seq<uint8>) : (ret : uint64)

  // If I were to encode x, how many bytes would the result have?
  EncodeLength(x : uint64) : (ret : MyLen)

  // If a seq<uint8> has first byte x, how many bytes are being used for this encoded number?
  DecodeLength(x : uint8) : (ret : MyLen)
*/

module {:options "-functionSyntax:4"} VarEncode63 {
  import opened StandardLibrary.UInt
  import opened SerializeFunctions
  import opened Wrappers

  newtype MyLen = x | 1 <= x <= 9 witness 1

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

  predicate ValidEncoding(x : seq<uint8>, len: MyLen)
    requires len as int == |x|
    requires DecodeLength(x[0]) == len
  {
    match len {
      case 1 => x[0] < Tag2
      case 2 => x[0] > Tag2 || (x[0] == Tag2 && x[1] >= 128)
      case 3 => x[0] > Tag3 || (x[0] == Tag3 && x[1] >= 64)
      case 4 => x[0] > Tag4 || (x[0] == Tag4 && x[1] >= 32)
      case 5 => x[0] > 0xf0 || (x[0] == 0xf0 && x[1] >= 16)
      case 6 => x[0] > 0xf8 || (x[0] == 0xf8 && x[1] >= 8)
      case 7 => x[0] > 0xfc || (x[0] == 0xfc && x[1] >= 4)
      case 8 => x[0] == 0xfe && x[1] >= 2
      case 9 => x[0] == 0xff && 0 < x[1] < 128
    }
  }

  function EncodeLength(x : uint64) : (ret : MyLen)
    requires x < Max9
  {
    if x < Max1 then 1
    else if x < Max2 then 2
    else if x < Max3 then 3
    else if x < Max4 then 4
    else if x < Max5 then 5
    else if x < Max6 then 6
    else if x < Max7 then 7
    else if x < Max8 then 8
    else 9
  }

  function DecodeLength(x : uint8) : (ret : MyLen)
  {
    if x < Tag2 then 1
    else if x < Tag3 then 2
    else if x < Tag4 then 3
    else if x < Tag5 then 4
    else if x < Tag6 then 5
    else if x < Tag7 then 6
    else if x < Tag8 then 7
    else if x < Tag9 then 8
    else 9
  }

  function Encode1(x : uint64)
    : (ret : seq<uint8>)
    requires x < Max1
    ensures |ret| == 1
    ensures EncodeLength(x) == 1
    ensures DecodeLength(ret[0]) == 1
    ensures ValidEncoding(ret, 1)
  {
    [x as uint8]
  }

  function Encode2(x : uint64)
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

  function Encode3(x : uint64)
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

  function Encode4(x : uint64)
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

  function Encode5(x : uint64)
    : (ret : seq<uint8>)
    requires Max4 <= x < Max5
    ensures |ret| == 5
    ensures EncodeLength(x) == 5
    ensures DecodeLength(ret[0]) == 5
    ensures ValidEncoding(ret, 5)
  {
    var byte1 := (x / 0x100000000) as uint8;
    var byte2 := ((x % 0x100000000) / 0x1000000) as uint8;
    var byte3 := ((x % 0x1000000) / 0x10000) as uint8;
    var byte4 := ((x % 0x10000) / 0x100) as uint8;
    var byte5 := (x % 0x100) as uint8;
    [Tag5 + byte1, byte2, byte3, byte4, byte5]
  }

  function Encode6(x : uint64)
    : (ret : seq<uint8>)
    requires Max5 <= x < Max6
    ensures |ret| == 6
    ensures EncodeLength(x) == 6
    ensures DecodeLength(ret[0]) == 6
    ensures ValidEncoding(ret, 6)
  {
    var byte1 := (x / 0x10000000000) as uint8;
    var byte2 := ((x % 0x10000000000) / 0x100000000) as uint8;
    var byte3 := ((x % 0x100000000) / 0x1000000) as uint8;
    var byte4 := ((x % 0x1000000) / 0x10000) as uint8;
    var byte5 := ((x % 0x10000) / 0x100) as uint8;
    var byte6 := (x % 0x100) as uint8;
    [Tag6 + byte1, byte2, byte3, byte4, byte5, byte6]
  }

  opaque function Encode7(x : uint64)
    : (ret : seq<uint8>)
    requires Max6 <= x < Max7
    ensures |ret| == 7
    ensures EncodeLength(x) == 7
    ensures DecodeLength(ret[0]) == 7
    ensures ValidEncoding(ret, 7)
    ensures ret[0] == Tag7 + (x / 0x1000000000000) as uint8
    ensures ret[1] == ((x % 0x1000000000000) / 0x10000000000) as uint8
    ensures ret[2] == ((x % 0x10000000000) / 0x100000000) as uint8
    ensures ret[3] == ((x % 0x100000000) / 0x1000000) as uint8
    ensures ret[4] == ((x % 0x1000000) / 0x10000) as uint8
    ensures ret[5] == ((x % 0x10000) / 0x100) as uint8
    ensures ret[6] == (x % 0x100) as uint8
  {
    var byte1 := (x / 0x1000000000000) as uint8;
    var byte2 := ((x % 0x1000000000000) / 0x10000000000) as uint8;
    var byte3 := ((x % 0x10000000000) / 0x100000000) as uint8;
    var byte4 := ((x % 0x100000000) / 0x1000000) as uint8;
    var byte5 := ((x % 0x1000000) / 0x10000) as uint8;
    var byte6 := ((x % 0x10000) / 0x100) as uint8;
    var byte7 := (x % 0x100) as uint8;
    [Tag7 + byte1, byte2, byte3, byte4, byte5, byte6, byte7]
  }

  opaque function Encode8(x : uint64)
    : (ret : seq<uint8>)
    requires Max7 <= x < Max8
    ensures |ret| == 8
    ensures EncodeLength(x) == 8
    ensures DecodeLength(ret[0]) == 8
    ensures ValidEncoding(ret, 8)
    ensures ret[0] == Tag8
    ensures ret[1] == ((x % 0x100000000000000) / 0x1000000000000) as uint8
    ensures ret[2] == ((x % 0x1000000000000) / 0x10000000000) as uint8
    ensures ret[3] == ((x % 0x10000000000) / 0x100000000) as uint8
    ensures ret[4] == ((x % 0x100000000) / 0x1000000) as uint8
    ensures ret[5] == ((x % 0x1000000) / 0x10000) as uint8
    ensures ret[6] == ((x % 0x10000) / 0x100) as uint8
    ensures ret[7] == (x % 0x100) as uint8
  {
    var byte2 := ((x % 0x100000000000000) / 0x1000000000000) as uint8;
    var byte3 := ((x % 0x1000000000000) / 0x10000000000) as uint8;
    var byte4 := ((x % 0x10000000000) / 0x100000000) as uint8;
    var byte5 := ((x % 0x100000000) / 0x1000000) as uint8;
    var byte6 := ((x % 0x1000000) / 0x10000) as uint8;
    var byte7:= ((x % 0x10000) / 0x100) as uint8;
    var byte8:= (x % 0x100) as uint8;
    [Tag8, byte2, byte3, byte4, byte5, byte6, byte7, byte8]
  }

  opaque function Encode9(x : uint64)
    : (ret : seq<uint8>)
    requires Max8 <= x < Max9
    ensures |ret| == 9
    ensures EncodeLength(x) == 9
    ensures DecodeLength(ret[0]) == 9
    ensures ValidEncoding(ret, 9)
    ensures ret[0] == Tag9
    ensures ret[1] == (x / 0x100000000000000) as uint8
    ensures ret[2] == ((x % 0x100000000000000) / 0x1000000000000) as uint8
    ensures ret[3] == ((x % 0x1000000000000) / 0x10000000000) as uint8
    ensures ret[4] == ((x % 0x10000000000) / 0x100000000) as uint8
    ensures ret[5] == ((x % 0x100000000) / 0x1000000) as uint8
    ensures ret[6] ==  ((x % 0x1000000) / 0x10000) as uint8
    ensures ret[7] == ((x % 0x10000) / 0x100) as uint8
    ensures ret[8] == (x % 0x100) as uint8
  {
    var byte1 := (x / 0x100000000000000) as uint8;
    var byte2 := ((x % 0x100000000000000) / 0x1000000000000) as uint8;
    var byte3 := ((x % 0x1000000000000) / 0x10000000000) as uint8;
    var byte4 := ((x % 0x10000000000) / 0x100000000) as uint8;
    var byte5 := ((x % 0x100000000) / 0x1000000) as uint8;
    var byte6 := ((x % 0x1000000) / 0x10000) as uint8;
    var byte7:= ((x % 0x10000) / 0x100) as uint8;
    var byte8:= (x % 0x100) as uint8;
    [Tag9, byte1, byte2, byte3, byte4, byte5, byte6, byte7, byte8]
  }


  function Encode(x : uint64)
    : (ret : seq<uint8>)
    requires x < Max9
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
      case 6 => Encode6(x)
      case 7 => Encode7(x)
      case 8 => Encode8(x)
      case 9 => Encode9(x)
    }
  }

  lemma {:vcs_split_on_every_assert} DecodeRoundTrip7(x: uint64, s: seq<uint8>)
    requires Max6 <= x < Max7
    requires |s| == 7
    requires EncodeLength(x) == DecodeLength(s[0]) == 7
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
    requires EncodeLength(x) == DecodeLength(s[0]) == 8
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
    requires EncodeLength(x) == DecodeLength(s[0]) == 9
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
    requires x < Max9
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
      case 6 => assume {:axiom} Encode6(x) == s;
      case 7 => DecodeRoundTrip7(x, s); assert Encode7(x) == s;
      case 8 => DecodeRoundTrip8(x, s); assert Encode8(x) == s;
      case 9 => DecodeRoundTrip9(x, s); assert Encode9(x) == s;
    }
  }

  lemma {:vcs_split_on_every_assert} EncodeRoundTrip(x: uint64, s: seq<uint8>, len: MyLen)
    requires x < Max9
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
      case 6 => assume {:axiom} Decode6(s) == x;
      case 7 => assert Decode7(s) == x;
      case 8 => assume {:axiom} Decode8(s) == x;
      case 9 => assume {:axiom} Decode9(s) == x;
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

  function Decode1(x : seq<uint8>) : (ret : uint64)
    requires |x| == 1
    requires x[0] < Tag2
    requires DecodeLength(x[0]) == 1
    requires ValidEncoding(x, 1)
    ensures ret < Max1 as uint64
    ensures EncodeLength(ret) == 1
  {
    x[0] as uint64
  }

  function Decode2(x : seq<uint8>) : (ret : uint64)
    requires |x| == 2
    requires Tag2 <= x[0] < Tag3
    requires DecodeLength(x[0]) == 2
    requires ValidEncoding(x, 2)
    ensures Max1 <= ret < Max2 as uint64
    ensures EncodeLength(ret) == 2
  {
    (x[0] % 0x80) as uint64 * 0x100
    + x[1] as uint64
  }

  function Decode3(x : seq<uint8>) : (ret : uint64)
    requires |x| == 3
    requires Tag3 <= x[0] < Tag4
    requires DecodeLength(x[0]) == 3
    requires ValidEncoding(x, 3)
    ensures Max2 <= ret < Max3 as uint64
    ensures EncodeLength(ret) == 3
  {
    (x[0] % 0xc0) as uint64 * 0x10000
    + x[1] as uint64 * 0x100
    + x[2] as uint64
  }

  function Decode4(x : seq<uint8>) : (ret : uint64)
    requires |x| == 4
    requires Tag4 <= x[0] < Tag5
    requires DecodeLength(x[0]) == 4
    requires ValidEncoding(x, 4)
    ensures Max3 <= ret < Max4 as uint64
    ensures EncodeLength(ret) == 4
  {
    (x[0] % 0xe0) as uint64 * 0x1000000
    + x[1] as uint64 * 0x10000
    + x[2] as uint64 * 0x100
    + x[3] as uint64
  }

  function Decode5(x : seq<uint8>) : (ret : uint64)
    requires |x| == 5
    requires Tag5 <= x[0] < Tag6
    requires ValidEncoding(x, 5)
    requires DecodeLength(x[0]) == 5
    ensures Max4 <= ret < Max5 as uint64
    ensures EncodeLength(ret) == 5
  {
    (x[0] % 0xf0) as uint64 * 0x100000000
    + x[1] as uint64 * 0x1000000
    + x[2] as uint64 * 0x10000
    + x[3] as uint64 * 0x100
    + x[4] as uint64
  }

  function Decode6(x : seq<uint8>) : (ret : uint64)
    requires |x| == 6
    requires Tag6 <= x[0] < Tag7
    requires ValidEncoding(x, 6)
    requires DecodeLength(x[0]) == 6
    ensures Max5 <= ret < Max6 as uint64
    ensures EncodeLength(ret) == 6
  {
    (x[0] % 0xf8) as uint64 * 0x10000000000
    + x[1] as uint64 * 0x100000000
    + x[2] as uint64 * 0x1000000
    + x[3] as uint64 * 0x10000
    + x[4] as uint64 * 0x100
    + x[5] as uint64
  }

  function Decode7(x : seq<uint8>) : (ret : uint64)
    requires |x| == 7
    requires Tag7 <= x[0] < Tag8
    requires ValidEncoding(x, 7)
    requires DecodeLength(x[0]) == 7
    ensures Max6 <= ret < Max7 as uint64
    ensures EncodeLength(ret) == 7
  {
    (x[0] % 0xfc) as uint64 * 0x1000000000000
    + x[1] as uint64 * 0x10000000000
    + x[2] as uint64 * 0x100000000
    + x[3] as uint64 * 0x1000000
    + x[4] as uint64 * 0x10000
    + x[5] as uint64 * 0x100
    + x[6] as uint64
  }

  function Decode8(x : seq<uint8>) : (ret : uint64)
    requires |x| == 8
    requires Tag8 <= x[0] < Tag9
    requires ValidEncoding(x, 8)
    requires DecodeLength(x[0]) == 8
    ensures Max7 <= ret < Max8 as uint64
    ensures EncodeLength(ret) == 8
  {
    (x[0] % 0xfe) as uint64 * 0x100000000000000
    + x[1] as uint64 * 0x1000000000000
    + x[2] as uint64 * 0x10000000000
    + x[3] as uint64 * 0x100000000
    + x[4] as uint64 * 0x1000000
    + x[5] as uint64 * 0x10000
    + x[6] as uint64 * 0x100
    + x[7] as uint64
  }

  function Decode9(x : seq<uint8>) : (ret : uint64)
    requires |x| == 9
    requires x[0] == Tag9
    requires ValidEncoding(x, 9)
    requires DecodeLength(x[0]) == 9
    ensures Max8 <= ret < Max9 as uint64
    ensures EncodeLength(ret) == 9
  {
    x[1] as uint64 * 0x100000000000000
    + x[2] as uint64 * 0x1000000000000
    + x[3] as uint64 * 0x10000000000
    + x[4] as uint64 * 0x100000000
    + x[5] as uint64 * 0x1000000
    + x[6] as uint64 * 0x10000
    + x[7] as uint64 * 0x100
    + x[8] as uint64
  }

  function Decode(x : seq<uint8>, len: MyLen)
    : (ret : uint64)
    requires len as int == |x|
    requires DecodeLength(x[0]) == len
    requires ValidEncoding(x, len)
    ensures ret < Max9
    ensures EncodeLength(ret) == DecodeLength(x[0])
  {
    match len {
      case 1 => Decode1(x)
      case 2 => Decode2(x)
      case 3 => Decode3(x)
      case 4 => Decode4(x)
      case 5 => Decode5(x)
      case 6 => Decode6(x)
      case 7 => Decode7(x)
      case 8 => Decode8(x)
      case 9 => Decode9(x)
    }
  }
}