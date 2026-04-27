// Class InputCompressionType_ZSTD
// Dafny class InputCompressionType_ZSTD compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class InputCompressionType_ZSTD extends InputCompressionType {
  public InputCompressionType_ZSTD () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    InputCompressionType_ZSTD o = (InputCompressionType_ZSTD)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 1;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.InputCompressionType.ZSTD");
    return s.toString();
  }
}
