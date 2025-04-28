// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
package software.amazon.cryptography.example.hierarchy.mutations;

import static software.amazon.cryptography.example.hierarchy.mutations.MutationsProvider.executeInitialize;
import static software.amazon.cryptography.example.hierarchy.mutations.MutationsProvider.workPage;

import java.util.List;
import java.util.Objects;
import javax.annotation.Nonnull;
import javax.annotation.Nullable;
import software.amazon.awssdk.services.kms.KmsClient;
import software.amazon.cryptography.example.Fixtures;
import software.amazon.cryptography.example.hierarchy.AdminProvider;
import software.amazon.cryptography.keystore.model.HierarchyVersion;
import software.amazon.cryptography.keystoreadmin.KeyStoreAdmin;
import software.amazon.cryptography.keystoreadmin.model.ApplyMutationResult;
import software.amazon.cryptography.keystoreadmin.model.InitializeMutationInput;
import software.amazon.cryptography.keystoreadmin.model.KeyManagementStrategy;
import software.amazon.cryptography.keystoreadmin.model.MutationToken;
import software.amazon.cryptography.keystoreadmin.model.MutationVerificationException;
import software.amazon.cryptography.keystoreadmin.model.Mutations;
import software.amazon.cryptography.keystoreadmin.model.SystemKey;

/**
 * To ensure a Mutation is applied consistently to all items
 * of a Branch Key,
 * the library persists the Mutation into the Key Store's Storage.
 * An agent with write access to this storage
 * could manipulate the persisted Mutation.
 * To mitigate this risk,
 * AWS Crypto Tools recommends using a KMS System Key.
 * This example demonstrates a KMS System Key configuration,
 * which protects these persisted non-Branch Key items with a KMS Key.
 */
public class MutationSystemKeyKMSExample {

  public static String End2End(
    @Nonnull final String systemKeyArn,
    @Nonnull final String identifier,
    @Nonnull final String terminalKmsArn,
    @Nullable final HierarchyVersion terminalHierarchyVersion
  ) {
    return End2End(
      systemKeyArn,
      identifier,
      terminalKmsArn,
      terminalHierarchyVersion,
      null,
      null,
      null,
      null,
      null
    );
  }

  public static String End2End(
    @Nonnull final String systemKeyArn,
    @Nonnull final String identifier,
    @Nonnull final String terminalKmsArn,
    @Nonnull final HierarchyVersion terminalHierarchyVersion,
    @Nullable KmsClient systemKeyKmsClient,
    @Nullable List<String> systemKeyGrantTokens,
    @Nullable KeyStoreAdmin admin,
    @Nullable Mutations mutations,
    @Nullable KeyManagementStrategy strategy
  ) {
    // 1. Create a SystemKey Object
    SystemKey systemKey = MutationsProvider.KmsSystemKey(
      systemKeyArn,
      systemKeyKmsClient,
      systemKeyGrantTokens
    );

    // 2. Mutation's persisted objects will now be signed by the KMS Key
    assert mutations == null ||
    Objects.equals(mutations.TerminalKmsArn(), terminalKmsArn);
    admin =
      admin == null
        ? AdminProvider.admin(
          Fixtures.TEST_KEYSTORE_NAME,
          Fixtures.TEST_LOGICAL_KEYSTORE_NAME,
          Fixtures.ddbClientWest2
        )
        : admin;
    mutations =
      mutations == null
        ? MutationsProvider.defaultMutation(
          terminalKmsArn,
          terminalHierarchyVersion
        )
        : mutations;
    strategy = strategy == null ? AdminProvider.strategy(null) : strategy;
    InitializeMutationInput initInput = InitializeMutationInput
      .builder()
      .Mutations(mutations)
      .Identifier(identifier)
      .Strategy(strategy)
      .SystemKey(systemKey)
      .build();

    // InitializeMutation will protect the Mutation Commitment and Mutation Index with the System Key
    MutationToken token = executeInitialize(
      identifier,
      admin,
      initInput,
      "InitLogs"
    );

    ApplyMutationResult result;
    boolean exThrown = false;
    // The Mutation is protected from Downgrade attacks
    try {
      result =
        workPage(
          identifier,
          MutationsProvider.TrustStorage(),
          token,
          strategy,
          admin,
          1
        );
    } catch (MutationVerificationException ex) {
      System.out.println(
        "Apply with wrong SystemKey failed with: \n" +
        ex.getClass().getSimpleName() +
        ": " +
        ex.getMessage()
      );
      exThrown = true;
    }

    // The Mutation can be completed with the correct System Key
    result = workPage(identifier, systemKey, token, strategy, admin, 99);
    assert exThrown;
    assert result.CompleteMutation() != null;
    return identifier;
  }
}
