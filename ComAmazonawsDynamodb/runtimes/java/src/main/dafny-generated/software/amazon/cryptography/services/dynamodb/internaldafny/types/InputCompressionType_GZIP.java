// Class InputCompressionType_GZIP
// Dafny class InputCompressionType_GZIP compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class InputCompressionType_GZIP extends InputCompressionType {
  public InputCompressionType_GZIP () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    InputCompressionType_GZIP o = (InputCompressionType_GZIP)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.InputCompressionType.GZIP");
    return s.toString();
  }
}
