package software.amazon.cryptography.example;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;
import javax.annotation.Nullable;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
import software.amazon.awssdk.services.dynamodb.model.AttributeValue;
import software.amazon.awssdk.services.dynamodb.model.Delete;
import software.amazon.awssdk.services.dynamodb.model.DeleteItemRequest;
import software.amazon.awssdk.services.dynamodb.model.DeleteItemResponse;
import software.amazon.awssdk.services.dynamodb.model.GetItemRequest;
import software.amazon.awssdk.services.dynamodb.model.GetItemResponse;
import software.amazon.awssdk.services.dynamodb.model.QueryRequest;
import software.amazon.awssdk.services.dynamodb.model.QueryResponse;
import software.amazon.awssdk.services.dynamodb.model.ReturnValue;
import software.amazon.awssdk.services.dynamodb.model.TransactWriteItem;
import software.amazon.awssdk.services.dynamodb.model.TransactWriteItemsRequest;
import software.amazon.cryptography.example.hierarchy.AdminProvider;

public class DdbHelper {

  public static boolean deleteKeyStoreDdbItem(
    final String branchKeyId,
    final String branchKeyType,
    final String physicalName,
    @Nullable DynamoDbClient dynamoDbClient,
    boolean verbose
  ) {
    dynamoDbClient = AdminProvider.dynamoDB(dynamoDbClient);
    return reallyDeleteKeyStoreDdbItem(
      branchKeyId,
      branchKeyType,
      physicalName,
      1,
      0,
      dynamoDbClient,
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
    final Map<String, AttributeValue> item,
    final String _tableName
  ) {
    final Map<String, AttributeValue> key = new HashMap<>(3, 1);
    key.put(Constants.BRANCH_KEY_ID, item.get(Constants.BRANCH_KEY_ID));
    key.put(Constants.TYPE, item.get(Constants.TYPE));
    return TransactWriteItem
      .builder()
      .delete(Delete.builder().tableName(_tableName).key(key).build())
      .build();
  }

  public static boolean DeleteBranchKey(
    final String branchKeyId,
    @Nullable String tableName,
    @Nullable String hierarchyVersion,
    @Nullable DynamoDbClient ddbClient
  ) {
    final String _tableName = tableName == null
      ? Fixtures.TEST_KEYSTORE_NAME
      : tableName;
    final String _hierarchyVersion = hierarchyVersion == null
      ? "1"
      : hierarchyVersion;
    final DynamoDbClient _ddbClient = ddbClient == null
      ? Fixtures.ddbClientWest2
      : ddbClient;
    final Map<String, String> ExpressionAttributeNames = new HashMap<>(3, 1);
    ExpressionAttributeNames.put("#pk", Constants.BRANCH_KEY_ID);
    ExpressionAttributeNames.put("#hv", "hierarchy-version");
    final Map<String, AttributeValue> ExpressionAttributeValues = new HashMap<>(
      3,
      1
    );
    ExpressionAttributeValues.put(":pk", AttributeValue.fromS(branchKeyId));
    ExpressionAttributeValues.put(
      ":hv",
      AttributeValue.fromN(_hierarchyVersion)
    );
    final QueryRequest queryReq = QueryRequest
      .builder()
      .tableName(_tableName)
      .keyConditionExpression("#pk = :pk")
      .filterExpression("#hv = :hv")
      .expressionAttributeNames(ExpressionAttributeNames)
      .expressionAttributeValues(ExpressionAttributeValues)
      .build();
    final QueryResponse queryRes = _ddbClient.query(queryReq);
    final List<TransactWriteItem> deleteItems = queryRes
      .items()
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
}
