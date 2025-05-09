// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
package software.amazon.cryptography.example.hierarchy.mutations;

import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

import org.mockito.MockitoAnnotations;
import org.testng.Assert;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
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

  private static KeyStoreAdmin admin;
  private static String hv1BranchKeyId;
  private static String hv2BranchKeyId;

  @BeforeClass
  public static void setUp() {
    MockitoAnnotations.initMocks(KmsMutationExceptionTest.class);
    admin = AdminProvider.admin();
    String uuid = java.util.UUID.randomUUID().toString();
    hv1BranchKeyId = "mocked-kms-client-hv-1-" + uuid;
    hv2BranchKeyId = "mocked-kms-client-hv-2-" + uuid;

    // Create Branch Key with hierarchy-version-1 once for all tests
    CreateKeyExample.CreateKey(
      Fixtures.KEYSTORE_KMS_ARN,
      hv1BranchKeyId,
      admin,
      HierarchyVersion.v1
    );

    // Create Branch Key with hierarchy-version-2 once for all tests
    CreateKeyExample.CreateKey(
      Fixtures.KEYSTORE_KMS_ARN,
      hv2BranchKeyId,
      admin,
      HierarchyVersion.v2
    );
  }

  private InitializeMutationInput createMutationInput(
    String branchKeyId,
    KeyManagementStrategy strategy
  ) {
    return InitializeMutationInput
      .builder()
      .Mutations(
        Mutations.builder().TerminalKmsArn(Fixtures.POSTAL_HORN_KEY_ARN).build()
      )
      .Identifier(branchKeyId)
      .Strategy(strategy)
      .SystemKey(
        SystemKey.builder().trustStorage(TrustStorage.builder().build()).build()
      )
      .DoNotVersion(true)
      .build();
  }

  @Test
  public void testOriginalKeyDisabledException() {
    DisabledException exception = DisabledException
      .builder()
      .message(
        String.format("Key '%s' is disabled.", Fixtures.KEYSTORE_KMS_ARN)
      )
      .build();

    KmsClient mockKmsClient = mock(KmsClient.class);
    when(mockKmsClient.reEncrypt(any(ReEncryptRequest.class)))
      .thenThrow(exception);
    when(mockKmsClient.decrypt(any(DecryptRequest.class))).thenThrow(exception);

    // DecryptEncrypt Strategy with Mocked KmsClient only for Encrypt Client
    KeyManagementStrategy decryptEncrypt = AdminProvider.decryptEncryptStrategy(
      mockKmsClient,
      KmsClient.create()
    );

    // Expect exception for HV1 Branch Keys
    Assert.expectThrows(
      MutationFromException.class,
      () ->
        admin.InitializeMutation(
          createMutationInput(hv1BranchKeyId, decryptEncrypt)
        )
    );

    // Expect exception for HV2 Branch Keys
    Assert.expectThrows(
      MutationFromException.class,
      () ->
        admin.InitializeMutation(
          createMutationInput(hv2BranchKeyId, decryptEncrypt)
        )
    );
  }

  @Test
  public void testTerminalKeyDisabledException() {
    DisabledException exception = DisabledException
      .builder()
      .message(
        String.format("Key '%s' is disabled.", Fixtures.POSTAL_HORN_KEY_ARN)
      )
      .build();

    KmsClient mockKmsClient = mock(KmsClient.class);
    when(mockKmsClient.reEncrypt(any(ReEncryptRequest.class)))
      .thenThrow(exception);
    when(mockKmsClient.encrypt(any(EncryptRequest.class))).thenThrow(exception);

    // Decrypt/Encrypt Strategy
    KeyManagementStrategy decryptEncrypt = AdminProvider.decryptEncryptStrategy(
      KmsClient.create(),
      mockKmsClient
    );

    // Expect exception for HV1 Branch Keys
    Assert.expectThrows(
      MutationToException.class,
      () ->
        admin.InitializeMutation(
          createMutationInput(hv1BranchKeyId, decryptEncrypt)
        )
    );

    // Expect exception for HV2 Branch Keys
    Assert.expectThrows(
      MutationToException.class,
      () ->
        admin.InitializeMutation(
          createMutationInput(hv2BranchKeyId, decryptEncrypt)
        )
    );
  }

  @Test
  public void testOriginalKeyPendingDeletionException() {
    KmsInvalidStateException exception = KmsInvalidStateException
      .builder()
      .message(
        String.format(
          "Key '%s' is pending deletion.",
          Fixtures.KEYSTORE_KMS_ARN
        )
      )
      .build();

    KmsClient mockKmsClient = mock(KmsClient.class);
    when(mockKmsClient.reEncrypt(any(ReEncryptRequest.class)))
      .thenThrow(exception);
    when(mockKmsClient.decrypt(any(DecryptRequest.class))).thenThrow(exception);

    // Decrypt/Encrypt Strategy
    KeyManagementStrategy decryptEncrypt = AdminProvider.decryptEncryptStrategy(
      mockKmsClient,
      KmsClient.create()
    );

    // Expect exception for HV1 Branch Keys
    Assert.expectThrows(
      MutationFromException.class,
      () ->
        admin.InitializeMutation(
          createMutationInput(hv1BranchKeyId, decryptEncrypt)
        )
    );

    // Expect exception for HV2 Branch Keys
    Assert.expectThrows(
      MutationFromException.class,
      () ->
        admin.InitializeMutation(
          createMutationInput(hv2BranchKeyId, decryptEncrypt)
        )
    );
  }

  @Test
  public void testTerminalKeyPendingDeletionException() {
    KmsInvalidStateException exception = KmsInvalidStateException
      .builder()
      .message(
        String.format(
          "Key '%s' is pending deletion.",
          Fixtures.POSTAL_HORN_KEY_ARN
        )
      )
      .build();

    KmsClient mockKmsClient = mock(KmsClient.class);
    when(mockKmsClient.reEncrypt(any(ReEncryptRequest.class)))
      .thenThrow(exception);
    when(mockKmsClient.encrypt(any(EncryptRequest.class))).thenThrow(exception);

    KeyManagementStrategy decryptEncrypt = AdminProvider.decryptEncryptStrategy(
      KmsClient.create(),
      mockKmsClient
    );

    // Expect exception for HV1 Branch Keys
    Assert.expectThrows(
      MutationToException.class,
      () ->
        admin.InitializeMutation(
          createMutationInput(hv1BranchKeyId, decryptEncrypt)
        )
    );

    // Expect exception for HV2 Branch Keys
    Assert.expectThrows(
      MutationToException.class,
      () ->
        admin.InitializeMutation(
          createMutationInput(hv2BranchKeyId, decryptEncrypt)
        )
    );
  }

  @AfterClass
  public static void tearDown() {
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
