// Class DestinationStatus
// Dafny class DestinationStatus compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class DestinationStatus {
  public DestinationStatus() {
  }
  private static final dafny.TypeDescriptor<DestinationStatus> _TYPE = dafny.TypeDescriptor.<DestinationStatus>referenceWithInitializer(DestinationStatus.class, () -> DestinationStatus.Default());
  public static dafny.TypeDescriptor<DestinationStatus> _typeDescriptor() {
    return (dafny.TypeDescriptor<DestinationStatus>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DestinationStatus theDefault = DestinationStatus.create_ENABLING();
  public static DestinationStatus Default() {
    return theDefault;
  }
  public static DestinationStatus create_ENABLING() {
    return new DestinationStatus_ENABLING();
  }
  public static DestinationStatus create_ACTIVE() {
    return new DestinationStatus_ACTIVE();
  }
  public static DestinationStatus create_DISABLING() {
    return new DestinationStatus_DISABLING();
  }
  public static DestinationStatus create_DISABLED() {
    return new DestinationStatus_DISABLED();
  }
  public static DestinationStatus create_ENABLE__FAILED() {
    return new DestinationStatus_ENABLE__FAILED();
  }
  public static DestinationStatus create_UPDATING() {
    return new DestinationStatus_UPDATING();
  }
  public boolean is_ENABLING() { return this instanceof DestinationStatus_ENABLING; }
  public boolean is_ACTIVE() { return this instanceof DestinationStatus_ACTIVE; }
  public boolean is_DISABLING() { return this instanceof DestinationStatus_DISABLING; }
  public boolean is_DISABLED() { return this instanceof DestinationStatus_DISABLED; }
  public boolean is_ENABLE__FAILED() { return this instanceof DestinationStatus_ENABLE__FAILED; }
  public boolean is_UPDATING() { return this instanceof DestinationStatus_UPDATING; }
  public static java.util.ArrayList<DestinationStatus> AllSingletonConstructors() {
    java.util.ArrayList<DestinationStatus> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new DestinationStatus_ENABLING());
    singleton_iterator.add(new DestinationStatus_ACTIVE());
    singleton_iterator.add(new DestinationStatus_DISABLING());
    singleton_iterator.add(new DestinationStatus_DISABLED());
    singleton_iterator.add(new DestinationStatus_ENABLE__FAILED());
    singleton_iterator.add(new DestinationStatus_UPDATING());
    return singleton_iterator;
  }
}
