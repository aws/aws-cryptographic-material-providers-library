package aws.cryptography.mpl.testserver.server.protocol;

import java.io.OutputStream;
import java.nio.ByteBuffer;
import software.amazon.smithy.java.cbor.Rpcv2CborCodec;
import software.amazon.smithy.java.core.serde.Codec;
import software.amazon.smithy.java.core.serde.ShapeDeserializer;
import software.amazon.smithy.java.core.serde.ShapeSerializer;

/**
 * Codec identical to stock rpcv2Cbor except the serializer emits
 * {@code __type} on modeled errors. See
 * {@link DiscriminatingCborSerializer} for the underlying bug.
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
