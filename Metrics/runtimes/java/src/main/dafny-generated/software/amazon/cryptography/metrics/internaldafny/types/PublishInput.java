// Class PublishInput
// Dafny class PublishInput compiled into Java
package software.amazon.cryptography.metrics.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class PublishInput {
  public PublishInput () {
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    PublishInput o = (PublishInput)other;
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
    s.append("AwsCryptographyMetricsTypes.PublishInput.PublishInput");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<PublishInput> _TYPE = dafny.TypeDescriptor.<PublishInput>referenceWithInitializer(PublishInput.class, () -> PublishInput.Default());
  public static dafny.TypeDescriptor<PublishInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<PublishInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final PublishInput theDefault = software.amazon.cryptography.metrics.internaldafny.types.PublishInput.create();
  public static PublishInput Default() {
    return theDefault;
  }
  public static PublishInput create() {
    return new PublishInput();
  }
  public static PublishInput create_PublishInput() {
    return create();
  }
  public boolean is_PublishInput() { return true; }
  public static java.util.ArrayList<PublishInput> AllSingletonConstructors() {
    java.util.ArrayList<PublishInput> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new PublishInput());
    return singleton_iterator;
  }
}
