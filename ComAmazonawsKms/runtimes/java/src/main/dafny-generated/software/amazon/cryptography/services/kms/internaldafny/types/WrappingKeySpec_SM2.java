// Class WrappingKeySpec_SM2
// Dafny class WrappingKeySpec_SM2 compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class WrappingKeySpec_SM2 extends WrappingKeySpec {
  public WrappingKeySpec_SM2 () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    WrappingKeySpec_SM2 o = (WrappingKeySpec_SM2)other;
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
    s.append("ComAmazonawsKmsTypes.WrappingKeySpec.SM2");
    return s.toString();
  }
}
