// Class SSEStatus_UPDATING
// Dafny class SSEStatus_UPDATING compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class SSEStatus_UPDATING extends SSEStatus {
  public SSEStatus_UPDATING () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    SSEStatus_UPDATING o = (SSEStatus_UPDATING)other;
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
    s.append("ComAmazonawsDynamodbTypes.SSEStatus.UPDATING");
    return s.toString();
  }
}
