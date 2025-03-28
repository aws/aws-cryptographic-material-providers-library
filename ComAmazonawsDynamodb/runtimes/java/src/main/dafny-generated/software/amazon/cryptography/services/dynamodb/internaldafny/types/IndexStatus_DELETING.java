// Class IndexStatus_DELETING
// Dafny class IndexStatus_DELETING compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class IndexStatus_DELETING extends IndexStatus {
  public IndexStatus_DELETING () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    IndexStatus_DELETING o = (IndexStatus_DELETING)other;
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
    s.append("ComAmazonawsDynamodbTypes.IndexStatus.DELETING");
    return s.toString();
  }
}
