// Class GlobalTableStatus_ACTIVE
// Dafny class GlobalTableStatus_ACTIVE compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class GlobalTableStatus_ACTIVE extends GlobalTableStatus {
  public GlobalTableStatus_ACTIVE () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GlobalTableStatus_ACTIVE o = (GlobalTableStatus_ACTIVE)other;
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
    s.append("ComAmazonawsDynamodbTypes.GlobalTableStatus.ACTIVE");
    return s.toString();
  }
}
