// Class PointInTimeRecoveryStatus_ENABLED
// Dafny class PointInTimeRecoveryStatus_ENABLED compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class PointInTimeRecoveryStatus_ENABLED extends PointInTimeRecoveryStatus {
  public PointInTimeRecoveryStatus_ENABLED () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    PointInTimeRecoveryStatus_ENABLED o = (PointInTimeRecoveryStatus_ENABLED)other;
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
    s.append("ComAmazonawsDynamodbTypes.PointInTimeRecoveryStatus.ENABLED");
    return s.toString();
  }
}
