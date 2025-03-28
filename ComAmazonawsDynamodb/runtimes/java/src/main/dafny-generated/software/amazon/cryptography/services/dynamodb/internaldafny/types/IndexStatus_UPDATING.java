// Class IndexStatus_UPDATING
// Dafny class IndexStatus_UPDATING compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class IndexStatus_UPDATING extends IndexStatus {
  public IndexStatus_UPDATING () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    IndexStatus_UPDATING o = (IndexStatus_UPDATING)other;
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
    s.append("ComAmazonawsDynamodbTypes.IndexStatus.UPDATING");
    return s.toString();
  }
}
