// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
package software.amazon.cryptography.example.hierarchy.mutations;

import java.util.HashMap;
import javax.annotation.Nullable;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
import software.amazon.awssdk.services.kms.KmsClient;
import software.amazon.cryptography.example.DdbHelper;
import software.amazon.cryptography.example.Fixtures;
import software.amazon.cryptography.example.hierarchy.AdminProvider;
import software.amazon.cryptography.keystoreadmin.KeyStoreAdmin;
import software.amazon.cryptography.keystoreadmin.model.ApplyMutationResult;
import software.amazon.cryptography.keystoreadmin.model.InitializeMutationInput;
import software.amazon.cryptography.keystoreadmin.model.KeyManagementStrategy;
import software.amazon.cryptography.keystoreadmin.model.MutationConflictException;
import software.amazon.cryptography.keystoreadmin.model.MutationToken;
import software.amazon.cryptography.keystoreadmin.model.Mutations;
import software.amazon.cryptography.keystoreadmin.model.SystemKey;
import software.amazon.cryptography.keystoreadmin.model.TrustStorage;

public class MutationResumeExample {

  public static String Resume2End(
    String physicalName,
    String logicalName,
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
      physicalName,
      logicalName,
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

    MutationToken token = MutationsProvider.executeInitialize(
      branchKeyId,
      admin,
      initInput,
      "InitLogs"
    );
    // Work the Mutation once
    ApplyMutationResult result = MutationsProvider.workPage(
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
    token =
      MutationsProvider.executeInitialize(
        branchKeyId,
        admin,
        initInput,
        "Resume Logs"
      );
    result =
      MutationsProvider.workPage(
        branchKeyId,
        systemKey,
        token,
        strategy,
        admin,
        1
      );
    System.out.println(
      "\nInitialized vended a token and we applied one page of Mutation for: " +
      branchKeyId +
      "\n"
    );
    // If we want to restart the Mutation from the beginning, we delete the Index.
    DdbHelper.deleteKeyStoreDdbItem(
      branchKeyId,
      "branch:MUTATION_INDEX",
      logicalName,
      dynamoDbClient,
      false
    );
    // But if we deleted the index, we do need to call Initialize again
    token =
      MutationsProvider.executeInitialize(
        branchKeyId,
        admin,
        initInput,
        "Restart Logs"
      );
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
      MutationsProvider.executeInitialize(
        branchKeyId,
        admin,
        badInput,
        "Fail Resume Logs"
      );
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
    MutationsProvider.workMutation(
      branchKeyId,
      systemKey,
      token,
      strategy,
      admin
    );

    System.out.println("Done with Mutation: " + branchKeyId);

    assert mutationConflictThrown;
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
      SystemKey.builder().trustStorage(TrustStorage.builder().build()).build(),
      null,
      null
    );
    Fixtures.cleanUpBranchKeyId(null, branchKeyId, true);
  }
}
