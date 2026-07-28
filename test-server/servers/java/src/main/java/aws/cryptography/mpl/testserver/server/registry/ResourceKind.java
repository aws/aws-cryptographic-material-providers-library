package aws.cryptography.mpl.testserver.server.registry;

/**
 * The kinds of MPL resource a {@link ResourceRegistry} entry can hold.
 *
 * <p>Every MPL constructor returns an {@code aws.polymorph#reference} to a resource,
 * and a reference cannot cross a wire, so the TestServer hands out an opaque
 * {@code ResourceId} instead. All those ids share one Smithy shape, which means the
 * wire alone cannot stop a test from passing a keyring's id where a
 * MaterialProviders id belongs.
 *
 * <p>Recording the kind alongside each entry closes that gap: resolution demands the
 * expected kind and a mismatch becomes a {@code GenericServerError} naming both
 * kinds (Requirement 3.9, 3.10), rather than a {@link ClassCastException} surfacing
 * as an opaque server fault.
 */
public enum ResourceKind {
    /** A {@code MaterialProviders} instance -- the root of the Artifact_Under_Test. */
    MATERIAL_PROVIDERS("MaterialProviders"),

    /** An {@code IKeyring}, from any of the MPL's keyring constructors. */
    KEYRING("Keyring");

    private final String displayName;

    ResourceKind(String displayName) {
        this.displayName = displayName;
    }

    /** @return the name to use in an error message a test author has to read. */
    public String displayName() {
        return displayName;
    }
}
