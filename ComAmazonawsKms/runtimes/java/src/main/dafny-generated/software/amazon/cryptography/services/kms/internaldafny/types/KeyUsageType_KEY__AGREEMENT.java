// Class KeyUsageType_KEY__AGREEMENT
// Dafny class KeyUsageType_KEY__AGREEMENT compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class KeyUsageType_KEY__AGREEMENT extends KeyUsageType {
  public KeyUsageType_KEY__AGREEMENT () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KeyUsageType_KEY__AGREEMENT o = (KeyUsageType_KEY__AGREEMENT)other;
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
    s.append("ComAmazonawsKmsTypes.KeyUsageType.KEY_AGREEMENT");
    return s.toString();
  }
}
