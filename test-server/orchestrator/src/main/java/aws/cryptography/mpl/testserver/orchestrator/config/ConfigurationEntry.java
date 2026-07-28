package aws.cryptography.mpl.testserver.orchestrator.config;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import java.util.List;

/**
 * One Configuration_Entry: everything needed to build, launch, and reason about a single
 * Language_Server (Requirement 7.2).
 *
 * <p><b>There is deliberately no {@code libraryRepository} field</b> (Requirement 7.4). The
 * ESDK TestServer's schema carries per-entry library coordinates because each language's ESDK
 * lives in its own repository. The MPL's Artifact_Under_Test is always THIS repository's Dafny
 * source, transpiled from the working tree. A coordinates field would record a constant, and
 * imply -- falsely -- that the library could come from somewhere else.
 *
 * <p>The Feature_Declaration is inline for the same reason: no MPL language has its own
 * repository to declare it in (Requirement 7.5).
 *
 * @param language the implementation language, lower-case.
 * @param majorVersion the MPL major version this server exposes. Part of the server's identity
 *     alongside the language, so two concurrently supported majors stay separately nameable
 *     (Requirement 7.7).
 * @param port the port to bind, unique across the set.
 * @param supportedFeatures features from the catalog this server implements.
 * @param unsupportedFeatures features from the catalog it does not.
 * @param serverLocation where the server's implementation lives.
 */
@JsonIgnoreProperties({"_comment"})
public record ConfigurationEntry(
    String language,
    Integer majorVersion,
    Integer port,
    List<String> supportedFeatures,
    List<String> unsupportedFeatures,
    ServerLocation serverLocation
) {

    /** @return the stable short name for this server, for example {@code java-v1}. */
    public String name() {
        return language + "-v" + majorVersion;
    }

    /** @return the target-specification entry the Tests consume for this server. */
    public String targetSpecification() {
        return language + ":" + majorVersion + "=http://127.0.0.1:" + port;
    }
}
