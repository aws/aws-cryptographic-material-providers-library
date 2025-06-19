// Class MultiThreadedCache
// Dafny class MultiThreadedCache compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class MultiThreadedCache {
  public int _entryCapacity;
  public Wrappers_Compile.Option<java.lang.Integer> _entryPruningTailSize;
  public MultiThreadedCache (int entryCapacity, Wrappers_Compile.Option<java.lang.Integer> entryPruningTailSize) {
    this._entryCapacity = entryCapacity;
    this._entryPruningTailSize = entryPruningTailSize;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    MultiThreadedCache o = (MultiThreadedCache)other;
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
    s.append("AwsCryptographyMaterialProvidersTypes.MultiThreadedCache.MultiThreadedCache");
    s.append("(");
    s.append(this._entryCapacity);
    s.append(", ");
    s.append(dafny.Helpers.toString(this._entryPruningTailSize));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<MultiThreadedCache> _TYPE = dafny.TypeDescriptor.<MultiThreadedCache>referenceWithInitializer(MultiThreadedCache.class, () -> MultiThreadedCache.Default());
  public static dafny.TypeDescriptor<MultiThreadedCache> _typeDescriptor() {
    return (dafny.TypeDescriptor<MultiThreadedCache>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final MultiThreadedCache theDefault = MultiThreadedCache.create(0, Wrappers_Compile.Option.<java.lang.Integer>Default(CountingNumber._typeDescriptor()));
  public static MultiThreadedCache Default() {
    return theDefault;
  }
  public static MultiThreadedCache create(int entryCapacity, Wrappers_Compile.Option<java.lang.Integer> entryPruningTailSize) {
    return new MultiThreadedCache(entryCapacity, entryPruningTailSize);
  }
  public static MultiThreadedCache create_MultiThreadedCache(int entryCapacity, Wrappers_Compile.Option<java.lang.Integer> entryPruningTailSize) {
    return create(entryCapacity, entryPruningTailSize);
  }
  public boolean is_MultiThreadedCache() { return true; }
  public int dtor_entryCapacity() {
    return this._entryCapacity;
  }
  public Wrappers_Compile.Option<java.lang.Integer> dtor_entryPruningTailSize() {
    return this._entryPruningTailSize;
  }
}
