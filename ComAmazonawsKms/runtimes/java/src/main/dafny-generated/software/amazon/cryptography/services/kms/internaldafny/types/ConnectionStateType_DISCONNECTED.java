// Class ConnectionStateType_DISCONNECTED
// Dafny class ConnectionStateType_DISCONNECTED compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ConnectionStateType_DISCONNECTED extends ConnectionStateType {
  public ConnectionStateType_DISCONNECTED () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ConnectionStateType_DISCONNECTED o = (ConnectionStateType_DISCONNECTED)other;
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
    s.append("ComAmazonawsKmsTypes.ConnectionStateType.DISCONNECTED");
    return s.toString();
  }
}
