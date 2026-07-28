package aws.cryptography.mpl.testserver.server.handler;

import aws.cryptography.mpl.testserver.server.error.OperationWrapper;
import aws.cryptography.mpl.testserver.server.model.CreateRawRsaKeyringInput;
import aws.cryptography.mpl.testserver.server.model.CreateRawRsaKeyringOutput;
import aws.cryptography.mpl.testserver.server.registry.ResourceKind;
import aws.cryptography.mpl.testserver.server.service.CreateRawRsaKeyringOperation;
import software.amazon.cryptography.materialproviders.IKeyring;
import software.amazon.cryptography.materialproviders.MaterialProviders;
import software.amazon.cryptography.materialproviders.model.PaddingScheme;
import software.amazon.smithy.java.server.RequestContext;

/**
 * Creates a Raw RSA keyring and returns a handle to it.
 *
 * <p>Both keys are optional on the wire, mirroring the MPL. Notably this handler does NOT
 * validate that at least one is present: the MPL rejects that case itself, and letting it do
 * so means the resulting error is the MPL's own -- a {@code MaterialProvidersClientError}
 * carrying the MPL's message -- rather than a harness error that would tell a test nothing
 * about MPL behavior.
 */
public final class CreateRawRsaKeyringHandler implements CreateRawRsaKeyringOperation {

    private final ResourceHandles handles;
    private final OperationWrapper wrapper;

    public CreateRawRsaKeyringHandler(ResourceHandles handles, OperationWrapper wrapper) {
        this.handles = handles;
        this.wrapper = wrapper;
    }

    @Override
    public CreateRawRsaKeyringOutput createRawRsaKeyring(
        CreateRawRsaKeyringInput input,
        RequestContext context
    ) {
        return wrapper.invoke("CreateRawRsaKeyring", () -> doCreate(input));
    }

    private CreateRawRsaKeyringOutput doCreate(CreateRawRsaKeyringInput input) {
        MaterialProviders materialProviders = handles.materialProviders(input.getMplId());

        var mplInput = software.amazon.cryptography.materialproviders.model
            .CreateRawRsaKeyringInput.builder()
            .keyNamespace(input.getKeyNamespace())
            .keyName(input.getKeyName())
            .paddingScheme(PaddingScheme.valueOf(input.getPaddingScheme().getValue()));

        // Only set what was supplied. Passing an empty buffer for an absent key would turn
        // "no public key" into "a zero-length public key" and change which error the MPL
        // raises.
        if (input.getPublicKey() != null) {
            mplInput.publicKey(input.getPublicKey());
        }
        if (input.getPrivateKey() != null) {
            mplInput.privateKey(input.getPrivateKey());
        }

        IKeyring keyring = materialProviders.CreateRawRsaKeyring(mplInput.build());

        return CreateRawRsaKeyringOutput.builder()
            .keyringId(handles.registry()
                .register(ResourceKind.KEYRING, keyring, materialProviders))
            .build();
    }
}
