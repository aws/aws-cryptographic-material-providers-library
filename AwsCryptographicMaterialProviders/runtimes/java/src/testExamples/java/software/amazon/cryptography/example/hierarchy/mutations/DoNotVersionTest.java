package software.amazon.cryptography.example.hierarchy.mutations;

import static software.amazon.cryptography.example.Fixtures.MRK_ARN_WEST;

import org.testng.Assert;
import org.testng.annotations.Test;
import software.amazon.cryptography.example.Fixtures;
import software.amazon.cryptography.example.hierarchy.AdminProvider;
import software.amazon.cryptography.example.hierarchy.CreateKeyExample;
import software.amazon.cryptography.example.hierarchy.KeyStoreProvider;
import software.amazon.cryptography.example.hierarchy.ValidateKeyStoreItem;
import software.amazon.cryptography.keystore.KeyStore;
import software.amazon.cryptography.keystoreadmin.KeyStoreAdmin;
import software.amazon.cryptography.keystoreadmin.model.InitializeMutationInput;
import software.amazon.cryptography.keystoreadmin.model.InitializeMutationOutput;
import software.amazon.cryptography.keystoreadmin.model.KeyManagementStrategy;
import software.amazon.cryptography.keystoreadmin.model.Mutations;
import software.amazon.cryptography.keystoreadmin.model.SystemKey;
import software.amazon.cryptography.keystoreadmin.model.UnsupportedFeatureException;

public class DoNotVersionTest {

  static final String testPrefix = "initialize-mutation-do-not-version-java-";

  @Test
  public void DoNotVersion() {
    final KeyStoreAdmin admin = AdminProvider.admin();
    String branchKeyId = testPrefix + java.util.UUID.randomUUID().toString();
    Assert.assertEquals(
      branchKeyId,
      CreateKeyExample.CreateKey(Fixtures.KEYSTORE_KMS_ARN, branchKeyId, admin),
      "Creation of test BK failed."
    );
    SystemKey systemKey = MutationsProvider.KmsSystemKey();
    KeyManagementStrategy strategy = AdminProvider.strategy(
      Fixtures.kmsClientWest2
    );
    InitializeMutationInput initInput = InitializeMutationInput
      .builder()
      .Mutations(
        MutationsProvider.defaultMutation(Fixtures.POSTAL_HORN_KEY_ARN)
      )
      .Identifier(branchKeyId)
      .DoNotVersion(true)
      .SystemKey(systemKey)
      .Strategy(strategy)
      .build();
    InitializeMutationOutput initOutput = admin.InitializeMutation(initInput);
    MutationsProvider.workMutation(
      branchKeyId,
      systemKey,
      initOutput.MutationToken(),
      strategy,
      admin,
      (short) 10
    );
    final KeyStore keyStore = KeyStoreProvider.keyStore();
    final String version = ValidateKeyStoreItem.ValidateActiveItem(
      branchKeyId,
      keyStore
    );
    Assert.assertNotNull(version, "Active Item validation failed.");
    Assert.assertTrue(
      ValidateKeyStoreItem.ValidateVersionItem(branchKeyId, version, keyStore),
      "Version validation failed."
    );
    Assert.assertTrue(
      ValidateKeyStoreItem.ValidateBeaconItem(branchKeyId, keyStore),
      "Beacon validation failed."
    );
  }
}
