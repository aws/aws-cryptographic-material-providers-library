// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
package software.amazon.cryptography.example.hierarchy;

import org.testng.annotations.Test;
import software.amazon.cryptography.example.TestUtils;
import software.amazon.cryptography.keystore.KeyStorageInterface;
import software.amazon.cryptography.keystore.model.QueryForVersionsInput;
import software.amazon.cryptography.keystore.model.QueryForVersionsOutput;

public class MutationExampleTests {

  @Test
  public void testMutationExample() {
    String branchKeyId = MutationExample.End2End(
      TestUtils.TEST_KEYSTORE_NAME,
      TestUtils.TEST_LOGICAL_KEYSTORE_NAME,
      TestUtils.KEYSTORE_KMS_ARN,
      TestUtils.POSTAL_HORN_KEY_ARN,
      TestUtils.dynamoDbClient,
      TestUtils.kmsClient
    );
    KeyStorageInterface storage = StorageCheater.create(
      TestUtils.dynamoDbClient,
      TestUtils.TEST_KEYSTORE_NAME,
      TestUtils.TEST_LOGICAL_KEYSTORE_NAME
    );
    QueryForVersionsOutput versions = storage.QueryForVersions(
      QueryForVersionsInput
        .builder()
        .Identifier(branchKeyId)
        .pageSize(10)
        .build()
    );
    versions
      .items()
      .forEach(item ->
        TestUtils.deleteKeyStoreDdbItem(
          item.Identifier(),
          item.Type().HierarchicalSymmetricVersion().Version(),
          TestUtils.TEST_KEYSTORE_NAME,
          TestUtils.dynamoDbClient
        )
      );

    TestUtils.deleteKeyStoreDdbItem(
      branchKeyId,
      "branch:ACTIVE",
      TestUtils.TEST_KEYSTORE_NAME,
      TestUtils.dynamoDbClient
    );
    TestUtils.deleteKeyStoreDdbItem(
      branchKeyId,
      "beacon:ACTIVE",
      TestUtils.TEST_KEYSTORE_NAME,
      TestUtils.dynamoDbClient
    );
  }
}
