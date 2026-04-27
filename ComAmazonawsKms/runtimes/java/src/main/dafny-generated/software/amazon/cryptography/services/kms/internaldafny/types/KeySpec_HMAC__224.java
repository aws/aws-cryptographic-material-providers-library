// Class KeySpec_HMAC__224
// Dafny class KeySpec_HMAC__224 compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class KeySpec_HMAC__224 extends KeySpec {
  public KeySpec_HMAC__224 () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KeySpec_HMAC__224 o = (KeySpec_HMAC__224)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 8;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.KeySpec.HMAC_224");
    return s.toString();
  }
}
