package aws.cryptography.mpl.testserver.orchestrator.config;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import java.util.List;

/**
 * One Configuration_Entry: everything needed to launch and identify a
 * single Language_Server.
 *
 * <p>There is deliberately no {@code libraryRepository} field. The MPL's
 * artifact under test is always THIS repository's Dafny source transpiled
 * from the working tree; a coordinates field would record a constant and
 * falsely imply the library could come from elsewhere. The
 * Feature_Declaration is inline for the same reason -- no MPL language
 * has its own repository. {@code majorVersion} is part of the server's
 * identity so two concurrently supported majors stay separately nameable.
 */
@JsonIgnoreProperties({ "_comment" })
public record ConfigurationEntry(
  String language,
  Integer majorVersion,
  Integer port,
  List<String> supportedFeatures,
  List<String> unsupportedFeatures,
  ServerLocation serverLocation
) {
  /** Stable short name, e.g. {@code java-v1}. */
  public String name() {
    return language + "-v" + majorVersion;
  }

  /** Target-specification entry the Tests consume for this server. */
  public String targetSpecification() {
    return language + ":" + majorVersion + "=http://127.0.0.1:" + port;
  }
}
