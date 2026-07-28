package aws.cryptography.mpl.testserver.orchestrator.config;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

/**
 * Where a Language_Server's implementation lives (Requirement 7.2).
 *
 * <p>{@code repository} is recorded even though every MPL Language_Server lives in this one
 * repository, so the field means something the day a server moves out -- and so that a
 * mismatched value is a loud configuration error rather than a silent assumption.
 *
 * @param repository the repository hosting the implementation.
 * @param path the path to the implementation, relative to that repository's root.
 */
@JsonIgnoreProperties({"_comment"})
public record ServerLocation(String repository, String path) {
}
