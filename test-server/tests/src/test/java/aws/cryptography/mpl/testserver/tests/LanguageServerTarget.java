package aws.cryptography.mpl.testserver.tests;

import java.net.URI;
import java.util.Objects;

/**
 * One Language_Server the Tests can drive, identified by the tuple of its language,
 * its major version, and its endpoint (Requirement 7.7).
 *
 * <p>The identity is deliberately a tuple rather than a bare language name. The MPL
 * can have two concurrently supported major versions, and when it does, {@code
 * java-v1} and {@code java-v2} must be separately nameable -- both in configuration
 * and in test-execution names. Building that in now means adding a version later is a
 * configuration change rather than a refactor of every test name.
 *
 * @param language the implementation language, lower-case (for example {@code java}).
 * @param majorVersion the MPL major version this server exposes; at least 1.
 * @param endpoint the base URL the server is reachable at.
 */
public record LanguageServerTarget(String language, int majorVersion, URI endpoint) {

    public LanguageServerTarget {
        Objects.requireNonNull(language, "language cannot be null");
        Objects.requireNonNull(endpoint, "endpoint cannot be null");
        if (language.isBlank()) {
            throw new IllegalArgumentException("language cannot be blank");
        }
        if (majorVersion < 1) {
            throw new IllegalArgumentException(
                "majorVersion must be at least 1, but was " + majorVersion);
        }
    }

    /**
     * @return the short, stable name used in test-execution display names, for example
     *     {@code java-v1}.
     */
    public String name() {
        return language + "-v" + majorVersion;
    }

    @Override
    public String toString() {
        return name() + "@" + endpoint;
    }
}
