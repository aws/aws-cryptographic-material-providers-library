// Class AlgorithmSpec_RSA__AES__KEY__WRAP__SHA__1
// Dafny class AlgorithmSpec_RSA__AES__KEY__WRAP__SHA__1 compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class AlgorithmSpec_RSA__AES__KEY__WRAP__SHA__1 extends AlgorithmSpec {
  public AlgorithmSpec_RSA__AES__KEY__WRAP__SHA__1 () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    AlgorithmSpec_RSA__AES__KEY__WRAP__SHA__1 o = (AlgorithmSpec_RSA__AES__KEY__WRAP__SHA__1)other;
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
    s.append("ComAmazonawsKmsTypes.AlgorithmSpec.RSA_AES_KEY_WRAP_SHA_1");
    return s.toString();
  }
}
