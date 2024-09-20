// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
package software.amazon.cryptography.example.hierarchy;

import javax.annotation.Nullable;

import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
import software.amazon.awssdk.services.kms.KmsClient;
import software.amazon.cryptography.keystore.model.AwsKms;
import software.amazon.cryptography.keystoreadmin.KeyStoreAdmin;
import software.amazon.cryptography.keystoreadmin.model.KMSIdentifier;
import software.amazon.cryptography.keystoreadmin.model.KeyManagementStrategy;
import software.amazon.cryptography.keystoreadmin.model.CreateKeyInput;

/*
  The Hierarchical Keyring Example and Searchable Encryption Examples
  rely on the existence of a DDB-backed key store with pre-existing
  branch key material or beacon key material.

  See the "Create KeyStore Table Example" for how to first set up
  the DDB Table that will back this KeyStore.

  This example demonstrates configuring a KeyStore and then
  using a helper method to create a branch key and beacon key
  that share the same Id, then return that Id.
  We will always create a new beacon key alongside a new branch key,
  even if you are not using searchable encryption.

  This key creation should occur within your control plane.
 */
public class CreateKeyExample {

  public static String CreateKey(
    String keyStoreTableName,
    String logicalKeyStoreName,
    String kmsKeyArn,
    @Nullable DynamoDbClient dynamoDbClient,
    @Nullable KmsClient kmsClient
  ) {
    if (kmsClient == null) {
      kmsClient = KmsClient.create();
    }
    KeyStoreAdmin admin = AdminProvider.admin(
      keyStoreTableName,
      logicalKeyStoreName,
      dynamoDbClient
    );

    // 2. Create a new branch key and beacon key in our KeyStore.
    //    Both the branch key and the beacon key will share an Id.
    //    This creation is eventually consistent.

    final String branchKeyId = admin
      .CreateKey(
        CreateKeyInput.builder()
        .kmsArn(
          KMSIdentifier.builder().kmsKeyArn(kmsKeyArn).build())
        .strategy(
          KeyManagementStrategy.builder()
            .AwsKmsReEncrypt(
              AwsKms.builder().kmsClient(kmsClient).build()
            ).build()
        ).build()).branchKeyIdentifier();

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
    CreateKey(keyStoreTableName, logicalKeyStoreName, kmsKeyArn, null, null);
  }
}
