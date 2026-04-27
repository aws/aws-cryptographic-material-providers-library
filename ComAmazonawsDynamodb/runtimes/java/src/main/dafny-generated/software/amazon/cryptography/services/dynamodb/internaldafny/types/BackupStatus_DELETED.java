// Class BackupStatus_DELETED
// Dafny class BackupStatus_DELETED compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class BackupStatus_DELETED extends BackupStatus {
  public BackupStatus_DELETED () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    BackupStatus_DELETED o = (BackupStatus_DELETED)other;
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
    s.append("ComAmazonawsDynamodbTypes.BackupStatus.DELETED");
    return s.toString();
  }
}
