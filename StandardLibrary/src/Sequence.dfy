// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

module StandardLibrary.Sequence {
  export provides SequenceEqual

  /* No Allocation Comparison of two Sequences. Author: ajewellamz */
  predicate method SequenceEqual<T(==)>(
    nameonly seq1 : seq<T>,
    nameonly seq2 : seq<T>,
    nameonly start1 : nat,
    nameonly start2 : nat,
    nameonly size : nat
  ): (ret: bool) // returns (ret : bool)

    requires start1 + size <= |seq1|
    requires start2 + size <= |seq2|
    ensures ret ==> seq1[start1 .. start1 + size] == seq2[start2 .. start2+size]
  {
    // for i : nat := 0 to size {
    //   if seq1[start1+i] != seq2[start2+i] {
    //     return false;
    //   }
    // }
    // return true;
    forall i | 0 <= i < size :: seq1[start1+i] == seq2[start2+i]
  }
}
