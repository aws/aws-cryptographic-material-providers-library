// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "StandardLibrary.dfy"
include "UInt.dfy"
include "Base64.dfy"

module Base64Lemmas {
  import opened StandardLibrary
  import opened Wrappers
  import opened UInt = StandardLibrary.UInt
  import opened Base64

  lemma DecodeValidEncodeEmpty(s: seq<char>)
    requires s == []
    ensures Encode(DecodeValid(s)) == s
  {}

  lemma DecodeValidEncodeUnpadded(s: seq<char>)
    requires IsBase64String(s)
    requires |s| >= 4
    requires !Is1Padding(s[(|s| - 4)..])
    requires !Is2Padding(s[(|s| - 4)..])
    ensures Encode(DecodeValid(s)) == s
  {
    calc {
      Encode(DecodeValid(s));
    ==
      Encode(DecodeUnpadded(s));
    ==
      EncodeUnpadded(DecodeUnpadded(s));
    == { DecodeEncodeUnpadded(s); }
      s;
    }
  }

  lemma DecodeValidUnpaddedPartialFrom1PaddedSeq(s: seq<char>)
    requires IsBase64String(s)
    requires |s| >= 4
    requires Is1Padding(s[(|s| - 4)..])
    ensures DecodeValid(s)[..(|DecodeValid(s)| - 2)] == DecodeUnpadded(s[..(|s| - 4)])
  {}

  lemma DecodeValid1PaddedPartialFrom1PaddedSeq(s: seq<char>)
    requires IsBase64String(s)
    requires |s| >= 4
    requires Is1Padding(s[(|s| - 4)..])
    ensures DecodeValid(s)[(|DecodeValid(s)| - 2)..] == Decode1Padding(s[(|s| - 4)..])
  {}

  lemma {:vcs_split_on_every_assert} DecodeValidEncode1Padding(s: seq<char>)
    requires IsBase64String(s)
    requires |s| >= 4
    requires Is1Padding(s[(|s| - 4)..])
    ensures Encode(DecodeValid(s)) == s
  {
    DecodeValidEncode1PaddingHelper(s);
    calc {
      Encode(DecodeValid(s));
    ==
      EncodeUnpadded(DecodeValid(s)[..(|DecodeValid(s)| - 2)]) + Encode1Padding(DecodeValid(s)[(|DecodeValid(s)| - 2)..]);
    == { DecodeValidUnpaddedPartialFrom1PaddedSeq(s); }
      assert IsUnpaddedBase64String(s[..(|s| - 4)]) by {
        assert |s| % 4 == 0;
      }
      EncodeUnpadded(DecodeUnpadded(s[..(|s| - 4)])) + Encode1Padding(DecodeValid(s)[(|DecodeValid(s)| - 2)..]);
    == { DecodeEncodeUnpadded(s[..(|s| - 4)]); }
      s[..(|s| - 4)] + Encode1Padding(DecodeValid(s)[(|DecodeValid(s)| - 2)..]);
    == { DecodeValid1PaddedPartialFrom1PaddedSeq(s); }
      s[..(|s| - 4)] + Encode1Padding(Decode1Padding(s[(|s| - 4)..]));
    == { DecodeEncode1Padding(s[(|s| - 4)..]); }
      s[..(|s| - 4)] + s[(|s| - 4)..];
    == { SeqPartsMakeWhole(s, (|s| - 4)); }
      s;
    }
  }

  lemma DecodeValidEncode1PaddingHelper(s: seq<char>)
    requires IsBase64String(s)
    requires |s| >= 4
    requires Is1Padding(s[(|s| - 4)..])
  {
    assert |s| % 4 == 0;
    assert |DecodeValid(s)| % 3 == 2;
    assert 2 <= |DecodeValid(s)|;
  }

  lemma DecodeValidUnpaddedPartialFrom2PaddedSeq(s: seq<char>)
    requires IsBase64String(s)
    requires |s| >= 4
    requires Is2Padding(s[(|s| - 4)..])
    ensures DecodeValid(s)[..(|DecodeValid(s)| - 1)] == DecodeUnpadded(s[..(|s| - 4)])
  {}

  lemma DecodeValid2PaddedPartialFrom2PaddedSeq(s: seq<char>)
    requires IsBase64String(s)
    requires |s| >= 4
    requires Is2Padding(s[(|s| - 4)..])
    ensures DecodeValid(s)[(|DecodeValid(s)| - 1)..] == Decode2Padding(s[(|s| - 4)..])
  {}

  lemma {:vcs_split_on_every_assert} DecodeValidEncode2Padding(s: seq<char>)
    requires IsBase64String(s)
    requires |s| >= 4
    requires Is2Padding(s[(|s| - 4)..])
    ensures Encode(DecodeValid(s)) == s
  {
    DecodeValid2PaddingPropertiesHelper(s);
    calc {
      Encode(DecodeValid(s));
    ==
      EncodeUnpadded(DecodeValid(s)[..(|DecodeValid(s)| - 1)]) + Encode2Padding(DecodeValid(s)[(|DecodeValid(s)| - 1)..]);
    == { DecodeValidUnpaddedPartialFrom2PaddedSeq(s); }
      EncodeUnpadded(DecodeUnpadded(s[..(|s| - 4)])) + Encode2Padding(DecodeValid(s)[(|DecodeValid(s)| - 1)..]);
    == { DecodeEncodeUnpadded(s[..(|s| - 4)]); }
      s[..(|s| - 4)] + Encode2Padding(DecodeValid(s)[(|DecodeValid(s)| - 1)..]);
    == { DecodeValid2PaddedPartialFrom2PaddedSeq(s); }
      s[..(|s| - 4)] + Encode2Padding(Decode2Padding(s[(|s| - 4)..]));
    == { DecodeEncode2Padding(s[(|s| - 4)..]); }
      s[..(|s| - 4)] + s[(|s| - 4)..];
    == { SeqPartsMakeWhole(s, (|s| - 4)); }
      s;
    }
  }

  lemma DecodeValid2PaddingPropertiesHelper(s: seq<char>)
    requires IsBase64String(s)
    requires |s| >= 4
    requires Is2Padding(s[(|s| - 4)..])
  {
    assert |DecodeUnpadded(s[..|s|-4])| % 3 == 0;
    assert |DecodeValid(s)| % 3 == 1;
  }

  lemma DecodeValidEncode(s: seq<char>)
    requires IsBase64String(s)
    ensures Encode(DecodeValid(s)) == s
  {
    if s == [] {
      calc {
        Encode(DecodeValid(s));
      == { DecodeValidEncodeEmpty(s); }
        s;
      }
    } else if |s| >= 4 && Is1Padding(s[(|s| - 4)..]) {
      calc {
        Encode(DecodeValid(s));
      == { DecodeValidEncode1Padding(s); }
        s;
      }
    } else if |s| >= 4 && Is2Padding(s[(|s| - 4)..]) {
      calc {
        Encode(DecodeValid(s));
      == { DecodeValidEncode2Padding(s); }
        s;
      }
    } else {
      calc {
        Encode(DecodeValid(s));
      == { DecodeValidEncodeUnpadded(s); }
        s;
      }
    }
  }

  lemma {:vcs_split_on_every_assert} EncodeDecodeValid(b: seq<uint8>)
    ensures DecodeValid(Encode(b)) == b
  {
    if |b| % 3 == 0 {
      EncodeDecodeValid0(b);
    }
    else if |b| % 3 == 1 {
      EncodeDecodeValid1(b);
    }
    else {
      EncodeDecodeValid2(b);
    }
  }

  lemma EncodeDecodeValid0(b: seq<uint8>)
    requires |b| % 3 == 0
    ensures DecodeValid(Encode(b)) == b
  {}

  lemma EncodeDecodeValid1(b: seq<uint8>)
    requires |b| % 3 == 1
    ensures DecodeValid(Encode(b)) == b
  {}

  lemma EncodeDecodeValid2(b: seq<uint8>)
    requires |b| % 3 == 2
    ensures DecodeValid(Encode(b)) == b
  {}


  lemma DecodeEncode(s: seq<char>)
    requires IsBase64String(s)
    ensures Encode(Decode(s).value) == s
  {
    calc {
      Encode(Decode(s).value);
    == { DecodeValidEncode(s); }
      s;
    }
  }

  lemma EncodeDecode(b: seq<uint8>)
    ensures Decode(Encode(b)) == Success(b)
  {
    calc {
      Decode(Encode(b));
    == { assert IsBase64String(Encode(b)); }
      Success(DecodeValid(Encode(b)));
    == { EncodeDecodeValid(b); }
      Success(b);
    }
  }
}
