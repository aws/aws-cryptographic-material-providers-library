// Class InputCompressionType_NONE
// Dafny class InputCompressionType_NONE compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class InputCompressionType_NONE extends InputCompressionType {
  public InputCompressionType_NONE () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    InputCompressionType_NONE o = (InputCompressionType_NONE)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 2;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.InputCompressionType.NONE");
    return s.toString();
  }
}
