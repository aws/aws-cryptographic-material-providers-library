// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
package software.amazon.cryptography.example.hierarchy.mutations;

import static org.mockito.ArgumentMatchers.any;

import org.mockito.Mockito;
import org.testng.Assert;
import org.testng.annotations.Test;
import software.amazon.awssdk.services.kms.KmsClient;
import software.amazon.awssdk.services.kms.model.*;
import software.amazon.cryptography.example.DdbHelper;
import software.amazon.cryptography.example.Fixtures;
import software.amazon.cryptography.example.hierarchy.AdminProvider;
import software.amazon.cryptography.example.hierarchy.CreateKeyExample;
import software.amazon.cryptography.keystore.model.HierarchyVersion;
import software.amazon.cryptography.keystoreadmin.KeyStoreAdmin;
import software.amazon.cryptography.keystoreadmin.model.*;

public class KmsMutationExceptionTest {

  /**
   * Helper method to create a KMS client that throws exceptions for specific KMS ARNs.
   */
  private KmsClient createMockKmsClientWithException(
    String kmsArn,
    String exceptionMessage
  ) {
    // Create the exception
    DisabledException exception = DisabledException
      .builder()
      .message(exceptionMessage)
      .build();

    // Create a real KMS client to delegate to for normal operations
    KmsClient realKmsClient = KmsClient.create();

    // Create a spy on the real client (this will use real behavior by default)
    KmsClient spyKmsClient = Mockito.spy(realKmsClient);

    // Configure for all operations that might use the target KMS ARN
    // For decrypt operations
    Mockito
      .doAnswer(invocation -> {
        DecryptRequest request = invocation.getArgument(0);
        if (request.keyId() != null && request.keyId().equals(kmsArn)) {
          throw exception;
        }
        return invocation.callRealMethod();
      })
      .when(spyKmsClient)
      .decrypt(any(DecryptRequest.class));

    // For encrypt operations
    Mockito
      .doAnswer(invocation -> {
        EncryptRequest request = invocation.getArgument(0);
        if (request.keyId().equals(kmsArn)) {
          throw exception;
        }
        return invocation.callRealMethod();
      })
      .when(spyKmsClient)
      .encrypt(any(EncryptRequest.class));

    // For reEncrypt operations - check both source and destination
    Mockito
      .doAnswer(invocation -> {
        ReEncryptRequest request = invocation.getArgument(0);
        // Check if either source or destination key matches the target ARN
        if (
          (request.sourceKeyId() != null &&
            request.sourceKeyId().equals(kmsArn)) ||
          request.destinationKeyId().equals(kmsArn)
        ) {
          throw exception;
        }
        return invocation.callRealMethod();
      })
      .when(spyKmsClient)
      .reEncrypt(any(ReEncryptRequest.class));

    // For generateDataKey operations
    Mockito
      .doAnswer(invocation -> {
        GenerateDataKeyRequest request = invocation.getArgument(0);
        if (request.keyId().equals(kmsArn)) {
          throw exception;
        }
        return invocation.callRealMethod();
      })
      .when(spyKmsClient)
      .generateDataKey(any(GenerateDataKeyRequest.class));

    // For generateDataKeyWithoutPlaintext operations
    Mockito
      .doAnswer(invocation -> {
        GenerateDataKeyWithoutPlaintextRequest request = invocation.getArgument(
          0
        );
        if (request.keyId().equals(kmsArn)) {
          throw exception;
        }
        return invocation.callRealMethod();
      })
      .when(spyKmsClient)
      .generateDataKeyWithoutPlaintext(
        any(GenerateDataKeyWithoutPlaintextRequest.class)
      );

    return spyKmsClient;
  }

  /**
   * Helper method to test a strategy with a disabled key.
   */
  private void testStrategyWithDisabledKey(
    KeyStoreAdmin admin,
    String branchKeyId,
    KeyManagementStrategy strategy,
    Class<? extends Exception> expectedExceptionClass,
    String disabledKmsArn,
    Mutations mutations
  ) {
    Exception exception = Assert.expectThrows(
      expectedExceptionClass,
      () ->
        admin.InitializeMutation(
          InitializeMutationInput
            .builder()
            .Mutations(mutations)
            .Identifier(branchKeyId)
            .Strategy(strategy)
            .SystemKey(
              SystemKey
                .builder()
                .trustStorage(TrustStorage.builder().build())
                .build()
            )
            .DoNotVersion(true)
            .build()
        )
    );
    Assert.assertTrue(
      exception
        .getMessage()
        .contains("Key '" + disabledKmsArn + "' is disabled"),
      "Exception message should contain the disabled key information"
    );
  }

  /**
   * Test original key disabled exception with all three strategies.
   * This comprehensive test verifies that all strategies handle a disabled original key correctly.
   */
  @Test
  public void testOriginalKeyDisabledWithAllStrategies() {
    // Create mock client that throws exception for original key
    final KmsClient mockClient = createMockKmsClientWithException(
      Fixtures.KEYSTORE_KMS_ARN,
      String.format("Key '%s' is disabled.", Fixtures.KEYSTORE_KMS_ARN)
    );

    // Create all three strategies
    final KeyManagementStrategy kmsSimple = AdminProvider.kmsSimpleStrategy(
      mockClient
    );
    final KeyManagementStrategy reEncrypt = AdminProvider.reEncryptStrategy(
      mockClient
    );
    final KeyManagementStrategy decryptEncrypt =
      AdminProvider.decryptEncryptStrategy(
        mockClient, // For decrypt operations (disabled original key)
        KmsClient.create() // For encrypt operations (normal terminal key)
      );

    final String uuid = java.util.UUID.randomUUID().toString();
    final String hv1BranchKeyId = "mocked-kms-client-hv-1-" + uuid;
    final String hv2BranchKeyId = "mocked-kms-client-hv-2-" + uuid;

    // Key Store Admin
    final KeyStoreAdmin admin = AdminProvider.admin();

    // Create Branch Keys
    CreateKeyExample.CreateKey(
      Fixtures.KEYSTORE_KMS_ARN,
      hv1BranchKeyId,
      admin,
      HierarchyVersion.v1,
      null
    );
    CreateKeyExample.CreateKey(
      Fixtures.KEYSTORE_KMS_ARN,
      hv2BranchKeyId,
      admin,
      HierarchyVersion.v2,
      null
    );

    // Mutation Request
    final Mutations mutations = Mutations
      .builder()
      .TerminalKmsArn(Fixtures.POSTAL_HORN_KEY_ARN)
      .build();

    // Test all strategies with HV1
    testStrategyWithDisabledKey(
      admin,
      hv1BranchKeyId,
      kmsSimple,
      MutationFromException.class,
      Fixtures.KEYSTORE_KMS_ARN,
      mutations
    );

    testStrategyWithDisabledKey(
      admin,
      hv1BranchKeyId,
      reEncrypt,
      MutationFromException.class,
      Fixtures.KEYSTORE_KMS_ARN,
      mutations
    );

    testStrategyWithDisabledKey(
      admin,
      hv1BranchKeyId,
      decryptEncrypt,
      MutationFromException.class,
      Fixtures.KEYSTORE_KMS_ARN,
      mutations
    );

    // Test supported strategies with HV2
    testStrategyWithDisabledKey(
      admin,
      hv2BranchKeyId,
      kmsSimple,
      MutationFromException.class,
      Fixtures.KEYSTORE_KMS_ARN,
      mutations
    );

    testStrategyWithDisabledKey(
      admin,
      hv2BranchKeyId,
      decryptEncrypt,
      MutationFromException.class,
      Fixtures.KEYSTORE_KMS_ARN,
      mutations
    );

    try {
      DdbHelper.DeleteBranchKey(
        hv1BranchKeyId,
        Fixtures.TEST_KEYSTORE_NAME,
        null
      );
    } catch (Exception e) {
      // ignore
    }
    try {
      DdbHelper.DeleteBranchKey(
        hv2BranchKeyId,
        Fixtures.TEST_KEYSTORE_NAME,
        null
      );
    } catch (Exception e) {
      //ignore
    }
  }

  /**
   * Test terminal key disabled exception with all three strategies.
   * This test verifies that all strategies handle a disabled terminal key correctly.
   */
  @Test
  public void testTerminalKeyDisabledWithAllStrategies() {
    // Create mock client that throws exception for terminal key
    final KmsClient mockClient = createMockKmsClientWithException(
      Fixtures.POSTAL_HORN_KEY_ARN,
      String.format("Key '%s' is disabled.", Fixtures.POSTAL_HORN_KEY_ARN)
    );

    // Create all three strategies
    final KeyManagementStrategy kmsSimple = AdminProvider.kmsSimpleStrategy(
      mockClient
    );
    final KeyManagementStrategy reEncrypt = AdminProvider.reEncryptStrategy(
      mockClient
    );
    final KeyManagementStrategy decryptEncrypt =
      AdminProvider.decryptEncryptStrategy(
        KmsClient.create(), // For decrypt operations (normal original key)
        mockClient // For encrypt operations (disabled terminal key)
      );

    // Create Branch Keys
    final String uuid = java.util.UUID.randomUUID().toString();
    final String hv1BranchKeyId = "mocked-kms-client-hv-1-" + uuid;
    final String hv2BranchKeyId = "mocked-kms-client-hv-2-" + uuid;

    // Key Store Admin
    final KeyStoreAdmin admin = AdminProvider.admin();

    // Create Branch Keys
    CreateKeyExample.CreateKey(
      Fixtures.KEYSTORE_KMS_ARN,
      hv1BranchKeyId,
      admin,
      HierarchyVersion.v1,
      null
    );
    CreateKeyExample.CreateKey(
      Fixtures.KEYSTORE_KMS_ARN,
      hv2BranchKeyId,
      admin,
      HierarchyVersion.v2,
      null
    );

    // Mutation Request
    final Mutations mutations = Mutations
      .builder()
      .TerminalKmsArn(Fixtures.POSTAL_HORN_KEY_ARN)
      .build();

    // Test all strategies with HV1
    testStrategyWithDisabledKey(
      admin,
      hv1BranchKeyId,
      kmsSimple,
      MutationToException.class,
      Fixtures.POSTAL_HORN_KEY_ARN,
      mutations
    );

    testStrategyWithDisabledKey(
      admin,
      hv1BranchKeyId,
      reEncrypt,
      MutationToException.class,
      Fixtures.POSTAL_HORN_KEY_ARN,
      mutations
    );

    testStrategyWithDisabledKey(
      admin,
      hv1BranchKeyId,
      decryptEncrypt,
      MutationToException.class,
      Fixtures.POSTAL_HORN_KEY_ARN,
      mutations
    );

    // Test supported strategies with HV2
    testStrategyWithDisabledKey(
      admin,
      hv2BranchKeyId,
      kmsSimple,
      MutationToException.class,
      Fixtures.POSTAL_HORN_KEY_ARN,
      mutations
    );

    testStrategyWithDisabledKey(
      admin,
      hv2BranchKeyId,
      decryptEncrypt,
      MutationToException.class,
      Fixtures.POSTAL_HORN_KEY_ARN,
      mutations
    );
    // Note: We don't test ReEncrypt with HV2 as it's not supported

    try {
      DdbHelper.DeleteBranchKey(
        hv1BranchKeyId,
        Fixtures.TEST_KEYSTORE_NAME,
        null
      );
    } catch (Exception e) {
      // ignore
    }
    try {
      DdbHelper.DeleteBranchKey(
        hv2BranchKeyId,
        Fixtures.TEST_KEYSTORE_NAME,
        null
      );
    } catch (Exception e) {
      //ignore
    }
  }
}
