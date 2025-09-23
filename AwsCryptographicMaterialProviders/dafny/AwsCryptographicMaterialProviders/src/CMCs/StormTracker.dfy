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

  // = aws-encryption-sdk-specification/framework/storm-tracking-cryptographic-materials-cache.md#consistency
  // = type=implication
  // # - The [Grace Interval](#grace-interval) MUST be less than or equal to the [Inflight TTL](#inflight-ttl).

  predicate ConsistentSettings(
    cache: Types.StormTrackingCache
  ) {
    && cache.graceInterval <= cache.gracePeriod
    && cache.inFlightTTL <= cache.gracePeriod
    && cache.graceInterval <= cache.inFlightTTL
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
      reads this, wrapped, wrapped.InternalModifies, inFlight
    {
      && this !in wrapped.InternalModifies
      && inFlight !in wrapped.InternalModifies
      && wrapped.InternalValidState()
      && wrapped.ValidState()
      && 0 < fanOut
      && inFlight.Size() <= fanOut as nat
      && graceInterval <= gracePeriod
      && inFlightTTL <= gracePeriod
    }
    var wrapped : LocalCMC.LocalCMC // the actual cache
    var inFlight: MutableMap<seq<uint8>, Types.PositiveLong> // the time at which this key became in flight
    var gracePeriod : Types.PositiveLong // seconds before expiration that we start putting things in flight
    var graceInterval : Types.PositiveLong // minimum seconds before putting the same key in flight again
    var fanOut : Types.PositiveLong // maximum keys in flight at one time
    var inFlightTTL : Types.PositiveLong // maximum time before a key is no longer in flight
    var lastPrune : Types.PositiveLong // timestamp of last call to PruneInFlight
    var sleepMilli : Types.PositiveLong // how long to sleep, if we sleep

    constructor(
      cache: Types.StormTrackingCache
    )
      requires ConsistentSettings(cache)
      ensures
        && this.ValidState()
        && fresh(this.wrapped)
        && fresh(this.wrapped.InternalModifies)
        && fresh(this.inFlight)
      ensures
        && inFlight.Size() == 0
        && lastPrune == 0
    {
      var gracePeriod, graceInterval, inFlightTTL;
      if cache.timeUnits.UnwrapOr(Types.Seconds).Seconds? {
        gracePeriod := cache.gracePeriod as Types.PositiveLong * 1000;
        graceInterval := cache.graceInterval as Types.PositiveLong * 1000;
        inFlightTTL := cache.inFlightTTL as Types.PositiveLong * 1000;
      } else {
        gracePeriod := cache.gracePeriod as Types.PositiveLong;
        graceInterval := cache.graceInterval as Types.PositiveLong;
        inFlightTTL := cache.inFlightTTL as Types.PositiveLong;
      }

      this.wrapped := new LocalCMC.LocalCMC(cache.entryCapacity as uint64, cache.entryPruningTailSize.UnwrapOr(1) as uint64);
      this.inFlight := new MutableMap((k: seq<uint8>, v: Types.PositiveLong) => true, true);
      this.gracePeriod := gracePeriod;
      this.graceInterval := graceInterval;
      this.fanOut := cache.fanOut as Types.PositiveLong;
      this.inFlightTTL := inFlightTTL;
      this.sleepMilli := cache.sleepMilli as Types.PositiveLong;
      this.lastPrune := 0;
    }

    // return true if InFlight is full
    method FanOutReached(now : Types.PositiveLong) returns (res : bool)
      modifies this`lastPrune, inFlight
      requires ValidState()
      ensures ValidState()
      ensures
        && old(inFlight.Size()) < fanOut as nat
        ==>
          && !res
          && inFlight.content() == old(inFlight.content())
      ensures !res <==> inFlight.Size() < fanOut as nat
      ensures res <==> inFlight.Size() == fanOut as nat
    {
      PruneInFlight(now);
      return fanOut <= inFlight.Size() as Types.PositiveLong;
    }

    function AddLong(x : Types.PositiveLong, y : Types.PositiveLong) : Types.PositiveLong
    {
      if x < (INT64_MAX_LIMIT as Types.PositiveLong - y) then
        x + y
      else
        INT64_MAX_LIMIT as Types.PositiveLong
    }

    lemma ExpiryTimeInSecondsCanBeConvertedToMilliseconds()
      ensures INT64_MAX_LIMIT / 1000 == 0x20C49BA5E353F7
    {}

    predicate GracePeriod?(result: Types.GetCacheEntryOutput, now : Types.PositiveLong)
      : (output: bool)
      reads this`gracePeriod
      requires now / 1000 <= result.expiryTime
      ensures
        output ==>
          && result.expiryTime < 0x20C49BA5E353F7
          // The + 1 comes because (now / 1000) * 1000 <= now
          // Consider (5001 / 1000) <= 5
          // (5001 / 1000) == 5
          // but 5 * 1000 < 5001
          && (result.expiryTime  * 1000) - gracePeriod <= now < (result.expiryTime + 1) * 1000
    {
      // This is just showing where this constant comes from
      // It is so that we know that we can convert
      // the expiryTime from seconds to milliseconds
      // This should get fixed sometime before July 29, 31252
      ExpiryTimeInSecondsCanBeConvertedToMilliseconds();
      && result.expiryTime < 0x20C49BA5E353F7
      && (result.expiryTime  * 1000) - gracePeriod <= now
    }

    // If entry is within `grace time` of expiration, then return EmptyFetch once per `grace interval`,
    // and return cached value otherwise
    method CheckInFlight(identifier: seq<uint8>, result: Types.GetCacheEntryOutput, now : Types.PositiveLong)
      returns (output: CacheState)
      modifies this`lastPrune, inFlight

      // Do check an expired result
      requires now / 1000 <= result.expiryTime

      requires ValidState()
      ensures ValidState()

      // Only return what was passed in
      ensures output.Full? ==> output.data == result

      // Never return an expired entry
      ensures output.Full? ==> now as nat < (result.expiryTime as nat + 1) * 1000

      // EmptyFetch only happens in the grace period
      ensures output.EmptyFetch? ==> GracePeriod?(result, now)

      // Before the grace period
      // ==> Full
      ensures !GracePeriod?(result, now) ==> output.Full?

      // EmptyFetch puts the identifier inFlight
      ensures output.EmptyFetch? ==>
                && inFlight.HasKey(identifier)
                && inFlight.Select(identifier) == now

      // In the grace period,
      // if fanOut has space and the identifier is not inflight
      // ==> EmptyFetch
      ensures
        && GracePeriod?(result, now)
        && old(inFlight.Size()) < fanOut as nat
        && !old(inFlight.HasKey(identifier))
        ==> output.EmptyFetch?

      // In the grace period,
      // if fanOut has space and the identifier is inflight but has not exceed the graceInterval
      // ==> Full
      ensures
        && GracePeriod?(result, now)
        && old(inFlight.Size()) < fanOut as nat
        && old(inFlight.HasKey(identifier))
        && now < AddLong(old(inFlight.Select(identifier)), graceInterval)
        ==> output.Full?

      // In the grace period,
      // if fanOut has space
      // and the identifier is inflight and has been inflight for longer than the graceInterval
      // ==> EmptyFetch
      ensures
        && GracePeriod?(result, now)
        && old(inFlight.Size()) < fanOut as nat
        && old(inFlight.HasKey(identifier))
        && AddLong(old(inFlight.Select(identifier)), graceInterval) <= now
        ==> output.EmptyFetch?

    {
      var fanOutReached := FanOutReached(now);
      if fanOutReached {
        assert inFlight.Size() == fanOut as nat;
        return Full(result);
      } else if !GracePeriod?(result, now) { // lots of time left
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
      requires ValidState()
      ensures ValidState()
      ensures
        old(inFlight.Size()) < fanOut as nat
        ==>
          && inFlight.content() == old(inFlight.content())
          && inFlight.Size() < fanOut as nat
    {
      // Pruning is expensive, so only do it if we have to,
      // i.e. if without pruning, InFlight is full
      // with luck, we will never have to prune
      if inFlight.Size() as Types.PositiveLong < fanOut {
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
      // This list SHOULD be represented by an `array`
      // The mutable map gives fast access to a random value
      // But an array can hold all the values in order
      // Since we only add elements to this array
      // in order of time,
      // the order of elements will naturally be in order.
      // With a little clever work
      // we can iterate over the array backwards
      // and ensure that the elements are in order
      // of decreasing time.
      // That is T[max] is the oldest
      // and T[0] is the most recent.
      var keySet := inFlight.Keys();
      var keys := SortedSets.ComputeSetToSequence(keySet);
      for i : uint64 := 0 to |keys| as uint64
        invariant forall k | i as nat <= k < |keys| :: keys[k] in inFlight.Keys()
        invariant ValidState()
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
      requires ValidState()
      ensures ValidState()

      // Never return an entry
      ensures !output.Full?

      // EmptyFetch puts the identifier inFlight
      ensures output.EmptyFetch? ==>
                && inFlight.HasKey(identifier)
                && inFlight.Select(identifier) == now

      // If fanOut has space and the identifier is not inflight
      // ==> EmptyFetch
      ensures
        && old(inFlight.Size()) < fanOut as nat
        && !old(inFlight.HasKey(identifier))
        ==> output.EmptyFetch?

      // If fanOut has space and the identifier is inflight
      // but has not exceed the graceInterval
      // ==> EmptyWait
      ensures
        && old(inFlight.Size()) < fanOut as nat
        && old(inFlight.HasKey(identifier))
        && now < AddLong(old(inFlight.Select(identifier)), graceInterval)
        ==> output.EmptyWait?

      // If fanOut has space and the identifier is inflight
      // and has been inflight for longer
      // than the the graceInterval
      // ==> EmptyFetch
      ensures
        && old(inFlight.Size()) < fanOut as nat
        && old(inFlight.HasKey(identifier))
        && AddLong(old(inFlight.Select(identifier)), graceInterval) <= now
        ==> output.EmptyFetch?

    {
      var fanOutReached := FanOutReached(now);
      if fanOutReached {
        return EmptyWait;
      } else if inFlight.HasKey(identifier) {
        var entry := inFlight.Select(identifier);
        // We want to return EmptyWait as little as possible.
        // We want to wait (return EmptyWait) for the smallest duration.
        // This is most important if the entries are consistently failing.
        // We do not want the system to back up waiting to try to fail.
        // See the extern to observe how inFlightTTL
        // is used with EmptyWait
        if now < AddLong(entry, graceInterval) {  // already returned an EmptyFetch for this interval
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
      // The wrapped CMC is a LocalCMC that uses Seconds.
      var result := wrapped.GetCacheEntryWithTime(input, now / 1000);
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
