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
import software.amazon.cryptography.materialproviders.model.EntryDoesNotExist;
import software.amazon.cryptography.materialproviders.model.GetCacheEntryInput;
import software.amazon.cryptography.materialproviders.model.GetCacheEntryOutput;
import software.amazon.cryptography.materialproviders.model.MaterialProvidersConfig;
import software.amazon.cryptography.materialproviders.model.Materials;
import software.amazon.cryptography.materialproviders.model.MultiThreadedCache;
import software.amazon.cryptography.materialproviders.model.PutCacheEntryInput;

public class MultiThreadedCMCTest {

  private static final ICryptographicMaterialsCache cmcUnderTest;
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
  private static final int ALWAYS_PICK = 22;
  private static final GetCacheEntryInput ALWAYS_PICK_INPUT;
  private static final PutCacheEntryInput ALWAYS_PUT_INPUT;
  private static final AtomicInteger ALWAYS_PICK_HIT = new AtomicInteger(0);
  private static final AtomicInteger ALWAYS_PICK_MISS = new AtomicInteger(0);

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
    cmcUnderTest =
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
    cmcUnderTest.PutCacheEntry(ALWAYS_PUT_INPUT);
  }

  @Test(threadPoolSize = 10, invocationCount = 300_000, timeOut = 10_000)
  public void testTryGetCatchPut() {
    // Always Pick Provides assurance on the LRU nature of our CMCs.
    // Every thread tries to use it every time,
    // so it will be the MOST used element, and should never be evicted
    try {
      cmcUnderTest.GetCacheEntry(ALWAYS_PICK_INPUT);
      ALWAYS_PICK_HIT.incrementAndGet();
    } catch (EntryDoesNotExist ex) {
      ALWAYS_PICK_MISS.incrementAndGet();
      cmcUnderTest.PutCacheEntry(ALWAYS_PUT_INPUT);
    }

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

    tryGetCatchPut(
      getCacheEntryInput,
      cacheIdentifier,
      index,
      putCacheEntryInput
    );
  }

  private static void tryGetCatchPut(
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
      CacheHitCounter.getAndAdd(index, 1);
    } catch (EntryDoesNotExist ex) {
      CacheMissCounter.getAndAdd(index, 1);
      cmcUnderTest.PutCacheEntry(putCacheEntryInput);
    }
  }

  // This test asserts that there were cache misses and cache hits.
  @Test(dependsOnMethods = { "testTryGetCatchPut" })
  public void validateTestALotOfAdding() {
    int sumOfHits = 0;
    int sumOfMisses = 0;
    int idSelectedCount = -1;
    for (int i = 0; i < IDS_SIZE; i++) {
      idSelectedCount = IdCounter.get(i);
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
      sumOfHits += CacheHitCounter.get(i);
      sumOfMisses += CacheMissCounter.get(i);
    }
    System.out.printf(
      "LocalCMC Test: ALWAYS_PICK: %s hit %s miss %s%n",
      ALWAYS_PICK,
      ALWAYS_PICK_HIT.get(),
      ALWAYS_PICK_MISS.get()
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
      ALWAYS_PICK_MISS.get(),
      0,
      "How was the always Pick missed!"
    );
  }
}
