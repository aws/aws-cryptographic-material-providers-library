package aws.cryptography.mpl.testserver.server.handler;

import aws.cryptography.mpl.testserver.server.convert.AlgorithmSuites;
import aws.cryptography.mpl.testserver.server.convert.Materials;
import aws.cryptography.mpl.testserver.server.error.OperationWrapper;
import aws.cryptography.mpl.testserver.server.model.InitializeDecryptionMaterialsInput;
import aws.cryptography.mpl.testserver.server.model.InitializeDecryptionMaterialsOutput;
import aws.cryptography.mpl.testserver.server.service.InitializeDecryptionMaterialsOperation;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import software.amazon.cryptography.materialproviders.MaterialProviders;
import software.amazon.cryptography.materialproviders.model.DecryptionMaterials;
import software.amazon.smithy.java.server.RequestContext;

/**
 * Produces well-formed, empty decryption materials for an algorithm suite, by calling
 * the MPL's own {@code InitializeDecryptionMaterials} (Requirement 5.2).
 *
 * <p>This is the decrypt half of a round-trip's setup. Note that it takes only the suite
 * identity and the encryption context -- NOT anything derived from the encrypt half. The
 * encrypted data keys travel separately, on the {@code OnDecrypt} request. That
 * separation is what allows the two halves of a round-trip to be sent to two different
 * language servers.
 */
public final class InitializeDecryptionMaterialsHandler
        implements InitializeDecryptionMaterialsOperation {

    private final ResourceHandles handles;
    private final OperationWrapper wrapper;

    public InitializeDecryptionMaterialsHandler(ResourceHandles handles, OperationWrapper wrapper) {
        this.handles = handles;
        this.wrapper = wrapper;
    }

    @Override
    public InitializeDecryptionMaterialsOutput initializeDecryptionMaterials(
        InitializeDecryptionMaterialsInput input,
        RequestContext context
    ) {
        return wrapper.invoke("InitializeDecryptionMaterials", () -> doInitialize(input));
    }

    private InitializeDecryptionMaterialsOutput doInitialize(
        InitializeDecryptionMaterialsInput input
    ) {
        MaterialProviders materialProviders = handles.materialProviders(input.getMplId());

        var mplInput = software.amazon.cryptography.materialproviders.model
            .InitializeDecryptionMaterialsInput.builder()
            .algorithmSuiteId(AlgorithmSuites.toMpl(input.getAlgorithmSuiteId()))
            .encryptionContext(input.getEncryptionContext() == null
                ? Map.of() : Map.copyOf(input.getEncryptionContext()))
            .requiredEncryptionContextKeys(input.getRequiredEncryptionContextKeys() == null
                ? List.of() : new ArrayList<>(input.getRequiredEncryptionContextKeys()))
            .build();

        DecryptionMaterials materials = materialProviders.InitializeDecryptionMaterials(mplInput);

        return InitializeDecryptionMaterialsOutput.builder()
            .materials(Materials.toWire(materials))
            .build();
    }
}
