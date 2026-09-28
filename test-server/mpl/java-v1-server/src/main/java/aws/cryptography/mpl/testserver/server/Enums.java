package aws.cryptography.mpl.testserver.server;

import java.nio.ByteBuffer;
import java.util.EnumMap;
import java.util.List;
import java.util.Map;
import software.amazon.cryptography.materialproviders.MaterialProviders;
import software.amazon.cryptography.materialproviders.model.AlgorithmSuiteId;
import software.amazon.cryptography.materialproviders.model.AlgorithmSuiteInfo;
import software.amazon.cryptography.materialproviders.model.CommitmentPolicy;
import software.amazon.cryptography.materialproviders.model.ESDKAlgorithmSuiteId;
import software.amazon.cryptography.materialproviders.model.ESDKCommitmentPolicy;

/**
 * Wire enum names to MPL values and back. The wire carries ESDK suites and
 * commitment policies only (the model has no DBE members), under the same
 * constant names the MPL's ESDK enums use.
 */
final class Enums {

  /** The two-byte message-format id of each ESDK suite, for GetAlgorithmSuiteInfo. */
  private static final Map<ESDKAlgorithmSuiteId, Integer> BINARY_IDS =
    binaryIds();

  private static final String ESDK_POLICY_PREFIX = "ESDK_";

  private final Map<ESDKAlgorithmSuiteId, AlgorithmSuiteInfo> suiteInfo =
    new EnumMap<>(ESDKAlgorithmSuiteId.class);

  /**
   * Resolve every suite's AlgorithmSuiteInfo from the MPL once, and check the
   * id table above against what the MPL reports, so a wrong entry fails at
   * startup rather than as a confusing materials error later.
   */
  Enums(MaterialProviders materialProviders) {
    for (ESDKAlgorithmSuiteId suite : ESDKAlgorithmSuiteId.values()) {
      Integer binary = BINARY_IDS.get(suite);
      if (binary == null) {
        throw new IllegalStateException(
          "no binary id for ESDK suite " + suite.name()
        );
      }
      ByteBuffer id = ByteBuffer.wrap(
        new byte[] { (byte) (binary >> 8), (byte) (binary & 0xFF) }
      );
      AlgorithmSuiteInfo info = materialProviders.GetAlgorithmSuiteInfo(id);
      if (info.id().ESDK() != suite) {
        throw new IllegalStateException(
          "binary id table maps " + suite.name() + " to " + info.id()
        );
      }
      suiteInfo.put(suite, info);
    }
  }

  static AlgorithmSuiteId suiteId(String wire) {
    return AlgorithmSuiteId.builder().ESDK(esdkSuite(wire)).build();
  }

  AlgorithmSuiteInfo suiteInfo(String wire) {
    return suiteInfo.get(esdkSuite(wire));
  }

  static String suiteToWire(AlgorithmSuiteId id) {
    if (id.ESDK() == null) {
      throw ModeledError.generic(
        "the MPL returned a non-ESDK algorithm suite, which the model cannot carry: " +
        id
      );
    }
    return id.ESDK().name();
  }

  static CommitmentPolicy commitmentPolicy(String wire) {
    if (!wire.startsWith(ESDK_POLICY_PREFIX)) {
      throw ModeledError.generic("unknown commitment policy: " + wire);
    }
    try {
      return CommitmentPolicy
        .builder()
        .ESDK(
          ESDKCommitmentPolicy.valueOf(
            wire.substring(ESDK_POLICY_PREFIX.length())
          )
        )
        .build();
    } catch (IllegalArgumentException e) {
      throw ModeledError.generic("unknown commitment policy: " + wire);
    }
  }

  static software.amazon.cryptography.materialproviders.model.AesWrappingAlg aesWrappingAlg(
    String wire
  ) {
    try {
      return software.amazon.cryptography.materialproviders.model.AesWrappingAlg.valueOf(
        wire
      );
    } catch (IllegalArgumentException e) {
      throw ModeledError.generic("unknown AES wrapping algorithm: " + wire);
    }
  }

  private static ESDKAlgorithmSuiteId esdkSuite(String wire) {
    try {
      return ESDKAlgorithmSuiteId.valueOf(wire);
    } catch (IllegalArgumentException e) {
      throw ModeledError.generic("unknown algorithm suite: " + wire);
    }
  }

  private static Map<ESDKAlgorithmSuiteId, Integer> binaryIds() {
    Map<ESDKAlgorithmSuiteId, Integer> ids = new EnumMap<>(
      ESDKAlgorithmSuiteId.class
    );
    List
      .of(
        Map.entry(
          ESDKAlgorithmSuiteId.ALG_AES_128_GCM_IV12_TAG16_NO_KDF,
          0x0014
        ),
        Map.entry(
          ESDKAlgorithmSuiteId.ALG_AES_192_GCM_IV12_TAG16_NO_KDF,
          0x0046
        ),
        Map.entry(
          ESDKAlgorithmSuiteId.ALG_AES_256_GCM_IV12_TAG16_NO_KDF,
          0x0078
        ),
        Map.entry(
          ESDKAlgorithmSuiteId.ALG_AES_128_GCM_IV12_TAG16_HKDF_SHA256,
          0x0114
        ),
        Map.entry(
          ESDKAlgorithmSuiteId.ALG_AES_192_GCM_IV12_TAG16_HKDF_SHA256,
          0x0146
        ),
        Map.entry(
          ESDKAlgorithmSuiteId.ALG_AES_256_GCM_IV12_TAG16_HKDF_SHA256,
          0x0178
        ),
        Map.entry(
          ESDKAlgorithmSuiteId.ALG_AES_128_GCM_IV12_TAG16_HKDF_SHA256_ECDSA_P256,
          0x0214
        ),
        Map.entry(
          ESDKAlgorithmSuiteId.ALG_AES_192_GCM_IV12_TAG16_HKDF_SHA384_ECDSA_P384,
          0x0346
        ),
        Map.entry(
          ESDKAlgorithmSuiteId.ALG_AES_256_GCM_IV12_TAG16_HKDF_SHA384_ECDSA_P384,
          0x0378
        ),
        Map.entry(
          ESDKAlgorithmSuiteId.ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY,
          0x0478
        ),
        Map.entry(
          ESDKAlgorithmSuiteId.ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY_ECDSA_P384,
          0x0578
        )
      )
      .forEach(entry -> ids.put(entry.getKey(), entry.getValue()));
    return ids;
  }
}
