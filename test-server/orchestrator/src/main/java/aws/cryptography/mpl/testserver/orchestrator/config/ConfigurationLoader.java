package aws.cryptography.mpl.testserver.orchestrator.config;

import com.fasterxml.jackson.core.JsonParser;
import com.fasterxml.jackson.databind.DeserializationFeature;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.json.JsonMapper;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

/**
 * Reads and parses the Configuration_Set.
 *
 * <p>STRICT_DUPLICATE_DETECTION: a duplicated port would otherwise be
 * last-one-wins while a reader of the file believes otherwise.
 * FAIL_ON_UNKNOWN_PROPERTIES: a typo is not a silently discarded
 * setting. {@code _comment} is the one allowed exception.
 */
public final class ConfigurationLoader {

  private final ObjectMapper mapper = JsonMapper
    .builder()
    .enable(JsonParser.Feature.STRICT_DUPLICATE_DETECTION)
    .enable(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES)
    .build();

  /**
   * Load a Configuration_Set from disk.
   *
   * @throws ConfigurationException if the file is missing or unparseable.
   */
  public ConfigurationSet load(Path path) {
    if (!Files.isRegularFile(path)) {
      throw new ConfigurationException(
        "Configuration_Set not found at " +
        path.toAbsolutePath() +
        ". Pass its location with --configuration-set <path>."
      );
    }
    try {
      ConfigurationSet set = mapper.readValue(
        path.toFile(),
        ConfigurationSet.class
      );
      if (set == null) {
        throw new ConfigurationException(
          "Configuration_Set at " +
          path.toAbsolutePath() +
          " parsed to nothing."
        );
      }
      return set;
    } catch (IOException e) {
      throw new ConfigurationException(
        "Could not parse the Configuration_Set at " +
        path.toAbsolutePath() +
        ": " +
        e.getMessage(),
        e
      );
    }
  }
}
