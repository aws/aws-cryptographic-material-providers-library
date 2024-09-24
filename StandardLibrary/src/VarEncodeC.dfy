// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "UInt.dfy"
include "SerializeFunctions.dfy"

/*
  Converts unsigned numbers into variable length seq<uint8>
  Seven bits per byte used to store actual data.
*/

module {:options "-functionSyntax:4"} VarEncode {
  import opened StandardLibrary.UInt
  import opened SerializeFunctions
  import opened Wrappers


  function WriteVarEncode64(num: uint64): seq<uint8>
  {
    Encode(num)
  }

  function ReadVarEncode64(
    buffer: ReadableBuffer
  ):
    (res: ReadCorrect<uint64>)
    ensures CorrectlyRead(buffer, res, WriteVarEncode64)
  {
    :- Need(buffer.start < |buffer.bytes|, MoreNeeded(1));
    :- Need(MaybeValidEncoding(buffer.bytes[buffer.start..]), MoreNeeded(1));
    var len := DecodeLength(buffer.bytes[buffer.start..]);
    var SuccessfulRead(data, tail) :- Read(buffer, len as nat);
    CorrectlyReadByteRange(buffer, tail, data);

    :- Need(ValidEncoding(data, len), Error( message := "Var64 encoding error"));

    var num := Decode(data, len);

    reveal CorrectlyReadRange();
    DecodeRoundTrip(num, data, len);

    Success(SuccessfulRead(
              num,
              tail
            ))
  }

  function WriteVarEncode32(num: uint32): seq<uint8>
  {
    Encode(num as uint64)
  }

  const UINT32_MAX: uint64 := BoundedInts.UINT32_MAX as uint64;

  function ReadVarEncode32(
    buffer: ReadableBuffer
  ):
    (res: ReadCorrect<uint32>)
    ensures CorrectlyRead(buffer, res, WriteVarEncode32)
  {
    :- Need(buffer.start < |buffer.bytes|, MoreNeeded(1));
    :- Need(MaybeValidEncoding(buffer.bytes[buffer.start..]), MoreNeeded(1));
    var len := DecodeLength(buffer.bytes[buffer.start..]);
    var SuccessfulRead(data, tail) :- Read(buffer, len as nat);
    CorrectlyReadByteRange(buffer, tail, data);

    :- Need(len <= 6, Error( message := "Var encoding exceeds 32 bytes."));
    :- Need(ValidEncoding(data, len), Error( message := "Var64 encoding error"));

    var num := Decode(data, len);
    :- Need(num <= UINT32_MAX, Error( message := "Var encoding exceeds 32 bytes."));

    reveal CorrectlyReadRange();
    DecodeRoundTrip(num, data, len);

    Success(SuccessfulRead(
              num as uint32,
              tail
            ))
  }

  /*

    Implementation

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

  function Decode(x : seq<uint8>, len: MyLen)
    : (ret : uint64)
    requires len as int == |x|
    requires MaybeValidEncoding(x)
    requires DecodeLength(x) == len
    requires ValidEncoding(x, len)
    ensures EncodeLength(ret) == DecodeLength(x)
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
      case 10 => Decode10(x)
    }
  }

  newtype MyLen = x | 1 <= x <= 10 witness 1

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

  const Tags: seq<seq<uint8>> := [
    [0x80],
    [0xc0],
    [0xe0],
    [0xf0],
    [0xf8],
    [0xfc],
    [0xfe],
    [0xff],
    [0xff, 0x80]
  ]

  predicate MaybeValidEncoding(x : seq<uint8>)
    requires 0 < |x|
  {
    if x[0] == 0xff then
      1 < |x|
    else
      true
  }

  predicate {:only} ValidEncoding(x : seq<uint8>, len: MyLen)
    requires len as int == |x|
    // requires MaybeValidEncoding(x)
    // requires DecodeLength(x) == len
  {
    match len {
      case 1 => x[0] < Tag2
      case 2 => x[0] > Tag2 || (x[0] == Tag2 && x[1] >= 128)
      case 3 => x[0] > Tag3 || (x[0] == Tag3 && x[1] >= 64)
      case 4 => x[0] > Tag4 || (x[0] == Tag4 && x[1] >= 32)
      case 5 => x[0] > Tag5 || (x[0] == Tag5 && x[1] >= 16)
      case 6 => x[0] > Tag6 || (x[0] == Tag6 && x[1] >= 8)
      case 7 => x[0] > Tag7 || (x[0] == Tag7 && x[1] >= 4)
      case 8 => x[0] == 0xfe && x[1] >= 2
      case 9 => x[0] == 0xff && 0 < x[1] < Tag2
      case 10 => x[0] == 0xff && x[1] == Tag2 && Tag2 <= x[2]
    }
  }


  // predicate ValidEncoding222(x : seq<uint8>, len: MyLen)
  //   requires len as int == |x|
  //   requires MaybeValidEncoding(x)
  //   requires DecodeLength(x) == len
  // {
  //   match len {
  //     case 1 => x[0] < Tag2
  //     case 2 => Tag2 < x[0] || (x[0] == Tag2 && 128 <= x[1])
  //     case 3 => Tag3 < x[0] || (x[0] == Tag3 && 64 <= x[1])
  //     case 4 => Tag4 < x[0] || (x[0] == Tag4 && 32 <= x[1])
  //     case 5 => Tag5 < x[0] || (x[0] == Tag5 && 16 <= x[1])
  //     case 6 => Tag6 < x[0] || (x[0] == Tag6 && 8 <= x[1])
  //     case 7 => Tag7 < x[0] || (x[0] == Tag7 && 4 <= x[1])
  //     case 8 => x[0] == 0xfe && 2 <= x[1]
  //     case 9 => x[0] == 0xff && 0 < x[1] < Tag2
  //     case 10 => x[0] == 0xff && x[1] == Tag2 && Tag2 <= x[2]
  //   }
  // }

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

  // byte1, given that byte0 was 0xff
  function DecodeLength2(x : uint8) : (ret : MyLen)
  {
    if x < Tag10 then 9
    else 10
  }

  function DecodeLength(x : seq<uint8>) : (ret : MyLen)
    requires 0 < |x|
    requires MaybeValidEncoding(x)
  {
    if x[0] == 0xff then
      DecodeLength2(x[1])
    else
      DecodeLength1(x[0])
  }

  function {:only} DecodeLength?(s: seq<uint8>, i: nat := 0)
    : (output : Result<MyLen, ReadProblems>)
    decreases |Tags| - i
    ensures output.Success? ==>
    && i < |Tags|
    && output.value as nat == |s|
    && ValidEncoding(s, output.value)
  {
    :- Need(i < |Tags|, Error(message := "Invalid encoding"));
    :- Need(|Tags[i]| < |s|, MoreNeeded(|Tags[i]|));
    if LessThanTag?(s, i) then
      var len := (i + 1) as MyLen;
      :- Need(|s| == len as nat, Error( message := "Invalid encoding"));
      :- Need(ValidEncoding(s, len), Error( message := "Invalid encoding"));
      Success(len as MyLen)
    else
      DecodeLength?(s, i + 1)
  }

  predicate {:only} LessThanTag?(
    s: seq<uint8>,
    i: nat,
    k: nat := 0
  )
    requires i < |Tags|
    requires k < |Tags[i]| < |s|
    decreases |Tags[i]| - k
  {
    if s[k] < Tags[i][k] then
      if k + 1 < |Tags[i]| then
        LessThanTag?(s, i, k + 1)
      else
        true
    else
      false
  }

  // function DecodeLength?(s : seq<uint8>, index: nat := 0)
  //   : (output : Result<nat, string>)

  //   requires index < |s|
  //   decreases |s| - index
  // {
  //   if s[index] < Tag2 then
  //     :- Need(|s| == index + 1, "");
  //     Success(index + 1)
  //   else if s[index] == Tag2 then
  //     :- Need(|s| == index + 2 && s[index + 1] >= 128, "");
  //     Success(index + 2)
  //   else if s[index] < Tag3 then

  //     Success(index + 2)
  //   else if s[index] < Tag4 then
  //     :- Need(|s| == index + 3 && s[index + 1] >= 64, "");
  //     Success(index + 3)
  //   else if s[index] < Tag5 then
  //     :- Need(|s| == index + 5 && s[index + 1] >= 32, "");
  //     Success(4)
  //   else if s[index] < Tag6 then
  //     :- Need(|s| == index + 6 && s[index + 1] >= 16, "");
  //     Success(5)
  //   else if s[index] < Tag7 then
  //     :- Need(|s| == index + 7 && s[index + 1] >= 8, "");
  //     Success(6)
  //   else if s[index] < Tag8 then
  //     :- Need(|s| == index + 8 && s[index + 1] >= 4, "");
  //     Success(7)
  //   else if s[index] < Tag9 then Success(8)
  //   else
  //     assert s[index] == Tag9;
  //     :- Need(index + 1 < |s|, "");
  //     if s[index + 1] < Tag2 then
  //       Success(9)
  //     else
  //       var tail :- DecodeLength?(s, index + 1);
  //       Success(9 + tail)
  // }

  lemma {:only} asdfa(s : seq<uint8>)
    // requires 0 < |s| <= 10
    requires DecodeLength?(s).Success?
    // ensures MaybeValidEncoding(s)

    // requires MaybeValidEncoding(s)
    // requires DecodeLength(s) as nat == |s|
    requires ValidEncoding(s, DecodeLength?(s).value)
    
    ensures DecodeLength?(s).value == DecodeLength(s)
  {
  }


  ghost function Pow(e: nat): (ret: nat)
    decreases e
    ensures 0 < ret
  {
    if e == 0 then
      1
    else
      0x100 * Pow(e - 1)
  }

  // 0x89 ==> 137
  // 0x80
  
  lemma {:only} BarBar(x: uint64, s: seq<uint8>, i: nat)
    requires 0 < i < |s| <= 10
    requires Encode(x) == s
    requires |s| == 10 ==> 1 < i
    ensures
      var len := DecodeLength(s) as nat;
      s[i] == ((x as nat % Pow(len-i)) / Pow((len-1)-i)) as uint8
  {}


  function Encode1(x : uint64)
    : (ret : seq<uint8>)
    requires x < Max1
    ensures |ret| == 1
    ensures EncodeLength(x) == 1
    ensures MaybeValidEncoding(ret)
    ensures DecodeLength(ret) == 1
    ensures ValidEncoding(ret, 1)
  {
    [x as uint8]
  }

  function Encode2(x : uint64)
    : (ret : seq<uint8>)
    requires Max1 <= x < Max2
    ensures |ret| == 2
    ensures EncodeLength(x) == 2
    ensures DecodeLength(ret) == 2
    ensures ValidEncoding(ret, 2)
  {
    var byte0 := Tag2 + (x / 0x100) as uint8;
    var byte1 := (x % 0x100) as uint8;
    [byte0, byte1]
  }

  function Encode3(x : uint64)
    : (ret : seq<uint8>)
    requires Max2 <= x < Max3
    ensures |ret| == 3
    ensures EncodeLength(x) == 3
    ensures DecodeLength(ret) == 3
    ensures ValidEncoding(ret, 3)
  {
    var byte0 := Tag3 + (x / 0x10000) as uint8;
    var byte1 := ((x % 0x10000) / 0x100) as uint8;
    var byte2 := (x % 0x100) as uint8;
    [byte0, byte1, byte2]
  }

  function Encode4(x : uint64)
    : (ret : seq<uint8>)
    requires Max3 <= x < Max4
    ensures |ret| == 4
    ensures EncodeLength(x) == 4
    ensures DecodeLength(ret) == 4
    ensures ValidEncoding(ret, 4)
  {
    var byte0 := Tag4 + (x / 0x1000000) as uint8;
    var byte1 := ((x % 0x1000000) / 0x10000) as uint8;
    var byte2 := ((x % 0x10000) / 0x100) as uint8;
    var byte3 := (x % 0x100) as uint8;
    [byte0, byte1, byte2, byte3]
  }

  function Encode5(x : uint64)
    : (ret : seq<uint8>)
    requires Max4 <= x < Max5
    ensures |ret| == 5
    ensures EncodeLength(x) == 5
    ensures DecodeLength(ret) == 5
    ensures ValidEncoding(ret, 5)
  {
    var byte0 := Tag5 + (x / 0x100000000) as uint8;
    var byte1 := ((x % 0x100000000) / 0x1000000) as uint8;
    var byte2 := ((x % 0x1000000) / 0x10000) as uint8;
    var byte3 := ((x % 0x10000) / 0x100) as uint8;
    var byte4 := (x % 0x100) as uint8;
    [byte0, byte1, byte2, byte3, byte4]
  }

  function Encode6(x : uint64)
    : (ret : seq<uint8>)
    requires Max5 <= x < Max6
    ensures |ret| == 6
    ensures EncodeLength(x) == 6
    ensures DecodeLength(ret) == 6
    ensures ValidEncoding(ret, 6)
  {
    var byte0 := Tag6 + (x / 0x10000000000) as uint8;
    var byte1 := ((x % 0x10000000000) / 0x100000000) as uint8;
    var byte2 := ((x % 0x100000000) / 0x1000000) as uint8;
    var byte3 := ((x % 0x1000000) / 0x10000) as uint8;
    var byte4 := ((x % 0x10000) / 0x100) as uint8;
    var byte5 := (x % 0x100) as uint8;
    [byte0, byte1, byte2, byte3, byte4, byte5]
  }

  opaque function Encode7(x : uint64)
    : (ret : seq<uint8>)
    requires Max6 <= x < Max7
    ensures |ret| == 7
    ensures EncodeLength(x) == 7
    ensures DecodeLength(ret) == 7
    ensures ValidEncoding(ret, 7)
    ensures ret[0] == Tag7 + (x / 0x1000000000000) as uint8
    ensures ret[1] == ((x % 0x1000000000000) / 0x10000000000) as uint8
    ensures ret[2] == ((x % 0x10000000000) / 0x100000000) as uint8
    ensures ret[3] == ((x % 0x100000000) / 0x1000000) as uint8
    ensures ret[4] == ((x % 0x1000000) / 0x10000) as uint8
    ensures ret[5] == ((x % 0x10000) / 0x100) as uint8
    ensures ret[6] == (x % 0x100) as uint8
  {
    var byte0 := Tag7 + (x / 0x1000000000000) as uint8;
    var byte1 := ((x % 0x1000000000000) / 0x10000000000) as uint8;
    var byte2 := ((x % 0x10000000000) / 0x100000000) as uint8;
    var byte3 := ((x % 0x100000000) / 0x1000000) as uint8;
    var byte4 := ((x % 0x1000000) / 0x10000) as uint8;
    var byte5 := ((x % 0x10000) / 0x100) as uint8;
    var byte6 := (x % 0x100) as uint8;
    [byte0, byte1, byte2, byte3, byte4, byte5, byte6]
  }

  opaque function Encode8(x : uint64)
    : (ret : seq<uint8>)
    requires Max7 <= x < Max8
    ensures |ret| == 8
    ensures EncodeLength(x) == 8
    ensures DecodeLength(ret) == 8
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
    var byte1 := ((x % 0x100000000000000) / 0x1000000000000) as uint8;
    var byte2 := ((x % 0x1000000000000) / 0x10000000000) as uint8;
    var byte3 := ((x % 0x10000000000) / 0x100000000) as uint8;
    var byte4 := ((x % 0x100000000) / 0x1000000) as uint8;
    var byte5 := ((x % 0x1000000) / 0x10000) as uint8;
    var byte6:= ((x % 0x10000) / 0x100) as uint8;
    var byte7:= (x % 0x100) as uint8;
    [Tag8, byte1, byte2, byte3, byte4, byte5, byte6, byte7]
  }

  opaque function Encode9(x : uint64)
    : (ret : seq<uint8>)
    requires Max8 <= x < Max9
    ensures |ret| == 9
    ensures EncodeLength(x) == 9
    ensures DecodeLength(ret) == 9
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

  opaque function Encode10(x : uint64)
    : (ret : seq<uint8>)
    requires Max9 <= x
    ensures |ret| == 10
    ensures EncodeLength(x) == 10
    ensures DecodeLength(ret) == 10
    ensures ValidEncoding(ret, 10)
    ensures ret[0] == Tag9
    ensures ret[1] == Tag2
    ensures ret[2] == (x / 0x100000000000000) as uint8
    ensures ret[3] == ((x % 0x100000000000000) / 0x1000000000000) as uint8
    ensures ret[4] == ((x % 0x1000000000000) / 0x10000000000) as uint8
    ensures ret[5] == ((x % 0x10000000000) / 0x100000000) as uint8
    ensures ret[6] == ((x % 0x100000000) / 0x1000000) as uint8
    ensures ret[7] ==  ((x % 0x1000000) / 0x10000) as uint8
    ensures ret[8] == ((x % 0x10000) / 0x100) as uint8
    ensures ret[9] == (x % 0x100) as uint8
  {
    var byte2 := (x / 0x100000000000000) as uint8;
    var byte3 := ((x % 0x100000000000000) / 0x1000000000000) as uint8;
    var byte4 := ((x % 0x1000000000000) / 0x10000000000) as uint8;
    var byte5 := ((x % 0x10000000000) / 0x100000000) as uint8;
    var byte6 := ((x % 0x100000000) / 0x1000000) as uint8;
    var byte7 := ((x % 0x1000000) / 0x10000) as uint8;
    var byte8 := ((x % 0x10000) / 0x100) as uint8;
    var byte9 := (x % 0x100) as uint8;
    [Tag9, Tag2, byte2, byte3, byte4, byte5, byte6, byte7, byte8, byte9]
  }

  function Decode1(x : seq<uint8>) : (ret : uint64)
    requires |x| == 1
    requires x[0] < Tag2
    requires DecodeLength(x) == 1
    requires ValidEncoding(x, 1)
    ensures ret < Max1 as uint64
    ensures EncodeLength(ret) == 1
  {
    x[0] as uint64
  }

  function Decode2(x : seq<uint8>) : (ret : uint64)
    requires |x| == 2
    requires Tag2 <= x[0] < Tag3
    requires DecodeLength(x) == 2
    requires ValidEncoding(x, 2)
    ensures Max1 <= ret < Max2 as uint64
    ensures EncodeLength(ret) == 2
  {
    (x[0] % Tag2) as uint64 * 0x100
    + x[1] as uint64
  }

  function Decode3(x : seq<uint8>) : (ret : uint64)
    requires |x| == 3
    requires Tag3 <= x[0] < Tag4
    requires DecodeLength(x) == 3
    requires ValidEncoding(x, 3)
    ensures Max2 <= ret < Max3 as uint64
    ensures EncodeLength(ret) == 3
  {
    (x[0] % Tag3) as uint64 * 0x10000
    + x[1] as uint64 * 0x100
    + x[2] as uint64
  }

  function Decode4(x : seq<uint8>) : (ret : uint64)
    requires |x| == 4
    requires Tag4 <= x[0] < Tag5
    requires DecodeLength(x) == 4
    requires ValidEncoding(x, 4)
    ensures Max3 <= ret < Max4 as uint64
    ensures EncodeLength(ret) == 4
  {
    (x[0] % Tag4) as uint64 * 0x1000000
    + x[1] as uint64 * 0x10000
    + x[2] as uint64 * 0x100
    + x[3] as uint64
  }

  function Decode5(x : seq<uint8>) : (ret : uint64)
    requires |x| == 5
    requires Tag5 <= x[0] < Tag6
    requires ValidEncoding(x, 5)
    requires DecodeLength(x) == 5
    ensures Max4 <= ret < Max5 as uint64
    ensures EncodeLength(ret) == 5
  {
    (x[0] % Tag5) as uint64 * 0x100000000
    + x[1] as uint64 * 0x1000000
    + x[2] as uint64 * 0x10000
    + x[3] as uint64 * 0x100
    + x[4] as uint64
  }

  function Decode6(x : seq<uint8>) : (ret : uint64)
    requires |x| == 6
    requires Tag6 <= x[0] < Tag7
    requires ValidEncoding(x, 6)
    requires DecodeLength(x) == 6
    ensures Max5 <= ret < Max6 as uint64
    ensures EncodeLength(ret) == 6
  {
    (x[0] % Tag6) as uint64 * 0x10000000000
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
    requires DecodeLength(x) == 7
    ensures Max6 <= ret < Max7 as uint64
    ensures EncodeLength(ret) == 7
  {
    (x[0] % Tag7) as uint64 * 0x1000000000000
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
    requires DecodeLength(x) == 8
    ensures Max7 <= ret < Max8 as uint64
    ensures EncodeLength(ret) == 8
  {
    (x[0] % Tag8) as uint64 * 0x100000000000000
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
    requires MaybeValidEncoding(x)
    requires DecodeLength(x) == 9
    requires ValidEncoding(x, 9)
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

  function Decode10(x : seq<uint8>) : (ret : uint64)
    requires |x| == 10
    requires x[0] == Tag9
    requires x[1] == Tag2
    requires MaybeValidEncoding(x)
    requires ValidEncoding(x, 10)
    requires DecodeLength(x) == 10
    ensures Max9 <= ret
    ensures EncodeLength(ret) == 10
  {
    x[2] as uint64 * 0x100000000000000
    + x[3] as uint64 * 0x1000000000000
    + x[4] as uint64 * 0x10000000000
    + x[5] as uint64 * 0x100000000
    + x[6] as uint64 * 0x1000000
    + x[7] as uint64 * 0x10000
    + x[8] as uint64 * 0x100
    + x[9] as uint64
  }

  // Proof of Decode soundness

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
      case 4 => DecodeRoundTrip4(x, s); assert Encode4(x) == s;
      case 5 => DecodeRoundTrip5(x, s); assert Encode5(x) == s;
      case 6 => DecodeRoundTrip6(x, s); assert Encode6(x) == s;
      case 7 => DecodeRoundTrip7(x, s); assert Encode7(x) == s;
      case 8 => DecodeRoundTrip8(x, s); assert Encode8(x) == s;
      case 9 => DecodeRoundTrip9(x, s); assert Encode9(x) == s;
      case 10 => DecodeRoundTrip10(x, s); assert Encode10(x) == s;
    }
  }

  // lemma {:vcs_split_on_every_assert} EncodeRoundTrip(x: uint64, s: seq<uint8>, len: MyLen)
  //   requires len as int == |s|
  //   requires MaybeValidEncoding(s)
  //   requires len == EncodeLength(x) == DecodeLength(s)
  //   requires ValidEncoding(s, DecodeLength(s))
  //   requires Encode(x) == s
  //   ensures Decode(s, len) == x
  // {
  //   match len {
  //     case 1 => assert Decode1(s) == x;
  //     case 2 => assert Decode2(s) == x;
  //     case 3 => assert Decode3(s) == x;
  //     case 4 => EncodeRoundTrip4(x, s); assert Decode4(s) == x;
  //     case 5 => assert Decode5(s) == x;
  //     case 6 => assert Decode6(s) == x;
  //     case 7 => assume {:axiom} Decode7(s) == x;
  //     case 8 => assume {:axiom} Decode8(s) == x;
  //     case 9 => assume {:axiom} Decode9(s) == x;
  //     case 10 => assume {:axiom} Decode10(s) == x;
  //   }
  // }

  lemma EncodeRoundTrip4(x: uint64, s: seq<uint8>)
    requires Max3 <= x < Max4
    requires |s| == 4
    requires EncodeLength(x) == DecodeLength(s) == 4
    requires ValidEncoding(s, 4)
    requires Encode(x) == s
    ensures Decode4(s) == x
  {}

  lemma {:vcs_split_on_every_assert} DecodeRoundTrip4(x: uint64, s: seq<uint8>)
    requires Max3 <= x < Max4
    requires |s| == 4
    requires EncodeLength(x) == DecodeLength(s) == 4
    requires ValidEncoding(s, 4)
    requires Decode4(s) == x
    ensures Encode(x) == s
  {
    assert s[0] == Tag4 + (x / 0x1000000) as uint8;
    assert s[1] == ((x % 0x1000000) / 0x10000) as uint8;
    assert s[2] == ((x % 0x10000) / 0x100) as uint8 by {
      LemmaFundamentalDivMod(s[2] as int, 0x10000);
      assert x == ((s[0] % 0xe0) as uint64 * 0x1000000
                   + s[1] as uint64 * 0x10000)
                  + (s[2] as uint64 * 0x100
                     + s[3] as uint64);
    }
    assert s[3] == (x % 0x100) as uint8;
  }

  lemma {:vcs_split_on_every_assert} DecodeRoundTrip5(x: uint64, s: seq<uint8>)
    requires Max4 <= x < Max5
    requires |s| == 5
    requires EncodeLength(x) == DecodeLength(s) == 5
    requires ValidEncoding(s, 5)
    requires Decode5(s) == x
    ensures Encode(x) == s
  {
    assert s[0] == Tag5 + (x / 0x100000000) as uint8;
    assert s[1] == ((x % 0x100000000) / 0x1000000) as uint8;
    assert s[2] == ((x % 0x1000000) / 0x10000) as uint8;
    assert s[3] == ((x % 0x10000) / 0x100) as uint8;
    assert s[4] == (x % 0x100) as uint8;
  }

  // lemma {:isolate_assertion} {:only} EncodeRoundTrip6(x: uint64, s: seq<uint8>)
  //   requires Max5 <= x < Max6
  //   requires |s| == 6
  //   requires EncodeLength(x) == DecodeLength(s) == 6
  //   requires ValidEncoding(s, 6)
  //   requires Encode(x) == s
  //   ensures Decode6(s) == x
  // {

  // }

  lemma LemmaDivMultiplesVanish(x: int, d: int)
    requires 0 < d
    ensures (d * x) / d == x

  lemma {:vcs_split_on_every_assert} DecodeRoundTrip6(x: uint64, s: seq<uint8>)
    requires Max5 <= x < Max6
    requires |s| == 6
    requires EncodeLength(x) == DecodeLength(s) == 6
    requires ValidEncoding(s, 6)
    requires Decode6(s) == x
    ensures Encode(x) == s
  {
    LemmaFundamentalDivModAuto();

    assert s[0] == Tag6 + (x / 0x10000000000) as uint8;
    assert s[1] == ((x % 0x10000000000) / 0x100000000) as uint8;
    assert s[2] == ((x % 0x100000000) / 0x1000000) as uint8;
    assert s[3] == ((x % 0x1000000) / 0x10000) as uint8;
    assert s[4] == ((x % 0x10000) / 0x100) as uint8;
    assert s[5] == (x % 0x100) as uint8;
  }

  lemma {:vcs_split_on_every_assert} DecodeRoundTrip7(x: uint64, s: seq<uint8>)
    requires Max6 <= x < Max7
    requires |s| == 7
    requires EncodeLength(x) == DecodeLength(s) == 7
    requires ValidEncoding(s, 7)
    requires Decode7(s) == x
    ensures Encode(x) == s
  {

    LemmaFundamentalDivModAuto();
    assert s[0] == Tag7 + (x / 0x1000000000000) as uint8;
    assert s[1] == ((x % 0x1000000000000) / 0x10000000000) as uint8;
    assert s[2] == ((x % 0x10000000000) / 0x100000000) as uint8;
    assert s[3] == ((x % 0x100000000) / 0x1000000) as uint8;
    assert s[4] == ((x % 0x1000000) / 0x10000) as uint8;
    assert s[5] == ((x % 0x10000) / 0x100) as uint8;
    assert s[6] == (x % 0x100) as uint8;
  }

  lemma {:vcs_split_on_every_assert} {:only} Foo(x: uint64, s: seq<uint8>, i: nat)
    requires Max7 <= x < Max8
    requires 0 < i < |s| == 8
    requires EncodeLength(x) == DecodeLength(s) == 8
    requires ValidEncoding(s, 8)
    requires Decode8(s) == x
    ensures s[i] == ((x as nat % Pow(8-i)) / Pow(7-i)) as uint8

    decreases 8 - i
  {
    if i == 7 {
      assert Pow(8-i) == 0x100;
      assert Pow(7-i) == 0x1;
      assert s[7] == ((x as nat % Pow(8-i)) / Pow(7-i)) as uint8;
    } else {
      // assume i == 6;

    }
  }

  lemma {:vcs_split_on_every_assert} {:only} Bar(x: uint64, s: seq<uint8>, i: nat)
    requires Max7 <= x < Max8
    requires 0 < i < |s| == 8
    requires EncodeLength(x) == DecodeLength(s) == 8
    requires ValidEncoding(s, 8)
    requires Encode8(x) == s
    ensures s[i] == ((x as nat % Pow(8-i)) / Pow(7-i)) as uint8
  {

  }



  lemma {:only} DecodeRoundTrip8(x: uint64, s: seq<uint8>)
    requires Max7 <= x < Max8
    requires |s| == 8
    requires EncodeLength(x) == DecodeLength(s) == 8
    requires ValidEncoding(s, 8)
    requires Decode8(s) == x
    ensures Encode(x) == s
  {

    assert s[0] == Tag8;

    forall i
      | 0 < i < |s| == 8
      ensures s[i] == ((x as nat % Pow(8-i)) / Pow(7-i)) as uint8
    {
      Foo(x, s, i);
    }


    // assert s[1] == ((x % 0x100000000000000) / 0x1000000000000) as uint8;
    // assert s[2] == ((x % 0x1000000000000) / 0x10000000000) as uint8;

    // assert s[3] == ((x as nat % Pow(5)) / Pow(4)) as uint8;

    // assert s[3] == ((x % 0x10000000000) / 0x100000000) as uint8;



    // assert s[4] == ((x % 0x100000000) / 0x1000000) as uint8 by {
    //   LemmaFundamentalDivMod(s[4] as int, 0x100000000);

    //   var r: uint64 := s[0] as uint64;
    //   r := r * 0x100 + s[1] as uint64;
    //   r := r * 0x100 + s[2] as uint64;
    //   r := r * 0x100 + s[3] as uint64;
    //   r := r * 0x100 + s[4] as uint64;
    //   r := r * 0x100 + s[5] as uint64;
    //   r := r * 0x100 + s[6] as uint64;
    //   r := r * 0x100 + s[7] as uint64;

    //   // assert r == x;

    //   // r := r * 0x100 + s[2];
    //   // r := r * 0x100 + s[2];
    //   // assert x == (s[0] % 0xfe) as uint64 * 0x100000000000000
    //   //             + s[1] as uint64 * 0x1000000000000
    //   //             + s[2] as uint64 * 0x10000000000
    //   //             + s[3] as uint64 * 0x100000000
    //   //             + s[4] as uint64 * 0x1000000
    //   //             + s[5] as uint64 * 0x10000
    //   //             + s[6] as uint64 * 0x100
    //   //             + s[7] as uint64;
    // }
    // assert s[5] == ((x % 0x1000000) / 0x10000) as uint8 by {
    //   LemmaFundamentalDivMod(s[5] as int, 0x1000000);
    // }
    // assert s[6] == ((x % 0x10000) / 0x100) as uint8 by {
    //   LemmaFundamentalDivMod(s[6] as int, 0x10000);
    // }

    // assert s[7] == ((x as nat % Pow(1)) / Pow(0)) as uint8;
    // assert s[7] ==(x % 0x100) as uint8;
  }

  lemma {:vcs_split_on_every_assert} DecodeRoundTrip9(x: uint64, s: seq<uint8>)
    requires Max8 <= x < Max9
    requires |s| == 9
    requires EncodeLength(x) == DecodeLength(s) == 9
    requires ValidEncoding(s, 9)
    requires Decode9(s) == x
    ensures Encode(x) == s
  {
    assert s[0] == 0xff;
    assert s[1] == (x / 0x100000000000000) as uint8;
    assert s[2] == ((x % 0x100000000000000) / 0x1000000000000) as uint8;
    assert s[3] == ((x % 0x1000000000000) / 0x10000000000) as uint8 by {
      LemmaFundamentalDivMod(s[3] as int, 0x1000000000000);
    }
    assert s[4] == ((x % 0x10000000000) / 0x100000000) as uint8 by {
      LemmaFundamentalDivMod(s[4] as int, 0x10000000000);
    }
    assert s[5] == ((x % 0x100000000) / 0x1000000) as uint8 by {
      LemmaFundamentalDivMod(s[5] as int, 0x100000000);
    }
    assert s[6] == ((x % 0x1000000) / 0x10000) as uint8 by {
      LemmaFundamentalDivMod(s[6] as int, 0x1000000);
    }
    assert s[7] == ((x % 0x10000) / 0x100) as uint8 by {
      LemmaFundamentalDivMod(s[7] as int, 0x10000);
    }
    assert s[8] == (x % 0x100) as uint8;
  }

  lemma {:vcs_split_on_every_assert} DecodeRoundTrip10(x: uint64, s: seq<uint8>)
    requires Max9 <= x
    requires |s| == 10
    requires EncodeLength(x) == DecodeLength(s) == 10
    requires ValidEncoding(s, 10)
    requires Decode10(s) == x
    ensures Encode(x) == s
  {
    assert s[0] == Tag9;
    assert s[1] == Tag2;
    assert s[2] == (x / 0x100000000000000) as uint8;
    assert s[3] == ((x % 0x100000000000000) / 0x1000000000000) as uint8;
    assert s[4] == ((x % 0x1000000000000) / 0x10000000000) as uint8  by {
      LemmaFundamentalDivMod(s[4] as int, 0x1000000000000);
      assert x == (s[2] as uint64 * 0x100000000000000
                   + s[3] as uint64 * 0x1000000000000)
                  + s[4] as uint64 * 0x10000000000
                  + (s[5] as uint64 * 0x100000000
                     + s[6] as uint64 * 0x1000000
                     + s[7] as uint64 * 0x10000
                     + s[8] as uint64 * 0x100
                     + s[9] as uint64);
    }
    assert s[5] == ((x % 0x10000000000) / 0x100000000) as uint8  by {
      LemmaFundamentalDivMod(s[5] as int, 0x10000000000);
      assert x == (s[2] as uint64 * 0x100000000000000
                   + s[3] as uint64 * 0x1000000000000
                   + s[4] as uint64 * 0x10000000000)
                  + s[5] as uint64 * 0x100000000
                  + (s[6] as uint64 * 0x1000000
                     + s[7] as uint64 * 0x10000
                     + s[8] as uint64 * 0x100
                     + s[9] as uint64);
    }
    assert s[6] == ((x % 0x100000000) / 0x1000000) as uint8  by {
      LemmaFundamentalDivMod(s[6] as int, 0x100000000);
      assert x == (s[2] as uint64 * 0x100000000000000
                   + s[3] as uint64 * 0x1000000000000
                   + s[4] as uint64 * 0x10000000000
                   + s[5] as uint64 * 0x100000000)
                  + s[6] as uint64 * 0x1000000
                  + (s[7] as uint64 * 0x10000
                     + s[8] as uint64 * 0x100
                     + s[9] as uint64);
    }
    assert s[7] == ((x % 0x1000000) / 0x10000) as uint8 by {
      LemmaFundamentalDivMod(s[7] as int, 0x1000000);
    }
    assert s[8] == ((x % 0x10000) / 0x100) as uint8;
    assert s[9] == (x % 0x100) as uint8;
  }

  // These are helper Lemmas copied from
  // the Dafny standard library.
  // Std/Arithmetic/DivMod.dfy
  // https://github.com/dafny-lang/dafny/blob/master/Source/DafnyStandardLibraries/src/Std/Arithmetic/DivMod.dfy#L476-L492

  lemma LemmaFundamentalDivMod(x:int, d:int)
    requires d != 0
    ensures x == d * (x / d) + (x % d)
  {}

  lemma LemmaFundamentalDivModAuto()
    ensures forall x: int, d: int {:trigger d * (x / d) + (x % d)} :: d != 0 ==> x == d * (x / d) + (x % d)
  {
    forall x: int, d: int | d != 0
      ensures x == d * (x / d) + (x % d)
    {
      LemmaFundamentalDivMod(x, d);
    }
  }

}