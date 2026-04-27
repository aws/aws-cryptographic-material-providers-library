// Class BackupStatus_CREATING
// Dafny class BackupStatus_CREATING compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class BackupStatus_CREATING extends BackupStatus {
  public BackupStatus_CREATING () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    BackupStatus_CREATING o = (BackupStatus_CREATING)other;
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
    s.append("ComAmazonawsDynamodbTypes.BackupStatus.CREATING");
    return s.toString();
  }
}
