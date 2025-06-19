// Class CacheType_Shared
// Dafny class CacheType_Shared compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class CacheType_Shared extends CacheType {
  public ICryptographicMaterialsCache _Shared;
  public CacheType_Shared (ICryptographicMaterialsCache Shared) {
    super();
    this._Shared = Shared;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CacheType_Shared o = (CacheType_Shared)other;
    return true && this._Shared == o._Shared;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 5;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Shared);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.CacheType.Shared");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Shared));
    s.append(")");
    return s.toString();
  }
}
