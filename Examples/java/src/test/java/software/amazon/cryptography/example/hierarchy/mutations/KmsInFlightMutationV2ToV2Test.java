package software.amazon.cryptography.example.hierarchy.mutations;

import static software.amazon.cryptography.example.Fixtures.MRK_ARN_WEST;
import static software.amazon.cryptography.example.Fixtures.POSTAL_HORN_KEY_ARN;

import java.util.UUID;
import org.testng.annotations.Test;
import software.amazon.cryptography.example.DdbHelper;
import software.amazon.cryptography.example.Fixtures;
import software.amazon.cryptography.example.hierarchy.AdminProvider;
import software.amazon.cryptography.keystore.model.HierarchyVersion;
import software.amazon.cryptography.keystoreadmin.model.Mutations;

public class KmsInFlightMutationV2ToV2Test {

  @Test
  public void testDecryptEncryptOriginalException() {
    String branchKeyId =
      "test-mutation-kms-access-in-flight-original-" +
      UUID.randomUUID().toString();

    AdminProvider.createHappyCaseId(
      MRK_ARN_WEST,
      branchKeyId,
      AdminProvider.admin(),
      HierarchyVersion.v2,
      1
    );

    try {
      Mutations mutations = Mutations
        .builder()
        .TerminalKmsArn(POSTAL_HORN_KEY_ARN)
        .build();

      KmsInFlightMutationAccessDeniedRunner.runMutationTest(
        branchKeyId,
        mutations,
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
    } finally {
      DdbHelper.DeleteBranchKey(branchKeyId, Fixtures.TEST_KEYSTORE_NAME, null);
    }
  }

  @Test
  public void testDecryptEncryptTerminalException() {
    String branchKeyId =
      "test-mutation-kms-access-in-flight-terminal-" +
      UUID.randomUUID().toString();

    AdminProvider.createHappyCaseId(
      POSTAL_HORN_KEY_ARN,
      branchKeyId,
      AdminProvider.admin(),
      HierarchyVersion.v2,
      1
    );

    try {
      Mutations mutations = Mutations
        .builder()
        .TerminalKmsArn(MRK_ARN_WEST)
        .build();

      KmsInFlightMutationAccessDeniedRunner.runMutationTest(
        branchKeyId,
        mutations,
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
    } finally {
      DdbHelper.DeleteBranchKey(branchKeyId, Fixtures.TEST_KEYSTORE_NAME, null);
    }
  }

  @Test
  public void testKmsSimpleOriginalException() {
    String branchKeyId =
      "test-mutation-kms-access-in-flight-original-" +
      UUID.randomUUID().toString();

    AdminProvider.createHappyCaseId(
      MRK_ARN_WEST,
      branchKeyId,
      AdminProvider.admin(),
      HierarchyVersion.v2,
      1
    );

    try {
      Mutations mutations = Mutations
        .builder()
        .TerminalKmsArn(POSTAL_HORN_KEY_ARN)
        .build();

      KmsInFlightMutationAccessDeniedRunner.runMutationTest(
        branchKeyId,
        mutations,
        AdminProvider.kmsSimpleStrategy(Fixtures.kmsClientWest2),
        AdminProvider.kmsSimpleStrategy(Fixtures.denyMrkKmsClient),
        1, // expectedExceptionCount
        true, // expectFromException
        false // expectToException
      );
    } finally {
      DdbHelper.DeleteBranchKey(branchKeyId, Fixtures.TEST_KEYSTORE_NAME, null);
    }
  }

  @Test
  public void testKmsSimpleTerminalException() {
    String branchKeyId =
      "test-mutation-kms-access-in-flight-terminal-" +
      UUID.randomUUID().toString();

    AdminProvider.createHappyCaseId(
      POSTAL_HORN_KEY_ARN,
      branchKeyId,
      AdminProvider.admin(),
      HierarchyVersion.v2,
      1
    );

    try {
      Mutations mutations = Mutations
        .builder()
        .TerminalKmsArn(MRK_ARN_WEST)
        .build();

      KmsInFlightMutationAccessDeniedRunner.runMutationTest(
        branchKeyId,
        mutations,
        AdminProvider.kmsSimpleStrategy(Fixtures.kmsClientWest2),
        AdminProvider.kmsSimpleStrategy(Fixtures.denyMrkKmsClient),
        2, // expectedExceptionCount
        false, // expectFromException
        true // expectToException
      );
    } finally {
      DdbHelper.DeleteBranchKey(branchKeyId, Fixtures.TEST_KEYSTORE_NAME, null);
    }
  }
}
