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
import software.amazon.cryptography.example.Fixtures;
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
import software.amazon.cryptography.keystoreadmin.model.MutationToken;
import software.amazon.cryptography.keystoreadmin.model.Mutations;

public class MutationKmsAccessInFlightTest {

  static final String testPrefix = "mutation-kms-access-in-flight-test-";

  @Test
  public void test() {
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
      POSTAL_HORN_KEY_ARN,
      branchKeyId,
      Fixtures.ddbClientWest2
    );
    KeyManagementStrategy strategyWest2 = AdminProvider.strategy(
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
      .terminalEncryptionContext(terminalEC)
      .terminalKmsArn(MRK_ARN_WEST)
      .build();

    InitializeMutationInput initInput = InitializeMutationInput
      .builder()
      .mutations(mutations)
      .branchKeyIdentifier(branchKeyId)
      .strategy(strategyWest2)
      .build();

    InitializeMutationOutput initOutput = admin.InitializeMutation(initInput);
    MutationToken token = initOutput.mutationToken();
    System.out.println(
      "InitLogs: " +
      branchKeyId +
      " items: \n" +
      AdminProvider.mutatedItemsToString(initOutput.mutatedBranchKeyItems())
    );
    boolean done = false;
    List<KmsException> kmsExceptions = new ArrayList<>();
    boolean isFromThrown = false;
    boolean isToThrown = false;
    int limitLoop = 5;

    while (!done) {
      try {
        limitLoop--;
        if (limitLoop == 0) done = true;
        ApplyMutationInput applyInput = ApplyMutationInput
          .builder()
          .mutationToken(token)
          .pageSize(1)
          .strategy(strategyDenyMrk)
          .build();
        ApplyMutationOutput applyOutput = admin.ApplyMutation(applyInput);
        ApplyMutationResult result = applyOutput.result();
        System.out.println(
          "ApplyLogs: " +
          branchKeyId +
          " items: \n" +
          AdminProvider.mutatedItemsToString(
            applyOutput.mutatedBranchKeyItems()
          )
        );

        if (result.continueMutation() != null) token =
          result.continueMutation();
        if (result.completeMutation() != null) done = true;
      } catch (KmsException accessDenied) {
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
        kmsExceptions.add(accessDenied);
        // An exception was thrown, let's delete the item
        QueryForVersionsOutput versions = storage.QueryForVersions(
          QueryForVersionsInput
            .builder()
            .Identifier(branchKeyId)
            .pageSize(1)
            .build()
        );
        versions
          .items()
          .forEach(item -> {
            String typStr = item.EncryptionContext().get("type");
            Fixtures.deleteKeyStoreDdbItem(
              item.Identifier(),
              typStr,
              Fixtures.TEST_KEYSTORE_NAME,
              Fixtures.ddbClientWest2
            );
            System.out.println(
              "\nItem: " +
              typStr +
              " \tKMS Exception: " +
              accessDenied.getMessage()
            );
          });
      }
    }

    // Clean Up
    Fixtures.cleanUpBranchKeyId(storage, branchKeyId);
    Assert.assertTrue(
      (kmsExceptions.size() == 2),
      "More KMS Exceptions thrown than expected. kmsExceptions: " +
      kmsExceptions
    );
    Assert.assertTrue(isFromThrown, "Apply never verified the new decrypt.");
    Assert.assertTrue(isToThrown, "Apply never mutated the old decrypt.");
  }
}
