// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../../libraries/src/Wrappers.dfy"
include "Sequence.dfy"

module StandardLibrary.String {
  import opened Wrappers
  import opened UInt
  import opened Sequence
  import opened MemoryMath
  export provides Int2String, Base10Int2String, HasSubString, Wrappers, UInt,
                  HasSubStringPos, SearchAndReplace, SearchAndReplacePos, SearchAndReplaceAll,
                  SearchAndReplacePosNot, SearchAndReplaceAllNot, AlphaNumeric, AlphaNumericUnder

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

  // Replace first occurrence of old_str in source with new_str and return the result.
  // If old_str does not exist in source, the source is returned unchanged
  method SearchAndReplace<T(==)>(source: seq<T>, old_str: seq<T>, new_str: seq<T>)
    returns (o : seq<T>)
    requires 0 < |old_str|
  {
    var old_pos := HasSubString(source, old_str);
    if old_pos.None? {
      return source;
    } else {
      SequenceIsSafeBecauseItIsInMemory(source);
      SequenceIsSafeBecauseItIsInMemory(old_str);
      ValueIsSafeBecauseItIsInMemory(old_pos.value);
      var pos : uint64 := old_pos.value as uint64;
      var source_len : uint64 := |source| as uint64;
      var old_str_len : uint64 := |old_str| as uint64;
      return source[..pos] + new_str + source[pos+old_str_len..];
    }
  }

  // Replace first occurrence of old_str after pos in source with new_str and return the result.
  // If old_str does not exist in source, the source is returned unchanged
  // second value in output is None if old_str not found, otherwise it points just after the replaced value
  method SearchAndReplacePos<T(==)>(source: seq<T>, old_str: seq<T>, new_str: seq<T>, pos : uint64)
    returns (o : (seq<T>, Option<uint64>))
    requires pos as nat <= |source|
    requires 0 < |old_str|
    ensures o.1.Some? ==> |o.0| - o.1.value as nat < |source| - pos as nat
    ensures o.1.Some? ==> o.1.value as nat <= |o.0|
  {
    var old_pos := HasSubStringPos(source, old_str, pos);
    if old_pos.None? {
      return (source, None);
    } else {
      SequenceIsSafeBecauseItIsInMemory(source);
      SequenceIsSafeBecauseItIsInMemory(old_str);
      SequenceIsSafeBecauseItIsInMemory(new_str);
      var source_len : uint64 := |source| as uint64;
      var old_str_len : uint64 := |old_str| as uint64;
      var new_str_len : uint64 := |new_str| as uint64;
      o := (source[..old_pos.value] + new_str + source[old_pos.value+old_str_len..], Some(Add(old_pos.value, new_str_len)));
      assert |o.0| - o.1.value as nat < |source| - pos as nat;
      return o;
    }
  }

  predicate method BadStart<T(==)>(source : seq<T>, pos : uint64, forbid : seq<T>)
    requires pos as nat <= |source|
  {
    if pos == 0 then
      false
    else
      source[pos-1] in forbid
  }

  predicate method BadEnd<T(==)>(source : seq<T>, pos : uint64, match_len : uint64, forbid : seq<T>) {
    SequenceIsSafeBecauseItIsInMemory(source);
    var source_len : uint64 := |source| as uint64;
    if Add(pos, match_len) >= source_len then
      false
    else
      source[pos+match_len] in forbid

  }
  predicate method BadMatch<T(==)>(source : seq<T>, pos : uint64, match_len : uint64, forbid : seq<T>)
    requires pos as nat <= |source|
  {
    BadStart(source, pos, forbid) || BadEnd(source, pos, match_len, forbid)
  }

  const AlphaNumeric      : string := "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
  const AlphaNumericUnder : string := "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"

  // Replace first occurrence of old_str after pos in source with new_str and return the result.
  // If old_str does not exist in source, the source is returned unchanged
  // second value in output is None if old_str not found, otherwise it points just after the replaced value
  // a match only counts if the character before or after is not in forbid
  method SearchAndReplacePosNot<T(==)>(source: seq<T>, old_str: seq<T>, new_str: seq<T>, xpos : uint64, forbid : seq<T>)
    returns (o : (seq<T>, Option<uint64>))
    requires xpos as nat <= |source|
    requires 0 < |old_str|
    ensures o.1.Some? ==> |o.0| - o.1.value as nat < |source| - xpos as nat
    ensures o.1.Some? ==> o.1.value as nat <= |o.0|
  {
    SequenceIsSafeBecauseItIsInMemory(source);
    SequenceIsSafeBecauseItIsInMemory(old_str);
    var old_str_len : uint64 := |old_str| as uint64;
    var pos : uint64 := xpos;

    while pos < |source| as uint64 {
      var old_pos := HasSubStringPos(source, old_str, pos);
      if old_pos.None? {
        return (source, None);
      } else if BadMatch(source, old_pos.value, old_str_len, forbid) {
        pos := old_pos.value + 1;
      } else {
        SequenceIsSafeBecauseItIsInMemory(source);
        SequenceIsSafeBecauseItIsInMemory(new_str);
        var source_len : uint64 := |source| as uint64;
        var new_str_len : uint64 := |new_str| as uint64;
        o := (source[..old_pos.value] + new_str + source[old_pos.value+old_str_len..], Some(Add(old_pos.value, new_str_len)));
        assert |o.0| - o.1.value as nat < |source| - pos as nat;
        return o;
      }
    }
    return (source, None); // not really needed, but Dafny is dumb
  }


  // Replace all occurrences of old_str in source with new_str and return the result.
  // If old_str does not exist in source, the source is returned unchanged
  // safe to use if new_str contains old_str
  method SearchAndReplaceAll<T(==)>(source_in: seq<T>, old_str: seq<T>, new_str: seq<T>)
    returns (o : seq<T>)
    requires 0 < |old_str|
  {
    var pos : uint64 := 0;
    var source := source_in;
    while true
      invariant pos as nat <= |source|
      decreases |source| - pos as nat
    {
      var res := SearchAndReplacePos(source, old_str, new_str, pos);
      if res.1.None? {
        SequenceIsSafeBecauseItIsInMemory(source);
        pos := |source| as uint64;
        return res.0;
      }
      source := res.0;
      pos := res.1.value;
    }
  }

  // Replace all occurrences of old_str in source with new_str and return the result.
  // If old_str does not exist in source, the source is returned unchanged
  // safe to use if new_str contains old_str
  // a match only counts if the character before or after is not in forbid
  method SearchAndReplaceAllNot<T(==)>(source_in: seq<T>, old_str: seq<T>, new_str: seq<T>, forbid : seq<T>)
    returns (o : seq<T>)
    requires 0 < |old_str|
  {
    var pos : uint64 := 0;
    var source := source_in;
    while true
      invariant pos as nat <= |source|
      decreases |source| - pos as nat
    {
      var res := SearchAndReplacePosNot(source, old_str, new_str, pos, forbid);
      if res.1.None? {
        SequenceIsSafeBecauseItIsInMemory(source);
        pos := |source| as uint64; // unneeded, but Dafny is dumb
        return res.0;
      }
      source := res.0;
      pos := res.1.value;
    }
  }


  /* Returns the index of a substring or None, if the substring is not in the string */
  method HasSubString<T(==)>(haystack: seq<T>, needle: seq<T>)
    returns (o: Option<nat>)

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
      return None;
    }

    var size : uint64 := |needle| as uint64;
    var limit: uint64 := Add(|haystack| as uint64 - size, 1);

    for index := 0 to limit
      invariant forall i | 0 <= i < index :: haystack[i..][..size] != needle
    {
      if SequenceEqual(seq1 := haystack, seq2 := needle, start1 := index, start2 := 0, size := size) {
        return Some(index as nat);
      }
    }
    return None;
  }

  /* Returns the index of a substring or None, if the substring is not in the string */
  method HasSubStringPos<T(==)>(haystack: seq<T>, needle: seq<T>, pos : uint64)
    returns (o: Option<uint64>)
    requires pos as nat <= |haystack|

    ensures o.Some? ==>
              && pos <= o.value
              && o.value as nat <= |haystack| - |needle| && haystack[o.value..(o.value as nat + |needle|)] == needle
              && (forall i | pos <= i < o.value :: haystack[i..][..|needle|] != needle)

    ensures |haystack| - pos as nat < |needle| ==> o.None?

    ensures o.None? && |needle| <= |haystack| && |haystack| <= (UINT64_MAX_LIMIT-1) ==>
              (forall i | pos as nat <= i <= (|haystack|-|needle|) :: haystack[i..][..|needle|] != needle)
  {
    SequenceIsSafeBecauseItIsInMemory(haystack);
    SequenceIsSafeBecauseItIsInMemory(needle);
    if |haystack| as uint64 - pos < |needle| as uint64 {
      return None;
    }

    var size : uint64 := |needle| as uint64;
    var limit: uint64 := Add(|haystack| as uint64 - size, 1);

    for index := pos to limit
      invariant forall i | pos <= i < index :: haystack[i..][..size] != needle
    {
      if SequenceEqual(seq1 := haystack, seq2 := needle, start1 := index, start2 := 0, size := size) {
        return Some(index);
      }
    }
    return None;
  }
}
