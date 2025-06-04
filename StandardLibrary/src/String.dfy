// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../../libraries/src/Wrappers.dfy"
include "Sequence.dfy"

module StandardLibrary.String {
  import Wrappers
  import opened UInt
  import opened Sequence
  import opened MemoryMath
  export provides Int2String, Base10Int2String, HasSubString, Wrappers, UInt

  const Base10: seq<char> := ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

  function method {:tailrecursion} Int2Digits(n: int, base: int): (digits: seq<int>)
    requires base > 1
    requires n >= 0
    decreases n
    ensures forall d | d in digits :: 0 <= d < base
  {
    if n == 0 then
      []
    else
      assert n > 0;
      assert base > 1;
      assert n < base * n;
      assert n / base < n;
      Int2Digits(n / base, base) + [n % base]
  }

  function method {:tailrecursion} Digits2String(digits: seq<int>, chars: seq<char>) : string
    requires forall d | d in digits :: 0 <= d < |chars|
  {
    if digits == [] then ""
    else
      assert digits[0] in digits;
      assert forall d | d in digits[1..] :: d in digits;
      [chars[digits[0]]] + Digits2String(digits[1..], chars)
  }

  function method Int2String(n: int, chars: seq<char>) : string
    requires |chars| > 1
  {
    var base := |chars|;
    if n == 0 then
      "0"
    else if n > 0 then
      Digits2String(Int2Digits(n, base), chars)
    else
      "-" + Digits2String(Int2Digits(-n, base), chars)
  }

  function method Base10Int2String(n: int) : string
  {
    Int2String(n, Base10)
  }

  /* Returns the index of a substring or None, if the substring is not in the string */
  method HasSubString<T(==)>(haystack: seq<T>, needle: seq<T>)
    returns (o: Wrappers.Option<nat>)

    ensures o.Some? ==>
              && o.value <= |haystack| - |needle| && haystack[o.value..(o.value + |needle|)] == needle
              && (forall i | 0 <= i < o.value :: haystack[i..][..|needle|] != needle)

    ensures |haystack| < |needle| ==> o.None?

    ensures o.None? && |needle| <= |haystack| && |haystack| <= (UINT64_MAX_LIMIT-1) ==>
              (forall i | 0 <= i <= (|haystack|-|needle|) :: haystack[i..][..|needle|] != needle)
  {
    SequenceIsSafeBecauseItIsInMemory(haystack);
    SequenceIsSafeBecauseItIsInMemory(needle);
    if |haystack| as uint64 < |needle| as uint64 {
      return Wrappers.None;
    }

    var size : uint64 := |needle| as uint64;
    var limit: uint64 := Add(|haystack| as uint64 - size, 1);

    for index := 0 to limit
      invariant forall i | 0 <= i < index :: haystack[i..][..size] != needle
    {
      if SequenceEqual(seq1 := haystack, seq2 := needle, start1 := index, start2 := 0, size := size) {
        return Wrappers.Some(index as nat);
      }
    }
    return Wrappers.None;
  }
}
