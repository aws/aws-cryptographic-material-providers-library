import Random_Compile.ExternRandom;
import java.nio.ByteBuffer;
import java.nio.charset.StandardCharsets;
import java.time.Instant;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Random;
import java.util.concurrent.atomic.AtomicIntegerArray;
import org.testng.Assert;
import org.testng.annotations.Test;
import software.amazon.cryptography.keystore.model.BeaconKeyMaterials;
import software.amazon.cryptography.materialproviders.ICryptographicMaterialsCache;
import software.amazon.cryptography.materialproviders.MaterialProviders;
import software.amazon.cryptography.materialproviders.model.CacheType;
import software.amazon.cryptography.materialproviders.model.CreateCryptographicMaterialsCacheInput;
import software.amazon.cryptography.materialproviders.model.DefaultCache;
import software.amazon.cryptography.materialproviders.model.EntryDoesNotExist;
import software.amazon.cryptography.materialproviders.model.GetCacheEntryInput;
import software.amazon.cryptography.materialproviders.model.GetCacheEntryOutput;
import software.amazon.cryptography.materialproviders.model.MaterialProvidersConfig;
import software.amazon.cryptography.materialproviders.model.Materials;
import software.amazon.cryptography.materialproviders.model.MultiThreadedCache;
import software.amazon.cryptography.materialproviders.model.PutCacheEntryInput;

public class LocalCMCTests {

  private static final ICryptographicMaterialsCache test = MaterialProviders
    .builder()
    .MaterialProvidersConfig(MaterialProvidersConfig.builder().build())
    .build()
    .CreateCryptographicMaterialsCache(
      CreateCryptographicMaterialsCacheInput
        .builder()
        .cache(
          CacheType
            .builder()
            .MultiThreaded(
              MultiThreadedCache.builder().entryCapacity(10).build()
            )
            .build()
        )
        .build()
    );
  private static final List<String> identifies = Collections.unmodifiableList(
    Arrays.asList(
      "one",
      "two",
      "three",
      "four",
      "five",
      "six",
      "seven",
      "eight",
      "nine",
      "ten",
      "eleven",
      "twelve",
      "thirteen",
      "fourteen",
      "fifteen",
      "sixteen",
      "seventeen",
      "eighteen",
      "nineteen",
      "twenty",
      "twenty one"
    )
  );
  private static final int IDS_SIZE = identifies.size();
  private static final AtomicIntegerArray CacheHitCounter =
    new AtomicIntegerArray(IDS_SIZE);
  private static final AtomicIntegerArray CacheMissCounter =
    new AtomicIntegerArray(IDS_SIZE);
  private static final AtomicIntegerArray IdCounter = new AtomicIntegerArray(
    IDS_SIZE
  );

  @Test(threadPoolSize = 10, invocationCount = 300000, timeOut = 10000)
  public void TestALotOfAdding() {
    Random rand = ExternRandom.getSecureRandom();
    int index = rand.nextInt(IDS_SIZE);
    IdCounter.getAndAdd(index, 1);
    String beaconKeyIdentifier = identifies.get(index);

    ByteBuffer cacheIdentifier = ByteBuffer.wrap(
      beaconKeyIdentifier.getBytes(StandardCharsets.UTF_8)
    );

    GetCacheEntryInput getCacheEntryInput = GetCacheEntryInput
      .builder()
      .identifier(cacheIdentifier)
      .build();

    try {
      GetCacheEntryOutput getCacheEntryOutput = test.GetCacheEntry(
        getCacheEntryInput
      );
      Assert.assertNotNull(
        getCacheEntryOutput.materials().BeaconKey(),
        "Beacon Materials are null!"
      );
      Assert.assertEquals(
        getCacheEntryOutput.materials().BeaconKey().beaconKey(),
        cacheIdentifier
      );
      CacheHitCounter.getAndAdd(index, 1);
    } catch (EntryDoesNotExist ex) {
      CacheMissCounter.getAndAdd(index, 1);
      Materials materials = Materials
        .builder()
        .BeaconKey(
          BeaconKeyMaterials
            .builder()
            .beaconKeyIdentifier(beaconKeyIdentifier)
            // The cacheIdentifier is used as the material
            // because we are not testing the cryptography here.
            .beaconKey(cacheIdentifier)
            .encryptionContext(Collections.emptyMap())
            .build()
        )
        .build();

      PutCacheEntryInput putCacheEntryInput = PutCacheEntryInput
        .builder()
        .identifier(cacheIdentifier)
        .creationTime(Instant.now().getEpochSecond())
        .expiryTime(Instant.now().getEpochSecond() + 1)
        .materials(materials)
        .build();
      test.PutCacheEntry(putCacheEntryInput);
    }
  }

  // This test asserts that there were cache misses and cache hits.
  @Test(dependsOnMethods = { "TestALotOfAdding" })
  public void validateTestALotOfAdding() {
    int sumOfHits = 0;
    int sumOfMisses = 0;
    int idSelectedCount = -1;
    for (int i = 0; i < IDS_SIZE; i++) {
      // Was the ID ever randomly selected?
      idSelectedCount = IdCounter.get(i);
      if (idSelectedCount > 1) {
        // if the ID was hit, it MUST have been a HIT or MISS
        Assert.assertEquals(
          idSelectedCount,
          CacheHitCounter.get(i) + CacheMissCounter.get(i),
          "Cache hits for ID + Cache misses for ID != ID selection"
        );
        System.out.printf(
          "LocalCMC Test: ID: %s hit %s miss %s%n",
          i,
          CacheHitCounter.get(i),
          CacheMissCounter.get(i)
        );
      }
      sumOfHits += CacheHitCounter.get(i);
      sumOfMisses += CacheMissCounter.get(i);
      idSelectedCount = -1;
    }
    // Assert there were misses, as the cache started empty
    Assert.assertTrue(sumOfMisses > 0, "How were there no misses!");
    // Assert there was at least one hit
    Assert.assertTrue(sumOfHits > 0, "How were there no hits!");
    // Without better ID selection control,
    // along with finer timing control,
    // we cannot assert expected hits or misses
  }
}
