// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
package software.amazon.cryptography.example.hierarchy;

import org.testng.annotations.Test;
import software.amazon.cryptography.example.Fixtures;
import software.amazon.cryptography.keystore.KeyStorageInterface;

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
    branchKeyId =
      MutationExample.End2End(
        Fixtures.TEST_KEYSTORE_NAME,
        Fixtures.TEST_LOGICAL_KEYSTORE_NAME,
        Fixtures.POSTAL_HORN_KEY_ARN,
        branchKeyId,
        Fixtures.ddbClientWest2,
        Fixtures.kmsClientWest2
      );
    branchKeyId =
      VersionKeyExample.VersionKey(
        Fixtures.TEST_KEYSTORE_NAME,
        Fixtures.TEST_LOGICAL_KEYSTORE_NAME,
        Fixtures.POSTAL_HORN_KEY_ARN,
        branchKeyId,
        Fixtures.ddbClientWest2
      );
    branchKeyId =
      MutationResumeExample.Resume2End(
        Fixtures.TEST_KEYSTORE_NAME,
        Fixtures.TEST_LOGICAL_KEYSTORE_NAME,
        Fixtures.KEYSTORE_KMS_ARN,
        branchKeyId,
        Fixtures.ddbClientWest2,
        Fixtures.kmsClientWest2
      );
    KeyStorageInterface storage = StorageCheater.create(
      Fixtures.ddbClientWest2,
      Fixtures.TEST_KEYSTORE_NAME,
      Fixtures.TEST_LOGICAL_KEYSTORE_NAME
    );
    Fixtures.cleanUpBranchKeyId(storage, branchKeyId);
  }
}
