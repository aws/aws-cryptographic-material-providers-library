// Class ReplicaStatus_CREATION__FAILED
// Dafny class ReplicaStatus_CREATION__FAILED compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ReplicaStatus_CREATION__FAILED extends ReplicaStatus {
  public ReplicaStatus_CREATION__FAILED () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ReplicaStatus_CREATION__FAILED o = (ReplicaStatus_CREATION__FAILED)other;
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
    s.append("ComAmazonawsDynamodbTypes.ReplicaStatus.CREATION_FAILED");
    return s.toString();
  }
}
