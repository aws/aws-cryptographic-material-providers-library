package aws.cryptography.mpl.testserver.server.error;

import aws.cryptography.mpl.testserver.server.model.GenericServerError;
import aws.cryptography.mpl.testserver.server.model.MPLTestServerException;
import aws.cryptography.mpl.testserver.server.model.MaterialProvidersClientError;
import software.amazon.cryptography.materialproviders.model.AwsCryptographicMaterialProvidersException;

/**
 * Maps any throwable onto one of the two modeled error shapes based on
 * whether the failure came from the MPL or from the harness.
 *
 * <p>The MPL declares four unrelated exception types with no common supertype.
 * Matching on the PACKAGE prefix rather than enumerating types means a new
 * MPL error type is classified correctly the day it appears. The cause
 * chain is walked because Dafny-generated code sometimes wraps MPL errors
 * in a plain RuntimeException. The MPL message is forwarded verbatim so
 * negative tests can assert on it.
 */
public final class ErrorClassifier {

  /**
   * Package prefix identifying the Artifact_Under_Test. A new MPL error
   * type under this prefix is automatically classified as MPL-origin.
   */
  private static final String MPL_PACKAGE_PREFIX =
    "software.amazon.cryptography.";

  /**
   * Classify a failure by its origin.
   *
   * @param operationName used to build the harness-error message.
   * @param failure the throwable raised by the handler body.
   */
  public MPLTestServerException classify(
    String operationName,
    Throwable failure
  ) {
    if (failure instanceof MPLTestServerException modeled) {
      return modeled;
    }

    if (isFromArtifactUnderTest(failure)) {
      return MaterialProvidersClientError
        .builder()
        .message(mplMessage(failure))
        .build();
    }

    return GenericServerError
      .builder()
      .message("Operation '" + operationName + "' failed: " + describe(failure))
      .build();
  }

  /** Walk the cause chain looking for an MPL-origin exception. */
  private static boolean isFromArtifactUnderTest(Throwable failure) {
    for (Throwable t = failure; t != null; t = t.getCause()) {
      if (t.getClass().getName().startsWith(MPL_PACKAGE_PREFIX)) {
        return true;
      }
      if (t.getCause() == t) {
        break;
      }
    }
    return false;
  }

  /**
   * Extract the MPL's own message so negative tests assert on the MPL's
   * words, not the harness's paraphrase.
   */
  private static String mplMessage(Throwable failure) {
    for (Throwable t = failure; t != null; t = t.getCause()) {
      if (t instanceof AwsCryptographicMaterialProvidersException mpl) {
        String message = mpl.message();
        if (message != null && !message.isEmpty()) {
          return message;
        }
      }
      if (t.getClass().getName().startsWith(MPL_PACKAGE_PREFIX)) {
        String message = t.getMessage();
        if (message != null && !message.isEmpty()) {
          return message;
        }
        // Message-less MPL error -- name the type so the response is
        // never empty.
        return t.getClass().getSimpleName();
      }
      if (t.getCause() == t) {
        break;
      }
    }
    return describe(failure);
  }

  /** Build a non-empty description of a non-modeled failure. */
  private static String describe(Throwable failure) {
    if (failure == null) {
      return "unknown error";
    }
    String type = failure.getClass().getName();
    String message = failure.getMessage();
    return (message == null || message.isEmpty())
      ? type
      : type + ": " + message;
  }
}
