package aws.cryptography.mpl.testserver.server.handler;

import aws.cryptography.mpl.testserver.server.error.OperationWrapper;
import aws.cryptography.mpl.testserver.server.registry.ResourceRegistry;
import aws.cryptography.mpl.testserver.server.service.MPLTestServer;

/**
 * Single assembly point for the Java Language_Server: one
 * {@link ResourceRegistry} shared by every handler, one
 * {@link OperationWrapper}, and the generated service wired to the
 * handlers. One shared registry because handles must compose across
 * handlers (e.g. multi-keyring references keyrings from another).
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

  /** Returns the registry shared by every handler. */
  public ResourceRegistry registry() {
    return registry;
  }

  /**
   * Returns the generated service wired to the hand-written handlers.
   * The generated builder is staged and enforces alphabetical operation
   * order, so adding a model operation changes the required call order
   * here -- making it impossible to forget to wire a handler.
   */
  public MPLTestServer service() {
    return MPLTestServer
      .builder()
      .addCreateMPLOperation(new CreateMPLHandler(registry, wrapper))
      .addCreateMultiKeyringOperation(
        new CreateMultiKeyringHandler(handles, wrapper)
      )
      .addCreateRawAesKeyringOperation(
        new CreateRawAesKeyringHandler(handles, wrapper)
      )
      .addCreateRawRsaKeyringOperation(
        new CreateRawRsaKeyringHandler(handles, wrapper)
      )
      .addInitializeDecryptionMaterialsOperation(
        new InitializeDecryptionMaterialsHandler(handles, wrapper)
      )
      .addInitializeEncryptionMaterialsOperation(
        new InitializeEncryptionMaterialsHandler(handles, wrapper)
      )
      .addOnDecryptOperation(new OnDecryptHandler(handles, wrapper))
      .addOnEncryptOperation(new OnEncryptHandler(handles, wrapper))
      .build();
  }
}
