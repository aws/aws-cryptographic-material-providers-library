// Class ConnectionErrorCodeType_USER__LOGGED__IN
// Dafny class ConnectionErrorCodeType_USER__LOGGED__IN compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ConnectionErrorCodeType_USER__LOGGED__IN extends ConnectionErrorCodeType {
  public ConnectionErrorCodeType_USER__LOGGED__IN () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ConnectionErrorCodeType_USER__LOGGED__IN o = (ConnectionErrorCodeType_USER__LOGGED__IN)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 7;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.ConnectionErrorCodeType.USER_LOGGED_IN");
    return s.toString();
  }
}
