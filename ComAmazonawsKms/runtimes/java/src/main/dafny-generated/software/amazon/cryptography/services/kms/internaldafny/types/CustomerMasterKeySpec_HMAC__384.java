// Class CustomerMasterKeySpec_HMAC__384
// Dafny class CustomerMasterKeySpec_HMAC__384 compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class CustomerMasterKeySpec_HMAC__384 extends CustomerMasterKeySpec {
  public CustomerMasterKeySpec_HMAC__384 () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CustomerMasterKeySpec_HMAC__384 o = (CustomerMasterKeySpec_HMAC__384)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 10;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.CustomerMasterKeySpec.HMAC_384");
    return s.toString();
  }
}
