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

public class MutationResumeExample {

  public static String Resume2End(
    String keyStoreTableName,
    String logicalKeyStoreName,
    String kmsKeyArnTerminal,
    String branchKeyId,
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

    System.out.println("BranchKey ID to mutate: " + branchKeyId);
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
      .build();

    InitializeMutationOutput initOutput = admin.InitializeMutation(initInput);

    MutationToken token = initOutput.MutationToken();
    System.out.println(
      "InitLogs: " +
      branchKeyId +
      " items: \n" +
      AdminProvider.mutatedItemsToString(initOutput.MutatedBranchKeyItems())
    );

    // Pretend the Mutation is halted for some reason.
    initOutput = admin.InitializeMutation(initInput);

    token = initOutput.MutationToken();
    System.out.println(
      "Resume Logs: " +
      branchKeyId +
      " items: \n" +
      AdminProvider.mutatedItemsToString(initOutput.MutatedBranchKeyItems())
    );

    boolean done = false;
    int limitLoop = 10;

    while (!done) {
      ApplyMutationInput applyInput = ApplyMutationInput
        .builder()
        .MutationToken(token)
        .PageSize(98)
        .Strategy(strategy)
        .build();
      ApplyMutationOutput applyOutput = admin.ApplyMutation(applyInput);
      ApplyMutationResult result = applyOutput.MutationResult();

      System.out.println(
        "ApplyLogs: " +
        branchKeyId +
        " items: \n" +
        AdminProvider.mutatedItemsToString(applyOutput.MutatedBranchKeyItems())
      );

      if (result.ContinueMutation() != null) {
        token = result.ContinueMutation();
      }
      if (result.CompleteMutation() != null) {
        done = true;
      }
      if (limitLoop == 0) {
        done = true;
      }

      limitLoop--;
    }

    System.out.println("Done with Mutation: " + branchKeyId);

    return branchKeyId;
  }

  public static void main(final String[] args) {
    if (args.length <= 1) {
      throw new IllegalArgumentException(
        "To run this example, include the keyStoreTableName, logicalKeyStoreName, and kmsKeyTerminal in args"
      );
    }
    final String keyStoreTableName = args[0];
    final String logicalKeyStoreName = args[1];
    final String kmsKeyArnTerminal = args[2];
    final String branchKeyId = args[3];
    Resume2End(
      keyStoreTableName,
      logicalKeyStoreName,
      kmsKeyArnTerminal,
      branchKeyId,
      null,
      null
    );
  }
}
