// Class KeyDescription_Hierarchy
// Dafny class KeyDescription_Hierarchy compiled into Java
package software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class KeyDescription_Hierarchy extends KeyDescription {
  public HierarchyKeyring _Hierarchy;
  public KeyDescription_Hierarchy (HierarchyKeyring Hierarchy) {
    super();
    this._Hierarchy = Hierarchy;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KeyDescription_Hierarchy o = (KeyDescription_Hierarchy)other;
    return true && java.util.Objects.equals(this._Hierarchy, o._Hierarchy);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 9;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Hierarchy);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.Hierarchy");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Hierarchy));
    s.append(")");
    return s.toString();
  }
}
