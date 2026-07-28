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
 * Every way a resource handle can be wrong must yield {@code GenericServerError}. A
 * bad handle is a fault in how the test called the harness, so it must be a framework
 * error -- never an MPL error.
 *
 * <p>The wrong-kind case is subtle: all handles are the same Smithy shape, so only
 * the registry's recorded kind can distinguish them.
 */
class ResourceHandleContractTest {

  private static MPLTestServerClient client;
  private static String mplId;
  private static String keyringId;

  @BeforeAll
  static void setUp() {
    client =
      TestServerClients.forTarget(LanguageServerRegistry.shared().primary());
    mplId =
      client
        .createMPL(
          CreateMPLInput
            .builder()
            .config(MaterialProvidersConfig.builder().build())
            .build()
        )
        .getMplId();
    keyringId =
      client
        .createRawAesKeyring(
          CreateRawAesKeyringInput
            .builder()
            .mplId(mplId)
            .keyNamespace(TestKeyMaterial.KEY_NAMESPACE)
            .keyName(TestKeyMaterial.AES_KEY_NAME)
            .wrappingKey(TestKeyMaterial.aesKeyForBits(256))
            .wrappingAlg(AesWrappingAlg.ALG_AES256_GCM_IV12_TAG16)
            .build()
        )
        .getKeyringId();
  }

  private static GenericServerError initializeWithMplId(String candidateMplId) {
    return assertThrows(
      GenericServerError.class,
      () ->
        client.initializeEncryptionMaterials(
          InitializeEncryptionMaterialsInput
            .builder()
            .mplId(candidateMplId)
            .algorithmSuiteId(
              AlgorithmSuiteId
                .builder()
                .esdk(
                  ESDKAlgorithmSuiteId.ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY
                )
                .build()
            )
            .encryptionContext(Map.of())
            .requiredEncryptionContextKeys(List.of())
            .build()
        )
    );
  }

  @Test
  @DisplayName("An unknown handle is refused")
  void unknownHandleIsRefused() {
    String unknown = UUID.randomUUID().toString();
    GenericServerError error = initializeWithMplId(unknown);

    assertTrue(
      error.getMessage().contains(unknown),
      "the error must name the handle it could not resolve, but was: " +
      error.getMessage()
    );
  }

  @Test
  @DisplayName("An empty handle is refused by the modeled length constraint")
  void emptyHandleIsRefused() {
    // Documented limitation: an empty handle surfaces as smithy-java's
    // ValidationException, not one of the two modeled errors, because @length(min:1)
    // is enforced in the framework layer BEFORE any handler runs.
    ValidationException error = assertThrows(
      ValidationException.class,
      () ->
        client.initializeEncryptionMaterials(
          InitializeEncryptionMaterialsInput
            .builder()
            .mplId("")
            .algorithmSuiteId(
              AlgorithmSuiteId
                .builder()
                .esdk(
                  ESDKAlgorithmSuiteId.ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY
                )
                .build()
            )
            .encryptionContext(Map.of())
            .requiredEncryptionContextKeys(List.of())
            .build()
        )
    );

    assertTrue(
      error.getMessage().toLowerCase().contains("mplid") ||
      error.getMessage().toLowerCase().contains("length"),
      "the validation failure should identify the offending member, but was: " +
      error.getMessage()
    );
  }

  @Test
  @DisplayName(
    "A keyring handle passed where a MaterialProviders handle belongs is refused"
  )
  void wrongKindHandleIsRefused() {
    GenericServerError error = initializeWithMplId(keyringId);

    String message = error.getMessage();
    assertTrue(
      message.contains("Keyring") && message.contains("MaterialProviders"),
      "the error must name both the actual and the required kind, but was: " +
      message
    );
  }

  @Test
  @DisplayName(
    "A MaterialProviders handle passed where a keyring handle belongs is refused"
  )
  void wrongKindHandleIsRefusedOnKeyringOperation() {
    var materials = client
      .initializeEncryptionMaterials(
        InitializeEncryptionMaterialsInput
          .builder()
          .mplId(mplId)
          .algorithmSuiteId(
            AlgorithmSuiteId
              .builder()
              .esdk(ESDKAlgorithmSuiteId.ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY)
              .build()
          )
          .encryptionContext(Map.of())
          .requiredEncryptionContextKeys(List.of())
          .build()
      )
      .getMaterials();

    GenericServerError error = assertThrows(
      GenericServerError.class,
      () ->
        client.onEncrypt(
          OnEncryptInput.builder().keyringId(mplId).materials(materials).build()
        )
    );

    String message = error.getMessage();
    assertTrue(
      message.contains("Keyring") && message.contains("MaterialProviders"),
      "the error must name both the actual and the required kind, but was: " +
      message
    );
  }
}
