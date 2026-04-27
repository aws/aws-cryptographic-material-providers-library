// Class CacheState_EmptyWait
// Dafny class CacheState_EmptyWait compiled into Java
package StormTracker_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class CacheState_EmptyWait extends CacheState {
  public CacheState_EmptyWait () {
    super();
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CacheState_EmptyWait o = (CacheState_EmptyWait)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("StormTracker.CacheState.EmptyWait");
    return s.toString();
  }
}
