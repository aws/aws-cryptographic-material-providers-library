// Class ConnectionErrorCodeType_INVALID__CREDENTIALS
// Dafny class ConnectionErrorCodeType_INVALID__CREDENTIALS compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ConnectionErrorCodeType_INVALID__CREDENTIALS extends ConnectionErrorCodeType {
  public ConnectionErrorCodeType_INVALID__CREDENTIALS () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ConnectionErrorCodeType_INVALID__CREDENTIALS o = (ConnectionErrorCodeType_INVALID__CREDENTIALS)other;
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
    s.append("ComAmazonawsKmsTypes.ConnectionErrorCodeType.INVALID_CREDENTIALS");
    return s.toString();
  }
}
