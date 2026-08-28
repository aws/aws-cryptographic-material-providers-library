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
 * Produces well-formed, empty decryption materials via the MPL's own
 * {@code InitializeDecryptionMaterials}. EDKs travel separately on the
 * {@code OnDecrypt} request, which is what lets the two halves of a
 * round-trip go to different language servers.
 */
public final class InitializeDecryptionMaterialsHandler
  implements InitializeDecryptionMaterialsOperation {

  private final ResourceHandles handles;
  private final OperationWrapper wrapper;

  public InitializeDecryptionMaterialsHandler(
    ResourceHandles handles,
    OperationWrapper wrapper
  ) {
    this.handles = handles;
    this.wrapper = wrapper;
  }

  @Override
  public InitializeDecryptionMaterialsOutput initializeDecryptionMaterials(
    InitializeDecryptionMaterialsInput input,
    RequestContext context
  ) {
    return wrapper.invoke(
      "InitializeDecryptionMaterials",
      () -> doInitialize(input)
    );
  }

  private InitializeDecryptionMaterialsOutput doInitialize(
    InitializeDecryptionMaterialsInput input
  ) {
    MaterialProviders materialProviders = handles.materialProviders(
      input.getMplId()
    );

    var mplInput =
      software.amazon.cryptography.materialproviders.model.InitializeDecryptionMaterialsInput
        .builder()
        .algorithmSuiteId(AlgorithmSuites.toMpl(input.getAlgorithmSuiteId()))
        .encryptionContext(
          input.getEncryptionContext() == null
            ? Map.of()
            : Map.copyOf(input.getEncryptionContext())
        )
        .requiredEncryptionContextKeys(
          input.getRequiredEncryptionContextKeys() == null
            ? List.of()
            : new ArrayList<>(input.getRequiredEncryptionContextKeys())
        )
        .build();

    DecryptionMaterials materials =
      materialProviders.InitializeDecryptionMaterials(mplInput);

    return InitializeDecryptionMaterialsOutput
      .builder()
      .materials(Materials.toWire(materials))
      .build();
  }
}
