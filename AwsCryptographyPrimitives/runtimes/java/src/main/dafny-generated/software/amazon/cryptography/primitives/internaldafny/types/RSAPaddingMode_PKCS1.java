// Class RSAPaddingMode_PKCS1
// Dafny class RSAPaddingMode_PKCS1 compiled into Java
package software.amazon.cryptography.primitives.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class RSAPaddingMode_PKCS1 extends RSAPaddingMode {
  public RSAPaddingMode_PKCS1 () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    RSAPaddingMode_PKCS1 o = (RSAPaddingMode_PKCS1)other;
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
    s.append("AwsCryptographyPrimitivesTypes.RSAPaddingMode.PKCS1");
    return s.toString();
  }
}
