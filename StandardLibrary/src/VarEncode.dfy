include "UInt.dfy"

/*
  Converts unsigned numbers into variable length seq<uint8>
  Seven bits per byte used to store actual data.

  // Type for the encoded length
  newtype MyLen = x | 1 <= x <= 9 witness 1

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


module {:options "-functionSyntax:4"} VarEncode {
  import opened StandardLibrary.UInt

  newtype MyLen = x | 1 <= x <= 9 witness 1

  predicate ValidEncoding(x : seq<uint8>)
    requires 0 < |x|
    requires DecodeLength(x[0]) as nat <= |x|
  {
    var len := DecodeLength(x[0]);
    match len {
      case 1 => x[0] < 0x80
      case 2 => x[0] > 0x80 || (x[0] == 0x80 && x[1] >= 128)
      case 3 => x[0] > 0xc0 || (x[0] == 0xc0 && x[1] >= 64)
      case 4 => x[0] > 0xe0 || (x[0] == 0xe0 && x[1] >= 32)
      case 5 => x[0] > 0xf0 || (x[0] == 0xf0 && x[1] >= 16)
      case 6 => x[0] > 0xf8 || (x[0] == 0xf8 && x[1] >= 8)
      case 7 => x[0] > 0xfc || (x[0] == 0xfc && x[1] >= 4)
      case 8 => x[0] == 0xfe && x[1] >= 2
      case 9 => x[0] == 0xff && x[1] >= 1
    }
  }

  function Encode(x : uint64)
    : (ret : seq<uint8>)
    ensures |ret| == EncodeLength(x) as nat
    ensures |ret| == DecodeLength(ret[0]) as nat
    ensures ValidEncoding(ret)
  {
    var len := EncodeLength(x);
    match len {
      case 1 => [x as uint8]
      case 2 =>
        var byte1 := (x / 0x100) as uint8;
        var byte2 := (x % 0x100) as uint8;
        [0x80 + byte1, byte2]
      case 3 =>
        var byte1 := (x / 0x10000) as uint8;
        var byte2 := ((x % 0x10000) / 0x100) as uint8;
        var byte3 := (x % 0x100) as uint8;
        [0xc0 + byte1, byte2, byte3]
      case 4 =>
        var byte1 := (x / 0x1000000) as uint8;
        var byte2 := ((x % 0x1000000) / 0x10000) as uint8;
        var byte3 := ((x % 0x10000) / 0x100) as uint8;
        var byte4 := (x % 0x100) as uint8;
        [0xe0 + byte1, byte2, byte3, byte4]
      case 5 =>
        var byte1 := (x / 0x100000000) as uint8;
        var byte2 := ((x % 0x100000000) / 0x1000000) as uint8;
        var byte3 := ((x % 0x1000000) / 0x10000) as uint8;
        var byte4 := ((x % 0x10000) / 0x100) as uint8;
        var byte5 := (x % 0x100) as uint8;
        [0xf0 + byte1, byte2, byte3, byte4, byte5]
      case 6 =>
        var byte1 := (x / 0x10000000000) as uint8;
        var byte2 := ((x % 0x10000000000) / 0x100000000) as uint8;
        var byte3 := ((x % 0x100000000) / 0x1000000) as uint8;
        var byte4 := ((x % 0x1000000) / 0x10000) as uint8;
        var byte5 := ((x % 0x10000) / 0x100) as uint8;
        var byte6 := (x % 0x100) as uint8;
        [0xf8 + byte1, byte2, byte3, byte4, byte5, byte6]
      case 7 =>
        var byte1 := (x / 0x1000000000000) as uint8;
        var byte2 := ((x % 0x1000000000000) / 0x10000000000) as uint8;
        var byte3 := ((x % 0x10000000000) / 0x100000000) as uint8;
        var byte4 := ((x % 0x100000000) / 0x1000000) as uint8;
        var byte5 := ((x % 0x1000000) / 0x10000) as uint8;
        var byte6 := ((x % 0x10000) / 0x100) as uint8;
        var byte7 := (x % 0x100) as uint8;
        [0xfc + byte1, byte2, byte3, byte4, byte5, byte6, byte7]
      case 8 =>
        var byte2 := ((x % 0x100000000000000) / 0x1000000000000) as uint8;
        var byte3 := ((x % 0x1000000000000) / 0x10000000000) as uint8;
        var byte4 := ((x % 0x10000000000) / 0x100000000) as uint8;
        var byte5 := ((x % 0x100000000) / 0x1000000) as uint8;
        var byte6 := ((x % 0x1000000) / 0x10000) as uint8;
        var byte7:= ((x % 0x10000) / 0x100) as uint8;
        var byte8:= (x % 0x100) as uint8;
        [0xfe, byte2, byte3, byte4, byte5, byte6, byte7, byte8]
      case 9 =>
        var byte1 := (x / 0x100000000000000) as uint8;
        var byte2 := ((x % 0x100000000000000) / 0x1000000000000) as uint8;
        var byte3 := ((x % 0x1000000000000) / 0x10000000000) as uint8;
        var byte4 := ((x % 0x10000000000) / 0x100000000) as uint8;
        var byte5 := ((x % 0x100000000) / 0x1000000) as uint8;
        var byte6 := ((x % 0x1000000) / 0x10000) as uint8;
        var byte7:= ((x % 0x10000) / 0x100) as uint8;
        var byte8:= (x % 0x100) as uint8;
        [0xff, byte1, byte2, byte3, byte4, byte5, byte6, byte7, byte8]
    }
  }

  function EncodeLength(x : uint64) : (ret : MyLen)
    ensures 1 <= ret <= 9
  {
    if x < 0x80 then
      1
    else if x < 0x4000 then
      2
    else if x < 0x200000 then
      3
    else if x < 0x10000000 then
      4
    else if x < 0x800000000 then
      5
    else if x < 0x40000000000 then
      6
    else if x < 0x2000000000000 then
      7
    else if x < 0x100000000000000 then
      8
    else
      9
  }

  function DecodeLength(x : uint8) : (ret : MyLen)
    ensures 1 <= ret <= 9
  {
    if x < 0x80 then
      1
    else if x < 0xc0 then
      2
    else if x < 0xe0 then
      3
    else if x < 0xf0 then
      4
    else if x < 0xf8 then
      5
    else if x < 0xfc then
      6
    else if x < 0xfe then
      7
    else if x < 0xff then
      8
    else
      9
  }

  function Decode(x : seq<uint8>)
    : (ret : uint64)
    requires 0 < |x|
    requires DecodeLength(x[0]) as nat <= |x|
    requires ValidEncoding(x)
    ensures EncodeLength(ret) == DecodeLength(x[0])
  {
    var len := DecodeLength(x[0]);
    match len {
      case 1 =>  x[0] as uint64
      case 2 => ((x[0] % 0x80)
                 as uint64 * 0x100
                 + x[1] as uint64)
      case 3 => (x[0] % 0xc0)
      as uint64 * 0x10000
      + x[1] as uint64 * 0x100
      + x[2] as uint64
      case 4 => (x[0] % 0xe0)
      as uint64 * 0x1000000
      + x[1] as uint64 * 0x10000
      + x[2] as uint64 * 0x100
      + x[3] as uint64
      case 5 => (x[0] % 0xf0)
      as uint64 * 0x100000000
      + x[1] as uint64 * 0x1000000
      + x[2] as uint64 * 0x10000
      + x[3] as uint64 * 0x100
      + x[4] as uint64
      case 6 => (x[0] % 0xf8)
      as uint64 * 0x10000000000
      + x[1] as uint64 * 0x100000000
      + x[2] as uint64 * 0x1000000
      + x[3] as uint64 * 0x10000
      + x[4] as uint64 * 0x100
      + x[5] as uint64
      case 7 => (x[0] % 0xfc)
      as uint64 * 0x1000000000000
      + x[1] as uint64 * 0x10000000000
      + x[2] as uint64 * 0x100000000
      + x[3] as uint64 * 0x1000000
      + x[4] as uint64 * 0x10000
      + x[5] as uint64 * 0x100
      + x[6] as uint64
      case 8 => (x[0] % 0xfe)
      as uint64 * 0x100000000000000
      + x[1] as uint64 * 0x1000000000000
      + x[2] as uint64 * 0x10000000000
      + x[3] as uint64 * 0x100000000
      + x[4] as uint64 * 0x1000000
      + x[5] as uint64 * 0x10000
      + x[6] as uint64 * 0x100
      + x[7] as uint64
      case 9 =>
        x[1] as uint64 * 0x100000000000000
        + x[2] as uint64 * 0x1000000000000
        + x[3] as uint64 * 0x10000000000
        + x[4] as uint64 * 0x100000000
        + x[5] as uint64 * 0x1000000
        + x[6] as uint64 * 0x10000
        + x[7] as uint64 * 0x100
        + x[8] as uint64
    }
  }

  lemma Bar1(x : seq<uint8>)
    requires |x| == 1
    requires DecodeLength(x[0]) == 1
    requires ValidEncoding(x)
    ensures Encode(Decode(x)) == x
  {
    assert 0 <= Decode(x) < 0x80;
  }

  lemma Bar2(x : seq<uint8>)
    requires |x| == 2
    requires DecodeLength(x[0]) == 2
    requires ValidEncoding(x)
    ensures Encode(Decode(x)) == x
  {
    assert 0x80 <= Decode(x) < 0x4000;
  }

  lemma Bar3(x : seq<uint8>)
    requires |x| == 3
    requires DecodeLength(x[0]) as nat == 3
    requires ValidEncoding(x)
    ensures Encode(Decode(x)) == x
  {
    assert 0x4000 <= Decode(x) < 0x200000;
  }

  lemma Bar4(x : seq<uint8>)
    requires |x| == 4
    requires DecodeLength(x[0]) as nat == 4
    requires ValidEncoding(x)
    ensures Encode(Decode(x)) == x
  {
    assert 0x200000 <= Decode(x) < 0x10000000;
    assume {:axiom} Encode(Decode(x)) == x;
  }

  lemma Bar5(x : seq<uint8>)
    requires |x| == 5
    requires DecodeLength(x[0]) as nat == 5
    requires ValidEncoding(x)
    ensures Encode(Decode(x)) == x
  {
    assume {:axiom} 0x10000000 <= Decode(x) < 0x800000000;
    assume {:axiom} Encode(Decode(x)) == x;
  }

  lemma Bar6(x : seq<uint8>)
    requires |x| == 6
    requires DecodeLength(x[0]) as nat == 6
    requires ValidEncoding(x)
    ensures Encode(Decode(x)) == x
  {
    assert 0x800000000 <= Decode(x) < 0x40000000000;
    assume {:axiom} Encode(Decode(x)) == x;
  }

  lemma Bar7(x : seq<uint8>)
    requires |x| == 7
    requires DecodeLength(x[0]) as nat == 7
    requires ValidEncoding(x)
    ensures Encode(Decode(x)) == x
  {
    assert 0x40000000000 <= Decode(x) < 0x2000000000000;
    assume {:axiom} Encode(Decode(x)) == x;
  }

  lemma Bar8(x : seq<uint8>)
    requires |x| == 8
    requires DecodeLength(x[0]) as nat == 8
    requires ValidEncoding(x)
    ensures Encode(Decode(x)) == x
  {
    assert 0x2000000000000 <= Decode(x) < 0x100000000000000;
    assume {:axiom} Encode(Decode(x)) == x;
  }


  lemma Bar9(x : seq<uint8>)
    requires |x| == 9
    requires DecodeLength(x[0]) as nat == 9
    requires ValidEncoding(x)
    ensures Encode(Decode(x)) == x
  {
    assume {:axiom} 0x100000000000000 <= Decode(x) < 0x8000000000000000;
    assume {:axiom} Encode(Decode(x)) == x;
  }

  lemma Foo1(x : uint64)
    requires x < 0x80
    ensures Decode(Encode(x)) == x
  {}

  lemma Foo2(x : uint64)
    requires x < 0x4000
    ensures x ==
            ((x % 0x10000) / 0x100) * 0x100
            + (x % 0x100)
    ensures Decode(Encode(x)) == x
  {}

  lemma Foo3(x : uint64)
    requires x < 0x200000
    ensures x ==
            ((x % 0x1000000) / 0x10000) * 0x10000
            + ((x % 0x10000) / 0x100) * 0x100
            + (x % 0x100)
    ensures Decode(Encode(x)) == x
  {}

  lemma Foo4(x : uint64)
    requires x < 0x10000000
    ensures x ==
            ((x % 0x100000000) / 0x1000000) * 0x1000000
            + ((x % 0x1000000) / 0x10000) * 0x10000
            + ((x % 0x10000) / 0x100) * 0x100
            + (x % 0x100)
    ensures Decode(Encode(x)) == x
  {
    assert x % 0x10000 == ((x % 0x10000) / 0x100) * 0x100 + (x % 0x100);
  }

  lemma Foo5(x : uint64)
    requires x < 0x800000000
    ensures x == (x / 0x100000000) * 0x100000000
                 + ((x % 0x100000000) / 0x1000000) * 0x1000000
                 + ((x % 0x1000000) / 0x10000) * 0x10000
                 + ((x % 0x10000) / 0x100) * 0x100
                 + (x % 0x100)
    ensures Decode(Encode(x)) == x
  {
    assert x % 0x10000 == ((x % 0x10000) / 0x100) * 0x100 + (x % 0x100);
    assert x % 0x1000000 == ((x % 0x1000000) / 0x10000) * 0x10000 + ((x % 0x10000) / 0x100) * 0x100 + (x % 0x100);
  }

  lemma Foo6(x : uint64)
    requires x < 0x40000000000
    ensures x == (x / 0x10000000000) * 0x10000000000
                 + ((x % 0x10000000000) / 0x100000000) * 0x100000000
                 + ((x % 0x100000000) / 0x1000000) * 0x1000000
                 + ((x % 0x1000000) / 0x10000) * 0x10000
                 + ((x % 0x10000) / 0x100) * 0x100
                 + (x % 0x100)
    ensures Decode(Encode(x)) == x
  {
    assert x % 0x10000 == ((x % 0x10000) / 0x100) * 0x100 + (x % 0x100);
    assert x % 0x1000000 == ((x % 0x1000000) / 0x10000) * 0x10000 + ((x % 0x10000) / 0x100) * 0x100 + (x % 0x100);
    assume {:axiom} x % 0x100000000 == ((x % 0x100000000) / 0x1000000) * 0x1000000 + ((x % 0x1000000) / 0x10000) * 0x10000 + ((x % 0x10000) / 0x100) * 0x100 + (x % 0x100);
  }

  lemma Foo7(x : uint64)
    requires x < 0x2000000000000
    ensures x == (x / 0x1000000000000) * 0x1000000000000
                 + ((x % 0x1000000000000) / 0x10000000000) * 0x10000000000
                 + ((x % 0x10000000000) / 0x100000000) * 0x100000000
                 + ((x % 0x100000000) / 0x1000000) * 0x1000000
                 + ((x % 0x1000000) / 0x10000) * 0x10000
                 + ((x % 0x10000) / 0x100) * 0x100
                 + (x % 0x100)
    ensures Decode(Encode(x)) == x
  {
    assert x % 0x10000 == ((x % 0x10000) / 0x100) * 0x100 + (x % 0x100);
    assert x % 0x1000000 == ((x % 0x1000000) / 0x10000) * 0x10000 + ((x % 0x10000) / 0x100) * 0x100 + (x % 0x100);

    var two := ((x % 0x10000) / 0x100) * 0x100 + (x % 0x100);
    assert x % 0x10000 == two;
    var three := ((x % 0x1000000) / 0x10000) * 0x10000 + two;
    assert x % 0x1000000 == three;
    var four := ((x % 0x100000000) / 0x1000000) * 0x1000000 + three;
    assert x % 0x100000000 == four;
    var five := ((x % 0x10000000000) / 0x100000000) * 0x100000000 + four;
    assume {:axiom} x % 0x10000000000 == five;
    var six := ((x % 0x1000000000000) / 0x10000000000) * 0x10000000000 + five;
    assume {:axiom} x % 0x1000000000000 == six;

    assume {:axiom} x == (x / 0x1000000000000) * 0x1000000000000
                         + ((x % 0x1000000000000) / 0x10000000000) * 0x10000000000
                         + ((x % 0x10000000000) / 0x100000000) * 0x100000000
                         + ((x % 0x100000000) / 0x1000000) * 0x1000000
                         + ((x % 0x1000000) / 0x10000) * 0x10000
                         + ((x % 0x10000) / 0x100) * 0x100
                         + (x % 0x100);
  }

  lemma EncodeRoundTrip(x : uint64)
    ensures Decode(Encode(x)) == x
  {
    var enc := Encode(x);
    var num := Decode(enc);
    assert Decode(Encode(x)) == num;

    match EncodeLength(x) {
      case 1 =>
      case 2 => Foo2(x);
      case 3 => Foo3(x);
      case 4 => Foo4(x);
      case 5 => Foo5(x);
      case 6 => Foo6(x);
      case 7 => Foo7(x);
      case 8 => assume {:axiom} false;
      case 9 => assume {:axiom} false;
    }
  }

  lemma DecodeRoundTrip(x : seq<uint8>)
    requires 0 < |x|
    requires DecodeLength(x[0]) as nat == |x|
    requires ValidEncoding(x)
    ensures Encode(Decode(x)) == x[..DecodeLength(x[0])]
  {
    var num := Decode(x);
    var enc := Encode(num);
    assert Encode(Decode(x)) == enc;

    match DecodeLength(x[0]) {
      case 1 => Bar1(x);
      case 2 => Bar2(x);
      case 3 => Bar3(x);
      case 4 => Bar4(x);
      case 5 => Bar5(x);
      case 6 => Bar6(x);
      case 7 => Bar7(x);
      case 8 => Bar8(x);
      case 9 => Bar9(x);
    }
  }
}