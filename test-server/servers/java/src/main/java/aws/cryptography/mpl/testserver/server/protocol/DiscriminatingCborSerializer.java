package aws.cryptography.mpl.testserver.server.protocol;

import java.math.BigDecimal;
import java.math.BigInteger;
import java.nio.ByteBuffer;
import java.time.Instant;
import java.util.function.BiConsumer;
import software.amazon.smithy.java.core.error.ModeledException;
import software.amazon.smithy.java.core.schema.Schema;
import software.amazon.smithy.java.core.schema.SerializableStruct;
import software.amazon.smithy.java.core.serde.MapSerializer;
import software.amazon.smithy.java.core.serde.ShapeSerializer;
import software.amazon.smithy.java.core.serde.document.Document;
import software.amazon.smithy.java.core.serde.event.EventStream;
import software.amazon.smithy.java.io.datastream.DataStream;

/**
 * Delegates every serialization decision to the stock rpcv2Cbor serializer, EXCEPT that
 * a modeled error is written as a <em>discriminated document</em> rather than a plain
 * struct.
 *
 * <p><b>Why this class exists.</b> Stock smithy-java through 1.4.0 serializes a modeled
 * error over rpcv2Cbor as a bare map of its members -- {@code {"message": ...}} -- with
 * no {@code __type} discriminator, even though the per-operation {@code TypeRegistry} is
 * correctly populated with both error shapes. The generated client's error deserializer
 * keys off {@code __type} to pick the concrete shape, so without it BOTH
 * {@code GenericServerError} and {@code MaterialProvidersClientError} arrive as an
 * untyped {@code CallException}.
 *
 * <p>That would defeat a core guarantee of this harness (Requirement 4.9): a test must be
 * able to tell "the MPL rejected this" from "the harness is broken", and must be able to
 * read the MPL's own message. Collapsing both into one opaque type makes every negative
 * test assert nothing more than "something went wrong".
 *
 * <p>Serializing the error as {@code Document.of(struct)} routes it through the CBOR
 * <em>document</em> path, which emits {@code __type} (the error's absolute shape id)
 * alongside the members. Non-error structs -- meaning every successful response -- are
 * delegated untouched, so success responses stay byte-identical to stock.
 */
final class DiscriminatingCborSerializer implements ShapeSerializer {

    private final ShapeSerializer delegate;

    DiscriminatingCborSerializer(ShapeSerializer delegate) {
        this.delegate = delegate;
    }

    @Override
    public void writeStruct(Schema schema, SerializableStruct struct) {
        if (struct instanceof ModeledException) {
            // The document path is what emits __type. This single branch is the whole fix.
            Document.of(struct).serialize(delegate);
        } else {
            delegate.writeStruct(schema, struct);
        }
    }

    // ---- everything else delegates unchanged --------------------------------

    @Override
    public <T> void writeList(Schema schema, T state, int size,
                              BiConsumer<T, ShapeSerializer> consumer) {
        delegate.writeList(schema, state, size, consumer);
    }

    @Override
    public <T> void writeMap(Schema schema, T state, int size,
                             BiConsumer<T, MapSerializer> consumer) {
        delegate.writeMap(schema, state, size, consumer);
    }

    @Override
    public void writeBoolean(Schema schema, boolean value) {
        delegate.writeBoolean(schema, value);
    }

    @Override
    public void writeByte(Schema schema, byte value) {
        delegate.writeByte(schema, value);
    }

    @Override
    public void writeShort(Schema schema, short value) {
        delegate.writeShort(schema, value);
    }

    @Override
    public void writeInteger(Schema schema, int value) {
        delegate.writeInteger(schema, value);
    }

    @Override
    public void writeLong(Schema schema, long value) {
        delegate.writeLong(schema, value);
    }

    @Override
    public void writeFloat(Schema schema, float value) {
        delegate.writeFloat(schema, value);
    }

    @Override
    public void writeDouble(Schema schema, double value) {
        delegate.writeDouble(schema, value);
    }

    @Override
    public void writeBigInteger(Schema schema, BigInteger value) {
        delegate.writeBigInteger(schema, value);
    }

    @Override
    public void writeBigDecimal(Schema schema, BigDecimal value) {
        delegate.writeBigDecimal(schema, value);
    }

    @Override
    public void writeString(Schema schema, String value) {
        delegate.writeString(schema, value);
    }

    @Override
    public void writeBlob(Schema schema, ByteBuffer value) {
        delegate.writeBlob(schema, value);
    }

    @Override
    public void writeBlob(Schema schema, byte[] value) {
        delegate.writeBlob(schema, value);
    }

    @Override
    public void writeDataStream(Schema schema, DataStream value) {
        delegate.writeDataStream(schema, value);
    }

    @Override
    public void writeEventStream(Schema schema,
                                 EventStream<? extends SerializableStruct> value) {
        delegate.writeEventStream(schema, value);
    }

    @Override
    public void writeTimestamp(Schema schema, Instant value) {
        delegate.writeTimestamp(schema, value);
    }

    @Override
    public void writeDocument(Schema schema, Document value) {
        delegate.writeDocument(schema, value);
    }

    @Override
    public void writeNull(Schema schema) {
        delegate.writeNull(schema);
    }

    @Override
    public void flush() {
        delegate.flush();
    }

    @Override
    public void close() {
        delegate.close();
    }
}
