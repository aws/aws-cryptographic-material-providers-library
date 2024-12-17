package software.amazon.cryptography.example.hierarchy.concurrent;

import static software.amazon.cryptography.example.hierarchy.concurrent.StorageWriteReadConcurrencyTests.createKeyStore;
import static software.amazon.cryptography.example.hierarchy.concurrent.StorageWriteReadConcurrencyTests.createStorageLayer;

import java.nio.ByteBuffer;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Arrays;
import java.util.Collections;
import java.util.Date;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.TimeZone;
import java.util.UUID;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.ConcurrentLinkedDeque;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.stream.IntStream;
import org.testng.Assert;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
import software.amazon.awssdk.services.dynamodb.model.AttributeValue;
import software.amazon.awssdk.services.dynamodb.model.QueryRequest;
import software.amazon.awssdk.services.dynamodb.model.QueryResponse;
import software.amazon.awssdk.services.dynamodb.model.TransactionCanceledException;
import software.amazon.cryptography.example.DdbHelper;
import software.amazon.cryptography.example.Fixtures;
import software.amazon.cryptography.keystore.KeyStore;
import software.amazon.cryptography.keystore.model.DynamoDBTable;
import software.amazon.cryptography.keystore.model.GetActiveBranchKeyInput;
import software.amazon.cryptography.keystore.model.GetActiveBranchKeyOutput;
import software.amazon.cryptography.keystore.model.Storage;
import software.amazon.cryptography.keystoreadmin.KeyStoreAdmin;
import software.amazon.cryptography.keystoreadmin.model.CreateKeyInput;
import software.amazon.cryptography.keystoreadmin.model.KeyStoreAdminConfig;
import software.amazon.cryptography.keystoreadmin.model.KmsSymmetricKeyArn;
import software.amazon.cryptography.keystoreadmin.model.VersionKeyInput;

// This class contains a suite of tests that check for behavior of reading
// a branch key while a version operation is in flight
public class StorageVersionReadConcurrencyTests {

  private static final String branchKeyId =
    "concurrency-test-version-key-" + UUID.randomUUID();
  private static final Integer threadCount = 10;
  private static final List<String> identifiers = Collections.unmodifiableList(
    Arrays.asList(
      IntStream
        .rangeClosed(1, 10)
        .mapToObj(String::valueOf)
        .toArray(String[]::new)
    )
  );

  private Map<String, Storage> threadIndexToStorage;
  private Map<String, KeyStore> threadIndexToKeyStore;
  private static Map<
    String,
    String
  > storageIndexToThreadId, keyStoreIndexToThreadId;
  private static Map<String, ByteBuffer> versionKeyOutputMap;
  private ConcurrentLinkedDeque<
    String
  > unpickedIndicesForStorage, unpickedIndicesForKeyStore;
  private static Map<String, String> encryptionContext;
  private static final AtomicInteger counter = new AtomicInteger(0);
  private static final TimeZone timeZone = TimeZone.getTimeZone("UTC");
  private static final DateFormat dateFormat = new SimpleDateFormat(
    "yyyy-MM-dd'T'HH:mm:ss.SSSSS'Z'"
  );
  private static final QueryRequest queryRequestForCleanUp = QueryRequest
    .builder()
    .tableName(Fixtures.TEST_KEYSTORE_NAME)
    .keyConditionExpression("#pk = :pkval")
    .expressionAttributeNames(
      new HashMap<String, String>() {
        {
          put("#pk", "branch-key-id");
        }
      }
    )
    .expressionAttributeValues(
      new HashMap<String, AttributeValue>() {
        {
          put(":pkval", AttributeValue.builder().s(branchKeyId).build());
        }
      }
    )
    .build();

  @BeforeClass
  public void setup() {
    dateFormat.setTimeZone(timeZone);
    threadIndexToStorage = new ConcurrentHashMap<>(16, 1, threadCount);
    threadIndexToKeyStore = new ConcurrentHashMap<>(16, 1, threadCount);
    storageIndexToThreadId = new ConcurrentHashMap<>(16, 1, threadCount);
    keyStoreIndexToThreadId = new ConcurrentHashMap<>(16, 1, threadCount);
    versionKeyOutputMap = new ConcurrentHashMap<>(16, 1, threadCount);

    unpickedIndicesForStorage = new ConcurrentLinkedDeque<>(identifiers);
    unpickedIndicesForKeyStore = new ConcurrentLinkedDeque<>(identifiers);
    // For every identifier which will ultimately map to one thread, we will create a unique
    // storage layer per thread with a unique ddb client. This will make it so that
    // we isolate resources even further and prevent resource reuse.
    identifiers.forEach(id -> {
      threadIndexToStorage.put(id, createStorageLayer());
      threadIndexToKeyStore.put(id, createKeyStore());
    });

    encryptionContext = new HashMap<>();
    encryptionContext.put("custom", "ec");

    final DynamoDbClient _ddbClient = DynamoDbClient.create();
    DynamoDBTable table = DynamoDBTable
      .builder()
      .ddbClient(_ddbClient)
      .ddbTableName(Fixtures.TEST_KEYSTORE_NAME)
      .build();
    Storage tmp = Storage.builder().ddb(table).build();
    KeyStoreAdmin admin = KeyStoreAdmin
      .builder()
      .KeyStoreAdminConfig(
        KeyStoreAdminConfig
          .builder()
          .storage(tmp)
          .logicalKeyStoreName(Fixtures.TEST_KEYSTORE_NAME)
          .build()
      )
      .build();
    CreateKeyInput createKeyInput = CreateKeyInput
      .builder()
      .Identifier(branchKeyId)
      .EncryptionContext(encryptionContext)
      .KmsArn(
        KmsSymmetricKeyArn
          .builder()
          .KmsKeyArn(Fixtures.KEYSTORE_KMS_ARN)
          .build()
      )
      .build();
    admin.CreateKey(createKeyInput);
    System.out.println(
      "Successfully set up test with branch key: " + branchKeyId
    );
  }

  @AfterClass
  public void teardown() {
    final DynamoDbClient _ddbClient = DynamoDbClient.create();
    DdbHelper.deleteKeyStoreDdbItem(
      branchKeyId,
      "branch:ACTIVE",
      Fixtures.TEST_KEYSTORE_NAME,
      DynamoDbClient.create(),
      true
    );
    DdbHelper.deleteKeyStoreDdbItem(
      branchKeyId,
      "beacon:ACTIVE",
      Fixtures.TEST_KEYSTORE_NAME,
      DynamoDbClient.create(),
      true
    );
    QueryResponse res = _ddbClient.query(queryRequestForCleanUp);
    res
      .items()
      .forEach(response -> {
        DdbHelper.deleteKeyStoreDdbItem(
          branchKeyId,
          response.get("type").s(),
          Fixtures.TEST_KEYSTORE_NAME,
          DynamoDbClient.create(),
          true
        );
      });
  }

  private Storage storageForThread(final String threadIdToIndex) {
    return threadIndexToStorage.computeIfAbsent(
      threadIdToIndex,
      k -> createStorageLayer()
    );
  }

  private KeyStore keyStoreForThread(String threadIdToIndex) {
    return threadIndexToKeyStore.computeIfAbsent(
      threadIdToIndex,
      k -> createKeyStore()
    );
  }

  private void raceToVersionWithStorage(KeyStoreAdmin admin) {
    VersionKeyInput input = VersionKeyInput
      .builder()
      .Identifier(branchKeyId)
      .KmsArn(
        KmsSymmetricKeyArn
          .builder()
          .KmsKeyArn(Fixtures.KEYSTORE_KMS_ARN)
          .build()
      )
      .build();
    admin.VersionKey(input);
  }

  private GetActiveBranchKeyOutput raceToReadActiveWithKeyStore(
    KeyStore keyStore
  ) {
    GetActiveBranchKeyInput input = GetActiveBranchKeyInput
      .builder()
      .branchKeyIdentifier(branchKeyId)
      .build();
    return keyStore.GetActiveBranchKey(input);
  }

  @Test(threadPoolSize = 10, invocationCount = 100, timeOut = 10000)
  public void testConcurrentVersionWithStorage() {
    String threadId = String.valueOf(Thread.currentThread().getId());
    String threadIdToIndex = storageIndexToThreadId.computeIfAbsent(
      threadId,
      str -> unpickedIndicesForStorage.pop()
    );

    String timestamp = dateFormat.format(new Date());
    try {
      Storage threadStorage = storageForThread(threadIdToIndex);
      KeyStoreAdminConfig keyStoreAdminConfig = KeyStoreAdminConfig
        .builder()
        .storage(threadStorage)
        .logicalKeyStoreName(Fixtures.TEST_KEYSTORE_NAME)
        .build();
      KeyStoreAdmin admin = KeyStoreAdmin
        .builder()
        .KeyStoreAdminConfig(keyStoreAdminConfig)
        .build();
      raceToVersionWithStorage(admin);
      System.out.println(
        "Successfully versioned branch key! Thread ID: " +
        Thread.currentThread().getId() +
        " ThreadIndex: " +
        threadIdToIndex +
        " Timestamp: " +
        timestamp +
        " BranchKeyId: " +
        branchKeyId
      );
    } catch (TransactionCanceledException exception) {
      System.out.println("Failed to write branch key: " + branchKeyId);
      // Exceptions that get thrown when you write keys using the Storage interface
      exception
        .cancellationReasons()
        .forEach(cancellationReason -> {
          Assert.assertTrue(
            (cancellationReason.code().equals("TransactionConflict") ||
              cancellationReason.code().equals("None") ||
              cancellationReason.code().equals("ConditionalCheckFailed"))
          );
        });
    }
  }

  @Test(threadPoolSize = 10, invocationCount = 100, timeOut = 10000)
  public void testConcurrentActiveReadWhileVersionInFlight() {
    // Since on set up we create a branch key, we should always be able to read.
    String threadId = String.valueOf(Thread.currentThread().getId());
    String threadIdToIndex = keyStoreIndexToThreadId.computeIfAbsent(
      threadId,
      str -> unpickedIndicesForKeyStore.pop()
    );
    KeyStore keyStore = keyStoreForThread(threadIdToIndex);
    GetActiveBranchKeyOutput output = raceToReadActiveWithKeyStore(keyStore);
    versionKeyOutputMap.put(
      output.branchKeyMaterials().branchKeyVersion(),
      output.branchKeyMaterials().branchKey()
    );
    System.out.println(
      "Successfully read branch key: " +
      branchKeyId +
      " with version: " +
      output.branchKeyMaterials().branchKeyVersion()
    );
  }

  @Test(
    dependsOnMethods = {
      "testConcurrentActiveReadWhileVersionInFlight",
      "testConcurrentVersionWithStorage",
    }
  )
  public void testVersionReads() {
    Assert.assertFalse(versionKeyOutputMap.isEmpty());
    for (String key : versionKeyOutputMap.keySet()) {
      System.out.println(
        "key: " + key + " value " + versionKeyOutputMap.get(key)
      );
    }
  }
}
