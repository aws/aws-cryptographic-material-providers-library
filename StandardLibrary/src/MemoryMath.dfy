// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

// When dealing with actual data in actual memory, we can be confident that
// none of the numbers will exceed an exabyte, so we can use uint64, rather than nat.
// To convince Dafny that this is true, we have the following functions
// with assumptions as needed.


include "../../libraries/src/BoundedInts.dfy"
include "UInt.dfy"

module {:options "--function-syntax:4"} MemoryMath {
  import opened StandardLibrary.UInt

  // This is safe because it is being held in memory
  lemma {:axiom} ValueIsSafeBecauseItIsInMemory(value : nat)
    ensures HasUint64Size(value)

  lemma SequenceIsSafeBecauseItIsInMemory<T>(value : seq<T>)
    ensures HasUint64Len(value)
  {
    ValueIsSafeBecauseItIsInMemory(|value|);
  }

  function {:opaque} Add(x : uint64, y : uint64) : (ret : uint64)
    ensures ret as nat == x as nat + y as nat
  {
    ValueIsSafeBecauseItIsInMemory(x as nat + y as nat);
    x + y
  }

  function {:opaque} Add3(x : uint64, y : uint64, z : uint64) : (ret : uint64)
    ensures ret as nat == x as nat + y as nat + z as nat
  {
    ValueIsSafeBecauseItIsInMemory(x as nat + y as nat + z as nat);
    x + y + z
  }

  function {:opaque} Add4(w : uint64, x : uint64, y : uint64, z : uint64) : (ret : uint64)
    ensures ret as nat == w as nat + x as nat + y as nat + z as nat
  {
    ValueIsSafeBecauseItIsInMemory(w as nat + x as nat + y as nat + z as nat);
    w + x + y + z
  }

  function {:opaque} Concat<T>(x : seq<T>, y : seq<T>) : (ret : seq64<T>)
    ensures ret == x + y
  {
    SequenceIsSafeBecauseItIsInMemory(x + y);
    x + y
  }

  function {:opaque} Concat3<T>(x : seq<T>, y : seq<T>, z : seq<T>) : (ret : seq64<T>)
    ensures ret == x + y + z
  {
    SequenceIsSafeBecauseItIsInMemory(x + y + z);
    x + y + z
  }

  function {:opaque} Concat4<T>(w : seq<T>, x : seq<T>, y : seq<T>, z : seq<T>) : (ret : seq64<T>)
    ensures ret == w + x + y + z
  {
    SequenceIsSafeBecauseItIsInMemory(w + x + y + z);
    w + x + y + z
  }

  function {:opaque} Concat5<T>(v : seq<T>, w : seq<T>, x : seq<T>, y : seq<T>, z : seq<T>) : (ret : seq64<T>)
    ensures ret == v + w + x + y + z
  {
    SequenceIsSafeBecauseItIsInMemory(v + w + x + y + z);
    v + w + x + y + z
  }

  function {:opaque} Concat6<T>(u : seq<T>, v : seq<T>, w : seq<T>, x : seq<T>, y : seq<T>, z : seq<T>) : (ret : seq64<T>)
    ensures ret == u + v + w + x + y + z
  {
    SequenceIsSafeBecauseItIsInMemory(u + v + w + x + y + z);
    u + v + w + x + y + z
  }

}
