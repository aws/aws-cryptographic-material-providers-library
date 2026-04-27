// Class NoCache
// Dafny class NoCache compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class NoCache {
  public NoCache () {
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    NoCache o = (NoCache)other;
    return true;
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.NoCache.NoCache");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<NoCache> _TYPE = dafny.TypeDescriptor.<NoCache>referenceWithInitializer(NoCache.class, () -> NoCache.Default());
  public static dafny.TypeDescriptor<NoCache> _typeDescriptor() {
    return (dafny.TypeDescriptor<NoCache>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final NoCache theDefault = NoCache.create();
  public static NoCache Default() {
    return theDefault;
  }
  public static NoCache create() {
    return new NoCache();
  }
  public static NoCache create_NoCache() {
    return create();
  }
  public boolean is_NoCache() { return true; }
  public static java.util.ArrayList<NoCache> AllSingletonConstructors() {
    java.util.ArrayList<NoCache> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new NoCache());
    return singleton_iterator;
  }
}
