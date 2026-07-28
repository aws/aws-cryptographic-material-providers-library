package aws.cryptography.mpl.testserver.server.launcher;

import aws.cryptography.mpl.testserver.server.handler.MPLTestServerHandlers;
import software.amazon.smithy.java.server.Server;

/**
 * Starts the Java Language_Server: the generated rpcv2Cbor service over HTTP, bound
 * to a port, delegating to the MPL as transpiled from this repository's Dafny source.
 *
 * <p>The port is resolved from, in order: the first command-line argument, the system
 * property {@value #PORT_PROPERTY}, the environment variable {@value #PORT_ENV}, then
 * {@value #DEFAULT_PORT}. It is validated rather than trusted, because a port
 * rejected at startup is far easier to diagnose than one that silently binds
 * somewhere unexpected.
 *
 * <p><b>Loopback only.</b> The server binds 127.0.0.1. It carries unwrapped plaintext
 * data keys in {@code OnEncrypt} responses over unencrypted HTTP -- which is accepted
 * for a harness driving test-only key material, and is the reason it must not be
 * reachable off the host. See the TestServer README.
 */
public final class ServerBootstrap {

    /** System property carrying the port to bind. */
    public static final String PORT_PROPERTY = "mpl.testserver.port";

    /** Environment variable equivalent of {@link #PORT_PROPERTY}. */
    public static final String PORT_ENV = "MPL_TESTSERVER_PORT";

    /**
     * The port used when none is configured. Matches the java entry's {@code port} in
     * {@code config/configuration-set.json}.
     */
    public static final int DEFAULT_PORT = 8101;

    private ServerBootstrap() {
    }

    public static void main(String[] args) throws InterruptedException {
        int port = resolvePort(args);

        MPLTestServerHandlers handlers = new MPLTestServerHandlers();
        Server server = Server.builder()
            .endpoints(port)
            .addService(handlers.service())
            .build();

        Runtime.getRuntime().addShutdownHook(new Thread(() -> {
            System.out.println("Shutting down the MPL TestServer (Java) ...");
            server.shutdown().join();
        }, "mpl-testserver-shutdown"));

        server.start();
        // Printed on one line and flushed immediately: the orchestrator's launcher
        // waits for this to know the server is accepting connections.
        System.out.println("MPL TestServer (Java) listening at http://127.0.0.1:" + port);
        System.out.println("Point the Tests at it with: "
            + "-Dmpl.testserver.targets=java:1=http://127.0.0.1:" + port);
        System.out.println("Press Ctrl-C to stop.");
        System.out.flush();

        // Block for the process lifetime; the shutdown hook handles SIGINT/SIGTERM.
        Thread.currentThread().join();
    }

    /**
     * Resolve and validate the port.
     *
     * @throws IllegalArgumentException if the configured value is not an integer in
     *     1..65535.
     */
    static int resolvePort(String[] args) {
        String raw = null;
        if (args != null && args.length > 0 && args[0] != null && !args[0].isBlank()) {
            raw = args[0].trim();
        } else {
            String property = System.getProperty(PORT_PROPERTY);
            if (property != null && !property.isBlank()) {
                raw = property.trim();
            } else {
                String env = System.getenv(PORT_ENV);
                if (env != null && !env.isBlank()) {
                    raw = env.trim();
                }
            }
        }
        if (raw == null) {
            return DEFAULT_PORT;
        }
        int port;
        try {
            port = Integer.parseInt(raw);
        } catch (NumberFormatException e) {
            throw new IllegalArgumentException(
                "Invalid port '" + raw + "': must be an integer in 1..65535");
        }
        if (port < 1 || port > 65535) {
            throw new IllegalArgumentException(
                "Invalid port " + port + ": must be in the range 1..65535");
        }
        return port;
    }
}
