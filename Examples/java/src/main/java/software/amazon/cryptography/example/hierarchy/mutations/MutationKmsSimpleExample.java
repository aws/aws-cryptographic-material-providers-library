package software.amazon.cryptography.example.hierarchy.mutations;

import javax.annotation.Nonnull;
import javax.annotation.Nullable;
import software.amazon.cryptography.example.hierarchy.AdminProvider;
import software.amazon.cryptography.keystore.model.AwsKms;
import software.amazon.cryptography.keystore.model.HierarchyVersion;
import software.amazon.cryptography.keystoreadmin.KeyStoreAdmin;
import software.amazon.cryptography.keystoreadmin.model.*;

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
