package software.amazon.cryptography.example.hierarchy.mutations;

import static software.amazon.cryptography.example.hierarchy.mutations.DescribeMutationExample.Example;
import static software.amazon.cryptography.example.hierarchy.mutations.DescribeMutationExample.InitMutation;

import java.util.Collections;
import org.testng.Assert;
import org.testng.annotations.Test;
import software.amazon.cryptography.example.Fixtures;
import software.amazon.cryptography.example.StorageCheater;
import software.amazon.cryptography.example.hierarchy.CreateKeyExample;
import software.amazon.cryptography.keystore.KeyStorageInterface;
import software.amazon.cryptography.keystoreadmin.model.DescribeMutationOutput;
import software.amazon.cryptography.keystoreadmin.model.MutationToken;
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
    Fixtures.cleanUpBranchKeyId(storage, branchKeyId, true);
  }

  @Test
  public void TestTrustStorageDescription() {
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
    CreateKeyExample.CreateKey(
      Fixtures.TEST_KEYSTORE_NAME,
      Fixtures.TEST_LOGICAL_KEYSTORE_NAME,
      Fixtures.KEYSTORE_KMS_ARN,
      branchKeyId,
      Fixtures.ddbClientWest2
    );
    MutationToken fromInit = InitMutation(
      Fixtures.TEST_KEYSTORE_NAME,
      Fixtures.TEST_LOGICAL_KEYSTORE_NAME,
      Fixtures.POSTAL_HORN_KEY_ARN,
      branchKeyId,
      systemKey,
      Fixtures.ddbClientWest2,
      Fixtures.kmsClientWest2
    );
    DescribeMutationOutput describeRes = Example(
      Fixtures.TEST_KEYSTORE_NAME,
      Fixtures.TEST_LOGICAL_KEYSTORE_NAME,
      branchKeyId,
      Fixtures.ddbClientWest2
    );
    Assert.assertEquals(
      describeRes.MutationInFlight().Yes().MutationDetails().SystemKey(),
      "Trust Storage"
    );
    Fixtures.cleanUpBranchKeyId(storage, branchKeyId, true);
  }

  @Test
  public void TestKmsSymEncDescription() {
    //noinspection unchecked
    SystemKey systemKey = MutationsProvider.KmsSystemKey(
      Fixtures.POSTAL_HORN_KEY_ARN,
      Fixtures.kmsClientWest2,
      Collections.EMPTY_LIST
    );
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
      Fixtures.KEYSTORE_KMS_ARN,
      branchKeyId,
      Fixtures.ddbClientWest2
    );
    MutationToken fromInit = InitMutation(
      Fixtures.TEST_KEYSTORE_NAME,
      Fixtures.TEST_LOGICAL_KEYSTORE_NAME,
      Fixtures.POSTAL_HORN_KEY_ARN,
      branchKeyId,
      systemKey,
      Fixtures.ddbClientWest2,
      Fixtures.kmsClientWest2
    );
    DescribeMutationOutput describeRes = Example(
      Fixtures.TEST_KEYSTORE_NAME,
      Fixtures.TEST_LOGICAL_KEYSTORE_NAME,
      branchKeyId,
      Fixtures.ddbClientWest2
    );
    Assert.assertEquals(
      describeRes.MutationInFlight().Yes().MutationDetails().SystemKey(),
      "KMS Symmetric Encryption"
    );
    Fixtures.cleanUpBranchKeyId(storage, branchKeyId, true);
  }
}
