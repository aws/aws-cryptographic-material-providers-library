// Class CustomerMasterKeySpec_HMAC__512
// Dafny class CustomerMasterKeySpec_HMAC__512 compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class CustomerMasterKeySpec_HMAC__512 extends CustomerMasterKeySpec {
  public CustomerMasterKeySpec_HMAC__512 () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CustomerMasterKeySpec_HMAC__512 o = (CustomerMasterKeySpec_HMAC__512)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 11;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.CustomerMasterKeySpec.HMAC_512");
    return s.toString();
  }
}
