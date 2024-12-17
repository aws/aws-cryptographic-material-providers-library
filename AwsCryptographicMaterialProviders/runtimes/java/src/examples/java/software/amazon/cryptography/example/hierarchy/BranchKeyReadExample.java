// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
package software.amazon.cryptography.example.hierarchy;

import java.util.List;
import javax.annotation.Nullable;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
import software.amazon.awssdk.services.kms.KmsClient;
import software.amazon.cryptography.keystore.KeyStore;
import software.amazon.cryptography.keystore.model.BeaconKeyMaterials;
import software.amazon.cryptography.keystore.model.BranchKeyMaterials;
import software.amazon.cryptography.keystore.model.GetActiveBranchKeyInput;
import software.amazon.cryptography.keystore.model.GetBeaconKeyInput;
import software.amazon.cryptography.keystore.model.GetBranchKeyVersionInput;

public class BranchKeyReadExample {

  public static String BranchKey(
    String branchKeyId,
    String kmsArn,
    String physicalName,
    String logicalName,
    List<String> grantTokens,
    @Nullable KmsClient kmsClient,
    @Nullable DynamoDbClient dynamoDbClient
  ) {
    // 1. Configure your Key Store resource.
    KeyStore strict = KeyStoreProvider.StrictKeyStore(
      kmsArn,
      physicalName,
      logicalName,
      null,
      kmsClient,
      dynamoDbClient
    );
    BranchKeyMaterials branchKeyMaterials;

    // 2. Get the Active Branch Key
    branchKeyMaterials =
      strict
        .GetActiveBranchKey(
          GetActiveBranchKeyInput
            .builder()
            .branchKeyIdentifier(branchKeyId)
            .build()
        )
        .branchKeyMaterials();
    // Print the Encryption Context
    System.out.println(branchKeyMaterials.encryptionContext().toString());

    // 3. Get the related Branch Key Version
    branchKeyMaterials =
      strict
        .GetBranchKeyVersion(
          GetBranchKeyVersionInput
            .builder()
            .branchKeyIdentifier(branchKeyId)
            .branchKeyVersion(branchKeyMaterials.branchKeyVersion())
            .build()
        )
        .branchKeyMaterials();

    // Print the Encryption Context
    System.out.println(branchKeyMaterials.encryptionContext().toString());

    // 3. Get the Beacon Key
    BeaconKeyMaterials beaconKeyMaterials = strict
      .GetBeaconKey(
        GetBeaconKeyInput.builder().branchKeyIdentifier(branchKeyId).build()
      )
      .beaconKeyMaterials();

    // Print the Encryption Context
    System.out.println(beaconKeyMaterials.encryptionContext().toString());
    return branchKeyId;
  }

  public static void main(final String[] args) {
    if (args.length <= 1) {
      throw new IllegalArgumentException(
        "To run this example, include the keyStoreTableName, logicalKeyStoreName, and kmsKeyArn in args"
      );
    }
    final String keyStoreTableName = args[0];
    final String logicalKeyStoreName = args[1];
    final String kmsKeyArn = args[2];
    final String branchKeyId = args[3];

    BranchKey(
      branchKeyId,
      kmsKeyArn,
      keyStoreTableName,
      logicalKeyStoreName,
      null,
      null,
      null
    );
  }
}
