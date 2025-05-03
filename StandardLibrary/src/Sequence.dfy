// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "MemoryMath.dfy"
include "WrappersInterop.dfy"

module StandardLibrary.Sequence {
  // export provides SequenceEqual, StandardLibrary
  import opened UInt
  import opened Wrappers

  lemma {:axiom} YYYValueIsSafeBecauseItIsInMemory(value : nat)
    ensures HasUint64Size(value)

  lemma YYYSequenceIsSafeBecauseItIsInMemory<T>(value : seq<T>)
    ensures HasUint64Len(value)
  {
    YYYValueIsSafeBecauseItIsInMemory(|value|);
  }

  // Just like Seq::MapWithResult, but not O(n^2)
  function method {:opaque} {:tailrecursion} MapWithResult<T, R, E>(f: (T ~> Result<R, E>), xs: seq<T>, pos : uint64 := 0, acc : seq<R> := [])
    : (result: Result<seq<R>, E>)
    requires forall i :: 0 <= i < |xs| ==> f.requires(xs[i])
    requires pos as nat <= |xs|
    requires |acc| == pos as nat
    requires forall i :: 0 <= i < pos ==>
                           && f(xs[i]).Success?
                           && acc[i] == f(xs[i]).value

    ensures result.Success? ==>
              && |result.value| == |xs|
              && (forall i :: 0 <= i < |xs| ==>
                                && f(xs[i]).Success?
                                && result.value[i] == f(xs[i]).value)
    reads set i, o | 0 <= i < |xs| && o in f.reads(xs[i]) :: o
    decreases |xs| - pos as nat
  {
    YYYSequenceIsSafeBecauseItIsInMemory(xs);
    if |xs| as uint64 == pos then
      Success(acc)
    else
      var head :- f(xs[pos]);
      MapWithResult(f, xs, pos+1, acc + [head])
  }


  /* Flattens a sequence of sequences into a single sequence by concatenating 
     subsequences, starting from the first element. */
  function method {:tailrecursion} Flatten<T>(xs: seq<seq<T>>, pos : uint64 := 0, acc : seq<T> := []): (ret : seq<T>)
    requires pos as nat <= |xs|
    decreases |xs| - pos as nat
  {
    YYYSequenceIsSafeBecauseItIsInMemory(xs);
    if |xs| as uint64 == pos then
      acc
    else
      Flatten(xs, pos+1, acc + xs[pos])
  }

  predicate method SequenceEqualNat<T(==)>(seq1: seq<T>, seq2: seq<T>, start1: nat, start2: nat, size: nat) : (ret : bool)
    requires start1 + size <= |seq1|
    requires start2 + size <= |seq2|
    ensures ret ==> seq1[start1..start1 + size] == seq2[start2..start2 + size]
  {
    YYYSequenceIsSafeBecauseItIsInMemory(seq1);
    YYYSequenceIsSafeBecauseItIsInMemory(seq2);
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
