// Class IDENTITY
// Dafny class IDENTITY compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class IDENTITY {
  public IDENTITY () {
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    IDENTITY o = (IDENTITY)other;
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
    s.append("AwsCryptographyMaterialProvidersTypes.IDENTITY.IDENTITY");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<IDENTITY> _TYPE = dafny.TypeDescriptor.<IDENTITY>referenceWithInitializer(IDENTITY.class, () -> IDENTITY.Default());
  public static dafny.TypeDescriptor<IDENTITY> _typeDescriptor() {
    return (dafny.TypeDescriptor<IDENTITY>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final IDENTITY theDefault = IDENTITY.create();
  public static IDENTITY Default() {
    return theDefault;
  }
  public static IDENTITY create() {
    return new IDENTITY();
  }
  public static IDENTITY create_IDENTITY() {
    return create();
  }
  public boolean is_IDENTITY() { return true; }
  public static java.util.ArrayList<IDENTITY> AllSingletonConstructors() {
    java.util.ArrayList<IDENTITY> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new IDENTITY());
    return singleton_iterator;
  }
}
