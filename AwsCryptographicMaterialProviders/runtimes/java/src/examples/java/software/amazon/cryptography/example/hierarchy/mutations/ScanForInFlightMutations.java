package software.amazon.cryptography.example.hierarchy.mutations;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import javax.annotation.Nonnull;
import javax.annotation.Nullable;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
import software.amazon.awssdk.services.dynamodb.model.AttributeValue;
import software.amazon.awssdk.services.dynamodb.model.ScanRequest;
import software.amazon.awssdk.services.dynamodb.model.ScanResponse;

public class ScanForInFlightMutations {

  @Nonnull
  private final DynamoDbClient dynamoDbClient;

  @Nonnull
  private final String tableName;

  @Nullable
  private final Integer limit;

  private static final Map<String, String> EAN;
  private static final Map<String, AttributeValue> EAV;
  private static final String PE = "#pk, #sk, #ct";

  static {
    EAN = new HashMap<>(3, 1);
    EAN.put("#sk", "type");
    EAN.put("#pk", "branch-key-id");
    EAN.put("#ct", "create-time");
    EAV = new HashMap<>(2, 1);
    EAV.put(
      ":type",
      AttributeValue.builder().s("branch:MUTATION_COMMITMENT").build()
    );
  }

  public ScanForInFlightMutations(
    @Nonnull DynamoDbClient dynamoDbClient,
    @Nonnull String tableName,
    @Nullable Integer limit
  ) {
    this.dynamoDbClient = dynamoDbClient;
    this.tableName = tableName;
    this.limit = limit;
  }

  public static class InFlightMutation {

    private final String branchKeyID;
    private final String createTime;

    public InFlightMutation(String branchKeyID, String createTime) {
      this.branchKeyID = branchKeyID;
      this.createTime = createTime;
    }

    public String branchKeyID() {
      return branchKeyID;
    }

    public String createTime() {
      return createTime;
    }

    @Override
    public String toString() {
      return branchKeyID + ": " + createTime;
    }
  }

  public static class PageResult {

    private final @Nonnull List<InFlightMutation> inFlightMutations;
    private final @Nullable Map<String, AttributeValue> lastEvaluatedKey;

    public PageResult(
      @Nonnull List<InFlightMutation> inFlightMutations,
      @Nullable Map<String, AttributeValue> lastEvaluatedKey
    ) {
      this.inFlightMutations = inFlightMutations;
      this.lastEvaluatedKey = lastEvaluatedKey;
    }

    public @Nonnull List<InFlightMutation> inFlightMutations() {
      return inFlightMutations;
    }

    public @Nullable Map<String, AttributeValue> lastEvaluatedKey() {
      return lastEvaluatedKey;
    }
  }

  public PageResult scanForMutationLock(
    @Nullable Map<String, AttributeValue> exclusiveStartKey
  ) {
    ScanRequest.Builder request = ScanRequest
      .builder()
      .tableName(tableName)
      .filterExpression("#sk = :type")
      .expressionAttributeNames(EAN)
      .expressionAttributeValues(EAV)
      .projectionExpression(PE);
    if (exclusiveStartKey != null) {
      request.exclusiveStartKey(exclusiveStartKey);
    }
    if (limit != null) {
      request.limit(limit);
    }
    ScanResponse response = this.dynamoDbClient.scan(request.build());
    Map<String, AttributeValue> lastEvaluatedKey = response.lastEvaluatedKey();
    List<InFlightMutation> list = new ArrayList<>();
    for (Map<
      String,
      AttributeValue
    > stringAttributeValueMap : response.items()) {
      String bkid = stringAttributeValueMap.get("branch-key-id").s();
      String createTime = stringAttributeValueMap.get("create-time").s();
      InFlightMutation apply = new InFlightMutation(bkid, createTime);
      list.add(apply);
    }
    if (lastEvaluatedKey != null && !lastEvaluatedKey.isEmpty()) {
      return new PageResult(list, lastEvaluatedKey);
    }
    return new PageResult(list, null);
  }
}
