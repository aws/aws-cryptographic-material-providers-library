// Class RSAPaddingMode_OAEP__SHA256
// Dafny class RSAPaddingMode_OAEP__SHA256 compiled into Java
package software.amazon.cryptography.primitives.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class RSAPaddingMode_OAEP__SHA256 extends RSAPaddingMode {
  public RSAPaddingMode_OAEP__SHA256 () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    RSAPaddingMode_OAEP__SHA256 o = (RSAPaddingMode_OAEP__SHA256)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 2;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyPrimitivesTypes.RSAPaddingMode.OAEP_SHA256");
    return s.toString();
  }
}
