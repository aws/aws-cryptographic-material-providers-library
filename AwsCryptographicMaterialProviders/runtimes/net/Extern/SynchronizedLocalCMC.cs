// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

using System;
using System.Threading;
using BitFaster.Caching.Lru;
using DafnyTypes = software.amazon.cryptography.materialproviders.internaldafny.types;

namespace software.amazon.cryptography.internaldafny.SynchronizedLocalCMC
{
  internal readonly struct ByteArrayKey : IEquatable<ByteArrayKey>
  {
    private readonly byte[] _bytes;
    private readonly int _hash;

    public ByteArrayKey(Dafny.ISequence<byte> dafnyBytes)
    {
      _bytes = dafnyBytes.CloneAsArray();
      unchecked
      {
        int hash = (int)2166136261;
        for (int i = 0; i < _bytes.Length; i++)
          hash = (hash ^ _bytes[i]) * 16777619;
        _hash = hash;
      }
    }

    public bool Equals(ByteArrayKey other) =>
        _bytes.AsSpan().SequenceEqual(other._bytes.AsSpan());

    public override bool Equals(object obj) => obj is ByteArrayKey other && Equals(other);
    public override int GetHashCode() => _hash;
  }

  internal class CacheEntry
  {
    public readonly Dafny.ISequence<byte> Identifier;
    public readonly DafnyTypes._IMaterials Materials;
    public readonly long CreationTime;
    public readonly long ExpiryTime;
    public int MessagesUsed;
    public int BytesUsed;

    public CacheEntry(
        Dafny.ISequence<byte> identifier,
        DafnyTypes._IMaterials materials,
        long creationTime,
        long expiryTime,
        int messagesUsed,
        int bytesUsed)
    {
      Identifier = identifier;
      Materials = materials;
      CreationTime = creationTime;
      ExpiryTime = expiryTime;
      MessagesUsed = messagesUsed;
      BytesUsed = bytesUsed;
    }
  }

  public partial class SynchronizedLocalCMC : DafnyTypes.ICryptographicMaterialsCache
  {
    private readonly ConcurrentLru<ByteArrayKey, CacheEntry> _cache;
    private const int INT32_SAFE_MAX = 0x79999999;

    public SynchronizedLocalCMC(LocalCMC_Compile.LocalCMC cmc)
    {
      int capacity = (int)cmc.entryCapacity;
      _cache = new ConcurrentLru<ByteArrayKey, CacheEntry>(capacity < 1 ? 1 : capacity);
    }

    private static long Now() => (long)(DateTime.Now - DateTime.MinValue).TotalSeconds;

    // ---- GetCacheEntry ----

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

      if (!_cache.TryGet(key, out var entry))
        return CreateGetFailure("Entry does not exist");

      if (Now() > entry.ExpiryTime)
      {
        _cache.TryRemove(key);
        return CreateGetFailure("Entry past TTL");
      }

      return Wrappers_Compile.Result<DafnyTypes._IGetCacheEntryOutput, DafnyTypes._IError>
          .create_Success(new DafnyTypes.GetCacheEntryOutput(
              entry.Materials, entry.CreationTime, entry.ExpiryTime,
              entry.MessagesUsed, entry.BytesUsed));
    }

    // ---- PutCacheEntry ----

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

      _cache.AddOrUpdate(key, entry);
      return CreateVoidSuccess();
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
      _cache.TryRemove(new ByteArrayKey(concrete._identifier));
      return CreateVoidSuccess();
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

      if (_cache.TryGet(key, out var entry))
      {
        if (entry.MessagesUsed <= INT32_SAFE_MAX - 1
            && entry.BytesUsed <= INT32_SAFE_MAX - concrete._bytesUsed)
        {
          Interlocked.Increment(ref entry.MessagesUsed);
          Interlocked.Add(ref entry.BytesUsed, concrete._bytesUsed);
        }
        else
        {
          _cache.TryRemove(key);
        }
      }

      return CreateVoidSuccess();
    }

    // ---- Helpers ----

    private static Wrappers_Compile._IResult<DafnyTypes._IGetCacheEntryOutput, DafnyTypes._IError>
        CreateGetFailure(string message)
    {
      return Wrappers_Compile.Result<DafnyTypes._IGetCacheEntryOutput, DafnyTypes._IError>
          .create_Failure(DafnyTypes.Error.create_EntryDoesNotExist(
              Dafny.Sequence<char>.FromString(message)));
    }

    private static Wrappers_Compile._IResult<_System._ITuple0, DafnyTypes._IError>
        CreateVoidSuccess()
    {
      return Wrappers_Compile.Result<_System._ITuple0, DafnyTypes._IError>
          .create_Success(_System.Tuple0.create());
    }
  }
}
