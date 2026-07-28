package aws.cryptography.mpl.testserver.tests;

import static org.junit.jupiter.api.Assertions.assertNotNull;

import aws.cryptography.mpl.testserver.client.client.MPLTestServerClient;
import aws.cryptography.mpl.testserver.client.model.AesWrappingAlg;
import aws.cryptography.mpl.testserver.client.model.AlgorithmSuiteId;
import aws.cryptography.mpl.testserver.client.model.CreateRawAesKeyringInput;
import aws.cryptography.mpl.testserver.client.model.ESDKAlgorithmSuiteId;
import java.util.Map;
import java.util.stream.Stream;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

/**
 * Raw AES keyring conformance: a data key wrapped by {@code OnEncrypt} is recovered
 * unchanged by {@code OnDecrypt}.
 *
 * <p>This is the phase-1 milestone. It exercises the entire harness -- the model, both
 * generated ends of the wire, the handle registry, the materials converters and the
 * algorithm-suite rehydration -- against the MPL as transpiled from this repository's Dafny
 * source, and it needs no AWS credentials.
 *
 * <p>Every wrapping algorithm is covered because each takes a different key length, and a
 * key-length mismatch is precisely the kind of fault a converter bug produces.
 */
class RawAesKeyringTest {

    private static MPLTestServerClient client;
    private static String mplId;

    @BeforeAll
    static void setUp() {
        client = TestServerClients.forTarget(LanguageServerRegistry.shared().primary());
        mplId = KeyringRoundTrip.createMpl(client);
    }

    /**
     * One case per wrapping algorithm, paired with the key length it requires and a
     * committing algorithm suite.
     */
    static Stream<Arguments> wrappingAlgorithms() {
        return Stream.of(
            Arguments.of(AesWrappingAlg.ALG_AES128_GCM_IV12_TAG16, 128),
            Arguments.of(AesWrappingAlg.ALG_AES192_GCM_IV12_TAG16, 192),
            Arguments.of(AesWrappingAlg.ALG_AES256_GCM_IV12_TAG16, 256));
    }

    @ParameterizedTest(name = "Raw AES round-trip with {0}")
    @MethodSource("wrappingAlgorithms")
    void roundTripsWithEachWrappingAlgorithm(AesWrappingAlg wrappingAlg, int keyBits) {
        String keyringId = client.createRawAesKeyring(CreateRawAesKeyringInput.builder()
            .mplId(mplId)
            .keyNamespace(TestKeyMaterial.KEY_NAMESPACE)
            .keyName(TestKeyMaterial.AES_KEY_NAME)
            .wrappingKey(TestKeyMaterial.aesKeyForBits(keyBits))
            .wrappingAlg(wrappingAlg)
            .build()).getKeyringId();

        assertNotNull(keyringId, "CreateRawAesKeyring must return a keyring handle");

        KeyringRoundTrip.assertRoundTrips(
            client,
            client,
            mplId,
            mplId,
            keyringId,
            keyringId,
            AlgorithmSuiteId.builder()
                .esdk(ESDKAlgorithmSuiteId.ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY)
                .build(),
            // A non-empty encryption context: it is authenticated additional data, so a
            // converter that dropped or reordered it would break the round-trip. An empty
            // context would hide that class of bug entirely.
            Map.of(
                "purpose", "mpl-test-server-conformance",
                "keyring", "raw-aes"));
    }

    @ParameterizedTest(name = "Raw AES round-trip with an empty encryption context, {0}")
    @MethodSource("wrappingAlgorithms")
    void roundTripsWithEmptyEncryptionContext(AesWrappingAlg wrappingAlg, int keyBits) {
        String keyringId = client.createRawAesKeyring(CreateRawAesKeyringInput.builder()
            .mplId(mplId)
            .keyNamespace(TestKeyMaterial.KEY_NAMESPACE)
            .keyName(TestKeyMaterial.AES_KEY_NAME)
            .wrappingKey(TestKeyMaterial.aesKeyForBits(keyBits))
            .wrappingAlg(wrappingAlg)
            .build()).getKeyringId();

        // An empty context is legal and is the boundary case for the map converter.
        KeyringRoundTrip.assertRoundTrips(
            client, client, mplId, mplId, keyringId, keyringId,
            AlgorithmSuiteId.builder()
                .esdk(ESDKAlgorithmSuiteId.ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY)
                .build(),
            Map.of());
    }
}
