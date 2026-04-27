// Class XksProxyConnectivityType_PUBLIC__ENDPOINT
// Dafny class XksProxyConnectivityType_PUBLIC__ENDPOINT compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class XksProxyConnectivityType_PUBLIC__ENDPOINT extends XksProxyConnectivityType {
  public XksProxyConnectivityType_PUBLIC__ENDPOINT () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    XksProxyConnectivityType_PUBLIC__ENDPOINT o = (XksProxyConnectivityType_PUBLIC__ENDPOINT)other;
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
    s.append("ComAmazonawsKmsTypes.XksProxyConnectivityType.PUBLIC_ENDPOINT");
    return s.toString();
  }
}
