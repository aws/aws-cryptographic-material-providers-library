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
 * Creates a Multi-keyring from keyrings the server already holds and
 * returns a handle to it. Every child handle is resolved BEFORE the MPL
 * is called, so a request naming one bad child creates nothing. Handles
 * are why recursion needs no recursive Smithy shape -- a child handle
 * may itself denote a multi-keyring.
 */
public final class CreateMultiKeyringHandler
  implements CreateMultiKeyringOperation {

  private final ResourceHandles handles;
  private final OperationWrapper wrapper;

  public CreateMultiKeyringHandler(
    ResourceHandles handles,
    OperationWrapper wrapper
  ) {
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
    MaterialProviders materialProviders = handles.materialProviders(
      input.getMplId()
    );

    var mplInput =
      software.amazon.cryptography.materialproviders.model.CreateMultiKeyringInput.builder();

    // Generator is optional: absent must stay absent, not become a placeholder.
    if (
      input.getGeneratorKeyringId() != null &&
      !input.getGeneratorKeyringId().isEmpty()
    ) {
      mplInput.generator(handles.keyring(input.getGeneratorKeyringId()));
    }

    // Resolve every child up front so a bad handle prevents creation.
    List<String> childIds = input.getChildKeyringIds() == null
      ? List.of()
      : input.getChildKeyringIds();
    List<IKeyring> children = new ArrayList<>(childIds.size());
    for (String childId : childIds) {
      children.add(handles.keyring(childId));
    }
    mplInput.childKeyrings(children);

    IKeyring keyring = materialProviders.CreateMultiKeyring(mplInput.build());

    return CreateMultiKeyringOutput
      .builder()
      .keyringId(
        handles
          .registry()
          .register(ResourceKind.KEYRING, keyring, materialProviders)
      )
      .build();
  }
}
