// Class TableStatus_INACCESSIBLE__ENCRYPTION__CREDENTIALS
// Dafny class TableStatus_INACCESSIBLE__ENCRYPTION__CREDENTIALS compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class TableStatus_INACCESSIBLE__ENCRYPTION__CREDENTIALS extends TableStatus {
  public TableStatus_INACCESSIBLE__ENCRYPTION__CREDENTIALS () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    TableStatus_INACCESSIBLE__ENCRYPTION__CREDENTIALS o = (TableStatus_INACCESSIBLE__ENCRYPTION__CREDENTIALS)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 4;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.TableStatus.INACCESSIBLE_ENCRYPTION_CREDENTIALS");
    return s.toString();
  }
}
