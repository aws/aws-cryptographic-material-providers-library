package aws.cryptography.mpl.testserver.orchestrator.launch;

/** A Language_Server could not be started, or never became ready. */
public class ServerLaunchException extends RuntimeException {

  public ServerLaunchException(String message) {
    super(message);
  }

  public ServerLaunchException(String message, Throwable cause) {
    super(message, cause);
  }
}
