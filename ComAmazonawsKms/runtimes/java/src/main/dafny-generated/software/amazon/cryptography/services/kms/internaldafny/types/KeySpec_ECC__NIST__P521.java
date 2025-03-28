// Class KeySpec_ECC__NIST__P521
// Dafny class KeySpec_ECC__NIST__P521 compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class KeySpec_ECC__NIST__P521 extends KeySpec {
  public KeySpec_ECC__NIST__P521 () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KeySpec_ECC__NIST__P521 o = (KeySpec_ECC__NIST__P521)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 5;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.KeySpec.ECC_NIST_P521");
    return s.toString();
  }
}
