package software.amazon.cryptography.example;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;
import javax.annotation.Nonnull;
import javax.annotation.Nullable;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
import software.amazon.awssdk.services.dynamodb.model.AttributeValue;
import software.amazon.awssdk.services.dynamodb.model.Delete;
import software.amazon.awssdk.services.dynamodb.model.DeleteItemRequest;
import software.amazon.awssdk.services.dynamodb.model.DeleteItemResponse;
import software.amazon.awssdk.services.dynamodb.model.GetItemRequest;
import software.amazon.awssdk.services.dynamodb.model.GetItemResponse;
import software.amazon.awssdk.services.dynamodb.model.Put;
import software.amazon.awssdk.services.dynamodb.model.QueryRequest;
import software.amazon.awssdk.services.dynamodb.model.QueryResponse;
import software.amazon.awssdk.services.dynamodb.model.ReturnValue;
import software.amazon.awssdk.services.dynamodb.model.TransactWriteItem;
import software.amazon.awssdk.services.dynamodb.model.TransactWriteItemsRequest;
import software.amazon.cryptography.example.hierarchy.AdminProvider;
import software.amazon.cryptography.example.hierarchy.CreateKeyExample;
import software.amazon.cryptography.example.hierarchy.VersionKeyExample;
import software.amazon.cryptography.keystore.model.HierarchyVersion;
import software.amazon.cryptography.keystoreadmin.KeyStoreAdmin;

public class DdbHelper {

  // Creates a Branch Key and also create a new version.
  public static void createHappyCaseId(
    @Nonnull String kmsKeyArn,
    @Nonnull String branchKeyId,
    @Nonnull KeyStoreAdmin admin,
    @Nonnull HierarchyVersion hierarchyVersion
  ) {
    CreateKeyExample.CreateKey(kmsKeyArn, branchKeyId, admin, hierarchyVersion);
    VersionKeyExample.VersionKey(kmsKeyArn, branchKeyId, admin);
  }

  public static boolean deleteKeyStoreDdbItem(
    final String branchKeyId,
    final String branchKeyType,
    final String physicalName,
    @Nullable DynamoDbClient dynamoDbClient,
    boolean verbose
  ) {
    return reallyDeleteKeyStoreDdbItem(
      branchKeyId,
      branchKeyType,
      physicalName,
      1,
      0,
      AdminProvider.dynamoDB(dynamoDbClient),
      verbose
    );
  }

  public static boolean reallyDeleteKeyStoreDdbItem(
    final String branchKeyId,
    final String branchKeyType,
    final String physicalName,
    int retryCount,
    final int sleep,
    final DynamoDbClient dynamoDbClient,
    boolean verbose
  ) {
    Map<String, AttributeValue> ddbKey = new HashMap<>(3, 1);
    ddbKey.put(
      Constants.BRANCH_KEY_ID,
      AttributeValue.builder().s(branchKeyId).build()
    );
    ddbKey.put(
      Constants.TYPE,
      AttributeValue.builder().s(branchKeyType).build()
    );
    DeleteItemRequest deleteReq = DeleteItemRequest
      .builder()
      .tableName(physicalName)
      .key(ddbKey)
      .returnValues(ReturnValue.ALL_OLD)
      .build();
    DeleteItemResponse deleteRes;
    GetItemRequest getReq = GetItemRequest
      .builder()
      .key(ddbKey)
      .tableName(physicalName)
      .build();
    GetItemResponse getRes;
    boolean done = false;
    while (retryCount > 0 && !done) {
      deleteRes = dynamoDbClient.deleteItem(deleteReq);
      getRes = dynamoDbClient.getItem(getReq);
      if (deleteRes.hasAttributes()) {
        if (verbose) {
          System.out.println(
            "Deleted with result: " + deleteRes.attributes().get(Constants.TYPE)
          );
        }
      }
      if (getRes.hasItem()) {
        if (verbose) {
          System.out.println(
            "Got with result: " + getRes.item().get(Constants.TYPE)
          );
        }
        retryCount--;
        try {
          Thread.sleep(sleep);
        } catch (InterruptedException e) {
          throw new RuntimeException(e);
        }
      } else {
        if (verbose) {
          System.out.println("Got no result.");
        }
        done = true;
      }
    }
    return done;
  }

  public static GetItemResponse getKeyStoreDdbItem(
    final String branchKeyId,
    final String branchKeyType,
    final String physicalName,
    @Nullable DynamoDbClient dynamoDbClient
  ) {
    Map<String, AttributeValue> ddbKey = new HashMap<>(3);
    ddbKey.put(
      Constants.BRANCH_KEY_ID,
      AttributeValue.builder().s(branchKeyId).build()
    );
    ddbKey.put(
      Constants.TYPE,
      AttributeValue.builder().s(branchKeyType).build()
    );
    return AdminProvider
      .dynamoDB(dynamoDbClient)
      .getItem(builder -> builder.tableName(physicalName).key(ddbKey));
  }

  private static TransactWriteItem bkItemToDeleteReq(
    final Map<String, AttributeValue> key,
    final String _tableName
  ) {
    assert key.size() == 2 : "key parameter should only have 2 items";
    return TransactWriteItem
      .builder()
      .delete(Delete.builder().tableName(_tableName).key(key).build())
      .build();
  }

  private static Map<String, AttributeValue> itemToDDBKey(
    Map<String, AttributeValue> item
  ) {
    final Map<String, AttributeValue> key = new HashMap<>(3, 1);
    assert item.get(Constants.BRANCH_KEY_ID) != null : Constants.BRANCH_KEY_ID +
    " should not be null";
    assert item.get(Constants.TYPE) != null : Constants.TYPE +
    " should not be null";
    key.put(Constants.BRANCH_KEY_ID, item.get(Constants.BRANCH_KEY_ID));
    key.put(Constants.TYPE, item.get(Constants.TYPE));
    return key;
  }

  public static boolean DeleteBranchKey(
    final String branchKeyId,
    @Nullable String tableName,
    @Nullable DynamoDbClient ddbClient
  ) {
    final String _tableName = tableName == null
      ? Fixtures.TEST_KEYSTORE_NAME
      : tableName;
    final DynamoDbClient _ddbClient = ddbClient == null
      ? Fixtures.ddbClientWest2
      : ddbClient;
    final List<Map<String, AttributeValue>> ddbKeys = QueryForAllBkItemsDDBKeys(
      branchKeyId,
      _tableName,
      _ddbClient
    );
    return DeleteAllBkKeys(ddbKeys, _tableName, _ddbClient);
  }

  public static boolean DeleteAllBkKeys(
    @Nonnull List<Map<String, AttributeValue>> ddbKeys,
    @Nullable String tableName,
    @Nullable DynamoDbClient ddbClient
  ) {
    final String _tableName = tableName == null
      ? Fixtures.TEST_KEYSTORE_NAME
      : tableName;
    final DynamoDbClient _ddbClient = ddbClient == null
      ? Fixtures.ddbClientWest2
      : ddbClient;
    final List<TransactWriteItem> deleteItems = ddbKeys
      .stream()
      .map(item -> bkItemToDeleteReq(item, _tableName))
      .collect(Collectors.toList());
    if (deleteItems.isEmpty()) {
      return true;
    }
    final TransactWriteItemsRequest deleteReq = TransactWriteItemsRequest
      .builder()
      .transactItems(
        deleteItems.size() > 100 ? deleteItems.subList(0, 100) : deleteItems
      )
      .build();
    _ddbClient.transactWriteItems(deleteReq);
    return deleteItems.size() < 100;
  }

  public static void CopyBranchKey(
    final String branchKeyId,
    @Nonnull String sourceTableName,
    @Nonnull String targetTableName,
    @Nullable DynamoDbClient ddbClient
  ) {
    final DynamoDbClient _ddbClient = ddbClient == null
      ? Fixtures.ddbClientWest2
      : ddbClient;
    final List<Map<String, AttributeValue>> ddbKeys = QueryForAllBkItemsDDBKeys(
      branchKeyId,
      sourceTableName,
      _ddbClient
    );
    CopyAllBkKeys(ddbKeys, targetTableName, _ddbClient);
  }

  public static void CopyAllBkKeys(
    @Nonnull List<Map<String, AttributeValue>> ddbItems,
    @Nonnull String tableName,
    @Nullable DynamoDbClient ddbClient
  ) {
    final DynamoDbClient _ddbClient = ddbClient == null
      ? Fixtures.ddbClientWest2
      : ddbClient;

    final List<TransactWriteItem> putItems = ddbItems
      .stream()
      .map(item ->
        TransactWriteItem
          .builder()
          .put(Put.builder().item(item).tableName(tableName).build())
          .build()
      )
      .collect(Collectors.toList());

    if (putItems.isEmpty()) {
      return;
    }

    // Process put items in batches of 100
    for (int i = 0; i < putItems.size(); i += 100) {
      int endIndex = Math.min(i + 100, putItems.size());
      List<TransactWriteItem> batchItems = putItems.subList(i, endIndex);

      final TransactWriteItemsRequest putReq = TransactWriteItemsRequest
        .builder()
        .transactItems(batchItems)
        .build();
      _ddbClient.transactWriteItems(putReq);
    }
  }

  public static List<Map<String, AttributeValue>> QueryForAllBkItemsDDBKeys(
    final String branchKeyId,
    @Nullable String tableName,
    @Nullable DynamoDbClient ddbClient
  ) {
    final String _tableName = tableName == null
      ? Fixtures.TEST_KEYSTORE_NAME
      : tableName;
    final DynamoDbClient _ddbClient = ddbClient == null
      ? Fixtures.ddbClientWest2
      : ddbClient;
    final QueryResponse queryRes = queryForAllBkItems(
      branchKeyId,
      _tableName,
      _ddbClient
    );
    return queryRes
      .items()
      .stream()
      .map(DdbHelper::itemToDDBKey)
      .collect(Collectors.toList());
  }

  private static QueryResponse queryForAllBkItems(
    String branchKeyId,
    String _tableName,
    DynamoDbClient _ddbClient
  ) {
    final Map<String, String> ExpressionAttributeNames = new HashMap<>(3, 1);
    ExpressionAttributeNames.put("#pk", Constants.BRANCH_KEY_ID);
    final Map<String, AttributeValue> ExpressionAttributeValues = new HashMap<>(
      3,
      1
    );
    ExpressionAttributeValues.put(":pk", AttributeValue.fromS(branchKeyId));
    final QueryRequest queryReq = QueryRequest
      .builder()
      .tableName(_tableName)
      .keyConditionExpression("#pk = :pk")
      .expressionAttributeNames(ExpressionAttributeNames)
      .expressionAttributeValues(ExpressionAttributeValues)
      .build();
    return _ddbClient.query(queryReq);
  }
}
