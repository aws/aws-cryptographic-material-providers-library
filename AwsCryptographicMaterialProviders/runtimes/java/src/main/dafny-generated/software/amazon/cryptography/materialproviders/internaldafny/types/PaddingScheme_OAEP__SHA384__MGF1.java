// Class PaddingScheme_OAEP__SHA384__MGF1
// Dafny class PaddingScheme_OAEP__SHA384__MGF1 compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class PaddingScheme_OAEP__SHA384__MGF1 extends PaddingScheme {
  public PaddingScheme_OAEP__SHA384__MGF1 () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    PaddingScheme_OAEP__SHA384__MGF1 o = (PaddingScheme_OAEP__SHA384__MGF1)other;
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
    s.append("AwsCryptographyMaterialProvidersTypes.PaddingScheme.OAEP_SHA384_MGF1");
    return s.toString();
  }
}
