package aws.cryptography.mpl.testserver.server.protocol;

import java.util.List;
import software.amazon.smithy.java.core.serde.Codec;
import software.amazon.smithy.java.server.Service;
import software.amazon.smithy.java.server.rpcv2.AbstractRpcV2ServerProtocol;
import software.amazon.smithy.model.shapes.ShapeId;

/**
 * rpcv2Cbor server protocol whose codec emits {@code __type} on modeled
 * errors. Uses a distinct protocol id because the framework keys
 * providers by {@link ShapeId} -- reusing
 * {@code smithy.protocols#rpcv2Cbor} would be a duplicate-key clash.
 * Wire behavior is still rpcv2Cbor.
 */
public final class ErrorTypeRpcV2CborServerProtocol
  extends AbstractRpcV2ServerProtocol {

  static final ShapeId PROTOCOL_ID = ShapeId.from(
    "aws.cryptography.materialProviders.testServer#rpcV2CborWithErrorType"
  );

  private final Codec codec = new DiscriminatingCborCodec();

  ErrorTypeRpcV2CborServerProtocol(List<Service> services) {
    super(services, "application/cbor", true);
  }

  @Override
  public ShapeId getProtocolId() {
    return PROTOCOL_ID;
  }

  @Override
  protected Codec codec() {
    return codec;
  }
}
