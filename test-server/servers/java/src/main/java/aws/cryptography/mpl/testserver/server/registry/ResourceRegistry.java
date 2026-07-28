package aws.cryptography.mpl.testserver.server.registry;

import java.util.Objects;
import java.util.Optional;
import java.util.UUID;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.ConcurrentMap;

/**
 * Thread-safe registry of live MPL resources, keyed by opaque UUID handles
 * (Requirement 3).
 *
 * <p>Every MPL constructor returns an aws.polymorph#reference that cannot be
 * serialized, so the registry keeps the real resource server-side and gives
 * the test a UUID to name it by. Entries are never evicted, handles are
 * unique via putIfAbsent, and resolution demands the expected
 * {@link ResourceKind} so a wrong-kind handle is a clear error.
 */
public final class ResourceRegistry {

  /**
   * One registry entry.
   *
   * @param owner the {@code MaterialProviders} instance this resource was
   *     constructed through, or {@code null} when the resource IS one.
   *     Materials conversion needs GetAlgorithmSuiteInfo (a
   *     MaterialProviders method), but the MPL keyring interface takes no
   *     mplId -- a keyring is self-contained -- so the wire carries none
   *     either. The owner is recovered from here instead.
   */
  private record Entry(ResourceKind kind, Object resource, Object owner) {}

  private final ConcurrentMap<String, Entry> entries =
    new ConcurrentHashMap<>();

  /**
   * Raised when a handle resolves to a resource of an unexpected kind.
   */
  public static final class WrongKindException extends RuntimeException {

    private final ResourceKind expected;
    private final ResourceKind actual;

    WrongKindException(
      String resourceId,
      ResourceKind expected,
      ResourceKind actual
    ) {
      super(
        "ResourceId '" +
        resourceId +
        "' refers to a " +
        actual.displayName() +
        ", but a " +
        expected.displayName() +
        " is required here."
      );
      this.expected = expected;
      this.actual = actual;
    }

    public ResourceKind expected() {
      return expected;
    }

    public ResourceKind actual() {
      return actual;
    }
  }

  /** Store a resource that has no owner (a MaterialProviders instance). */
  public String register(ResourceKind kind, Object resource) {
    return register(kind, resource, null);
  }

  /** Store a resource, recording the MaterialProviders it was built from. */
  public String register(ResourceKind kind, Object resource, Object owner) {
    Objects.requireNonNull(kind, "kind cannot be null");
    Objects.requireNonNull(resource, "resource cannot be null");
    Entry entry = new Entry(kind, resource, owner);
    while (true) {
      String id = UUID.randomUUID().toString();
      if (entries.putIfAbsent(id, entry) == null) {
        return id;
      }
    }
  }

  /**
   * Resolve the MaterialProviders instance a resource was built from.
   */
  public <T> Optional<T> owner(String resourceId, Class<T> type) {
    if (resourceId == null || resourceId.isEmpty()) {
      return Optional.empty();
    }
    Entry entry = entries.get(resourceId);
    if (entry == null || entry.owner() == null) {
      return Optional.empty();
    }
    return Optional.of(type.cast(entry.owner()));
  }

  /**
   * Resolve a handle to a resource of the expected kind.
   *
   * @param resourceId the handle from the request. Empty and absent are the
   *     same case here -- generated shapes substitute empty for absent.
   * @throws WrongKindException if the handle names another kind.
   */
  public <T> Optional<T> resolve(
    String resourceId,
    ResourceKind kind,
    Class<T> type
  ) {
    if (resourceId == null || resourceId.isEmpty()) {
      return Optional.empty();
    }
    Entry entry = entries.get(resourceId);
    if (entry == null) {
      return Optional.empty();
    }
    if (entry.kind() != kind) {
      throw new WrongKindException(resourceId, kind, entry.kind());
    }
    return Optional.of(type.cast(entry.resource()));
  }

  /** Whether a handle is currently held. */
  public boolean contains(String resourceId) {
    return (
      resourceId != null &&
      !resourceId.isEmpty() &&
      entries.containsKey(resourceId)
    );
  }

  /** The number of handles currently held. */
  public int size() {
    return entries.size();
  }
}
