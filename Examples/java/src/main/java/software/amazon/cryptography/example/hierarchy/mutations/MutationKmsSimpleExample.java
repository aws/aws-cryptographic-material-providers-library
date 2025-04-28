package software.amazon.cryptography.example.hierarchy.mutations;

import javax.annotation.Nonnull;
import javax.annotation.Nullable;
import software.amazon.cryptography.example.hierarchy.AdminProvider;
import software.amazon.cryptography.keystore.model.AwsKms;
import software.amazon.cryptography.keystore.model.HierarchyVersion;
import software.amazon.cryptography.keystoreadmin.KeyStoreAdmin;
import software.amazon.cryptography.keystoreadmin.model.*;

// TODO-HV-2-FF: Support KMS simple for HV-1 to HV-1 mutation
/**
 * See {@link MutationExample} for an explanation on Mutations.
 * AwsKmsSimple is the simple option, that uses one KMS Client (and Grant Token list) and supports both hierarchy-versions.
 * For HV-1, kms:GenerateDataKeyWithoutPlaintext followed by kms:ReEncrypt is used to create branch keys.
 * For HV-2, plain-text data keys (PDKs) are created locally via the hosts random number generator;
 * The branch key context (BKC) and the PDK are protected by kms:Encrypt.
 * For HV-1, to validate a branch key item, kms:ReEncrypt is used.
 * For HV-2, to validate a branch key item, kms:Decrypt un-wraps the BKC-PDK tuple,
 * and the client verifies the read BKC against the protected BKC.
 */

public class MutationKmsSimpleExample {

  public static String End2End(
    @Nonnull final String branchKeyId,
    @Nonnull final String terminalKmsArn,
    @Nullable final HierarchyVersion terminalHierarchyVersion,
    @Nonnull final SystemKey systemKey,
    @Nullable final KeyStoreAdmin admin
  ) {
    final KeyManagementStrategy strategy = KeyManagementStrategy
      .builder()
      .AwsKmsSimple(AwsKms.builder().build())
      .build();
    Mutations mutations = MutationsProvider.defaultMutation(
      terminalKmsArn,
      terminalHierarchyVersion
    );
    final KeyStoreAdmin _admin = admin == null ? AdminProvider.admin() : admin;
    InitializeMutationInput initInput = InitializeMutationInput
      .builder()
      .Mutations(mutations)
      .Identifier(branchKeyId)
      .Strategy(strategy)
      .SystemKey(systemKey)
      // TODO-HV-2-FF: Versioning in KMS simple is not yet supported.
      .DoNotVersion(true)
      .build();
    InitializeMutationOutput initOutput = _admin.InitializeMutation(initInput);
    MutationToken token = initOutput.MutationToken();
    System.out.println(
      "InitLogs: " +
      branchKeyId +
      " items: \n" +
      MutationsProvider.mutatedItemsToString(initOutput.MutatedBranchKeyItems())
    );
    MutationsProvider.workMutation(
      branchKeyId,
      systemKey,
      token,
      strategy,
      _admin,
      (short) 10
    );
    System.out.println("Done with Mutation: " + branchKeyId);
    return branchKeyId;
  }
}
