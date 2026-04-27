// Class KeyDescription_KmsMrk
// Dafny class KeyDescription_KmsMrk compiled into Java
package software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class KeyDescription_KmsMrk extends KeyDescription {
  public KmsMrkAware _KmsMrk;
  public KeyDescription_KmsMrk (KmsMrkAware KmsMrk) {
    super();
    this._KmsMrk = KmsMrk;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KeyDescription_KmsMrk o = (KeyDescription_KmsMrk)other;
    return true && java.util.Objects.equals(this._KmsMrk, o._KmsMrk);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 1;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KmsMrk);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.KmsMrk");
    s.append("(");
    s.append(dafny.Helpers.toString(this._KmsMrk));
    s.append(")");
    return s.toString();
  }
}
