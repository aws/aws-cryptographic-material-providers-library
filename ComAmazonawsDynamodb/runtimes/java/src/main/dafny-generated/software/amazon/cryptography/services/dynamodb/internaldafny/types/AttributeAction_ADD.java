// Class AttributeAction_ADD
// Dafny class AttributeAction_ADD compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class AttributeAction_ADD extends AttributeAction {
  public AttributeAction_ADD () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    AttributeAction_ADD o = (AttributeAction_ADD)other;
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
    s.append("ComAmazonawsDynamodbTypes.AttributeAction.ADD");
    return s.toString();
  }
}
