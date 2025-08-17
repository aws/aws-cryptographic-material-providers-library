package DafnyLibraries;

import dafny.DafnyMap;
import dafny.DafnySet;
import dafny.Tuple2;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Map;
import java.util.concurrent.*;

public class MutableMap<K, V> implements DafnyLibraries.MutableMapTrait<K, V> {

  private ConcurrentHashMap<K, V> m;

  // TODO: remove bytesKeys
  public MutableMap(
    dafny.TypeDescriptor<K> _td_K,
    dafny.TypeDescriptor<V> _td_V,
    boolean bytesKeys
  ) {
    m = new ConcurrentHashMap<K, V>();
  }

  public void __ctor(boolean bytesKeys) {}

  @Override
  public DafnyMap<K, V> content() {
    return new DafnyMap<K, V>(m);
  }

  @Override
  public void Put(K k, V v) {
    m.put(k, v);
  }

  @Override
  public DafnySet<? extends K> Keys() {
    return new DafnySet(m.keySet());
  }

  @Override
  public boolean HasKey(K k) {
    return m.containsKey(k);
  }

  @Override
  public DafnySet<? extends V> Values() {
    return new DafnySet(m.values());
  }

  @Override
  public DafnySet<? extends Tuple2<K, V>> Items() {
    ArrayList<Tuple2<K, V>> list = new ArrayList<Tuple2<K, V>>();
    for (Map.Entry<K, V> entry : m.entrySet()) {
      list.add(new Tuple2<K, V>(entry.getKey(), entry.getValue()));
    }
    return new DafnySet<Tuple2<K, V>>(list);
  }

  @Override
  public V Select(K k) {
    return m.get(k);
  }

  @Override
  public void Remove(K k) {
    m.remove(k);
  }

  @Override
  public BigInteger Size() {
    return BigInteger.valueOf(m.size());
  }
}
