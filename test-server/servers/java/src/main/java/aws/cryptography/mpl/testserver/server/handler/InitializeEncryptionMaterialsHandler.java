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
 * Produces well-formed, empty encryption materials via the MPL's own
 * {@code InitializeEncryptionMaterials}. Exposed so tests never
 * hand-build materials, which would encode the harness's idea of
 * well-formed rather than the MPL's.
 */
public final class InitializeEncryptionMaterialsHandler
  implements InitializeEncryptionMaterialsOperation {

  private final ResourceHandles handles;
  private final OperationWrapper wrapper;

  public InitializeEncryptionMaterialsHandler(
    ResourceHandles handles,
    OperationWrapper wrapper
  ) {
    this.handles = handles;
    this.wrapper = wrapper;
  }

  @Override
  public InitializeEncryptionMaterialsOutput initializeEncryptionMaterials(
    InitializeEncryptionMaterialsInput input,
    RequestContext context
  ) {
    return wrapper.invoke(
      "InitializeEncryptionMaterials",
      () -> doInitialize(input)
    );
  }

  private InitializeEncryptionMaterialsOutput doInitialize(
    InitializeEncryptionMaterialsInput input
  ) {
    // Handle resolved first -- a bad handle must fail before any MPL call.
    MaterialProviders materialProviders = handles.materialProviders(
      input.getMplId()
    );

    var mplInput =
      software.amazon.cryptography.materialproviders.model.InitializeEncryptionMaterialsInput
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
        );

    if (input.getSigningKey() != null) {
      mplInput.signingKey(input.getSigningKey());
    }
    if (input.getVerificationKey() != null) {
      mplInput.verificationKey(input.getVerificationKey());
    }

    EncryptionMaterials materials =
      materialProviders.InitializeEncryptionMaterials(mplInput.build());

    return InitializeEncryptionMaterialsOutput
      .builder()
      .materials(Materials.toWire(materials))
      .build();
  }
}
