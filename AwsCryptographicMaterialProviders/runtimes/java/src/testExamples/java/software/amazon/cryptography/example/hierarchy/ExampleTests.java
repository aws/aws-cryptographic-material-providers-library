// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
package software.amazon.cryptography.example.hierarchy;

import org.testng.annotations.Test;
import software.amazon.cryptography.example.Fixtures;
import software.amazon.cryptography.keystore.KeyStorageInterface;
import software.amazon.cryptography.keystore.model.QueryForVersionsInput;
import software.amazon.cryptography.keystore.model.QueryForVersionsOutput;

public class ExampleTests {

  @Test
  public void End2EndTests() {
    String branchKeyId = CreateKeyExample.CreateKey(
      Fixtures.TEST_KEYSTORE_NAME,
      Fixtures.TEST_LOGICAL_KEYSTORE_NAME,
      Fixtures.KEYSTORE_KMS_ARN,
      Fixtures.dynamoDbClient
    );
    branchKeyId =
      MutationExample.End2End(
        Fixtures.TEST_KEYSTORE_NAME,
        Fixtures.TEST_LOGICAL_KEYSTORE_NAME,
        Fixtures.POSTAL_HORN_KEY_ARN,
        branchKeyId,
        Fixtures.dynamoDbClient,
        Fixtures.kmsClient
      );
    branchKeyId =
      VersionKeyExample.VersionKey(
        Fixtures.TEST_KEYSTORE_NAME,
        Fixtures.TEST_LOGICAL_KEYSTORE_NAME,
        Fixtures.POSTAL_HORN_KEY_ARN,
        branchKeyId,
        Fixtures.dynamoDbClient
      );
    KeyStorageInterface storage = StorageCheater.create(
      Fixtures.dynamoDbClient,
      Fixtures.TEST_KEYSTORE_NAME,
      Fixtures.TEST_LOGICAL_KEYSTORE_NAME
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
        Fixtures.deleteKeyStoreDdbItem(
          item.Identifier(),
          item.Type().HierarchicalSymmetricVersion().Version(),
          Fixtures.TEST_KEYSTORE_NAME,
          Fixtures.dynamoDbClient
        )
      );

    Fixtures.deleteKeyStoreDdbItem(
      branchKeyId,
      "branch:ACTIVE",
      Fixtures.TEST_KEYSTORE_NAME,
      Fixtures.dynamoDbClient
    );
    Fixtures.deleteKeyStoreDdbItem(
      branchKeyId,
      "beacon:ACTIVE",
      Fixtures.TEST_KEYSTORE_NAME,
      Fixtures.dynamoDbClient
    );
  }
}
