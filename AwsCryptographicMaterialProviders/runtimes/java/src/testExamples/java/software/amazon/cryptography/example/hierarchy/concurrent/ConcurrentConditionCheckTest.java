package software.amazon.cryptography.example.hierarchy.concurrent;

import org.testng.Assert;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.ConcurrentLinkedDeque;

import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
import software.amazon.awssdk.services.dynamodb.model.AttributeValue;
import software.amazon.awssdk.services.dynamodb.model.GetItemResponse;
import software.amazon.awssdk.services.dynamodb.model.TransactWriteItem;
import software.amazon.awssdk.services.dynamodb.model.TransactWriteItemsRequest;
import software.amazon.awssdk.services.dynamodb.model.TransactWriteItemsResponse;
import software.amazon.awssdk.services.dynamodb.model.TransactionCanceledException;
import software.amazon.awssdk.utils.ImmutableMap;
import software.amazon.cryptography.example.DdbHelper;
import software.amazon.cryptography.example.Fixtures;


// We check a thing and write a thing if the thing is good.
public class ConcurrentConditionCheckTest {
  private static final List<String> identifies = Collections.unmodifiableList(
    Arrays.asList(
      "1",
      "2",
      "3",
      "4",
      "5"
    )
  );
  private static DynamoDbClient ddbClient;
  private static final String mLockedId = "test-get-items-for-initialize-mutation";
  private static final String mLockType = "branch:MUTATION_LOCK";
  private static Map<String, AttributeValue> LOCK_EXPR_ATT_VALUES;
  private static final Map<String, String> INDEX_EXPR_ATT_NAMES = ImmutableMap.of(
    "#pk", "branch-key-id",
    "#v", "value");
  private static final Map<String, String> LOCK_EXPR_ATT_NAMES = ImmutableMap.of(
    "#pk", "branch-key-id");
  private static final Map<String, AttributeValue> M_LOCK_DDB_KEY = ImmutableMap.of(
    "branch-key-id", AttributeValue.builder().s(mLockedId).build(),
    "type", AttributeValue.builder().s(mLockType).build()
  );
  private Map<String, String> indexToThreadId;
  private ConcurrentLinkedDeque<String> unpickedIndexes;

  @BeforeClass
  public void setup() {
    ddbClient = Fixtures.ddbClientWest2;
    GetItemResponse response = DdbHelper.getKeyStoreDdbItem(
      mLockedId,
      mLockType,
      Fixtures.TEST_KEYSTORE_NAME,
      ddbClient);
    Map<String, AttributeValue> mLock = response.item();
    LOCK_EXPR_ATT_VALUES = ImmutableMap.of(
      ":original", mLock.get("original"),
      ":terminal", mLock.get("terminal")
    );
    identifies.forEach(id -> createIndexItem(id, 0, ddbClient));
    indexToThreadId = new ConcurrentHashMap<>(6, 1, 5);
    unpickedIndexes = new ConcurrentLinkedDeque<>(identifies);
  }

  @AfterClass
  public void teardown() {
    identifies.forEach(id ->
      DdbHelper.deleteKeyStoreDdbItem(
        mLockedId,
        "branch:MUTATION_INDEX:" + id,
        Fixtures.TEST_KEYSTORE_NAME,
        ddbClient,
        true));
  }

  public static void createIndexItem(
    final String index,
    final int value,
    final DynamoDbClient ddbClient
  ) {
    ddbClient.putItem(builder -> builder
      .item(indexItem(index, AttributeValue.fromN(Integer.toString(value))))
      .tableName(Fixtures.TEST_KEYSTORE_NAME));
  }

  public static Map<String, AttributeValue> indexItem(
    final String index,
    final AttributeValue value
  ) {
    Map<String, AttributeValue> item = new HashMap<>();
    item.put("branch-key-id", AttributeValue.builder().s(mLockedId).build());
    item.put("type", AttributeValue.builder().s(indexType(index)).build());
    item.put("value", value);
    return item;
  }

  private static String indexType(String index) {
    return "branch:MUTATION_INDEX:" + index;
  }

  public static TransactWriteItem conditionalWrite(
    final String index,
    final AttributeValue value,
    final AttributeValue oldValue
  )
  {
    Map<String, AttributeValue> attrValues = new HashMap<>();
    attrValues.put(":oldValue", oldValue);

    return TransactWriteItem.builder().put(putBuilder -> putBuilder
        .tableName(Fixtures.TEST_KEYSTORE_NAME)
        .item(indexItem(index, value))
        .conditionExpression("attribute_exists(#pk) and #v = :oldValue")
        .expressionAttributeNames(INDEX_EXPR_ATT_NAMES)
        .expressionAttributeValues(attrValues))
      .build();
  }

  public static TransactWriteItem conditionCheck() {
    return
      TransactWriteItem.builder().conditionCheck(checkBuilder -> checkBuilder
        .key(M_LOCK_DDB_KEY)
        .conditionExpression("attribute_exists(#pk) AND original = :original AND terminal = :terminal")
        .expressionAttributeNames(LOCK_EXPR_ATT_NAMES)
        .expressionAttributeValues(LOCK_EXPR_ATT_VALUES)
        .tableName(Fixtures.TEST_KEYSTORE_NAME).build()).build();
  }

  private String indexForThread(final String threadId) {
    return indexToThreadId.computeIfAbsent(threadId, str -> unpickedIndexes.pop());
  }

  @Test(threadPoolSize = 5, invocationCount = 30, timeOut = 1000)
  public void TestConcurrentConditionCheck() {
    String index = indexForThread(String.valueOf(Thread.currentThread().getId()));
    Map<String, AttributeValue> indexItem = DdbHelper.getKeyStoreDdbItem(
      mLockedId, indexType(index), Fixtures.TEST_KEYSTORE_NAME, ddbClient).item();
    AttributeValue oldValue = indexItem.get("value");
    int value = Integer.parseInt(oldValue.n()) + 1;
    AttributeValue newValue = AttributeValue.fromN(Integer.toString(value));
    System.out.println(
      "Thread ID: " + Thread.currentThread().getId()
        + " Index: " + index
        + " newValue: " + newValue.n()
        + " oldValue: " + oldValue.n());
    try {
      TransactWriteItemsResponse transactWriteItemsResponse = ddbClient.
        transactWriteItems(TransactWriteItemsRequest
          .builder()
          .transactItems(
            conditionCheck(),
            conditionalWrite(index, newValue, oldValue))
          .build());
      Assert.assertTrue(transactWriteItemsResponse.sdkHttpResponse().isSuccessful());
    } catch (TransactionCanceledException exception) {
      exception.cancellationReasons().forEach(System.out::println);
    }
  }

}
