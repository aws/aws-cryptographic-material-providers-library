// Class ApproximateCreationDateTimePrecision
// Dafny class ApproximateCreationDateTimePrecision compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public abstract class ApproximateCreationDateTimePrecision {
  public ApproximateCreationDateTimePrecision() {
  }
  private static final dafny.TypeDescriptor<ApproximateCreationDateTimePrecision> _TYPE = dafny.TypeDescriptor.<ApproximateCreationDateTimePrecision>referenceWithInitializer(ApproximateCreationDateTimePrecision.class, () -> ApproximateCreationDateTimePrecision.Default());
  public static dafny.TypeDescriptor<ApproximateCreationDateTimePrecision> _typeDescriptor() {
    return (dafny.TypeDescriptor<ApproximateCreationDateTimePrecision>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ApproximateCreationDateTimePrecision theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.ApproximateCreationDateTimePrecision.create_MILLISECOND();
  public static ApproximateCreationDateTimePrecision Default() {
    return theDefault;
  }
  public static ApproximateCreationDateTimePrecision create_MILLISECOND() {
    return new ApproximateCreationDateTimePrecision_MILLISECOND();
  }
  public static ApproximateCreationDateTimePrecision create_MICROSECOND() {
    return new ApproximateCreationDateTimePrecision_MICROSECOND();
  }
  public boolean is_MILLISECOND() { return this instanceof ApproximateCreationDateTimePrecision_MILLISECOND; }
  public boolean is_MICROSECOND() { return this instanceof ApproximateCreationDateTimePrecision_MICROSECOND; }
  public static java.util.ArrayList<ApproximateCreationDateTimePrecision> AllSingletonConstructors() {
    java.util.ArrayList<ApproximateCreationDateTimePrecision> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new ApproximateCreationDateTimePrecision_MILLISECOND());
    singleton_iterator.add(new ApproximateCreationDateTimePrecision_MICROSECOND());
    return singleton_iterator;
  }
}
