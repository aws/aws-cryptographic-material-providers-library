package software.amazon.cryptography.example.hierarchy.mutations;

import org.testng.annotations.Test;
import software.amazon.cryptography.example.Fixtures;
import software.amazon.cryptography.example.StorageCheater;
import software.amazon.cryptography.example.hierarchy.DescribeMutationExample;
import software.amazon.cryptography.keystore.KeyStorageInterface;
import software.amazon.cryptography.keystoreadmin.model.SystemKey;
import software.amazon.cryptography.keystoreadmin.model.TrustStorage;

public class DescribeMutationTest {

  static final String testPrefix = "mutation-describe-java-test-";

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
    DescribeMutationExample.CompleteExample(
      Fixtures.TEST_KEYSTORE_NAME,
      Fixtures.TEST_LOGICAL_KEYSTORE_NAME,
      Fixtures.KEYSTORE_KMS_ARN,
      Fixtures.POSTAL_HORN_KEY_ARN,
      branchKeyId,
      systemKey,
      Fixtures.ddbClientWest2,
      Fixtures.kmsClientWest2
    );
    Fixtures.cleanUpBranchKeyId(storage, branchKeyId);
  }
}
