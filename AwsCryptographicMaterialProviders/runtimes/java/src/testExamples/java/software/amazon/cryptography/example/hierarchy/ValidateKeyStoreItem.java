package software.amazon.cryptography.example.hierarchy;

import software.amazon.cryptography.keystore.KeyStore;
import software.amazon.cryptography.keystore.model.GetActiveBranchKeyInput;
import software.amazon.cryptography.keystore.model.GetActiveBranchKeyOutput;
import software.amazon.cryptography.keystore.model.GetBeaconKeyInput;
import software.amazon.cryptography.keystore.model.GetBeaconKeyOutput;
import software.amazon.cryptography.keystore.model.GetBranchKeyVersionInput;
import software.amazon.cryptography.keystore.model.GetBranchKeyVersionOutput;

public class ValidateKeyStoreItem {

  public static String ValidateActiveItem(
    String branchKeyId,
    KeyStore keyStore
  ) {
    GetActiveBranchKeyOutput output = keyStore.GetActiveBranchKey(
      GetActiveBranchKeyInput.builder().branchKeyIdentifier(branchKeyId).build()
    );
    return output.branchKeyMaterials().branchKeyVersion();
  }

  public static boolean ValidateVersionItem(
    String branchKeyId,
    String version,
    KeyStore keyStore
  ) {
    GetBranchKeyVersionOutput output = keyStore.GetBranchKeyVersion(
      GetBranchKeyVersionInput
        .builder()
        .branchKeyIdentifier(branchKeyId)
        .branchKeyVersion(version)
        .build()
    );
    return true;
  }

  public static boolean ValidateBeaconItem(
    String branchKeyId,
    KeyStore keyStore
  ) {
    GetBeaconKeyOutput output = keyStore.GetBeaconKey(
      GetBeaconKeyInput.builder().branchKeyIdentifier(branchKeyId).build()
    );
    return true;
  }
  // Will author later,
  // public static void ValidateBranchKey(
  //   String branchKeyId,
  //   KeyStore keyStore
  // ) {
  // }
}
