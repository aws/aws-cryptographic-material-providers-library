package aws.cryptography.mpl.testserver.orchestrator.config;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import java.util.List;

/**
 * The Configuration_Set: the declarative description of every Language_Server
 * (Requirement 7.1).
 *
 * <p>{@code _comment} is ignored so the file can carry its own rationale, but every other
 * unknown key is a hard error -- a mistyped field name must not be silently discarded, leaving
 * a run to use a default nobody intended.
 *
 * @param product the product under test. Always {@code mpl} here; present so the schema is
 *     shared with the other TestServers in this family.
 * @param features the feature catalog every {@code Feature_Declaration} draws from.
 * @param entries one entry per Language_Server.
 */
@JsonIgnoreProperties({"_comment"})
public record ConfigurationSet(
    String product,
    List<String> features,
    List<ConfigurationEntry> entries
) {
}
