package software.amazon.cryptography.example;

import java.util.HashMap;
import java.util.Map;
import javax.annotation.Nullable;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
import software.amazon.awssdk.services.dynamodb.model.AttributeValue;
import software.amazon.cryptography.example.hierarchy.AdminProvider;

public class DdbHelper {

  public static void deleteKeyStoreDdbItem(
    final String branchKeyId,
    final String branchKeyType,
    final String physicalName,
    @Nullable DynamoDbClient dynamoDbClient
  ) {
    Map<String, AttributeValue> ddbKey = new HashMap<>(3);
    ddbKey.put(
      "branch-key-id",
      AttributeValue.builder().s(branchKeyId).build()
    );
    ddbKey.put("type", AttributeValue.builder().s(branchKeyType).build());
    dynamoDbClient = AdminProvider.dynamoDB(dynamoDbClient);
    dynamoDbClient.deleteItem(builder ->
      builder.tableName(physicalName).key(ddbKey)
    );
  }
}
