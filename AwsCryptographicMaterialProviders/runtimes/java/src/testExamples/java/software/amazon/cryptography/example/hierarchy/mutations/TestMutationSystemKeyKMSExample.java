package software.amazon.cryptography.example.hierarchy.mutations;

import org.testng.annotations.Test;
import software.amazon.cryptography.example.Fixtures;
import software.amazon.cryptography.example.hierarchy.CreateKeyExample;
import software.amazon.cryptography.example.hierarchy.StorageExample;
import software.amazon.cryptography.keystore.KeyStorageInterface;

public class TestMutationSystemKeyKMSExample {

  static final String testPrefix = "java-test-mutation-system-key-kms-example-";

  @Test
  public void test() {
    final String branchKeyId =
      testPrefix + java.util.UUID.randomUUID().toString();
    CreateKeyExample.CreateKey(
      Fixtures.TEST_KEYSTORE_NAME,
      Fixtures.TEST_LOGICAL_KEYSTORE_NAME,
      Fixtures.MRK_ARN_WEST,
      branchKeyId,
      Fixtures.ddbClientWest2
    );
    MutationSystemKeyKMSExample.End2End(
      Fixtures.POSTAL_HORN_KEY_ARN,
      branchKeyId,
      Fixtures.KEYSTORE_KMS_ARN
    );
    KeyStorageInterface storage = StorageExample.create(
      Fixtures.ddbClientWest2,
      Fixtures.TEST_KEYSTORE_NAME,
      Fixtures.TEST_LOGICAL_KEYSTORE_NAME
    );
    Fixtures.cleanUpBranchKeyId(storage, branchKeyId, false);
  }
}
