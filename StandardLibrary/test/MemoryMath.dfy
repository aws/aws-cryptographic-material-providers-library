// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/MemoryMath.dfy"

module {:options "--function-syntax:4"} MemoryMathTest {
  import MemoryMath
  import opened BoundedInts

  method Constrained(x : seq<uint8>, y : uint64, z : uint64) returns (ret : uint64)
    requires |x| < UINT64_MAX as nat
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

  method {:test} BasicTests() {
    UnConstrained([0,1,2,3]);
  }
}


