package software.amazon.cryptography.example.cmc;

import Time.__default;
import java.nio.ByteBuffer;
import java.nio.charset.StandardCharsets;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.ConcurrentLinkedDeque;

import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

import software.amazon.cryptography.keystore.model.BranchKeyMaterials;
import software.amazon.cryptography.materialproviders.ICryptographicMaterialsCache;
import software.amazon.cryptography.materialproviders.model.CacheType;
import software.amazon.cryptography.materialproviders.model.EntryDoesNotExist;
import software.amazon.cryptography.materialproviders.model.GetCacheEntryInput;
import software.amazon.cryptography.materialproviders.model.GetCacheEntryOutput;
import software.amazon.cryptography.materialproviders.model.Materials;
import software.amazon.cryptography.materialproviders.model.PutCacheEntryInput;

public class ConcurrentGuavaTest {

  public static final long FIVE_MINUTES_IN_SECONDS = 5 * 60;
  private static final List<String> identifies = Collections.unmodifiableList(
    Arrays.asList("1", "2", "3", "4", "5")
  );
  private Map<String, String> indexToThreadId;
  private ConcurrentLinkedDeque<String> unpickedIndexes;
  private ICryptographicMaterialsCache underTest;

  @BeforeClass
  public void setup() {
    // Keep threads, threadPoolSize, & |identifies| equal
    final int threads = 5;
    indexToThreadId = new ConcurrentHashMap<>(threads + 1, 1, threads);
    unpickedIndexes = new ConcurrentLinkedDeque<>(identifies);
    CacheType cmc = GuavaCMC.create(threads, 10, 10, false);
    underTest = cmc.Shared();
    // GuavaCMC.ConcurrentCMC;
    System.out.println(
      "Thread ID: " +
      Thread.currentThread().getId() +
      " Cache: " +
      underTest.getClass().getSimpleName()
    );
    // assert underTest instanceof GuavaCMC.ConcurrentCMC;
    identifies.forEach(id -> createEntry(id, 0, underTest));
  }

  private void createEntry(
    String index,
    @SuppressWarnings("SameParameterValue") int value,
    ICryptographicMaterialsCache underTest
  ) {
    PutCacheEntryInput input = PutCacheEntryInput
      .builder()
      .identifier(identifier(index))
      .creationTime(__default.CurrentRelativeTime())
      .expiryTime(__default.CurrentRelativeTime() + FIVE_MINUTES_IN_SECONDS)
      .messagesUsed(0)
      .bytesUsed(0)
      .materials(
        Materials
          .builder()
          .BranchKey(
            BranchKeyMaterials
              .builder()
              .branchKeyIdentifier(index)
              .branchKeyVersion("0")
              .encryptionContext(
                Collections.singletonMap("Robbie", Integer.toString(value))
              )
              .branchKey(identifier("4"))
              .build()
          )
          .build()
      )
      .build();
    underTest.PutCacheEntry(input);
  }

  public ByteBuffer identifier(String index) {
    return ByteBuffer.wrap(index.getBytes(StandardCharsets.UTF_8));
  }

  @AfterClass
  public void teardown() {}

  private String indexForThread(final String threadId) {
    return indexToThreadId.computeIfAbsent(
      threadId,
      str -> unpickedIndexes.pop()
    );
  }

  @Test(threadPoolSize = 5, invocationCount = 300, timeOut = 1000)
  public void TestConcurrentCMC() {
    String index = indexForThread(
      String.valueOf(Thread.currentThread().getId())
    );
    ByteBuffer identifier = identifier(index);
    GetCacheEntryInput input = GetCacheEntryInput
      .builder()
      .identifier(identifier)
      .bytesUsed(0L)
      .build();
    try {
      GetCacheEntryOutput output = underTest.GetCacheEntry(input);
      String oldValue = output
        .materials()
        .BranchKey()
        .encryptionContext()
        .get("Robbie");
      String newValue = Integer.toString(Integer.parseInt(oldValue) + 1);
      System.out.println(
        "Thread ID: " +
        Thread.currentThread().getId() +
        " Index: " +
        index +
        " newValue: " +
        newValue +
        " oldValue: " +
        oldValue
      );
      output
        .materials()
        .BranchKey()
        .encryptionContext()
        .put("Robbie", newValue);
      PutCacheEntryInput putInput = fromCacheOutput(output, identifier);
      underTest.PutCacheEntry(putInput);
    } catch (EntryDoesNotExist exception) {
      System.out.println(
        "Thread ID: " +
        Thread.currentThread().getId() +
        " Index: " +
        index +
        " Got EntryDoesNotExist exception"
      );
    }
  }

  public PutCacheEntryInput fromCacheOutput(
    GetCacheEntryOutput output,
    ByteBuffer identifier
  ) {
    return PutCacheEntryInput
      .builder()
      .identifier(identifier)
      .materials(output.materials())
      .creationTime(output.creationTime())
      .expiryTime(output.expiryTime())
      .bytesUsed(output.bytesUsed())
      .messagesUsed(output.messagesUsed())
      .build();
  }
}
