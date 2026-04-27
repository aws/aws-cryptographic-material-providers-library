// Class MacAlgorithmSpec_HMAC__SHA__384
// Dafny class MacAlgorithmSpec_HMAC__SHA__384 compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class MacAlgorithmSpec_HMAC__SHA__384 extends MacAlgorithmSpec {
  public MacAlgorithmSpec_HMAC__SHA__384 () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    MacAlgorithmSpec_HMAC__SHA__384 o = (MacAlgorithmSpec_HMAC__SHA__384)other;
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
    s.append("ComAmazonawsKmsTypes.MacAlgorithmSpec.HMAC_SHA_384");
    return s.toString();
  }
}
