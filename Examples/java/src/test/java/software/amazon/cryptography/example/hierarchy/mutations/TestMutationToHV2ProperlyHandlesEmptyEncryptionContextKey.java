package software.amazon.cryptography.example.hierarchy.mutations;

import java.util.Collections;
import java.util.HashMap;
import java.util.Map;
import java.util.Objects;
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
import software.amazon.cryptography.keystoreadmin.model.KeyStoreAdminException;

public class TestMutationToHV2ProperlyHandlesEmptyEncryptionContextKey {

  static final String testPrefix =
    "mutation-to-hv-2-properly-handles-empty-encryption-context-key-java-test-";
  private static final Map<String, String> encryptionContext;

  @SuppressWarnings("SpellCheckingInspection")
  private static final String expectedErrorMsgContains =
    "Emptyish Keys: one or more Keys in the Encryption Context are emptyish";

  static {
    // Initial Capacity of 8 b/c we have 8 key-pairs
    // LoadFactor greater than 1 should ensure that we never re-size the hash map
    Map<String, String> _encryptionContext = new HashMap<>(8, 2);
    _encryptionContext.put("\n", "newline");
    _encryptionContext.put("\t", "tab");
    _encryptionContext.put("\r", "carriage-return");
    _encryptionContext.put(" ", "space");
    _encryptionContext.put("", "empty");
    _encryptionContext.put("NormalKey", "Value with\nspecial\rchars\t");
    _encryptionContext.put("\u0007", "bell-unicode");
    _encryptionContext.put("\u0001", "unicode");
    encryptionContext = Collections.unmodifiableMap(_encryptionContext);
  }

  protected String createHV1WithAnEmptyEncryptionContextKey() {
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
      "Test HV-1 Branch Key does not have expected encryption context."
    );
  }

  protected void mutateToHV2(final String branchKeyId) {
    MutationKmsSimpleExample.End2End(
      branchKeyId,
      Fixtures.POSTAL_HORN_KEY_ARN,
      HierarchyVersion.v2,
      MutationsProvider.TrustStorage(),
      AdminProvider.admin()
    );
  }

  @Test
  public void testHV2ProperlyHandlesEmptyEncryptionContextKey()
    throws InterruptedException {
    Throwable caughtException = null;
    final String branchKeyId = createHV1WithAnEmptyEncryptionContextKey();
    Thread.sleep(5000); // DDB eventual consistency
    try {
      checkBranchKey(branchKeyId);
      try {
        mutateToHV2(branchKeyId);
      } catch (KeyStoreAdminException e) {
        caughtException = e;
      }
      Thread.sleep(5000); // DDB eventual consistency
      checkBranchKey(branchKeyId);
    } finally {
      DdbHelper.DeleteBranchKey(branchKeyId, Fixtures.TEST_KEYSTORE_NAME, null);
    }
    Assert.assertTrue(
      Objects.nonNull(caughtException),
      "Exception was expected"
    );
    // TODO-HV-2-FOLLOW : Create unique errors for Emptyish vs Out of Bound Modification
    Assert.assertTrue(
      caughtException.getMessage().contains(expectedErrorMsgContains),
      "Error Message did not contain expected content. Expected message to contain: " +
      expectedErrorMsgContains +
      "\n but the message was: " +
      caughtException.getMessage()
    );
  }
}
