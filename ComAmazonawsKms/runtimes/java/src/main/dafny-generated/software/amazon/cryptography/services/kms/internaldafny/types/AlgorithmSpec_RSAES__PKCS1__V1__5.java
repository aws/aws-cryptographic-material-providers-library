// Class AlgorithmSpec_RSAES__PKCS1__V1__5
// Dafny class AlgorithmSpec_RSAES__PKCS1__V1__5 compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class AlgorithmSpec_RSAES__PKCS1__V1__5 extends AlgorithmSpec {
  public AlgorithmSpec_RSAES__PKCS1__V1__5 () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    AlgorithmSpec_RSAES__PKCS1__V1__5 o = (AlgorithmSpec_RSAES__PKCS1__V1__5)other;
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
    s.append("ComAmazonawsKmsTypes.AlgorithmSpec.RSAES_PKCS1_V1_5");
    return s.toString();
  }
}
