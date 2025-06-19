// Class CacheEntry
// Dafny class CacheEntry compiled into Java
package LocalCMC_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class CacheEntry {
  public CacheEntry() {
    this.prev = Ref.<CacheEntry>Default(((dafny.TypeDescriptor<CacheEntry>)(java.lang.Object)dafny.TypeDescriptor.reference(CacheEntry.class)));
    this.next = Ref.<CacheEntry>Default(((dafny.TypeDescriptor<CacheEntry>)(java.lang.Object)dafny.TypeDescriptor.reference(CacheEntry.class)));
    this.messagesUsed = 0;
    this.bytesUsed = 0;
    this._identifier = dafny.DafnySequence.<java.lang.Byte> empty(BoundedInts_Compile.uint8._typeDescriptor());
    this._materials = (software.amazon.cryptography.materialproviders.internaldafny.types.Materials)null;
    this._creationTime = 0L;
    this._expiryTime = 0L;
  }
  public Ref<CacheEntry> prev;
  public Ref<CacheEntry> next;
  public int messagesUsed;
  public int bytesUsed;
  public void __ctor(software.amazon.cryptography.materialproviders.internaldafny.types.Materials materials_k, dafny.DafnySequence<? extends java.lang.Byte> identifier_k, long creationTime_k, long expiryTime_k, int messagesUsed_k, int bytesUsed_k)
  {
    (this)._materials = materials_k;
    (this)._identifier = identifier_k;
    (this)._creationTime = creationTime_k;
    (this)._expiryTime = expiryTime_k;
    (this).messagesUsed = messagesUsed_k;
    (this).bytesUsed = bytesUsed_k;
    (this).prev = __default.NULL();
    (this).next = __default.NULL();
  }
  public dafny.DafnySequence<? extends java.lang.Byte> _identifier;
  public dafny.DafnySequence<? extends java.lang.Byte> identifier()
  {
    return this._identifier;
  }
  public software.amazon.cryptography.materialproviders.internaldafny.types.Materials _materials;
  public software.amazon.cryptography.materialproviders.internaldafny.types.Materials materials()
  {
    return this._materials;
  }
  public long _creationTime;
  public long creationTime()
  {
    return this._creationTime;
  }
  public long _expiryTime;
  public long expiryTime()
  {
    return this._expiryTime;
  }
  private static final dafny.TypeDescriptor<CacheEntry> _TYPE = dafny.TypeDescriptor.<CacheEntry>referenceWithInitializer(CacheEntry.class, () -> (CacheEntry) null);
  public static dafny.TypeDescriptor<CacheEntry> _typeDescriptor() {
    return (dafny.TypeDescriptor<CacheEntry>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "LocalCMC.CacheEntry";
  }
}
