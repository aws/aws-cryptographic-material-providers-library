// Class PutOutput
// Dafny class PutOutput compiled into Java
package software.amazon.cryptography.metrics.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class PutOutput {
  public PutOutput () {
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    PutOutput o = (PutOutput)other;
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
    s.append("AwsCryptographyMetricsTypes.PutOutput.PutOutput");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<PutOutput> _TYPE = dafny.TypeDescriptor.<PutOutput>referenceWithInitializer(PutOutput.class, () -> PutOutput.Default());
  public static dafny.TypeDescriptor<PutOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<PutOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final PutOutput theDefault = software.amazon.cryptography.metrics.internaldafny.types.PutOutput.create();
  public static PutOutput Default() {
    return theDefault;
  }
  public static PutOutput create() {
    return new PutOutput();
  }
  public static PutOutput create_PutOutput() {
    return create();
  }
  public boolean is_PutOutput() { return true; }
  public static java.util.ArrayList<PutOutput> AllSingletonConstructors() {
    java.util.ArrayList<PutOutput> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new PutOutput());
    return singleton_iterator;
  }
}
