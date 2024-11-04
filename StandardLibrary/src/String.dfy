// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
include "../../libraries/src/Wrappers.dfy"

module StandardLibrary.String {
  import Wrappers
  export provides Int2String, Base10Int2String, HasSubString, Wrappers

  const Base10: seq<char> := ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

  function method Int2Digits(n: int, base: int): (digits: seq<int>)
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

  function method Digits2String(digits: seq<int>, chars: seq<char>) : string
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

  /* Returns the index of a substraing or None, if the substring is not in the string */
  method HasSubString(xs: string, ss: string)
    returns (o: Wrappers.Option<nat>)
    requires |ss| <= |xs|
    ensures o.Some? ==>
              o.value <= |xs| - |ss| && xs[o.value..(o.value + |ss|)] == ss
    // TODO: ensures o.None? ==> no such index exists
  {
    var index: nat := 0;
    var limit: nat := |xs| - |ss|;
    while index <= limit
      decreases limit - index
    {
      if (xs[index .. index + |ss|] == ss) {
        return Wrappers.Some(index);
      } else {
        index := index + 1;
      }
    }
    return Wrappers.None;
  }
}
