package aws.cryptography.mpl.testserver.server.handler;

import aws.cryptography.mpl.testserver.server.convert.Materials;
import aws.cryptography.mpl.testserver.server.error.OperationWrapper;
import aws.cryptography.mpl.testserver.server.model.GenericServerError;
import aws.cryptography.mpl.testserver.server.model.OnEncryptInput;
import aws.cryptography.mpl.testserver.server.model.OnEncryptOutput;
import aws.cryptography.mpl.testserver.server.service.OnEncryptOperation;
import software.amazon.cryptography.materialproviders.IKeyring;
import software.amazon.cryptography.materialproviders.MaterialProviders;
import software.amazon.cryptography.materialproviders.model.OnEncryptInput
    .Builder;
import software.amazon.smithy.java.server.RequestContext;

/**
 * Invokes a keyring's {@code OnEncrypt}.
 *
 * <p>Note the two handles this operation needs and the one it is given. The wire request
 * carries only a {@code keyringId}, but converting the incoming materials requires a
 * {@code MaterialProviders} instance -- {@code GetAlgorithmSuiteInfo} lives on it -- and
 * the request does not say which one. The MaterialProviders instance the keyring was
 * built through is the right one, so the registry records that association when a keyring
 * is created and this handler follows it.
 *
 * <p>The alternative -- putting an {@code mplId} on every keyring operation -- would
 * diverge from the MPL, where a keyring is a self-contained object you simply call.
 */
public final class OnEncryptHandler implements OnEncryptOperation {

    private final ResourceHandles handles;
    private final OperationWrapper wrapper;

    public OnEncryptHandler(ResourceHandles handles, OperationWrapper wrapper) {
        this.handles = handles;
        this.wrapper = wrapper;
    }

    @Override
    public OnEncryptOutput onEncrypt(OnEncryptInput input, RequestContext context) {
        return wrapper.invoke("OnEncrypt", () -> doOnEncrypt(input));
    }

    private OnEncryptOutput doOnEncrypt(OnEncryptInput input) {
        IKeyring keyring = handles.keyring(input.getKeyringId());
        MaterialProviders materialProviders = handles.owningMaterialProviders(input.getKeyringId());

        if (input.getMaterials() == null) {
            throw GenericServerError.builder()
                .message("OnEncrypt requires materials, but none were supplied.")
                .build();
        }

        Builder mplInput = software.amazon.cryptography.materialproviders.model
            .OnEncryptInput.builder()
            .materials(Materials.toMpl(materialProviders, input.getMaterials()));

        var output = keyring.OnEncrypt(mplInput.build());

        return OnEncryptOutput.builder()
            .materials(Materials.toWire(output.materials()))
            .build();
    }
}
