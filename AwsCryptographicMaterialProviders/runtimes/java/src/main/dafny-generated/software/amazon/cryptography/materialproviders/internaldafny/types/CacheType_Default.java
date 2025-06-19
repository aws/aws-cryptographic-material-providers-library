// Class CacheType_Default
// Dafny class CacheType_Default compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class CacheType_Default extends CacheType {
  public DefaultCache _Default;
  public CacheType_Default (DefaultCache Default_) {
    super();
    this._Default = Default_;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CacheType_Default o = (CacheType_Default)other;
    return true && java.util.Objects.equals(this._Default, o._Default);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Default);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.CacheType.Default");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Default));
    s.append(")");
    return s.toString();
  }
}
