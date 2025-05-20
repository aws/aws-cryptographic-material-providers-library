package software.amazon.cryptography.example.hierarchy.mutations;

import static software.amazon.cryptography.example.hierarchy.mutations.MutationsProvider.executeInitialize;

import java.util.Collections;
import java.util.Map;
import java.util.List;
import java.util.Map;
import org.testng.Assert;
import org.testng.annotations.Test;
import software.amazon.awssdk.services.dynamodb.model.AttributeValue;
import software.amazon.cryptography.example.DdbHelper;
import software.amazon.cryptography.example.Fixtures;
import software.amazon.cryptography.example.hierarchy.AdminProvider;
import software.amazon.cryptography.example.hierarchy.CreateKeyExample;
import software.amazon.cryptography.example.hierarchy.KeyStoreProvider;
import software.amazon.cryptography.example.hierarchy.ValidateKeyStoreItem;
import software.amazon.cryptography.keystore.KeyStore;
import software.amazon.cryptography.keystore.model.HierarchyVersion;
import software.amazon.cryptography.keystoreadmin.KeyStoreAdmin;
import software.amazon.cryptography.keystoreadmin.model.InitializeMutationInput;
import software.amazon.cryptography.keystoreadmin.model.KeyManagementStrategy;
import software.amazon.cryptography.keystoreadmin.model.MutationToken;
import software.amazon.cryptography.keystoreadmin.model.SystemKey;

public class DoNotVersionTest {

  static final String testPrefix = "initialize-mutation-do-not-version-java-";

  @Test
  public void DoNotVersion() {
    final KeyStoreAdmin admin = AdminProvider.admin();
    String branchKeyId = testPrefix + java.util.UUID.randomUUID().toString();
    final Map<String, String> encryptionContext = Collections.singletonMap(
      "Robbie",
      "Is a Dog."
    );
    Assert.assertEquals(
      branchKeyId,
      CreateKeyExample.CreateKey(
        Fixtures.KEYSTORE_KMS_ARN,
        branchKeyId,
        admin,
        HierarchyVersion.v1,
        encryptionContext
      ),
      "Creation of test BK failed."
    );
    SystemKey systemKey = MutationsProvider.KmsSystemKey();
    KeyManagementStrategy strategy = AdminProvider.reEncryptStrategy(
      Fixtures.kmsClientWest2
    );
    InitializeMutationInput initInput = InitializeMutationInput
      .builder()
      .Mutations(
        MutationsProvider.defaultMutation(Fixtures.POSTAL_HORN_KEY_ARN, null)
      )
      .Identifier(branchKeyId)
      .DoNotVersion(true)
      .SystemKey(systemKey)
      .Strategy(strategy)
      .build();

    MutationToken token = executeInitialize(
      branchKeyId,
      admin,
      initInput,
      "InitLogs"
    );

    MutationsProvider.workMutation(
      branchKeyId,
      systemKey,
      token,
      strategy,
      admin,
      (short) 10
    );
    final KeyStore keyStore = KeyStoreProvider.keyStore(
      Fixtures.POSTAL_HORN_KEY_ARN
    );
    ValidateKeyStoreItem.ValidateBranchKey(branchKeyId, keyStore);
    final List<Map<String, AttributeValue>> allBKItems =
      DdbHelper.QueryForAllBkItemsDDBKeys(branchKeyId, null, null);
    Assert.assertEquals(allBKItems.size(), 3, "Incorrect number of BK items.");
    DdbHelper.DeleteAllBkKeys(allBKItems, null, null);
  }
}
