// Class ReplicaStatus_INACCESSIBLE__ENCRYPTION__CREDENTIALS
// Dafny class ReplicaStatus_INACCESSIBLE__ENCRYPTION__CREDENTIALS compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ReplicaStatus_INACCESSIBLE__ENCRYPTION__CREDENTIALS extends ReplicaStatus {
  public ReplicaStatus_INACCESSIBLE__ENCRYPTION__CREDENTIALS () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ReplicaStatus_INACCESSIBLE__ENCRYPTION__CREDENTIALS o = (ReplicaStatus_INACCESSIBLE__ENCRYPTION__CREDENTIALS)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 6;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ReplicaStatus.INACCESSIBLE_ENCRYPTION_CREDENTIALS");
    return s.toString();
  }
}
