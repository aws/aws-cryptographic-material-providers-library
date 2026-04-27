// Class BackupStatus_AVAILABLE
// Dafny class BackupStatus_AVAILABLE compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class BackupStatus_AVAILABLE extends BackupStatus {
  public BackupStatus_AVAILABLE () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    BackupStatus_AVAILABLE o = (BackupStatus_AVAILABLE)other;
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
    s.append("ComAmazonawsDynamodbTypes.BackupStatus.AVAILABLE");
    return s.toString();
  }
}
