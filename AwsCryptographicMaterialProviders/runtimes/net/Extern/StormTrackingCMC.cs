// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

using System;
using System.Collections.Concurrent;
using System.Threading;
using DafnyTypes = software.amazon.cryptography.materialproviders.internaldafny.types;

// Re-use ByteArrayKey and CacheEntry from SynchronizedLocalCMC
using software.amazon.cryptography.internaldafny.SynchronizedLocalCMC;

namespace software.amazon.cryptography.internaldafny.StormTrackingCMC
{
    internal class InFlightEntry
    {
        public long Timestamp;
        public readonly ManualResetEventSlim Signal = new ManualResetEventSlim(false);
    }

    public partial class StormTrackingCMC : DafnyTypes.ICryptographicMaterialsCache
    {
        private readonly ConcurrentDictionary<ByteArrayKey, CacheEntry> _cache = new();
        private readonly ConcurrentDictionary<ByteArrayKey, InFlightEntry> _inFlight = new();
        private readonly int _capacity;

        private readonly long _gracePeriod;      // milliseconds
        private readonly long _graceInterval;    // milliseconds
        private readonly long _fanOut;
        private readonly long _inFlightTTL;      // milliseconds
        private readonly int _sleepMilli;

        private const int INT32_SAFE_MAX = 0x79999999;

        public StormTrackingCMC(StormTracker_Compile.StormTracker cmc)
        {
            _capacity = (int)cmc.wrapped.entryCapacity;
            if (_capacity < 1) _capacity = 1;
            _gracePeriod = cmc.gracePeriod;
            _graceInterval = cmc.graceInterval;
            _fanOut = cmc.fanOut;
            _inFlightTTL = cmc.inFlightTTL;
            _sleepMilli = (int)cmc.sleepMilli;
        }

        private static long NowMillis() => (long)(DateTime.Now - DateTime.MinValue).TotalMilliseconds;

        private void EvictIfNeeded()
        {
            while (_cache.Count >= _capacity)
            {
                ByteArrayKey oldestKey = default;
                long oldestTime = long.MaxValue;
                foreach (var kvp in _cache)
                {
                    long accessed = Interlocked.Read(ref kvp.Value.LastAccessed);
                    if (accessed < oldestTime)
                    {
                        oldestTime = accessed;
                        oldestKey = kvp.Key;
                    }
                }
                _cache.TryRemove(oldestKey, out _);
            }
        }

        // ---- GetCacheEntry: the main entry point ----

        public Wrappers_Compile._IResult<DafnyTypes._IGetCacheEntryOutput, DafnyTypes._IError>
            GetCacheEntry(DafnyTypes._IGetCacheEntryInput input)
        {
            return GetCacheEntry_k(input);
        }

        public Wrappers_Compile._IResult<DafnyTypes._IGetCacheEntryOutput, DafnyTypes._IError>
            GetCacheEntry_k(DafnyTypes._IGetCacheEntryInput input)
        {
            var concrete = (DafnyTypes.GetCacheEntryInput)input;
            var key = new ByteArrayKey(concrete._identifier);
            long maxWaitUntil = NowMillis() + _inFlightTTL;

            while (true)
            {
                var state = GetFromCache(key);

                switch (state)
                {
                    case CacheState.Full full:
                        return Wrappers_Compile.Result<DafnyTypes._IGetCacheEntryOutput, DafnyTypes._IError>
                            .create_Success(new DafnyTypes.GetCacheEntryOutput(
                                full.Entry.Materials, full.Entry.CreationTime,
                                full.Entry.ExpiryTime, full.Entry.MessagesUsed, full.Entry.BytesUsed));

                    case CacheState.EmptyFetch:
                        return Wrappers_Compile.Result<DafnyTypes._IGetCacheEntryOutput, DafnyTypes._IError>
                            .create_Failure(DafnyTypes.Error.create_EntryDoesNotExist(
                                Dafny.Sequence<char>.FromString("Entry does not exist")));

                    case CacheState.EmptyWait wait:
                        if (NowMillis() > maxWaitUntil)
                        {
                            return Wrappers_Compile.Result<DafnyTypes._IGetCacheEntryOutput, DafnyTypes._IError>
                                .create_Failure(DafnyTypes.Error.create_InFlightTTLExceeded(
                                    Dafny.Sequence<char>.FromString("Storm cache inFlightTTL exceeded")));
                        }
                        wait.Signal.Wait(_sleepMilli);
                        break;
                }
            }
        }

        // ---- Storm tracking state machine ----

        private CacheState GetFromCache(ByteArrayKey key)
        {
            long now = NowMillis();
            long nowSec = now / 1000;

            if (_cache.TryGetValue(key, out var entry))
            {
                // TTL expired
                if (nowSec > entry.ExpiryTime)
                {
                    _cache.TryRemove(key, out _);
                    return CheckNewEntry(key, now);
                }

                Interlocked.Exchange(ref entry.LastAccessed, now);

                // Check if in grace period
                bool inGracePeriod = entry.ExpiryTime < 0x20C49BA5E353F7L
                    && (entry.ExpiryTime * 1000) - _gracePeriod <= now;

                if (!inGracePeriod)
                    return new CacheState.Full(entry);

                return CheckInFlight(key, entry, now);
            }

            return CheckNewEntry(key, now);
        }

        private CacheState CheckInFlight(ByteArrayKey key, CacheEntry entry, long now)
        {
            PruneInFlight(now);
            if (_inFlight.Count >= _fanOut)
                return new CacheState.Full(entry);

            if (_inFlight.TryGetValue(key, out var existing))
            {
                if (now < Interlocked.Read(ref existing.Timestamp) + _graceInterval)
                    return new CacheState.Full(entry);

                Interlocked.Exchange(ref existing.Timestamp, now);
                return CacheState.EmptyFetch.Instance;
            }

            _inFlight[key] = new InFlightEntry { Timestamp = now };
            return CacheState.EmptyFetch.Instance;
        }

        private CacheState CheckNewEntry(ByteArrayKey key, long now)
        {
            PruneInFlight(now);
            if (_inFlight.Count >= _fanOut)
                return new CacheState.EmptyWait(null);

            if (_inFlight.TryGetValue(key, out var existing))
            {
                if (now < Interlocked.Read(ref existing.Timestamp) + _graceInterval)
                    return new CacheState.EmptyWait(existing.Signal);

                Interlocked.Exchange(ref existing.Timestamp, now);
                return CacheState.EmptyFetch.Instance;
            }

            var inFlightEntry = new InFlightEntry { Timestamp = now };
            _inFlight[key] = inFlightEntry;
            return CacheState.EmptyFetch.Instance;
        }

        private void PruneInFlight(long now)
        {
            if (_inFlight.Count < _fanOut) return;

            foreach (var kvp in _inFlight)
            {
                if (now >= Interlocked.Read(ref kvp.Value.Timestamp) + _inFlightTTL)
                {
                    _inFlight.TryRemove(kvp.Key, out _);
                }
            }
        }

        // ---- PutCacheEntry: fills cache and wakes waiters ----

        public Wrappers_Compile._IResult<_System._ITuple0, DafnyTypes._IError>
            PutCacheEntry(DafnyTypes._IPutCacheEntryInput input)
        {
            return PutCacheEntry_k(input);
        }

        public Wrappers_Compile._IResult<_System._ITuple0, DafnyTypes._IError>
            PutCacheEntry_k(DafnyTypes._IPutCacheEntryInput input)
        {
            var concrete = (DafnyTypes.PutCacheEntryInput)input;
            var key = new ByteArrayKey(concrete._identifier);

            var entry = new CacheEntry(
                concrete._identifier, concrete._materials,
                concrete._creationTime, concrete._expiryTime,
                concrete._messagesUsed.is_Some ? (int)concrete._messagesUsed.dtor_value : 0,
                concrete._bytesUsed.is_Some ? (int)concrete._bytesUsed.dtor_value : 0);

            _cache[key] = entry;
            EvictIfNeeded();

            if (_inFlight.TryRemove(key, out var inFlightEntry))
            {
                inFlightEntry.Signal.Set();
            }

            return Wrappers_Compile.Result<_System._ITuple0, DafnyTypes._IError>
                .create_Success(_System.Tuple0.create());
        }

        // ---- DeleteCacheEntry ----

        public Wrappers_Compile._IResult<_System._ITuple0, DafnyTypes._IError>
            DeleteCacheEntry(DafnyTypes._IDeleteCacheEntryInput input)
        {
            return DeleteCacheEntry_k(input);
        }

        public Wrappers_Compile._IResult<_System._ITuple0, DafnyTypes._IError>
            DeleteCacheEntry_k(DafnyTypes._IDeleteCacheEntryInput input)
        {
            var concrete = (DafnyTypes.DeleteCacheEntryInput)input;
            var key = new ByteArrayKey(concrete._identifier);
            _cache.TryRemove(key, out _);
            if (_inFlight.TryRemove(key, out var inFlightEntry))
            {
                inFlightEntry.Signal.Set();
            }
            return Wrappers_Compile.Result<_System._ITuple0, DafnyTypes._IError>
                .create_Success(_System.Tuple0.create());
        }

        // ---- UpdateUsageMetadata ----

        public Wrappers_Compile._IResult<_System._ITuple0, DafnyTypes._IError>
            UpdateUsageMetadata(DafnyTypes._IUpdateUsageMetadataInput input)
        {
            return UpdateUsageMetadata_k(input);
        }

        public Wrappers_Compile._IResult<_System._ITuple0, DafnyTypes._IError>
            UpdateUsageMetadata_k(DafnyTypes._IUpdateUsageMetadataInput input)
        {
            var concrete = (DafnyTypes.UpdateUsageMetadataInput)input;
            var key = new ByteArrayKey(concrete._identifier);

            if (_cache.TryGetValue(key, out var entry))
            {
                if (entry.MessagesUsed <= INT32_SAFE_MAX - 1
                    && entry.BytesUsed <= INT32_SAFE_MAX - concrete._bytesUsed)
                {
                    Interlocked.Increment(ref entry.MessagesUsed);
                    Interlocked.Add(ref entry.BytesUsed, concrete._bytesUsed);
                }
                else
                {
                    _cache.TryRemove(key, out _);
                }
            }

            return Wrappers_Compile.Result<_System._ITuple0, DafnyTypes._IError>
                .create_Success(_System.Tuple0.create());
        }

        // Also expose GetFromCacheInner for compatibility with transpiled code
        public Wrappers_Compile._IResult<StormTracker_Compile._ICacheState, DafnyTypes._IError>
            GetFromCacheInner(DafnyTypes._IGetCacheEntryInput input)
        {
            throw new NotSupportedException("Native StormTrackingCMC does not use GetFromCacheInner");
        }
    }

    // ---- Cache state discriminated union ----

    internal abstract class CacheState
    {
        internal class Full : CacheState
        {
            public readonly CacheEntry Entry;
            public Full(CacheEntry entry) { Entry = entry; }
        }

        internal class EmptyFetch : CacheState
        {
            public static readonly EmptyFetch Instance = new EmptyFetch();
        }

        internal class EmptyWait : CacheState
        {
            public readonly ManualResetEventSlim Signal;
            public EmptyWait(ManualResetEventSlim signal) { Signal = signal; }
        }
    }
}
