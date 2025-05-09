// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

// When dealing with actual data in actual memory, we can be confident that
// none of the numbers will exceed an exabyte, so we can use uint64, rather than nat.
// To convince Dafny that this is true, we have the following functions
// with assumptions as needed.

include "../../libraries/src/Wrappers.dfy"
include "UInt.dfy"

module {:options "--function-syntax:4"} StandardLibrary.MemoryMath {
  import opened UInt
  import opened Wrappers

  // This is safe because it is being held in memory
  lemma {:axiom} ValueIsSafeBecauseItIsInMemory(value : nat)
    ensures HasUint64Size(value)

  lemma SequenceIsSafeBecauseItIsInMemory<T>(value : seq<T>)
    ensures HasUint64Len(value)
  {
    ValueIsSafeBecauseItIsInMemory(|value|);
  }

  lemma SetIsSafeBecauseItIsInMemory<T>(value : set<T>)
    ensures HasUint64Size(|value|)
  {
    ValueIsSafeBecauseItIsInMemory(|value|);
  }

  lemma OptionalSequenceIsSafeBecauseItIsInMemory<T>(value : Option<seq<T>>)
    ensures value.Some? ==> HasUint64Len(value.value)
  {
    if value.Some? {
      SequenceIsSafeBecauseItIsInMemory(value.value);
    }
  }

  lemma MapIsSafeBecauseItIsInMemory<K, V>(value : map<K, V>)
    ensures HasUint64Size(|value|)
  {
    ValueIsSafeBecauseItIsInMemory(|value|);
  }

  lemma OptionalMapIsSafeBecauseItIsInMemory<K, V>(value : Option<map<K, V>>)
    ensures value.Some? ==> HasUint64Size(|value.value|)
  {
    if value.Some? {
      ValueIsSafeBecauseItIsInMemory(|value.value|);
    }
  }

  lemma ArrayIsSafeBecauseItIsInMemory<T>(value : array<T>)
    ensures HasUint64Size(value.Length)
  {
    ValueIsSafeBecauseItIsInMemory(value.Length);
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
}
