// Class DataKeyPairSpec_ECC__SECG__P256K1
// Dafny class DataKeyPairSpec_ECC__SECG__P256K1 compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class DataKeyPairSpec_ECC__SECG__P256K1 extends DataKeyPairSpec {
  public DataKeyPairSpec_ECC__SECG__P256K1 () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DataKeyPairSpec_ECC__SECG__P256K1 o = (DataKeyPairSpec_ECC__SECG__P256K1)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 6;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.DataKeyPairSpec.ECC_SECG_P256K1");
    return s.toString();
  }
}
