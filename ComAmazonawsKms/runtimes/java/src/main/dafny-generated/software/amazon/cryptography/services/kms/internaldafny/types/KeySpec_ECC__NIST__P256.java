// Class KeySpec_ECC__NIST__P256
// Dafny class KeySpec_ECC__NIST__P256 compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class KeySpec_ECC__NIST__P256 extends KeySpec {
  public KeySpec_ECC__NIST__P256 () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KeySpec_ECC__NIST__P256 o = (KeySpec_ECC__NIST__P256)other;
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
    s.append("ComAmazonawsKmsTypes.KeySpec.ECC_NIST_P256");
    return s.toString();
  }
}
