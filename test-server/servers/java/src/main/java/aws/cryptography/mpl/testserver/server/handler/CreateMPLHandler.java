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
 * Constructs a {@code MaterialProviders} instance -- the root of the
 * Artifact_Under_Test -- and returns a handle to it (Requirement 3.2).
 *
 * <p>Because the handle is what every later operation is scoped by, a test can hold
 * several independently configured instances at once and be certain which one a
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
    public CreateMPLOutput createMPL(CreateMPLInput input, RequestContext context) {
        return wrapper.invoke("CreateMPL", () -> doCreateMPL(input));
    }

    private CreateMPLOutput doCreateMPL(CreateMPLInput input) {
        // The MPL's own MaterialProvidersConfig has no members today. The wire shape is
        // still consulted rather than ignored, so that when the MPL gives the config
        // members this handler is the only place that has to change.
        MaterialProvidersConfig config = MaterialProvidersConfig.builder().build();

        // Note the capitalised builder method: the MPL's generated builder names this
        // setter after the SHAPE (MaterialProvidersConfig), not after the member, unlike
        // every other builder in the library.
        MaterialProviders materialProviders = MaterialProviders.builder()
            .MaterialProvidersConfig(config)
            .build();

        String mplId = registry.register(ResourceKind.MATERIAL_PROVIDERS, materialProviders);

        return CreateMPLOutput.builder()
            .mplId(mplId)
            .build();
    }
}
