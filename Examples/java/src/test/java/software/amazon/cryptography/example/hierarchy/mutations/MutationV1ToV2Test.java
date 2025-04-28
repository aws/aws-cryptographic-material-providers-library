package software.amazon.cryptography.example.hierarchy.mutations;

import static software.amazon.cryptography.example.Fixtures.MRK_ARN_WEST;
import static software.amazon.cryptography.example.Fixtures.POSTAL_HORN_KEY_ARN;

import java.util.UUID;
import org.testng.annotations.Test;
import software.amazon.cryptography.example.Fixtures;
import software.amazon.cryptography.example.hierarchy.AdminProvider;
import software.amazon.cryptography.keystore.model.HierarchyVersion;

public class MutationV1ToV2Test {

  @Test
  public void testDecryptEncryptOriginalException() {
    String branchKeyId =
      "test-mutation-kms-access-in-flight-original-" +
      UUID.randomUUID().toString();

    MutationKmsAccessInFlightTestRunner.runMutationTest(
      branchKeyId,
      MRK_ARN_WEST,
      POSTAL_HORN_KEY_ARN,
      HierarchyVersion.v1,
      HierarchyVersion.v2,
      AdminProvider.decryptEncryptStrategy(
        Fixtures.kmsClientWest2,
        Fixtures.kmsClientWest2
      ),
      AdminProvider.decryptEncryptStrategy(
        Fixtures.denyMrkKmsClient,
        Fixtures.denyMrkKmsClient
      ),
      1, // expectedExceptionCount
      true, // expectFromException
      false // expectToException
    );
  }

  @Test
  public void testDecryptEncryptTerminalException() {
    String branchKeyId =
      "test-mutation-kms-access-in-flight-terminal-" +
      UUID.randomUUID().toString();

    MutationKmsAccessInFlightTestRunner.runMutationTest(
      branchKeyId,
      POSTAL_HORN_KEY_ARN,
      MRK_ARN_WEST,
      HierarchyVersion.v1,
      HierarchyVersion.v2,
      AdminProvider.decryptEncryptStrategy(
        Fixtures.kmsClientWest2,
        Fixtures.kmsClientWest2
      ),
      AdminProvider.decryptEncryptStrategy(
        Fixtures.denyMrkKmsClient,
        Fixtures.denyMrkKmsClient
      ),
      2, // expectedExceptionCount
      false, // expectFromException
      true // expectToException
    );
  }

  @Test
  public void testKmsSimpleOriginalException() {
    String branchKeyId =
      "test-mutation-kms-access-in-flight-original-" +
      UUID.randomUUID().toString();

    MutationKmsAccessInFlightTestRunner.runMutationTest(
      branchKeyId,
      MRK_ARN_WEST,
      POSTAL_HORN_KEY_ARN,
      HierarchyVersion.v1,
      HierarchyVersion.v2,
      AdminProvider.kmsSimpleStrategy(Fixtures.kmsClientWest2),
      AdminProvider.kmsSimpleStrategy(Fixtures.denyMrkKmsClient),
      1, // expectedExceptionCount
      true, // expectFromException
      false // expectToException
    );
  }

  @Test
  public void testKmsSimpleTerminalException() {
    String branchKeyId =
      "test-mutation-kms-access-in-flight-terminal-" +
      UUID.randomUUID().toString();

    MutationKmsAccessInFlightTestRunner.runMutationTest(
      branchKeyId,
      POSTAL_HORN_KEY_ARN,
      MRK_ARN_WEST,
      HierarchyVersion.v1,
      HierarchyVersion.v2,
      AdminProvider.kmsSimpleStrategy(Fixtures.kmsClientWest2),
      AdminProvider.kmsSimpleStrategy(Fixtures.denyMrkKmsClient),
      2, // expectedExceptionCount
      false, // expectFromException
      true // expectToException
    );
  }
}
