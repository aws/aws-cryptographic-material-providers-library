// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/VarEncode.dfy"
include "../src/VarEncode16.dfy"
include "../src/VarEncode32.dfy"
include "../src/VarEncode64.dfy"

module {:options "-functionSyntax:4"} VarEncode32Test {
  import VarEncode
  import VarEncode16
  import VarEncode32
  import VarEncode64
  import opened BoundedInts
  import opened Wrappers

  method CheckValue(val : nat)
  {
    if val < TWO_TO_THE_16 {
      var enc := VarEncode.Encode(val);
      var enc16 := VarEncode16.Encode(val as uint16);
      var enc32 := VarEncode32.Encode(val as uint32);
      var enc64 := VarEncode64.Encode(val as uint64);
      expect enc == enc16 == enc32 == enc64;
    } else if val < TWO_TO_THE_32 {
      var enc := VarEncode.Encode(val);
      var enc32 := VarEncode32.Encode(val as uint32);
      var enc64 := VarEncode64.Encode(val as uint64);
      expect enc == enc32 == enc64;
    } else if val < TWO_TO_THE_64 {
      var enc := VarEncode.Encode(val);
      var enc64 := VarEncode64.Encode(val as uint64);
      expect enc == enc64;
    }
  }

  method {:test} TestEncodeSmallNumbers() {
    for i := 0 to 1000000 {
      CheckValue(i);
    }
  }

  method {:test} TestEncodePowersOfTwo() {
    var currPo2 : nat := 1024;
    for p := 10 to 80
      invariant currPo2 >= 1024
    {
      for i : int := -100 to 100 {
        var val := currPo2 + i;
        if val < TWO_TO_THE_32 {
          CheckValue(val);
        }
      }
      currPo2 := currPo2 * 2;
    }
  }
}
