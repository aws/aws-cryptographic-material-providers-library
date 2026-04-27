// Class CustomerMasterKeySpec_ECC__SECG__P256K1
// Dafny class CustomerMasterKeySpec_ECC__SECG__P256K1 compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class CustomerMasterKeySpec_ECC__SECG__P256K1 extends CustomerMasterKeySpec {
  public CustomerMasterKeySpec_ECC__SECG__P256K1 () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CustomerMasterKeySpec_ECC__SECG__P256K1 o = (CustomerMasterKeySpec_ECC__SECG__P256K1)other;
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
    s.append("ComAmazonawsKmsTypes.CustomerMasterKeySpec.ECC_SECG_P256K1");
    return s.toString();
  }
}
