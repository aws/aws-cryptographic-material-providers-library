// Class RSAPaddingMode_OAEP__SHA1
// Dafny class RSAPaddingMode_OAEP__SHA1 compiled into Java
package software.amazon.cryptography.primitives.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class RSAPaddingMode_OAEP__SHA1 extends RSAPaddingMode {
  public RSAPaddingMode_OAEP__SHA1 () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    RSAPaddingMode_OAEP__SHA1 o = (RSAPaddingMode_OAEP__SHA1)other;
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
    s.append("AwsCryptographyPrimitivesTypes.RSAPaddingMode.OAEP_SHA1");
    return s.toString();
  }
}
