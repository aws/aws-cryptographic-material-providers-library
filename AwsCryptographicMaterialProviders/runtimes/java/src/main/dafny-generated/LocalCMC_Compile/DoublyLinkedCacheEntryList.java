// Class DoublyLinkedCacheEntryList
// Dafny class DoublyLinkedCacheEntryList compiled into Java
package LocalCMC_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class DoublyLinkedCacheEntryList {
  public DoublyLinkedCacheEntryList() {
    this.head = Ref.<CacheEntry>Default(((dafny.TypeDescriptor<CacheEntry>)(java.lang.Object)dafny.TypeDescriptor.reference(CacheEntry.class)));
    this.tail = Ref.<CacheEntry>Default(((dafny.TypeDescriptor<CacheEntry>)(java.lang.Object)dafny.TypeDescriptor.reference(CacheEntry.class)));
  }
  public void __ctor()
  {
    (this).head = Ref.<CacheEntry>create_Null(((dafny.TypeDescriptor<CacheEntry>)(java.lang.Object)dafny.TypeDescriptor.reference(CacheEntry.class)));
    (this).tail = Ref.<CacheEntry>create_Null(((dafny.TypeDescriptor<CacheEntry>)(java.lang.Object)dafny.TypeDescriptor.reference(CacheEntry.class)));
  }
  public Ref<CacheEntry> head;
  public Ref<CacheEntry> tail;
  public void pushCell(CacheEntry toPush)
  {
    Ref<CacheEntry> _0_cRef;
    _0_cRef = Ref.<CacheEntry>create_Ptr(((dafny.TypeDescriptor<CacheEntry>)(java.lang.Object)dafny.TypeDescriptor.reference(CacheEntry.class)), toPush);
    if ((this.head).is_Ptr()) {
      CacheEntry _obj0 = (this.head).dtor_deref();
      _obj0.prev = _0_cRef;
      (toPush).next = this.head;
      (this).head = _0_cRef;
    } else {
      (this).head = _0_cRef;
      (this).tail = this.head;
    }
  }
  public void moveToFront(CacheEntry c)
  {
    if (((this.head).dtor_deref()) != (Object)  (c)) {
      Ref<CacheEntry> _0_toPush;
      _0_toPush = Ref.<CacheEntry>create_Ptr(((dafny.TypeDescriptor<CacheEntry>)(java.lang.Object)dafny.TypeDescriptor.reference(CacheEntry.class)), c);
      (this).remove(c);
      if ((this.head).is_Ptr()) {
        CacheEntry _obj0 = (this.head).dtor_deref();
        _obj0.prev = _0_toPush;
        CacheEntry _obj1 = (_0_toPush).dtor_deref();
        _obj1.next = this.head;
        (this).head = _0_toPush;
      } else {
        (this).head = _0_toPush;
        (this).tail = this.head;
      }
    }
  }
  public void remove(CacheEntry toRemove)
  {
    if ((toRemove.prev).is_Null()) {
      (this).head = toRemove.next;
    } else {
      CacheEntry _obj0 = (toRemove.prev).dtor_deref();
      _obj0.next = toRemove.next;
    }
    if ((toRemove.next).is_Null()) {
      (this).tail = toRemove.prev;
    } else {
      CacheEntry _obj1 = (toRemove.next).dtor_deref();
      _obj1.prev = toRemove.prev;
    }
    goto_0: {
    }
    (toRemove).next = __default.NULL();
    (toRemove).prev = __default.NULL();
  }
  private static final dafny.TypeDescriptor<DoublyLinkedCacheEntryList> _TYPE = dafny.TypeDescriptor.<DoublyLinkedCacheEntryList>referenceWithInitializer(DoublyLinkedCacheEntryList.class, () -> (DoublyLinkedCacheEntryList) null);
  public static dafny.TypeDescriptor<DoublyLinkedCacheEntryList> _typeDescriptor() {
    return (dafny.TypeDescriptor<DoublyLinkedCacheEntryList>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "LocalCMC.DoublyLinkedCacheEntryList";
  }
}
