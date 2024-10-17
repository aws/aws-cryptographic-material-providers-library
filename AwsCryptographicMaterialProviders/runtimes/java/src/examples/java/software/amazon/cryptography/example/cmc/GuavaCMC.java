package software.amazon.cryptography.example.cmc;

import com.google.common.cache.Cache;
import com.google.common.cache.CacheBuilder;
import java.nio.ByteBuffer;
import javax.annotation.Nullable;
import javax.annotation.concurrent.NotThreadSafe;
import javax.annotation.concurrent.ThreadSafe;
import software.amazon.cryptography.materialproviders.ICryptographicMaterialsCache;
import software.amazon.cryptography.materialproviders.model.CacheType;
import software.amazon.cryptography.materialproviders.model.DeleteCacheEntryInput;
import software.amazon.cryptography.materialproviders.model.EntryDoesNotExist;
import software.amazon.cryptography.materialproviders.model.GetCacheEntryInput;
import software.amazon.cryptography.materialproviders.model.GetCacheEntryOutput;
import software.amazon.cryptography.materialproviders.model.Materials;
import software.amazon.cryptography.materialproviders.model.PutCacheEntryInput;
import software.amazon.cryptography.materialproviders.model.UpdateUsageMetadataInput;

/**
 * <a href="https://github.com/google/guava">Utilize Google's Guava Cache</a>
 * to implement a
 * <a href="https://github.com/awslabs/aws-encryption-sdk-specification/blob/master/framework/cryptographic-materials-cache.md">Cryptographic Materials Cache</a>
 * </p>
 * At this time,
 * we cannot utilize the loader functionality,
 * as the Keyrings and CMMs that utilize the Cache
 * expect an EntryDoesNotExist exception on a cache miss.</p>
 */
public class GuavaCMC {

  /**
   * Guava is responsible for the LRU logic, but the TTL logic is still handled by us.
   * @param threads <a href="https://guava.dev/releases/21.0/api/docs/com/google/common/cache/CacheBuilder.html#concurrencyLevel-int-">Guides the allowed concurrency among update operations.</a>
   * @param initialCapacity <a href="https://guava.dev/releases/21.0/api/docs/com/google/common/cache/CacheBuilder.html#initialCapacity-int-">Sets the minimum total size for the internal hash tables.</a>
   * @param maximumCapacity <a href="https://guava.dev/releases/21.0/api/docs/com/google/common/cache/CacheBuilder.html#maximumSize-long-">Specifies the maximum number of entries the cache may contain.</a>
   * @param trackUsage Not all applications need to track bytes or messages used. Doing so may help some security engineers, but at a performance cost.
   * @return CacheType holding Guava Cache
   */
  public static CacheType create(
    final int threads,
    final int initialCapacity,
    final int maximumCapacity,
    boolean trackUsage
  ) {
    if (threads < 1 || maximumCapacity < 1 || initialCapacity < 1) {
      throw new IllegalArgumentException(
        "threads and maximumCapacity must be greater than 0"
      );
    }
    Cache<ByteBuffer, CacheEntry> guaveCache = CacheBuilder
      .newBuilder()
      .concurrencyLevel(threads)
      .maximumSize(maximumCapacity)
      .initialCapacity(initialCapacity)
      .build();
    ConcurrentCMC cmc = new ConcurrentCMC(guaveCache, trackUsage);
    return CacheType.builder().Shared(cmc).build();
  }

  @ThreadSafe
  public static class ConcurrentCMC implements ICryptographicMaterialsCache {

    private final Cache<ByteBuffer, CacheEntry> cache;
    private final boolean trackUsage;

    public ConcurrentCMC(
      Cache<ByteBuffer, CacheEntry> cache,
      boolean trackUsage
    ) {
      this.cache = cache;
      this.trackUsage = trackUsage;
    }

    @Override
    public void DeleteCacheEntry(DeleteCacheEntryInput input) {
      this.cache.invalidate(input.identifier());
    }

    @Override
    public GetCacheEntryOutput GetCacheEntry(GetCacheEntryInput input) {
      @Nullable
      CacheEntry entry = this.cache.getIfPresent(input.identifier());
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
      if (
        entry != null && Time.__default.CurrentRelativeTime() < entry.expiryTime
      ) {
        if (trackUsage) {
          // Not all applications need to track bytes or messages used.
          // Doing so may help some security engineers, but at a performance cost.
          entry.updateUsage(input.bytesUsed(), 1);
        }
        return entry.toGetCacheEntryOutput();
      } else if (entry != null) {
        this.cache.invalidate(input.identifier());
        // It is CRITICAL that Expired entries are not returned.
        // Additionally, it is CRITICAL that an EntryDoesNotExist exception is thrown
        throw EntryDoesNotExist.builder().message("Entry past TTL.").build();
      }
      // It is CRITICAL that an EntryDoesNotExist exception is thrown for cache miss
      throw EntryDoesNotExist
        .builder()
        .message("Entry does not exist.")
        .build();
    }

    @Override
    public void PutCacheEntry(PutCacheEntryInput input) {
      this.cache.put(input.identifier(), new CacheEntry(input));
    }

    @Override
    public void UpdateUsageMetadata(UpdateUsageMetadataInput input) {
      @Nullable
      CacheEntry entry = this.cache.getIfPresent(input.identifier());
      if (entry != null) {
        entry.updateUsage(input.bytesUsed(), 1);
        this.cache.put(input.identifier(), entry);
      }
    }
  }

  @NotThreadSafe
  public static class CacheEntry {

    private final Materials materials;
    private final Long creationTime;
    private final Long expiryTime;
    private Integer messagesUsed;
    private Integer bytesUsed;

    public CacheEntry(PutCacheEntryInput input) {
      this.materials = input.materials();
      this.creationTime = input.creationTime();
      this.expiryTime = input.expiryTime();
      this.messagesUsed = input.messagesUsed();
      this.bytesUsed = input.bytesUsed();
    }

    public GetCacheEntryOutput toGetCacheEntryOutput() {
      return GetCacheEntryOutput
        .builder()
        .materials(this.materials)
        .creationTime(this.creationTime)
        .expiryTime(this.expiryTime)
        .messagesUsed(Math.toIntExact(this.messagesUsed))
        .bytesUsed(Math.toIntExact(this.bytesUsed))
        .build();
    }

    public void updateUsage(long bytesUsed, int messagesUsed) {
      this.bytesUsed = addLongToInt(bytesUsed, this.bytesUsed);
      this.messagesUsed = addIntToInt(messagesUsed, this.messagesUsed);
    }

    // Edge case where a well-used item exceeds int max.
    private static int addLongToInt(long _long, int _int) {
      if (
        _int == Integer.MAX_VALUE ||
        _long >= Integer.MAX_VALUE ||
        _long + _int >= Integer.MAX_VALUE
      ) {
        return Integer.MAX_VALUE;
      }
      return _int + (int) _long;
    }

    // Edge case where a well-used item exceeds int max.
    private static int addIntToInt(int _int, int _int2) {
      if (
        _int == Integer.MAX_VALUE ||
        _int2 == Integer.MAX_VALUE ||
        (long) _int2 + _int >= Integer.MAX_VALUE
      ) {
        return Integer.MAX_VALUE;
      }
      return _int + _int2;
    }
  }
}
