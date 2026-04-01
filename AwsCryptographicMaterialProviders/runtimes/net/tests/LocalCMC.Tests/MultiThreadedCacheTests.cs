using System.Collections.Generic;
using System.Text;
using System.Threading;
using AWS.Cryptography.KeyStore;
using AWS.Cryptography.MaterialProviders;
using Xunit;

public class MultiThreadedCacheTests
{
    private static MaterialProviders mpl = new MaterialProviders(new MaterialProvidersConfig());

    private static readonly string[] Identifiers =
    {
        "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen",
        "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"
    };

    private static ICryptographicMaterialsCache CreateCache(int capacity)
    {
        return mpl.CreateCryptographicMaterialsCache(
            new CreateCryptographicMaterialsCacheInput
            {
                Cache = new CacheType
                {
                    MultiThreaded = new MultiThreadedCache { EntryCapacity = capacity }
                }
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
        var cache = CreateCache(10);
        cache.PutCacheEntry(MakePut("key1", Now() + 3600));
        var result = cache.GetCacheEntry(MakeGet("key1"));
        Assert.Equal("key1", result.Materials.BeaconKey.BeaconKeyIdentifier);
    }

    [Fact]
    public void GetMissingKeyThrows()
    {
        var cache = CreateCache(10);
        Assert.Throws<EntryDoesNotExist>(() => cache.GetCacheEntry(MakeGet("missing")));
    }

    [Fact]
    public void DeleteRemovesEntry()
    {
        var cache = CreateCache(10);
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
        var cache = CreateCache(10);
        cache.PutCacheEntry(MakePut("expired", Now() - 1));
        Assert.Throws<EntryDoesNotExist>(() => cache.GetCacheEntry(MakeGet("expired")));
    }

    [Fact]
    public void CapacityEviction()
    {
        var cache = CreateCache(5);
        for (int i = 0; i < 6; i++)
            cache.PutCacheEntry(MakePut($"cap{i}", Now() + 3600));

        int found = 0;
        for (int i = 0; i < 6; i++)
        {
            try { cache.GetCacheEntry(MakeGet($"cap{i}")); found++; }
            catch (EntryDoesNotExist) { }
        }
        Assert.True(found <= 5, $"Expected at most 5 entries but found {found}");
    }

    [Fact]
    public void PutOverwritesExistingKey()
    {
        var cache = CreateCache(10);
        cache.PutCacheEntry(MakePut("key1", Now() + 3600));
        cache.PutCacheEntry(MakePut("key1", Now() + 7200));
        var result = cache.GetCacheEntry(MakeGet("key1"));
        Assert.Equal("key1", result.Materials.BeaconKey.BeaconKeyIdentifier);
    }

    [Fact]
    public void ConcurrentStressTest()
    {
        var cache = CreateCache(10);
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
}
