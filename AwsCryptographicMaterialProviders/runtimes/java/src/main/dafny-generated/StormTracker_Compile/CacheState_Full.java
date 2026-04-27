// Class CacheState_Full
// Dafny class CacheState_Full compiled into Java
package StormTracker_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class CacheState_Full extends CacheState {
  public software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput _data;
  public CacheState_Full (software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput data) {
    super();
    this._data = data;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CacheState_Full o = (CacheState_Full)other;
    return true && java.util.Objects.equals(this._data, o._data);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 2;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._data);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("StormTracker.CacheState.Full");
    s.append("(");
    s.append(dafny.Helpers.toString(this._data));
    s.append(")");
    return s.toString();
  }
}
