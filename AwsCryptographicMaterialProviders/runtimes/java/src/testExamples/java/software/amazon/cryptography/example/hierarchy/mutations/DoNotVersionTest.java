package software.amazon.cryptography.example.hierarchy.mutations;

import static software.amazon.cryptography.example.Fixtures.MRK_ARN_WEST;

import org.testng.Assert;
import org.testng.annotations.Test;
import software.amazon.cryptography.example.Fixtures;
import software.amazon.cryptography.example.hierarchy.AdminProvider;
import software.amazon.cryptography.example.hierarchy.CreateKeyExample;
import software.amazon.cryptography.keystoreadmin.KeyStoreAdmin;
import software.amazon.cryptography.keystoreadmin.model.InitializeMutationInput;
import software.amazon.cryptography.keystoreadmin.model.InitializeMutationOutput;
import software.amazon.cryptography.keystoreadmin.model.Mutations;
import software.amazon.cryptography.keystoreadmin.model.UnsupportedFeatureException;

public class DoNotVersionTest {

  static final String testPrefix =
    "mutations-initialize-mutation-do-not-version-java";

  @Test
  public void DoNotVersionThrowsUnsupportedFeatureExceptionTest() {
    Assert.assertThrows(
      UnsupportedFeatureException.class,
      () -> {
        // Uncomment BK Creation if you need to re-create the test key
        // String branchKeyId = CreateKeyExample.CreateKey(
        //   Fixtures.TEST_KEYSTORE_NAME,
        //   Fixtures.TEST_LOGICAL_KEYSTORE_NAME,
        //   Fixtures.KEYSTORE_KMS_ARN,
        //   testPrefix,
        //   Fixtures.ddbClientWest2
        // );
        Mutations mutations = Mutations
          .builder()
          .TerminalKmsArn(MRK_ARN_WEST)
          .build();

        InitializeMutationInput initInput = InitializeMutationInput
          .builder()
          .Mutations(mutations)
          .Identifier(testPrefix)
          .DoNotVersion(true)
          .build();
        KeyStoreAdmin admin = AdminProvider.admin(
          Fixtures.TEST_KEYSTORE_NAME,
          Fixtures.TEST_LOGICAL_KEYSTORE_NAME,
          Fixtures.ddbClientWest2
        );
        InitializeMutationOutput initOutput = admin.InitializeMutation(
          initInput
        );
      }
    );
  }
}
