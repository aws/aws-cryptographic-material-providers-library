// Class KeyManagerType_CUSTOMER
// Dafny class KeyManagerType_CUSTOMER compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class KeyManagerType_CUSTOMER extends KeyManagerType {
  public KeyManagerType_CUSTOMER () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KeyManagerType_CUSTOMER o = (KeyManagerType_CUSTOMER)other;
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
    s.append("ComAmazonawsKmsTypes.KeyManagerType.CUSTOMER");
    return s.toString();
  }
}
