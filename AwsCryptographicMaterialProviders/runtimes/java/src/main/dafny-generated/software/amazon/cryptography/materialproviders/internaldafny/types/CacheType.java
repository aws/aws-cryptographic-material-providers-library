// Class CacheType
// Dafny class CacheType compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class CacheType {
  public CacheType() {
  }
  private static final dafny.TypeDescriptor<CacheType> _TYPE = dafny.TypeDescriptor.<CacheType>referenceWithInitializer(CacheType.class, () -> CacheType.Default());
  public static dafny.TypeDescriptor<CacheType> _typeDescriptor() {
    return (dafny.TypeDescriptor<CacheType>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final CacheType theDefault = CacheType.create_Default(DefaultCache.Default());
  public static CacheType Default() {
    return theDefault;
  }
  public static CacheType create_Default(DefaultCache Default_) {
    return new CacheType_Default(Default_);
  }
  public static CacheType create_No(NoCache No) {
    return new CacheType_No(No);
  }
  public static CacheType create_SingleThreaded(SingleThreadedCache SingleThreaded) {
    return new CacheType_SingleThreaded(SingleThreaded);
  }
  public static CacheType create_MultiThreaded(MultiThreadedCache MultiThreaded) {
    return new CacheType_MultiThreaded(MultiThreaded);
  }
  public static CacheType create_StormTracking(StormTrackingCache StormTracking) {
    return new CacheType_StormTracking(StormTracking);
  }
  public static CacheType create_Shared(ICryptographicMaterialsCache Shared) {
    return new CacheType_Shared(Shared);
  }
  public boolean is_Default() { return this instanceof CacheType_Default; }
  public boolean is_No() { return this instanceof CacheType_No; }
  public boolean is_SingleThreaded() { return this instanceof CacheType_SingleThreaded; }
  public boolean is_MultiThreaded() { return this instanceof CacheType_MultiThreaded; }
  public boolean is_StormTracking() { return this instanceof CacheType_StormTracking; }
  public boolean is_Shared() { return this instanceof CacheType_Shared; }
  public DefaultCache dtor_Default() {
    CacheType d = this;
    return ((CacheType_Default)d)._Default;
  }
  public NoCache dtor_No() {
    CacheType d = this;
    return ((CacheType_No)d)._No;
  }
  public SingleThreadedCache dtor_SingleThreaded() {
    CacheType d = this;
    return ((CacheType_SingleThreaded)d)._SingleThreaded;
  }
  public MultiThreadedCache dtor_MultiThreaded() {
    CacheType d = this;
    return ((CacheType_MultiThreaded)d)._MultiThreaded;
  }
  public StormTrackingCache dtor_StormTracking() {
    CacheType d = this;
    return ((CacheType_StormTracking)d)._StormTracking;
  }
  public ICryptographicMaterialsCache dtor_Shared() {
    CacheType d = this;
    return ((CacheType_Shared)d)._Shared;
  }
}
