package aws.cryptography.mpl.testserver.orchestrator.config;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

/**
 * Where a Language_Server's implementation lives.
 *
 * <p>{@code repository} is recorded even though every MPL server currently
 * lives in this one repository, so a mismatched value is a loud error
 * rather than a silent assumption.
 */
@JsonIgnoreProperties({ "_comment" })
public record ServerLocation(String repository, String path) {}
