// Class ConnectionStateType_FAILED
// Dafny class ConnectionStateType_FAILED compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ConnectionStateType_FAILED extends ConnectionStateType {
  public ConnectionStateType_FAILED () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ConnectionStateType_FAILED o = (ConnectionStateType_FAILED)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 2;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.ConnectionStateType.FAILED");
    return s.toString();
  }
}
