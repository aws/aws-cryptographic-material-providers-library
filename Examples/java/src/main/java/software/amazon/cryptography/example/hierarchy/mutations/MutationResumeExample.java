// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
package software.amazon.cryptography.example.hierarchy.mutations;

import java.util.HashMap;
import javax.annotation.Nonnull;
import javax.annotation.Nullable;
import software.amazon.cryptography.example.hierarchy.AdminProvider;
import software.amazon.cryptography.keystore.model.HierarchyVersion;
import software.amazon.cryptography.keystoreadmin.KeyStoreAdmin;
import software.amazon.cryptography.keystoreadmin.model.ApplyMutationResult;
import software.amazon.cryptography.keystoreadmin.model.DescribeMutationOutput;
import software.amazon.cryptography.keystoreadmin.model.InitializeMutationInput;
import software.amazon.cryptography.keystoreadmin.model.KeyManagementStrategy;
import software.amazon.cryptography.keystoreadmin.model.KmsSymmetricKeyArn;
import software.amazon.cryptography.keystoreadmin.model.MutationConflictException;
import software.amazon.cryptography.keystoreadmin.model.MutationToken;
import software.amazon.cryptography.keystoreadmin.model.Mutations;
import software.amazon.cryptography.keystoreadmin.model.SystemKey;

/**
 * Should a {@code MutationToken} be dropped,
 * a Mutation can still be completed by recovering the {@code MutationToken}
 * from the Key Store's Storage.
 * There are two ways to accomplish this:
 * <ul>
 *   <li>Call {@code InitializeMutation} with the same input</li>
 *   <li>Call {@code DescribeMutation} with the Branch Key ID</li>
 * </ul>
 * Both methods will return a {@code MutationToken} that can be used
 * by {@code ApplyMutation} to complete the Mutation.
 */
public class MutationResumeExample {

  public static String Resume2End(
    String branchKeyId,
    String terminalKmsArn,
    @Nullable HierarchyVersion terminalHierarchyVersion,
    @Nullable KeyManagementStrategy strategy,
    @Nullable SystemKey systemKey,
    @Nullable KeyStoreAdmin admin
  ) {
    boolean mutationConflictThrown = false;

    final KeyManagementStrategy _strategy = strategy == null
      ? AdminProvider.strategy(null)
      : strategy;
    final SystemKey _systemKey = systemKey == null
      ? MutationsProvider.KmsSystemKey()
      : systemKey;
    final KeyStoreAdmin _admin = admin == null ? AdminProvider.admin() : admin;

    System.out.println("BranchKey ID to mutate: " + branchKeyId);
    Mutations mutations = MutationsProvider.defaultMutation(
      terminalKmsArn,
      terminalHierarchyVersion
    );

    InitializeMutationInput initInput = InitializeMutationInput
      .builder()
      .Mutations(mutations)
      .Identifier(branchKeyId)
      .Strategy(_strategy)
      .SystemKey(_systemKey)
      .build();

    MutationToken token = MutationsProvider.executeInitialize(
      branchKeyId,
      _admin,
      initInput,
      "InitLogs"
    );
    // Work the Mutation once
    ApplyMutationResult result = MutationsProvider.workPage(
      branchKeyId,
      _systemKey,
      token,
      _strategy,
      _admin,
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
        _admin,
        initInput,
        "Resume Logs"
      );
    result =
      MutationsProvider.workPage(
        branchKeyId,
        _systemKey,
        token,
        _strategy,
        _admin,
        1
      );
    System.out.println(
      "\nInitialized vended a token and we applied one page of Mutation for: " +
      branchKeyId +
      "\n"
    );
    /*
    In some very advanced edge cases,
    it may be helpful to reset a Mutation,
    such that it goes over every Branch Key Version again.
    See {@link MutationsProvider#resetMutationIndex}
    for details on how to accomplish this.
    But this is NOT necessary to resume an in-flight Mutation;
    it is just helpful for this particular example.
    */
    MutationsProvider.resetMutationIndex(
      branchKeyId,
      initInput,
      null,
      null,
      _admin,
      null
    );
    try {
      // But if we try to resume it/call initialize mutation via a different input,
      // an exception is thrown
      HashMap<String, String> badTerminalEC = new HashMap<>();
      badTerminalEC.put("Robbie", "is a Cat.");
      Mutations badMutations = Mutations
        .builder()
        .TerminalEncryptionContext(badTerminalEC)
        .TerminalKmsArn(terminalKmsArn)
        .build();
      InitializeMutationInput badInput = InitializeMutationInput
        .builder()
        .Mutations(badMutations)
        .Identifier(branchKeyId)
        .Strategy(_strategy)
        .SystemKey(_systemKey)
        .build();
      MutationsProvider.executeInitialize(
        branchKeyId,
        _admin,
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
    // Instead of using Initialize to recover a token,
    // we can use DescribeMutation
    DescribeMutationOutput describeRes = DescribeMutationExample.Example(
      branchKeyId,
      null
    );
    assert describeRes != null : "DescribeMutationExample returned null";
    assert describeRes.MutationInFlight().Yes() !=
    null : "DescribeMutationExample returned no in-flight";
    // OK. We have proven we can Resume, Restart,
    // and correctly fail if the wrong input is given
    System.out.println(
      "\nGoing to complete the mutation for: " + branchKeyId + "\n"
    );
    MutationsProvider.workMutation(
      branchKeyId,
      _systemKey,
      describeRes.MutationInFlight().Yes().MutationToken(),
      _strategy,
      _admin,
      (short) 10
    );

    System.out.println("Done with Mutation: " + branchKeyId);

    assert mutationConflictThrown;
    return branchKeyId;
  }
}
