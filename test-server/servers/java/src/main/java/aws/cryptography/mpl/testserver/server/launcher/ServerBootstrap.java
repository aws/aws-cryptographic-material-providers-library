package aws.cryptography.mpl.testserver.server.launcher;

import aws.cryptography.mpl.testserver.server.handler.MPLTestServerHandlers;
import software.amazon.smithy.java.server.Server;

/**
 * Starts the rpcv2Cbor test server, bound to loopback only. Carries
 * unwrapped plaintext data keys over unencrypted HTTP -- accepted for
 * test-only material but must not be reachable off-host.
 *
 * <p>Port resolved from: CLI arg, system property
 * {@value #PORT_PROPERTY}, env var {@value #PORT_ENV}, then
 * {@value #DEFAULT_PORT}. Port is validated, not trusted.
 */
public final class ServerBootstrap {

  public static final String PORT_PROPERTY = "mpl.testserver.port";

  public static final String PORT_ENV = "MPL_TESTSERVER_PORT";

  /**
   * Default port; matches the java entry in
   * {@code config/configuration-set.json}.
   */
  public static final int DEFAULT_PORT = 8101;

  private ServerBootstrap() {}

  public static void main(String[] args) throws InterruptedException {
    int port = resolvePort(args);

    MPLTestServerHandlers handlers = new MPLTestServerHandlers();
    Server server = Server
      .builder()
      .endpoints(port)
      .addService(handlers.service())
      .build();

    Runtime
      .getRuntime()
      .addShutdownHook(
        new Thread(
          () -> {
            System.out.println("Shutting down the MPL TestServer (Java) ...");
            server.shutdown().join();
          },
          "mpl-testserver-shutdown"
        )
      );

    server.start();
    // The orchestrator waits for this line to know the server is up.
    System.out.println(
      "MPL TestServer (Java) listening at http://127.0.0.1:" + port
    );
    System.out.println(
      "Point the Tests at it with: " +
      "-Dmpl.testserver.targets=java:1=http://127.0.0.1:" +
      port
    );
    System.out.println("Press Ctrl-C to stop.");
    System.out.flush();

    Thread.currentThread().join();
  }

  /**
   * Resolve and validate the port.
   *
   * @throws IllegalArgumentException if the configured value is not an
   *     integer in 1..65535.
   */
  static int resolvePort(String[] args) {
    String raw = null;
    if (
      args != null && args.length > 0 && args[0] != null && !args[0].isBlank()
    ) {
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
        "Invalid port '" + raw + "': must be an integer in 1..65535"
      );
    }
    if (port < 1 || port > 65535) {
      throw new IllegalArgumentException(
        "Invalid port " + port + ": must be in the range 1..65535"
      );
    }
    return port;
  }
}
