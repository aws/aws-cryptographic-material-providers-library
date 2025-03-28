// Class KeyUsageType_SIGN__VERIFY
// Dafny class KeyUsageType_SIGN__VERIFY compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class KeyUsageType_SIGN__VERIFY extends KeyUsageType {
  public KeyUsageType_SIGN__VERIFY () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KeyUsageType_SIGN__VERIFY o = (KeyUsageType_SIGN__VERIFY)other;
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
    s.append("ComAmazonawsKmsTypes.KeyUsageType.SIGN_VERIFY");
    return s.toString();
  }
}
