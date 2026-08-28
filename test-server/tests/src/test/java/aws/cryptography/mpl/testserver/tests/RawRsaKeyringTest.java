package aws.cryptography.mpl.testserver.tests;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertThrows;

import aws.cryptography.mpl.testserver.client.client.MPLTestServerClient;
import aws.cryptography.mpl.testserver.client.model.AlgorithmSuiteId;
import aws.cryptography.mpl.testserver.client.model.CreateRawRsaKeyringInput;
import aws.cryptography.mpl.testserver.client.model.ESDKAlgorithmSuiteId;
import aws.cryptography.mpl.testserver.client.model.EncryptionMaterials;
import aws.cryptography.mpl.testserver.client.model.InitializeDecryptionMaterialsInput;
import aws.cryptography.mpl.testserver.client.model.InitializeEncryptionMaterialsInput;
import aws.cryptography.mpl.testserver.client.model.MaterialProvidersClientError;
import aws.cryptography.mpl.testserver.client.model.OnDecryptInput;
import aws.cryptography.mpl.testserver.client.model.OnEncryptInput;
import aws.cryptography.mpl.testserver.client.model.PaddingScheme;
import java.util.List;
import java.util.Map;
import java.util.stream.Stream;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.MethodSource;

/**
 * Raw RSA keyring conformance, including negative cases. The negatives are only
 * assertable because the {@code __type} discriminator fix makes
 * {@code MaterialProvidersClientError} arrive as its own type; without it every
 * negative could assert only "something failed".
 */
class RawRsaKeyringTest {

  private static final AlgorithmSuiteId SUITE = AlgorithmSuiteId
    .builder()
    .esdk(ESDKAlgorithmSuiteId.ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY)
    .build();

  private static MPLTestServerClient client;
  private static String mplId;

  @BeforeAll
  static void setUp() {
    client =
      TestServerClients.forTarget(LanguageServerRegistry.shared().primary());
    mplId = KeyringRoundTrip.createMpl(client);
  }

  private static String keyring(
    PaddingScheme padding,
    boolean withPublic,
    boolean withPrivate
  ) {
    var builder = CreateRawRsaKeyringInput
      .builder()
      .mplId(mplId)
      .keyNamespace(TestKeyMaterial.KEY_NAMESPACE)
      .keyName(TestKeyMaterial.RSA_KEY_NAME)
      .paddingScheme(padding);
    if (withPublic) {
      builder.publicKey(
        TestKeyMaterial.pem(TestKeyMaterial.RSA_PUBLIC_KEY_PEM)
      );
    }
    if (withPrivate) {
      builder.privateKey(
        TestKeyMaterial.pem(TestKeyMaterial.RSA_PRIVATE_KEY_PEM)
      );
    }
    return client.createRawRsaKeyring(builder.build()).getKeyringId();
  }

  /**
   * Uses {@code @MethodSource} rather than {@code @EnumSource} because smithy-java
   * generates enum shapes as sealed interfaces, not Java enums.
   */
  static Stream<PaddingScheme> paddingSchemes() {
    return PaddingScheme.values().stream();
  }

  @ParameterizedTest(name = "Raw RSA round-trip with padding {0}")
  @MethodSource("paddingSchemes")
  void roundTripsWithEachPaddingScheme(PaddingScheme padding) {
    String keyringId = keyring(padding, true, true);
    assertNotNull(
      keyringId,
      "CreateRawRsaKeyring must return a keyring handle"
    );

    KeyringRoundTrip.assertRoundTrips(
      client,
      client,
      mplId,
      mplId,
      keyringId,
      keyringId,
      SUITE,
      Map.of("purpose", "mpl-test-server-conformance", "keyring", "raw-rsa")
    );
  }

  @Test
  @DisplayName("A public-key-only keyring encrypts but is rejected on decrypt")
  void publicKeyOnlyCannotDecrypt() {
    String encryptOnly = keyring(PaddingScheme.OAEP_SHA256_MGF1, true, false);

    EncryptionMaterials encrypted = client
      .onEncrypt(
        OnEncryptInput
          .builder()
          .keyringId(encryptOnly)
          .materials(
            client
              .initializeEncryptionMaterials(
                InitializeEncryptionMaterialsInput
                  .builder()
                  .mplId(mplId)
                  .algorithmSuiteId(SUITE)
                  .encryptionContext(Map.of())
                  .requiredEncryptionContextKeys(List.of())
                  .build()
              )
              .getMaterials()
          )
          .build()
      )
      .getMaterials();

    assertNotNull(
      encrypted.getPlaintextDataKey(),
      "a public-key-only RSA keyring must still be able to encrypt"
    );

    var toDecrypt = client
      .initializeDecryptionMaterials(
        InitializeDecryptionMaterialsInput
          .builder()
          .mplId(mplId)
          .algorithmSuiteId(SUITE)
          .encryptionContext(Map.of())
          .requiredEncryptionContextKeys(List.of())
          .build()
      )
      .getMaterials();

    MaterialProvidersClientError error = assertThrows(
      MaterialProvidersClientError.class,
      () ->
        client.onDecrypt(
          OnDecryptInput
            .builder()
            .keyringId(encryptOnly)
            .materials(toDecrypt)
            .encryptedDataKeys(encrypted.getEncryptedDataKeys())
            .build()
        )
    );

    assertFalse(
      error.getMessage().isEmpty(),
      "the MPL's explanation must be forwarded, not swallowed"
    );
  }

  @Test
  @DisplayName("A private-key-only keyring decrypts but is rejected on encrypt")
  void privateKeyOnlyCannotEncrypt() {
    String bothKeys = keyring(PaddingScheme.OAEP_SHA256_MGF1, true, true);
    String decryptOnly = keyring(PaddingScheme.OAEP_SHA256_MGF1, false, true);

    var initialized = client
      .initializeEncryptionMaterials(
        InitializeEncryptionMaterialsInput
          .builder()
          .mplId(mplId)
          .algorithmSuiteId(SUITE)
          .encryptionContext(Map.of())
          .requiredEncryptionContextKeys(List.of())
          .build()
      )
      .getMaterials();

    MaterialProvidersClientError error = assertThrows(
      MaterialProvidersClientError.class,
      () ->
        client.onEncrypt(
          OnEncryptInput
            .builder()
            .keyringId(decryptOnly)
            .materials(initialized)
            .build()
        )
    );
    assertFalse(
      error.getMessage().isEmpty(),
      "the MPL's explanation must be forwarded, not swallowed"
    );

    // Asserting the decrypt SUCCEEDS proves the failure above was about the missing
    // public key, not bad key material.
    KeyringRoundTrip.assertRoundTrips(
      client,
      client,
      mplId,
      mplId,
      bothKeys,
      decryptOnly,
      SUITE,
      Map.of()
    );
  }

  @Test
  @DisplayName("A keyring with neither key is rejected at construction")
  void neitherKeyIsRejected() {
    MaterialProvidersClientError error = assertThrows(
      MaterialProvidersClientError.class,
      () -> keyring(PaddingScheme.OAEP_SHA256_MGF1, false, false)
    );

    assertFalse(
      error.getMessage().isEmpty(),
      "the MPL's explanation must be forwarded, not swallowed"
    );
  }
}
