// Class SSEStatus_ENABLED
// Dafny class SSEStatus_ENABLED compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class SSEStatus_ENABLED extends SSEStatus {
  public SSEStatus_ENABLED () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    SSEStatus_ENABLED o = (SSEStatus_ENABLED)other;
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
    s.append("ComAmazonawsDynamodbTypes.SSEStatus.ENABLED");
    return s.toString();
  }
}
