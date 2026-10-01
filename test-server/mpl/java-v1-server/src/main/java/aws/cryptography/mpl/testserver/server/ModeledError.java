package aws.cryptography.mpl.testserver.server;

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

  private ModeledError(Kind kind, String message) {
    super(message);
    this.kind = kind;
  }

  /** A framework-side failure: bad request, unknown operation, bad handle. */
  static ModeledError generic(String message) {
    return new ModeledError(Kind.GENERIC, message);
  }

  /** A failure raised by the Material Providers Library. */
  static ModeledError mpl(String message) {
    return new ModeledError(Kind.MPL, message);
  }

  String typeId() {
    return NAMESPACE + kind.shapeName;
  }
}
