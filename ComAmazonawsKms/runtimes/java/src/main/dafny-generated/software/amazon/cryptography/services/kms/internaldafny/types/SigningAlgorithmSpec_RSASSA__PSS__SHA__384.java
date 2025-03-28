// Class SigningAlgorithmSpec_RSASSA__PSS__SHA__384
// Dafny class SigningAlgorithmSpec_RSASSA__PSS__SHA__384 compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class SigningAlgorithmSpec_RSASSA__PSS__SHA__384 extends SigningAlgorithmSpec {
  public SigningAlgorithmSpec_RSASSA__PSS__SHA__384 () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    SigningAlgorithmSpec_RSASSA__PSS__SHA__384 o = (SigningAlgorithmSpec_RSASSA__PSS__SHA__384)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 1;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.SigningAlgorithmSpec.RSASSA_PSS_SHA_384");
    return s.toString();
  }
}
