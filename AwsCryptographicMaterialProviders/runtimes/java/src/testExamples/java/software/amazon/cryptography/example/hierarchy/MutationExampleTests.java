// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
package software.amazon.cryptography.example.hierarchy;

import org.testng.annotations.Test;

import software.amazon.cryptography.example.TestUtils;

public class MutationExampleTests {
  @Test
  public void testMutationExample() {
    MutationExample.End2End(
      TestUtils.TEST_KEYSTORE_NAME,
      TestUtils.TEST_LOGICAL_KEYSTORE_NAME,
      TestUtils.KEYSTORE_KMS_ARN,
      TestUtils.POSTAL_HORN_KEY_ARN,
      TestUtils.dynamoDbClient,
      TestUtils.kmsClient
    );
  }
}
