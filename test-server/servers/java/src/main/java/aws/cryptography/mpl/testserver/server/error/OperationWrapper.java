package aws.cryptography.mpl.testserver.server.error;

/**
 * The catch-all applied to every operation handler, so that each operation's outcome
 * is exactly one of: a successful modeled response, a {@code GenericServerError}, or
 * a {@code MaterialProvidersClientError} -- and never a bare HTTP error
 * (Requirement 4.5, 4.8).
 *
 * <p>Without this, an unmodeled exception reaches the client as a bodyless 4xx or
 * 5xx: no type, no message, nothing to debug. Since the classifier always yields one
 * of the two modeled errors, nothing unmodeled can escape a wrapped handler.
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
     * A handler body producing an operation's successful response, or throwing.
     *
     * <p>Declared to throw {@link Exception} rather than being a
     * {@link java.util.function.Supplier} so a body may propagate a checked
     * exception without wrapping it first.
     */
    @FunctionalInterface
    public interface HandlerBody<T> {
        T run() throws Exception;
    }

    /**
     * Run a handler body under the catch-all contract.
     *
     * @param operationName the operation name, used in framework-error messages.
     * @param body the handler body.
     * @return the successful response the body produced.
     */
    public <T> T invoke(String operationName, HandlerBody<T> body) {
        try {
            return body.run();
        } catch (Throwable failure) {
            throw classifier.classify(operationName, failure);
        }
    }
}
