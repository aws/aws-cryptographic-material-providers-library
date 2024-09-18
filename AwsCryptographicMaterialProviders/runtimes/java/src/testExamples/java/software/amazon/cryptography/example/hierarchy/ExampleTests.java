// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
package software.amazon.cryptography.example.hierarchy;

import org.testng.annotations.Test;
import software.amazon.cryptography.example.Fixtures;
import software.amazon.cryptography.example.StorageCheater;
import software.amazon.cryptography.keystore.KeyStorageInterface;
import software.amazon.cryptography.keystoreadmin.model.SystemKey;
import software.amazon.cryptography.keystoreadmin.model.TrustStorage;

public class ExampleTests {

  @Test
  public void End2EndTests() {
    String branchKeyId = CreateKeyExample.CreateKey(
      Fixtures.TEST_KEYSTORE_NAME,
      Fixtures.TEST_LOGICAL_KEYSTORE_NAME,
      Fixtures.KEYSTORE_KMS_ARN,
      null,
      Fixtures.ddbClientWest2
    );
    System.out.println("\nCreated Branch Key: " + branchKeyId);
    branchKeyId =
      MutationExample.End2End(
        Fixtures.TEST_KEYSTORE_NAME,
        Fixtures.TEST_LOGICAL_KEYSTORE_NAME,
        Fixtures.POSTAL_HORN_KEY_ARN,
        branchKeyId,
        SystemKey
          .builder()
          .trustStorage(TrustStorage.builder().build())
          .build(),
        Fixtures.ddbClientWest2,
        Fixtures.kmsClientWest2
      );
    System.out.println(
      "\nMutated Branch Key: " +
      branchKeyId +
      " to KMS ARN: " +
      Fixtures.POSTAL_HORN_KEY_ARN +
      "\n"
    );
    branchKeyId =
      VersionKeyExample.VersionKey(
        Fixtures.TEST_KEYSTORE_NAME,
        Fixtures.TEST_LOGICAL_KEYSTORE_NAME,
        Fixtures.POSTAL_HORN_KEY_ARN,
        branchKeyId,
        Fixtures.ddbClientWest2
      );
    System.out.println("\nVersioned Branch Key: " + branchKeyId + "\n");
    branchKeyId =
      MutationResumeExample.Resume2End(
        Fixtures.TEST_KEYSTORE_NAME,
        Fixtures.TEST_LOGICAL_KEYSTORE_NAME,
        Fixtures.KEYSTORE_KMS_ARN,
        branchKeyId,
        SystemKey
          .builder()
          .trustStorage(TrustStorage.builder().build())
          .build(),
        Fixtures.ddbClientWest2,
        Fixtures.kmsClientWest2
      );
    System.out.println(
      "\nMutated Branch Key with Resume: " +
      branchKeyId +
      " to KMS ARN: " +
      Fixtures.KEYSTORE_KMS_ARN +
      "\n"
    );
    KeyStorageInterface storage = StorageCheater.create(
      Fixtures.ddbClientWest2,
      Fixtures.TEST_KEYSTORE_NAME,
      Fixtures.TEST_LOGICAL_KEYSTORE_NAME
    );
    Fixtures.cleanUpBranchKeyId(storage, branchKeyId);
  }
}
