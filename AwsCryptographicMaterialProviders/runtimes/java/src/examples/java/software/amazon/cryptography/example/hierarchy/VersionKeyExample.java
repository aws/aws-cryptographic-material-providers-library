// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
package software.amazon.cryptography.example.hierarchy;

import java.util.List;

import javax.annotation.Nullable;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
import software.amazon.awssdk.services.kms.KmsClient;
import software.amazon.cryptography.keystore.KeyStore;
import software.amazon.cryptography.keystore.model.GetActiveBranchKeyInput;
import software.amazon.cryptography.keystore.model.GetActiveBranchKeyOutput;
import software.amazon.cryptography.keystore.model.VersionKeyInput;

/*
  There can only be one active version for each branch key at a time.
  The Hierarchical keyring typically uses each active branch key version
  to satisfy multiple requests.
  But you control the extent to which active branch keys are reused
  and determine how often the active branch key is rotated.

  Branch keys are not used to encrypt plaintext data keys.
  They are used to derive the unique wrapping keys
  that encrypt plaintext data keys.
  The wrapping key derivation process produces a
  unique 32 byte wrapping key with 28 bytes of randomness.
  This means that a branch key can derive more than 79 octillion, or 296,
  unique wrapping keys before cryptographic wear-out occurs.
  Despite this very low exhaustion risk,
  you might be required to rotate your active branch keys more often.

  The active version of the branch key remains active until you rotate it.
  Previous versions of the active branch key will not
  be used to perform encrypt operations and
  cannot be used to derive new wrapping keys.
  But they can still be queried and provide wrapping keys
  to decrypt the data keys that they encrypted while active.

  Use the Key Store's VersionKey operation to
  rotate your active branch key.
  When you rotate the active branch key,
  a new branch key is created to replace the previous version.
  The branch-key-id does not change when you rotate the active branch key.
  You must specify the branch-key-id that identifies
  the current active branch key when you call VersionKey.
 */
public class VersionKeyExample {

  public static String VersionKey(
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

    strict.VersionKey(
      VersionKeyInput
        .builder()
        // This the Identifier for the Branch Key that is being rotated/versioned.
        .branchKeyIdentifier(branchKeyId)
        .build()
    );
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
    VersionKey(
      branchKeyId, kmsKeyArn, keyStoreTableName,
      logicalKeyStoreName,
      null, null, null
    );
  }
}
