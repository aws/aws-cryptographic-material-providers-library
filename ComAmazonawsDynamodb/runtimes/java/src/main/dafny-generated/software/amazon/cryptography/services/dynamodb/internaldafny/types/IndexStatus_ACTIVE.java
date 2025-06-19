// Class IndexStatus_ACTIVE
// Dafny class IndexStatus_ACTIVE compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class IndexStatus_ACTIVE extends IndexStatus {
  public IndexStatus_ACTIVE () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    IndexStatus_ACTIVE o = (IndexStatus_ACTIVE)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 3;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.IndexStatus.ACTIVE");
    return s.toString();
  }
}
