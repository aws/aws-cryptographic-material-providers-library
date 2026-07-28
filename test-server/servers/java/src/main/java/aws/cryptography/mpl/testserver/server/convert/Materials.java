package aws.cryptography.mpl.testserver.server.convert;

import java.nio.ByteBuffer;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import software.amazon.cryptography.materialproviders.MaterialProviders;

/**
 * Converts cryptographic materials between the wire shapes and the MPL's
 * types.
 *
 * <p>Materials travel on the wire (not behind handles) so a test can carry
 * one server's OnEncrypt output into another server's OnDecrypt --
 * eventually across two language servers. The algorithm suite asymmetry
 * (wire carries id, MPL carries full AlgorithmSuiteInfo) is handled by
 * {@link AlgorithmSuites}.
 */
public final class Materials {

  private Materials() {}

  // -- Encryption materials -------------------------------------------------

  /** Convert wire encryption materials to the MPL's. */
  public static software.amazon.cryptography.materialproviders.model.EncryptionMaterials toMpl(
    MaterialProviders materialProviders,
    aws.cryptography.mpl.testserver.server.model.EncryptionMaterials wire
  ) {
    var builder =
      software.amazon.cryptography.materialproviders.model.EncryptionMaterials
        .builder()
        .algorithmSuite(
          AlgorithmSuites.info(materialProviders, wire.getAlgorithmSuiteId())
        )
        .encryptionContext(orEmptyMap(wire.getEncryptionContext()))
        .encryptedDataKeys(edksToMpl(wire.getEncryptedDataKeys()))
        .requiredEncryptionContextKeys(
          orEmptyList(wire.getRequiredEncryptionContextKeys())
        );

    // Optional members are only set when present: the MPL distinguishes
    // absent from empty (a zero-length plaintext data key is not the
    // same as no key at all).
    if (wire.getPlaintextDataKey() != null) {
      builder.plaintextDataKey(wire.getPlaintextDataKey());
    }
    if (wire.getSigningKey() != null) {
      builder.signingKey(wire.getSigningKey());
    }
    if (wire.getSymmetricSigningKeys() != null) {
      builder.symmetricSigningKeys(
        new ArrayList<>(wire.getSymmetricSigningKeys())
      );
    }
    return builder.build();
  }

  /** Convert the MPL's encryption materials to the wire shape. */
  public static aws.cryptography.mpl.testserver.server.model.EncryptionMaterials toWire(
    software.amazon.cryptography.materialproviders.model.EncryptionMaterials mpl
  ) {
    var builder =
      aws.cryptography.mpl.testserver.server.model.EncryptionMaterials
        .builder()
        .algorithmSuiteId(AlgorithmSuites.toWire(mpl.algorithmSuite().id()))
        .encryptionContext(orEmptyMap(mpl.encryptionContext()))
        .encryptedDataKeys(edksToWire(mpl.encryptedDataKeys()))
        .requiredEncryptionContextKeys(
          orEmptyList(mpl.requiredEncryptionContextKeys())
        );

    if (mpl.plaintextDataKey() != null) {
      builder.plaintextDataKey(mpl.plaintextDataKey());
    }
    if (mpl.signingKey() != null) {
      builder.signingKey(mpl.signingKey());
    }
    if (mpl.symmetricSigningKeys() != null) {
      builder.symmetricSigningKeys(List.copyOf(mpl.symmetricSigningKeys()));
    }
    return builder.build();
  }

  // -- Decryption materials -------------------------------------------------

  /** Convert wire decryption materials to the MPL's. */
  public static software.amazon.cryptography.materialproviders.model.DecryptionMaterials toMpl(
    MaterialProviders materialProviders,
    aws.cryptography.mpl.testserver.server.model.DecryptionMaterials wire
  ) {
    var builder =
      software.amazon.cryptography.materialproviders.model.DecryptionMaterials
        .builder()
        .algorithmSuite(
          AlgorithmSuites.info(materialProviders, wire.getAlgorithmSuiteId())
        )
        .encryptionContext(orEmptyMap(wire.getEncryptionContext()))
        .requiredEncryptionContextKeys(
          orEmptyList(wire.getRequiredEncryptionContextKeys())
        );

    if (wire.getPlaintextDataKey() != null) {
      builder.plaintextDataKey(wire.getPlaintextDataKey());
    }
    if (wire.getVerificationKey() != null) {
      builder.verificationKey(wire.getVerificationKey());
    }
    if (wire.getSymmetricSigningKey() != null) {
      builder.symmetricSigningKey(wire.getSymmetricSigningKey());
    }
    return builder.build();
  }

  /** Convert the MPL's decryption materials to the wire shape. */
  public static aws.cryptography.mpl.testserver.server.model.DecryptionMaterials toWire(
    software.amazon.cryptography.materialproviders.model.DecryptionMaterials mpl
  ) {
    var builder =
      aws.cryptography.mpl.testserver.server.model.DecryptionMaterials
        .builder()
        .algorithmSuiteId(AlgorithmSuites.toWire(mpl.algorithmSuite().id()))
        .encryptionContext(orEmptyMap(mpl.encryptionContext()))
        .requiredEncryptionContextKeys(
          orEmptyList(mpl.requiredEncryptionContextKeys())
        );

    if (mpl.plaintextDataKey() != null) {
      builder.plaintextDataKey(mpl.plaintextDataKey());
    }
    if (mpl.verificationKey() != null) {
      builder.verificationKey(mpl.verificationKey());
    }
    if (mpl.symmetricSigningKey() != null) {
      builder.symmetricSigningKey(mpl.symmetricSigningKey());
    }
    return builder.build();
  }

  // -- Encrypted data keys --------------------------------------------------

  /** Convert wire encrypted data keys to the MPL's. */
  public static List<
    software.amazon.cryptography.materialproviders.model.EncryptedDataKey
  > edksToMpl(
    List<aws.cryptography.mpl.testserver.server.model.EncryptedDataKey> wire
  ) {
    if (wire == null) {
      return List.of();
    }
    List<
      software.amazon.cryptography.materialproviders.model.EncryptedDataKey
    > mpl = new ArrayList<>(wire.size());
    for (var edk : wire) {
      mpl.add(
        software.amazon.cryptography.materialproviders.model.EncryptedDataKey
          .builder()
          .keyProviderId(edk.getKeyProviderId())
          .keyProviderInfo(edk.getKeyProviderInfo())
          .ciphertext(edk.getCiphertext())
          .build()
      );
    }
    return mpl;
  }

  /** Convert the MPL's encrypted data keys to the wire shape. */
  public static List<
    aws.cryptography.mpl.testserver.server.model.EncryptedDataKey
  > edksToWire(
    List<
      software.amazon.cryptography.materialproviders.model.EncryptedDataKey
    > mpl
  ) {
    if (mpl == null) {
      return List.of();
    }
    List<aws.cryptography.mpl.testserver.server.model.EncryptedDataKey> wire =
      new ArrayList<>(mpl.size());
    for (var edk : mpl) {
      wire.add(
        aws.cryptography.mpl.testserver.server.model.EncryptedDataKey
          .builder()
          .keyProviderId(edk.keyProviderId())
          .keyProviderInfo(edk.keyProviderInfo())
          .ciphertext(edk.ciphertext())
          .build()
      );
    }
    return wire;
  }

  // -- Helpers --------------------------------------------------------------

  private static Map<String, String> orEmptyMap(Map<String, String> value) {
    return value == null ? Map.of() : Map.copyOf(value);
  }

  private static List<String> orEmptyList(List<String> value) {
    return value == null ? List.of() : List.copyOf(value);
  }

  /**
   * Read a ByteBuffer without disturbing its position. The MPL returns
   * buffers it may still reference; consuming one in place would corrupt
   * a later read of the same materials.
   */
  public static byte[] toBytes(ByteBuffer buffer) {
    if (buffer == null) {
      return null;
    }
    ByteBuffer duplicate = buffer.asReadOnlyBuffer();
    byte[] bytes = new byte[duplicate.remaining()];
    duplicate.get(bytes);
    return bytes;
  }
}
