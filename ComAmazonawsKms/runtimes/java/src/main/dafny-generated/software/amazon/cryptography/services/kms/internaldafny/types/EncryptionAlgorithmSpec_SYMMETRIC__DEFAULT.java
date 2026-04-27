// Class EncryptionAlgorithmSpec_SYMMETRIC__DEFAULT
// Dafny class EncryptionAlgorithmSpec_SYMMETRIC__DEFAULT compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class EncryptionAlgorithmSpec_SYMMETRIC__DEFAULT extends EncryptionAlgorithmSpec {
  public EncryptionAlgorithmSpec_SYMMETRIC__DEFAULT () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    EncryptionAlgorithmSpec_SYMMETRIC__DEFAULT o = (EncryptionAlgorithmSpec_SYMMETRIC__DEFAULT)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.EncryptionAlgorithmSpec.SYMMETRIC_DEFAULT");
    return s.toString();
  }
}
