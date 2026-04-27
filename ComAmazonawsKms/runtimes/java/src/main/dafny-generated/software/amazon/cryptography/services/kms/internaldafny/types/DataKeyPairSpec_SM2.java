// Class DataKeyPairSpec_SM2
// Dafny class DataKeyPairSpec_SM2 compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class DataKeyPairSpec_SM2 extends DataKeyPairSpec {
  public DataKeyPairSpec_SM2 () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DataKeyPairSpec_SM2 o = (DataKeyPairSpec_SM2)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 7;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.DataKeyPairSpec.SM2");
    return s.toString();
  }
}
