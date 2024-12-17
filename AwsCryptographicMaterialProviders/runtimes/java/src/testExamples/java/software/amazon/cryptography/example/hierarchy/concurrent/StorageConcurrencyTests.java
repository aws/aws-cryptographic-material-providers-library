package software.amazon.cryptography.example.hierarchy.concurrent;

// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.*;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.ConcurrentLinkedDeque;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.stream.IntStream;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
import software.amazon.awssdk.services.dynamodb.model.DynamoDbException;
import software.amazon.awssdk.services.dynamodb.model.GetItemResponse;
import software.amazon.awssdk.services.kms.KmsClient;
import software.amazon.cryptography.example.DdbHelper;
import software.amazon.cryptography.example.Fixtures;
import software.amazon.cryptography.keystore.KeyStore;
import software.amazon.cryptography.keystore.model.DynamoDBTable;
import software.amazon.cryptography.keystore.model.GetActiveBranchKeyInput;
import software.amazon.cryptography.keystore.model.GetActiveBranchKeyOutput;
import software.amazon.cryptography.keystore.model.KMSConfiguration;
import software.amazon.cryptography.keystore.model.KeyStorageException;
import software.amazon.cryptography.keystore.model.KeyStoreConfig;
import software.amazon.cryptography.keystore.model.KeyStoreException;
import software.amazon.cryptography.keystore.model.Storage;
import software.amazon.cryptography.keystoreadmin.KeyStoreAdmin;
import software.amazon.cryptography.keystoreadmin.model.CreateKeyInput;
import software.amazon.cryptography.keystoreadmin.model.CreateKeyOutput;
import software.amazon.cryptography.keystoreadmin.model.KeyStoreAdminConfig;
import software.amazon.cryptography.keystoreadmin.model.KmsSymmetricKeyArn;

// This class contains a suite of tests to check behavior in the storage layer
// of the library's APIs. These APIs write to the storage layer. We are not testing
// with the KeyStore layer since this layer induces additional latency due to the calls
// to AWS KMS. To test the concurrent behavior we don't need to test additional network calls.
public class StorageConcurrencyTests {

  private static final String branchKeyId =
    "concurrency-test-write-key-" + UUID.randomUUID();
  private static final Integer threadCount = 15;
  private static final List<String> identifiers = Collections.unmodifiableList(
    Arrays.asList(
      IntStream
        .rangeClosed(1, 15)
        .mapToObj(String::valueOf)
        .toArray(String[]::new)
    )
  );

  private Map<String, Storage> threadIndexToStorage;
  private Map<String, KeyStore> threadIndexToKeyStore;
  private static Map<String, String> indexToThreadId, threadIndexToTimestamp;
  private static Map<
    String,
    GetActiveBranchKeyOutput
  > getActiveBranchKeyOutputs;
  private ConcurrentLinkedDeque<
    String
  > unpickedIndicesForStorage, unpickedIndicesForKeyStore;
  private static Map<String, String> encryptionContext;
  private static final AtomicInteger counter = new AtomicInteger(0);

  @BeforeClass
  public void setup() {
    threadIndexToStorage = new ConcurrentHashMap<>(16, 1, threadCount);
    threadIndexToKeyStore = new ConcurrentHashMap<>(16, 1, threadCount);
    indexToThreadId = new ConcurrentHashMap<>(16, 1, threadCount);
    threadIndexToTimestamp = new ConcurrentHashMap<>(16, 1, threadCount);
    getActiveBranchKeyOutputs = new ConcurrentHashMap<>(16, 1, threadCount);

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
  }

  private KeyStore createKeyStore() {
    final DynamoDbClient _ddbClient = DynamoDbClient.create();
    final KmsClient _kmsClient = KmsClient.create();
    final KeyStoreConfig config = KeyStoreConfig
      .builder()
      .ddbClient(_ddbClient)
      .ddbTableName(Fixtures.TEST_KEYSTORE_NAME)
      .logicalKeyStoreName(Fixtures.TEST_KEYSTORE_NAME)
      .kmsClient(_kmsClient)
      .kmsConfiguration(
        KMSConfiguration.builder().kmsKeyArn(Fixtures.KEYSTORE_KMS_ARN).build()
      )
      .build();
    return KeyStore.builder().KeyStoreConfig(config).build();
  }

  private Storage createStorageLayer() {
    final DynamoDbClient _ddbClient = DynamoDbClient.create();
    DynamoDBTable table = DynamoDBTable
      .builder()
      .ddbClient(_ddbClient)
      .ddbTableName(Fixtures.TEST_KEYSTORE_NAME)
      .build();
    return Storage.builder().ddb(table).build();
  }

  @AfterClass
  public void teardown() {
    GetItemResponse res = DdbHelper.getKeyStoreDdbItem(
      branchKeyId,
      "branch:ACTIVE",
      Fixtures.TEST_KEYSTORE_NAME,
      DynamoDbClient.create()
    );
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
    DdbHelper.deleteKeyStoreDdbItem(
      branchKeyId,
      res.item().get("version").s(),
      Fixtures.TEST_KEYSTORE_NAME,
      DynamoDbClient.create(),
      true
    );
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

  private CreateKeyOutput raceToWriteWithStorage(KeyStoreAdmin admin) {
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
    return admin.CreateKey(createKeyInput);
  }

  private GetActiveBranchKeyOutput raceToReadWithKeyStore(KeyStore keyStore) {
    GetActiveBranchKeyInput input = GetActiveBranchKeyInput
      .builder()
      .branchKeyIdentifier(branchKeyId)
      .build();
    return keyStore.GetActiveBranchKey(input);
  }

  @Test(threadPoolSize = 15, invocationCount = 150, timeOut = 10000)
  public void testConcurrentStorage() {
    String threadId = String.valueOf(Thread.currentThread().getId());
    String threadIdToIndex = indexToThreadId.computeIfAbsent(
      threadId,
      str -> unpickedIndicesForStorage.pop()
    );

    TimeZone tz = TimeZone.getTimeZone("UTC");
    DateFormat df = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss.SSSSS'Z'"); // Quoted "Z" to indicate UTC, no timezone offset
    df.setTimeZone(tz);
    String timestamp = df.format(new Date());

    System.out.println(
      "Thread ID: " +
      Thread.currentThread().getId() +
      " ThreadIndex: " +
      threadIdToIndex +
      " Timestamp: " +
      timestamp +
      " BranchKeyId: " +
      branchKeyId
    );
    threadIndexToTimestamp.putIfAbsent(threadIdToIndex, timestamp);

    try {
      if (Integer.parseInt(threadIdToIndex) % 2 == 0) {
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
        raceToWriteWithStorage(admin);
      } else {
        String iteration = String.valueOf(counter.incrementAndGet());
        KeyStore keyStore = keyStoreForThread(threadIdToIndex);
        GetActiveBranchKeyOutput output = raceToReadWithKeyStore(keyStore);
        getActiveBranchKeyOutputs.put(iteration, output);
      }
    } catch (DynamoDbException | KeyStorageException | KeyStoreException e) {
      System.out.println(e);
    }
  }

  @Test(dependsOnMethods = { "testConcurrentStorage" })
  public void testReadAfterWriteCheck() {
    System.out.println(getActiveBranchKeyOutputs.size());
    Set<String> keys = getActiveBranchKeyOutputs.keySet();
    for (String key : keys) {
      GetActiveBranchKeyOutput storedOutput = getActiveBranchKeyOutputs.get(
        key
      );
      System.out.println(
        Arrays.toString(storedOutput.branchKeyMaterials().branchKey().array())
      );
    }
  }
}
