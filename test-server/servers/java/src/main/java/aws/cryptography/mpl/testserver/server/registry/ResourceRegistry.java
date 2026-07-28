package aws.cryptography.mpl.testserver.server.registry;

import java.util.Objects;
import java.util.Optional;
import java.util.UUID;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.ConcurrentMap;

/**
 * The in-memory, thread-safe registry of live MPL resources, keyed by the opaque
 * {@code ResourceId} handles the TestServer hands out (Requirement 3).
 *
 * <p>This class is the reason the MPL TestServer can exist. Every MPL constructor --
 * {@code CreateRawAesKeyring}, {@code CreateMultiKeyring}, {@code CreateMPL} --
 * returns an {@code aws.polymorph#reference} to a resource. References cannot be
 * serialized, so they cannot cross a wire. The registry keeps the real resource
 * server-side and gives the test a UUID to name it by.
 *
 * <p>Guarantees, each of which a Tests scenario depends on:
 * <ul>
 *   <li><b>Unique handles.</b> {@link #register} claims its id with
 *       {@link ConcurrentMap#putIfAbsent}, retrying on the (astronomically
 *       unlikely) collision, so uniqueness is a guarantee rather than a
 *       probability -- even under concurrent registration (Requirements 3.5, 3.7).</li>
 *   <li><b>Atomic registration.</b> Either the entry is stored and an id returned,
 *       or nothing is stored and no id is returned (Requirement 3.7).</li>
 *   <li><b>No eviction.</b> A handle resolves to the same resource for the whole
 *       process lifetime, so a test may hold one across many operations
 *       (Requirement 3.8).</li>
 *   <li><b>Typed entries.</b> Resolution demands the expected {@link ResourceKind}
 *       (Requirement 3.9).</li>
 * </ul>
 *
 * <p>Resolution failures are reported here as an empty {@link Optional} or a
 * {@link WrongKindException}; turning those into the modeled {@code
 * GenericServerError} is the handler layer's job, so this class stays free of any
 * dependency on generated code.
 */
public final class ResourceRegistry {

    /**
     * One registry entry.
     *
     * @param kind the kind this resource was registered as.
     * @param resource the live MPL resource.
     * @param owner the {@code MaterialProviders} instance this resource was constructed
     *     through, or {@code null} when the resource IS a {@code MaterialProviders}.
     *     <p>Recording the owner is what lets a keyring operation work from a keyring
     *     handle alone. Converting materials needs {@code GetAlgorithmSuiteInfo}, which
     *     lives on {@code MaterialProviders}, but the MPL's own keyring interface takes
     *     no such parameter -- a keyring is a self-contained object you simply call. Since
     *     the wire mirrors the MPL, {@code OnEncrypt} carries only a {@code keyringId},
     *     and the server recovers the instance from here instead of demanding an
     *     {@code mplId} the MPL would never ask for.
     */
    private record Entry(ResourceKind kind, Object resource, Object owner) {}

    private final ConcurrentMap<String, Entry> entries = new ConcurrentHashMap<>();

    /**
     * Raised when a handle resolves to a resource of a kind the caller did not ask
     * for -- for example a keyring id passed where a MaterialProviders id belongs.
     *
     * <p>Carries both kinds so the handler can build a message that tells a test
     * author exactly what they mixed up.
     */
    public static final class WrongKindException extends RuntimeException {
        private final ResourceKind expected;
        private final ResourceKind actual;

        WrongKindException(String resourceId, ResourceKind expected, ResourceKind actual) {
            super("ResourceId '" + resourceId + "' refers to a " + actual.displayName()
                + ", but a " + expected.displayName() + " is required here.");
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

    /**
     * Store a resource that has no owner -- that is, a {@code MaterialProviders} instance.
     *
     * @param kind the kind being registered; never {@code null}.
     * @param resource the live MPL resource; never {@code null}.
     * @return a non-empty, UUID-format handle distinct from every handle currently
     *     held (Requirements 3.2, 3.3, 3.5).
     */
    public String register(ResourceKind kind, Object resource) {
        return register(kind, resource, null);
    }

    /**
     * Store a resource constructed through a {@code MaterialProviders} instance, recording
     * that instance so later operations on the resource can recover it.
     *
     * @param kind the kind being registered; never {@code null}.
     * @param resource the live MPL resource; never {@code null}.
     * @param owner the {@code MaterialProviders} the resource was constructed through.
     * @return a fresh handle.
     */
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
     * Resolve the {@code MaterialProviders} instance a registered resource was constructed
     * through.
     *
     * @param resourceId the handle of the derived resource (for example a keyring).
     * @param type the type to return the owner as.
     * @return the owning instance, or {@link Optional#empty()} if the handle is unknown or
     *     the entry has no owner.
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
     * Resolve a handle to a resource of an expected kind.
     *
     * @param resourceId the handle from the request. The generated shapes substitute
     *     an empty string for an absent required member, so empty and absent are the
     *     same case here.
     * @param kind the kind the caller requires.
     * @param type the Java type to return the resource as.
     * @return the resource, or {@link Optional#empty()} if the handle is
     *     {@code null}, empty, or not present.
     * @throws WrongKindException if the handle is present but names another kind.
     */
    public <T> Optional<T> resolve(String resourceId, ResourceKind kind, Class<T> type) {
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

    /** @return whether a handle is currently held. */
    public boolean contains(String resourceId) {
        return resourceId != null && !resourceId.isEmpty() && entries.containsKey(resourceId);
    }

    /** @return the number of handles currently held. */
    public int size() {
        return entries.size();
    }
}
