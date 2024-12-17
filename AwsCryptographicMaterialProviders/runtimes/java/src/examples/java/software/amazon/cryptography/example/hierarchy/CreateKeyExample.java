// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
package software.amazon.cryptography.example.hierarchy;

import java.util.Collections;
import java.util.List;
import java.util.Map;
import javax.annotation.Nonnull;
import javax.annotation.Nullable;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
import software.amazon.awssdk.utils.StringUtils;
import software.amazon.cryptography.keystore.KeyStore;
import software.amazon.awssdk.services.kms.KmsClient;
import software.amazon.cryptography.keystore.model.CreateKeyInput;


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
    @Nullable String branchKeyId,
    @Nonnull final String kmsArn,
    @Nonnull final String physicalName,
    @Nonnull final String logicalName,
    @Nullable final List<String> grantTokens,
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

    // 4. Create a new branch key and beacon key in our KeyStore.
    //    Both the branch key and the beacon key will share an Id.
    //    This creation is eventually consistent.
    final String actualBranchKeyId = strict
      .CreateKey(
        CreateKeyInput
          .builder()
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
    final String physical = args[0];
    final String logical = args[1];
    final String kmsKeyArn = args[2];
    CreateKey(null, kmsKeyArn, physical, logical, null, null, null);
  }
}
