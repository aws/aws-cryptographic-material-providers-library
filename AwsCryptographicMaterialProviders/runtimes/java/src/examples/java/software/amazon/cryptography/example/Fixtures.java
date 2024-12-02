// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
package software.amazon.cryptography.example;

import java.time.Duration;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;
import javax.annotation.Nullable;
import software.amazon.awssdk.auth.credentials.AwsCredentialsProvider;
import software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider;
import software.amazon.awssdk.http.SdkHttpClient;
import software.amazon.awssdk.http.apache.ApacheHttpClient;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
import software.amazon.awssdk.services.dynamodb.model.AttributeValue;
import software.amazon.awssdk.services.dynamodb.model.Delete;
import software.amazon.awssdk.services.dynamodb.model.GetItemResponse;
import software.amazon.awssdk.services.dynamodb.model.QueryRequest;
import software.amazon.awssdk.services.dynamodb.model.QueryResponse;
import software.amazon.awssdk.services.dynamodb.model.TransactWriteItem;
import software.amazon.awssdk.services.dynamodb.model.TransactWriteItemsRequest;
import software.amazon.awssdk.services.dynamodb.model.TransactWriteItemsResponse;
import software.amazon.awssdk.services.kms.KmsClient;
import software.amazon.cryptography.example.hierarchy.AdminProvider;
import software.amazon.cryptography.keystore.KeyStorageInterface;
import software.amazon.cryptography.keystore.model.GetKeyStorageInfoInput;
import software.amazon.cryptography.keystore.model.QueryForVersionsInput;
import software.amazon.cryptography.keystore.model.QueryForVersionsOutput;

public class Fixtures {

  public static final String TEST_KEYSTORE_NAME = "KeyStoreDdbTable";
  public static final String TEST_LOGICAL_KEYSTORE_NAME = "KeyStoreDdbTable";

  public static final String POSTAL_HORN_KEY_ARN =
    "arn:aws:kms:us-west-2:370957321024:key/bc127593-f7da-452c-a1f3-cd34c46f81f8";
  public static final String KEYSTORE_KMS_ARN =
    "arn:aws:kms:us-west-2:370957321024:key/9d989aa2-2f9c-438c-a745-cc57d3ad0126";
  public static final String MRK_ARN_EAST =
    "arn:aws:kms:us-east-1:658956600833:key/mrk-80bd8ecdcd4342aebd84b7dc9da498a7";
  public static final String MRK_ARN_WEST =
    "arn:aws:kms:us-west-2:658956600833:key/mrk-80bd8ecdcd4342aebd84b7dc9da498a7";
  // Key MUST NOT exist in ap-south-2
  public static final String MRK_ARN_AP =
    "arn:aws:kms:ap-south-2:658956600833:key/mrk-80bd8ecdcd4342aebd84b7dc9da498a7";
  public static final String LIMITED_KMS_ACCESS_IAM_ROLE =
    "arn:aws:iam::370957321024:role/GitHub-CI-MPL-Limited-KMS-us-west-2";
  // ^ can not access: MRK_ARN_EAST, MRK_ARN_WEST, and MRK_ARN_AP
  public static final String NO_KMS_ACCESS_IAM_ROLE =
    "arn:aws:iam::370957321024:role/GitHub-CI-MPL-No-KMS-us-west-2";

  public static final AwsCredentialsProvider defaultCreds =
    DefaultCredentialsProvider.create();
  public static final SdkHttpClient httpClient = ApacheHttpClient
    .builder()
    .connectionTimeToLive(Duration.ofSeconds(5))
    .build();
  public static final DynamoDbClient ddbClientWest2 = DynamoDbClient
    .builder()
    .httpClient(httpClient)
    .credentialsProvider(defaultCreds)
    .region(Region.US_WEST_2)
    .build();
  public static final KmsClient kmsClientWest2 = KmsClient
    .builder()
    .httpClient(httpClient)
    .credentialsProvider(defaultCreds)
    .region(Region.US_WEST_2)
    .build();
  public static final KmsClient kmsClientEast1 = KmsClient
    .builder()
    .httpClient(httpClient)
    .credentialsProvider(defaultCreds)
    .region(Region.US_EAST_1)
    .build();
  public static final KmsClient denyMrkKmsClient = KmsClient
    .builder()
    .credentialsProvider(
      CredentialUtils.credsForRole(
        Fixtures.LIMITED_KMS_ACCESS_IAM_ROLE,
        "java-mpl-examples",
        Region.US_WEST_2,
        Fixtures.httpClient,
        Fixtures.defaultCreds
      )
    )
    .region(Region.US_WEST_2)
    .httpClient(Fixtures.httpClient)
    .build();

  public static GetItemResponse getKeyStoreDdbItem(
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
    return dynamoDbClient.getItem(builder ->
      builder.tableName(physicalName).key(ddbKey)
    );
  }

  private static TransactWriteItem bkItemToDeleteReq(
    final Map<String, AttributeValue> item,
    final String _tableName
  ) {
    final Map<String, AttributeValue> key = new HashMap<>(3, 1);
    key.put("branch-key-id", item.get("branch-key-id"));
    key.put("type", item.get("type"));
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
      ? TEST_KEYSTORE_NAME
      : tableName;
    final String _hierarchyVersion = hierarchyVersion == null
      ? "1"
      : hierarchyVersion;
    final DynamoDbClient _ddbClient = ddbClient == null
      ? ddbClientWest2
      : ddbClient;
    final Map<String, String> ExpressionAttributeNames = new HashMap<>(3, 1);
    ExpressionAttributeNames.put("#pk", "branch-key-id");
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
