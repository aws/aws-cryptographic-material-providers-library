package aws.cryptography.mpl.testserver.server;

import java.util.List;

/** One of the two modeled TestServer errors, carrying its rpcv2Cbor shape id. */
final class ModeledError extends RuntimeException {

  enum Kind {
    GENERIC("GenericServerError"),
    MPL("MPLClientError");

    private final String shapeName;

    Kind(String shapeName) {
      this.shapeName = shapeName;
    }
  }

  private static final String NAMESPACE = "aws.cryptography.mpl.testserver#";

  final Kind kind;
  /** MPLClientError's collectedErrors, or null when the error collected none. */
  final List<String> collectedErrors;

  private ModeledError(
    Kind kind,
    String message,
    List<String> collectedErrors
  ) {
    super(message);
    this.kind = kind;
    this.collectedErrors = collectedErrors;
  }

  /** A framework-side failure: bad request, unknown operation, bad handle. */
  static ModeledError generic(String message) {
    return new ModeledError(Kind.GENERIC, message, null);
  }

  /** A failure raised by the Material Providers Library. */
  static ModeledError mpl(String message) {
    return new ModeledError(Kind.MPL, message, null);
  }

  /** A failure raised by the MPL, with the messages of the errors it collected. */
  static ModeledError mpl(String message, List<String> collectedErrors) {
    return new ModeledError(Kind.MPL, message, collectedErrors);
  }

  String typeId() {
    return NAMESPACE + kind.shapeName;
  }
}
