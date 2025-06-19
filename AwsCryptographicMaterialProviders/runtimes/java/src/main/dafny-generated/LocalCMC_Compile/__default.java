// Class __default
// Dafny class __default compiled into Java
package LocalCMC_Compile;

@SuppressWarnings({"unchecked", "deprecation"})
public class __default {
  public __default() {
  }
  public static <__K, __V> void RemoveValue(dafny.TypeDescriptor<__K> _td___K, dafny.TypeDescriptor<__V> _td___V, __K k0, dafny.DafnyMap<? extends __K, ? extends __V> m)
  {
    dafny.DafnyMap<? extends __K, ? extends __V> _0_m_k;
    _0_m_k = dafny.DafnyMap.<__K, __V>subtract(m, dafny.DafnySet.<__K> of(k0));
  }
  public static Ref<CacheEntry> NULL()
  {
    return Ref.<CacheEntry>create_Null(((dafny.TypeDescriptor<CacheEntry>)(java.lang.Object)dafny.TypeDescriptor.reference(CacheEntry.class)));
  }
  public static int INT32__MAX__VALUE()
  {
    return 2040109465;
  }
  public static long INT64__MAX__VALUE()
  {
    return (long) 8762203435012037017L;
  }
  @Override
  public java.lang.String toString() {
    return "LocalCMC._default";
  }
}
