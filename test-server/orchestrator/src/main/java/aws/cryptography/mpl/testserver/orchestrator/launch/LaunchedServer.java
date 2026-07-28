package aws.cryptography.mpl.testserver.orchestrator.launch;

import aws.cryptography.mpl.testserver.orchestrator.config.ConfigurationEntry;
import java.util.concurrent.TimeUnit;

/**
 * A running Language_Server, and the means to stop it.
 *
 * <p>{@link #close()} is idempotent and escalates from a polite {@code destroy} to a
 * {@code destroyForcibly}, because a server that ignores the first signal must not be able to
 * keep the orchestrator's port -- or the orchestrator itself -- hostage.
 */
public final class LaunchedServer implements AutoCloseable {

    private final ConfigurationEntry entry;
    private final Process process;

    LaunchedServer(ConfigurationEntry entry, Process process) {
        this.entry = entry;
        this.process = process;
    }

    /** @return the entry this server was launched from. */
    public ConfigurationEntry entry() {
        return entry;
    }

    /** @return the endpoint the Tests should be pointed at. */
    public String endpoint() {
        return "http://127.0.0.1:" + entry.port();
    }

    /** @return whether the process is still running. */
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
