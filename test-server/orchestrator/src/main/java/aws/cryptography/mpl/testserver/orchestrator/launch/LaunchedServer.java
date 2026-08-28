package aws.cryptography.mpl.testserver.orchestrator.launch;

import aws.cryptography.mpl.testserver.orchestrator.config.ConfigurationEntry;
import java.util.concurrent.TimeUnit;

/**
 * A running Language_Server and the means to stop it.
 *
 * <p>{@link #close()} is idempotent and escalates destroy ->
 * destroyForcibly.
 */
public final class LaunchedServer implements AutoCloseable {

  private final ConfigurationEntry entry;
  private final Process process;

  LaunchedServer(ConfigurationEntry entry, Process process) {
    this.entry = entry;
    this.process = process;
  }

  /** The entry this server was launched from. */
  public ConfigurationEntry entry() {
    return entry;
  }

  /** The endpoint the Tests should target. */
  public String endpoint() {
    return "http://127.0.0.1:" + entry.port();
  }

  /** Whether the process is still running. */
  public boolean isAlive() {
    return process.isAlive();
  }

  @Override
  public void close() {
    if (!process.isAlive()) {
      return;
    }
    process.destroy();
    try {
      if (!process.waitFor(15, TimeUnit.SECONDS)) {
        process.destroyForcibly();
      }
    } catch (InterruptedException e) {
      Thread.currentThread().interrupt();
      process.destroyForcibly();
    }
  }
}
