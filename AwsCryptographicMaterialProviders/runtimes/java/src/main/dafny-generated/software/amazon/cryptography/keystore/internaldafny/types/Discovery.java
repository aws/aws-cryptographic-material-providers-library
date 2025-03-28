// Class Discovery
// Dafny class Discovery compiled into Java
package software.amazon.cryptography.keystore.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class Discovery {
  public Discovery () {
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    Discovery o = (Discovery)other;
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
    s.append("AwsCryptographyKeyStoreTypes.Discovery.Discovery");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<Discovery> _TYPE = dafny.TypeDescriptor.<Discovery>referenceWithInitializer(Discovery.class, () -> Discovery.Default());
  public static dafny.TypeDescriptor<Discovery> _typeDescriptor() {
    return (dafny.TypeDescriptor<Discovery>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final Discovery theDefault = software.amazon.cryptography.keystore.internaldafny.types.Discovery.create();
  public static Discovery Default() {
    return theDefault;
  }
  public static Discovery create() {
    return new Discovery();
  }
  public static Discovery create_Discovery() {
    return create();
  }
  public boolean is_Discovery() { return true; }
  public static java.util.ArrayList<Discovery> AllSingletonConstructors() {
    java.util.ArrayList<Discovery> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new Discovery());
    return singleton_iterator;
  }
}
