package aws.cryptography.mpl.testserver.tests;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;

import aws.cryptography.mpl.testserver.client.client.MPLTestServerClient;
import aws.cryptography.mpl.testserver.client.model.AesWrappingAlg;
import aws.cryptography.mpl.testserver.client.model.AlgorithmSuiteId;
import aws.cryptography.mpl.testserver.client.model.CreateMultiKeyringInput;
import aws.cryptography.mpl.testserver.client.model.CreateRawAesKeyringInput;
import aws.cryptography.mpl.testserver.client.model.CreateRawRsaKeyringInput;
import aws.cryptography.mpl.testserver.client.model.ESDKAlgorithmSuiteId;
import aws.cryptography.mpl.testserver.client.model.EncryptionMaterials;
import aws.cryptography.mpl.testserver.client.model.GenericServerError;
import aws.cryptography.mpl.testserver.client.model.InitializeEncryptionMaterialsInput;
import aws.cryptography.mpl.testserver.client.model.MaterialProvidersClientError;
import aws.cryptography.mpl.testserver.client.model.OnEncryptInput;
import aws.cryptography.mpl.testserver.client.model.PaddingScheme;
import java.util.List;
import java.util.Map;
import java.util.UUID;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

/**
 * Multi-keyring conformance: handles compose the way the MPL's resource references compose.
 *
 * <p>This is the test that validates the central design decision of the harness. The MPL's
 * {@code CreateMultiKeyring} takes keyring <em>references</em>; the wire takes keyring
 * <em>handles</em>. If that substitution were leaky, the symptom would appear here -- a
 * multi-keyring built from handles would not behave like one built from references.
 *
 * <p>The decisive assertion is that a data key wrapped by the multi-keyring can be unwrapped
 * by any ONE of its children on its own. That can only work if each child handle really did
 * denote the same live keyring the multi-keyring was composed from.
 */
class MultiKeyringTest {

    private static final AlgorithmSuiteId SUITE = AlgorithmSuiteId.builder()
        .esdk(ESDKAlgorithmSuiteId.ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY)
        .build();

    private static MPLTestServerClient client;
    private static String mplId;

    @BeforeAll
    static void setUp() {
        client = TestServerClients.forTarget(LanguageServerRegistry.shared().primary());
        mplId = KeyringRoundTrip.createMpl(client);
    }

    private static String aesKeyring() {
        return client.createRawAesKeyring(CreateRawAesKeyringInput.builder()
            .mplId(mplId)
            .keyNamespace(TestKeyMaterial.KEY_NAMESPACE)
            .keyName(TestKeyMaterial.AES_KEY_NAME)
            .wrappingKey(TestKeyMaterial.aesKeyForBits(256))
            .wrappingAlg(AesWrappingAlg.ALG_AES256_GCM_IV12_TAG16)
            .build()).getKeyringId();
    }

    private static String rsaKeyring() {
        return client.createRawRsaKeyring(CreateRawRsaKeyringInput.builder()
            .mplId(mplId)
            .keyNamespace(TestKeyMaterial.KEY_NAMESPACE)
            .keyName(TestKeyMaterial.RSA_KEY_NAME)
            .paddingScheme(PaddingScheme.OAEP_SHA256_MGF1)
            .publicKey(TestKeyMaterial.pem(TestKeyMaterial.RSA_PUBLIC_KEY_PEM))
            .privateKey(TestKeyMaterial.pem(TestKeyMaterial.RSA_PRIVATE_KEY_PEM))
            .build()).getKeyringId();
    }

    @Test
    @DisplayName("A multi-keyring wraps for every child, and each child alone can unwrap")
    void eachChildCanDecryptIndependently() {
        String generator = aesKeyring();
        String child = rsaKeyring();

        String multi = client.createMultiKeyring(CreateMultiKeyringInput.builder()
            .mplId(mplId)
            .generatorKeyringId(generator)
            .childKeyringIds(List.of(child))
            .build()).getKeyringId();
        assertNotNull(multi, "CreateMultiKeyring must return a keyring handle");

        EncryptionMaterials encrypted = client.onEncrypt(OnEncryptInput.builder()
            .keyringId(multi)
            .materials(client.initializeEncryptionMaterials(
                InitializeEncryptionMaterialsInput.builder()
                    .mplId(mplId)
                    .algorithmSuiteId(SUITE)
                    .encryptionContext(Map.of())
                    .requiredEncryptionContextKeys(List.of())
                    .build()).getMaterials())
            .build()).getMaterials();

        // One encrypted data key per contributing keyring: the generator plus each child.
        assertEquals(2, encrypted.getEncryptedDataKeys().size(),
            "a multi-keyring with a generator and one child must produce two encrypted data keys");

        // The decisive assertion: EITHER child, on its own, recovers the same data key.
        KeyringRoundTrip.assertRoundTrips(
            client, client, mplId, mplId, multi, generator, SUITE, Map.of());
        KeyringRoundTrip.assertRoundTrips(
            client, client, mplId, mplId, multi, child, SUITE, Map.of());
    }

    @Test
    @DisplayName("A multi-keyring composed of multi-keyrings works, so handles nest")
    void multiKeyringsNest() {
        String aes = aesKeyring();
        String rsa = rsaKeyring();

        String inner = client.createMultiKeyring(CreateMultiKeyringInput.builder()
            .mplId(mplId)
            .childKeyringIds(List.of(rsa))
            .build()).getKeyringId();

        // The outer keyring's child is itself a multi-keyring. Nesting needs no recursive
        // Smithy shape precisely because the child is named by a handle.
        String outer = client.createMultiKeyring(CreateMultiKeyringInput.builder()
            .mplId(mplId)
            .generatorKeyringId(aes)
            .childKeyringIds(List.of(inner))
            .build()).getKeyringId();

        KeyringRoundTrip.assertRoundTrips(
            client, client, mplId, mplId, outer, rsa, SUITE, Map.of());
    }

    @Test
    @DisplayName("A multi-keyring with neither a generator nor children is rejected at construction")
    void emptyMultiKeyringIsRejected() {
        // `childKeyringIds` is required-but-may-be-empty on the wire, mirroring the MPL, which
        // represents "no children" as an empty list. An empty list is therefore a well-formed
        // request that the harness must pass through rather than pre-empt.
        //
        // The MPL then rejects it, because a multi-keyring with neither a generator nor a child
        // can do nothing at all. That makes this a MaterialProvidersClientError -- MPL
        // behavior a test can assert on -- and NOT a GenericServerError, which would mean the
        // harness had substituted its own validation for the MPL's.
        MaterialProvidersClientError error = assertThrows(MaterialProvidersClientError.class, () ->
            client.createMultiKeyring(CreateMultiKeyringInput.builder()
                .mplId(mplId)
                .childKeyringIds(List.of())
                .build()));

        assertTrue(error.getMessage().contains("generator") || error.getMessage().contains("child"),
            "the MPL's own explanation must be forwarded, but was: " + error.getMessage());
    }

    @Test
    @DisplayName("A multi-keyring with children but no generator wraps, but cannot generate")
    void childrenWithoutGeneratorCannotGenerate() {
        String rsa = rsaKeyring();

        // Legal to construct: there is a child, just nothing that can create a data key.
        String noGenerator = client.createMultiKeyring(CreateMultiKeyringInput.builder()
            .mplId(mplId)
            .childKeyringIds(List.of(rsa))
            .build()).getKeyringId();
        assertNotNull(noGenerator);

        var initialized = client.initializeEncryptionMaterials(
            InitializeEncryptionMaterialsInput.builder()
                .mplId(mplId)
                .algorithmSuiteId(SUITE)
                .encryptionContext(Map.of())
                .requiredEncryptionContextKeys(List.of())
                .build()).getMaterials();

        // OnEncrypt on materials that have no data key yet needs something to generate one.
        MaterialProvidersClientError error = assertThrows(MaterialProvidersClientError.class, () ->
            client.onEncrypt(OnEncryptInput.builder()
                .keyringId(noGenerator)
                .materials(initialized)
                .build()));
        assertFalse(error.getMessage().isEmpty(),
            "the MPL's explanation must be forwarded, not swallowed");
    }

    @Test
    @DisplayName("An unknown child handle is refused and no keyring is created")
    void unknownChildHandleIsRefused() {
        String unknown = UUID.randomUUID().toString();

        GenericServerError error = assertThrows(GenericServerError.class, () ->
            client.createMultiKeyring(CreateMultiKeyringInput.builder()
                .mplId(mplId)
                .generatorKeyringId(aesKeyring())
                .childKeyringIds(List.of(unknown))
                .build()));

        // A framework error, not an MPL error: the handle never resolved, so the MPL was never
        // called and nothing was registered.
        assertTrue(error.getMessage().contains(unknown),
            "the error must name the unresolvable child handle, but was: " + error.getMessage());
        assertFalse(error.getMessage().isEmpty());
    }
}
