// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

// A StormTracker wraps a LocalCMC, and prevents KMS storms
//
// NOT an ICryptographicMaterialsCache, because it implements GetFromCache
// instead of GetCacheEntry, to distinguish 'no data so sleep' from 'no data so get some'
//
// If an item in the cache is about to expire, return occasional 'data not found'
// so that the cache can be refreshed before all the threads suddenly need data
// giving all other threads the cached data
//
// If an item is not in the cache, return occasional 'data not found'
// so that the cache can be refreshed,
// forcing all other threads to sleep

include "LocalCMC.dfy"

module {:options "/functionSyntax:4" }  StormTracker {
  import opened Wrappers
  import opened StandardLibrary.UInt
  import opened DafnyLibraries
  import Types = AwsCryptographyMaterialProvidersTypes
  import LocalCMC
  import Time
  import SortedSets
  import Seq
  import StandardLibrary.String

  datatype CacheState =
    | EmptyWait // No data, client should wait
    | EmptyFetch // No data, client should fetch
    | Full(data : Types.GetCacheEntryOutput)

  function DefaultStorm() : Types.StormTrackingCache
  {
    Types.StormTrackingCache(
      entryCapacity := 1000,
      entryPruningTailSize := Some(1),
      gracePeriod := 10 * 1000,
      graceInterval := 1 * 1000,
      fanOut := 20,
      inFlightTTL := 10 * 1000,
      sleepMilli := 20,
      timeUnits := Some(Types.Milliseconds)
    )
  }

  // = aws-encryption-sdk-specification/framework/storm-tracking-cryptographic-materials-cache.md#consistency
  // = type=implication
  // # - The [Grace Interval](#grace-interval) MUST be less than or equal to the [Grace Period](#grace-period).

  // = aws-encryption-sdk-specification/framework/storm-tracking-cryptographic-materials-cache.md#consistency
  // = type=implication
  // # - The [Inflight TTL](#inflight-ttl) MUST be less than or equal to the [Grace Period](#grace-period).

  // Update the spec.
  // It was assuming that we are always in a happy place.
  // However, if the cache is empty and the system is unable to populate the cache
  // because the item is generally failing,
  // then would result in the system backing up
  // and both processing everything serially,
  // but also waiting the maximum duration between attempts.

  // = aws-encryption-sdk-specification/framework/storm-tracking-cryptographic-materials-cache.md#consistency
  // = type=exception
  // # - The [Grace Interval](#grace-interval) MUST be less than or equal to the [Inflight TTL](#inflight-ttl).

  predicate ConsistentSettings(
    cache: Types.StormTrackingCache
  ) {
    && cache.graceInterval <= cache.gracePeriod
    && cache.inFlightTTL <= cache.gracePeriod
  }

  function N(n : Types.CountingNumber) : string {
    String.Base10Int2String(n as int)
  }

  function BadCacheMsg(cache: Types.StormTrackingCache) : string
    requires !ConsistentSettings(cache)
  {
    var msg := "For a StormCache : ";

    var msg := msg +

               if !(cache.graceInterval <= cache.gracePeriod) then
                 "graceInterval must not exceed gracePeriod, yet configuration has graceInterval="
                 + N(cache.graceInterval) + " and gracePeriod=" + N(cache.gracePeriod) + ". "
               else
                 "";

    var msg := msg +
               if !(cache.inFlightTTL <= cache.gracePeriod) then
                 "inFlightTTL must not exceed gracePeriod, yet configuration has inFlightTTL="
                 + N(cache.inFlightTTL) + " and gracePeriod=" + N(cache.gracePeriod) + ". "
               else
                 "";

    var msg := msg +
               if !(cache.graceInterval <= cache.inFlightTTL) then
                 "graceInterval must not exceed inFlightTTL, yet configuration has graceInterval="
                 + N(cache.graceInterval) + " and inFlightTTL=" + N(cache.inFlightTTL) + ". "
               else
                 "";

    msg
  }

  function CheckSettings(
    cache: Types.StormTrackingCache
  ) : (res : Outcome<Types.Error> )
    ensures res.Pass? ==> ConsistentSettings(cache)
  {
    if ConsistentSettings(cache) then
      Pass
    else
      Fail(Types.AwsCryptographicMaterialProvidersException(message := BadCacheMsg(cache)))
  }

  class StormTracker {

    ghost predicate ValidState()
      reads this, wrapped, wrapped.InternalModifies
    {
      && this !in wrapped.InternalModifies
      && inFlight !in wrapped.InternalModifies
      && wrapped.InternalValidState()
      && wrapped.ValidState()
    }
    var wrapped : LocalCMC.LocalCMC // the actual cache
    const inFlight: MutableMap<seq<uint8>, Types.PositiveLong> // the time at which this key became in flight
    const gracePeriod : Types.PositiveLong // seconds before expiration that we start putting things in flight
    const graceInterval : Types.PositiveLong // minimum seconds before putting the same key in flight again
    const fanOut : Types.PositiveLong // maximum keys in flight at one time
    const inFlightTTL : Types.PositiveLong // maximum time before a key is no longer in flight
    var lastPrune : Types.PositiveLong // timestamp of last call to PruneInFlight
    const sleepMilli : Types.PositiveLong // how long to sleep, if we sleep

    constructor(
      nameonly ghost cache: Types.StormTrackingCache,
      nameonly entryCapacity: nat,
      nameonly entryPruningTailSize: nat,
      nameonly gracePeriod: Types.PositiveLong,
      nameonly graceInterval: Types.PositiveLong,
      nameonly fanOut: Types.PositiveLong,
      nameonly inFlightTTL: Types.PositiveLong,
      nameonly sleepMilli: Types.PositiveLong
    )
      requires ConsistentSettings(cache)
      // By changing the constructor parameters to Types.PositiveLong
      // the math between Seconds and Milliseconds will never be outside of our bounded int.
      // However, this means that we need to rebuild the consistency between
      // the storm cache options and the input variables needs work.
      // This way the cache only ever needs to deal with milliseconds.
      requires
        && (if cache.timeUnits.Some? && cache.timeUnits.value.Milliseconds? then
              && gracePeriod == cache.gracePeriod as Types.PositiveLong
              && graceInterval == cache.graceInterval as Types.PositiveLong
              && inFlightTTL == cache.inFlightTTL as Types.PositiveLong
            else
              && cache.timeUnits.UnwrapOr(Types.Seconds).Seconds?
              && gracePeriod == cache.gracePeriod as Types.PositiveLong * 1000
              && graceInterval == cache.graceInterval as Types.PositiveLong * 1000
              && inFlightTTL == cache.inFlightTTL as Types.PositiveLong * 1000
           )

        && entryCapacity == cache.entryCapacity as nat
        && entryPruningTailSize == cache.entryPruningTailSize.UnwrapOr(1) as nat
        && fanOut == cache.fanOut as Types.PositiveLong
        && sleepMilli == cache.sleepMilli as Types.PositiveLong
      ensures
        && this.ValidState()
        && fresh(this.wrapped)
        && fresh(this.wrapped.InternalModifies)
        && fresh(this.inFlight)
    {
      this.wrapped := new LocalCMC.LocalCMC(entryCapacity, entryPruningTailSize);
      this.inFlight := new MutableMap();
      this.gracePeriod := gracePeriod;
      this.graceInterval := graceInterval;
      this.fanOut := fanOut;
      this.inFlightTTL := inFlightTTL;
      this.sleepMilli := sleepMilli;
      this.lastPrune := 0;
    }

    function InFlightSize() : Types.PositiveLong
      reads this, this.inFlight
    {
      var x := inFlight.Size();
      assert x >= 0;
      if x <= INT64_MAX_LIMIT then
        x as Types.PositiveLong
      else
        INT64_MAX_LIMIT as Types.PositiveLong
    }

    // return true if InFlight is full
    method FanOutReached(now : Types.PositiveLong) returns (res : bool)
      modifies this`lastPrune, inFlight
    {
      PruneInFlight(now);
      return fanOut <= InFlightSize();
    }

    function AddLong(x : Types.PositiveLong, y : Types.PositiveLong) : Types.PositiveLong
    {
      if x < (INT64_MAX_LIMIT as Types.PositiveLong - y) then
        x + y
      else
        INT64_MAX_LIMIT as Types.PositiveLong
    }

    // If entry is within `grace time` of expiration, then return EmptyFetch once per `grace interval`,
    // and return cached value otherwise
    method CheckInFlight(identifier: seq<uint8>, result: Types.GetCacheEntryOutput, now : Types.PositiveLong)
      returns (output: CacheState)
      modifies this`lastPrune, inFlight
    {
      var fanOutReached := FanOutReached(now);
      if fanOutReached {
        return Full(result);
      } else if result.expiryTime <= now { // expired? should be impossible
        output := CheckNewEntry(identifier, now);
      } else if now < result.expiryTime - gracePeriod { // lots of time left
        return Full(result);
      } else { // in grace time
        if inFlight.HasKey(identifier) {
          var entry := inFlight.Select(identifier);
          if AddLong(entry, graceInterval) > now {  // already returned an EmptyFetch for this interval
            return Full(result);
          }
        }
        inFlight.Put(identifier, now);
        return EmptyFetch;
      }
    }

    // If InFlight is at maximum, see if any entries are too old
    method PruneInFlight(now : Types.PositiveLong)
      modifies this`lastPrune, inFlight
    {
      // Pruning is expensive, so only do it if we have to,
      // i.e. if without pruning, InFlight is full
      // with luck, we will never have to prune
      if fanOut > InFlightSize() {
        return;
      }

      // We don't need to check more than once per second,
      // because we would have already removed everything that expired in that second.
      // The units for the various values used to be seconds.
      // Now that these units are all in milliseconds,
      // it is not reasonable to prune every millisecond.
      if now - 1000 < lastPrune {
        return;
      }

      lastPrune := now;
      var keySet := inFlight.Keys();
      var keys := SortedSets.ComputeSetToSequence(keySet);
      for i := 0 to |keys|
        invariant forall k | i <= k < |keys| :: keys[k] in inFlight.Keys()
      {
        reveal Seq.HasNoDuplicates();
        var v := inFlight.Select(keys[i]);
        if now >= AddLong(v, inFlightTTL) {
          inFlight.Remove(keys[i]);
        }
      }
    }

    // If entry is not in cache, then return EmptyFetch once per second, and EmptyWait otherwise
    method CheckNewEntry(identifier: seq<uint8>, now : Types.PositiveLong)
      returns (output: CacheState)
      modifies this`lastPrune, inFlight
    {
      var fanOutReached := FanOutReached(now);
      if fanOutReached {
        return EmptyWait;
      } else if inFlight.HasKey(identifier) {
        var entry := inFlight.Select(identifier);
        // We want to return EmptyWait as little as possible.
        // We want to wait (return EmptyWait) for the smallest duration.
        // We will only return EmptyWait if we are within *both* durations.
        // This is because we are in an empty cache state,
        // and want to give the system the maximum opportunity
        // to populate the cache.
        // This is most important if the entries are consistently failing.
        // We do not want the system to back up waiting to try to fail.
        if
          && now < AddLong(entry, inFlightTTL)
          && now < AddLong(entry, graceInterval)
        {  // already returned an EmptyFetch for this interval
          return EmptyWait;
        }
      }
      inFlight.Put(identifier, now);
      return EmptyFetch;
    }

    // Pass in timestamp for easier testing
    method GetFromCacheWithTime(input: Types.GetCacheEntryInput, now : Types.PositiveLong)
      returns (output: Result<CacheState, Types.Error>)
      requires ValidState()
      modifies this`lastPrune, inFlight, wrapped.InternalModifies
      ensures ValidState()
      ensures inFlight == old(inFlight)
      ensures wrapped == old(wrapped)
      ensures wrapped.InternalModifies <= old(wrapped.InternalModifies)
    {
      var result := wrapped.GetCacheEntryWithTime(input, now);
      if result.Success? {
        var newResult := CheckInFlight(input.identifier, result.value, now);
        return Success(newResult);
      } else if result.error.EntryDoesNotExist? {
        var newResult := CheckNewEntry(input.identifier, now);
        return Success(newResult);
      } else {
        return Failure(result.error);
      }
    }

    method GetFromCache(input: Types.GetCacheEntryInput)
      returns (output: Result<CacheState, Types.Error>)
      requires ValidState()
      modifies this`lastPrune, inFlight, wrapped.InternalModifies
      ensures ValidState()
      ensures inFlight == old(inFlight)
      ensures wrapped == old(wrapped)
      ensures wrapped.InternalModifies <= old(wrapped.InternalModifies)
    {
      var now := Time.GetCurrentMilli();
      output := GetFromCacheWithTime(input, now);
    }

    // This should not be used directly.
    // If we needed StormTracker to be an ICryptographicMaterialsCache, this would be needed
    // It is also useful because Dafny generates almost the right code for the native StormTrackingCMC
    method GetCacheEntry(input: Types.GetCacheEntryInput)
      returns (output: Result<Types.GetCacheEntryOutput, Types.Error>)
      requires ValidState()
      modifies this`lastPrune, inFlight, wrapped.InternalModifies
      ensures ValidState()
      ensures inFlight == old(inFlight)
      ensures wrapped == old(wrapped)
      ensures wrapped.InternalModifies <= old(wrapped.InternalModifies)
    {
      var result := GetFromCache(input);
      if result.Failure? {
        return Failure(result.error);
      } else if result.value.Full? {
        return Success(result.value.data);
      } else {
        return Failure(Types.EntryDoesNotExist(message := "Entry does not exist"));
      }
    }

    method PutCacheEntry(input: Types.PutCacheEntryInput)
      returns (output: Result<(), Types.Error>)
      requires ValidState()
      modifies inFlight, wrapped.InternalModifies
      ensures ValidState()
      ensures inFlight == old(inFlight)
      ensures wrapped == old(wrapped)
      ensures fresh(wrapped.InternalModifies - old(wrapped.InternalModifies))
    {
      inFlight.Remove(input.identifier);
      output := wrapped.PutCacheEntry'(input);
    }

    method DeleteCacheEntry(input: Types.DeleteCacheEntryInput)
      returns (output: Result<(), Types.Error>)
      requires ValidState()
      modifies inFlight, wrapped.InternalModifies
      ensures ValidState()
      ensures wrapped.InternalModifies <= old(wrapped.InternalModifies)
    {
      inFlight.Remove(input.identifier);
      output := wrapped.DeleteCacheEntry'(input);
    }

    method UpdateUsageMetadata(input: Types.UpdateUsageMetadataInput)
      returns (output: Result<(), Types.Error>)
      requires ValidState()
      modifies inFlight, wrapped.InternalModifies
      ensures ValidState()
    {
      output := wrapped.UpdateUsageMetadata'(input);
    }
  }
}
