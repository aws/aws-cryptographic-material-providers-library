package aws.cryptography.mpl.testserver.orchestrator.run;

/** The Tests could not be run at all -- distinct from the Tests running and failing. */
public class TestRunException extends RuntimeException {

  public TestRunException(String message) {
    super(message);
  }

  public TestRunException(String message, Throwable cause) {
    super(message, cause);
  }
}
