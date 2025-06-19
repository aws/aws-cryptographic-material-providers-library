// Class MacAlgorithmSpec_HMAC__SHA__512
// Dafny class MacAlgorithmSpec_HMAC__SHA__512 compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class MacAlgorithmSpec_HMAC__SHA__512 extends MacAlgorithmSpec {
  public MacAlgorithmSpec_HMAC__SHA__512 () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    MacAlgorithmSpec_HMAC__SHA__512 o = (MacAlgorithmSpec_HMAC__SHA__512)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 3;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.MacAlgorithmSpec.HMAC_SHA_512");
    return s.toString();
  }
}
