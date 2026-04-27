// Class DefaultCache
// Dafny class DefaultCache compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class DefaultCache {
  public int _entryCapacity;
  public DefaultCache (int entryCapacity) {
    this._entryCapacity = entryCapacity;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DefaultCache o = (DefaultCache)other;
    return true && this._entryCapacity == o._entryCapacity;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.lang.Integer.hashCode(this._entryCapacity);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.DefaultCache.DefaultCache");
    s.append("(");
    s.append(this._entryCapacity);
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DefaultCache> _TYPE = dafny.TypeDescriptor.<DefaultCache>referenceWithInitializer(DefaultCache.class, () -> DefaultCache.Default());
  public static dafny.TypeDescriptor<DefaultCache> _typeDescriptor() {
    return (dafny.TypeDescriptor<DefaultCache>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DefaultCache theDefault = DefaultCache.create(0);
  public static DefaultCache Default() {
    return theDefault;
  }
  public static DefaultCache create(int entryCapacity) {
    return new DefaultCache(entryCapacity);
  }
  public static DefaultCache create_DefaultCache(int entryCapacity) {
    return create(entryCapacity);
  }
  public boolean is_DefaultCache() { return true; }
  public int dtor_entryCapacity() {
    return this._entryCapacity;
  }
}
