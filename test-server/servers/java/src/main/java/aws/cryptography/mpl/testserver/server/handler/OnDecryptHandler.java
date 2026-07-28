package aws.cryptography.mpl.testserver.server.handler;

import aws.cryptography.mpl.testserver.server.convert.Materials;
import aws.cryptography.mpl.testserver.server.error.OperationWrapper;
import aws.cryptography.mpl.testserver.server.model.GenericServerError;
import aws.cryptography.mpl.testserver.server.model.OnDecryptInput;
import aws.cryptography.mpl.testserver.server.model.OnDecryptOutput;
import aws.cryptography.mpl.testserver.server.service.OnDecryptOperation;
import java.util.List;
import software.amazon.cryptography.materialproviders.IKeyring;
import software.amazon.cryptography.materialproviders.MaterialProviders;
import software.amazon.smithy.java.server.RequestContext;

/**
 * Invokes a keyring's {@code OnDecrypt}. Only a keyringId is on the
 * wire; the owning MaterialProviders is recovered from the registry.
 * EDKs are a separate input (as in the MPL), which is what lets the
 * two halves of a round-trip go to different servers.
 */
public final class OnDecryptHandler implements OnDecryptOperation {

  private final ResourceHandles handles;
  private final OperationWrapper wrapper;

  public OnDecryptHandler(ResourceHandles handles, OperationWrapper wrapper) {
    this.handles = handles;
    this.wrapper = wrapper;
  }

  @Override
  public OnDecryptOutput onDecrypt(
    OnDecryptInput input,
    RequestContext context
  ) {
    return wrapper.invoke("OnDecrypt", () -> doOnDecrypt(input));
  }

  private OnDecryptOutput doOnDecrypt(OnDecryptInput input) {
    IKeyring keyring = handles.keyring(input.getKeyringId());
    MaterialProviders materialProviders = handles.owningMaterialProviders(
      input.getKeyringId()
    );

    if (input.getMaterials() == null) {
      throw GenericServerError
        .builder()
        .message("OnDecrypt requires materials, but none were supplied.")
        .build();
    }

    List<
      aws.cryptography.mpl.testserver.server.model.EncryptedDataKey
    > wireEdks = input.getEncryptedDataKeys();

    var mplInput =
      software.amazon.cryptography.materialproviders.model.OnDecryptInput
        .builder()
        .materials(Materials.toMpl(materialProviders, input.getMaterials()))
        // Empty list passed through: "no EDK matched" is MPL behavior a
        // negative test may want to observe.
        .encryptedDataKeys(Materials.edksToMpl(wireEdks))
        .build();

    var output = keyring.OnDecrypt(mplInput);

    return OnDecryptOutput
      .builder()
      .materials(Materials.toWire(output.materials()))
      .build();
  }
}
