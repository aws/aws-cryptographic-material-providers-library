package software.amazon.cryptography.example.hierarchy.mutations;

import static software.amazon.cryptography.example.hierarchy.mutations.MutationsProvider.executeInitialize;
import static software.amazon.cryptography.example.hierarchy.mutations.MutationsProvider.workPage;

import java.nio.charset.StandardCharsets;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;
import java.util.Objects;
import org.testng.Assert;
import org.testng.annotations.Test;
import software.amazon.awssdk.core.SdkBytes;
import software.amazon.awssdk.services.dynamodb.model.AttributeAction;
import software.amazon.awssdk.services.dynamodb.model.AttributeValue;
import software.amazon.awssdk.services.dynamodb.model.AttributeValueUpdate;
import software.amazon.cryptography.example.Fixtures;
import software.amazon.cryptography.example.hierarchy.AdminProvider;
import software.amazon.cryptography.example.hierarchy.CreateKeyExample;
import software.amazon.cryptography.example.hierarchy.StorageExample;
import software.amazon.cryptography.keystore.KeyStorageInterface;
import software.amazon.cryptography.keystoreadmin.KeyStoreAdmin;
import software.amazon.cryptography.keystoreadmin.model.InitializeMutationInput;
import software.amazon.cryptography.keystoreadmin.model.KeyManagementStrategy;
import software.amazon.cryptography.keystoreadmin.model.MutationToken;
import software.amazon.cryptography.keystoreadmin.model.MutationVerificationException;
import software.amazon.cryptography.keystoreadmin.model.Mutations;
import software.amazon.cryptography.keystoreadmin.model.SystemKey;

public class TestMutationsSystemKeyKMSTamper {

  static final String testPrefix = "java-test-mutation-system-key-kms-tamper-";

  public static Map<String, AttributeValue> ddbKeyForCommitment(
    final String identifier
  ) {
    Map<String, AttributeValue> ddbKey = new HashMap<>(3, 1);
    ddbKey.put("branch-key-id", AttributeValue.fromS(identifier));
    ddbKey.put("type", AttributeValue.fromS("branch:MUTATION_COMMITMENT"));
    return ddbKey;
  }

  public static Map<String, AttributeValue> ddbKeyForIndex(
    final String identifier
  ) {
    Map<String, AttributeValue> ddbKey = new HashMap<>(3, 1);
    ddbKey.put("branch-key-id", AttributeValue.fromS(identifier));
    ddbKey.put("type", AttributeValue.fromS("branch:MUTATION_INDEX"));
    return ddbKey;
  }

  @Test
  public void testCreateTimeCommitment() {
    Map<String, AttributeValueUpdate> tamper = new HashMap<>(2, 1);
    tamper.put(
      "create-time",
      AttributeValueUpdate
        .builder()
        .value(AttributeValue.fromS("now!"))
        .action(AttributeAction.PUT)
        .build()
    );
    testAttribute(
      tamper,
      testPrefix + "create-time-commitment-",
      "branch:MUTATION_COMMITMENT"
    );
  }

  @Test
  public void testCreateTimeIndex() {
    Map<String, AttributeValueUpdate> tamper = new HashMap<>(2, 1);
    tamper.put(
      "create-time",
      AttributeValueUpdate
        .builder()
        .value(AttributeValue.fromS("now!"))
        .action(AttributeAction.PUT)
        .build()
    );
    testAttribute(
      tamper,
      testPrefix + "create-time-index-",
      "branch:MUTATION_INDEX"
    );
  }

  // Tampering the H-Version results in a Key Storage Failure
  // @Test
  // public void testHierarchyVersion() {
  //   Map<String, AttributeValueUpdate> tamper = new HashMap<>(2, 1);
  //   tamper.put(
  //     "hierarchy-version",
  //     AttributeValueUpdate
  //       .builder()
  //       .value(AttributeValue.fromN("2"))
  //       .action(AttributeAction.PUT)
  //       .build()
  //   );
  //   testAttribute(tamper, testPrefix + "hierarchy-version-");
  // }

  @Test
  public void testInput() {
    Map<String, AttributeValueUpdate> tamper = new HashMap<>(2, 1);
    tamper.put(
      "input",
      AttributeValueUpdate
        .builder()
        .value(
          AttributeValue.fromB(
            SdkBytes.fromString(
              "{\"kms-arn\":\"arn:aws:kms:us-west-2:658956600833:key/mrk-80bd8ecdcd4342aebd84b7dc9da498a7\"}",
              StandardCharsets.UTF_8
            )
          )
        )
        .action(AttributeAction.PUT)
        .build()
    );
    testAttribute(tamper, testPrefix + "input-", "branch:MUTATION_COMMITMENT");
  }

  @Test
  public void testOriginal() {
    Map<String, AttributeValueUpdate> tamper = new HashMap<>(2, 1);
    tamper.put(
      "original",
      AttributeValueUpdate
        .builder()
        .value(
          AttributeValue.fromB(
            SdkBytes.fromString(
              "{\"kms-arn\":\"arn:aws:kms:us-west-2:658956600833:key/mrk-80bd8ecdcd4342aebd84b7dc9da498a7\"}",
              StandardCharsets.UTF_8
            )
          )
        )
        .action(AttributeAction.PUT)
        .build()
    );
    testAttribute(
      tamper,
      testPrefix + "original-",
      "branch:MUTATION_COMMITMENT"
    );
  }

  @Test
  public void testTerminal() {
    Map<String, AttributeValueUpdate> tamper = new HashMap<>(2, 1);
    tamper.put(
      "terminal",
      AttributeValueUpdate
        .builder()
        .value(
          AttributeValue.fromB(
            SdkBytes.fromString(
              "{\"kms-arn\":\"arn:aws:kms:us-west-2:658956600833:key/mrk-80bd8ecdcd4342aebd84b7dc9da498a7\"}",
              StandardCharsets.UTF_8
            )
          )
        )
        .action(AttributeAction.PUT)
        .build()
    );
    testAttribute(
      tamper,
      testPrefix + "terminal-",
      "branch:MUTATION_COMMITMENT"
    );
  }

  @Test
  public void testPageIndex() {
    Map<String, AttributeValueUpdate> tamper = new HashMap<>(2, 1);
    tamper.put(
      "pageIndex",
      AttributeValueUpdate
        .builder()
        .value(
          AttributeValue.fromB(
            SdkBytes.fromString("Done", StandardCharsets.UTF_8)
          )
        )
        .action(AttributeAction.PUT)
        .build()
    );
    testAttribute(tamper, testPrefix + "pageIndex-", "branch:MUTATION_INDEX");
  }

  public void testAttribute(
    Map<String, AttributeValueUpdate> tamper,
    String testPrefix,
    String type
  ) {
    final String identifier =
      testPrefix + java.util.UUID.randomUUID().toString();

    CreateKeyExample.CreateKey(
      Fixtures.TEST_KEYSTORE_NAME,
      Fixtures.TEST_LOGICAL_KEYSTORE_NAME,
      Fixtures.MRK_ARN_WEST,
      identifier,
      Fixtures.ddbClientWest2
    );
    //noinspection unchecked
    SystemKey systemKey = MutationsProvider.KmsSystemKey(
      Fixtures.POSTAL_HORN_KEY_ARN,
      Fixtures.kmsClientWest2,
      Collections.EMPTY_LIST
    );
    KeyStoreAdmin admin = AdminProvider.admin(
      Fixtures.TEST_KEYSTORE_NAME,
      Fixtures.TEST_LOGICAL_KEYSTORE_NAME,
      Fixtures.ddbClientWest2
    );
    Mutations mutations = MutationsProvider.defaultMutation(
      Fixtures.POSTAL_HORN_KEY_ARN
    );
    KeyManagementStrategy strategy = AdminProvider.strategy(null);
    InitializeMutationInput initInput = InitializeMutationInput
      .builder()
      .Mutations(mutations)
      .Identifier(identifier)
      .Strategy(strategy)
      .SystemKey(systemKey)
      .build();
    MutationToken token = executeInitialize(
      identifier,
      admin,
      initInput,
      "InitLogs"
    );
    Map<String, AttributeValue> ddbKey = Objects.equals(
        type,
        "branch:MUTATION_COMMITMENT"
      )
      ? ddbKeyForCommitment(identifier)
      : ddbKeyForIndex(identifier);
    Fixtures.ddbClientWest2.updateItem(builder ->
      builder
        .attributeUpdates(tamper)
        .tableName(Fixtures.TEST_KEYSTORE_NAME)
        .key(ddbKey)
    );
    boolean exThrown = false;
    try {
      workPage(identifier, systemKey, token, strategy, admin, 1);
    } catch (MutationVerificationException ex) {
      System.out.println(
        "Apply with wrong SystemKey failed with: \n" +
        ex.getClass().getSimpleName() +
        ": " +
        ex.getMessage()
      );
      exThrown = true;
    }
    KeyStorageInterface storage = StorageExample.create(
      Fixtures.ddbClientWest2,
      Fixtures.TEST_KEYSTORE_NAME,
      Fixtures.TEST_LOGICAL_KEYSTORE_NAME
    );
    Assert.assertTrue(
      exThrown,
      "Tampering should have lead to a MutationVerificationException! testId: " +
      identifier
    );
    Fixtures.cleanUpBranchKeyId(storage, identifier, true);
  }
}
