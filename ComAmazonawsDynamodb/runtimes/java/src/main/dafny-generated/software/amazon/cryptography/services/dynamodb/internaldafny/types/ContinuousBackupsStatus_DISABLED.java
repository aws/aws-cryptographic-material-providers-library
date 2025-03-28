// Class ContinuousBackupsStatus_DISABLED
// Dafny class ContinuousBackupsStatus_DISABLED compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ContinuousBackupsStatus_DISABLED extends ContinuousBackupsStatus {
  public ContinuousBackupsStatus_DISABLED () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ContinuousBackupsStatus_DISABLED o = (ContinuousBackupsStatus_DISABLED)other;
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
    s.append("ComAmazonawsDynamodbTypes.ContinuousBackupsStatus.DISABLED");
    return s.toString();
  }
}
