package aws.cryptography.mpl.testserver.server.protocol;

import java.io.OutputStream;
import java.nio.ByteBuffer;
import software.amazon.smithy.java.cbor.Rpcv2CborCodec;
import software.amazon.smithy.java.core.serde.Codec;
import software.amazon.smithy.java.core.serde.ShapeDeserializer;
import software.amazon.smithy.java.core.serde.ShapeSerializer;

/**
 * A {@link Codec} identical to the stock rpcv2Cbor codec for all deserialization and for
 * non-error serialization, but whose serializer emits the {@code __type} discriminator on
 * modeled errors (see {@link DiscriminatingCborSerializer} for why that is necessary).
 *
 * <p>This is the entire surface of the fix: one wrapped serializer. The model, the
 * generated client, and the wire form of every successful response are untouched.
 */
public final class DiscriminatingCborCodec implements Codec {

    private final Codec delegate = Rpcv2CborCodec.builder().build();

    @Override
    public ShapeSerializer createSerializer(OutputStream sink) {
        return new DiscriminatingCborSerializer(delegate.createSerializer(sink));
    }

    @Override
    public ShapeDeserializer createDeserializer(byte[] source) {
        return delegate.createDeserializer(source);
    }

    @Override
    public ShapeDeserializer createDeserializer(ByteBuffer source) {
        return delegate.createDeserializer(source);
    }

    @Override
    public void close() {
        delegate.close();
    }
}
