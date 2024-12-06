// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
package software.amazon.cryptography.example.hierarchy;

import org.testng.Assert;
import org.testng.annotations.Test;
import software.amazon.awssdk.services.dynamodb.model.GetItemResponse;
import software.amazon.cryptography.example.Constants;
import software.amazon.cryptography.example.DdbHelper;
import software.amazon.cryptography.example.Fixtures;
import software.amazon.cryptography.example.hierarchy.mutations.MutationDecryptEncryptExample;
import software.amazon.cryptography.example.hierarchy.mutations.MutationExample;
import software.amazon.cryptography.example.hierarchy.mutations.MutationResumeExample;
import software.amazon.cryptography.example.hierarchy.mutations.MutationsProvider;
import software.amazon.cryptography.keystore.model.AwsKms;

public class ExampleTests {

  @Test
  public void End2EndReEncryptTest() {
    String branchKeyId = CreateKeyExample.CreateKey(
      Fixtures.KEYSTORE_KMS_ARN,
      null,
      AdminProvider.admin()
    );
    System.out.println("\nCreated Branch Key: " + branchKeyId);
    branchKeyId =
      MutationExample.End2End(
        Fixtures.POSTAL_HORN_KEY_ARN,
        branchKeyId,
        MutationsProvider.TrustStorage(),
        AdminProvider.admin()
      );
    System.out.println(
      "\nMutated Branch Key: " +
      branchKeyId +
      " to KMS ARN: " +
      Fixtures.POSTAL_HORN_KEY_ARN +
      "\n"
    );
    branchKeyId =
      VersionKeyExample.VersionKey(
        Fixtures.POSTAL_HORN_KEY_ARN,
        branchKeyId,
        AdminProvider.admin()
      );
    branchKeyId =
      VersionKeyExample.VersionKey(
        Fixtures.POSTAL_HORN_KEY_ARN,
        branchKeyId,
        AdminProvider.admin()
      );
    System.out.println("\nVersioned Branch Key: " + branchKeyId + "\n");
    GetItemResponse mCommitmentRes = DdbHelper.getKeyStoreDdbItem(
      branchKeyId,
      Constants.MUTATION_COMMITMENT,
      Fixtures.TEST_KEYSTORE_NAME,
      Fixtures.ddbClientWest2
    );
    Assert.assertFalse(
      mCommitmentRes.hasItem(),
      Constants.MUTATION_COMMITMENT + " was not deleted!"
    );
    GetItemResponse mIndexRes = DdbHelper.getKeyStoreDdbItem(
      branchKeyId,
      Constants.MUTATION_INDEX,
      Fixtures.TEST_KEYSTORE_NAME,
      Fixtures.ddbClientWest2
    );
    Assert.assertFalse(
      mIndexRes.hasItem(),
      Constants.MUTATION_INDEX + " was not deleted!"
    );
    branchKeyId =
      MutationResumeExample.Resume2End(
        branchKeyId,
        Fixtures.KEYSTORE_KMS_ARN,
        AdminProvider.strategy(Fixtures.kmsClientWest2),
        MutationsProvider.TrustStorage(),
        AdminProvider.admin()
      );
    System.out.println(
      "\nMutated Branch Key with Resume: " +
      branchKeyId +
      " to KMS ARN: " +
      Fixtures.KEYSTORE_KMS_ARN +
      "\n"
    );
    mCommitmentRes =
      DdbHelper.getKeyStoreDdbItem(
        branchKeyId,
        Constants.MUTATION_COMMITMENT,
        Fixtures.TEST_KEYSTORE_NAME,
        Fixtures.ddbClientWest2
      );
    Assert.assertFalse(
      mCommitmentRes.hasItem(),
      Constants.MUTATION_COMMITMENT + " was not deleted!"
    );
    mIndexRes =
      DdbHelper.getKeyStoreDdbItem(
        branchKeyId,
        Constants.MUTATION_INDEX,
        Fixtures.TEST_KEYSTORE_NAME,
        Fixtures.ddbClientWest2
      );
    Assert.assertFalse(
      mIndexRes.hasItem(),
      Constants.MUTATION_INDEX + " was not deleted!"
    );
    DdbHelper.DeleteBranchKey(
      branchKeyId,
      Fixtures.TEST_KEYSTORE_NAME,
      "1",
      null
    );
  }

  @Test
  public void End2EndDecryptEncryptTest() {
    String branchKeyId = CreateKeyExample.CreateKey(
      Fixtures.KEYSTORE_KMS_ARN,
      null,
      AdminProvider.admin()
    );
    System.out.println("\nCreated Branch Key: " + branchKeyId);
    branchKeyId =
      MutationDecryptEncryptExample.End2End(
        branchKeyId,
        Fixtures.POSTAL_HORN_KEY_ARN,
        AwsKms.builder().kmsClient(Fixtures.keyStoreOnlyKmsClient).build(),
        AwsKms.builder().kmsClient(Fixtures.postalHornOnlyKmsClient).build(),
        MutationsProvider.KmsSystemKey(),
        AdminProvider.admin()
      );
    System.out.println(
      "\nMutated Branch Key: " +
      branchKeyId +
      " to KMS ARN: " +
      Fixtures.POSTAL_HORN_KEY_ARN +
      "\n"
    );
    GetItemResponse mCommitmentRes = DdbHelper.getKeyStoreDdbItem(
      branchKeyId,
      Constants.MUTATION_COMMITMENT,
      Fixtures.TEST_KEYSTORE_NAME,
      Fixtures.ddbClientWest2
    );
    Assert.assertFalse(
      mCommitmentRes.hasItem(),
      Constants.MUTATION_COMMITMENT + " was not deleted!"
    );
    GetItemResponse mIndexRes = DdbHelper.getKeyStoreDdbItem(
      branchKeyId,
      Constants.MUTATION_INDEX,
      Fixtures.TEST_KEYSTORE_NAME,
      Fixtures.ddbClientWest2
    );
    Assert.assertFalse(
      mIndexRes.hasItem(),
      Constants.MUTATION_INDEX + " was not deleted!"
    );
    branchKeyId =
      VersionKeyExample.VersionKey(
        Fixtures.POSTAL_HORN_KEY_ARN,
        branchKeyId,
        AdminProvider.admin()
      );
    branchKeyId =
      VersionKeyExample.VersionKey(
        Fixtures.POSTAL_HORN_KEY_ARN,
        branchKeyId,
        AdminProvider.admin()
      );
    System.out.println("\nVersioned Branch Key: " + branchKeyId + "\n");
    branchKeyId =
      MutationResumeExample.Resume2End(
        branchKeyId,
        Fixtures.KEYSTORE_KMS_ARN,
        AdminProvider.strategy(Fixtures.kmsClientWest2),
        MutationsProvider.TrustStorage(),
        AdminProvider.admin()
      );
    System.out.println(
      "\nMutated Branch Key with Resume: " +
      branchKeyId +
      " to KMS ARN: " +
      Fixtures.KEYSTORE_KMS_ARN +
      "\n"
    );
    mCommitmentRes =
      DdbHelper.getKeyStoreDdbItem(
        branchKeyId,
        Constants.MUTATION_COMMITMENT,
        Fixtures.TEST_KEYSTORE_NAME,
        Fixtures.ddbClientWest2
      );
    Assert.assertFalse(
      mCommitmentRes.hasItem(),
      Constants.MUTATION_COMMITMENT + " was not deleted!"
    );
    mIndexRes =
      DdbHelper.getKeyStoreDdbItem(
        branchKeyId,
        Constants.MUTATION_INDEX,
        Fixtures.TEST_KEYSTORE_NAME,
        Fixtures.ddbClientWest2
      );
    Assert.assertFalse(
      mIndexRes.hasItem(),
      Constants.MUTATION_INDEX + " was not deleted!"
    );
    DdbHelper.DeleteBranchKey(
      branchKeyId,
      Fixtures.TEST_KEYSTORE_NAME,
      "1",
      null
    );
  }
}
