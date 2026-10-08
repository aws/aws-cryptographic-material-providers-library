package aws.cryptography.mpl.testserver.server;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ArrayNode;
import com.fasterxml.jackson.databind.node.ObjectNode;
import com.fasterxml.jackson.dataformat.cbor.CBORFactory;
import java.io.IOException;
import java.nio.ByteBuffer;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

/**
 * CBOR read/write helpers: blobs travel as byte strings, enums as text. A
 * missing or mistyped required member is the harness's fault, so it is a
 * GenericServerError.
 */
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

  static boolean present(JsonNode node, String field) {
    JsonNode value = node.get(field);
    return value != null && !value.isNull();
  }

  static JsonNode member(JsonNode node, String field) {
    if (!present(node, field)) {
      throw ModeledError.generic("missing required member: " + field);
    }
    return node.get(field);
  }

  static byte[] blob(JsonNode node, String field) {
    JsonNode value = member(node, field);
    if (!value.isBinary()) {
      throw ModeledError.generic("member is not a blob: " + field);
    }
    try {
      return value.binaryValue();
    } catch (IOException e) {
      throw ModeledError.generic("invalid blob member: " + field);
    }
  }

  static ByteBuffer optionalBlob(JsonNode node, String field) {
    return present(node, field) ? ByteBuffer.wrap(blob(node, field)) : null;
  }

  static String string(JsonNode node, String field) {
    JsonNode value = member(node, field);
    if (!value.isTextual()) {
      throw ModeledError.generic("member is not a string: " + field);
    }
    return value.asText();
  }

  static long longValue(JsonNode node, String field) {
    JsonNode value = member(node, field);
    if (!value.isIntegralNumber()) {
      throw ModeledError.generic("member is not an integer: " + field);
    }
    return value.asLong();
  }

  /** A string-to-string map member; absent means empty. */
  static Map<String, String> stringMap(JsonNode node, String field) {
    Map<String, String> out = new LinkedHashMap<>();
    if (!present(node, field)) {
      return out;
    }
    JsonNode value = node.get(field);
    if (!value.isObject()) {
      throw ModeledError.generic("member is not a map: " + field);
    }
    Iterator<Map.Entry<String, JsonNode>> fields = value.fields();
    while (fields.hasNext()) {
      Map.Entry<String, JsonNode> entry = fields.next();
      if (!entry.getValue().isTextual()) {
        throw ModeledError.generic(
          "map value is not a string: " + field + "." + entry.getKey()
        );
      }
      out.put(entry.getKey(), entry.getValue().asText());
    }
    return out;
  }

  /** A list-of-strings member; absent means empty. */
  static List<String> stringList(JsonNode node, String field) {
    List<String> out = new ArrayList<>();
    if (!present(node, field)) {
      return out;
    }
    for (JsonNode element : list(node, field)) {
      if (!element.isTextual()) {
        throw ModeledError.generic("list element is not a string: " + field);
      }
      out.add(element.asText());
    }
    return out;
  }

  /** A list-of-blobs member, or null when absent. */
  static List<ByteBuffer> optionalBlobList(JsonNode node, String field) {
    if (!present(node, field)) {
      return null;
    }
    List<ByteBuffer> out = new ArrayList<>();
    for (JsonNode element : list(node, field)) {
      if (!element.isBinary()) {
        throw ModeledError.generic("list element is not a blob: " + field);
      }
      try {
        out.add(ByteBuffer.wrap(element.binaryValue()));
      } catch (IOException e) {
        throw ModeledError.generic("invalid blob in list: " + field);
      }
    }
    return out;
  }

  static JsonNode list(JsonNode node, String field) {
    JsonNode value = member(node, field);
    if (!value.isArray()) {
      throw ModeledError.generic("member is not a list: " + field);
    }
    return value;
  }

  static void putMap(ObjectNode node, String field, Map<String, String> map) {
    ObjectNode out = node.putObject(field);
    if (map != null) {
      map.forEach(out::put);
    }
  }

  static void putStringList(ObjectNode node, String field, List<String> list) {
    ArrayNode out = node.putArray(field);
    if (list != null) {
      list.forEach(out::add);
    }
  }

  static void putOptionalBlob(ObjectNode node, String field, ByteBuffer value) {
    if (value != null) {
      node.put(field, bytes(value));
    }
  }

  static void putOptionalBlobList(
    ObjectNode node,
    String field,
    List<ByteBuffer> values
  ) {
    if (values != null) {
      ArrayNode out = node.putArray(field);
      values.forEach(value -> out.add(bytes(value)));
    }
  }

  /** Copy a ByteBuffer's remaining bytes without moving its position. */
  static byte[] bytes(ByteBuffer buffer) {
    ByteBuffer view = buffer.duplicate();
    byte[] out = new byte[view.remaining()];
    view.get(out);
    return out;
  }
}
