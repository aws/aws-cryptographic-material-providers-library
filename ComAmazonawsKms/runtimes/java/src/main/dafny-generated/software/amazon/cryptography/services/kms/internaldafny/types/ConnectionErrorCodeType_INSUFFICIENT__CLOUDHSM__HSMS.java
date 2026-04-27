// Class ConnectionErrorCodeType_INSUFFICIENT__CLOUDHSM__HSMS
// Dafny class ConnectionErrorCodeType_INSUFFICIENT__CLOUDHSM__HSMS compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ConnectionErrorCodeType_INSUFFICIENT__CLOUDHSM__HSMS extends ConnectionErrorCodeType {
  public ConnectionErrorCodeType_INSUFFICIENT__CLOUDHSM__HSMS () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ConnectionErrorCodeType_INSUFFICIENT__CLOUDHSM__HSMS o = (ConnectionErrorCodeType_INSUFFICIENT__CLOUDHSM__HSMS)other;
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
    s.append("ComAmazonawsKmsTypes.ConnectionErrorCodeType.INSUFFICIENT_CLOUDHSM_HSMS");
    return s.toString();
  }
}
