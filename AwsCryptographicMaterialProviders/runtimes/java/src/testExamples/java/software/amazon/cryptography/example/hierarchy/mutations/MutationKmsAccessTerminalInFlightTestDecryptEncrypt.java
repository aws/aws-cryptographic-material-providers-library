package software.amazon.cryptography.example.hierarchy.mutations;

import static software.amazon.cryptography.example.Fixtures.MRK_ARN_WEST;
import static software.amazon.cryptography.example.Fixtures.POSTAL_HORN_KEY_ARN;
import static software.amazon.cryptography.example.hierarchy.mutations.MutationKmsAccessTerminalInFlightTest.matchBranchKeyType;
import static software.amazon.cryptography.example.hierarchy.mutations.MutationKmsAccessTerminalInFlightTest.testPrefix;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.regex.Matcher;
import java.util.stream.Collectors;
import org.testng.Assert;
import org.testng.annotations.Test;
import software.amazon.awssdk.services.kms.model.KmsException;
import software.amazon.cryptography.example.DdbHelper;
import software.amazon.cryptography.example.Fixtures;
import software.amazon.cryptography.example.hierarchy.AdminProvider;
import software.amazon.cryptography.example.hierarchy.CreateKeyExample;
import software.amazon.cryptography.keystoreadmin.KeyStoreAdmin;
import software.amazon.cryptography.keystoreadmin.model.ApplyMutationInput;
import software.amazon.cryptography.keystoreadmin.model.ApplyMutationOutput;
import software.amazon.cryptography.keystoreadmin.model.ApplyMutationResult;
import software.amazon.cryptography.keystoreadmin.model.InitializeMutationInput;
import software.amazon.cryptography.keystoreadmin.model.InitializeMutationOutput;
import software.amazon.cryptography.keystoreadmin.model.KeyManagementStrategy;
import software.amazon.cryptography.keystoreadmin.model.KeyStoreAdminException;
import software.amazon.cryptography.keystoreadmin.model.KmsSymmetricKeyArn;
import software.amazon.cryptography.keystoreadmin.model.MutationFromException;
import software.amazon.cryptography.keystoreadmin.model.MutationToException;
import software.amazon.cryptography.keystoreadmin.model.MutationToken;
import software.amazon.cryptography.keystoreadmin.model.Mutations;
import software.amazon.cryptography.keystoreadmin.model.SystemKey;
import software.amazon.cryptography.keystoreadmin.model.TrustStorage;

public class MutationKmsAccessTerminalInFlightTestDecryptEncrypt {

  @Test
  public void test() {
    SystemKey systemKey = SystemKey
      .builder()
      .trustStorage(TrustStorage.builder().build())
      .build();
    KeyStoreAdmin admin = AdminProvider.admin();
    final String branchKeyId =
      testPrefix + java.util.UUID.randomUUID().toString();
    CreateKeyExample.CreateKey(POSTAL_HORN_KEY_ARN, branchKeyId, admin);
    KeyManagementStrategy strategyWest2 = AdminProvider.decryptEncryptStrategy(
      Fixtures.kmsClientWest2,
      Fixtures.kmsClientWest2
    );
    KeyManagementStrategy strategyDenyMrk =
      AdminProvider.decryptEncryptStrategy(
        Fixtures.denyMrkKmsClient,
        Fixtures.denyMrkKmsClient
      );
    System.out.println("BranchKey ID to mutate: " + branchKeyId);
    HashMap<String, String> terminalEC = new HashMap<>(2, 1);
    terminalEC.put("Koda", "is a dog.");

    Mutations mutations = Mutations
      .builder()
      .TerminalEncryptionContext(terminalEC)
      .TerminalKmsArn(MRK_ARN_WEST)
      .build();

    InitializeMutationInput initInput = InitializeMutationInput
      .builder()
      .Mutations(mutations)
      .Identifier(branchKeyId)
      .Strategy(strategyWest2)
      .SystemKey(systemKey)
      .build();

    InitializeMutationOutput initOutput = admin.InitializeMutation(initInput);
    MutationToken token = initOutput.MutationToken();
    System.out.println(
      "InitLogs: " +
      branchKeyId +
      " items: \n" +
      MutationsProvider.mutatedItemsToString(initOutput.MutatedBranchKeyItems())
    );

    boolean done = false;
    List<Exception> exceptions = new ArrayList<>();
    boolean isFromThrown = false;
    boolean isToThrown = false;
    int limitLoop = 5;

    while (!done) {
      try {
        limitLoop--;
        if (limitLoop == 0) done = true;
        ApplyMutationInput applyInput = ApplyMutationInput
          .builder()
          .MutationToken(token)
          .PageSize(1)
          .Strategy(strategyDenyMrk)
          .SystemKey(systemKey)
          .build();
        ApplyMutationOutput applyOutput = admin.ApplyMutation(applyInput);
        ApplyMutationResult result = applyOutput.MutationResult();
        System.out.println(
          "ApplyLogs: " +
          branchKeyId +
          " items: \n" +
          MutationsProvider.mutatedItemsToString(
            applyOutput.MutatedBranchKeyItems()
          )
        );

        if (result.ContinueMutation() != null) {
          token = result.ContinueMutation();
        }
        if (result.CompleteMutation() != null) {
          done = true;
        }
      } catch (
        KmsException
        | MutationFromException
        | MutationToException
        | KeyStoreAdminException accessDenied
      ) {
        if (accessDenied instanceof MutationToException) {
          isToThrown = true;
        }
        if (accessDenied instanceof MutationFromException) {
          isFromThrown = true;
        }
        if (accessDenied instanceof KmsException) {
          boolean kmsIsFrom = accessDenied.getMessage().contains("Decrypt");
          boolean kmsIsTo = accessDenied.getMessage().contains("Encrypt");
          Assert.assertFalse(
            (kmsIsFrom || kmsIsTo),
            "KMS Exception SHOULD have been cast to Mutation Exception. testId: " +
            branchKeyId +
            ". KMS Exception: " +
            accessDenied
          );
        }
        // An exception was thrown, let's delete the item
        if (accessDenied.getMessage().contains("branch:version")) {
          Matcher matcher = matchBranchKeyType.matcher(
            accessDenied.getMessage()
          );
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
              accessDenied.getClass().getSimpleName() +
              ": " +
              accessDenied.getMessage()
            );
          }
        }
        exceptions.add(accessDenied);
      }
    }

    // Clean Up
    DdbHelper.DeleteBranchKey(
      branchKeyId,
      Fixtures.TEST_KEYSTORE_NAME,
      "1",
      null
    );
    Assert.assertTrue(
      (exceptions.size() == 2),
      "Only two exceptions should have been thrown. But got " +
      exceptions.size() +
      ". Exceptions:\n" +
      exceptions
        .stream()
        .map(Throwable::toString)
        .collect(Collectors.joining("\n"))
    );
    Assert.assertTrue(isToThrown, "MutationToException MUST be thrown.");
    Assert.assertFalse(
      isFromThrown,
      "MutationFromException should never be thrown."
    );
  }
}
