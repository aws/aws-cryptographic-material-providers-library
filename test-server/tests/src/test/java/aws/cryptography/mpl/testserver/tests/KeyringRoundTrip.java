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
 * The keyring round-trip: the load-bearing conformance assertion of the whole harness.
 *
 * <p>The MPL has no "encrypt this plaintext" operation to test. A keyring takes materials
 * in and hands materials back, so a round-trip is:
 *
 * <pre>
 *   InitializeEncryptionMaterials(suite, ec)   -&gt; materials with no data key
 *   OnEncrypt(keyring, materials)              -&gt; materials WITH a data key + EDKs
 *                                                 (the test carries EDKs + suite id)
 *   InitializeDecryptionMaterials(suite, ec)   -&gt; materials with no data key
 *   OnDecrypt(keyring, materials, EDKs)        -&gt; materials WITH a data key
 *   assert the two plaintext data keys are equal
 * </pre>
 *
 * <p><b>Nothing server-side links the two halves.</b> The encrypted data keys and the
 * algorithm suite identity travel back to the test and in again. That is deliberate: it is
 * exactly what will let the encrypt half go to one language server and the decrypt half to
 * another, with no change to this method.
 */
public final class KeyringRoundTrip {

    private KeyringRoundTrip() {
    }

    /** Create a MaterialProviders instance and return its handle. */
    public static String createMpl(MPLTestServerClient client) {
        return client.createMPL(CreateMPLInput.builder()
            .config(MaterialProvidersConfig.builder().build())
            .build()).getMplId();
    }

    /**
     * Drive a full round-trip and assert the data key survives it.
     *
     * @param encryptClient the client for the server performing the encrypt half.
     * @param decryptClient the client for the server performing the decrypt half. Today
     *     the same as {@code encryptClient}; a separate parameter so the cross-language
     *     matrix needs no change here.
     * @param encryptMplId a MaterialProviders handle on the encrypt server.
     * @param decryptMplId a MaterialProviders handle on the decrypt server.
     * @param encryptKeyringId the keyring to encrypt with.
     * @param decryptKeyringId the keyring to decrypt with. May differ from the encrypt
     *     keyring -- which is how multi-keyring composition is verified.
     * @param suite the algorithm suite to use.
     * @param encryptionContext the encryption context.
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
        EncryptionMaterials initialized = encryptClient.initializeEncryptionMaterials(
            InitializeEncryptionMaterialsInput.builder()
                .mplId(encryptMplId)
                .algorithmSuiteId(suite)
                .encryptionContext(encryptionContext)
                .requiredEncryptionContextKeys(List.of())
                .build()).getMaterials();

        // Freshly initialized materials must have no data key: if they arrived with one, the
        // round-trip below would prove nothing about the keyring.
        assertNull(initialized.getPlaintextDataKey(),
            "InitializeEncryptionMaterials must not produce a plaintext data key");
        assertTrue(initialized.getEncryptedDataKeys().isEmpty(),
            "InitializeEncryptionMaterials must not produce encrypted data keys");

        EncryptionMaterials encrypted = encryptClient.onEncrypt(OnEncryptInput.builder()
            .keyringId(encryptKeyringId)
            .materials(initialized)
            .build()).getMaterials();

        assertNotNull(encrypted.getPlaintextDataKey(),
            "OnEncrypt must produce a plaintext data key");
        List<EncryptedDataKey> edks = encrypted.getEncryptedDataKeys();
        assertFalse(edks.isEmpty(), "OnEncrypt must produce at least one encrypted data key");

        // --- decrypt half: only the EDKs and the suite identity cross over ---
        DecryptionMaterials toDecrypt = decryptClient.initializeDecryptionMaterials(
            InitializeDecryptionMaterialsInput.builder()
                .mplId(decryptMplId)
                .algorithmSuiteId(suite)
                .encryptionContext(encryptionContext)
                .requiredEncryptionContextKeys(List.of())
                .build()).getMaterials();

        assertNull(toDecrypt.getPlaintextDataKey(),
            "InitializeDecryptionMaterials must not produce a plaintext data key");

        DecryptionMaterials decrypted = decryptClient.onDecrypt(OnDecryptInput.builder()
            .keyringId(decryptKeyringId)
            .materials(toDecrypt)
            .encryptedDataKeys(edks)
            .build()).getMaterials();

        assertNotNull(decrypted.getPlaintextDataKey(),
            "OnDecrypt must produce a plaintext data key");

        // The assertion the whole harness exists to make.
        assertEquals(
            hex(encrypted.getPlaintextDataKey()),
            hex(decrypted.getPlaintextDataKey()),
            "the data key recovered by OnDecrypt must equal the one OnEncrypt generated");
    }

    /**
     * Render a buffer as hex.
     *
     * <p>Compared as hex rather than by {@code ByteBuffer.equals} so a failure message shows
     * what actually differed, and so a buffer whose position has been advanced does not
     * compare unequal to an identical one that has not.
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
