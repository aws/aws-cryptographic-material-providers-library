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
 * Launches a Language_Server as a subprocess and waits for it to accept connections.
 *
 * <p>A subprocess rather than an in-process server, for two reasons. First, it is what a
 * non-JVM Language_Server will require, so the orchestrator's contract does not have to change
 * when one arrives. Second, an in-process server would share a JVM -- and a classpath -- with
 * the orchestrator, which is precisely the isolation a conformance harness should not give up.
 *
 * <p>Readiness is determined by the server ANNOUNCING itself on stdout, not by a sleep and not
 * by polling the port. A sleep is either too short (flaky) or too long (slow), and an open port
 * does not yet mean the service is wired up.
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
     * Start the server described by an entry and return a handle for shutting it down.
     *
     * @throws ServerLaunchException if the process cannot be started, exits early, or does not
     *     announce readiness within the timeout. In every case the process is cleaned up first,
     *     so a failed launch never leaves an orphan holding the port.
     */
    public LaunchedServer launch(ConfigurationEntry entry) {
        List<String> command = List.of(
            testServerRoot.resolve("gradlew").toString(),
            "-p", "servers/" + entry.language(),
            "runServer",
            "--args=" + entry.port(),
            "--console=plain");

        ProcessBuilder builder = new ProcessBuilder(command)
            .directory(testServerRoot.toFile())
            .redirectErrorStream(true);

        Process process;
        try {
            process = builder.start();
        } catch (IOException e) {
            throw new ServerLaunchException("Could not start the " + entry.name()
                + " Language_Server with: " + String.join(" ", command), e);
        }

        StringBuilder transcript = new StringBuilder();
        try (BufferedReader output = new BufferedReader(
            new InputStreamReader(process.getInputStream(), StandardCharsets.UTF_8))) {

            Instant deadline = Instant.now().plus(startupTimeout);
            String line;
            while (Instant.now().isBefore(deadline) && (line = output.readLine()) != null) {
                transcript.append(line).append(System.lineSeparator());
                if (line.contains(READY_MARKER)) {
                    // Drain the rest of the output on a daemon thread. Without this the pipe
                    // buffer eventually fills and the server blocks writing to stdout -- which
                    // looks exactly like a hung server, for a reason nowhere near the real one.
                    Thread drain = new Thread(() -> drain(process), entry.name() + "-output");
                    drain.setDaemon(true);
                    drain.start();
                    return new LaunchedServer(entry, process);
                }
            }
        } catch (IOException e) {
            terminate(process);
            throw new ServerLaunchException("Failed while reading " + entry.name()
                + " server output. Output so far:" + System.lineSeparator() + transcript, e);
        }

        terminate(process);
        if (!process.isAlive()) {
            throw new ServerLaunchException("The " + entry.name()
                + " Language_Server exited before it was ready. Output:"
                + System.lineSeparator() + transcript);
        }
        throw new ServerLaunchException("The " + entry.name()
            + " Language_Server did not report readiness within " + startupTimeout.toSeconds()
            + "s. Output:" + System.lineSeparator() + transcript);
    }

    private static void drain(Process process) {
        try (BufferedReader reader = new BufferedReader(
            new InputStreamReader(process.getInputStream(), StandardCharsets.UTF_8))) {
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
