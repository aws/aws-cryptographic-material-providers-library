package software.amazon.cryptography.example.hierarchy.mutations;

import java.util.HashMap;
import javax.annotation.Nullable;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
import software.amazon.awssdk.services.kms.KmsClient;
import software.amazon.cryptography.example.Fixtures;
import software.amazon.cryptography.example.hierarchy.AdminProvider;
import software.amazon.cryptography.example.hierarchy.StorageExample;
import software.amazon.cryptography.keystore.KeyStorageInterface;
import software.amazon.cryptography.keystoreadmin.KeyStoreAdmin;
import software.amazon.cryptography.keystoreadmin.model.InitializeMutationInput;
import software.amazon.cryptography.keystoreadmin.model.InitializeMutationOutput;
import software.amazon.cryptography.keystoreadmin.model.KeyManagementStrategy;
import software.amazon.cryptography.keystoreadmin.model.MutationToken;
import software.amazon.cryptography.keystoreadmin.model.Mutations;
import software.amazon.cryptography.keystoreadmin.model.SystemKey;
import software.amazon.cryptography.keystoreadmin.model.TrustStorage;

public class MutationExampleDecryptEncryptStrategy {

  public static String End2EndDecryptEncrypt(
    String keyStoreTableName,
    String logicalKeyStoreName,
    String kmsKeyArnTerminal,
    String branchKeyId,
    SystemKey systemKey,
    @Nullable DynamoDbClient dynamoDbClient,
    @Nullable KmsClient decryptKmsClient,
    @Nullable KmsClient encryptKmsClient
  ) {
    decryptKmsClient = AdminProvider.kms(decryptKmsClient);
    encryptKmsClient = AdminProvider.kms(encryptKmsClient);

    KeyManagementStrategy strategy = AdminProvider.decryptEncryptStrategy(
      decryptKmsClient,
      encryptKmsClient
    );
    KeyStoreAdmin admin = AdminProvider.admin(
      keyStoreTableName,
      logicalKeyStoreName,
      dynamoDbClient
    );

    System.out.println("BranchKey ID to mutate: " + branchKeyId);
    HashMap<String, String> terminalEC = new HashMap<>();
    terminalEC.put("Koda", "is a dog.");
    Mutations mutations = Mutations
      .builder()
      .TerminalEncryptionContext(terminalEC)
      .TerminalKmsArn(kmsKeyArnTerminal)
      .build();

    InitializeMutationInput initInput = InitializeMutationInput
      .builder()
      .Mutations(mutations)
      .Identifier(branchKeyId)
      .Strategy(strategy)
      .SystemKey(systemKey)
      .build();

    InitializeMutationOutput initOutput = admin.InitializeMutation(initInput);

    MutationToken token = initOutput.MutationToken();
    System.out.println(
      "InitLogs: " +
      branchKeyId +
      " items: \n" +
      MutationsProvider.mutatedItemsToString(initOutput.MutatedBranchKeyItems())
    );
    MutationsProvider.workMutation(
      branchKeyId,
      systemKey,
      token,
      strategy,
      admin
    );

    System.out.println("Done with Mutation: " + branchKeyId);

    return branchKeyId;
  }

  public static void main(final String[] args) {
    if (args.length <= 3) {
      throw new IllegalArgumentException(
        "To run this example, include the keyStoreTableName, logicalKeyStoreName, kmsKeyTerminal, and branchKeyId in args"
      );
    }
    final String keyStoreTableName = args[0];
    final String logicalKeyStoreName = args[1];
    final String kmsKeyArnTerminal = args[2];
    final String branchKeyId = args[3];
    End2EndDecryptEncrypt(
      keyStoreTableName,
      logicalKeyStoreName,
      kmsKeyArnTerminal,
      branchKeyId,
      SystemKey.builder().trustStorage(TrustStorage.builder().build()).build(),
      null,
      null,
      null
    );

    // We clean up our items to make sure the table doesn't grow indefinitely.
    Fixtures.cleanUpBranchKeyId(null, branchKeyId, true);
  }
}
