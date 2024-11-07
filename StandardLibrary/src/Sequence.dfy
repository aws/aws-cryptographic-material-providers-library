// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "UInt.dfy"

module StandardLibrary.Sequence {
  // export provides SequenceEqual, StandardLibrary
  import opened UInt

  predicate method SequenceEqualNat<T(==)>(seq1: seq<T>, seq2: seq<T>, start1: nat, start2: nat, size: nat) : (ret : bool)
    requires start1 + size <= |seq1|
    requires start2 + size <= |seq2|
    ensures ret ==> seq1[start1..start1 + size] == seq2[start2..start2 + size]
  {
    if |seq1| > UINT64_MAX_LIMIT || |seq2| > UINT64_MAX_LIMIT then
      // This line of code will never be executed, but is included for correctness
      seq1[start1..start1 + size] == seq2[start2..start2 + size]
    else
      SequenceEqual(seq1, seq2, start1 as uint64, start2 as uint64, size as uint64)
  }

  predicate SequenceEqual<T(==)>(seq1: seq64<T>, seq2: seq64<T>, start1: uint64, start2: uint64, size: uint64) : (ret : bool)
    requires start1 as nat + size as nat <= |seq1|
    requires start2 as nat + size as nat <= |seq2|
    ensures ret <==> seq1[start1..start1 + size] == seq2[start2..start2 + size]
  {
    seq1[start1..start1 + size] == seq2[start2..start2 + size]
  } by method {
    var j := start2 as uint64;
    for i := start1 as uint64 to (start1 + size) as uint64
      invariant j == i - start1 + start2
      invariant forall k : uint64 | start1 <= k < i :: seq1[k] == seq2[k - start1 + start2]
    {
      if seq1[i] != seq2[j] {
        return false;
      }
      j := j + 1;
    }
    return true;
  }

}
