// Class SigningAlgorithmSpec_SM2DSA
// Dafny class SigningAlgorithmSpec_SM2DSA compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class SigningAlgorithmSpec_SM2DSA extends SigningAlgorithmSpec {
  public SigningAlgorithmSpec_SM2DSA () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    SigningAlgorithmSpec_SM2DSA o = (SigningAlgorithmSpec_SM2DSA)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 9;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.SigningAlgorithmSpec.SM2DSA");
    return s.toString();
  }
}
