package aws.cryptography.mpl.testserver.tests;

import java.net.URI;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Optional;

/**
 * The set of language servers resolved once from runtime configuration.
 *
 * <p>The tests are endpoint-only: a server is located exclusively through
 * {@value #TARGETS_PROPERTY} or {@value #TARGETS_ENV}, a comma-separated list of
 * {@code <language>:<majorVersion>=<endpointUrl>} entries. There is deliberately no
 * default and no in-process fallback -- a default would let a run that reached no
 * server look like a pass. Pairwise matrix deferred: with one target it collapses
 * to a self-pair.
 */
public final class LanguageServerRegistry {

  /** Runtime-config key: comma-separated {@code language:major=url} entries. */
  public static final String TARGETS_PROPERTY = "mpl.testserver.targets";

  /** Environment-variable equivalent of {@link #TARGETS_PROPERTY}. */
  public static final String TARGETS_ENV = "MPL_TESTSERVER_TARGETS";

  private static volatile LanguageServerRegistry instance;

  private final List<LanguageServerTarget> targets;

  private LanguageServerRegistry(List<LanguageServerTarget> targets) {
    this.targets = List.copyOf(targets);
  }

  /**
   * Return the process-wide registry, resolving on first access. Safe to call from
   * a static {@code @MethodSource}.
   */
  public static LanguageServerRegistry shared() {
    LanguageServerRegistry local = instance;
    if (local == null) {
      synchronized (LanguageServerRegistry.class) {
        local = instance;
        if (local == null) {
          local =
            new LanguageServerRegistry(
              parse(
                configured()
                  .orElseThrow(() ->
                    new IllegalStateException(
                      "No Language_Server targets configured. The Tests are endpoint-only: " +
                      "supply -D" +
                      TARGETS_PROPERTY +
                      " or the " +
                      TARGETS_ENV +
                      " environment variable as a comma-separated list of " +
                      "<language>:<majorVersion>=<endpointUrl> entries, e.g. " +
                      "java:1=http://127.0.0.1:8101. Run `make orchestrate` to have " +
                      "this supplied automatically, or start a server with " +
                      "`make run-server` and use `make test`."
                    )
                  )
              )
            );
          instance = local;
        }
      }
    }
    return local;
  }

  /** Every configured target, in the order configured. */
  public List<LanguageServerTarget> targets() {
    return targets;
  }

  /**
   * The first configured target. Meta tests run against one target only since they
   * exercise the wire contract, not MPL behavior.
   */
  public LanguageServerTarget primary() {
    return targets.get(0);
  }

  private static Optional<String> configured() {
    String property = System.getProperty(TARGETS_PROPERTY);
    if (property != null && !property.isBlank()) {
      return Optional.of(property);
    }
    String env = System.getenv(TARGETS_ENV);
    if (env != null && !env.isBlank()) {
      return Optional.of(env);
    }
    return Optional.empty();
  }

  /**
   * Parse the targets specification. Every fault quotes the offending entry because
   * a misconfigured target otherwise surfaces much later as a meaningless connection
   * failure.
   */
  static List<LanguageServerTarget> parse(String specification) {
    Map<String, LanguageServerTarget> byName = new LinkedHashMap<>();
    List<LanguageServerTarget> parsed = new ArrayList<>();

    for (String rawEntry : specification.split(",")) {
      String entry = rawEntry.trim();
      if (entry.isEmpty()) {
        continue;
      }
      int equals = entry.indexOf('=');
      if (equals < 0) {
        throw new IllegalStateException(
          "Malformed target entry '" +
          entry +
          "': expected <language>:<majorVersion>=<endpointUrl>."
        );
      }
      String identity = entry.substring(0, equals).trim();
      String endpoint = entry.substring(equals + 1).trim();

      int colon = identity.indexOf(':');
      if (colon < 0) {
        throw new IllegalStateException(
          "Malformed target identity '" +
          identity +
          "' in entry '" +
          entry +
          "': expected <language>:<majorVersion>."
        );
      }
      String language = identity.substring(0, colon).trim();
      String majorVersionText = identity.substring(colon + 1).trim();

      int majorVersion;
      try {
        majorVersion = Integer.parseInt(majorVersionText);
      } catch (NumberFormatException e) {
        throw new IllegalStateException(
          "Malformed majorVersion '" +
          majorVersionText +
          "' in entry '" +
          entry +
          "': expected an integer of at least 1."
        );
      }
      if (endpoint.isEmpty()) {
        throw new IllegalStateException(
          "Missing endpoint URL in target entry '" + entry + "'."
        );
      }

      LanguageServerTarget target;
      try {
        target =
          new LanguageServerTarget(
            language,
            majorVersion,
            URI.create(endpoint)
          );
      } catch (IllegalArgumentException e) {
        throw new IllegalStateException(
          "Invalid target entry '" + entry + "': " + e.getMessage(),
          e
        );
      }

      LanguageServerTarget existing = byName.putIfAbsent(target.name(), target);
      if (existing != null) {
        throw new IllegalStateException(
          "Duplicate target '" +
          target.name() +
          "' configured at both " +
          existing.endpoint() +
          " and " +
          target.endpoint() +
          "."
        );
      }
      parsed.add(target);
    }

    if (parsed.isEmpty()) {
      throw new IllegalStateException(
        "No target entries parsed from '" + specification + "'."
      );
    }
    return parsed;
  }
}
