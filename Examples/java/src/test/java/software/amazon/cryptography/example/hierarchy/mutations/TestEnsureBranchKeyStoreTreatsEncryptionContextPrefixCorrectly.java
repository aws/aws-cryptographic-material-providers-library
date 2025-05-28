// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
package software.amazon.cryptography.example.hierarchy.mutations;

import static software.amazon.cryptography.example.Constants.DEFAULT_ENCRYPTION_CONTEXT;

import java.util.UUID;
import org.testng.Assert;
import org.testng.annotations.Test;
import software.amazon.awssdk.services.kms.KmsClient;
import software.amazon.awssdk.services.kms.model.KmsException;
import software.amazon.cryptography.example.DdbHelper;
import software.amazon.cryptography.example.Fixtures;
import software.amazon.cryptography.example.hierarchy.AdminProvider;
import software.amazon.cryptography.example.hierarchy.CreateKeyExample;
import software.amazon.cryptography.example.hierarchy.KeyStoreProvider;
import software.amazon.cryptography.keystore.KeyStore;
import software.amazon.cryptography.keystore.model.GetActiveBranchKeyInput;
import software.amazon.cryptography.keystore.model.GetActiveBranchKeyOutput;
import software.amazon.cryptography.keystore.model.HierarchyVersion;

public class TestEnsureBranchKeyStoreTreatsEncryptionContextPrefixCorrectly {

  static final String testPrefix =
    "ensure-branch-key-store-treats-ec-prefix-correctly-java-test-";

  protected String createHV1() {
    final String testBranchKeyId = testPrefix + UUID.randomUUID().toString();
    CreateKeyExample.CreateKey(
      Fixtures.KEYSTORE_KMS_ARN,
      testBranchKeyId,
      AdminProvider.admin(),
      HierarchyVersion.v1,
      DEFAULT_ENCRYPTION_CONTEXT
    );
    return testBranchKeyId;
  }

  protected void checkBranchKey(final String branchKeyId, KmsClient kmsClient) {
    KeyStore discoveryKeyStore = KeyStoreProvider.keyStore(null, kmsClient);
    GetActiveBranchKeyOutput getActiveBranchKeyOutput =
      discoveryKeyStore.GetActiveBranchKey(
        GetActiveBranchKeyInput
          .builder()
          .branchKeyIdentifier(branchKeyId)
          .build()
      );
    Assert.assertEquals(
      getActiveBranchKeyOutput.branchKeyMaterials().encryptionContext(),
      DEFAULT_ENCRYPTION_CONTEXT,
      "Test Branch Key does not have expected encryption context."
    );
  }

  protected void mutateToHV2(final String branchKeyId) {
    MutationKmsSimpleExample.End2End(
      branchKeyId,
      Fixtures.POSTAL_HORN_KEY_ARN,
      HierarchyVersion.v2,
      DEFAULT_ENCRYPTION_CONTEXT,
      MutationsProvider.KmsSystemKey(),
      AdminProvider.admin()
    );
  }

  @Test
  public void testEnsureBranchKeyStoreTreatsEncryptionContextPrefixCorrectly()
    throws InterruptedException {
    final String branchKeyId = createHV1();
    Thread.sleep(5000); // DDB eventual consistency
    try {
      // The IAM Role associated with "prefixedRobbiePresent" requires that "aws-crypto-ec:Robbie": "Is a Dog." is present
      checkBranchKey(branchKeyId, Fixtures.prefixedRobbiePresent);
      // The IAM Role associated with "defixedRobbieOnly" requires that the Encryption Context ONLY be "Robbie": "Is a Dog."
      Assert.assertThrows(
        KmsException.class,
        () -> checkBranchKey(branchKeyId, Fixtures.defixedRobbieOnly)
      );
      mutateToHV2(branchKeyId);
      Thread.sleep(5000); // DDB eventual consistency
      checkBranchKey(branchKeyId, Fixtures.defixedRobbieOnly);
      Assert.assertThrows(
        KmsException.class,
        () -> checkBranchKey(branchKeyId, Fixtures.prefixedRobbiePresent)
      );
    } finally {
      DdbHelper.DeleteBranchKey(branchKeyId, Fixtures.TEST_KEYSTORE_NAME, null);
    }
  }
}
