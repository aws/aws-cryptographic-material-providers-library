package aws.cryptography.mpl.testserver.server.protocol;

import java.util.List;
import software.amazon.smithy.java.server.Service;
import software.amazon.smithy.java.server.core.ServerProtocol;
import software.amazon.smithy.java.server.core.ServerProtocolProvider;
import software.amazon.smithy.model.shapes.ShapeId;

/**
 * SPI provider for {@link ErrorTypeRpcV2CborServerProtocol}. Framework
 * sorts providers by precision ascending (lower tried first), so -100
 * beats the stock provider's 0 and makes the discriminating codec the
 * one that actually serves requests.
 */
public final class ErrorTypeRpcV2CborServerProtocolProvider
  implements ServerProtocolProvider {

  @Override
  public ServerProtocol provideProtocolHandler(List<Service> services) {
    return new ErrorTypeRpcV2CborServerProtocol(services);
  }

  @Override
  public ShapeId getProtocolId() {
    return ErrorTypeRpcV2CborServerProtocol.PROTOCOL_ID;
  }

  @Override
  public int precision() {
    // Sorted ascending; -100 beats stock provider's 0.
    return -100;
  }
}
