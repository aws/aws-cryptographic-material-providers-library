// Class ContinuousBackupsStatus
// Dafny class ContinuousBackupsStatus compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class ContinuousBackupsStatus {
  public ContinuousBackupsStatus() {
  }
  private static final dafny.TypeDescriptor<ContinuousBackupsStatus> _TYPE = dafny.TypeDescriptor.<ContinuousBackupsStatus>referenceWithInitializer(ContinuousBackupsStatus.class, () -> ContinuousBackupsStatus.Default());
  public static dafny.TypeDescriptor<ContinuousBackupsStatus> _typeDescriptor() {
    return (dafny.TypeDescriptor<ContinuousBackupsStatus>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ContinuousBackupsStatus theDefault = ContinuousBackupsStatus.create_ENABLED();
  public static ContinuousBackupsStatus Default() {
    return theDefault;
  }
  public static ContinuousBackupsStatus create_ENABLED() {
    return new ContinuousBackupsStatus_ENABLED();
  }
  public static ContinuousBackupsStatus create_DISABLED() {
    return new ContinuousBackupsStatus_DISABLED();
  }
  public boolean is_ENABLED() { return this instanceof ContinuousBackupsStatus_ENABLED; }
  public boolean is_DISABLED() { return this instanceof ContinuousBackupsStatus_DISABLED; }
  public static java.util.ArrayList<ContinuousBackupsStatus> AllSingletonConstructors() {
    java.util.ArrayList<ContinuousBackupsStatus> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new ContinuousBackupsStatus_ENABLED());
    singleton_iterator.add(new ContinuousBackupsStatus_DISABLED());
    return singleton_iterator;
  }
}
