package aws.cryptography.mpl.testserver.server.error;

import aws.cryptography.mpl.testserver.server.model.GenericServerError;
import aws.cryptography.mpl.testserver.server.model.MPLTestServerException;
import aws.cryptography.mpl.testserver.server.model.MaterialProvidersClientError;
import software.amazon.cryptography.materialproviders.model.AwsCryptographicMaterialProvidersException;

/**
 * Maps any {@link Throwable} raised while handling an operation onto exactly one of
 * the two modeled error shapes, according to where the failure came from
 * (Requirement 4).
 *
 * <p>The boundary this class draws is the whole point of having two error shapes: a
 * test must be able to tell "the MPL rejected this" from "the harness is broken".
 * The mapping is:
 *
 * <ul>
 *   <li>An already-modeled error passes through with its type and message intact
 *       (Requirement 4.6).</li>
 *   <li>A failure raised by the Artifact_Under_Test becomes a
 *       {@link MaterialProvidersClientError} carrying the MPL's own message,
 *       unmodified, so a negative test can assert on it (Requirement 4.4).</li>
 *   <li>Anything else is a harness failure and becomes a
 *       {@link GenericServerError} whose non-empty message describes it
 *       (Requirement 4.7).</li>
 * </ul>
 *
 * <p><b>Recognising MPL-origin failures.</b> The MPL declares four unrelated
 * exception types -- {@code AwsCryptographicMaterialProvidersException},
 * {@code OpaqueError}, {@code OpaqueWithTextError} and {@code CollectionOfErrors} --
 * each extending {@link RuntimeException} directly, with no common MPL supertype to
 * catch. Matching on the package rather than enumerating the types means a new MPL
 * error type is classified correctly the day it appears, instead of being silently
 * misreported as a harness bug.
 *
 * <p>This is a pure function of the throwable and the operation name: no I/O, no
 * state.
 */
public final class ErrorClassifier {

    /**
     * Every type the transpiled MPL and its generated dependencies raise lives under
     * this package, so it identifies a failure as coming from the
     * Artifact_Under_Test rather than from the harness.
     */
    private static final String MPL_PACKAGE_PREFIX = "software.amazon.cryptography.";

    /**
     * Classify a failure by its origin.
     *
     * @param operationName the operation being handled, used to build a message a
     *     test author can act on.
     * @param failure the throwable raised by the handler body.
     * @return a {@link GenericServerError} or a {@link MaterialProvidersClientError};
     *     never {@code null}.
     */
    public MPLTestServerException classify(String operationName, Throwable failure) {
        // (4.6) Modeled errors pass through untouched.
        if (failure instanceof MPLTestServerException modeled) {
            return modeled;
        }

        // (4.4) MPL-origin failures forward the MPL's message verbatim.
        if (isFromArtifactUnderTest(failure)) {
            return MaterialProvidersClientError.builder()
                .message(mplMessage(failure))
                .build();
        }

        // (4.7) Everything else is a harness failure.
        return GenericServerError.builder()
            .message("Operation '" + operationName + "' failed: " + describe(failure))
            .build();
    }

    /**
     * Whether a throwable, or any exception that caused it, originates in the
     * Artifact_Under_Test.
     *
     * <p>The cause chain is walked because the MPL's own Dafny-generated code
     * sometimes surfaces a failure wrapped in a plain runtime exception; treating
     * such a failure as a harness bug would send a test author hunting in the wrong
     * codebase.
     */
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
     * Extract the message the MPL itself produced, so a negative test asserts on the
     * MPL's words and not on the harness's paraphrase.
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
                // A message-less MPL error is still an MPL error; name the type so the
                // response is never an empty string.
                return t.getClass().getSimpleName();
            }
            if (t.getCause() == t) {
                break;
            }
        }
        return describe(failure);
    }

    /** Build a non-empty description of a non-modeled failure (Requirement 4.7). */
    private static String describe(Throwable failure) {
        if (failure == null) {
            return "unknown error";
        }
        String type = failure.getClass().getName();
        String message = failure.getMessage();
        return (message == null || message.isEmpty()) ? type : type + ": " + message;
    }
}
