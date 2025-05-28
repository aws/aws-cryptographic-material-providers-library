// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
package software.amazon.cryptography.example.hierarchy.mutations;

import static software.amazon.cryptography.example.Constants.DEFAULT_ENCRYPTION_CONTEXT;

import java.util.Collections;
import java.util.HashMap;
import java.util.Map;
import java.util.UUID;
import org.testng.Assert;
import org.testng.annotations.Test;
import software.amazon.cryptography.example.DdbHelper;
import software.amazon.cryptography.example.Fixtures;
import software.amazon.cryptography.example.hierarchy.AdminProvider;
import software.amazon.cryptography.example.hierarchy.CreateKeyExample;
import software.amazon.cryptography.example.hierarchy.KeyStoreProvider;
import software.amazon.cryptography.keystore.KeyStore;
import software.amazon.cryptography.keystore.model.GetActiveBranchKeyInput;
import software.amazon.cryptography.keystore.model.GetActiveBranchKeyOutput;
import software.amazon.cryptography.keystore.model.HierarchyVersion;

public class TestMutationsWithEscapeCharactersInEC {

  static final String testPrefix =
    "mutations-with-escape-characters-in-ec-java-test-";
  private static final Map<String, String> encryptionContext;

  static {
    Map<String, String> _encryptionContext = new HashMap<>(
      DEFAULT_ENCRYPTION_CONTEXT
    );
    _encryptionContext.put("\n\n\u0007", "escape-characters-plus-bell");
    encryptionContext = Collections.unmodifiableMap(_encryptionContext);
  }

  protected String createHV1WithEscapeCharactersInEC() {
    final String testBranchKeyId = testPrefix + UUID.randomUUID().toString();
    CreateKeyExample.CreateKey(
      Fixtures.KEYSTORE_KMS_ARN,
      testBranchKeyId,
      AdminProvider.admin(),
      HierarchyVersion.v1,
      encryptionContext
    );
    return testBranchKeyId;
  }

  protected void checkBranchKey(final String branchKeyId) {
    KeyStore discoveryKeyStore = KeyStoreProvider.keyStore(null);
    GetActiveBranchKeyOutput getActiveBranchKeyOutput =
      discoveryKeyStore.GetActiveBranchKey(
        GetActiveBranchKeyInput
          .builder()
          .branchKeyIdentifier(branchKeyId)
          .build()
      );
    Assert.assertEquals(
      getActiveBranchKeyOutput.branchKeyMaterials().encryptionContext(),
      encryptionContext,
      "Test Branch Key does not have expected encryption context."
    );
  }

  protected void mutateToHV2(final String branchKeyId) {
    MutationKmsSimpleExample.End2End(
      branchKeyId,
      Fixtures.POSTAL_HORN_KEY_ARN,
      HierarchyVersion.v2,
      encryptionContext,
      MutationsProvider.KmsSystemKey(),
      AdminProvider.admin()
    );
  }

  @Test
  public void testMutationsWithEscapeCharactersInEC()
    throws InterruptedException {
    final String branchKeyId = createHV1WithEscapeCharactersInEC();
    Thread.sleep(5000); // DDB eventual consistency
    try {
      checkBranchKey(branchKeyId);
      mutateToHV2(branchKeyId);
      Thread.sleep(5000); // DDB eventual consistency
      checkBranchKey(branchKeyId);
    } finally {
      DdbHelper.DeleteBranchKey(branchKeyId, Fixtures.TEST_KEYSTORE_NAME, null);
    }
  }
}
