// Class AlgorithmSpec_SM2PKE
// Dafny class AlgorithmSpec_SM2PKE compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class AlgorithmSpec_SM2PKE extends AlgorithmSpec {
  public AlgorithmSpec_SM2PKE () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    AlgorithmSpec_SM2PKE o = (AlgorithmSpec_SM2PKE)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 5;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.AlgorithmSpec.SM2PKE");
    return s.toString();
  }
}
