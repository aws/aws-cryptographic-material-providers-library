// Class PointInTimeRecoveryStatus
// Dafny class PointInTimeRecoveryStatus compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class PointInTimeRecoveryStatus {
  public PointInTimeRecoveryStatus() {
  }
  private static final dafny.TypeDescriptor<PointInTimeRecoveryStatus> _TYPE = dafny.TypeDescriptor.<PointInTimeRecoveryStatus>referenceWithInitializer(PointInTimeRecoveryStatus.class, () -> PointInTimeRecoveryStatus.Default());
  public static dafny.TypeDescriptor<PointInTimeRecoveryStatus> _typeDescriptor() {
    return (dafny.TypeDescriptor<PointInTimeRecoveryStatus>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final PointInTimeRecoveryStatus theDefault = PointInTimeRecoveryStatus.create_ENABLED();
  public static PointInTimeRecoveryStatus Default() {
    return theDefault;
  }
  public static PointInTimeRecoveryStatus create_ENABLED() {
    return new PointInTimeRecoveryStatus_ENABLED();
  }
  public static PointInTimeRecoveryStatus create_DISABLED() {
    return new PointInTimeRecoveryStatus_DISABLED();
  }
  public boolean is_ENABLED() { return this instanceof PointInTimeRecoveryStatus_ENABLED; }
  public boolean is_DISABLED() { return this instanceof PointInTimeRecoveryStatus_DISABLED; }
  public static java.util.ArrayList<PointInTimeRecoveryStatus> AllSingletonConstructors() {
    java.util.ArrayList<PointInTimeRecoveryStatus> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new PointInTimeRecoveryStatus_ENABLED());
    singleton_iterator.add(new PointInTimeRecoveryStatus_DISABLED());
    return singleton_iterator;
  }
}
