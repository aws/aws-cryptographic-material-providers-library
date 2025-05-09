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
    // Test case: Original KMS key (used for decryption) is disabled
    // Creates a DisabledException with the original keystore KMS ARN
    DisabledException exception = DisabledException
      .builder()
      .message(
        String.format("Key '%s' is disabled.", Fixtures.KEYSTORE_KMS_ARN)
      )
      .build();

    // Mock KMS client to throw DisabledException during decrypt and reEncrypt operations
    // This simulates the original key being disabled
    KmsClient mockKmsClient = mock(KmsClient.class);
    when(mockKmsClient.reEncrypt(any(ReEncryptRequest.class)))
      .thenThrow(exception);
    when(mockKmsClient.decrypt(any(DecryptRequest.class))).thenThrow(exception);

    // Create DecryptEncrypt strategy where:
    // - Decrypt use the mocked client (simulating disabled original key)
    // - Encrypt use a regular client
    KeyManagementStrategy decryptEncrypt = AdminProvider.decryptEncryptStrategy(
      mockKmsClient,
      KmsClient.create()
    );

    // Initializing mutation with disabled original key throws MutationFromException
    // for both hierarchy version branch keys
    MutationFromException hv1Exception = Assert.expectThrows(
      MutationFromException.class, // Exception expected when original (FROM) key fails
      () ->
        admin.InitializeMutation(
          createMutationInput(hv1BranchKeyId, decryptEncrypt)
        )
    );
    Assert.assertTrue(
      hv1Exception
        .getMessage()
        .contains("Key '" + Fixtures.KEYSTORE_KMS_ARN + "' is disabled"),
      "Exception message should contain the disabled key information"
    );

    MutationFromException hv2Exception = Assert.expectThrows(
      MutationFromException.class,
      () ->
        admin.InitializeMutation(
          createMutationInput(hv2BranchKeyId, decryptEncrypt)
        )
    );
    Assert.assertTrue(
      hv2Exception
        .getMessage()
        .contains("Key '" + Fixtures.KEYSTORE_KMS_ARN + "' is disabled"),
      "Exception message should contain the disabled key information"
    );
  }

  @Test
  public void testTerminalKeyDisabledException() {
    // Test case: Terminal KMS key (used for encryption) is disabled
    // Creates a DisabledException with the terminal (destination) KMS ARN
    DisabledException exception = DisabledException
      .builder()
      .message(
        String.format("Key '%s' is disabled.", Fixtures.POSTAL_HORN_KEY_ARN)
      )
      .build();

    // Mock KMS client to throw DisabledException during encrypt and reEncrypt operations
    // This simulates the terminal key being disabled
    KmsClient mockKmsClient = mock(KmsClient.class);
    when(mockKmsClient.reEncrypt(any(ReEncryptRequest.class)))
      .thenThrow(exception);
    when(mockKmsClient.encrypt(any(EncryptRequest.class))).thenThrow(exception);

    // Create DecryptEncrypt strategy where:
    // - Decrypt use regular client
    // - Encrypt use the mocked client (simulating disabled terminal key)
    KeyManagementStrategy decryptEncrypt = AdminProvider.decryptEncryptStrategy(
      KmsClient.create(),
      mockKmsClient
    );

    // Initializing mutation with disabled terminal key throws MutationToException
    // for both hierarchy version branch keys
    MutationToException hv1Exception = Assert.expectThrows(
      MutationToException.class, // Exception expected when terminal (TO) key fails
      () ->
        admin.InitializeMutation(
          createMutationInput(hv1BranchKeyId, decryptEncrypt)
        )
    );
    Assert.assertTrue(
      hv1Exception
        .getMessage()
        .contains("Key '" + Fixtures.POSTAL_HORN_KEY_ARN + "' is disabled"),
      "Exception message should contain the disabled key information"
    );

    MutationToException hv2Exception = Assert.expectThrows(
      MutationToException.class,
      () ->
        admin.InitializeMutation(
          createMutationInput(hv2BranchKeyId, decryptEncrypt)
        )
    );
    Assert.assertTrue(
      hv2Exception
        .getMessage()
        .contains("Key '" + Fixtures.POSTAL_HORN_KEY_ARN + "' is disabled"),
      "Exception message should contain the disabled key information"
    );
  }

  @Test
  public void testOriginalKeyPendingDeletionException() {
    // Test case: Original KMS key (used for decryption) is pending deletion
    // Creates a KmsInvalidStateException with the original keystore KMS ARN
    KmsInvalidStateException exception = KmsInvalidStateException
      .builder()
      .message(
        String.format(
          "Key '%s' is pending deletion.",
          Fixtures.KEYSTORE_KMS_ARN
        )
      )
      .build();

    // Mock KMS client to throw KmsInvalidStateException during decrypt and reEncrypt operations
    // This simulates the original key being in pending deletion state
    KmsClient mockKmsClient = mock(KmsClient.class);
    when(mockKmsClient.reEncrypt(any(ReEncryptRequest.class)))
      .thenThrow(exception);
    when(mockKmsClient.decrypt(any(DecryptRequest.class))).thenThrow(exception);

    // Create DecryptEncrypt strategy where:
    // - Decrypt use the mocked client (simulating original key pending deletion)
    // - Encrypt use a regular client
    KeyManagementStrategy decryptEncrypt = AdminProvider.decryptEncryptStrategy(
      mockKmsClient,
      KmsClient.create()
    );

    // Initializing mutation with original key pending deletion throws MutationFromException
    // for both hierarchy version branch keys
    MutationFromException hv1Exception = Assert.expectThrows(
      MutationFromException.class, // Exception expected when original (FROM) key fails
      () ->
        admin.InitializeMutation(
          createMutationInput(hv1BranchKeyId, decryptEncrypt)
        )
    );
    Assert.assertTrue(
      hv1Exception
        .getMessage()
        .contains(
          "Key '" + Fixtures.KEYSTORE_KMS_ARN + "' is pending deletion"
        ),
      "Exception message should contain the pending deletion key information"
    );

    MutationFromException hv2Exception = Assert.expectThrows(
      MutationFromException.class,
      () ->
        admin.InitializeMutation(
          createMutationInput(hv2BranchKeyId, decryptEncrypt)
        )
    );
    Assert.assertTrue(
      hv2Exception
        .getMessage()
        .contains(
          "Key '" + Fixtures.KEYSTORE_KMS_ARN + "' is pending deletion"
        ),
      "Exception message should contain the pending deletion key information"
    );
  }

  @Test
  public void testTerminalKeyPendingDeletionException() {
    // Test case: Terminal KMS key (used for encryption) is pending deletion
    // Creates a KmsInvalidStateException with the terminal (destination) KMS ARN
    KmsInvalidStateException exception = KmsInvalidStateException
      .builder()
      .message(
        String.format(
          "Key '%s' is pending deletion.",
          Fixtures.POSTAL_HORN_KEY_ARN
        )
      )
      .build();

    // Mock KMS client to throw KmsInvalidStateException during encrypt and reEncrypt operations
    // This simulates the terminal key being in pending deletion state
    KmsClient mockKmsClient = mock(KmsClient.class);
    when(mockKmsClient.reEncrypt(any(ReEncryptRequest.class)))
      .thenThrow(exception);
    when(mockKmsClient.encrypt(any(EncryptRequest.class))).thenThrow(exception);

    // Create DecryptEncrypt strategy where:
    // - Decrypt use regular client
    // - Encrypt use the mocked client (simulating terminal key pending deletion)
    KeyManagementStrategy decryptEncrypt = AdminProvider.decryptEncryptStrategy(
      KmsClient.create(),
      mockKmsClient
    );

    // Initializing mutation with terminal key pending deletion throws MutationToException
    // for both hierarchy version branch keys
    MutationToException hv1Exception = Assert.expectThrows(
      MutationToException.class, // Exception expected when terminal (TO) key fails
      () ->
        admin.InitializeMutation(
          createMutationInput(hv1BranchKeyId, decryptEncrypt)
        )
    );
    Assert.assertTrue(
      hv1Exception
        .getMessage()
        .contains(
          "Key '" + Fixtures.POSTAL_HORN_KEY_ARN + "' is pending deletion"
        ),
      "Exception message should contain the pending deletion key information"
    );

    MutationToException hv2Exception = Assert.expectThrows(
      MutationToException.class,
      () ->
        admin.InitializeMutation(
          createMutationInput(hv2BranchKeyId, decryptEncrypt)
        )
    );
    Assert.assertTrue(
      hv2Exception
        .getMessage()
        .contains(
          "Key '" + Fixtures.POSTAL_HORN_KEY_ARN + "' is pending deletion"
        ),
      "Exception message should contain the pending deletion key information"
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
