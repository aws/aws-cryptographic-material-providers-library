package aws.cryptography.mpl.testserver.tests;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertNull;
import static org.junit.jupiter.api.Assertions.assertTrue;

import aws.cryptography.mpl.testserver.client.client.MPLTestServerClient;
import aws.cryptography.mpl.testserver.client.model.AlgorithmSuiteId;
import aws.cryptography.mpl.testserver.client.model.CreateMPLInput;
import aws.cryptography.mpl.testserver.client.model.DecryptionMaterials;
import aws.cryptography.mpl.testserver.client.model.EncryptedDataKey;
import aws.cryptography.mpl.testserver.client.model.EncryptionMaterials;
import aws.cryptography.mpl.testserver.client.model.InitializeDecryptionMaterialsInput;
import aws.cryptography.mpl.testserver.client.model.InitializeEncryptionMaterialsInput;
import aws.cryptography.mpl.testserver.client.model.MaterialProvidersConfig;
import aws.cryptography.mpl.testserver.client.model.OnDecryptInput;
import aws.cryptography.mpl.testserver.client.model.OnEncryptInput;
import java.nio.ByteBuffer;
import java.util.List;
import java.util.Map;

/**
 * The keyring round-trip: the core conformance assertion of the harness.
 *
 * <p>The MPL has no "encrypt this plaintext" operation. A keyring takes materials in
 * and hands materials back, so a round-trip is:
 *
 * <pre>
 *   InitializeEncryptionMaterials(suite, ec)   -&gt; materials, no data key
 *   OnEncrypt(keyring, materials)              -&gt; materials WITH data key + EDKs
 *   InitializeDecryptionMaterials(suite, ec)   -&gt; materials, no data key
 *   OnDecrypt(keyring, materials, EDKs)        -&gt; materials WITH data key
 *   assert the two plaintext data keys are equal
 * </pre>
 *
 * <p>Nothing server-side links the two halves -- the EDKs and suite identity travel
 * back to the test and in again. This is what lets the encrypt and decrypt halves go
 * to different servers later with no change to this method.
 */
public final class KeyringRoundTrip {

  private KeyringRoundTrip() {}

  /** Create a MaterialProviders instance and return its handle. */
  public static String createMpl(MPLTestServerClient client) {
    return client
      .createMPL(
        CreateMPLInput
          .builder()
          .config(MaterialProvidersConfig.builder().build())
          .build()
      )
      .getMplId();
  }

  /**
   * Drive a full round-trip and assert the data key survives it.
   *
   * @param encryptClient the client for the encrypt half.
   * @param decryptClient the client for the decrypt half -- separate parameter so
   *     the cross-language matrix needs no change here.
   * @param encryptKeyringId the keyring to encrypt with.
   * @param decryptKeyringId the keyring to decrypt with -- may differ, which is how
   *     multi-keyring composition is verified.
   */
  public static void assertRoundTrips(
    MPLTestServerClient encryptClient,
    MPLTestServerClient decryptClient,
    String encryptMplId,
    String decryptMplId,
    String encryptKeyringId,
    String decryptKeyringId,
    AlgorithmSuiteId suite,
    Map<String, String> encryptionContext
  ) {
    // --- encrypt half ---
    EncryptionMaterials initialized = encryptClient
      .initializeEncryptionMaterials(
        InitializeEncryptionMaterialsInput
          .builder()
          .mplId(encryptMplId)
          .algorithmSuiteId(suite)
          .encryptionContext(encryptionContext)
          .requiredEncryptionContextKeys(List.of())
          .build()
      )
      .getMaterials();

    assertNull(
      initialized.getPlaintextDataKey(),
      "InitializeEncryptionMaterials must not produce a plaintext data key"
    );
    assertTrue(
      initialized.getEncryptedDataKeys().isEmpty(),
      "InitializeEncryptionMaterials must not produce encrypted data keys"
    );

    EncryptionMaterials encrypted = encryptClient
      .onEncrypt(
        OnEncryptInput
          .builder()
          .keyringId(encryptKeyringId)
          .materials(initialized)
          .build()
      )
      .getMaterials();

    assertNotNull(
      encrypted.getPlaintextDataKey(),
      "OnEncrypt must produce a plaintext data key"
    );
    List<EncryptedDataKey> edks = encrypted.getEncryptedDataKeys();
    assertFalse(
      edks.isEmpty(),
      "OnEncrypt must produce at least one encrypted data key"
    );

    // --- decrypt half: only the EDKs and the suite identity cross over ---
    DecryptionMaterials toDecrypt = decryptClient
      .initializeDecryptionMaterials(
        InitializeDecryptionMaterialsInput
          .builder()
          .mplId(decryptMplId)
          .algorithmSuiteId(suite)
          .encryptionContext(encryptionContext)
          .requiredEncryptionContextKeys(List.of())
          .build()
      )
      .getMaterials();

    assertNull(
      toDecrypt.getPlaintextDataKey(),
      "InitializeDecryptionMaterials must not produce a plaintext data key"
    );

    DecryptionMaterials decrypted = decryptClient
      .onDecrypt(
        OnDecryptInput
          .builder()
          .keyringId(decryptKeyringId)
          .materials(toDecrypt)
          .encryptedDataKeys(edks)
          .build()
      )
      .getMaterials();

    assertNotNull(
      decrypted.getPlaintextDataKey(),
      "OnDecrypt must produce a plaintext data key"
    );

    assertEquals(
      hex(encrypted.getPlaintextDataKey()),
      hex(decrypted.getPlaintextDataKey()),
      "the data key recovered by OnDecrypt must equal the one OnEncrypt generated"
    );
  }

  /**
   * Render a buffer as hex so failure messages show what differed and a buffer
   * whose position has advanced does not compare unequal to an identical one.
   */
  public static String hex(ByteBuffer buffer) {
    if (buffer == null) {
      return "<absent>";
    }
    ByteBuffer readOnly = buffer.asReadOnlyBuffer();
    StringBuilder out = new StringBuilder(readOnly.remaining() * 2);
    while (readOnly.hasRemaining()) {
      out.append(String.format("%02x", readOnly.get()));
    }
    return out.toString();
  }
}
