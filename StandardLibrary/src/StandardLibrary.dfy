// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../../libraries/src/Wrappers.dfy"
include "MemoryMath.dfy"

module StandardLibrary {
  import opened Wrappers
  import opened U = UInt
  import opened MemoryMath

  lemma SeqTakeAppend<A>(s: seq<A>, i: int)
    requires 0 <= i < |s|
    ensures s[..i] + [s[i]] == s[..i + 1]
  {}

  function Join<T>(ss: seq<seq<T>>, joiner: seq<T>): (s: seq<T>)
    requires 0 < |ss|
  {
    if |ss| == 1 then ss[0] else ss[0] + joiner + Join(ss[1..], joiner)
  }
  by method {
    SequenceIsSafeBecauseItIsInMemory(ss);
    var size := |ss| as uint64;
    var result : seq<T>  := ss[size-1];
    var i : uint64 := size - 1;
    while i > 0
      decreases i
      invariant result == Join(ss[i..], joiner)
    {
      i := i - 1;
      result := ss[i] + joiner + result;
    }
    return result;
  }

  function method {:tailrecursion} Split<T(==)>(s: seq<T>, delim: T): (res: seq<seq<T>>)
    ensures delim !in s ==> res == [s]
    ensures s == [] ==> res == [[]]
    ensures 0 < |res|
    ensures forall i :: 0 <= i < |res| ==> delim !in res[i]
    ensures Join(res, [delim]) == s
    decreases |s|
  {
    var i := FindIndexMatching(s, delim, 0);
    if i.Some? then [s[..i.value]] + Split(s[Add(i.value, 1)..], delim) else [s]
  }

  // split on first occurrence of delim, which must exist
  function method {:tailrecursion} SplitOnce<T(==)>(s: seq<T>, delim: T): (res : (seq<T>,seq<T>))
    requires delim in s
    ensures res.0 + [delim] + res.1 == s
    ensures !(delim in res.0)
  {
    var i := FindIndexMatching(s, delim, 0);
    assert i.Some?;
    (s[..i.value], s[Add(i.value, 1)..])
  }

  // split on first occurrence of delim, return None if delim not present
  function method {:tailrecursion} SplitOnce?<T(==)>(s: seq<T>, delim: T): (res : Option<(seq<T>,seq<T>)>)
    ensures res.Some? ==> res.value.0 + [delim] + res.value.1 == s
    ensures res.None? ==> !(delim in s)
    ensures res.Some? ==> !(delim in res.value.0)
  {
    var i :- FindIndexMatching(s, delim, 0);
    Some((s[..i], s[Add(i, 1)..]))
  }

  lemma {:vcs_split_on_every_assert} WillSplitOnDelim<T>(s: seq<T>, delim: T, prefix: seq<T>)
    requires |prefix| < |s|
    requires forall i :: 0 <= i < |prefix| ==> prefix[i] == s[i]
    requires delim !in prefix && s[|prefix|] == delim
    ensures Split(s, delim) == [prefix] + Split(s[|prefix| + 1..], delim)
  {
    calc {
      Split(s, delim);
    ==
      var i := FindIndexMatching(s, delim, 0);
      if i.Some? then [s[..i.value]] + Split(s[Add(i.value, 1)..], delim) else [s];
    ==  { FindIndexMatchingLocatesElem(s, delim, 0, |prefix| as uint64); assert FindIndexMatching(s, delim, 0).Some?; }
      [s[..|prefix|]] + Split(s[|prefix| + 1..], delim);
    ==  { assert s[..|prefix|] == prefix; }
      [prefix] + Split(s[|prefix| + 1..], delim);
    }
  }

  lemma WillNotSplitWithOutDelim<T>(s: seq<T>, delim: T)
    requires delim !in s
    ensures Split(s, delim) == [s]
  {
    SequenceIsSafeBecauseItIsInMemory(s);
    calc {
      Split(s, delim);
    ==
      var i := FindIndexMatching(s, delim, 0);
      if i.Some? then [s[..i.value]] + Split(s[i.value+1..], delim) else [s];
    ==  { FindIndexMatchingLocatesElem(s, delim, 0, |s| as uint64); }
      [s];
    }
  }

  lemma FindIndexMatchingLocatesElem<T>(s: seq<T>, c: T, start: uint64, elemIndex: uint64)
    requires start as nat <= elemIndex as nat <= |s|
    requires forall i :: start <= i < elemIndex ==> s[i] != c
    requires elemIndex as nat == |s| || s[elemIndex] == c
    ensures FindIndexMatching(s, c, start) == if elemIndex as nat == |s| then None else Some(elemIndex)
    decreases elemIndex - start
  {}

  function method FindIndexMatching<T(==)>(s: seq<T>, c: T, i: uint64): (index: Option<uint64>)
    requires i as nat <= |s|
    ensures index.Some? ==>  i as nat <= index.value as nat < |s| && s[index.value] == c && c !in s[i..index.value]
    ensures index.None? ==> c !in s[i..]
    decreases |s| - i as nat
  {
    FindIndex(s, x => x == c, i)
  }

  function method {:tailrecursion} FindIndex<T>(s: seq<T>, f: T -> bool, i: uint64): (index: Option<uint64>)
    requires i as nat <= |s|
    ensures index.Some? ==> i as nat <= index.value as nat < |s| && f(s[index.value]) && (forall j :: i <= j < index.value ==> !f(s[j]))
    ensures index.None? ==> forall j :: i as nat <= j < |s| ==> !f(s[j])
    decreases |s| - i as nat
  {
    SequenceIsSafeBecauseItIsInMemory(s);
    if i == |s| as uint64 then None
    else if f(s[i]) then Some(i)
    else FindIndex(s, f, i + 1)
  }

  function Filter<T>(s: seq<T>, f: T -> bool): (res: seq<T>)
    ensures forall i :: 0 <= i < |s| && f(s[i]) ==> s[i] in res
    ensures forall i :: 0 <= i < |res| ==> res[i] in s && f(res[i])
    ensures |res| <= |s|
  {
    if |s| == 0 then []
    else if f(s[0]) then [s[0]] + Filter(s[1..], f)
    else Filter(s[1..], f)
  }
  by method {
    SequenceIsSafeBecauseItIsInMemory(s);
    var result : seq<T>  := [];
    var i : uint64 := |s| as uint64;
    while i > 0
      decreases i
      invariant result == Filter(s[i..], f)
    {
      i := i - 1;
      if f(s[i]) {
        result := [s[i]] + result;
      }
    }
    return result;
  }

  lemma FilterIsDistributive<T>(s: seq<T>, s': seq<T>, f: T -> bool)
    ensures Filter(s + s', f) == Filter(s, f) + Filter(s', f)
  {
    if s == [] {
      assert s + s' == s';
    } else {
      var S := s + s';
      var s1 := s[1..];
      calc {
        Filter(S, f);
      ==  // def. Filter
        if f(S[0]) then [S[0]] + Filter(S[1..], f) else Filter(S[1..], f);
      ==  { assert S[0] == s[0] && S[1..] == s1 + s'; }
        if f(s[0]) then [s[0]] + Filter(s1 + s', f) else Filter(s1 + s', f);
      ==  { FilterIsDistributive(s1, s', f); }
        if f(s[0]) then [s[0]] + (Filter(s1, f) + Filter(s', f)) else Filter(s1, f) + Filter(s', f);
      ==  // associativity of +
        if f(s[0]) then ([s[0]] + Filter(s1, f)) + Filter(s', f) else Filter(s1, f) + Filter(s', f);
      ==  // distribute + over if-then-else
        (if f(s[0]) then [s[0]] + Filter(s1, f) else Filter(s1, f)) + Filter(s', f);
      ==  // def. Filter
        Filter(s, f) + Filter(s', f);
      }
    }
  }

  function method Min(a: int, b: int): int {
    if a < b then a else b
  }

  // If we make this `n: uint64` then Dafny produces bad code for Dotnet
  function method Fill<T>(value: T, n: nat): seq<T>
    ensures |Fill(value, n)| == n as nat
    ensures forall i :: 0 <= i < n ==> Fill(value, n)[i] == value
  {
    seq(n, _ => value)
  }

  method SeqToArray<T>(s: seq) returns (a: array)
    // "Fresh" expressions require editing memory
    ensures fresh(a)
    ensures a.Length == |s|
    ensures forall i :: 0 <= i < |s| ==> a[i] == s[i]
  {
    a := new T[|s|](i requires 0 <= i < |s| => s[i]);
  }

  lemma SeqPartsMakeWhole<T>(s: seq<T>, i: nat)
    requires 0 <= i <= |s|
    ensures s[..i] + s[i..] == s
  {}

  /*
   * Lexicographic comparison of sequences.
   *
   * Given two sequences `a` and `b` and a strict (that is, irreflexive)
   * ordering `less` on the elements of these sequences, determine whether or not
   * `a` is lexicographically "less than or equal to" `b`.
   *
   * `a` is lexicographically "less than or equal to" `b` holds iff
   *   there exists a `k` such that
   *   - the first `k` elements of `a` and `b` are the same
   *   - either:
   *      -- `a` has length `k` (that is, `a` is a prefix of `b`)
   *      -- `a[k]` is strictly less (using `less`) than `b[k]`
   *
   * This has ridiculously bad runtime performance, but fortunately we almost never use it
   */

  predicate method LexicographicLessOrEqual<T(==)>(a: seq<T>, b: seq<T>, less: (T, T) -> bool) {
    exists k :: 0 <= k <= |a| && LexicographicLessOrEqualAux(a, b, less, k)
  }

  predicate method LexicographicLessOrEqualAux<T(==)>(a: seq<T>, b: seq<T>, less: (T, T) -> bool, lengthOfCommonPrefix: nat)
    requires 0 <= lengthOfCommonPrefix <= |a|
  {
    lengthOfCommonPrefix <= |b|
    && (forall i :: 0 <= i < lengthOfCommonPrefix ==> a[i] == b[i])
    && (lengthOfCommonPrefix == |a| || (lengthOfCommonPrefix < |b| && less(a[lengthOfCommonPrefix], b[lengthOfCommonPrefix])))
  }

  /*
   * In order for the lexicographic ordering above to have the expected properties, the
   * relation "less" must be trichotomous and transitive.
   *
   * For an ordering `less` to be _trichotomous_ means that for any two `x` and `y`,
   * EXACTLY one of the following three conditions holds:
   *   - less(x, y)
   *   - x == y
   *   - less(y, x)
   * Note that being trichotomous implies being irreflexive.
   */

  predicate Trichotomous<T(!new)>(less: (T, T) -> bool) {
    (forall x, y :: less(x, y) || x == y || less(y, x)) &&  // at least one of the three
    (forall x, y :: less(x, y) && less(y, x) ==> false) &&  // not both of the less's
    (forall x, y :: less(x, y) ==> x != y)  // not a less and the equality
  }

  predicate Transitive<T(!new)>(R: (T, T) -> bool) {
    forall x, y, z :: R(x, y) && R(y, z) ==> R(x, z)
  }

  /*
   * Here is an example relation and a lemma that says the relation is appropriate for use in
   * lexicographic orderings.
   */

  lemma UInt8LessIsTrichotomousTransitive()
    ensures Trichotomous(UInt8Less)
    ensures Transitive(UInt8Less)
  {
  }

  /*
   * As the following lemmas show, the lexicographic ordering is reflexive, antisymmetric, transitive, and total.
   * The proofs are a bit pedantic and include steps that can be automated.
   */

  lemma LexIsReflexive<T>(a: seq<T>, less: (T, T) -> bool)
    ensures LexicographicLessOrEqual(a, a, less)
  {
    assert LexicographicLessOrEqualAux(a, a, less, |a|);
  }

  lemma LexIsAntisymmetric<T(!new)>(a: seq<T>, b: seq<T>, less: (T, T) -> bool)
    requires Trich: Trichotomous(less)
    requires LexicographicLessOrEqual(a, b, less)
    requires LexicographicLessOrEqual(b, a, less)
    ensures a == b
  {
    assert LessIrreflexive: forall x,y :: less(x, y) ==> x != y by {
      reveal Trich;
    }
    assert ASymmetric: forall x,y :: less(x, y) && less(y, x) ==> false by {
      reveal Trich;
    }
    var k0 :| 0 <= k0 <= |a| && LexicographicLessOrEqualAux(a, b, less, k0);
    var k1 :| 0 <= k1 <= |b| && LexicographicLessOrEqualAux(b, a, less, k1);
    var max := if k0 < k1 then k1 else k0;
    assert max <= |a| && max <= |b|;
    assert SameUntilMax: forall i :: 0 <= i < max ==> a[i] == b[i];
    assert AA: k0 == |a| || (k0 < |b| && less(a[k0], b[k0]));
    assert BB: k1 == |b| || (k1 < |a| && less(b[k1], a[k1]));
    calc {
      true;
    ==>  { reveal AA, BB; }
      (k0 == |a| || (k0 < |b| && less(a[k0], b[k0]))) && (k1 == |b| || (k1 < |a| && less(b[k1], a[k1])));
    ==  // distribute && and ||
      (k0 == |a| && k1 == |b|) ||
      (k0 == |a| && k1 < |a| && less(b[k1], a[k1])) ||
      (k0 < |b| && less(a[k0], b[k0]) && k1 == |b|) ||
      (k0 < |b| && less(a[k0], b[k0]) && k1 < |a| && less(b[k1], a[k1]));
    ==  { reveal LessIrreflexive, SameUntilMax; }
      (k0 == |a| && k1 == |b|) ||
      (k0 < |b| && less(a[k0], b[k0]) && k1 < |a| && less(b[k1], a[k1]));
    ==>  { reveal LessIrreflexive, SameUntilMax; assert max <= k0 && max <= k1; }
      (k0 == |a| && k1 == |b|) ||
      (k0 < |b| && less(a[k0], b[k0]) && k1 < |a| && less(b[k1], a[k1]) && k0 == k1 == max);
    ==  { reveal ASymmetric; }
      k0 == |a| && k1 == |b|;
    ==>  { assert |a| == k0 <= max && |b| == k1 <= max ==> k0 == k1; }
      max == |a| == |b|;
    ==>  { reveal SameUntilMax; }
      a == b;
    }
  }

  lemma LexIsTransitive<T(!new)>(a: seq<T>, b: seq<T>, c: seq<T>, less: (T, T) -> bool)
    requires Transitive(less)
    requires LexicographicLessOrEqual(a, b, less)
    requires LexicographicLessOrEqual(b, c, less)
    ensures LexicographicLessOrEqual(a, c, less)
  {
    var k0 :| 0 <= k0 <= |a| && LexicographicLessOrEqualAux(a, b, less, k0);
    var k1 :| 0 <= k1 <= |b| && LexicographicLessOrEqualAux(b, c, less, k1);
    var k := if k0 < k1 then k0 else k1;
    assert LexicographicLessOrEqualAux(a, c, less, k);
  }

  lemma LexIsTotal<T(!new)>(a: seq<T>, b: seq<T>, less: (T, T) -> bool)
    requires Trich: Trichotomous(less)
    ensures LexicographicLessOrEqual(a, b, less) || LexicographicLessOrEqual(b, a, less)
  {
    var m := 0;
    while m < |a| && m < |b| && a[m] == b[m]
      invariant m <= |a| && m <= |b|
      invariant forall i :: 0 <= i < m ==> a[i] == b[i]
    {
      m := m + 1;
    }
    // m is the length of the common prefix of a and b
    if m == |a| == |b| {
      assert a == b;
      LexIsReflexive(a, less);
    } else if m == |a| < |b| {
      assert LexicographicLessOrEqualAux(a, b, less, m);
    } else if m == |b| < |a| {
      assert LexicographicLessOrEqualAux(b, a, less, m);
    } else {
      assert m < |a| && m < |b|;
      reveal Trich;
      if
      case less(a[m], b[m]) =>
        assert LexicographicLessOrEqualAux(a, b, less, m);
      case less(b[m], a[m]) =>
        assert LexicographicLessOrEqualAux(b, a, less, m);
    }
  }

  /*
   * SetToOrderedSequence(s, less) takes a set of T-strings and returns them as a sequence,
   * ordered by the lexicographic ordering whose underlying irreflexive ordering is "less".
   * The function is compilable, but will not exhibit enviable performance.
   * It is ghost. ComputeSetToOrderedSequence2 should be used instead.
   */

  function SetToOrderedSequence<T(!new)>(s: set<seq<T>>, less: (T, T) -> bool): (q: seq<seq<T>>)
    requires Trichotomous(less) && Transitive(less)
    ensures |s| == |q|
    ensures forall i :: 0 <= i < |q| ==> q[i] in s
    ensures forall k :: k in s ==> k in q
    ensures forall i :: 0 < i < |q| ==> LexicographicLessOrEqual(q[i-1], q[i], less)
    ensures forall i, j | 0 <= i < j < |q| :: q[i] != q[j]
  {
    if s == {} then
      []
    else
      // In preparation for the assign-such-that statement below, we'll need to
      // prove that a minimum exists and that it is unique.
      // The following lemma shows existence:
      ThereIsAMinimum(s, less);
      // The following assertion shows uniqueness:
      assert forall a, b :: IsMinimum(a, s, less) && IsMinimum(b, s, less) ==> a == b by {
        // The proof of the assertion is the following forall statement.
        // But why did we even bother to write the assert-by instead of
        // just writing this forall statement in the first place? Because
        // we are in an expression context and a forall statement cannot start
        // an expression (because the "forall" makes the parser think that
        // a forall expression is coming).
        forall a, b | IsMinimum(a, s, less) && IsMinimum(b, s, less) {
          // For the given a and b, the proof is settled by calling the following lemma:
          MinimumIsUnique(a, b, s, less);
        }
      }
      // The "a in s" in the following line follows from IsMinimum(a, s), so it
      // is logically redundant. However, it is needed to convince the compiler
      // that the assign-such-that statement is compilable.
      var a :| a in s && IsMinimum(a, s, less);
      [a] + SetToOrderedSequence(s - {a}, less)
  }

  predicate method IsMinimum<T(==)>(a: seq<T>, s: set<seq<T>>, less: (T, T) -> bool) {
    a in s &&
    forall z :: z in s ==> LexicographicLessOrEqual(a, z, less)
  }

  lemma ThereIsAMinimum<T(!new)>(s: set<seq<T>>, less: (T, T) -> bool)
    requires s != {}
    requires Trichotomous(less) && Transitive(less)
    ensures exists a :: IsMinimum(a, s, less)
  {
    var a := FindMinimum(s, less);
  }

  lemma MinimumIsUnique<T(!new)>(a: seq<T>, b: seq<T>, s: set<seq<T>>, less: (T, T) -> bool)
    requires IsMinimum(a, s, less) && IsMinimum(b, s, less)
    requires Trichotomous(less)
    ensures a == b
  {
    LexIsAntisymmetric(a, b, less);
  }

  lemma FindMinimum<T(!new)>(s: set<seq<T>>, less: (T, T) -> bool) returns (a: seq<T>)
    requires s != {}
    requires Trichotomous(less) && Transitive(less)
    ensures IsMinimum(a, s, less)
  {
    a :| a in s;
    if s == {a} {
      LexIsReflexive(a, less);
    } else {
      var s' := s - {a};
      assert forall x :: x in s <==> x == a || x in s';
      var a' := FindMinimum(s', less);
      if LexicographicLessOrEqual(a', a, less) {
        a := a';
      } else {
        assert LexicographicLessOrEqual(a, a', less) by {
          LexIsTotal(a, a', less);
        }
        forall z | z in s
          ensures LexicographicLessOrEqual(a, z, less)
        {
          if z == a {
            LexIsReflexive(a, less);
          } else {
            calc {
              true;
            ==  // z in s && z != a
              z in s';
            ==>  // by postcondition of FindMinim(s') above
              LexicographicLessOrEqual(a', z, less);
            ==>  { LexIsTransitive(a, a', z, less); }
              LexicographicLessOrEqual(a, z, less);
            }
          }
        }
      }
    }
  }
}
