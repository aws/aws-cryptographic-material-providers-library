package aws.cryptography.mpl.testserver.tests.meta;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;

import aws.cryptography.mpl.testserver.client.client.MPLTestServerClient;
import aws.cryptography.mpl.testserver.client.model.AlgorithmSuiteId;
import aws.cryptography.mpl.testserver.client.model.CreateMPLInput;
import aws.cryptography.mpl.testserver.client.model.ESDKAlgorithmSuiteId;
import aws.cryptography.mpl.testserver.client.model.GenericServerError;
import aws.cryptography.mpl.testserver.client.model.InitializeEncryptionMaterialsInput;
import aws.cryptography.mpl.testserver.client.model.MaterialProvidersClientError;
import aws.cryptography.mpl.testserver.client.model.MaterialProvidersConfig;
import aws.cryptography.mpl.testserver.tests.LanguageServerRegistry;
import aws.cryptography.mpl.testserver.tests.TestServerClients;
import java.util.List;
import java.util.Map;
import java.util.UUID;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

/**
 * Verifies that the two modeled errors reach the client as distinct types with their
 * messages intact. This justifies the {@code __type}-emitting protocol fix -- without
 * it every error would arrive as an untyped {@code CallException} and every negative
 * test could assert only "something failed". If this test fails untyped, check the
 * {@code META-INF/services} SPI registration.
 */
class ModeledErrorTransmissionTest {

  private static MPLTestServerClient client;

  @BeforeAll
  static void resolveTarget() {
    client =
      TestServerClients.forTarget(LanguageServerRegistry.shared().primary());
  }

  private static String createMpl() {
    return client
      .createMPL(
        CreateMPLInput
          .builder()
          .config(MaterialProvidersConfig.builder().build())
          .build()
      )
      .getMplId();
  }

  @Test
  @DisplayName(
    "A framework failure arrives as GenericServerError with a usable message"
  )
  void frameworkFailureArrivesAsGenericServerError() {
    String unknownHandle = UUID.randomUUID().toString();

    GenericServerError error = assertThrows(
      GenericServerError.class,
      () ->
        client.initializeEncryptionMaterials(
          InitializeEncryptionMaterialsInput
            .builder()
            .mplId(unknownHandle)
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

    assertNotNull(
      error.getMessage(),
      "GenericServerError must carry a message"
    );
    assertFalse(error.getMessage().isEmpty(), "the message must not be empty");
    assertTrue(
      error.getMessage().contains(unknownHandle),
      "the message should name the unresolvable handle, but was: " +
      error.getMessage()
    );
  }

  @Test
  @DisplayName(
    "An MPL failure arrives as MaterialProvidersClientError with the MPL's message"
  )
  void mplFailureArrivesAsMaterialProvidersClientError() {
    String mplId = createMpl();

    MaterialProvidersClientError error = assertThrows(
      MaterialProvidersClientError.class,
      () ->
        client.initializeEncryptionMaterials(
          InitializeEncryptionMaterialsInput
            .builder()
            .mplId(mplId)
            .algorithmSuiteId(
              AlgorithmSuiteId
                .builder()
                .esdk(
                  ESDKAlgorithmSuiteId.ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY_ECDSA_P384
                )
                .build()
            )
            .encryptionContext(Map.of())
            .requiredEncryptionContextKeys(List.of())
            .build()
        )
    );

    assertNotNull(
      error.getMessage(),
      "MaterialProvidersClientError must carry a message"
    );
    assertFalse(
      error.getMessage().isEmpty(),
      "the MPL's own message must be forwarded, not swallowed"
    );
  }
}
