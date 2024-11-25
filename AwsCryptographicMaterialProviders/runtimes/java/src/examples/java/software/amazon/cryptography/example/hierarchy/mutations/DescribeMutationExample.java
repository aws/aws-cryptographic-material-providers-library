// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
package software.amazon.cryptography.example.hierarchy.mutations;

import static software.amazon.cryptography.example.hierarchy.mutations.MutationsProvider.executeInitialize;

import java.util.HashMap;
import java.util.Objects;
import javax.annotation.Nullable;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
import software.amazon.awssdk.services.kms.KmsClient;
import software.amazon.cryptography.example.hierarchy.AdminProvider;
import software.amazon.cryptography.example.hierarchy.CreateKeyExample;
import software.amazon.cryptography.keystoreadmin.KeyStoreAdmin;
import software.amazon.cryptography.keystoreadmin.model.DescribeMutationInput;
import software.amazon.cryptography.keystoreadmin.model.DescribeMutationOutput;
import software.amazon.cryptography.keystoreadmin.model.InitializeMutationInput;
import software.amazon.cryptography.keystoreadmin.model.KeyManagementStrategy;
import software.amazon.cryptography.keystoreadmin.model.MutationDescription;
import software.amazon.cryptography.keystoreadmin.model.MutationToken;
import software.amazon.cryptography.keystoreadmin.model.Mutations;
import software.amazon.cryptography.keystoreadmin.model.SystemKey;

public class DescribeMutationExample {

  @Nullable
  public static MutationToken Example(
    String keyStoreTableName,
    String logicalKeyStoreName,
    String branchKeyId,
    @Nullable DynamoDbClient dynamoDbClient
  ) {
    KeyStoreAdmin admin = AdminProvider.admin(
      keyStoreTableName,
      logicalKeyStoreName,
      dynamoDbClient
    );
    DescribeMutationInput input = DescribeMutationInput
      .builder()
      .Identifier(branchKeyId)
      .build();
    DescribeMutationOutput output = admin.DescribeMutation(input);
    if (output.MutationInFlight().No() != null) {
      System.out.println(
        "There is no mutation in flight for Branch Key ID: " + branchKeyId
      );
      return null;
    }
    if (output.MutationInFlight().Yes() != null) {
      MutationDescription description = output.MutationInFlight().Yes();
      System.out.println(
        "There is a mutation in flight for Branch Key ID: " + branchKeyId
      );
      System.out.println(
        "Description: " + description.MutationDetails().UUID()
      );
      return description.MutationToken();
    }
    throw new RuntimeException("Key Store Admin returned nonsensical response");
  }

  public static MutationToken InitMutation(
    String keyStoreTableName,
    String logicalKeyStoreName,
    String kmsKeyArnTerminal,
    String branchKeyId,
    SystemKey systemKey,
    @Nullable DynamoDbClient dynamoDbClient,
    @Nullable KmsClient kmsClient
  ) {
    kmsClient = AdminProvider.kms(kmsClient);
    KeyManagementStrategy strategy = AdminProvider.strategy(kmsClient);
    KeyStoreAdmin admin = AdminProvider.admin(
      keyStoreTableName,
      logicalKeyStoreName,
      dynamoDbClient
    );
    HashMap<String, String> terminalEC = new HashMap<>();
    terminalEC.put("Robbie", "is a dog.");
    Mutations mutations = Mutations
      .builder()
      .TerminalEncryptionContext(terminalEC)
      .TerminalKmsArn(kmsKeyArnTerminal)
      .build();
    InitializeMutationInput initInput = InitializeMutationInput
      .builder()
      .Mutations(mutations)
      .Identifier(branchKeyId)
      .Strategy(strategy)
      .SystemKey(systemKey)
      .build();

    MutationToken token = executeInitialize(
      branchKeyId,
      admin,
      initInput,
      "InitLogs"
    );
    return token;
  }

  public static void CompleteExample(
    String keyStoreTableName,
    String logicalKeyStoreName,
    String kmsKeyArnOriginal,
    String kmsKeyArnTerminal,
    String branchKeyId,
    SystemKey systemKey,
    @Nullable DynamoDbClient dynamoDbClient,
    @Nullable KmsClient kmsClient
  ) {
    CreateKeyExample.CreateKey(
      keyStoreTableName,
      logicalKeyStoreName,
      kmsKeyArnOriginal,
      branchKeyId,
      dynamoDbClient
    );

    MutationToken fromInit = InitMutation(
      keyStoreTableName,
      logicalKeyStoreName,
      kmsKeyArnTerminal,
      branchKeyId,
      systemKey,
      dynamoDbClient,
      kmsClient
    );

    MutationToken fromDescribe = Example(
      keyStoreTableName,
      logicalKeyStoreName,
      branchKeyId,
      dynamoDbClient
    );
    assert fromDescribe != null;
    assert Objects.equals(fromInit.UUID(), fromDescribe.UUID());
  }
}
