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
 * <p>Two parser settings are deliberate:
 * <ul>
 *   <li><b>Strict duplicate detection.</b> A repeated JSON key is an error, not a
 *       last-one-wins. A duplicated {@code port} would otherwise silently take one value while
 *       a reader of the file believes it takes the other.</li>
 *   <li><b>Fail on unknown properties.</b> A mistyped field name is an error rather than a
 *       silently discarded setting that leaves the run using a default nobody chose. The one
 *       exception is {@code _comment}, declared on each record, so the file can document
 *       itself.</li>
 * </ul>
 */
public final class ConfigurationLoader {

    private final ObjectMapper mapper = JsonMapper.builder()
        .enable(JsonParser.Feature.STRICT_DUPLICATE_DETECTION)
        .enable(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES)
        .build();

    /**
     * Load a Configuration_Set from disk.
     *
     * @throws ConfigurationException if the file is missing or cannot be parsed. The message
     *     always names the path, since "could not parse" without one is useless in a build log.
     */
    public ConfigurationSet load(Path path) {
        if (!Files.isRegularFile(path)) {
            throw new ConfigurationException(
                "Configuration_Set not found at " + path.toAbsolutePath()
                    + ". Pass its location with --configuration-set <path>.");
        }
        try {
            ConfigurationSet set = mapper.readValue(path.toFile(), ConfigurationSet.class);
            if (set == null) {
                throw new ConfigurationException(
                    "Configuration_Set at " + path.toAbsolutePath() + " parsed to nothing.");
            }
            return set;
        } catch (IOException e) {
            throw new ConfigurationException(
                "Could not parse the Configuration_Set at " + path.toAbsolutePath() + ": "
                    + e.getMessage(), e);
        }
    }
}
