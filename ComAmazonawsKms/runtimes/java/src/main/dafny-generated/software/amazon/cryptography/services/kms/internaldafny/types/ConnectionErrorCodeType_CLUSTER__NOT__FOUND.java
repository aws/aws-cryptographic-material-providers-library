// Class ConnectionErrorCodeType_CLUSTER__NOT__FOUND
// Dafny class ConnectionErrorCodeType_CLUSTER__NOT__FOUND compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ConnectionErrorCodeType_CLUSTER__NOT__FOUND extends ConnectionErrorCodeType {
  public ConnectionErrorCodeType_CLUSTER__NOT__FOUND () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ConnectionErrorCodeType_CLUSTER__NOT__FOUND o = (ConnectionErrorCodeType_CLUSTER__NOT__FOUND)other;
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
    s.append("ComAmazonawsKmsTypes.ConnectionErrorCodeType.CLUSTER_NOT_FOUND");
    return s.toString();
  }
}
