// Class ConnectionErrorCodeType_INTERNAL__ERROR
// Dafny class ConnectionErrorCodeType_INTERNAL__ERROR compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ConnectionErrorCodeType_INTERNAL__ERROR extends ConnectionErrorCodeType {
  public ConnectionErrorCodeType_INTERNAL__ERROR () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ConnectionErrorCodeType_INTERNAL__ERROR o = (ConnectionErrorCodeType_INTERNAL__ERROR)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 3;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.ConnectionErrorCodeType.INTERNAL_ERROR");
    return s.toString();
  }
}
