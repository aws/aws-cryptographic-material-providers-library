// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/MemoryMath.dfy"

module {:options "--function-syntax:4"} MemoryMathTest {
  import MemoryMath
  import opened StandardLibrary.UInt

  method Constrained(x : seq<uint8>, y : uint64, z : uint64) returns (ret : uint64)
    requires HasUint64Len(x)
  {
    expect z == MemoryMath.Add(|x| as uint64, y);
    return z;
  }

  method UnConstrained(x : seq<uint8>)
  {
    MemoryMath.ValueIsSafeBecauseItIsInMemory(|x|);
    var value := Constrained(x, |x| as uint64, 8);
    expect value == 8;
  }

  method UnConstrained2(x : seq<uint8>)
  {
    MemoryMath.SequenceIsSafeBecauseItIsInMemory(x);
    var value := Constrained(x, |x| as uint64, 8);
    expect value == 8;
  }

  method {:test} BasicTests() {
    UnConstrained([0,1,2,3]);
    UnConstrained2([4,5,6,7]);
  }
}


