// Class WrappingKeySpec_RSA__3072
// Dafny class WrappingKeySpec_RSA__3072 compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class WrappingKeySpec_RSA__3072 extends WrappingKeySpec {
  public WrappingKeySpec_RSA__3072 () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    WrappingKeySpec_RSA__3072 o = (WrappingKeySpec_RSA__3072)other;
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
    s.append("ComAmazonawsKmsTypes.WrappingKeySpec.RSA_3072");
    return s.toString();
  }
}
