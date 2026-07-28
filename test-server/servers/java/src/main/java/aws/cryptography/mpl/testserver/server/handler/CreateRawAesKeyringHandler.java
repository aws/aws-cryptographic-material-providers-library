package aws.cryptography.mpl.testserver.server.handler;

import aws.cryptography.mpl.testserver.server.error.OperationWrapper;
import aws.cryptography.mpl.testserver.server.model.CreateRawAesKeyringInput;
import aws.cryptography.mpl.testserver.server.model.CreateRawAesKeyringOutput;
import aws.cryptography.mpl.testserver.server.registry.ResourceKind;
import aws.cryptography.mpl.testserver.server.service.CreateRawAesKeyringOperation;
import software.amazon.cryptography.materialproviders.IKeyring;
import software.amazon.cryptography.materialproviders.MaterialProviders;
import software.amazon.cryptography.materialproviders.model.AesWrappingAlg;
import software.amazon.cryptography.materialproviders.model.CreateRawAesKeyringInput.Builder;
import software.amazon.smithy.java.server.RequestContext;

/**
 * Creates a Raw AES keyring and returns a handle to it. Local-only --
 * no AWS call is made, so phase-1 conformance runs without credentials.
 */
public final class CreateRawAesKeyringHandler
  implements CreateRawAesKeyringOperation {

  private final ResourceHandles handles;
  private final OperationWrapper wrapper;

  public CreateRawAesKeyringHandler(
    ResourceHandles handles,
    OperationWrapper wrapper
  ) {
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
    MaterialProviders materialProviders = handles.materialProviders(
      input.getMplId()
    );

    Builder mplInput =
      software.amazon.cryptography.materialproviders.model.CreateRawAesKeyringInput
        .builder()
        .keyNamespace(input.getKeyNamespace())
        .keyName(input.getKeyName())
        .wrappingKey(input.getWrappingKey())
        // Wire enum resolved directly to MPL enum to avoid a translation
        // table that could drift.
        .wrappingAlg(AesWrappingAlg.valueOf(input.getWrappingAlg().getValue()));

    IKeyring keyring = materialProviders.CreateRawAesKeyring(mplInput.build());

    return CreateRawAesKeyringOutput
      .builder()
      // Keyrings register their owning MaterialProviders so
      // OnEncrypt/OnDecrypt can convert materials without an mplId on
      // the wire (see ResourceHandles.owningMaterialProviders).
      .keyringId(
        handles
          .registry()
          .register(ResourceKind.KEYRING, keyring, materialProviders)
      )
      .build();
  }
}
