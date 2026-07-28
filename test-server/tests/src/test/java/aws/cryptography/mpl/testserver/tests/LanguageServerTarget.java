package aws.cryptography.mpl.testserver.tests;

import java.net.URI;
import java.util.Objects;

/**
 * One language server the tests can drive. Identity is a (language, majorVersion)
 * tuple so two concurrently supported majors stay separately nameable -- adding a
 * version later is a configuration change, not a refactor of every test name.
 */
public record LanguageServerTarget(
  String language,
  int majorVersion,
  URI endpoint
) {
  public LanguageServerTarget {
    Objects.requireNonNull(language, "language cannot be null");
    Objects.requireNonNull(endpoint, "endpoint cannot be null");
    if (language.isBlank()) {
      throw new IllegalArgumentException("language cannot be blank");
    }
    if (majorVersion < 1) {
      throw new IllegalArgumentException(
        "majorVersion must be at least 1, but was " + majorVersion
      );
    }
  }

  /** Short stable name for test display, e.g. {@code java-v1}. */
  public String name() {
    return language + "-v" + majorVersion;
  }

  @Override
  public String toString() {
    return name() + "@" + endpoint;
  }
}
