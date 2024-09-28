// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
package software.amazon.cryptography.example.hierarchy;

import java.util.List;
import java.util.stream.Collectors;
import javax.annotation.Nullable;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
import software.amazon.awssdk.services.kms.KmsClient;
import software.amazon.cryptography.keystore.model.AwsKms;
import software.amazon.cryptography.keystore.model.DynamoDBTable;
import software.amazon.cryptography.keystore.model.Storage;
import software.amazon.cryptography.keystoreadmin.KeyStoreAdmin;
import software.amazon.cryptography.keystoreadmin.model.KeyManagementStrategy;
import software.amazon.cryptography.keystoreadmin.model.KeyStoreAdminConfig;
import software.amazon.cryptography.keystoreadmin.model.MutatedBranchKeyItem;

public class AdminProvider {

  public static KeyStoreAdmin admin(
    String keyStoreTableName,
    String logicalKeyStoreName,
    @Nullable DynamoDbClient dynamoDbClient
  ) {
    DynamoDBTable table = DynamoDBTable
      .builder()
      .ddbClient(dynamoDbClient)
      .ddbTableName(keyStoreTableName)
      .build();
    Storage storage = Storage.builder().ddb(table).build();

    KeyStoreAdminConfig config = KeyStoreAdminConfig
      .builder()
      .logicalKeyStoreName(logicalKeyStoreName)
      .storage(storage)
      .build();

    return KeyStoreAdmin.builder().KeyStoreAdminConfig(config).build();
  }

  public static KeyManagementStrategy strategy(@Nullable KmsClient kmsClient) {
    kmsClient = kms(kmsClient);
    return KeyManagementStrategy
      .builder()
      .AwsKmsReEncrypt(AwsKms.builder().kmsClient(kmsClient).build())
      .build();
  }

  @SuppressWarnings("resource")
  public static DynamoDbClient dynamoDB(
    @Nullable DynamoDbClient dynamoDbClient
  ) {
    if (dynamoDbClient == null) {
      dynamoDbClient = DynamoDbClient.create();
    }
    return dynamoDbClient;
  }

  @SuppressWarnings("resource")
  public static KmsClient kms(@Nullable KmsClient kmsClient) {
    if (kmsClient == null) {
      kmsClient = KmsClient.create();
    }
    return kmsClient;
  }

  public static String mutatedItemsToString(
    List<MutatedBranchKeyItem> mutatedItems
  ) {
    return mutatedItems
      .stream()
      .map(item -> String.format("%s : %s", item.ItemType(), item.Description())
      )
      .collect(Collectors.joining(",\n"));
  }
}
