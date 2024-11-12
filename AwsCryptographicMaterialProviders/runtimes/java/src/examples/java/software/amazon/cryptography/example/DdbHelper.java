package software.amazon.cryptography.example;

import java.util.HashMap;
import java.util.Map;
import javax.annotation.Nullable;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
import software.amazon.awssdk.services.dynamodb.model.AttributeValue;
import software.amazon.awssdk.services.dynamodb.model.DeleteItemRequest;
import software.amazon.awssdk.services.dynamodb.model.DeleteItemResponse;
import software.amazon.awssdk.services.dynamodb.model.GetItemRequest;
import software.amazon.awssdk.services.dynamodb.model.GetItemResponse;
import software.amazon.awssdk.services.dynamodb.model.ReturnValue;
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
      "branch-key-id",
      AttributeValue.builder().s(branchKeyId).build()
    );
    ddbKey.put("type", AttributeValue.builder().s(branchKeyType).build());
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
            "Deleted with result: " + deleteRes.attributes().get("type")
          );
        }
      }
      if (getRes.hasItem()) {
        if (verbose) {
          System.out.println("Got with result: " + getRes.item().get("type"));
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
}
