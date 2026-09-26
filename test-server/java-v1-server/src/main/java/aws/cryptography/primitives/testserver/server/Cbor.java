package aws.cryptography.primitives.testserver.server;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ObjectNode;
import com.fasterxml.jackson.dataformat.cbor.CBORFactory;
import java.io.IOException;
import java.nio.ByteBuffer;

/** CBOR read/write helpers: blobs travel as byte strings, enums as text. */
final class Cbor {

  private static final ObjectMapper MAPPER = new ObjectMapper(
    new CBORFactory()
  );

  private Cbor() {}

  static JsonNode decode(byte[] body) {
    try {
      return MAPPER.readTree(body);
    } catch (IOException e) {
      throw ModeledError.generic(
        "failed to decode CBOR request: " + e.getMessage()
      );
    }
  }

  static byte[] encode(ObjectNode node) {
    try {
      return MAPPER.writeValueAsBytes(node);
    } catch (IOException e) {
      throw ModeledError.generic(
        "failed to encode CBOR response: " + e.getMessage()
      );
    }
  }

  static ObjectNode object() {
    return MAPPER.createObjectNode();
  }

  static byte[] blob(JsonNode request, String field) {
    JsonNode value = request.get(field);
    if (value == null || !value.isBinary()) {
      throw ModeledError.generic("missing or non-blob field: " + field);
    }
    try {
      return value.binaryValue();
    } catch (IOException e) {
      throw ModeledError.generic("invalid blob field: " + field);
    }
  }

  static String string(JsonNode request, String field) {
    JsonNode value = request.get(field);
    if (value == null || !value.isTextual()) {
      throw ModeledError.generic("missing or non-string field: " + field);
    }
    return value.asText();
  }

  static int integer(JsonNode request, String field) {
    JsonNode value = request.get(field);
    if (value == null || !value.isNumber()) {
      throw ModeledError.generic("missing or non-integer field: " + field);
    }
    return value.asInt();
  }

  static byte[] bytes(ByteBuffer buffer) {
    ByteBuffer view = buffer.duplicate();
    byte[] out = new byte[view.remaining()];
    view.get(out);
    return out;
  }
}
