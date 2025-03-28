// Class ScalarAttributeType_S
// Dafny class ScalarAttributeType_S compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ScalarAttributeType_S extends ScalarAttributeType {
  public ScalarAttributeType_S () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ScalarAttributeType_S o = (ScalarAttributeType_S)other;
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
    s.append("ComAmazonawsDynamodbTypes.ScalarAttributeType.S");
    return s.toString();
  }
}
