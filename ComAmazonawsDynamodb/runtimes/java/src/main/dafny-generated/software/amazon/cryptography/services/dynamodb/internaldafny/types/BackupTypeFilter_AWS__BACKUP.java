// Class BackupTypeFilter_AWS__BACKUP
// Dafny class BackupTypeFilter_AWS__BACKUP compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class BackupTypeFilter_AWS__BACKUP extends BackupTypeFilter {
  public BackupTypeFilter_AWS__BACKUP () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    BackupTypeFilter_AWS__BACKUP o = (BackupTypeFilter_AWS__BACKUP)other;
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
    s.append("ComAmazonawsDynamodbTypes.BackupTypeFilter.AWS_BACKUP");
    return s.toString();
  }
}
