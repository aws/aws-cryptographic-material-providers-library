// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
package software.amazon.cryptography.example.hierarchy;

import java.util.Collections;
import java.util.Map;
import javax.annotation.Nonnull;
import javax.annotation.Nullable;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
import software.amazon.awssdk.utils.StringUtils;
import software.amazon.cryptography.keystoreadmin.KeyStoreAdmin;
import software.amazon.cryptography.keystoreadmin.model.CreateKeyInput;
import software.amazon.cryptography.keystoreadmin.model.KMSIdentifier;

/*
  The Hierarchical Keyring Example relies on the existence of a
  key store with pre-existing branch key material or beacon key material.

  This example demonstrates configuring a Key Store Admin and then
  using a helper method to create a branch key and beacon key
  that share the same Id, then return that Id.
  We will always create a new beacon key alongside a new branch key,
  even if you are not using searchable encryption.

  This key creation should occur within your control plane.
 */
public class CreateKeyExample {

  public static String CreateKey(
    @Nonnull String keyStoreTableName,
    @Nonnull String logicalKeyStoreName,
    @Nonnull String kmsKeyArn,
    @Nullable String branchKeyId,
    @Nullable DynamoDbClient dynamoDbClient
  ) {
    // 1. Configure your Key Store Admin resource.
    KeyStoreAdmin admin = AdminProvider.admin(
      keyStoreTableName,
      logicalKeyStoreName,
      dynamoDbClient
    );

    // 2. If you need to specify the Identifier for a Branch Key, you may.
    // This is an optional argument.
    // If an Identifier is not provided, a v4 UUID will be generated and used.
    // This example provides a combination of a fixed string and a v4 UUID;
    // this makes it easy for Crypto Tools to clean up these Example Branch Keys.
    branchKeyId =
      StringUtils.isBlank(branchKeyId)
        ? "mpl-java-example-" + java.util.UUID.randomUUID().toString()
        : branchKeyId;

    // 3. Create a custom encryption context for the Branch Key.
    // Most encrypted data should have an associated encryption context
    // to protect integrity. This sample uses placeholder values.
    // Note that the custom encryption context for a Branch Key is
    // prefixed by the library with `aws-crypto-ec:`.
    // For more information see:
    // blogs.aws.amazon.com/security/post/Tx2LZ6WBJJANTNW/How-to-Protect-the-Integrity-of-Your-Encrypted-Data-by-Using-AWS-Key-Management
    final Map<String, String> encryptionContext = Collections.singletonMap(
      "ExampleContextKey",
      "ExampleContextValue"
    );

    // 2. Create a new branch key and beacon key in our KeyStore.
    //    Both the branch key and the beacon key will share an Id.
    //    This creation is eventually consistent.
    final String actualBranchKeyId = admin
      .CreateKey(
        CreateKeyInput
          .builder()
          // This is the KMS ARN that will be used to protect the Branch Key.
          // It is a required argument.
          .kmsArn(KMSIdentifier.builder().kmsKeyArn(kmsKeyArn).build())
          // If you need to specify the Identifier for a Branch Key, you may.
          // This is an optional argument.
          .branchKeyIdentifier(branchKeyId)
          // If a branch key Identifier is provided,
          // custom encryption context MUST be provided as well.
          .encryptionContext(encryptionContext)
          .build()
      )
      .branchKeyIdentifier();

    assert actualBranchKeyId.equals(branchKeyId);
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
