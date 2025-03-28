// Class CacheType_SingleThreaded
// Dafny class CacheType_SingleThreaded compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class CacheType_SingleThreaded extends CacheType {
  public SingleThreadedCache _SingleThreaded;
  public CacheType_SingleThreaded (SingleThreadedCache SingleThreaded) {
    super();
    this._SingleThreaded = SingleThreaded;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CacheType_SingleThreaded o = (CacheType_SingleThreaded)other;
    return true && java.util.Objects.equals(this._SingleThreaded, o._SingleThreaded);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 2;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._SingleThreaded);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.CacheType.SingleThreaded");
    s.append("(");
    s.append(dafny.Helpers.toString(this._SingleThreaded));
    s.append(")");
    return s.toString();
  }
}
