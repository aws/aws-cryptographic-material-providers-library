// Class PublishOutput
// Dafny class PublishOutput compiled into Java
package software.amazon.cryptography.metrics.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class PublishOutput {
  public PublishOutput () {
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    PublishOutput o = (PublishOutput)other;
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
    s.append("AwsCryptographyMetricsTypes.PublishOutput.PublishOutput");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<PublishOutput> _TYPE = dafny.TypeDescriptor.<PublishOutput>referenceWithInitializer(PublishOutput.class, () -> PublishOutput.Default());
  public static dafny.TypeDescriptor<PublishOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<PublishOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final PublishOutput theDefault = software.amazon.cryptography.metrics.internaldafny.types.PublishOutput.create();
  public static PublishOutput Default() {
    return theDefault;
  }
  public static PublishOutput create() {
    return new PublishOutput();
  }
  public static PublishOutput create_PublishOutput() {
    return create();
  }
  public boolean is_PublishOutput() { return true; }
  public static java.util.ArrayList<PublishOutput> AllSingletonConstructors() {
    java.util.ArrayList<PublishOutput> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new PublishOutput());
    return singleton_iterator;
  }
}
