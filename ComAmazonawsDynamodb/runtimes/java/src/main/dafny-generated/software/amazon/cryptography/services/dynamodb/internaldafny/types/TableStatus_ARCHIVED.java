// Class TableStatus_ARCHIVED
// Dafny class TableStatus_ARCHIVED compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class TableStatus_ARCHIVED extends TableStatus {
  public TableStatus_ARCHIVED () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    TableStatus_ARCHIVED o = (TableStatus_ARCHIVED)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 6;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.TableStatus.ARCHIVED");
    return s.toString();
  }
}
