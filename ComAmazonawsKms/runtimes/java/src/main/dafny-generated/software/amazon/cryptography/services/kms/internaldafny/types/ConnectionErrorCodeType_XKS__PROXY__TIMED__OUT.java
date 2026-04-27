// Class ConnectionErrorCodeType_XKS__PROXY__TIMED__OUT
// Dafny class ConnectionErrorCodeType_XKS__PROXY__TIMED__OUT compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ConnectionErrorCodeType_XKS__PROXY__TIMED__OUT extends ConnectionErrorCodeType {
  public ConnectionErrorCodeType_XKS__PROXY__TIMED__OUT () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ConnectionErrorCodeType_XKS__PROXY__TIMED__OUT o = (ConnectionErrorCodeType_XKS__PROXY__TIMED__OUT)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 16;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.ConnectionErrorCodeType.XKS_PROXY_TIMED_OUT");
    return s.toString();
  }
}
