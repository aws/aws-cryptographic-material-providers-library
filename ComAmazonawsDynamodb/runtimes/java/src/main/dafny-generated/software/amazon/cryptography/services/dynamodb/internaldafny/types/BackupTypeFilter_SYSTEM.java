// Class BackupTypeFilter_SYSTEM
// Dafny class BackupTypeFilter_SYSTEM compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class BackupTypeFilter_SYSTEM extends BackupTypeFilter {
  public BackupTypeFilter_SYSTEM () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    BackupTypeFilter_SYSTEM o = (BackupTypeFilter_SYSTEM)other;
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
    s.append("ComAmazonawsDynamodbTypes.BackupTypeFilter.SYSTEM");
    return s.toString();
  }
}
