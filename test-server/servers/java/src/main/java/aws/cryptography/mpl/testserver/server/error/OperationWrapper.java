package aws.cryptography.mpl.testserver.server.error;

/**
 * Catch-all applied to every operation handler so that an unmodeled
 * exception never reaches the client as a bodyless 4xx/5xx with nothing
 * to debug. Every outcome is a modeled response, a GenericServerError,
 * or a MaterialProvidersClientError.
 */
public final class OperationWrapper {

  private final ErrorClassifier classifier;

  public OperationWrapper() {
    this(new ErrorClassifier());
  }

  public OperationWrapper(ErrorClassifier classifier) {
    this.classifier = classifier;
  }

  /**
   * A handler body that may throw checked exceptions without wrapping.
   */
  @FunctionalInterface
  public interface HandlerBody<T> {
    T run() throws Exception;
  }

  /**
   * Run a handler body under the catch-all contract.
   *
   * @param operationName used in framework-error messages.
   */
  public <T> T invoke(String operationName, HandlerBody<T> body) {
    try {
      return body.run();
    } catch (Throwable failure) {
      throw classifier.classify(operationName, failure);
    }
  }
}
