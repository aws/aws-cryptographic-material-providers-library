package aws.cryptography.mpl.testserver.server.convert;

import aws.cryptography.mpl.testserver.server.model.AlgorithmSuiteId;
import aws.cryptography.mpl.testserver.server.model.DBEAlgorithmSuiteId;
import aws.cryptography.mpl.testserver.server.model.ESDKAlgorithmSuiteId;
import aws.cryptography.mpl.testserver.server.model.GenericServerError;
import java.nio.ByteBuffer;
import java.util.HashMap;
import java.util.Map;
import software.amazon.cryptography.materialproviders.MaterialProviders;
import software.amazon.cryptography.materialproviders.model.AlgorithmSuiteInfo;

/**
 * Converts algorithm suite identities between the wire shapes and the
 * MPL's types, and rehydrates AlgorithmSuiteInfo from an identifier.
 *
 * <p>Deliberate deviation (Requirement 8): the wire carries only the
 * algorithmSuiteId, not the full AlgorithmSuiteInfo (5 nested unions +
 * 4 imported shapes, ~15 extra shapes to model). This is lossless
 * because AlgorithmSuiteInfo is a total function of the id and the MPL
 * provides GetAlgorithmSuiteInfo to rehydrate it.
 */
public final class AlgorithmSuites {

  /**
   * MPL enum constants indexed on constant.toString() rather than a
   * hand-written table, so a new MPL suite cannot silently rot it.
   */
  private static final Map<
    String,
    software.amazon.cryptography.materialproviders.model.ESDKAlgorithmSuiteId
  > MPL_ESDK_BY_VALUE = indexEsdk();

  private static final Map<
    String,
    software.amazon.cryptography.materialproviders.model.DBEAlgorithmSuiteId
  > MPL_DBE_BY_VALUE = indexDbe();

  private AlgorithmSuites() {}

  private static Map<
    String,
    software.amazon.cryptography.materialproviders.model.ESDKAlgorithmSuiteId
  > indexEsdk() {
    Map<
      String,
      software.amazon.cryptography.materialproviders.model.ESDKAlgorithmSuiteId
    > byValue = new HashMap<>();
    for (var constant : software.amazon.cryptography.materialproviders.model.ESDKAlgorithmSuiteId.values()) {
      byValue.put(constant.toString(), constant);
    }
    return Map.copyOf(byValue);
  }

  private static Map<
    String,
    software.amazon.cryptography.materialproviders.model.DBEAlgorithmSuiteId
  > indexDbe() {
    Map<
      String,
      software.amazon.cryptography.materialproviders.model.DBEAlgorithmSuiteId
    > byValue = new HashMap<>();
    for (var constant : software.amazon.cryptography.materialproviders.model.DBEAlgorithmSuiteId.values()) {
      byValue.put(constant.toString(), constant);
    }
    return Map.copyOf(byValue);
  }

  /** Convert a wire algorithm suite identifier to the MPL's. */
  public static software.amazon.cryptography.materialproviders.model.AlgorithmSuiteId toMpl(
    AlgorithmSuiteId wire
  ) {
    if (wire == null) {
      throw GenericServerError
        .builder()
        .message("An algorithmSuiteId is required but was absent.")
        .build();
    }
    if (wire instanceof AlgorithmSuiteId.EsdkMember esdk) {
      String value = esdk.getValue().getValue();
      var mpl = MPL_ESDK_BY_VALUE.get(value);
      if (mpl == null) {
        throw unknownSuite("ESDK", value);
      }
      return software.amazon.cryptography.materialproviders.model.AlgorithmSuiteId
        .builder()
        .ESDK(mpl)
        .build();
    }
    if (wire instanceof AlgorithmSuiteId.DbeMember dbe) {
      String value = dbe.getValue().getValue();
      var mpl = MPL_DBE_BY_VALUE.get(value);
      if (mpl == null) {
        throw unknownSuite("DBE", value);
      }
      return software.amazon.cryptography.materialproviders.model.AlgorithmSuiteId
        .builder()
        .DBE(mpl)
        .build();
    }
    throw GenericServerError
      .builder()
      .message(
        "Unrecognized algorithmSuiteId union member: " +
        wire +
        ". Exactly one of ESDK or DBE must be set."
      )
      .build();
  }

  /** Convert the MPL's algorithm suite identifier to the wire shape. */
  public static AlgorithmSuiteId toWire(
    software.amazon.cryptography.materialproviders.model.AlgorithmSuiteId mpl
  ) {
    if (mpl == null) {
      throw GenericServerError
        .builder()
        .message("The MPL returned materials with no algorithm suite id.")
        .build();
    }
    if (mpl.ESDK() != null) {
      return AlgorithmSuiteId
        .builder()
        .esdk(ESDKAlgorithmSuiteId.from(mpl.ESDK().toString()))
        .build();
    }
    if (mpl.DBE() != null) {
      return AlgorithmSuiteId
        .builder()
        .dbe(DBEAlgorithmSuiteId.from(mpl.DBE().toString()))
        .build();
    }
    throw GenericServerError
      .builder()
      .message(
        "The MPL returned an AlgorithmSuiteId with neither ESDK nor DBE set."
      )
      .build();
  }

  /**
   * Rehydrate the full AlgorithmSuiteInfo from a wire identifier using
   * the MPL's own lookup. Suite values are hex text (e.g. 0x0478) and
   * the lookup needs binary, hence the hex decode.
   */
  public static AlgorithmSuiteInfo info(
    MaterialProviders materialProviders,
    AlgorithmSuiteId wire
  ) {
    String value = wireValue(wire);
    return materialProviders.GetAlgorithmSuiteInfo(
      ByteBuffer.wrap(decodeHex(value))
    );
  }

  private static String wireValue(AlgorithmSuiteId wire) {
    if (wire instanceof AlgorithmSuiteId.EsdkMember esdk) {
      return esdk.getValue().getValue();
    }
    if (wire instanceof AlgorithmSuiteId.DbeMember dbe) {
      return dbe.getValue().getValue();
    }
    throw GenericServerError
      .builder()
      .message(
        "Unrecognized algorithmSuiteId union member: " +
        wire +
        ". Exactly one of ESDK or DBE must be set."
      )
      .build();
  }

  /**
   * Decode a suite value such as {@code 0x0478} to its bytes.
   *
   * @throws GenericServerError if the value is not valid hex -- a harness
   *     failure, since the wire enum restricts to MPL constants.
   */
  private static byte[] decodeHex(String value) {
    String digits = value.startsWith("0x") || value.startsWith("0X")
      ? value.substring(2)
      : value;
    if (digits.isEmpty() || digits.length() % 2 != 0) {
      throw GenericServerError
        .builder()
        .message(
          "Algorithm suite value '" +
          value +
          "' is not an even-length hex string, so it cannot be a binary suite id."
        )
        .build();
    }
    byte[] bytes = new byte[digits.length() / 2];
    for (int i = 0; i < bytes.length; i++) {
      int high = Character.digit(digits.charAt(i * 2), 16);
      int low = Character.digit(digits.charAt(i * 2 + 1), 16);
      if (high < 0 || low < 0) {
        throw GenericServerError
          .builder()
          .message(
            "Algorithm suite value '" + value + "' contains non-hex characters."
          )
          .build();
      }
      bytes[i] = (byte) ((high << 4) | low);
    }
    return bytes;
  }

  private static GenericServerError unknownSuite(String format, String value) {
    return GenericServerError
      .builder()
      .message(
        "The wire model names " +
        format +
        " algorithm suite '" +
        value +
        "', but the MPL this server is built against does not define it. The model and" +
        " the Artifact_Under_Test have diverged."
      )
      .build();
  }
}
