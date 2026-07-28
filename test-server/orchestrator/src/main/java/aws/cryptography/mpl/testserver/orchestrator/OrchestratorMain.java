package aws.cryptography.mpl.testserver.orchestrator;

import aws.cryptography.mpl.testserver.orchestrator.config.ConfigurationEntry;
import aws.cryptography.mpl.testserver.orchestrator.config.ConfigurationException;
import aws.cryptography.mpl.testserver.orchestrator.config.ConfigurationLoader;
import aws.cryptography.mpl.testserver.orchestrator.config.ConfigurationSet;
import aws.cryptography.mpl.testserver.orchestrator.config.ConfigurationValidator;
import aws.cryptography.mpl.testserver.orchestrator.launch.JavaServerLauncher;
import aws.cryptography.mpl.testserver.orchestrator.launch.LaunchedServer;
import aws.cryptography.mpl.testserver.orchestrator.launch.ServerLaunchException;
import aws.cryptography.mpl.testserver.orchestrator.run.GradleTestRunner;
import aws.cryptography.mpl.testserver.orchestrator.run.TestRunException;
import java.nio.file.Path;
import java.time.Duration;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

/**
 * Orchestrated conformance run: load, validate, launch, test, tear down.
 *
 * <p>Every failure mode exits non-zero with a stated reason -- there is no
 * path on which a run that did not exercise the artifact reports success.
 * A server that dies mid-run invalidates the result even if the suite
 * passed. Teardown is reverse order and never masks the real result.
 * Pairwise matrix deferred; adding a server is a config change.
 */
public final class OrchestratorMain {

  private static final Duration STARTUP_TIMEOUT = Duration.ofMinutes(3);

  private OrchestratorMain() {}

  public static void main(String[] args) {
    Path configurationSetPath = null;
    Path testServerRoot = null;

    for (int i = 0; i < args.length - 1; i++) {
      switch (args[i]) {
        case "--configuration-set" -> configurationSetPath = Path.of(args[++i]);
        case "--test-server-root" -> testServerRoot = Path.of(args[++i]);
        default -> {}
      }
    }

    if (configurationSetPath == null || testServerRoot == null) {
      System.err.println(
        "Usage: orchestrator --configuration-set <path> " +
        "--test-server-root <path>"
      );
      System.exit(2);
      return;
    }

    System.exit(run(configurationSetPath, testServerRoot));
  }

  static int run(Path configurationSetPath, Path testServerRoot) {
    ConfigurationSet set;
    try {
      set = new ConfigurationLoader().load(configurationSetPath);
      new ConfigurationValidator().validate(set);
    } catch (ConfigurationException e) {
      System.err.println("FAILED: " + e.getMessage());
      return 1;
    }

    System.out.println(
      "Configuration_Set: " + configurationSetPath.toAbsolutePath()
    );
    System.out.println("  product : " + set.product());
    System.out.println("  features: " + String.join(", ", set.features()));
    for (ConfigurationEntry entry : set.entries()) {
      System.out.println(
        "  server  : " +
        entry.name() +
        " on port " +
        entry.port() +
        " (" +
        entry.serverLocation().path() +
        ")"
      );
    }

    JavaServerLauncher launcher = new JavaServerLauncher(
      testServerRoot,
      STARTUP_TIMEOUT
    );
    List<LaunchedServer> launched = new ArrayList<>();

    try {
      for (ConfigurationEntry entry : set.entries()) {
        System.out.println("Launching " + entry.name() + " ...");
        launched.add(launcher.launch(entry));
        System.out.println("  ready at http://127.0.0.1:" + entry.port());
      }

      String targets = set
        .entries()
        .stream()
        .map(ConfigurationEntry::targetSpecification)
        .collect(Collectors.joining(","));

      System.out.println("Running the Tests against: " + targets);
      int status = new GradleTestRunner(testServerRoot).run(targets);

      for (LaunchedServer server : launched) {
        if (!server.isAlive()) {
          System.err.println(
            "FAILED: the " +
            server.entry().name() +
            " Language_Server exited during the run; the result is not " +
            "trustworthy."
          );
          return 1;
        }
      }

      if (status != 0) {
        System.err.println(
          "FAILED: the Tests reported failures (exit " + status + ")."
        );
        return status;
      }

      System.out.println(
        "PASSED: the Tests are green against " +
        launched
          .stream()
          .map(s -> s.entry().name())
          .collect(Collectors.joining(", ")) +
        "."
      );
      return 0;
    } catch (ServerLaunchException e) {
      System.err.println("FAILED: " + e.getMessage());
      return 1;
    } catch (TestRunException e) {
      System.err.println("FAILED: " + e.getMessage());
      return 1;
    } finally {
      for (int i = launched.size() - 1; i >= 0; i--) {
        LaunchedServer server = launched.get(i);
        System.out.println("Stopping " + server.entry().name() + " ...");
        try {
          server.close();
        } catch (RuntimeException e) {
          System.err.println(
            "  warning: could not cleanly stop " +
            server.entry().name() +
            ": " +
            e.getMessage()
          );
        }
      }
    }
  }
}
