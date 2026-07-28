package aws.cryptography.mpl.testserver.server.protocol;

import java.util.List;
import software.amazon.smithy.java.core.serde.Codec;
import software.amazon.smithy.java.server.Service;
import software.amazon.smithy.java.server.rpcv2.AbstractRpcV2ServerProtocol;
import software.amazon.smithy.model.shapes.ShapeId;

/**
 * A drop-in rpcv2Cbor server protocol identical to the stock one except that its codec
 * emits the {@code __type} discriminator on modeled errors, so
 * {@code GenericServerError} and {@code MaterialProvidersClientError} stay
 * distinguishable through the stock generated client (Requirement 4.9).
 *
 * <p>Request parsing, path-based operation resolution, and input decoding are all
 * inherited unchanged from {@link AbstractRpcV2ServerProtocol}, and the codec delegates
 * every non-error decision to the stock CBOR codec. Only the error response body gains a
 * field.
 *
 * <p><b>Why a distinct protocol id.</b> The framework keys its protocol providers by
 * {@link ShapeId}. Reusing {@code smithy.protocols#rpcv2Cbor} -- the stock provider's key
 * -- would be a duplicate key and throw at startup. Advertising a different id lets this
 * protocol coexist with the stock one; the companion provider then ranks itself ahead so
 * this is the protocol that actually serves the service's requests. The wire behavior
 * remains rpcv2Cbor.
 */
public final class ErrorTypeRpcV2CborServerProtocol extends AbstractRpcV2ServerProtocol {

    /**
     * A protocol id distinct from {@code smithy.protocols#rpcv2Cbor}, so this protocol and
     * the stock one can both live in the framework's ShapeId-keyed provider map.
     */
    static final ShapeId PROTOCOL_ID =
        ShapeId.from("aws.cryptography.materialProviders.testServer#rpcV2CborWithErrorType");

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
