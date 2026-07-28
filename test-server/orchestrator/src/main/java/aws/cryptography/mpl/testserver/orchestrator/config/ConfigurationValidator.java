package aws.cryptography.mpl.testserver.orchestrator.config;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

/**
 * Validates a Configuration_Set.
 *
 * <p>Collects every fault instead of throwing on the first, and runs to
 * completion BEFORE anything is launched -- so a bad port does not leave
 * orphaned processes. A port collision names both languages. An
 * out-of-catalog feature is almost always a typo that would otherwise
 * mean a feature silently never ran (Requirement 7.6).
 */
public final class ConfigurationValidator {

  /**
   * @throws ConfigurationException listing every fault found.
   */
  public void validate(ConfigurationSet set) {
    List<String> faults = new ArrayList<>();

    if (isBlank(set.product())) {
      faults.add("the Configuration_Set must declare a non-empty `product`");
    }
    Set<String> catalog = new HashSet<>();
    if (set.features() == null || set.features().isEmpty()) {
      faults.add(
        "the Configuration_Set must declare a non-empty `features` catalog"
      );
    } else {
      catalog.addAll(set.features());
    }
    if (set.entries() == null || set.entries().isEmpty()) {
      faults.add("the Configuration_Set must declare at least one entry");
      // Nothing further can be checked; report what is known.
      throw failure(faults);
    }

    Map<Integer, String> portOwners = new HashMap<>();
    Set<String> names = new HashSet<>();

    for (ConfigurationEntry entry : set.entries()) {
      String who = isBlank(entry.language())
        ? "<entry with no language>"
        : entry.language();

      if (isBlank(entry.language())) {
        faults.add("an entry is missing a non-empty `language`");
      }
      if (entry.majorVersion() == null) {
        faults.add(who + ": missing `majorVersion`");
      } else if (entry.majorVersion() < 1) {
        faults.add(
          who +
          ": `majorVersion` must be at least 1, but was " +
          entry.majorVersion()
        );
      }
      if (entry.port() == null) {
        faults.add(who + ": missing `port`");
      } else if (entry.port() < 1 || entry.port() > 65535) {
        faults.add(
          who + ": `port` must be in 1..65535, but was " + entry.port()
        );
      } else {
        String previous = portOwners.putIfAbsent(entry.port(), who);
        if (previous != null) {
          faults.add(
            "port " +
            entry.port() +
            " is claimed by both " +
            previous +
            " and " +
            who +
            "; ports must be unique across the Configuration_Set"
          );
        }
      }

      if (
        entry.language() != null &&
        entry.majorVersion() != null &&
        !names.add(entry.name())
      ) {
        faults.add(
          "two entries share the identity " +
          entry.name() +
          "; each (language, majorVersion) pair must appear once"
        );
      }

      ServerLocation location = entry.serverLocation();
      if (location == null) {
        faults.add(who + ": missing `serverLocation`");
      } else {
        if (isBlank(location.repository())) {
          faults.add(who + ": `serverLocation.repository` is missing or empty");
        }
        if (isBlank(location.path())) {
          faults.add(who + ": `serverLocation.path` is missing or empty");
        }
      }

      faults.addAll(
        unknownFeatures(
          who,
          "supportedFeatures",
          entry.supportedFeatures(),
          catalog
        )
      );
      faults.addAll(
        unknownFeatures(
          who,
          "unsupportedFeatures",
          entry.unsupportedFeatures(),
          catalog
        )
      );
    }

    if (!faults.isEmpty()) {
      throw failure(faults);
    }
  }

  private static List<String> unknownFeatures(
    String who,
    String field,
    List<String> declared,
    Set<String> catalog
  ) {
    List<String> faults = new ArrayList<>();
    if (declared == null) {
      return faults;
    }
    for (String feature : declared) {
      if (!catalog.contains(feature)) {
        faults.add(
          who +
          ": `" +
          field +
          "` names '" +
          feature +
          "', which is not in the Configuration_Set's `features` catalog"
        );
      }
    }
    return faults;
  }

  private static ConfigurationException failure(List<String> faults) {
    StringBuilder message = new StringBuilder(
      "The Configuration_Set is invalid (" +
      faults.size() +
      (faults.size() == 1 ? " fault" : " faults") +
      "):"
    );
    for (String fault : faults) {
      message.append("\n  - ").append(fault);
    }
    return new ConfigurationException(message.toString());
  }

  private static boolean isBlank(String value) {
    return value == null || value.isBlank();
  }
}
