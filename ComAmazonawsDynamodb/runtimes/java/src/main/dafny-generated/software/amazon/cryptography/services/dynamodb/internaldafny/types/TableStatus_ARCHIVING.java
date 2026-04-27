// Class TableStatus_ARCHIVING
// Dafny class TableStatus_ARCHIVING compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class TableStatus_ARCHIVING extends TableStatus {
  public TableStatus_ARCHIVING () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    TableStatus_ARCHIVING o = (TableStatus_ARCHIVING)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 5;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.TableStatus.ARCHIVING");
    return s.toString();
  }
}
