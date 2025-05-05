package software.amazon.cryptography.example.hierarchy.mutations;

import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import org.testng.Assert;
import software.amazon.awssdk.services.kms.model.KmsException;
import software.amazon.cryptography.example.DdbHelper;
import software.amazon.cryptography.example.Fixtures;
import software.amazon.cryptography.example.hierarchy.AdminProvider;
import software.amazon.cryptography.keystoreadmin.KeyStoreAdmin;
import software.amazon.cryptography.keystoreadmin.model.ApplyMutationInput;
import software.amazon.cryptography.keystoreadmin.model.ApplyMutationOutput;
import software.amazon.cryptography.keystoreadmin.model.ApplyMutationResult;
import software.amazon.cryptography.keystoreadmin.model.InitializeMutationInput;
import software.amazon.cryptography.keystoreadmin.model.InitializeMutationOutput;
import software.amazon.cryptography.keystoreadmin.model.KeyManagementStrategy;
import software.amazon.cryptography.keystoreadmin.model.MutationFromException;
import software.amazon.cryptography.keystoreadmin.model.MutationToException;
import software.amazon.cryptography.keystoreadmin.model.MutationToken;
import software.amazon.cryptography.keystoreadmin.model.Mutations;
import software.amazon.cryptography.keystoreadmin.model.SystemKey;
import software.amazon.cryptography.keystoreadmin.model.TrustStorage;

public class KmsInFlightMutationAccessDeniedRunner {

  private static final Pattern BRANCH_KEY_TYPE_PATTERN = Pattern.compile(
    "Branch Key Type: ([^;]+)"
  );

  public static void runMutationTest(
    String branchKeyId,
    Mutations mutations,
    KeyManagementStrategy initStrategy,
    KeyManagementStrategy applyStrategy,
    int expectedExceptionCount,
    boolean expectFromException,
    boolean expectToException
  ) {
    List<Exception> exceptions = new ArrayList<>();
    boolean isFromThrown = false;
    boolean isToThrown = false;

    SystemKey systemKey = SystemKey
      .builder()
      .trustStorage(TrustStorage.builder().build())
      .build();
    KeyStoreAdmin admin = AdminProvider.admin();

    // Initialize mutation
    InitializeMutationOutput initOutput = admin.InitializeMutation(
      InitializeMutationInput
        .builder()
        .Mutations(mutations)
        .Identifier(branchKeyId)
        .Strategy(initStrategy)
        .DoNotVersion(true)
        .SystemKey(systemKey)
        .build()
    );
    System.out.println(
      "InitLogs: " +
      branchKeyId +
      " items: \n" +
      MutationsProvider.mutatedItemsToString(initOutput.MutatedBranchKeyItems())
    );

    // Apply mutation
    MutationToken token = initOutput.MutationToken();
    boolean done = false;
    int limitLoop = 5;

    while (!done) {
      try {
        limitLoop--;
        if (limitLoop == 0) done = true;

        ApplyMutationOutput applyOutput = admin.ApplyMutation(
          ApplyMutationInput
            .builder()
            .MutationToken(token)
            .PageSize(1)
            .Strategy(applyStrategy)
            .SystemKey(systemKey)
            .build()
        );
        System.out.println(
          "\nApplyLogs: " +
          branchKeyId +
          " items: \n" +
          MutationsProvider.mutatedItemsToString(
            applyOutput.MutatedBranchKeyItems()
          )
        );
        ApplyMutationResult result = applyOutput.MutationResult();
        if (result.ContinueMutation() != null) {
          token = result.ContinueMutation();
        }
        if (result.CompleteMutation() != null) {
          done = true;
        }
      } catch (Exception e) {
        if (e instanceof MutationToException) {
          isToThrown = true;
        }
        if (e instanceof MutationFromException) {
          isFromThrown = true;
        }
        handleException(e, branchKeyId);
        exceptions.add(e);
      }
    }

    // Verify results
    Assert.assertEquals(
      exceptions.size(),
      expectedExceptionCount,
      String.format(
        "Expected %d exceptions but got %d",
        expectedExceptionCount,
        exceptions.size()
      )
    );
    Assert.assertEquals(
      isFromThrown,
      expectFromException,
      "MutationFromException expectation mismatch"
    );
    Assert.assertEquals(
      isToThrown,
      expectToException,
      "MutationToException expectation mismatch"
    );
  }

  private static void handleException(Exception e, String branchKeyId) {
    if (e instanceof KmsException) {
      boolean kmsIsFrom =
        e.getMessage().contains("ReEncryptFrom") ||
        e.getMessage().contains("Decrypt");
      boolean kmsIsTo =
        e.getMessage().contains("ReEncryptTo") ||
        e.getMessage().contains("Encrypt");

      Assert.assertFalse(
        (kmsIsFrom || kmsIsTo),
        "KMS Exception SHOULD have been cast to Mutation Exception. testId: " +
        branchKeyId +
        ". KMS Exception: " +
        e
      );
    }
    if (e.getMessage().contains("branch:version")) {
      Matcher matcher = BRANCH_KEY_TYPE_PATTERN.matcher(e.getMessage());
      if (matcher.find()) {
        String typStr = matcher.group(1).trim();
        // An exception was thrown, let's delete the item
        DdbHelper.reallyDeleteKeyStoreDdbItem(
          branchKeyId,
          typStr,
          Fixtures.TEST_KEYSTORE_NAME,
          3,
          5000,
          Fixtures.ddbClientWest2,
          false
        );
        System.out.println(
          "\nItem: " +
          typStr +
          " \t" +
          e.getClass().getSimpleName() +
          ": " +
          e.getMessage()
        );
      }
    }
  }
}
