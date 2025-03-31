package software.amazon.cryptography.example.hierarchy.mutations;

import static software.amazon.cryptography.example.hierarchy.mutations.DescribeMutationExample.Example;
import static software.amazon.cryptography.example.hierarchy.mutations.DescribeMutationExample.InitMutation;

import java.util.Collections;
import org.testng.Assert;
import org.testng.annotations.Test;
import software.amazon.cryptography.example.DdbHelper;
import software.amazon.cryptography.example.Fixtures;
import software.amazon.cryptography.example.hierarchy.CreateKeyExample;
import software.amazon.cryptography.keystoreadmin.model.DescribeMutationOutput;
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
    final String branchKeyId =
      testPrefix + java.util.UUID.randomUUID().toString();
    DescribeMutationExample.CompleteExample(
      Fixtures.KEYSTORE_KMS_ARN,
      Fixtures.POSTAL_HORN_KEY_ARN,
      branchKeyId,
      systemKey,
      null,
      null
    );
    DdbHelper.DeleteBranchKey(
      branchKeyId,
      Fixtures.TEST_KEYSTORE_NAME,
      "1",
      null
    );
  }

  @Test
  public void TestTrustStorageDescription() {
    SystemKey systemKey = SystemKey
      .builder()
      .trustStorage(TrustStorage.builder().build())
      .build();
    final String branchKeyId =
      testPrefix + java.util.UUID.randomUUID().toString();
    CreateKeyExample.CreateKey(Fixtures.KEYSTORE_KMS_ARN, branchKeyId, null);
    InitMutation(
      branchKeyId,
      Fixtures.POSTAL_HORN_KEY_ARN,
      systemKey,
      null,
      null
    );
    DescribeMutationOutput describeRes = Example(branchKeyId, null);
    Assert.assertTrue(
      describeRes != null &&
      describeRes.MutationInFlight() != null &&
      describeRes.MutationInFlight().Yes() != null,
      "No Mutation In-flight or Describe Mutation failed."
    );
    Assert.assertEquals(
      describeRes.MutationInFlight().Yes().MutationDetails().SystemKey(),
      "Trust Storage"
    );
    DdbHelper.DeleteBranchKey(
      branchKeyId,
      Fixtures.TEST_KEYSTORE_NAME,
      "1",
      null
    );
  }

  @Test
  public void TestKmsSymEncDescription() {
    //noinspection unchecked
    SystemKey systemKey = MutationsProvider.KmsSystemKey(
      Fixtures.KSA_SYSTEM_KEY,
      Fixtures.kmsClientWest2,
      Collections.EMPTY_LIST
    );
    final String branchKeyId =
      testPrefix + java.util.UUID.randomUUID().toString();
    CreateKeyExample.CreateKey(Fixtures.KEYSTORE_KMS_ARN, branchKeyId, null);
    InitMutation(
      branchKeyId,
      Fixtures.POSTAL_HORN_KEY_ARN,
      systemKey,
      null,
      null
    );
    DescribeMutationOutput describeRes = Example(branchKeyId, null);
    Assert.assertTrue(
      describeRes != null &&
      describeRes.MutationInFlight() != null &&
      describeRes.MutationInFlight().Yes() != null,
      "No Mutation In-flight or Describe Mutation failed."
    );
    Assert.assertEquals(
      describeRes.MutationInFlight().Yes().MutationDetails().SystemKey(),
      "KMS Symmetric Encryption"
    );
    DdbHelper.DeleteBranchKey(
      branchKeyId,
      Fixtures.TEST_KEYSTORE_NAME,
      "1",
      null
    );
  }
}
