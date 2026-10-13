package aws.cryptography.primitives.testserver.server;

/** One of the two modeled TestServer errors, carrying its rpcv2Cbor shape id. */
final class ModeledError extends RuntimeException {

  enum Kind {
    GENERIC("GenericServerError"),
    PRIMITIVES("PrimitivesError");

    private final String shapeName;

    Kind(String shapeName) {
      this.shapeName = shapeName;
    }
  }

  private static final String NAMESPACE =
    "aws.cryptography.primitives.testserver#";

  final Kind kind;

  private ModeledError(Kind kind, String message) {
    super(message);
    this.kind = kind;
  }

  /** A framework-side failure: bad request, unknown operation, malformed input. */
  static ModeledError generic(String message) {
    return new ModeledError(Kind.GENERIC, message);
  }

  /** A failure forwarded from the primitives library. */
  static ModeledError primitives(String message) {
    return new ModeledError(Kind.PRIMITIVES, message);
  }

  String typeId() {
    return NAMESPACE + kind.shapeName;
  }
}
