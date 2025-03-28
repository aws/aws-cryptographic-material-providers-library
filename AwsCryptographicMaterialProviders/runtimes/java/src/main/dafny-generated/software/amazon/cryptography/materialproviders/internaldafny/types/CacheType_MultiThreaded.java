// Class CacheType_MultiThreaded
// Dafny class CacheType_MultiThreaded compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class CacheType_MultiThreaded extends CacheType {
  public MultiThreadedCache _MultiThreaded;
  public CacheType_MultiThreaded (MultiThreadedCache MultiThreaded) {
    super();
    this._MultiThreaded = MultiThreaded;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CacheType_MultiThreaded o = (CacheType_MultiThreaded)other;
    return true && java.util.Objects.equals(this._MultiThreaded, o._MultiThreaded);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 3;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._MultiThreaded);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.CacheType.MultiThreaded");
    s.append("(");
    s.append(dafny.Helpers.toString(this._MultiThreaded));
    s.append(")");
    return s.toString();
  }
}
