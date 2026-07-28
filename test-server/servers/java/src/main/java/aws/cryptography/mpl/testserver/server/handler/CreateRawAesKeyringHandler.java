package aws.cryptography.mpl.testserver.server.handler;

import aws.cryptography.mpl.testserver.server.error.OperationWrapper;
import aws.cryptography.mpl.testserver.server.model.CreateRawAesKeyringInput;
import aws.cryptography.mpl.testserver.server.model.CreateRawAesKeyringOutput;
import aws.cryptography.mpl.testserver.server.registry.ResourceKind;
import aws.cryptography.mpl.testserver.server.service.CreateRawAesKeyringOperation;
import software.amazon.cryptography.materialproviders.IKeyring;
import software.amazon.cryptography.materialproviders.MaterialProviders;
import software.amazon.cryptography.materialproviders.model.AesWrappingAlg;
import software.amazon.cryptography.materialproviders.model.CreateRawAesKeyringInput
    .Builder;
import software.amazon.smithy.java.server.RequestContext;

/**
 * Creates a Raw AES keyring and returns a handle to it.
 *
 * <p>Local-only: constructing and using this keyring makes no AWS call, which is what
 * lets the phase-1 conformance suite run green without credentials.
 */
public final class CreateRawAesKeyringHandler implements CreateRawAesKeyringOperation {

    private final ResourceHandles handles;
    private final OperationWrapper wrapper;

    public CreateRawAesKeyringHandler(ResourceHandles handles, OperationWrapper wrapper) {
        this.handles = handles;
        this.wrapper = wrapper;
    }

    @Override
    public CreateRawAesKeyringOutput createRawAesKeyring(
        CreateRawAesKeyringInput input,
        RequestContext context
    ) {
        return wrapper.invoke("CreateRawAesKeyring", () -> doCreate(input));
    }

    private CreateRawAesKeyringOutput doCreate(CreateRawAesKeyringInput input) {
        MaterialProviders materialProviders = handles.materialProviders(input.getMplId());

        Builder mplInput = software.amazon.cryptography.materialproviders.model
            .CreateRawAesKeyringInput.builder()
            .keyNamespace(input.getKeyNamespace())
            .keyName(input.getKeyName())
            .wrappingKey(input.getWrappingKey())
            // The wire enum restricts the value to the MPL's own constants, so the MPL
            // enum is resolved from that value rather than from a translation table that
            // could drift.
            .wrappingAlg(AesWrappingAlg.valueOf(input.getWrappingAlg().getValue()));

        IKeyring keyring = materialProviders.CreateRawAesKeyring(mplInput.build());

        return CreateRawAesKeyringOutput.builder()
            // The owning MaterialProviders is recorded so OnEncrypt/OnDecrypt can convert
            // materials from a keyring handle alone, without the wire having to carry an
            // mplId the MPL's own keyring interface never asks for.
            .keyringId(handles.registry()
                .register(ResourceKind.KEYRING, keyring, materialProviders))
            .build();
    }
}
