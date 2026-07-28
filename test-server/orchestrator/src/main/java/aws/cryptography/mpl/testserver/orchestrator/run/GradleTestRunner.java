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
 * <p>Three flags carry weight:
 * <ul>
 *   <li><b>{@code cleanTest}</b> -- Gradle caches test results and will report the suite
 *       "up-to-date" without running it. Against a freshly launched server that would be a
 *       green result proving nothing.</li>
 *   <li><b>{@code --no-daemon}</b> -- so the {@code -D} system properties reach a fresh JVM
 *       rather than being ignored by a warm daemon started with different ones.</li>
 *   <li><b>{@code -Dmpl.testserver.targets}</b> -- the single runtime input that tells the Tests
 *       where every server is. The Tests have no default, so this is what makes them runnable
 *       at all (Requirement 9.2).</li>
 * </ul>
 */
public final class GradleTestRunner {

    private final Path testServerRoot;

    public GradleTestRunner(Path testServerRoot) {
        this.testServerRoot = testServerRoot;
    }

    /**
     * Run the Tests.
     *
     * @param targetSpecification the comma-separated {@code language:major=url} entries.
     * @return the suite's exit status: zero on success.
     */
    public int run(String targetSpecification) {
        List<String> command = new ArrayList<>(List.of(
            testServerRoot.resolve("gradlew").toString(),
            "-p", "tests",
            "cleanTest", "test",
            "--no-daemon",
            "--console=plain",
            "-Dmpl.testserver.targets=" + targetSpecification));

        ProcessBuilder builder = new ProcessBuilder(command)
            .directory(testServerRoot.toFile())
            .redirectErrorStream(true);

        try {
            Process process = builder.start();
            // Streamed rather than captured: a developer watching an orchestrated run wants the
            // per-test output as it happens, not a wall of text after the fact.
            try (BufferedReader reader = new BufferedReader(
                new InputStreamReader(process.getInputStream(), StandardCharsets.UTF_8))) {
                String line;
                while ((line = reader.readLine()) != null) {
                    System.out.println(line);
                }
            }
            return process.waitFor();
        } catch (IOException e) {
            throw new TestRunException("Could not run the Tests with: "
                + String.join(" ", command), e);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            throw new TestRunException("Interrupted while running the Tests", e);
        }
    }
}
