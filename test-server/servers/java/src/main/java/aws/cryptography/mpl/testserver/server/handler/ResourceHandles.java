package aws.cryptography.mpl.testserver.server.handler;

import aws.cryptography.mpl.testserver.server.model.GenericServerError;
import aws.cryptography.mpl.testserver.server.registry.ResourceKind;
import aws.cryptography.mpl.testserver.server.registry.ResourceRegistry;
import software.amazon.cryptography.materialproviders.IKeyring;
import software.amazon.cryptography.materialproviders.MaterialProviders;

/**
 * Resolves the {@code ResourceId} handles that every operation but {@code CreateMPL}
 * requires, turning a bad handle into a {@link GenericServerError}
 * (Requirement 3.10).
 *
 * <p>The guard runs BEFORE any MPL call, so a bad handle means no MPL operation is
 * performed and the {@link ResourceRegistry} is left unchanged -- which is what lets
 * a negative test assert that a rejected request had no side effect.
 */
public final class ResourceHandles {

    private final ResourceRegistry registry;

    public ResourceHandles(ResourceRegistry registry) {
        this.registry = registry;
    }

    /** @return the registry these handles are resolved against. */
    public ResourceRegistry registry() {
        return registry;
    }

    /**
     * Resolve a handle to the {@code MaterialProviders} instance to construct through.
     *
     * @throws GenericServerError if the handle is absent, empty, unknown, or names
     *     another kind of resource.
     */
    public MaterialProviders materialProviders(String mplId) {
        return resolve(mplId, ResourceKind.MATERIAL_PROVIDERS, MaterialProviders.class,
            "Call CreateMPL first and pass the returned mplId.");
    }

    /**
     * Resolve a handle to a keyring.
     *
     * @throws GenericServerError if the handle is absent, empty, unknown, or names
     *     another kind of resource.
     */
    public IKeyring keyring(String keyringId) {
        return resolve(keyringId, ResourceKind.KEYRING, IKeyring.class,
            "Call one of the Create*Keyring operations first and pass the returned keyringId.");
    }

    /**
     * Resolve the {@code MaterialProviders} instance a resource was constructed through.
     *
     * <p>Needed because converting materials calls {@code GetAlgorithmSuiteInfo}, which
     * lives on {@code MaterialProviders} -- while the MPL's keyring interface takes no such
     * parameter, so neither does the wire. The association is recorded at construction.
     *
     * @throws GenericServerError if the handle is unknown or was registered without an
     *     owner, which would be a harness defect rather than a caller mistake.
     */
    public MaterialProviders owningMaterialProviders(String resourceId) {
        return registry.owner(resourceId, MaterialProviders.class)
            .orElseThrow(() -> GenericServerError.builder()
                .message("No MaterialProviders instance is recorded as the owner of ResourceId '"
                    + (resourceId == null ? "" : resourceId)
                    + "'. Every resource created through CreateMPL records its owner, so this"
                    + " indicates the handle was never created by a Create* operation.")
                .build());
    }

    private <T> T resolve(String resourceId, ResourceKind kind, Class<T> type, String hint) {
        try {
            return registry.resolve(resourceId, kind, type)
                .orElseThrow(() -> GenericServerError.builder()
                    .message("No " + kind.displayName() + " is registered under ResourceId '"
                        + (resourceId == null ? "" : resourceId) + "'. " + hint)
                    .build());
        } catch (ResourceRegistry.WrongKindException wrongKind) {
            // A handle that exists but names the wrong kind is a distinct mistake from
            // one that does not exist, and deserves a message that says so.
            throw GenericServerError.builder()
                .message(wrongKind.getMessage())
                .withCause(wrongKind)
                .build();
        }
    }
}
