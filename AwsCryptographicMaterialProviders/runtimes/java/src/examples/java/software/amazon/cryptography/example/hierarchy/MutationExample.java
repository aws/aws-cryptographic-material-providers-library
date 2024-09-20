// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
package software.amazon.cryptography.example.hierarchy;

import java.util.HashMap;
import javax.annotation.Nullable;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
import software.amazon.awssdk.services.kms.KmsClient;
import software.amazon.cryptography.keystoreadmin.KeyStoreAdmin;
import software.amazon.cryptography.keystoreadmin.model.ApplyMutationInput;
import software.amazon.cryptography.keystoreadmin.model.ApplyMutationOutput;
import software.amazon.cryptography.keystoreadmin.model.ApplyMutationResult;
import software.amazon.cryptography.keystoreadmin.model.InitializeMutationInput;
import software.amazon.cryptography.keystoreadmin.model.InitializeMutationOutput;
import software.amazon.cryptography.keystoreadmin.model.KeyManagementStrategy;
import software.amazon.cryptography.keystoreadmin.model.MutationToken;
import software.amazon.cryptography.keystoreadmin.model.Mutations;

public class MutationExample {

  public static String End2End(
    String keyStoreTableName,
    String logicalKeyStoreName,
    String kmsKeyArnOriginal,
    String kmsKeyArnTerminal,
    @Nullable DynamoDbClient dynamoDbClient,
    @Nullable KmsClient kmsClient
  ) {
    kmsClient = AdminProvider.kms(kmsClient);
    KeyStoreAdmin admin = AdminProvider.admin(
      keyStoreTableName,
      logicalKeyStoreName,
      dynamoDbClient
    );
    KeyManagementStrategy strategy = AdminProvider.strategy(kmsClient);

    String branchKeyId = CreateKeyExample.CreateKey(
      keyStoreTableName,
      logicalKeyStoreName,
      kmsKeyArnOriginal,
      dynamoDbClient,
      kmsClient
    );
    System.out.println("BranchKey ID to mutate: " + branchKeyId);
    HashMap<String, String> terminalEC = new HashMap<>();
    terminalEC.put("Robbie", "is a dog.");
    Mutations mutations = Mutations
      .builder()
      .terminalEncryptionContext(terminalEC)
      .terminalKmsArn(kmsKeyArnTerminal)
      .build();

    InitializeMutationInput initInput = InitializeMutationInput
      .builder()
      .mutations(mutations)
      .branchKeyIdentifier(branchKeyId)
      .strategy(strategy)
      .build();

    InitializeMutationOutput initOutput = admin.InitializeMutation(initInput);

    MutationToken token = initOutput.mutationToken();
    System.out.println(
      "InitLogs: " +
      branchKeyId +
      " items: \n" +
      AdminProvider.mutatedItemsToString(initOutput.mutatedBranchKeyItems())
    );
    boolean done = false;
    int limitLoop = 10;

    while (!done) {
      ApplyMutationInput applyInput = ApplyMutationInput
        .builder()
        .mutationToken(token)
        .pageSize(98)
        .strategy(strategy)
        .build();
      ApplyMutationOutput applyOutput = admin.ApplyMutation(applyInput);
      ApplyMutationResult result = applyOutput.result();

      System.out.println(
        "ApplyLogs: " +
        branchKeyId +
        " items: \n" +
        AdminProvider.mutatedItemsToString(applyOutput.mutatedBranchKeyItems())
      );

      if (result.continueMutation() != null) token = result.continueMutation();
      if (result.completeMutation() != null) done = true;
      if (limitLoop == 0) done = true;

      limitLoop--;
    }

    System.out.println("Done with Mutation: " + branchKeyId);

    return branchKeyId;
  }

  public static void main(final String[] args) {
    if (args.length <= 1) {
      throw new IllegalArgumentException(
        "To run this example, include the keyStoreTableName, logicalKeyStoreName, kmsKeyOriginal, and kmsKeyTerminal in args"
      );
    }
    final String keyStoreTableName = args[0];
    final String logicalKeyStoreName = args[1];
    final String kmsKeyArnOriginal = args[2];
    final String kmsKeyArnTerminal = args[3];
    End2End(
      keyStoreTableName,
      logicalKeyStoreName,
      kmsKeyArnOriginal,
      kmsKeyArnTerminal,
      null,
      null
    );
  }
}
