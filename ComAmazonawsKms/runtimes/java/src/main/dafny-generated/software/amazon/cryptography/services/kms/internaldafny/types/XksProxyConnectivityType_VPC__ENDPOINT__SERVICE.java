// Class XksProxyConnectivityType_VPC__ENDPOINT__SERVICE
// Dafny class XksProxyConnectivityType_VPC__ENDPOINT__SERVICE compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class XksProxyConnectivityType_VPC__ENDPOINT__SERVICE extends XksProxyConnectivityType {
  public XksProxyConnectivityType_VPC__ENDPOINT__SERVICE () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    XksProxyConnectivityType_VPC__ENDPOINT__SERVICE o = (XksProxyConnectivityType_VPC__ENDPOINT__SERVICE)other;
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
    s.append("ComAmazonawsKmsTypes.XksProxyConnectivityType.VPC_ENDPOINT_SERVICE");
    return s.toString();
  }
}
