package software.amazon.cryptography.example.hierarchy.mutations;

import org.testng.annotations.Test;
import software.amazon.cryptography.example.Fixtures;
import software.amazon.cryptography.example.hierarchy.CreateKeyExample;

public class TestMutationSystemKeyKMSExample {

  static final String testPrefix = "java-test-mutation-system-key-kms-example-";

  @Test
  public void test() {
    final String branchKeyId =
      testPrefix + java.util.UUID.randomUUID().toString();
    CreateKeyExample.CreateKey(Fixtures.MRK_ARN_WEST, branchKeyId, null);
    MutationSystemKeyKMSExample.End2End(
      Fixtures.POSTAL_HORN_KEY_ARN,
      branchKeyId,
      Fixtures.KEYSTORE_KMS_ARN
    );
    Fixtures.DeleteBranchKey(
      branchKeyId,
      Fixtures.TEST_KEYSTORE_NAME,
      "1",
      null
    );
  }
}
