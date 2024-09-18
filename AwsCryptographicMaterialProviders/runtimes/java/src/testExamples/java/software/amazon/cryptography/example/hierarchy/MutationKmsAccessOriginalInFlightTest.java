// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
package software.amazon.cryptography.example.hierarchy;

import static software.amazon.cryptography.example.Fixtures.MRK_ARN_WEST;
import static software.amazon.cryptography.example.Fixtures.POSTAL_HORN_KEY_ARN;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import org.testng.Assert;
import org.testng.annotations.Test;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.kms.KmsClient;
import software.amazon.awssdk.services.kms.model.KmsException;
import software.amazon.cryptography.example.CredentialUtils;
import software.amazon.cryptography.example.DdbHelper;
import software.amazon.cryptography.example.Fixtures;
import software.amazon.cryptography.example.StorageCheater;
import software.amazon.cryptography.keystore.KeyStorageInterface;
import software.amazon.cryptography.keystore.model.QueryForVersionsInput;
import software.amazon.cryptography.keystore.model.QueryForVersionsOutput;
import software.amazon.cryptography.keystoreadmin.KeyStoreAdmin;
import software.amazon.cryptography.keystoreadmin.model.ApplyMutationInput;
import software.amazon.cryptography.keystoreadmin.model.ApplyMutationOutput;
import software.amazon.cryptography.keystoreadmin.model.ApplyMutationResult;
import software.amazon.cryptography.keystoreadmin.model.InitializeMutationInput;
import software.amazon.cryptography.keystoreadmin.model.InitializeMutationOutput;
import software.amazon.cryptography.keystoreadmin.model.KeyManagementStrategy;
import software.amazon.cryptography.keystoreadmin.model.KeyStoreAdminException;
import software.amazon.cryptography.keystoreadmin.model.MutationFromException;
import software.amazon.cryptography.keystoreadmin.model.MutationToException;
import software.amazon.cryptography.keystoreadmin.model.MutationToken;
import software.amazon.cryptography.keystoreadmin.model.Mutations;
import software.amazon.cryptography.keystoreadmin.model.SystemKey;
import software.amazon.cryptography.keystoreadmin.model.TrustStorage;

public class MutationKmsAccessOriginalInFlightTest {

  static final String testPrefix =
    "mutation-kms-access-in-flight-original-test-";

  @Test
  public void test() {
    SystemKey systemKey = SystemKey
      .builder()
      .trustStorage(TrustStorage.builder().build())
      .build();
    KeyStorageInterface storage = StorageCheater.create(
      Fixtures.ddbClientWest2,
      Fixtures.TEST_KEYSTORE_NAME,
      Fixtures.TEST_LOGICAL_KEYSTORE_NAME
    );
    final String branchKeyId =
      testPrefix + java.util.UUID.randomUUID().toString();
    CreateKeyExample.CreateKey(
      Fixtures.TEST_KEYSTORE_NAME,
      Fixtures.TEST_LOGICAL_KEYSTORE_NAME,
      MRK_ARN_WEST,
      branchKeyId,
      Fixtures.ddbClientWest2
    );
    KeyManagementStrategy strategyAll = AdminProvider.strategy(
      Fixtures.kmsClientWest2
    );
    KmsClient denyMrk = KmsClient
      .builder()
      .credentialsProvider(
        CredentialUtils.credsForRole(
          Fixtures.LIMITED_KMS_ACCESS_IAM_ROLE,
          "java-mpl-examples",
          Region.US_WEST_2,
          Fixtures.httpClient,
          Fixtures.defaultCreds
        )
      )
      .region(Region.US_WEST_2)
      .httpClient(Fixtures.httpClient)
      .build();

    KeyManagementStrategy strategyDenyMrk = AdminProvider.strategy(denyMrk);
    KeyStoreAdmin admin = AdminProvider.admin(
      Fixtures.TEST_KEYSTORE_NAME,
      Fixtures.TEST_LOGICAL_KEYSTORE_NAME,
      Fixtures.ddbClientWest2
    );

    System.out.println("BranchKey ID to mutate: " + branchKeyId);
    HashMap<String, String> terminalEC = new HashMap<>();
    terminalEC.put("Robbie", "is a dog.");

    Mutations mutations = Mutations
      .builder()
      .TerminalEncryptionContext(terminalEC)
      .TerminalKmsArn(POSTAL_HORN_KEY_ARN)
      .build();

    InitializeMutationInput initInput = InitializeMutationInput
      .builder()
      .Mutations(mutations)
      .Identifier(branchKeyId)
      .Strategy(strategyAll)
      .SystemKey(systemKey)
      .build();

    InitializeMutationOutput initOutput = admin.InitializeMutation(initInput);
    MutationToken token = initOutput.MutationToken();
    System.out.println(
      "InitLogs: " +
      branchKeyId +
      " items: \n" +
      AdminProvider.mutatedItemsToString(initOutput.MutatedBranchKeyItems())
    );
    boolean done = false;
    List<Exception> exceptions = new ArrayList<>();
    boolean isFromThrown = false;
    boolean isToThrown = false;
    boolean verifyTerminalThrown = false;
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
          AdminProvider.mutatedItemsToString(
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
          boolean isTo =
            ((MutationToException) accessDenied).getMessage()
              .contains("while verifying a Version with terminal properities");
          verifyTerminalThrown = verifyTerminalThrown || isTo;
        }
        if (accessDenied instanceof MutationFromException) {
          boolean isFrom =
            ((MutationFromException) accessDenied).getMessage()
              .contains("while verifying a Version with terminal properities");
          verifyTerminalThrown = verifyTerminalThrown || isFrom;
        }
        if (accessDenied instanceof KmsException) {
          boolean isFrom = accessDenied.getMessage().contains("ReEncryptFrom");
          isFromThrown = isFromThrown || isFrom;
          boolean isTo = accessDenied.getMessage().contains("ReEncryptTo");
          isToThrown = isToThrown || isTo;
          Assert.assertTrue(
            (isTo || isFrom),
            "KMS Exception does not meet expectations. testId: " +
            branchKeyId +
            ". KMS Exception: " +
            accessDenied
          );
        }
        exceptions.add(accessDenied);
        // An exception was thrown, let's delete the item
        QueryForVersionsOutput versions = storage.QueryForVersions(
          QueryForVersionsInput
            .builder()
            .Identifier(branchKeyId)
            .PageSize(1)
            .build()
        );
        versions
          .Items()
          .forEach(item -> {
            String typStr = item.EncryptionContext().get("type");
            DdbHelper.deleteKeyStoreDdbItem(
              item.Identifier(),
              typStr,
              Fixtures.TEST_KEYSTORE_NAME,
              Fixtures.ddbClientWest2
            );
            System.out.println(
              "\nItem: " +
              typStr +
              " \t" +
              accessDenied.getClass().getSimpleName() +
              ": " +
              accessDenied.getMessage()
            );
          });
      }
    }

    // Clean Up
    Fixtures.cleanUpBranchKeyId(storage, branchKeyId);
    Assert.assertTrue(
      (exceptions.size() == 1),
      "Incorrect number of exceptions thrown than expected. Exceptions: " + exceptions
    );
    Assert.assertTrue(
      isFromThrown,
      "Apply never failed to read the old."
    );
  }
}
