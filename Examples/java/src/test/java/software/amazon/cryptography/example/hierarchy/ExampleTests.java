// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
package software.amazon.cryptography.example.hierarchy;

import javax.annotation.Nonnull;
import javax.annotation.Nullable;
import org.testng.Assert;
import org.testng.annotations.Test;
import software.amazon.awssdk.services.dynamodb.model.GetItemResponse;
import software.amazon.cryptography.example.Constants;
import software.amazon.cryptography.example.DdbHelper;
import software.amazon.cryptography.example.Fixtures;
import software.amazon.cryptography.example.hierarchy.mutations.MutationDecryptEncryptExample;
import software.amazon.cryptography.example.hierarchy.mutations.MutationExample;
import software.amazon.cryptography.example.hierarchy.mutations.MutationKmsSimpleExample;
import software.amazon.cryptography.example.hierarchy.mutations.MutationResumeExample;
import software.amazon.cryptography.example.hierarchy.mutations.MutationsProvider;
import software.amazon.cryptography.keystore.KeyStore;
import software.amazon.cryptography.keystore.model.AwsKms;
import software.amazon.cryptography.keystore.model.GetActiveBranchKeyInput;
import software.amazon.cryptography.keystore.model.GetActiveBranchKeyOutput;
import software.amazon.cryptography.keystore.model.GetBeaconKeyInput;
import software.amazon.cryptography.keystore.model.GetBeaconKeyOutput;
import software.amazon.cryptography.keystore.model.GetBranchKeyVersionInput;
import software.amazon.cryptography.keystore.model.GetBranchKeyVersionOutput;
import software.amazon.cryptography.keystore.model.HierarchyVersion;

public class ExampleTests {

  static final String hv2CreateTestPrefix = "create-hierarchy-version-2-java-";

  @Test
  public void createKeyHv2Test() {
    String branchKeyId =
      hv2CreateTestPrefix + java.util.UUID.randomUUID().toString();
    // Create Branch Key with `hierarchy-version-2` (HV-2)
    final String actualBranchKeyId = CreateKeyExample.CreateKey(
      Fixtures.KEYSTORE_KMS_ARN,
      branchKeyId,
      AdminProvider.admin(),
      HierarchyVersion.v2
    );
    final KeyStore keyStore = KeyStoreProvider.keyStore(
      Fixtures.KEYSTORE_KMS_ARN
    );
    // Get Branch Key Items
    GetActiveBranchKeyOutput activeOutput = keyStore.GetActiveBranchKey(
      GetActiveBranchKeyInput
        .builder()
        .branchKeyIdentifier(actualBranchKeyId)
        .build()
    );
    GetBranchKeyVersionOutput decryptOnlyOutput = keyStore.GetBranchKeyVersion(
      GetBranchKeyVersionInput
        .builder()
        .branchKeyIdentifier(actualBranchKeyId)
        .branchKeyVersion(activeOutput.branchKeyMaterials().branchKeyVersion())
        .build()
    );
    GetBeaconKeyOutput beaconOutput = keyStore.GetBeaconKey(
      GetBeaconKeyInput.builder().branchKeyIdentifier(actualBranchKeyId).build()
    );

    assert branchKeyId.equals(
      activeOutput.branchKeyMaterials().branchKeyIdentifier()
    );
    assert branchKeyId.equals(
      decryptOnlyOutput.branchKeyMaterials().branchKeyIdentifier()
    );
    assert activeOutput
      .branchKeyMaterials()
      .branchKeyVersion()
      .equals(decryptOnlyOutput.branchKeyMaterials().branchKeyVersion());
    assert branchKeyId.equals(
      beaconOutput.beaconKeyMaterials().beaconKeyIdentifier()
    );

    DdbHelper.DeleteBranchKey(branchKeyId, Fixtures.TEST_KEYSTORE_NAME, null);
  }

  @Test
  public void end2EndKmsSimpleTest() {
    // Run the test with v1 -> v2 mutation
    end2EndKmsSimpleTestHelper(HierarchyVersion.v1, HierarchyVersion.v2);
  }

  @Test
  public void end2EndKmsReEncryptTest() {
    // Run the test for v1 item mutation
    end2EndKmsReEncryptTestHelper(HierarchyVersion.v1);
  }

  @Test
  public void end2EndDecryptEncryptTest() {
    // Run the test for v1 item mutation
    end2EndDecryptEncryptTestHelper(HierarchyVersion.v1, HierarchyVersion.v2, true);
  }

  /**
   * Parameterized test helper that allows testing different hierarchy version
   * combinations for KMS Simple strategy
   * @param initialHVersion The hierarchy version to use when creating the branch key
   * @param terminalHVersion The hierarchy version to mutate to.
   * terminalHVersion can be null if mutation of HierarchyVersion is not required
   */
  private void end2EndKmsSimpleTestHelper(
    final HierarchyVersion initialHVersion,
    @Nullable final HierarchyVersion terminalHVersion
  ) {
    String branchKeyId = CreateKeyExample.CreateKey(
      Fixtures.KEYSTORE_KMS_ARN,
      null,
      AdminProvider.admin(),
      initialHVersion
    );
    System.out.println("\nCreated Branch Key: " + branchKeyId);
    branchKeyId =
      MutationKmsSimpleExample.End2End(
        branchKeyId,
        Fixtures.POSTAL_HORN_KEY_ARN,
        terminalHVersion,
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
      Constants.TYPE_MUTATION_COMMITMENT,
      Fixtures.TEST_KEYSTORE_NAME,
      Fixtures.ddbClientWest2
    );
    Assert.assertFalse(
      mCommitmentRes.hasItem(),
      Constants.TYPE_MUTATION_COMMITMENT + " was not deleted!"
    );
    GetItemResponse mIndexRes = DdbHelper.getKeyStoreDdbItem(
      branchKeyId,
      Constants.TYPE_MUTATION_INDEX,
      Fixtures.TEST_KEYSTORE_NAME,
      Fixtures.ddbClientWest2
    );
    Assert.assertFalse(
      mIndexRes.hasItem(),
      Constants.TYPE_MUTATION_INDEX + " was not deleted!"
    );
    KeyStore postalHornKS = KeyStoreProvider.keyStore(
      Fixtures.POSTAL_HORN_KEY_ARN
    );
    ValidateKeyStoreItem.ValidateBranchKey(branchKeyId, postalHornKS);

    DdbHelper.DeleteBranchKey(branchKeyId, Fixtures.TEST_KEYSTORE_NAME, null);
  }

  /**
   * Parameterized test helper that allows testing different hierarchy version
   * combinations for Kms ReEncrypt strategy
   * @param initialHVersion The hierarchy version to use when creating the branch key
   *
   * Note: terminalHVersion is not added in the test because hv1 to hv2 is not supported
   */
  private void end2EndKmsReEncryptTestHelper(
    @Nullable final HierarchyVersion initialHVersion
  ) {
    String branchKeyId = CreateKeyExample.CreateKey(
      Fixtures.KEYSTORE_KMS_ARN,
      null,
      AdminProvider.admin(),
      initialHVersion
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
    KeyStore postalHornKS = KeyStoreProvider.keyStore(
      Fixtures.POSTAL_HORN_KEY_ARN
    );
    ValidateKeyStoreItem.ValidateBranchKey(branchKeyId, postalHornKS);
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
      Constants.TYPE_MUTATION_COMMITMENT,
      Fixtures.TEST_KEYSTORE_NAME,
      Fixtures.ddbClientWest2
    );
    Assert.assertFalse(
      mCommitmentRes.hasItem(),
      Constants.TYPE_MUTATION_COMMITMENT + " was not deleted!"
    );
    GetItemResponse mIndexRes = DdbHelper.getKeyStoreDdbItem(
      branchKeyId,
      Constants.TYPE_MUTATION_INDEX,
      Fixtures.TEST_KEYSTORE_NAME,
      Fixtures.ddbClientWest2
    );
    Assert.assertFalse(
      mIndexRes.hasItem(),
      Constants.TYPE_MUTATION_INDEX + " was not deleted!"
    );
    branchKeyId =
      MutationResumeExample.Resume2End(
        branchKeyId,
        Fixtures.KEYSTORE_KMS_ARN,
        null,
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
        Constants.TYPE_MUTATION_COMMITMENT,
        Fixtures.TEST_KEYSTORE_NAME,
        Fixtures.ddbClientWest2
      );
    Assert.assertFalse(
      mCommitmentRes.hasItem(),
      Constants.TYPE_MUTATION_COMMITMENT + " was not deleted!"
    );
    mIndexRes =
      DdbHelper.getKeyStoreDdbItem(
        branchKeyId,
        Constants.TYPE_MUTATION_INDEX,
        Fixtures.TEST_KEYSTORE_NAME,
        Fixtures.ddbClientWest2
      );
    Assert.assertFalse(
      mIndexRes.hasItem(),
      Constants.TYPE_MUTATION_INDEX + " was not deleted!"
    );
    KeyStore keyStoreKS = KeyStoreProvider.keyStore(Fixtures.KEYSTORE_KMS_ARN);
    ValidateKeyStoreItem.ValidateBranchKey(branchKeyId, keyStoreKS);
    DdbHelper.DeleteBranchKey(branchKeyId, Fixtures.TEST_KEYSTORE_NAME, null);
  }

  /**
   * Parameterized test helper that allows testing different hierarchy version
   * combinations for KMS Simple strategy
   * @param initialHVersion The hierarchy version to use when creating the branch key
   * @param terminalHVersion The hierarchy version to mutate to.
   * terminalHVersion can be null if mutation of HierarchyVersion is not required
   */
  private void end2EndDecryptEncryptTestHelper(
    @Nonnull final HierarchyVersion initialHVersion,
    @Nullable final HierarchyVersion terminalHVersion,
    @Nullable final boolean doNotVersion
  ) {
    String branchKeyId = CreateKeyExample.CreateKey(
      Fixtures.KEYSTORE_KMS_ARN,
      null,
      AdminProvider.admin(),
      initialHVersion
    );
    System.out.println("\nCreated Branch Key: " + branchKeyId);
    branchKeyId =
            MutationDecryptEncryptExample.End2End(
                    branchKeyId,
                    Fixtures.POSTAL_HORN_KEY_ARN,
                    AwsKms.builder().kmsClient(Fixtures.keyStoreOnlyKmsClient).build(),
                    AwsKms.builder().kmsClient(Fixtures.postalHornOnlyKmsClient).build(),
                    terminalHVersion,
                    MutationsProvider.KmsSystemKey(),
                    AdminProvider.admin(),
                    doNotVersion
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
      Constants.TYPE_MUTATION_COMMITMENT,
      Fixtures.TEST_KEYSTORE_NAME,
      Fixtures.ddbClientWest2
    );
    Assert.assertFalse(
      mCommitmentRes.hasItem(),
      Constants.TYPE_MUTATION_COMMITMENT + " was not deleted!"
    );
    GetItemResponse mIndexRes = DdbHelper.getKeyStoreDdbItem(
      branchKeyId,
      Constants.TYPE_MUTATION_INDEX,
      Fixtures.TEST_KEYSTORE_NAME,
      Fixtures.ddbClientWest2
    );
    Assert.assertFalse(
      mIndexRes.hasItem(),
      Constants.TYPE_MUTATION_INDEX + " was not deleted!"
    );
    KeyStore postalHornKS = KeyStoreProvider.keyStore(
      Fixtures.POSTAL_HORN_KEY_ARN
    );
    ValidateKeyStoreItem.ValidateBranchKey(branchKeyId, postalHornKS);
    if (doNotVersion == false) {
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
    }
    try {
    branchKeyId =
      MutationResumeExample.Resume2End(
        branchKeyId,
        Fixtures.KEYSTORE_KMS_ARN,
        null,
        AdminProvider.strategy(Fixtures.kmsClientWest2),
        MutationsProvider.TrustStorage(),
        AdminProvider.admin()
      );
    } catch (Exception e) {
      e.printStackTrace(); // This will print the full stack trace
      throw e;
    }

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
        Constants.TYPE_MUTATION_COMMITMENT,
        Fixtures.TEST_KEYSTORE_NAME,
        Fixtures.ddbClientWest2
      );
    Assert.assertFalse(
      mCommitmentRes.hasItem(),
      Constants.TYPE_MUTATION_COMMITMENT + " was not deleted!"
    );
    mIndexRes =
      DdbHelper.getKeyStoreDdbItem(
        branchKeyId,
        Constants.TYPE_MUTATION_INDEX,
        Fixtures.TEST_KEYSTORE_NAME,
        Fixtures.ddbClientWest2
      );
    Assert.assertFalse(
      mIndexRes.hasItem(),
      Constants.TYPE_MUTATION_INDEX + " was not deleted!"
    );
    KeyStore keyStoreKS = KeyStoreProvider.keyStore(Fixtures.KEYSTORE_KMS_ARN);
    ValidateKeyStoreItem.ValidateBranchKey(branchKeyId, keyStoreKS);
    DdbHelper.DeleteBranchKey(branchKeyId, Fixtures.TEST_KEYSTORE_NAME, null);
  }
}
