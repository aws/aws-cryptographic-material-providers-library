// Class VersionKeyOutput
// Dafny class VersionKeyOutput compiled into Java
package software.amazon.cryptography.keystore.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class VersionKeyOutput {
  public VersionKeyOutput () {
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    VersionKeyOutput o = (VersionKeyOutput)other;
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
    s.append("AwsCryptographyKeyStoreTypes.VersionKeyOutput.VersionKeyOutput");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<VersionKeyOutput> _TYPE = dafny.TypeDescriptor.<VersionKeyOutput>referenceWithInitializer(VersionKeyOutput.class, () -> VersionKeyOutput.Default());
  public static dafny.TypeDescriptor<VersionKeyOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<VersionKeyOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final VersionKeyOutput theDefault = software.amazon.cryptography.keystore.internaldafny.types.VersionKeyOutput.create();
  public static VersionKeyOutput Default() {
    return theDefault;
  }
  public static VersionKeyOutput create() {
    return new VersionKeyOutput();
  }
  public static VersionKeyOutput create_VersionKeyOutput() {
    return create();
  }
  public boolean is_VersionKeyOutput() { return true; }
  public static java.util.ArrayList<VersionKeyOutput> AllSingletonConstructors() {
    java.util.ArrayList<VersionKeyOutput> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new VersionKeyOutput());
    return singleton_iterator;
  }
}
