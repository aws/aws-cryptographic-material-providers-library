package aws.cryptography.mpl.testserver.orchestrator.config;

/** A Configuration_Set could not be loaded or is invalid. */
public class ConfigurationException extends RuntimeException {

    public ConfigurationException(String message) {
        super(message);
    }

    public ConfigurationException(String message, Throwable cause) {
        super(message, cause);
    }
}
