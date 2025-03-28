// Class GlobalTableStatus_DELETING
// Dafny class GlobalTableStatus_DELETING compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class GlobalTableStatus_DELETING extends GlobalTableStatus {
  public GlobalTableStatus_DELETING () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GlobalTableStatus_DELETING o = (GlobalTableStatus_DELETING)other;
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
    s.append("ComAmazonawsDynamodbTypes.GlobalTableStatus.DELETING");
    return s.toString();
  }
}
