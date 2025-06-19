// Class CacheState
// Dafny class CacheState compiled into Java
package StormTracker_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class CacheState {
  public CacheState() {
  }
  private static final dafny.TypeDescriptor<CacheState> _TYPE = dafny.TypeDescriptor.<CacheState>referenceWithInitializer(CacheState.class, () -> CacheState.Default());
  public static dafny.TypeDescriptor<CacheState> _typeDescriptor() {
    return (dafny.TypeDescriptor<CacheState>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final CacheState theDefault = CacheState.create_EmptyWait();
  public static CacheState Default() {
    return theDefault;
  }
  public static CacheState create_EmptyWait() {
    return new CacheState_EmptyWait();
  }
  public static CacheState create_EmptyFetch() {
    return new CacheState_EmptyFetch();
  }
  public static CacheState create_Full(software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput data) {
    return new CacheState_Full(data);
  }
  public boolean is_EmptyWait() { return this instanceof CacheState_EmptyWait; }
  public boolean is_EmptyFetch() { return this instanceof CacheState_EmptyFetch; }
  public boolean is_Full() { return this instanceof CacheState_Full; }
  public software.amazon.cryptography.materialproviders.internaldafny.types.GetCacheEntryOutput dtor_data() {
    CacheState d = this;
    return ((CacheState_Full)d)._data;
  }
}
