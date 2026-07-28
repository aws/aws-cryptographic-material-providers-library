package aws.cryptography.mpl.testserver.orchestrator.config;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import java.util.List;

/**
 * The Configuration_Set: declarative description of every Language_Server.
 *
 * <p>{@code _comment} is ignored so the file can carry rationale, but every
 * other unknown key is a hard error -- a mistyped field name must not be
 * silently discarded.
 */
@JsonIgnoreProperties({ "_comment" })
public record ConfigurationSet(
  String product,
  List<String> features,
  List<ConfigurationEntry> entries
) {}
