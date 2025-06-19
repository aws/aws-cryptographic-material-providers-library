// Class DIRECT__KEY__WRAPPING
// Dafny class DIRECT__KEY__WRAPPING compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class DIRECT__KEY__WRAPPING {
  public DIRECT__KEY__WRAPPING () {
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DIRECT__KEY__WRAPPING o = (DIRECT__KEY__WRAPPING)other;
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
    s.append("AwsCryptographyMaterialProvidersTypes.DIRECT_KEY_WRAPPING.DIRECT_KEY_WRAPPING");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DIRECT__KEY__WRAPPING> _TYPE = dafny.TypeDescriptor.<DIRECT__KEY__WRAPPING>referenceWithInitializer(DIRECT__KEY__WRAPPING.class, () -> DIRECT__KEY__WRAPPING.Default());
  public static dafny.TypeDescriptor<DIRECT__KEY__WRAPPING> _typeDescriptor() {
    return (dafny.TypeDescriptor<DIRECT__KEY__WRAPPING>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DIRECT__KEY__WRAPPING theDefault = DIRECT__KEY__WRAPPING.create();
  public static DIRECT__KEY__WRAPPING Default() {
    return theDefault;
  }
  public static DIRECT__KEY__WRAPPING create() {
    return new DIRECT__KEY__WRAPPING();
  }
  public static DIRECT__KEY__WRAPPING create_DIRECT__KEY__WRAPPING() {
    return create();
  }
  public boolean is_DIRECT__KEY__WRAPPING() { return true; }
  public static java.util.ArrayList<DIRECT__KEY__WRAPPING> AllSingletonConstructors() {
    java.util.ArrayList<DIRECT__KEY__WRAPPING> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new DIRECT__KEY__WRAPPING());
    return singleton_iterator;
  }
}
