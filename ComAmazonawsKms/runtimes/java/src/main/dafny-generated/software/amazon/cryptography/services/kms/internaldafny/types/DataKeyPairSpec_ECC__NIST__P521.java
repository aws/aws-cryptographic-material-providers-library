// Class DataKeyPairSpec_ECC__NIST__P521
// Dafny class DataKeyPairSpec_ECC__NIST__P521 compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class DataKeyPairSpec_ECC__NIST__P521 extends DataKeyPairSpec {
  public DataKeyPairSpec_ECC__NIST__P521 () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DataKeyPairSpec_ECC__NIST__P521 o = (DataKeyPairSpec_ECC__NIST__P521)other;
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
    s.append("ComAmazonawsKmsTypes.DataKeyPairSpec.ECC_NIST_P521");
    return s.toString();
  }
}
