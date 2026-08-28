package aws.cryptography.mpl.testserver.server.handler;

import aws.cryptography.mpl.testserver.server.error.OperationWrapper;
import aws.cryptography.mpl.testserver.server.model.CreateMPLInput;
import aws.cryptography.mpl.testserver.server.model.CreateMPLOutput;
import aws.cryptography.mpl.testserver.server.registry.ResourceKind;
import aws.cryptography.mpl.testserver.server.registry.ResourceRegistry;
import aws.cryptography.mpl.testserver.server.service.CreateMPLOperation;
import software.amazon.cryptography.materialproviders.MaterialProviders;
import software.amazon.cryptography.materialproviders.model.MaterialProvidersConfig;
import software.amazon.smithy.java.server.RequestContext;

/**
 * Constructs a {@code MaterialProviders} instance and returns a handle
 * to it. Tests can hold several instances at once and know which one a
 * keyring was built through.
 */
public final class CreateMPLHandler implements CreateMPLOperation {

  private final ResourceRegistry registry;
  private final OperationWrapper wrapper;

  public CreateMPLHandler(ResourceRegistry registry, OperationWrapper wrapper) {
    this.registry = registry;
    this.wrapper = wrapper;
  }

  @Override
  public CreateMPLOutput createMPL(
    CreateMPLInput input,
    RequestContext context
  ) {
    return wrapper.invoke("CreateMPL", () -> doCreateMPL(input));
  }

  private CreateMPLOutput doCreateMPL(CreateMPLInput input) {
    // MaterialProvidersConfig is empty today but modeled for extensibility.
    MaterialProvidersConfig config = MaterialProvidersConfig.builder().build();

    // The builder method is capitalised after the SHAPE (.MaterialProvidersConfig()),
    // unlike every other builder in the library.
    MaterialProviders materialProviders = MaterialProviders
      .builder()
      .MaterialProvidersConfig(config)
      .build();

    String mplId = registry.register(
      ResourceKind.MATERIAL_PROVIDERS,
      materialProviders
    );

    return CreateMPLOutput.builder().mplId(mplId).build();
  }
}
