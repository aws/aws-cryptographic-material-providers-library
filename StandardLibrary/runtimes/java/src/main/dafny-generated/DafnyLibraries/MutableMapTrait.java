// Interface MutableMapTrait
// Dafny trait MutableMapTrait compiled into Java
package DafnyLibraries;

@SuppressWarnings({"unchecked", "deprecation"})
public interface MutableMapTrait<K, V> {
  public dafny.DafnyMap<? extends K, ? extends V> content();
  public void Put(K k, V v);
  public dafny.DafnySet<? extends K> Keys();
  public boolean HasKey(K k);
  public dafny.DafnySet<? extends V> Values();
  public dafny.DafnySet<? extends dafny.Tuple2<K, V>> Items();
  public V Select(K k);
  public void Remove(K k);
  public java.math.BigInteger Size();
}
