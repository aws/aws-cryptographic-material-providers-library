// Class KeyDescription_Static
// Dafny class KeyDescription_Static compiled into Java
package software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class KeyDescription_Static extends KeyDescription {
  public StaticKeyring _Static;
  public KeyDescription_Static (StaticKeyring Static) {
    super();
    this._Static = Static;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KeyDescription_Static o = (KeyDescription_Static)other;
    return true && java.util.Objects.equals(this._Static, o._Static);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 6;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Static);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.Static");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Static));
    s.append(")");
    return s.toString();
  }
}
