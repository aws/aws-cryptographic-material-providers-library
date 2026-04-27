// Class SSEStatus_DISABLING
// Dafny class SSEStatus_DISABLING compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class SSEStatus_DISABLING extends SSEStatus {
  public SSEStatus_DISABLING () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    SSEStatus_DISABLING o = (SSEStatus_DISABLING)other;
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
    s.append("ComAmazonawsDynamodbTypes.SSEStatus.DISABLING");
    return s.toString();
  }
}
