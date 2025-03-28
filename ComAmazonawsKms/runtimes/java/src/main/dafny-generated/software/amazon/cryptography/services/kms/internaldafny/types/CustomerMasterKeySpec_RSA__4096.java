// Class CustomerMasterKeySpec_RSA__4096
// Dafny class CustomerMasterKeySpec_RSA__4096 compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class CustomerMasterKeySpec_RSA__4096 extends CustomerMasterKeySpec {
  public CustomerMasterKeySpec_RSA__4096 () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CustomerMasterKeySpec_RSA__4096 o = (CustomerMasterKeySpec_RSA__4096)other;
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
    s.append("ComAmazonawsKmsTypes.CustomerMasterKeySpec.RSA_4096");
    return s.toString();
  }
}
