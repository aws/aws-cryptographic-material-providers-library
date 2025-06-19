// Class BackupTypeFilter_USER
// Dafny class BackupTypeFilter_USER compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class BackupTypeFilter_USER extends BackupTypeFilter {
  public BackupTypeFilter_USER () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    BackupTypeFilter_USER o = (BackupTypeFilter_USER)other;
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
    s.append("ComAmazonawsDynamodbTypes.BackupTypeFilter.USER");
    return s.toString();
  }
}
