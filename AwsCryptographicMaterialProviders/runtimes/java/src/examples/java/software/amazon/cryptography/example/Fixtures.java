// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
package software.amazon.cryptography.example;

import java.time.Duration;
import java.util.HashMap;
import java.util.Map;
import javax.annotation.Nullable;
import software.amazon.awssdk.auth.credentials.AwsCredentialsProvider;
import software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider;
import software.amazon.awssdk.http.SdkHttpClient;
import software.amazon.awssdk.http.apache.ApacheHttpClient;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
import software.amazon.awssdk.services.dynamodb.model.AttributeValue;
import software.amazon.awssdk.services.dynamodb.model.GetItemResponse;
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

  public static void cleanUpBranchKeyId(
    KeyStorageInterface storage,
    String branchKeyId
  ) {
    QueryForVersionsOutput versions = storage.QueryForVersions(
      QueryForVersionsInput
        .builder()
        .Identifier(branchKeyId)
        .PageSize(99)
        .build()
    );
    String physicalName = storage
      .GetKeyStorageInfo(GetKeyStorageInfoInput.builder().build())
      .Name();
    versions
      .Items()
      .forEach(item ->
        DdbHelper.deleteKeyStoreDdbItem(
          item.Identifier(),
          item.EncryptionContext().get("type"),
          physicalName,
          ddbClientWest2,
          false
        )
      );

    DdbHelper.deleteKeyStoreDdbItem(
      branchKeyId,
      "branch:ACTIVE",
      physicalName,
      ddbClientWest2,
      false
    );
    DdbHelper.deleteKeyStoreDdbItem(
      branchKeyId,
      "beacon:ACTIVE",
      physicalName,
      ddbClientWest2,
      false
    );
  }
}
