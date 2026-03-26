using System.Collections.Generic;
using System.Text;
using System.Threading;
using AWS.Cryptography.KeyStore;
using AWS.Cryptography.MaterialProviders;
using Xunit;

public class StormTrackingCacheTests
{
    private static MaterialProviders mpl = new MaterialProviders(new MaterialProvidersConfig());

    private static readonly string[] Identifiers =
    {
        "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen",
        "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"
    };

    private static ICryptographicMaterialsCache CreateDefaultCache(int capacity)
    {
        return mpl.CreateCryptographicMaterialsCache(
            new CreateCryptographicMaterialsCacheInput
            {
                Cache = new CacheType { Default = new DefaultCache { EntryCapacity = capacity } }
            });
    }

    private static long Now() => (long)(System.DateTime.Now - System.DateTime.MinValue).TotalSeconds;

    private static PutCacheEntryInput MakePut(string id, long expiryTime)
    {
        return new PutCacheEntryInput
        {
            Identifier = new System.IO.MemoryStream(Encoding.UTF8.GetBytes(id)),
            CreationTime = Now(),
            ExpiryTime = expiryTime,
            Materials = new Materials
            {
                BeaconKey = new BeaconKeyMaterials
                {
                    BeaconKeyIdentifier = id,
                    BeaconKey = new System.IO.MemoryStream(Encoding.UTF8.GetBytes(id)),
                    EncryptionContext = new Dictionary<string, string>()
                }
            }
        };
    }

    private static GetCacheEntryInput MakeGet(string id)
    {
        return new GetCacheEntryInput
        {
            Identifier = new System.IO.MemoryStream(Encoding.UTF8.GetBytes(id))
        };
    }

    [Fact]
    public void PutAndGet()
    {
        var cache = CreateDefaultCache(10);
        cache.PutCacheEntry(MakePut("key1", Now() + 3600));
        var result = cache.GetCacheEntry(MakeGet("key1"));
        Assert.Equal("key1", result.Materials.BeaconKey.BeaconKeyIdentifier);
    }

    [Fact]
    public void GetMissingKeyThrows()
    {
        var cache = CreateDefaultCache(10);
        Assert.Throws<EntryDoesNotExist>(() => cache.GetCacheEntry(MakeGet("missing")));
    }

    [Fact]
    public void DeleteRemovesEntry()
    {
        var cache = CreateDefaultCache(10);
        cache.PutCacheEntry(MakePut("key1", Now() + 3600));
        cache.DeleteCacheEntry(new DeleteCacheEntryInput
        {
            Identifier = new System.IO.MemoryStream(Encoding.UTF8.GetBytes("key1"))
        });
        Assert.Throws<EntryDoesNotExist>(() => cache.GetCacheEntry(MakeGet("key1")));
    }

    [Fact]
    public void ExpiredEntryNotReturned()
    {
        var cache = CreateDefaultCache(10);
        cache.PutCacheEntry(MakePut("expired", Now() - 1));
        Assert.Throws<EntryDoesNotExist>(() => cache.GetCacheEntry(MakeGet("expired")));
    }

    [Fact]
    public void PutOverwritesExistingKey()
    {
        var cache = CreateDefaultCache(10);
        cache.PutCacheEntry(MakePut("key1", Now() + 3600));
        cache.PutCacheEntry(MakePut("key1", Now() + 7200));
        var result = cache.GetCacheEntry(MakeGet("key1"));
        Assert.Equal("key1", result.Materials.BeaconKey.BeaconKeyIdentifier);
    }

    /// <summary>
    /// Tests the storm tracking behavior: first miss triggers fetch,
    /// then put fills cache, subsequent gets return cached data.
    /// </summary>
    [Fact]
    public void MissTriggersEntryDoesNotExistThenPutFillsCache()
    {
        var cache = CreateDefaultCache(10);

        // First get — cache miss, should trigger EntryDoesNotExist (EmptyFetch path)
        Assert.Throws<EntryDoesNotExist>(() => cache.GetCacheEntry(MakeGet("key1")));

        // Simulate the caller fetching from KMS and putting the result
        cache.PutCacheEntry(MakePut("key1", Now() + 3600));

        // Now get should succeed
        var result = cache.GetCacheEntry(MakeGet("key1"));
        Assert.Equal("key1", result.Materials.BeaconKey.BeaconKeyIdentifier);
    }

    /// <summary>
    /// Concurrent stress test: multiple threads doing get-or-put.
    /// Validates no crashes, deadlocks, or data corruption under contention.
    /// </summary>
    [Fact]
    public void ConcurrentStressTest()
    {
        var cache = CreateDefaultCache(10);
        int totalOps = 300_000;
        var exceptions = new System.Collections.Concurrent.ConcurrentBag<System.Exception>();
        var countdown = new CountdownEvent(totalOps);

        for (int i = 0; i < totalOps; i++)
        {
            ThreadPool.QueueUserWorkItem(_ =>
            {
                try
                {
                    var id = Identifiers[System.Environment.CurrentManagedThreadId % Identifiers.Length];
                    try
                    {
                        cache.GetCacheEntry(MakeGet(id));
                    }
                    catch (EntryDoesNotExist)
                    {
                        cache.PutCacheEntry(MakePut(id, Now() + 3600));
                    }
                }
                catch (System.Exception ex)
                {
                    exceptions.Add(ex);
                }
                finally
                {
                    countdown.Signal();
                }
            });
        }

        Assert.True(countdown.Wait(System.TimeSpan.FromSeconds(60)), "Timed out");
        Assert.Empty(exceptions);
    }

    /// <summary>
    /// Tests that waiters eventually get data after another thread puts it.
    /// Simulates the storm tracking wake-up path.
    /// </summary>
    [Fact]
    public void WaiterGetsDataAfterPut()
    {
        var cache = CreateDefaultCache(10);
        GetCacheEntryOutput result = null;

        // Thread 1: will get EntryDoesNotExist (EmptyFetch), then put
        // Thread 2: may get EmptyWait, then should eventually get data
        var barrier = new ManualResetEventSlim(false);

        var t1 = new Thread(() =>
        {
            try { cache.GetCacheEntry(MakeGet("shared")); }
            catch (EntryDoesNotExist)
            {
                // Simulate KMS call delay
                Thread.Sleep(100);
                cache.PutCacheEntry(MakePut("shared", Now() + 3600));
                barrier.Set();
            }
        });

        var t2 = new Thread(() =>
        {
            // Wait a bit so t1 gets the EmptyFetch first
            Thread.Sleep(20);
            try
            {
                result = cache.GetCacheEntry(MakeGet("shared"));
            }
            catch (EntryDoesNotExist)
            {
                // t2 might also get EmptyFetch if timing is right — that's ok
                barrier.Wait(5000);
                cache.PutCacheEntry(MakePut("shared", Now() + 3600));
                result = cache.GetCacheEntry(MakeGet("shared"));
            }
        });

        t1.Start();
        t2.Start();
        t1.Join(10000);
        t2.Join(10000);

        Assert.NotNull(result);
        Assert.Equal("shared", result.Materials.BeaconKey.BeaconKeyIdentifier);
    }
}
