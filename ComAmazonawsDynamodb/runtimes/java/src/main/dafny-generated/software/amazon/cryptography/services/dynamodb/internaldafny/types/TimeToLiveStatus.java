// Class TimeToLiveStatus
// Dafny class TimeToLiveStatus compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public abstract class TimeToLiveStatus {
  public TimeToLiveStatus() {
  }
  private static final dafny.TypeDescriptor<TimeToLiveStatus> _TYPE = dafny.TypeDescriptor.<TimeToLiveStatus>referenceWithInitializer(TimeToLiveStatus.class, () -> TimeToLiveStatus.Default());
  public static dafny.TypeDescriptor<TimeToLiveStatus> _typeDescriptor() {
    return (dafny.TypeDescriptor<TimeToLiveStatus>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final TimeToLiveStatus theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.TimeToLiveStatus.create_ENABLING();
  public static TimeToLiveStatus Default() {
    return theDefault;
  }
  public static TimeToLiveStatus create_ENABLING() {
    return new TimeToLiveStatus_ENABLING();
  }
  public static TimeToLiveStatus create_DISABLING() {
    return new TimeToLiveStatus_DISABLING();
  }
  public static TimeToLiveStatus create_ENABLED() {
    return new TimeToLiveStatus_ENABLED();
  }
  public static TimeToLiveStatus create_DISABLED() {
    return new TimeToLiveStatus_DISABLED();
  }
  public boolean is_ENABLING() { return this instanceof TimeToLiveStatus_ENABLING; }
  public boolean is_DISABLING() { return this instanceof TimeToLiveStatus_DISABLING; }
  public boolean is_ENABLED() { return this instanceof TimeToLiveStatus_ENABLED; }
  public boolean is_DISABLED() { return this instanceof TimeToLiveStatus_DISABLED; }
  public static java.util.ArrayList<TimeToLiveStatus> AllSingletonConstructors() {
    java.util.ArrayList<TimeToLiveStatus> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new TimeToLiveStatus_ENABLING());
    singleton_iterator.add(new TimeToLiveStatus_DISABLING());
    singleton_iterator.add(new TimeToLiveStatus_ENABLED());
    singleton_iterator.add(new TimeToLiveStatus_DISABLED());
    return singleton_iterator;
  }
}
