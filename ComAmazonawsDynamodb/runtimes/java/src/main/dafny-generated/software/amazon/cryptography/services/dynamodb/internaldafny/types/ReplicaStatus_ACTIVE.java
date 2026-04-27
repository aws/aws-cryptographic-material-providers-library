// Class ReplicaStatus_ACTIVE
// Dafny class ReplicaStatus_ACTIVE compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ReplicaStatus_ACTIVE extends ReplicaStatus {
  public ReplicaStatus_ACTIVE () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ReplicaStatus_ACTIVE o = (ReplicaStatus_ACTIVE)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 4;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ReplicaStatus.ACTIVE");
    return s.toString();
  }
}
