// Class SingleThreadedCache
// Dafny class SingleThreadedCache compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

import software.amazon.cryptography.keystore.internaldafny.types.*;

@SuppressWarnings({"unchecked", "deprecation"})
public class SingleThreadedCache {
  public int _entryCapacity;
  public Wrappers_Compile.Option<java.lang.Integer> _entryPruningTailSize;
  public SingleThreadedCache (int entryCapacity, Wrappers_Compile.Option<java.lang.Integer> entryPruningTailSize) {
    this._entryCapacity = entryCapacity;
    this._entryPruningTailSize = entryPruningTailSize;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    SingleThreadedCache o = (SingleThreadedCache)other;
    return true && this._entryCapacity == o._entryCapacity && java.util.Objects.equals(this._entryPruningTailSize, o._entryPruningTailSize);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.lang.Integer.hashCode(this._entryCapacity);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._entryPruningTailSize);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.SingleThreadedCache.SingleThreadedCache");
    s.append("(");
    s.append(this._entryCapacity);
    s.append(", ");
    s.append(dafny.Helpers.toString(this._entryPruningTailSize));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<SingleThreadedCache> _TYPE = dafny.TypeDescriptor.<SingleThreadedCache>referenceWithInitializer(SingleThreadedCache.class, () -> SingleThreadedCache.Default());
  public static dafny.TypeDescriptor<SingleThreadedCache> _typeDescriptor() {
    return (dafny.TypeDescriptor<SingleThreadedCache>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final SingleThreadedCache theDefault = software.amazon.cryptography.materialproviders.internaldafny.types.SingleThreadedCache.create(0, Wrappers_Compile.Option.<java.lang.Integer>Default(CountingNumber._typeDescriptor()));
  public static SingleThreadedCache Default() {
    return theDefault;
  }
  public static SingleThreadedCache create(int entryCapacity, Wrappers_Compile.Option<java.lang.Integer> entryPruningTailSize) {
    return new SingleThreadedCache(entryCapacity, entryPruningTailSize);
  }
  public static SingleThreadedCache create_SingleThreadedCache(int entryCapacity, Wrappers_Compile.Option<java.lang.Integer> entryPruningTailSize) {
    return create(entryCapacity, entryPruningTailSize);
  }
  public boolean is_SingleThreadedCache() { return true; }
  public int dtor_entryCapacity() {
    return this._entryCapacity;
  }
  public Wrappers_Compile.Option<java.lang.Integer> dtor_entryPruningTailSize() {
    return this._entryPruningTailSize;
  }
}
