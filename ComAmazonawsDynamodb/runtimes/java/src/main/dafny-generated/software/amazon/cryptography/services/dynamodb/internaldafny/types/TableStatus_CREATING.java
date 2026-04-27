// Class TableStatus_CREATING
// Dafny class TableStatus_CREATING compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class TableStatus_CREATING extends TableStatus {
  public TableStatus_CREATING () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    TableStatus_CREATING o = (TableStatus_CREATING)other;
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
    s.append("ComAmazonawsDynamodbTypes.TableStatus.CREATING");
    return s.toString();
  }
}
