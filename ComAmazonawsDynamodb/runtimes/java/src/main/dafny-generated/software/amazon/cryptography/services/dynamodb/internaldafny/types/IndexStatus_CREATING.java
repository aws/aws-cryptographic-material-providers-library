// Class IndexStatus_CREATING
// Dafny class IndexStatus_CREATING compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class IndexStatus_CREATING extends IndexStatus {
  public IndexStatus_CREATING () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    IndexStatus_CREATING o = (IndexStatus_CREATING)other;
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
    s.append("ComAmazonawsDynamodbTypes.IndexStatus.CREATING");
    return s.toString();
  }
}
