package aws.cryptography.mpl.testserver.server.protocol;

import java.util.List;
import software.amazon.smithy.java.server.Service;
import software.amazon.smithy.java.server.core.ServerProtocol;
import software.amazon.smithy.java.server.core.ServerProtocolProvider;
import software.amazon.smithy.model.shapes.ShapeId;

/**
 * SPI provider for {@link ErrorTypeRpcV2CborServerProtocol}, registered through
 * {@code META-INF/services/software.amazon.smithy.java.server.core.ServerProtocolProvider}.
 *
 * <p>It advertises a distinct protocol id so it does not collide with the stock rpcv2Cbor
 * provider in the framework's ShapeId-keyed provider map. The framework sorts providers by
 * {@link #precision()} ascending and dispatches each request to the first protocol that
 * resolves it, so returning a value below the stock provider's makes this the protocol that
 * serves the service -- and therefore makes the {@code __type}-emitting error
 * serialization what clients actually see.
 */
public final class ErrorTypeRpcV2CborServerProtocolProvider implements ServerProtocolProvider {

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
        // Sorted ascending; lower is tried first. Beat the stock provider (0) so this
        // protocol handles the service's rpcv2 requests.
        return -100;
    }
}
