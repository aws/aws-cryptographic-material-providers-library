// Class CacheState_EmptyFetch
// Dafny class CacheState_EmptyFetch compiled into Java
package StormTracker_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class CacheState_EmptyFetch extends CacheState {
  public CacheState_EmptyFetch () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CacheState_EmptyFetch o = (CacheState_EmptyFetch)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 1;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("StormTracker.CacheState.EmptyFetch");
    return s.toString();
  }
}
