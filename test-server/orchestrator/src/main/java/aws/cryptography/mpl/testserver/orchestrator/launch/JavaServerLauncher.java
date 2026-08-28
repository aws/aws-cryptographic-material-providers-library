package aws.cryptography.mpl.testserver.orchestrator.launch;

import aws.cryptography.mpl.testserver.orchestrator.config.ConfigurationEntry;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.nio.file.Path;
import java.time.Duration;
import java.time.Instant;
import java.util.List;

/**
 * Launches a Language_Server as a subprocess and waits for readiness.
 *
 * <p>A subprocess -- not in-process -- because that is what a non-JVM server
 * will need, and because sharing a JVM/classpath gives up the isolation a
 * conformance harness should keep. Readiness comes from the server
 * announcing itself on stdout, not a sleep (too short = flaky, too long =
 * slow) and not port polling (an open port does not mean the service is
 * wired up). Output is drained on a daemon thread or the pipe buffer
 * fills and the server blocks on stdout -- which looks exactly like a
 * hang for a reason nowhere near the real one. Any failure terminates the
 * process so no orphan holds the port.
 */
public final class JavaServerLauncher {

  /** The line {@code ServerBootstrap} prints once it is listening. */
  private static final String READY_MARKER = "listening at";

  private final Path testServerRoot;
  private final Duration startupTimeout;

  public JavaServerLauncher(Path testServerRoot, Duration startupTimeout) {
    this.testServerRoot = testServerRoot;
    this.startupTimeout = startupTimeout;
  }

  /**
   * Start the server described by an entry and return a handle.
   *
   * @throws ServerLaunchException if the process cannot be started, exits
   *     early, or does not announce readiness within the timeout. The
   *     process is always cleaned up first.
   */
  public LaunchedServer launch(ConfigurationEntry entry) {
    List<String> command = List.of(
      testServerRoot.resolve("gradlew").toString(),
      "-p",
      "servers/" + entry.language(),
      "runServer",
      "--args=" + entry.port(),
      "--console=plain"
    );

    ProcessBuilder builder = new ProcessBuilder(command)
      .directory(testServerRoot.toFile())
      .redirectErrorStream(true);

    Process process;
    try {
      process = builder.start();
    } catch (IOException e) {
      throw new ServerLaunchException(
        "Could not start the " +
        entry.name() +
        " Language_Server with: " +
        String.join(" ", command),
        e
      );
    }

    StringBuilder transcript = new StringBuilder();
    try (
      BufferedReader output = new BufferedReader(
        new InputStreamReader(process.getInputStream(), StandardCharsets.UTF_8)
      )
    ) {
      Instant deadline = Instant.now().plus(startupTimeout);
      String line;
      while (
        Instant.now().isBefore(deadline) && (line = output.readLine()) != null
      ) {
        transcript.append(line).append(System.lineSeparator());
        if (line.contains(READY_MARKER)) {
          // Drain output on a daemon thread to prevent pipe-buffer deadlock.
          Thread drain = new Thread(
            () -> drain(process),
            entry.name() + "-output"
          );
          drain.setDaemon(true);
          drain.start();
          return new LaunchedServer(entry, process);
        }
      }
    } catch (IOException e) {
      terminate(process);
      throw new ServerLaunchException(
        "Failed while reading " +
        entry.name() +
        " server output. Output so far:" +
        System.lineSeparator() +
        transcript,
        e
      );
    }

    terminate(process);
    if (!process.isAlive()) {
      throw new ServerLaunchException(
        "The " +
        entry.name() +
        " Language_Server exited before it was ready. Output:" +
        System.lineSeparator() +
        transcript
      );
    }
    throw new ServerLaunchException(
      "The " +
      entry.name() +
      " Language_Server did not report readiness within " +
      startupTimeout.toSeconds() +
      "s. Output:" +
      System.lineSeparator() +
      transcript
    );
  }

  private static void drain(Process process) {
    try (
      BufferedReader reader = new BufferedReader(
        new InputStreamReader(process.getInputStream(), StandardCharsets.UTF_8)
      )
    ) {
      while (reader.readLine() != null) {
        // Discarded: the server's own log is not the orchestrator's report.
      }
    } catch (IOException ignored) {
      // The process ended; nothing left to drain.
    }
  }

  private static void terminate(Process process) {
    process.destroy();
    try {
      if (!process.waitFor(10, java.util.concurrent.TimeUnit.SECONDS)) {
        process.destroyForcibly();
      }
    } catch (InterruptedException e) {
      Thread.currentThread().interrupt();
      process.destroyForcibly();
    }
  }
}
