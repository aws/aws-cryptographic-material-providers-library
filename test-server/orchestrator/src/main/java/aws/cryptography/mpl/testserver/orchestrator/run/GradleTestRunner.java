package aws.cryptography.mpl.testserver.orchestrator.run;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;

/**
 * Runs the Tests against a set of launched Language_Servers.
 *
 * <p>{@code cleanTest} because Gradle caches results and would report the
 * suite up-to-date without running it -- a green result proving nothing.
 * {@code --no-daemon} so {@code -D} properties reach a fresh JVM.
 * {@code -Dmpl.testserver.targets} is the single runtime input; the
 * Tests have no default.
 */
public final class GradleTestRunner {

  private final Path testServerRoot;

  public GradleTestRunner(Path testServerRoot) {
    this.testServerRoot = testServerRoot;
  }

  /**
   * Run the Tests.
   *
   * @return the suite's exit status: zero on success.
   */
  public int run(String targetSpecification) {
    List<String> command = new ArrayList<>(
      List.of(
        testServerRoot.resolve("gradlew").toString(),
        "-p",
        "tests",
        "cleanTest",
        "test",
        "--no-daemon",
        "--console=plain",
        "-Dmpl.testserver.targets=" + targetSpecification
      )
    );

    ProcessBuilder builder = new ProcessBuilder(command)
      .directory(testServerRoot.toFile())
      .redirectErrorStream(true);

    try {
      Process process = builder.start();
      // Stream output live rather than buffering.
      try (
        BufferedReader reader = new BufferedReader(
          new InputStreamReader(
            process.getInputStream(),
            StandardCharsets.UTF_8
          )
        )
      ) {
        String line;
        while ((line = reader.readLine()) != null) {
          System.out.println(line);
        }
      }
      return process.waitFor();
    } catch (IOException e) {
      throw new TestRunException(
        "Could not run the Tests with: " + String.join(" ", command),
        e
      );
    } catch (InterruptedException e) {
      Thread.currentThread().interrupt();
      throw new TestRunException("Interrupted while running the Tests", e);
    }
  }
}
