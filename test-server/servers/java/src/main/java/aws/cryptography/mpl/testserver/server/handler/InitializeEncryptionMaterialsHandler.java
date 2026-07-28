package aws.cryptography.mpl.testserver.server.handler;

import aws.cryptography.mpl.testserver.server.convert.AlgorithmSuites;
import aws.cryptography.mpl.testserver.server.convert.Materials;
import aws.cryptography.mpl.testserver.server.error.OperationWrapper;
import aws.cryptography.mpl.testserver.server.model.InitializeEncryptionMaterialsInput;
import aws.cryptography.mpl.testserver.server.model.InitializeEncryptionMaterialsOutput;
import aws.cryptography.mpl.testserver.server.service.InitializeEncryptionMaterialsOperation;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import software.amazon.cryptography.materialproviders.MaterialProviders;
import software.amazon.cryptography.materialproviders.model.EncryptionMaterials;
import software.amazon.smithy.java.server.RequestContext;

/**
 * Produces well-formed, empty encryption materials for an algorithm suite, by calling
 * the MPL's own {@code InitializeEncryptionMaterials} (Requirement 5.2).
 *
 * <p>Exposing this rather than letting tests hand-build materials matters: hand-built
 * materials would encode the harness's idea of "well-formed" instead of the MPL's, and a
 * keyring that then rejected them would leave a test unable to tell which side was
 * wrong.
 */
public final class InitializeEncryptionMaterialsHandler
        implements InitializeEncryptionMaterialsOperation {

    private final ResourceHandles handles;
    private final OperationWrapper wrapper;

    public InitializeEncryptionMaterialsHandler(ResourceHandles handles, OperationWrapper wrapper) {
        this.handles = handles;
        this.wrapper = wrapper;
    }

    @Override
    public InitializeEncryptionMaterialsOutput initializeEncryptionMaterials(
        InitializeEncryptionMaterialsInput input,
        RequestContext context
    ) {
        return wrapper.invoke("InitializeEncryptionMaterials", () -> doInitialize(input));
    }

    private InitializeEncryptionMaterialsOutput doInitialize(
        InitializeEncryptionMaterialsInput input
    ) {
        // Resolve the handle FIRST. A bad handle must fail before any MPL call, so a
        // rejected request provably has no side effect.
        MaterialProviders materialProviders = handles.materialProviders(input.getMplId());

        var mplInput = software.amazon.cryptography.materialproviders.model
            .InitializeEncryptionMaterialsInput.builder()
            .algorithmSuiteId(AlgorithmSuites.toMpl(input.getAlgorithmSuiteId()))
            .encryptionContext(input.getEncryptionContext() == null
                ? Map.of() : Map.copyOf(input.getEncryptionContext()))
            .requiredEncryptionContextKeys(input.getRequiredEncryptionContextKeys() == null
                ? List.of() : new ArrayList<>(input.getRequiredEncryptionContextKeys()));

        if (input.getSigningKey() != null) {
            mplInput.signingKey(input.getSigningKey());
        }
        if (input.getVerificationKey() != null) {
            mplInput.verificationKey(input.getVerificationKey());
        }

        EncryptionMaterials materials = materialProviders
            .InitializeEncryptionMaterials(mplInput.build());

        return InitializeEncryptionMaterialsOutput.builder()
            .materials(Materials.toWire(materials))
            .build();
    }
}
