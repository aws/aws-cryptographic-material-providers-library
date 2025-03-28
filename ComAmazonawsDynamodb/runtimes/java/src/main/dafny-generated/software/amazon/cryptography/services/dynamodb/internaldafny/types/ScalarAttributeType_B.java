// Class ScalarAttributeType_B
// Dafny class ScalarAttributeType_B compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ScalarAttributeType_B extends ScalarAttributeType {
  public ScalarAttributeType_B () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ScalarAttributeType_B o = (ScalarAttributeType_B)other;
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
    s.append("ComAmazonawsDynamodbTypes.ScalarAttributeType.B");
    return s.toString();
  }
}
