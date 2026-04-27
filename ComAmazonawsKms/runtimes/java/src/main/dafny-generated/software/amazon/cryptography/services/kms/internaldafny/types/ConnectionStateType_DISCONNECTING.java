// Class ConnectionStateType_DISCONNECTING
// Dafny class ConnectionStateType_DISCONNECTING compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ConnectionStateType_DISCONNECTING extends ConnectionStateType {
  public ConnectionStateType_DISCONNECTING () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ConnectionStateType_DISCONNECTING o = (ConnectionStateType_DISCONNECTING)other;
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
    s.append("ComAmazonawsKmsTypes.ConnectionStateType.DISCONNECTING");
    return s.toString();
  }
}
