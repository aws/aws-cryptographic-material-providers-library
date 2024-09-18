// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
package software.amazon.cryptography.example.hierarchy;

import java.util.HashMap;
import javax.annotation.Nullable;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
import software.amazon.awssdk.services.kms.KmsClient;
import software.amazon.cryptography.example.DdbHelper;
import software.amazon.cryptography.keystoreadmin.KeyStoreAdmin;
import software.amazon.cryptography.keystoreadmin.model.ApplyMutationInput;
import software.amazon.cryptography.keystoreadmin.model.ApplyMutationOutput;
import software.amazon.cryptography.keystoreadmin.model.ApplyMutationResult;
import software.amazon.cryptography.keystoreadmin.model.InitializeMutationInput;
import software.amazon.cryptography.keystoreadmin.model.InitializeMutationOutput;
import software.amazon.cryptography.keystoreadmin.model.KeyManagementStrategy;
import software.amazon.cryptography.keystoreadmin.model.MutationConflictException;
import software.amazon.cryptography.keystoreadmin.model.MutationToken;
import software.amazon.cryptography.keystoreadmin.model.Mutations;
import software.amazon.cryptography.keystoreadmin.model.SystemKey;
import software.amazon.cryptography.keystoreadmin.model.TrustStorage;

public class MutationResumeExample {

  public static String Resume2End(
    String keyStoreTableName,
    String logicalKeyStoreName,
    String kmsKeyArnTerminal,
    String branchKeyId,
    SystemKey systemKey,
    @Nullable DynamoDbClient dynamoDbClient,
    @Nullable KmsClient kmsClient
  ) {
    boolean mutationConflictThrown = false;

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
      .SystemKey(systemKey)
      .build();

    MutationToken token = executeInitialize(
      branchKeyId,
      admin,
      initInput,
      "InitLogs"
    );
    // Work the Mutation once
    ApplyMutationResult result = workPage(
      branchKeyId,
      systemKey,
      token,
      strategy,
      admin,
      1
    );
    System.out.println(
      "\nInitialized and Applied one page of Mutation for: " +
      branchKeyId +
      "\n"
    );
    // Pretend the Mutation is halted for some reason.
    // We can Resume it by calling Initialize again.
    token = executeInitialize(branchKeyId, admin, initInput, "Resume Logs");
    result = workPage(branchKeyId, systemKey, token, strategy, admin, 1);
    System.out.println(
      "\nInitialized vended a token and we applied one page of Mutation for: " +
      branchKeyId +
      "\n"
    );
    // If we want to restart the Mutation from the beginning, we delete the Index.
    DdbHelper.deleteKeyStoreDdbItem(
      branchKeyId,
      "branch:MUTATION_INDEX",
      logicalKeyStoreName,
      dynamoDbClient
    );
    // But if we deleted the index, we do need to call Initialize again
    token = executeInitialize(branchKeyId, admin, initInput, "Restart Logs");
    System.out.println(
      "\nDeletion of Index and subsequent call to Initialize reset the pageIndex: " +
      branchKeyId +
      "\n"
    );
    try {
      // But if we try to resume it/call initialize mutation via a different input,
      // an exception is thrown
      HashMap<String, String> badTerminalEC = new HashMap<>();
      badTerminalEC.put("Robbie", "is a Cat.");
      Mutations badMutations = Mutations
        .builder()
        .TerminalEncryptionContext(badTerminalEC)
        .TerminalKmsArn(kmsKeyArnTerminal)
        .build();
      InitializeMutationInput badInput = InitializeMutationInput
        .builder()
        .Mutations(badMutations)
        .Identifier(branchKeyId)
        .Strategy(strategy)
        .SystemKey(systemKey)
        .build();
      executeInitialize(branchKeyId, admin, badInput, "Fail Resume Logs");
    } catch (MutationConflictException ex) {
      System.out.println(
        "\nCalling Initialize for a different input failed for: " +
        branchKeyId +
        "\n"
      );
      System.out.println(ex.getMessage());
      mutationConflictThrown = true;
    }
    // OK. We have proven we can Resume, Restart,
    // and correctly fail if the wrong input is given
    System.out.println(
      "\nGoing to complete the mutation for: " + branchKeyId + "\n"
    );
    workMutation(branchKeyId, systemKey, token, strategy, admin);

    System.out.println("Done with Mutation: " + branchKeyId);

    assert mutationConflictThrown;
    return branchKeyId;
  }

  public static void workMutation(
    String branchKeyId,
    SystemKey systemKey,
    MutationToken token,
    KeyManagementStrategy strategy,
    KeyStoreAdmin admin
  ) {
    boolean done = false;
    int limitLoop = 10;

    while (!done) {
      ApplyMutationResult result = workPage(
        branchKeyId,
        systemKey,
        token,
        strategy,
        admin,
        98
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
  }

  private static ApplyMutationResult workPage(
    String branchKeyId,
    SystemKey systemKey,
    MutationToken token,
    KeyManagementStrategy strategy,
    KeyStoreAdmin admin,
    Integer pageSize
  ) {
    ApplyMutationInput applyInput = ApplyMutationInput
      .builder()
      .MutationToken(token)
      .PageSize(pageSize)
      .Strategy(strategy)
      .SystemKey(systemKey)
      .build();
    ApplyMutationOutput applyOutput = admin.ApplyMutation(applyInput);
    ApplyMutationResult result = applyOutput.MutationResult();

    System.out.println(
      "ApplyLogs: " +
      branchKeyId +
      " items: \n" +
      AdminProvider.mutatedItemsToString(applyOutput.MutatedBranchKeyItems())
    );
    return result;
  }

  private static MutationToken executeInitialize(
    String branchKeyId,
    KeyStoreAdmin admin,
    InitializeMutationInput initInput,
    String logPrefix
  ) {
    InitializeMutationOutput initOutput = admin.InitializeMutation(initInput);
    MutationToken token = initOutput.MutationToken();
    System.out.println(
      logPrefix +
      ": " +
      "\nFlag: " +
      initOutput.InitializeMutationFlag().toString() +
      "\nIdentifier: " +
      branchKeyId +
      "\nitems: \n" +
      AdminProvider.mutatedItemsToString(initOutput.MutatedBranchKeyItems())
    );
    return token;
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
      SystemKey.builder().trustStorage(TrustStorage.builder().build()).build(),
      null,
      null
    );
  }
}
