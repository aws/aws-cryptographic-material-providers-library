// Class DescribeLimitsInput
// Dafny class DescribeLimitsInput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class DescribeLimitsInput {
  public DescribeLimitsInput () {
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DescribeLimitsInput o = (DescribeLimitsInput)other;
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
    s.append("ComAmazonawsDynamodbTypes.DescribeLimitsInput.DescribeLimitsInput");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DescribeLimitsInput> _TYPE = dafny.TypeDescriptor.<DescribeLimitsInput>referenceWithInitializer(DescribeLimitsInput.class, () -> DescribeLimitsInput.Default());
  public static dafny.TypeDescriptor<DescribeLimitsInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<DescribeLimitsInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DescribeLimitsInput theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.DescribeLimitsInput.create();
  public static DescribeLimitsInput Default() {
    return theDefault;
  }
  public static DescribeLimitsInput create() {
    return new DescribeLimitsInput();
  }
  public static DescribeLimitsInput create_DescribeLimitsInput() {
    return create();
  }
  public boolean is_DescribeLimitsInput() { return true; }
  public static java.util.ArrayList<DescribeLimitsInput> AllSingletonConstructors() {
    java.util.ArrayList<DescribeLimitsInput> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new DescribeLimitsInput());
    return singleton_iterator;
  }
}
