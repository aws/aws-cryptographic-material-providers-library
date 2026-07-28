package aws.cryptography.mpl.testserver.server.handler;

import aws.cryptography.mpl.testserver.server.error.OperationWrapper;
import aws.cryptography.mpl.testserver.server.registry.ResourceRegistry;
import aws.cryptography.mpl.testserver.server.service.MPLTestServer;

/**
 * The single place the Java Language_Server is assembled: one {@link ResourceRegistry}
 * shared by every handler, one {@link OperationWrapper}, and the generated service
 * wired to the handlers.
 *
 * <p>There is exactly one assembly point on purpose. The standalone launcher and (via
 * it) the orchestrator both go through here, so what a manual run exercises is
 * bit-for-bit what an orchestrated run exercises.
 *
 * <p>The registry is shared rather than per-handler because handles must compose: a
 * multi-keyring created by one handler holds keyrings registered by another, and
 * {@code OnEncrypt} resolves a handle some {@code Create*} produced.
 */
public final class MPLTestServerHandlers {

    private final ResourceRegistry registry;
    private final OperationWrapper wrapper;
    private final ResourceHandles handles;

    public MPLTestServerHandlers() {
        this.registry = new ResourceRegistry();
        this.wrapper = new OperationWrapper();
        this.handles = new ResourceHandles(registry);
    }

    /** @return the registry shared by every handler. */
    public ResourceRegistry registry() {
        return registry;
    }

    /**
     * @return the generated service, wired to the hand-written handlers.
     *
     * <p>The generated builder is <b>staged</b>: each {@code addXOperation} returns the
     * next stage, so the operations must be added in the order the generator chose
     * (alphabetical by operation name) and every one must be supplied before
     * {@code build()} is reachable. Adding an operation to the model therefore changes
     * the required call order here -- which is a feature: it is impossible to forget to
     * wire a handler.
     */
    public MPLTestServer service() {
        return MPLTestServer.builder()
            .addCreateMPLOperation(new CreateMPLHandler(registry, wrapper))
            .addCreateMultiKeyringOperation(new CreateMultiKeyringHandler(handles, wrapper))
            .addCreateRawAesKeyringOperation(new CreateRawAesKeyringHandler(handles, wrapper))
            .addCreateRawRsaKeyringOperation(new CreateRawRsaKeyringHandler(handles, wrapper))
            .addInitializeDecryptionMaterialsOperation(
                new InitializeDecryptionMaterialsHandler(handles, wrapper))
            .addInitializeEncryptionMaterialsOperation(
                new InitializeEncryptionMaterialsHandler(handles, wrapper))
            .addOnDecryptOperation(new OnDecryptHandler(handles, wrapper))
            .addOnEncryptOperation(new OnEncryptHandler(handles, wrapper))
            .build();
    }
}
