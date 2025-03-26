// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
import Random_Compile.ExternRandom;
import java.nio.ByteBuffer;
import java.nio.charset.StandardCharsets;
import java.time.Instant;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Random;
import java.util.concurrent.atomic.AtomicInteger;
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
import software.amazon.cryptography.materialproviders.model.StormTrackingCache;
import software.amazon.cryptography.materialproviders.model.TimeUnits;

public class MultiThreadedCMCTest {

  private static final ICryptographicMaterialsCache multiThreadedCache;
  private static final ICryptographicMaterialsCache defaultCache;
  private static final ICryptographicMaterialsCache stormCache1;
  private static final ICryptographicMaterialsCache stormCache2;
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
  private static final int INVOCATIONS = 30000;
  private static final int ALWAYS_PICK = 22;
  private static final GetCacheEntryInput ALWAYS_PICK_INPUT;
  private static final PutCacheEntryInput ALWAYS_PUT_INPUT;
  private static final PerTestData TheData1 = new PerTestData();
  private static final PerTestData TheData2 = new PerTestData();
  private static final PerTestData TheData3 = new PerTestData();
  private static final PerTestData TheData4 = new PerTestData();

  static class PerTestData {

    AtomicIntegerArray CacheHitCounter = new AtomicIntegerArray(IDS_SIZE);
    AtomicIntegerArray CacheMissCounter = new AtomicIntegerArray(IDS_SIZE);
    AtomicIntegerArray IdCounter = new AtomicIntegerArray(IDS_SIZE);
    AtomicInteger ALWAYS_PICK_HIT = new AtomicInteger(0);
    AtomicInteger ALWAYS_PICK_MISS = new AtomicInteger(0);
  }

  static {
    String beaconKeyIdentifier = "twenty two";
    ByteBuffer cacheIdentifier = ByteBuffer.wrap(
      beaconKeyIdentifier.getBytes(StandardCharsets.UTF_8)
    );
    ALWAYS_PICK_INPUT =
      GetCacheEntryInput.builder().identifier(cacheIdentifier).build();
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
    ALWAYS_PUT_INPUT =
      PutCacheEntryInput
        .builder()
        .identifier(cacheIdentifier)
        .creationTime(Instant.now().getEpochSecond())
        .expiryTime(Instant.now().getEpochSecond() + 1_000_000_000)
        .materials(materials)
        .build();
    multiThreadedCache =
      MaterialProviders
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
                  // Capacity MUST be thread count + 1 (for always pick)
                  MultiThreadedCache.builder().entryCapacity(11).build()
                )
                .build()
            )
            .build()
        );
    multiThreadedCache.PutCacheEntry(ALWAYS_PUT_INPUT);
    defaultCache =
      MaterialProviders
        .builder()
        .MaterialProvidersConfig(MaterialProvidersConfig.builder().build())
        .build()
        .CreateCryptographicMaterialsCache(
          CreateCryptographicMaterialsCacheInput
            .builder()
            .cache(
              CacheType
                .builder()
                .Default(DefaultCache.builder().entryCapacity(11).build())
                .build()
            )
            .build()
        );
    defaultCache.PutCacheEntry(ALWAYS_PUT_INPUT);
    stormCache1 =
      MaterialProviders
        .builder()
        .MaterialProvidersConfig(MaterialProvidersConfig.builder().build())
        .build()
        .CreateCryptographicMaterialsCache(
          CreateCryptographicMaterialsCacheInput
            .builder()
            .cache(
              CacheType
                .builder()
                .StormTracking(
                  // Capacity MUST be thread count + 1 (for always pick)
                  StormTrackingCache
                    .builder()
                    .entryCapacity(11)
                    .gracePeriod(1)
                    .graceInterval(1)
                    .fanOut(10)
                    .inFlightTTL(1)
                    .sleepMilli(10)
                    .build()
                )
                .build()
            )
            .build()
        );
    stormCache1.PutCacheEntry(ALWAYS_PUT_INPUT);
    stormCache2 =
      MaterialProviders
        .builder()
        .MaterialProvidersConfig(MaterialProvidersConfig.builder().build())
        .build()
        .CreateCryptographicMaterialsCache(
          CreateCryptographicMaterialsCacheInput
            .builder()
            .cache(
              CacheType
                .builder()
                .StormTracking(
                  // Capacity MUST be thread count + 1 (for always pick)
                  StormTrackingCache
                    .builder()
                    .entryCapacity(11)
                    .gracePeriod(100)
                    .graceInterval(10)
                    .fanOut(10)
                    .inFlightTTL(100)
                    .sleepMilli(10)
                    .timeUnits(TimeUnits.Milliseconds)
                    .build()
                )
                .build()
            )
            .build()
        );
    stormCache2.PutCacheEntry(ALWAYS_PUT_INPUT);
  }

  @Test(threadPoolSize = 10, invocationCount = INVOCATIONS, timeOut = 10_000)
  public void testMultiThreadedCache() {
    doTestTryGetCatchPut(multiThreadedCache, TheData1, 2);
  }

  @Test(dependsOnMethods = { "testMultiThreadedCache" })
  public void validateMultiThreadedCache() {
    doValidateCacheHitsAndMisses(TheData1);
  }

  @Test(threadPoolSize = 10, invocationCount = INVOCATIONS, timeOut = 10_000)
  public void testDefaultCache() {
    doTestTryGetCatchPut(defaultCache, TheData2, 11);
  }

  @Test(dependsOnMethods = { "testDefaultCache" })
  public void validateDefaultCache() {
    doValidateCacheHitsAndMisses(TheData2);
  }

  @Test(threadPoolSize = 10, invocationCount = INVOCATIONS, timeOut = 10_000)
  public void testStormCache1() {
    doTestTryGetCatchPut(stormCache1, TheData3, 2);
  }

  @Test(dependsOnMethods = { "testStormCache1" })
  public void validateStormCache1() {
    doValidateCacheHitsAndMisses(TheData3);
  }

  @Test(threadPoolSize = 10, invocationCount = INVOCATIONS, timeOut = 10_000)
  public void testStormCache2() {
    doTestTryGetCatchPut(stormCache2, TheData4, 1);
  }

  @Test(dependsOnMethods = { "testStormCache2" })
  public void validateStormCache2() {
    doValidateCacheHitsAndMisses(TheData4);
  }

  public void doTestTryGetCatchPut(
    ICryptographicMaterialsCache cmcUnderTest,
    PerTestData data,
    int ttl
  ) {
    // Always Pick Provides assurance on the LRU nature of our CMCs.
    // Every thread tries to use it every time,
    // so it will be the MOST used element, and should never be evicted
    try {
      cmcUnderTest.GetCacheEntry(ALWAYS_PICK_INPUT);
      data.ALWAYS_PICK_HIT.incrementAndGet();
    } catch (EntryDoesNotExist ex) {
      data.ALWAYS_PICK_MISS.incrementAndGet();
      cmcUnderTest.PutCacheEntry(ALWAYS_PUT_INPUT);
    }

    Random rand = ExternRandom.getSecureRandom();
    int index = rand.nextInt(IDS_SIZE);
    data.IdCounter.getAndAdd(index, 1);
    String beaconKeyIdentifier = identifies.get(index);

    ByteBuffer cacheIdentifier = ByteBuffer.wrap(
      beaconKeyIdentifier.getBytes(StandardCharsets.UTF_8)
    );

    GetCacheEntryInput getCacheEntryInput = GetCacheEntryInput
      .builder()
      .identifier(cacheIdentifier)
      .build();
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
      .expiryTime(Instant.now().getEpochSecond() + ttl)
      .materials(materials)
      .build();

    tryGetCatchPut(
      cmcUnderTest,
      data,
      getCacheEntryInput,
      cacheIdentifier,
      index,
      putCacheEntryInput
    );
  }

  private static void tryGetCatchPut(
    ICryptographicMaterialsCache cmcUnderTest,
    PerTestData data,
    GetCacheEntryInput getCacheEntryInput,
    ByteBuffer cacheIdentifier,
    int index,
    PutCacheEntryInput putCacheEntryInput
  ) {
    try {
      GetCacheEntryOutput getCacheEntryOutput = cmcUnderTest.GetCacheEntry(
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
      data.CacheHitCounter.getAndAdd(index, 1);
    } catch (EntryDoesNotExist ex) {
      data.CacheMissCounter.getAndAdd(index, 1);
      cmcUnderTest.PutCacheEntry(putCacheEntryInput);
    }
  }

  // This test asserts that there were cache misses and cache hits.
  public void doValidateCacheHitsAndMisses(PerTestData data) {
    int sumOfHits = 0;
    int sumOfMisses = 0;
    int idSelectedCount = -1;
    for (int i = 0; i < IDS_SIZE; i++) {
      idSelectedCount = data.IdCounter.get(i);
      Assert.assertEquals(
        idSelectedCount,
        data.CacheHitCounter.get(i) + data.CacheMissCounter.get(i),
        "Cache hits for ID + Cache misses for ID != ID selection"
      );
      sumOfHits += data.CacheHitCounter.get(i);
      sumOfMisses += data.CacheMissCounter.get(i);
    }
    System.out.printf(
      "LocalCMC Test: TotalHits=%s TotalMisses=%s%n",
      sumOfHits,
      sumOfMisses
    );
    Assert.assertEquals(
      sumOfHits + sumOfMisses,
      INVOCATIONS,
      "Total hits and misses != total attempts!"
    );
    // Assert there were misses, as the cache started empty
    Assert.assertTrue(sumOfMisses > 0, "How were there no misses!");
    // Assert there was at least one hit
    Assert.assertTrue(sumOfHits > 0, "How were there no hits!");
    // Without better ID selection control,
    // along with finer timing control,
    // we cannot assert expected hits or misses
    // But we can assert that the ALWAYS_PICK was missed no more than thread count times
    Assert.assertEquals(
      data.ALWAYS_PICK_MISS.get(),
      0,
      "How was the always Pick missed!"
    );
  }
}
