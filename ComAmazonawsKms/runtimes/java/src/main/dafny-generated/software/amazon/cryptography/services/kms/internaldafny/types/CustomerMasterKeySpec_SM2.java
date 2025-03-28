// Class CustomerMasterKeySpec_SM2
// Dafny class CustomerMasterKeySpec_SM2 compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class CustomerMasterKeySpec_SM2 extends CustomerMasterKeySpec {
  public CustomerMasterKeySpec_SM2 () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CustomerMasterKeySpec_SM2 o = (CustomerMasterKeySpec_SM2)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 12;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.CustomerMasterKeySpec.SM2");
    return s.toString();
  }
}
