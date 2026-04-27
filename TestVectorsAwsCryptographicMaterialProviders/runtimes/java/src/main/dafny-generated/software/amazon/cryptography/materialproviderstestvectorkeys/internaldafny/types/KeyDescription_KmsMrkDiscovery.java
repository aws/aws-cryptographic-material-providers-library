// Class KeyDescription_KmsMrkDiscovery
// Dafny class KeyDescription_KmsMrkDiscovery compiled into Java
package software.amazon.cryptography.materialproviderstestvectorkeys.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class KeyDescription_KmsMrkDiscovery extends KeyDescription {
  public KmsMrkAwareDiscovery _KmsMrkDiscovery;
  public KeyDescription_KmsMrkDiscovery (KmsMrkAwareDiscovery KmsMrkDiscovery) {
    super();
    this._KmsMrkDiscovery = KmsMrkDiscovery;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KeyDescription_KmsMrkDiscovery o = (KeyDescription_KmsMrkDiscovery)other;
    return true && java.util.Objects.equals(this._KmsMrkDiscovery, o._KmsMrkDiscovery);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 2;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KmsMrkDiscovery);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTestVectorKeysTypes.KeyDescription.KmsMrkDiscovery");
    s.append("(");
    s.append(dafny.Helpers.toString(this._KmsMrkDiscovery));
    s.append(")");
    return s.toString();
  }
}
