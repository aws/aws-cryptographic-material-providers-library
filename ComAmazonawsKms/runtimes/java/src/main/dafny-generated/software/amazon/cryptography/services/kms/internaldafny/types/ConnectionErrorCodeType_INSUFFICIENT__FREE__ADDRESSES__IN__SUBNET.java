// Class ConnectionErrorCodeType_INSUFFICIENT__FREE__ADDRESSES__IN__SUBNET
// Dafny class ConnectionErrorCodeType_INSUFFICIENT__FREE__ADDRESSES__IN__SUBNET compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ConnectionErrorCodeType_INSUFFICIENT__FREE__ADDRESSES__IN__SUBNET extends ConnectionErrorCodeType {
  public ConnectionErrorCodeType_INSUFFICIENT__FREE__ADDRESSES__IN__SUBNET () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ConnectionErrorCodeType_INSUFFICIENT__FREE__ADDRESSES__IN__SUBNET o = (ConnectionErrorCodeType_INSUFFICIENT__FREE__ADDRESSES__IN__SUBNET)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 9;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.ConnectionErrorCodeType.INSUFFICIENT_FREE_ADDRESSES_IN_SUBNET");
    return s.toString();
  }
}
