// Class ConnectionErrorCodeType_USER__NOT__FOUND
// Dafny class ConnectionErrorCodeType_USER__NOT__FOUND compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ConnectionErrorCodeType_USER__NOT__FOUND extends ConnectionErrorCodeType {
  public ConnectionErrorCodeType_USER__NOT__FOUND () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ConnectionErrorCodeType_USER__NOT__FOUND o = (ConnectionErrorCodeType_USER__NOT__FOUND)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 6;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.ConnectionErrorCodeType.USER_NOT_FOUND");
    return s.toString();
  }
}
