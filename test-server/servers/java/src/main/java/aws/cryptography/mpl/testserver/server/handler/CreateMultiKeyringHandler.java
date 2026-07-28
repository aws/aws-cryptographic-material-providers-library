package aws.cryptography.mpl.testserver.server.handler;

import aws.cryptography.mpl.testserver.server.error.OperationWrapper;
import aws.cryptography.mpl.testserver.server.model.CreateMultiKeyringInput;
import aws.cryptography.mpl.testserver.server.model.CreateMultiKeyringOutput;
import aws.cryptography.mpl.testserver.server.registry.ResourceKind;
import aws.cryptography.mpl.testserver.server.service.CreateMultiKeyringOperation;
import java.util.ArrayList;
import java.util.List;
import software.amazon.cryptography.materialproviders.IKeyring;
import software.amazon.cryptography.materialproviders.MaterialProviders;
import software.amazon.smithy.java.server.RequestContext;

/**
 * Creates a Multi-keyring from keyrings the server already holds, and returns a handle to
 * it.
 *
 * <p>This is the operation that demonstrates why handles are the right model rather than a
 * workaround. The MPL's {@code CreateMultiKeyringInput} takes an {@code IKeyring} generator
 * and a {@code List<IKeyring>} of children; the wire takes handles to exactly those, so
 * composition on the wire is composition in the MPL. Recursion needs no special treatment --
 * a child handle may itself denote a multi-keyring.
 *
 * <p>Every child handle is resolved BEFORE the MPL is called, so a request naming one bad
 * child creates no keyring at all and registers nothing.
 */
public final class CreateMultiKeyringHandler implements CreateMultiKeyringOperation {

    private final ResourceHandles handles;
    private final OperationWrapper wrapper;

    public CreateMultiKeyringHandler(ResourceHandles handles, OperationWrapper wrapper) {
        this.handles = handles;
        this.wrapper = wrapper;
    }

    @Override
    public CreateMultiKeyringOutput createMultiKeyring(
        CreateMultiKeyringInput input,
        RequestContext context
    ) {
        return wrapper.invoke("CreateMultiKeyring", () -> doCreate(input));
    }

    private CreateMultiKeyringOutput doCreate(CreateMultiKeyringInput input) {
        MaterialProviders materialProviders = handles.materialProviders(input.getMplId());

        var mplInput = software.amazon.cryptography.materialproviders.model
            .CreateMultiKeyringInput.builder();

        // The generator is optional: without one the multi-keyring cannot generate a data
        // key, only wrap an existing one. An absent generator must therefore stay absent
        // rather than becoming some placeholder keyring.
        if (input.getGeneratorKeyringId() != null && !input.getGeneratorKeyringId().isEmpty()) {
            mplInput.generator(handles.keyring(input.getGeneratorKeyringId()));
        }

        // Resolve every child up front. A partially resolved list must not reach the MPL,
        // or a request naming one bad child could still create a keyring.
        List<String> childIds = input.getChildKeyringIds() == null
            ? List.of()
            : input.getChildKeyringIds();
        List<IKeyring> children = new ArrayList<>(childIds.size());
        for (String childId : childIds) {
            children.add(handles.keyring(childId));
        }
        mplInput.childKeyrings(children);

        IKeyring keyring = materialProviders.CreateMultiKeyring(mplInput.build());

        return CreateMultiKeyringOutput.builder()
            .keyringId(handles.registry()
                .register(ResourceKind.KEYRING, keyring, materialProviders))
            .build();
    }
}
