package software.amazon.cryptography.example.hierarchy.mutations;

import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.stream.Collectors;
import javax.annotation.Nonnull;
import javax.annotation.Nullable;
import software.amazon.awssdk.services.kms.KmsClient;
import software.amazon.cryptography.example.hierarchy.AdminProvider;
import software.amazon.cryptography.keystore.model.AwsKms;
import software.amazon.cryptography.keystoreadmin.KeyStoreAdmin;
import software.amazon.cryptography.keystoreadmin.model.ApplyMutationInput;
import software.amazon.cryptography.keystoreadmin.model.ApplyMutationOutput;
import software.amazon.cryptography.keystoreadmin.model.ApplyMutationResult;
import software.amazon.cryptography.keystoreadmin.model.InitializeMutationInput;
import software.amazon.cryptography.keystoreadmin.model.InitializeMutationOutput;
import software.amazon.cryptography.keystoreadmin.model.KeyManagementStrategy;
import software.amazon.cryptography.keystoreadmin.model.KmsSymmetricEncryption;
import software.amazon.cryptography.keystoreadmin.model.KmsSymmetricKeyArn;
import software.amazon.cryptography.keystoreadmin.model.MutatedBranchKeyItem;
import software.amazon.cryptography.keystoreadmin.model.MutationToken;
import software.amazon.cryptography.keystoreadmin.model.Mutations;
import software.amazon.cryptography.keystoreadmin.model.SystemKey;
import software.amazon.cryptography.keystoreadmin.model.TrustStorage;

public class MutationsProvider {

  public static String mutatedItemsToString(
    List<MutatedBranchKeyItem> mutatedItems
  ) {
    return mutatedItems
      .stream()
      .map(item -> String.format("%s : %s", item.ItemType(), item.Description())
      )
      .collect(Collectors.joining(",\n"));
  }

  public static Mutations defaultMutation(
    @Nonnull final String terminalKmsArn
  ) {
    HashMap<String, String> terminalEC = new HashMap<>(2, 1);
    terminalEC.put("Robbie", "is a dog.");
    return Mutations
      .builder()
      .TerminalEncryptionContext(terminalEC)
      .TerminalKmsArn(terminalKmsArn)
      .build();
  }

  public static SystemKey KmsSystemKey(@Nonnull final String systemKeyArn) {
    return KmsSystemKey(systemKeyArn, null, null);
  }

  public static SystemKey KmsSystemKey(
    @Nonnull final String systemKeyArn,
    @Nullable KmsClient systemKeyKmsClient,
    @Nullable List<String> systemKeyGrantTokens
  ) {
    //noinspection unchecked
    final List<String> tempList = systemKeyGrantTokens == null
      ? Collections.EMPTY_LIST
      : systemKeyGrantTokens;
    final KmsClient tempKms = systemKeyKmsClient == null
      ? AdminProvider.kms(null)
      : systemKeyKmsClient;
    final AwsKms tempAws = AwsKms
      .builder()
      .kmsClient(tempKms)
      .grantTokens(tempList)
      .build();
    return SystemKey
      .builder()
      .kmsSymmetricEncryption(
        KmsSymmetricEncryption
          .builder()
          .AwsKms(tempAws)
          .KmsArn(systemKeyArn)
          .build()
      )
      .build();
  }

  public static SystemKey TrustStorage() {
    return SystemKey
      .builder()
      .trustStorage(TrustStorage.builder().build())
      .build();
  }

  public static void workMutation(
    String branchKeyId,
    SystemKey systemKey,
    MutationToken token,
    KeyManagementStrategy strategy,
    KeyStoreAdmin admin
  ) {
    boolean done = false;
    int limitLoop = 10;

    while (!done) {
      ApplyMutationResult result = workPage(
        branchKeyId,
        systemKey,
        token,
        strategy,
        admin,
        1
      );

      if (result.ContinueMutation() != null) {
        token = result.ContinueMutation();
      }
      if (result.CompleteMutation() != null) {
        done = true;
      }
      if (limitLoop == 0) {
        done = true;
      }
      limitLoop--;
    }
  }

  static ApplyMutationResult workPage(
    String branchKeyId,
    SystemKey systemKey,
    MutationToken token,
    KeyManagementStrategy strategy,
    KeyStoreAdmin admin,
    Integer pageSize
  ) {
    ApplyMutationInput applyInput = ApplyMutationInput
      .builder()
      .MutationToken(token)
      .PageSize(pageSize)
      .Strategy(strategy)
      .SystemKey(systemKey)
      .build();
    ApplyMutationOutput applyOutput = admin.ApplyMutation(applyInput);
    ApplyMutationResult result = applyOutput.MutationResult();

    System.out.println(
      "ApplyLogs: " +
      branchKeyId +
      " items: \n" +
      mutatedItemsToString(applyOutput.MutatedBranchKeyItems())
    );
    return result;
  }

  static MutationToken executeInitialize(
    String branchKeyId,
    KeyStoreAdmin admin,
    InitializeMutationInput initInput,
    String logPrefix
  ) {
    InitializeMutationOutput initOutput = admin.InitializeMutation(initInput);
    MutationToken token = initOutput.MutationToken();
    System.out.println(
      logPrefix +
      ": " +
      "\nFlag: " +
      initOutput.InitializeMutationFlag().toString() +
      "\nIdentifier: " +
      branchKeyId +
      "\nitems: \n" +
      mutatedItemsToString(initOutput.MutatedBranchKeyItems())
    );
    return token;
  }
}
