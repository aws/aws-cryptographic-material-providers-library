// Class ScalarAttributeType_N
// Dafny class ScalarAttributeType_N compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ScalarAttributeType_N extends ScalarAttributeType {
  public ScalarAttributeType_N () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ScalarAttributeType_N o = (ScalarAttributeType_N)other;
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
    s.append("ComAmazonawsDynamodbTypes.ScalarAttributeType.N");
    return s.toString();
  }
}
