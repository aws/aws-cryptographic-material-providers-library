// Class DataKeyPairSpec_RSA__3072
// Dafny class DataKeyPairSpec_RSA__3072 compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class DataKeyPairSpec_RSA__3072 extends DataKeyPairSpec {
  public DataKeyPairSpec_RSA__3072 () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DataKeyPairSpec_RSA__3072 o = (DataKeyPairSpec_RSA__3072)other;
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
    s.append("ComAmazonawsKmsTypes.DataKeyPairSpec.RSA_3072");
    return s.toString();
  }
}
