// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/StandardLibrary.dfy"
include "../src/Sets.dfy"
include "../src/Time.dfy"
  // Just to make sure we don't conflict with dafny-lang/libraries' Sets.dfy
include "../../libraries/src/Collections/Sets/Sets.dfy"

// This function is commonly used for sorting
// But there are also subtle order effects
// that are important for cryptographic libraries.
// These order functions and externs MUST
// be interoperable across runtimes
// to be used for canonical ordering

module TestComputeSetToOrderedSequenceUInt8Less {
  import opened StandardLibrary
  import opened UInt = StandardLibrary.UInt
  import opened SortedSets
  import Time

  predicate method UInt8Greater(x : uint8, y : uint8) {
    y < x
  }

  method {:test} TestSetToOrderedSequenceEmpty() {
    var output := ComputeSetToOrderedSequence({}, UInt8Less);
    var output2 := ComputeSetToOrderedSequence2({}, UInt8Less);
    var expected := [];
    expect output == expected;
    expect output2 == expected;
  }

  method {:test} TestSetToOrderedSequenceOneItem() {
    var a := {[0]};
    var output := ComputeSetToOrderedSequence(a, UInt8Less);
    var output2 := ComputeSetToOrderedSequence2(a, UInt8Less);
    var expected := [[0]];
    expect output == expected;
    expect output2 == expected;
  }

  method {:test} TestSetToOrderedSequenceSimple() {
    var a := {[0, 2], [0, 1]};
    var output := ComputeSetToOrderedSequence(a, UInt8Less);
    var output2 := ComputeSetToOrderedSequence2(a, UInt8Less);
    var expected := [[0, 1], [0, 2]];
    expect output == expected;
    expect output2 == expected;
  }

  method {:test} TestSetToOrderedSequencePrefix() {
    var a := {[0, 1, 2], [0, 1]};
    var output := ComputeSetToOrderedSequence(a, UInt8Less);
    var output2 := ComputeSetToOrderedSequence2(a, UInt8Less);
    var expected := [[0, 1], [0, 1, 2]];
    expect output == expected;
    expect output2 == expected;
  }

  method {:test} TestSetToOrderedSequenceComplex() {
    var a := {[0, 1, 2], [1, 1, 2], [0, 1]};
    var output := ComputeSetToOrderedSequence(a, UInt8Less);
    var output2 := ComputeSetToOrderedSequence2(a, UInt8Less);
    var expected := [[0, 1], [0, 1, 2], [1, 1, 2]];
    expect output == expected;
    expect output2 == expected;
  }

  method {:test} TestSetToOrderedSequenceComplexReverse() {
    var a := {[0, 1, 2], [1, 1, 2], [0, 1]};
    var output := ComputeSetToOrderedSequence(a, UInt8Greater);
    var output2 := ComputeSetToOrderedSequence2(a, UInt8Greater);
    var expected := [[1, 1, 2], [0, 1], [0, 1, 2]];
    expect output == expected;
    expect output2 == expected;
  }

  method {:test} TestSetSequence() {
    var a := {[0, 1, 2], [1, 1, 2], [0, 1]};
    var output := ComputeSetToSequence(a);
    expect multiset(output) == multiset(a);
  }

  method {:test} TestSetToOrderedSequenceManyItems() {
    var time := Time.GetAbsoluteTime();
    var a := set x:uint16 | 0 <= x < 0xFFFF :: UInt16ToSeq(x);
    time := Time.PrintTimeSinceShortChained(time);
    var output := ComputeSetToOrderedSequence(a, UInt8Less);
    var output2 := ComputeSetToOrderedSequence2(a, UInt8Less);
    var expected : seq<seq<uint8>> := seq(0xFFFF, i requires 0 <= i < 0xFFFF => UInt16ToSeq(i as uint16));
    expect output == expected;
    expect output2 == expected;
    Time.PrintTimeSinceShort(time);
  }

}
