// Class PointInTimeRecoveryStatus_DISABLED
// Dafny class PointInTimeRecoveryStatus_DISABLED compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class PointInTimeRecoveryStatus_DISABLED extends PointInTimeRecoveryStatus {
  public PointInTimeRecoveryStatus_DISABLED () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    PointInTimeRecoveryStatus_DISABLED o = (PointInTimeRecoveryStatus_DISABLED)other;
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
    s.append("ComAmazonawsDynamodbTypes.PointInTimeRecoveryStatus.DISABLED");
    return s.toString();
  }
}
