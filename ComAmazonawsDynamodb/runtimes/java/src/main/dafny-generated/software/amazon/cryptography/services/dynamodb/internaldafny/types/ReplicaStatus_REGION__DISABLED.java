// Class ReplicaStatus_REGION__DISABLED
// Dafny class ReplicaStatus_REGION__DISABLED compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ReplicaStatus_REGION__DISABLED extends ReplicaStatus {
  public ReplicaStatus_REGION__DISABLED () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ReplicaStatus_REGION__DISABLED o = (ReplicaStatus_REGION__DISABLED)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 5;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ReplicaStatus.REGION_DISABLED");
    return s.toString();
  }
}
