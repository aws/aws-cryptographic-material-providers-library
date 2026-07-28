package aws.cryptography.mpl.testserver.tests.meta;

import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;

import aws.cryptography.mpl.testserver.client.client.MPLTestServerClient;
import aws.cryptography.mpl.testserver.client.model.AesWrappingAlg;
import aws.cryptography.mpl.testserver.client.model.AlgorithmSuiteId;
import aws.cryptography.mpl.testserver.client.model.CreateMPLInput;
import aws.cryptography.mpl.testserver.client.model.CreateRawAesKeyringInput;
import aws.cryptography.mpl.testserver.client.model.ESDKAlgorithmSuiteId;
import aws.cryptography.mpl.testserver.client.model.GenericServerError;
import aws.cryptography.mpl.testserver.client.model.InitializeEncryptionMaterialsInput;
import aws.cryptography.mpl.testserver.client.model.MaterialProvidersConfig;
import aws.cryptography.mpl.testserver.client.model.OnEncryptInput;
import aws.cryptography.mpl.testserver.tests.LanguageServerRegistry;
import aws.cryptography.mpl.testserver.tests.TestKeyMaterial;
import aws.cryptography.mpl.testserver.tests.TestServerClients;
import java.util.List;
import java.util.Map;
import java.util.UUID;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import software.amazon.smithy.java.framework.model.ValidationException;

/**
 * Every way a resource handle can be wrong must yield a {@code GenericServerError} -- never an
 * MPL error, and never a bodyless HTTP failure (Requirement 3.10).
 *
 * <p>Why this is a meta test and not a conformance test: a bad handle is a fault in how the
 * TEST called the harness, so it must be reported as a framework failure. If one of these
 * surfaced as a {@code MaterialProvidersClientError} instead, a test author would go looking
 * for a bug in the MPL that does not exist.
 *
 * <p>The wrong-kind case is the subtle one. Every handle is the same Smithy shape -- a
 * length-constrained string -- so the wire cannot distinguish a keyring handle from a
 * MaterialProviders handle. Only the server-side registry's recorded kind can, which is why it
 * records one.
 */
class ResourceHandleContractTest {

    private static MPLTestServerClient client;
    private static String mplId;
    private static String keyringId;

    @BeforeAll
    static void setUp() {
        client = TestServerClients.forTarget(LanguageServerRegistry.shared().primary());
        mplId = client.createMPL(CreateMPLInput.builder()
            .config(MaterialProvidersConfig.builder().build())
            .build()).getMplId();
        keyringId = client.createRawAesKeyring(CreateRawAesKeyringInput.builder()
            .mplId(mplId)
            .keyNamespace(TestKeyMaterial.KEY_NAMESPACE)
            .keyName(TestKeyMaterial.AES_KEY_NAME)
            .wrappingKey(TestKeyMaterial.aesKeyForBits(256))
            .wrappingAlg(AesWrappingAlg.ALG_AES256_GCM_IV12_TAG16)
            .build()).getKeyringId();
    }

    private static GenericServerError initializeWithMplId(String candidateMplId) {
        return assertThrows(GenericServerError.class, () ->
            client.initializeEncryptionMaterials(InitializeEncryptionMaterialsInput.builder()
                .mplId(candidateMplId)
                .algorithmSuiteId(AlgorithmSuiteId.builder()
                    .esdk(ESDKAlgorithmSuiteId.ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY)
                    .build())
                .encryptionContext(Map.of())
                .requiredEncryptionContextKeys(List.of())
                .build()));
    }

    @Test
    @DisplayName("An unknown handle is refused")
    void unknownHandleIsRefused() {
        String unknown = UUID.randomUUID().toString();
        GenericServerError error = initializeWithMplId(unknown);

        assertTrue(error.getMessage().contains(unknown),
            "the error must name the handle it could not resolve, but was: " + error.getMessage());
    }

    @Test
    @DisplayName("An empty handle is refused by the modeled length constraint")
    void emptyHandleIsRefused() {
        // NOTE, and an honest limitation: an empty handle does NOT arrive as one of the two
        // modeled errors. `ResourceId` carries `@length(min: 1)`, and smithy-java enforces that
        // constraint in the framework layer BEFORE any handler runs, so the caller sees
        // smithy-java's own `ValidationException` instead.
        //
        // That is acceptable -- the call still fails loudly, with a message naming the member --
        // but it means the "every failure is one of two modeled errors" guarantee holds for
        // handler outcomes, not for constraint violations the framework rejects first. The
        // alternative would be to drop the length constraint so empty strings reach the handler,
        // which would trade a precise, automatic rejection for a hand-written one.
        ValidationException error = assertThrows(ValidationException.class, () ->
            client.initializeEncryptionMaterials(InitializeEncryptionMaterialsInput.builder()
                .mplId("")
                .algorithmSuiteId(AlgorithmSuiteId.builder()
                    .esdk(ESDKAlgorithmSuiteId.ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY)
                    .build())
                .encryptionContext(Map.of())
                .requiredEncryptionContextKeys(List.of())
                .build()));

        assertTrue(error.getMessage().toLowerCase().contains("mplid")
                || error.getMessage().toLowerCase().contains("length"),
            "the validation failure should identify the offending member, but was: "
                + error.getMessage());
    }

    @Test
    @DisplayName("A keyring handle passed where a MaterialProviders handle belongs is refused")
    void wrongKindHandleIsRefused() {
        GenericServerError error = initializeWithMplId(keyringId);

        // The message must name BOTH kinds. "Not found" would be actively misleading here --
        // the handle exists, it simply denotes the wrong thing.
        String message = error.getMessage();
        assertTrue(message.contains("Keyring") && message.contains("MaterialProviders"),
            "the error must name both the actual and the required kind, but was: " + message);
    }

    @Test
    @DisplayName("A MaterialProviders handle passed where a keyring handle belongs is refused")
    void wrongKindHandleIsRefusedOnKeyringOperation() {
        var materials = client.initializeEncryptionMaterials(
            InitializeEncryptionMaterialsInput.builder()
                .mplId(mplId)
                .algorithmSuiteId(AlgorithmSuiteId.builder()
                    .esdk(ESDKAlgorithmSuiteId.ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY)
                    .build())
                .encryptionContext(Map.of())
                .requiredEncryptionContextKeys(List.of())
                .build()).getMaterials();

        // The mirror image of the previous case, verifying the kind check is enforced in both
        // directions rather than only where it was first needed.
        GenericServerError error = assertThrows(GenericServerError.class, () ->
            client.onEncrypt(OnEncryptInput.builder()
                .keyringId(mplId)
                .materials(materials)
                .build()));

        String message = error.getMessage();
        assertTrue(message.contains("Keyring") && message.contains("MaterialProviders"),
            "the error must name both the actual and the required kind, but was: " + message);
    }
}
