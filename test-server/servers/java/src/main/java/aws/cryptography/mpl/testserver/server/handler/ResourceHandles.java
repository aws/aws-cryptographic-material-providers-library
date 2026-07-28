package aws.cryptography.mpl.testserver.server.handler;

import aws.cryptography.mpl.testserver.server.model.GenericServerError;
import aws.cryptography.mpl.testserver.server.registry.ResourceKind;
import aws.cryptography.mpl.testserver.server.registry.ResourceRegistry;
import software.amazon.cryptography.materialproviders.IKeyring;
import software.amazon.cryptography.materialproviders.MaterialProviders;

/**
 * Resolves {@code ResourceId} handles to typed resources, turning a bad
 * handle into a {@link GenericServerError}. The guard runs BEFORE any
 * MPL call, so a bad handle means no MPL operation ran and the registry
 * is unchanged. A handle that exists but names the wrong kind is a
 * distinct error from one that does not exist.
 */
public final class ResourceHandles {

  private final ResourceRegistry registry;

  public ResourceHandles(ResourceRegistry registry) {
    this.registry = registry;
  }

  /** Returns the registry these handles are resolved against. */
  public ResourceRegistry registry() {
    return registry;
  }

  /**
   * Resolve a handle to the {@code MaterialProviders} instance to
   * construct through.
   */
  public MaterialProviders materialProviders(String mplId) {
    return resolve(
      mplId,
      ResourceKind.MATERIAL_PROVIDERS,
      MaterialProviders.class,
      "Call CreateMPL first and pass the returned mplId."
    );
  }

  /** Resolve a handle to a keyring. */
  public IKeyring keyring(String keyringId) {
    return resolve(
      keyringId,
      ResourceKind.KEYRING,
      IKeyring.class,
      "Call one of the Create*Keyring operations first and pass the returned keyringId."
    );
  }

  /**
   * Resolve the {@code MaterialProviders} a resource was constructed
   * through. Needed because materials conversion calls
   * {@code GetAlgorithmSuiteInfo} (which lives on MaterialProviders)
   * while the MPL keyring interface takes no such parameter, so
   * neither does the wire.
   */
  public MaterialProviders owningMaterialProviders(String resourceId) {
    return registry
      .owner(resourceId, MaterialProviders.class)
      .orElseThrow(() ->
        GenericServerError
          .builder()
          .message(
            "No MaterialProviders instance is recorded as the owner of ResourceId '" +
            (resourceId == null ? "" : resourceId) +
            "'. Every resource created through CreateMPL records its owner, so this" +
            " indicates the handle was never created by a Create* operation."
          )
          .build()
      );
  }

  private <T> T resolve(
    String resourceId,
    ResourceKind kind,
    Class<T> type,
    String hint
  ) {
    try {
      return registry
        .resolve(resourceId, kind, type)
        .orElseThrow(() ->
          GenericServerError
            .builder()
            .message(
              "No " +
              kind.displayName() +
              " is registered under ResourceId '" +
              (resourceId == null ? "" : resourceId) +
              "'. " +
              hint
            )
            .build()
        );
    } catch (ResourceRegistry.WrongKindException wrongKind) {
      // Wrong kind is distinct from not-found and deserves its own message.
      throw GenericServerError
        .builder()
        .message(wrongKind.getMessage())
        .withCause(wrongKind)
        .build();
    }
  }
}
