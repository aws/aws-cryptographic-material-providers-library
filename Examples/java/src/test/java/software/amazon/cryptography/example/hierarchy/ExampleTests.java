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

  @Test
  public void CreateKeyHv2Test() {
    // Create Branch Key with `hierarchy-version-2` (HV-2)
    final String branchKeyId = CreateKeyHv2Example.CreateKey(
      Fixtures.KEYSTORE_KMS_ARN,
      HierarchyVersion.v2,
      null,
      AdminProvider.admin()
    );

    System.out.println("Create Branch Key for HV-2: " + branchKeyId);

    final KeyStore keyStore = KeyStoreProvider.keyStore(
      Fixtures.KEYSTORE_KMS_ARN
    );

    // Get Branch Key Items
    GetActiveBranchKeyOutput activeOutput = keyStore.GetActiveBranchKey(
      GetActiveBranchKeyInput.builder().branchKeyIdentifier(branchKeyId).build()
    );
    GetBranchKeyVersionOutput decryptOnlyOutput = keyStore.GetBranchKeyVersion(
      GetBranchKeyVersionInput
        .builder()
        .branchKeyIdentifier(branchKeyId)
        .branchKeyVersion(activeOutput.branchKeyMaterials().branchKeyVersion())
        .build()
    );
    GetBeaconKeyOutput beaconOutput = keyStore.GetBeaconKey(
      GetBeaconKeyInput.builder().branchKeyIdentifier(branchKeyId).build()
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

    DdbHelper.DeleteBranchKey(
      branchKeyId,
      Fixtures.TEST_KEYSTORE_NAME,
      HierarchyVersion.v2.toString(),
      null
    );
  }

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
    DdbHelper.DeleteBranchKey(
      branchKeyId,
      Fixtures.TEST_KEYSTORE_NAME,
      "1",
      null
    );
  }
}
