// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../../Model/AwsCryptographyMaterialProvidersTypes.dfy"
include "../../../../../libraries/src/MutableMap/MutableMap.dfy"

module {:options "/functionSyntax:4" } LocalCMC {
  import opened Wrappers
  import opened StandardLibrary.UInt
  import opened StandardLibrary.MemoryMath
  import opened DafnyLibraries
  import Time
  import Types = AwsCryptographyMaterialProvidersTypes
  import Seq

  // This limits the visibility of the LocalCMC
  // Doing this ensures that the smithy-dafny `axiom`
  // added because the Types.ICryptographicMaterialsCache
  // has the @aws.polymorph#mutableLocalState trait added in the smithy model
  // can not leak and create unsoundness.
  export
    // This shows that LocalCMC extends Types.ICryptographicMaterialsCache
    // as well as revealing the constructors spec.
    reveals LocalCMC
    provides
      // These are dependent types that are needed
      Types,
      Wrappers,
      DafnyLibraries,
      CacheEntry,
      UInt,

      // These are the implementations of the trait
      LocalCMC.GetCacheEntry',
      LocalCMC.PutCacheEntry',
      LocalCMC.DeleteCacheEntry',
      LocalCMC.UpdateUsageMetadata',
      LocalCMC.GetCacheEntryEnsuresPublicly,
      LocalCMC.PutCacheEntryEnsuresPublicly,
      LocalCMC.DeleteCacheEntryEnsuresPublicly,
      LocalCMC.UpdateUsageMetadataEnsuresPublicly,
      LocalCMC.ValidState,
      LocalCMC.InternalValidState,
      LocalCMC.GetCacheEntryWithTime,

      // These are internal details
      // that come from the constructor
      // or the delete operation.
      LocalCMC.InternalDeleteCacheEntry?,
      LocalCMC.entryCapacity,
      LocalCMC.entryPruningTailSize

  datatype Ref<T> =
    | Ptr(deref: T)
    | Null

  // A const Null to avoid creating them all the time
  const NULL : Ref<CacheEntry> := Null
  const INT32_MAX_VALUE: int32 := 0x7999_9999
  const INT64_MAX_VALUE: int64 := 0x7999_9999_9999_9999

  class CacheEntry {
    var prev: Ref<CacheEntry>
    var next: Ref<CacheEntry>

    const materials: Types.Materials
    const identifier: seq<uint8>
    const creationTime: Types.PositiveLong
    const expiryTime: Types.PositiveLong
    var messagesUsed: Types.PositiveInteger
    var bytesUsed: Types.PositiveInteger

    constructor(
      nameonly materials': Types.Materials,
      nameonly identifier': seq<uint8>,
      nameonly creationTime': Types.PositiveLong,
      nameonly expiryTime': Types.PositiveLong,
      nameonly messagesUsed': Types.PositiveInteger,
      nameonly bytesUsed': Types.PositiveInteger
    )
      ensures
        && identifier == identifier'
        && materials == materials'
        && identifier == identifier'
        && creationTime == creationTime'
        && expiryTime == expiryTime'
        && messagesUsed == messagesUsed'
        && bytesUsed == bytesUsed'
      ensures prev == Null && next == Null
      ensures fresh(this)
    {
      materials := materials';
      identifier := identifier';
      creationTime := creationTime';
      expiryTime := expiryTime';
      messagesUsed := messagesUsed';
      bytesUsed := bytesUsed';
      prev := NULL;
      next := NULL;
    }
  }

  class DoublyLinkedCacheEntryList {

    ghost var Items : seq<CacheEntry>

    ghost predicate Invariant()
      reads this, Items
    {
      // head and tail properties
      && (0 == |Items| <==> head.Null? && tail.Null?)
      && (0 < |Items| <==>
          && head.Ptr?
          && tail.Ptr?
          && head.deref == Items[0]
          && tail.deref == Items[|Items| - 1])
      && (head.Ptr? <==> tail.Ptr?)
      && (head.Ptr? ==> head.deref.prev.Null?)
      && (tail.Ptr? ==> tail.deref.next.Null?)
         // Every Cell in the DoublyLinkedList MUST be unique.
         // Otherwise there would be loops in prev and next.
         // For a Cell at 4, next MUST point to 5 or Null?.
         // So if a Cell exists as 4 and 7
         // then it's next would need to point to _both_ 5 and 8.
      && (forall v <- Items :: multiset(Items)[v] == 1)
         // Proving order is easier by being more specific
         // and breaking up prev and next.
         // Order means Cell 4 point to 3 and 5
         // in prev and next respectively.
      && (forall i: nat | 0 <= i < |Items| ::
            && Prev?(i, Items[i], Items)
            && Next?(i, Items[i], Items)
         )
    }

    ghost predicate Prev?(i:nat, c: CacheEntry, Items' : seq<CacheEntry>)
      reads Items'
      requires 0 <= i < |Items'|
      requires Items'[i] == c
    {
      if i == 0 then
        Items'[0].prev.Null?
      else
        && Items'[i].prev.Ptr?
        && Items'[i].prev.deref == Items'[i - 1]
    }

    ghost predicate Next?(i:nat, c: CacheEntry, Items' : seq<CacheEntry>)
      reads Items'
      requires 0 <= i < |Items'|
      requires Items'[i] == c
    {
      if i < |Items'| -1 then
        && Items'[i].next.Ptr?
        && Items'[i].next.deref == Items'[i + 1]
      else
        assert i == |Items'| - 1;
        && Items'[i].next.Null?
    }

    constructor()
      ensures Items == []
      ensures Invariant()
    {
      head := Null;
      tail := Null;
      Items := [];
    }

    var head: Ref<CacheEntry>
    var tail: Ref<CacheEntry>

    method pushCell(toPush: CacheEntry)
      requires toPush !in Items
      requires toPush.next.Null? && toPush.prev.Null?
      requires Invariant()
      modifies this, Items, toPush
      ensures Invariant()
      ensures Items == [toPush] + old(Items)
    {
      Items := [toPush] + Items;
      var cRef := Ptr(toPush);
      if head.Ptr? {
        head.deref.prev := cRef;
        toPush.next := head;
        head := cRef;
      } else {
        head := cRef;
        tail := head;
      }
    }

    method moveToFront(c: CacheEntry)
      requires c in Items
      requires exists i: nat | 0 <= i < |Items| :: c == Items[i]
      requires Invariant()
      modifies this, Items
      ensures Invariant()
      ensures head.Ptr? && head.deref == c
      ensures multiset(Items) == multiset(old(Items))

    {
      if head.deref != c {
        // This SHOULD creating a new `Ref` object for the cell.
        var toPush := Ptr(c); //   c.prev.deref.next;
        remove(c);
        assert head.deref in Items;
        Items := [toPush.deref] + Items;
        if head.Ptr? {
          head.deref.prev := toPush;
          toPush.deref.next := head;
          head := toPush;
        } else {
          head := toPush;
          tail := head;
        }
      }

      assert (head.Ptr? <==> tail.Ptr?);
    }

    method {:vcs_split_on_every_assert} remove(toRemove: CacheEntry)
      requires Invariant()
      requires toRemove in Items
      modifies this, Items
      ensures Invariant()
      ensures multiset(Items) == multiset(old(Items)) - multiset{toRemove}
      ensures toRemove !in Items
      ensures toRemove.next.Null? && toRemove.prev.Null?
      ensures |Items| < |old(Items)|
    {
      ghost var pos := IndexOfCacheEntry(Items, toRemove);
      // This is s[..pos] + s[pos+1]
      // where pos :| s[pos] == c
      Items := RemoveCacheEntry(Items, toRemove);

      if toRemove.prev.Null? {
        // toRemove is head
        assert toRemove.prev.Null? ==> Ptr(toRemove) == head;
        assert pos == 0;
        head := toRemove.next;
      } else {
        // toRemove is !head
        assert toRemove != head.deref;
        assert 0 != pos;
        assert 0 < |Items|;
        assert Items[pos - 1] == toRemove.prev.deref;
        toRemove.prev.deref.next := toRemove.next;
      }

      if toRemove.next.Null? {
        // toRemove is tail
        assert toRemove.next.Null? ==> Ptr(toRemove) == tail;
        tail := toRemove.prev;
      } else {
        // toRemove is !tail
        assert toRemove != tail.deref;
        assert 0 < |Items|;
        toRemove.next.deref.prev := toRemove.prev;
      }

      label AFTER:

      assert {:split_here} true;
      assert Items == old@AFTER(Items);
      assert toRemove !in Items;

      toRemove.next := NULL;
      toRemove.prev := NULL;
    }
  }

  ghost function {:opaque} RemoveCacheEntry(s: seq<CacheEntry>, v: CacheEntry): (s': seq<CacheEntry>)
    requires multiset(s)[v] == 1
    ensures v !in s'
    ensures multiset(s') == multiset(s) - multiset{v}
    ensures
      var pos := IndexOfCacheEntry(s, v);
      && (forall i: nat | 0 <= i < pos :: s[i] == s'[i])
      && (forall i: nat | pos <= i < |s'| :: s[i+1] == s'[i])
      && (s' == s[..pos] + s[pos+1..])
  {
    var pos := IndexOfCacheEntry(s, v);
    // Associativity, s[pos..] is the sum of both sides
    assert s == s[..pos] + s[pos..];
    // the 1 v MUST be in the right side
    assert multiset(s[pos..])[v] == 1;
    // Associativity, s[pos..] is the sum of both sides
    assert s[pos..] == [s[pos]] + s[pos+1..];
    s[..pos] + s[pos+1..]
  }

  ghost function IndexOfCacheEntry(s: seq<CacheEntry>, v: CacheEntry): (pos: nat)
    requires v in s
    ensures pos < |s| && s[pos] == v
    ensures v !in s[..pos]
  {
    if s[0] == v then 0 else 1 + IndexOfCacheEntry(s[1..], v)
  }

  method RemoveValue<K, V(==)>(k0: K, m: map<K, V>)
    requires k0 in m
    requires forall k <- m, k' <- m | k != k' :: m[k] != m[k']
    ensures (m - {k0}).Values == m.Values - {m[k0]}
  {
    var m' := m - {k0};
    calc {
      m'.Values;
      set k <- m' :: m'[k];
      set k <- m - {k0} :: m[k];
      m.Values - {m[k0]};
    }
  }


  class LocalCMC extends Types.ICryptographicMaterialsCache {

    ghost predicate ValidState()
      ensures ValidState() ==>
                && History in Modifies
                && this in Modifies
    {
      && History in Modifies
      && this in Modifies
    }

    ghost predicate InternalValidState()
      reads this`InternalModifies, InternalModifies
      ensures InternalValidState() ==> History !in InternalModifies
    {
      && History !in InternalModifies
      && this in InternalModifies
      && queue in InternalModifies
      && cache in InternalModifies
                  // I want to say that `queue.Items` is somehow in InternalModifies
      && (forall i <- queue.Items :: i in InternalModifies)
      && Invariant()
    }

    ghost predicate Invariant()
      reads this, queue, queue.Items, cache
    {
      && queue.Invariant()
         // The cache is a cache of Cells, these Cells MUST be unique.
         // The actual value that the Cell contains MAY be a duplicate.
         // See the uniqueness comment on the DoublyLinkedList.Invariant.
      && MutableMapIsInjective(cache)
         // Given that cache.Values and queue.Items are unique
         // they MUST contain exactly the same elements.
      && multiset(cache.Values()) == multiset(queue.Items)
         // To remove the tail the key associated
         // with the tail MUST be in the cache
      && (forall c <- queue.Items :: c.identifier in cache.Keys() && cache.Select(c.identifier) == c)

      && (ValueIsSafeBecauseItIsInMemory(cache.Size()); cache.Size() as uint64 <= entryCapacity)
    }

    var queue: DoublyLinkedCacheEntryList
    var cache: MutableMap<seq<uint8>, CacheEntry>
    //= aws-encryption-sdk-specification/framework/local-cryptographic-materials-cache.md#entry-capacity
    //= type=implication
    //# The local CMC MUST accept entry capacity values between zero
    //# and an implementation-defined maximum, inclusive.
    const entryCapacity: uint64
    //= aws-encryption-sdk-specification/framework/local-cryptographic-materials-cache.md#entry-pruning-tail-size
    //= type=implication
    //# The _entry pruning tail size_
    //# is the number of least recently used entries that the local CMC
    //# MUST check during [pruning](#pruning)
    //# for TTL-expired entries to evict.
    const entryPruningTailSize: uint64

    //= aws-encryption-sdk-specification/framework/local-cryptographic-materials-cache.md#initialization
    //= type=implication
    //# On initialization of the local CMC,
    //# the caller MUST provide the following:
    //# - [Entry Capacity](#entry-capacity)
    //#
    //# The local CMC MUST also define the following:
    //#
    //# - [Entry Pruning Tail Size](#entry-pruning-tail-size)
    constructor(
      entryCapacity': uint64,
      entryPruningTailSize': uint64 := 1
    )
      requires entryPruningTailSize' >= 1
      ensures
        && entryCapacity == entryCapacity'
        && entryPruningTailSize == entryPruningTailSize'
        && ValidState()
        && InternalValidState()
        && fresh(this.Modifies)
        && fresh(this.InternalModifies)
    {
      entryCapacity := entryCapacity';
      entryPruningTailSize := entryPruningTailSize';
      cache := new MutableMap();
      queue := new DoublyLinkedCacheEntryList();

      History := new Types.ICryptographicMaterialsCacheCallHistory();

      Modifies := { History, this };
      InternalModifies := { queue, cache, this };

    }

    ghost predicate GetCacheEntryEnsuresPublicly(input: Types.GetCacheEntryInput, output: Result<Types.GetCacheEntryOutput, Types.Error>)
    {true}

    method GetCacheEntry'(input: Types.GetCacheEntryInput)
      returns (output: Result<Types.GetCacheEntryOutput, Types.Error>)
      requires InternalValidState()
      modifies InternalModifies
      decreases InternalModifies
      ensures InternalValidState()
      ensures GetCacheEntryEnsuresPublicly(input, output)
      ensures unchanged(History)
      ensures InternalModifies <= old(InternalModifies)
    {
      var now := Time.GetCurrent();
      output := GetCacheEntryWithTime(input, now);
    }

    method GetCacheEntryWithTime(input: Types.GetCacheEntryInput, now : Types.PositiveLong)
      returns (output: Result<Types.GetCacheEntryOutput, Types.Error>)
      requires InternalValidState()
      modifies InternalModifies
      decreases InternalModifies
      ensures InternalValidState()
      ensures GetCacheEntryEnsuresPublicly(input, output)
      ensures unchanged(History)
      ensures InternalModifies <= old(InternalModifies)
      ensures output.Success? ==> now <= output.value.expiryTime
    {
      if cache.HasKey(input.identifier) {
        var entry := cache.Select(input.identifier);
        //= aws-encryption-sdk-specification/framework/cryptographic-materials-cache.md#time-to-live-ttl
        //# After a cache entry's TTL has elapsed,
        //# we say that the entry is _TTL-expired_,
        //# and a CMC MUST NOT return the entry to any caller.
        //
        //= aws-encryption-sdk-specification/framework/cryptographic-materials-cache.md#get-cache-entry
        //# The CMC MUST validate that the cache entry
        //# has not exceeded it's stored [TTL](#time-to-live-ttl).
        //
        //= aws-encryption-sdk-specification/framework/local-cryptographic-materials-cache.md#get-cache-entry
        //# The local CMC MUST NOT return any TTL-expired entry.
        if now <= entry.expiryTime {
          // Dafny does not remember the equivalences of seq and multiset(seq)
          assert entry in multiset(queue.Items);
          queue.moveToFront(entry);
          output := Success(Types.GetCacheEntryOutput(
                              materials := entry.materials,
                              creationTime := entry.creationTime,
                              expiryTime := entry.expiryTime,
                              messagesUsed := entry.messagesUsed,
                              bytesUsed := entry.bytesUsed
                            ));
          //= aws-encryption-sdk-specification/framework/local-cryptographic-materials-cache.md#get-cache-entry
          //# When performing a Get Cache Entry operation,
          //# the local CMC MUST [prune TTL-expired cache entries](#pruning).
          var _ :- pruning(now);
        } else {
          // We removed this key,
          // no need to garbage collect
          var _ :- DeleteCacheEntry'(Types.DeleteCacheEntryInput( identifier := input.identifier ));
          output := Failure(Types.EntryDoesNotExist(message := "Entry past TTL"));
        }
      } else {
        output := Failure(Types.EntryDoesNotExist(message := "Entry does not exist"));
      }
    }

    ghost predicate PutCacheEntryEnsuresPublicly(input: Types.PutCacheEntryInput, output: Result<(), Types.Error>)
    {true}

    method {:vcs_split_on_every_assert} PutCacheEntry'(input: Types.PutCacheEntryInput)
      returns (output: Result<(), Types.Error>)
      requires InternalValidState()
      modifies InternalModifies
      decreases InternalModifies
      ensures InternalValidState()
      ensures PutCacheEntryEnsuresPublicly(input, output)
      ensures unchanged(History)
      ensures fresh(InternalModifies - old(InternalModifies))
    {

      if entryCapacity == 0 {
        return Success(());
      }

      if cache.HasKey(input.identifier) {
        var _ :- DeleteCacheEntry'(Types.DeleteCacheEntryInput(
                                     identifier := input.identifier
                                   ));
      }
      assert input.identifier !in cache.Keys();
      assert 0 < entryCapacity;

      //= aws-encryption-sdk-specification/framework/local-cryptographic-materials-cache.md#put-cache-entry
      //# However, before returning the local CMC MUST evict least-recently used entries
      //# until the number of stored entries does not exceed the entry capacity.
      // This is a todo, because this only decrements by 1.
      // While it is true that only 1 is added,
      // this should be a loop.
      //
      //= aws-encryption-sdk-specification/framework/local-cryptographic-materials-cache.md#entry-capacity
      //# The local CMC MUST NOT store more entries than this value,
      //# except temporarily while performing a Put Cache Entry operation.
      if entryCapacity == cache.Size() as uint64 {
        assert 0 < |multiset(cache.Values())|;
        assert queue.tail.deref.identifier in cache.Keys();
        var _ :- DeleteCacheEntry'(Types.DeleteCacheEntryInput(
                                     identifier := queue.tail.deref.identifier
                                   ));
      }

      label CAN_ADD:

      var cell := new CacheEntry(
        materials' := input.materials,
        identifier' := input.identifier,
        creationTime' := input.creationTime,
        expiryTime' := input.expiryTime,
        messagesUsed' := input.messagesUsed.UnwrapOr(0),
        bytesUsed' := input.bytesUsed.UnwrapOr(0)
      );

      if cell in cache.Values() {
        assert cell in multiset(cache.Values());
      }
      //= aws-encryption-sdk-specification/framework/local-cryptographic-materials-cache.md#put-cache-entry
      //= type=exception
      //# While performing a Put Cache Entry operation,
      //# the local CMC MAY store more entries than the entry capacity.
      queue.pushCell(cell);
      cache.Put(input.identifier, cell);
      InternalModifies := InternalModifies + {cell};

      output := Success(());

      forall k <- cache.Keys(), k' <- cache.Keys() | k != k' ensures cache.Select(k) != cache.Select(k') {
        if k != input.identifier && k' != input.identifier {
          assert k in old@CAN_ADD(cache.Keys());
          assert k' in old@CAN_ADD(cache.Keys());
          assert old@CAN_ADD(cache.Select(k)) != old@CAN_ADD(cache.Select(k'));
        }
      }
      assert  (forall c <- queue.Items :: c.identifier in cache.Keys() && cache.Select(c.identifier) == c);
      assert Invariant();
    }

    ghost predicate DeleteCacheEntryEnsuresPublicly(input: Types.DeleteCacheEntryInput, output: Result<(), Types.Error>)
    {true}

    twostate predicate InternalDeleteCacheEntry?(input: Types.DeleteCacheEntryInput, new output: Result<(), Types.Error>)
      requires InternalValidState()
      reads InternalModifies
    {
      && input.identifier !in cache.Keys()
      && (input.identifier in old(cache.Keys())
          ==>
            && (old(cache.Select(input.identifier)) !in queue.Items
                && cache.Size() == old(cache.Size()) - 1
                && old(cache.Keys()) - {input.identifier} == cache.Keys()))
    }

    method {:vcs_split_on_every_assert} DeleteCacheEntry'(input: Types.DeleteCacheEntryInput)
      returns (output: Result<(), Types.Error>)
      requires InternalValidState()
      modifies InternalModifies
      decreases InternalModifies
      ensures InternalValidState()
      ensures DeleteCacheEntryEnsuresPublicly(input, output)
      ensures unchanged(History)
      ensures InternalModifies <= old(InternalModifies)
      ensures InternalDeleteCacheEntry?(input, output)
    {
      if cache.HasKey(input.identifier) {
        assert input.identifier in cache.Keys();
        var cell := cache.Select(input.identifier);
        assert cell in multiset(queue.Items);
        label CAN_REMOVE:
        // Remove from the cache first
        // to keep others from using this value.
        // This is "more" thread safe.
        cache.Remove(input.identifier);
        assert cell !in cache.Values();

        assert MutableMapIsInjective(cache) by {
          // Since the map values are themselves heap objects, we need to check that they too are unchanged
          assert forall k <- cache.Keys() :: old(allocated(cache.Select(k)));
          assert forall k <- cache.Keys() :: unchanged(cache.Select(k));
          assert MutableMapIsInjective(old@CAN_REMOVE(cache));

          assert MutableMapContains(old@CAN_REMOVE(cache), cache);
          LemmaMutableMapContainsPreservesInjectivity(old@CAN_REMOVE(cache), cache);
        }
        assert |cache.Keys()| == |old@CAN_REMOVE(cache.Keys())| - 1;
        assert cache.Size() as uint64 <= old@CAN_REMOVE(cache.Size()) as uint64 <= entryCapacity;
        queue.remove(cell);
        assert multiset(cache.Values()) == multiset(queue.Items) by {
          var cacheMultiset := multiset(cache.Values());
          var queueMultiset := multiset(queue.Items);
          assert cacheMultiset[cell := 0] == queueMultiset[cell := 0];
          assert cell !in cacheMultiset;
          assert cell !in queueMultiset;
        }
        InternalModifies := InternalModifies - {cell};
      }

      output := Success(());
    }

    ghost predicate UpdateUsageMetadataEnsuresPublicly(input: Types.UpdateUsageMetadataInput, output: Result<(), Types.Error>)
    {true}

    method UpdateUsageMetadata'(input: Types.UpdateUsageMetadataInput)
      returns (output: Result<(), Types.Error>)
      requires InternalValidState()
      modifies InternalModifies
      decreases InternalModifies
      ensures InternalValidState()
      ensures InternalModifies <= old(InternalModifies)
    {
      if cache.HasKey(input.identifier) {
        var cell := cache.Select(input.identifier);
        assert cell in multiset(cache.Values());
        if
          && cell.messagesUsed <= INT32_MAX_VALUE - 1
          && cell.bytesUsed <= INT32_MAX_VALUE - input.bytesUsed
        {
          //= aws-encryption-sdk-specification/framework/cryptographic-materials-cache.md#usage-metadata
          //= type=exception
          //# Updating usage metadata SHOULD be atomic.
          // At this time Dafny does not have a way to enforce atomic operations
          // but this syntax attempts to express that intention.
          cell.messagesUsed, cell.bytesUsed := cell.messagesUsed + 1, cell.bytesUsed + input.bytesUsed;
        } else {
          var _ :- DeleteCacheEntry'(Types.DeleteCacheEntryInput(
                                       identifier := input.identifier
                                     ));
        }
      }
      return Success(());
    }

    // Dafny does not have cross language support for background threads
    //= aws-encryption-sdk-specification/framework/local-cryptographic-materials-cache.md#pruning
    //= type=exception
    //# The local CMC SHOULD also periodically evict all TTL-expired entries
    //# among the `N` least recently used entries.

    method pruning(now : Types.PositiveLong)
      returns (output: Result<(), Types.Error>)
      requires InternalValidState()
      modifies InternalModifies
      decreases InternalModifies
      ensures InternalValidState()
      ensures unchanged(History)
      ensures InternalModifies <= old(InternalModifies)
    {
      //= aws-encryption-sdk-specification/framework/local-cryptographic-materials-cache.md#pruning
      //# To prune TTL-expired cache entries,
      //# the local CMC MUST evict all TTL-expired entries
      //# among the `N` least recently used entries,
      //# where `N` is the [Entry Pruning Tail Size](#entry-pruning-tail-size).
      for i := 0 to entryPruningTailSize
        invariant InternalValidState()
        invariant InternalModifies <= old(InternalModifies)
      {
        if queue.tail.Ptr? {
          if queue.tail.deref.expiryTime < now {
            // The tail has timed out,
            // so it should be removed.
            // This should happen regardless
            // of the current size.
            var _ :- DeleteCacheEntry'(Types.DeleteCacheEntryInput(
                                         identifier := queue.tail.deref.identifier
                                       ));
          } else {
            // If this element has not expired,
            // there is no reason to loop,
            // because we will just continue to not process
            // the same single element
            return Success(());
          }
        } else {
          // Similarly, if there is no tail
          // there is no reason to loop,
          // because this loop is a noop.
          return Success(());
        }
      }
      return Success(());
    }
  }

  ghost predicate MutableMapIsInjective<K, V>(m: MutableMap<K, V>)
    reads m
  {
    forall k <- m.Keys(), k' <- m.Keys() | k != k' :: m.Select(k) != m.Select(k')
  }

  ghost predicate MutableMapContains<K, V>(big: MutableMap<K, V>, small: MutableMap<K, V>)
    reads {big, small}
  {
    && small.Keys() <= big.Keys()
    && forall k <- small.Keys() :: small.Select(k) == big.Select(k)
  }

  lemma LemmaMutableMapContainsPreservesInjectivity<K, V>(big: MutableMap<K, V>, small: MutableMap<K, V>)
    requires MutableMapContains(big, small)
    requires MutableMapIsInjective(big)
    ensures MutableMapIsInjective(small)
  {}
}
