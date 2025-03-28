// Class SigningAlgorithmSpec_ECDSA__SHA__256
// Dafny class SigningAlgorithmSpec_ECDSA__SHA__256 compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class SigningAlgorithmSpec_ECDSA__SHA__256 extends SigningAlgorithmSpec {
  public SigningAlgorithmSpec_ECDSA__SHA__256 () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    SigningAlgorithmSpec_ECDSA__SHA__256 o = (SigningAlgorithmSpec_ECDSA__SHA__256)other;
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
    s.append("ComAmazonawsKmsTypes.SigningAlgorithmSpec.ECDSA_SHA_256");
    return s.toString();
  }
}
