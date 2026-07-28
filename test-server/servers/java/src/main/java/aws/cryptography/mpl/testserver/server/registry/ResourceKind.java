package aws.cryptography.mpl.testserver.server.registry;

/**
 * The kinds of MPL resource a {@link ResourceRegistry} entry can hold.
 *
 * <p>All resource ids share one Smithy shape, so the wire alone cannot prevent
 * a keyring id being passed where a MaterialProviders id belongs. Recording
 * the kind closes that gap: a mismatch becomes a clear error naming both
 * kinds, not a ClassCastException surfacing as an opaque server fault.
 */
public enum ResourceKind {
  /** A {@code MaterialProviders} instance. */
  MATERIAL_PROVIDERS("MaterialProviders"),

  /** An {@code IKeyring} from any MPL keyring constructor. */
  KEYRING("Keyring");

  private final String displayName;

  ResourceKind(String displayName) {
    this.displayName = displayName;
  }

  /** Name used in error messages for test authors. */
  public String displayName() {
    return displayName;
  }
}
