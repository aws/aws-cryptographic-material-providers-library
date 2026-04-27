// Class KeyDescription_Multi
// Dafny class KeyDescription_Multi compiled into Java
package software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class KeyDescription_Multi extends KeyDescription {
  public MultiKeyring _Multi;
  public KeyDescription_Multi (MultiKeyring Multi) {
    super();
    this._Multi = Multi;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KeyDescription_Multi o = (KeyDescription_Multi)other;
    return true && java.util.Objects.equals(this._Multi, o._Multi);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 10;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Multi);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.Multi");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Multi));
    s.append(")");
    return s.toString();
  }
}
