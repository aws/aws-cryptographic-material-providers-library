// Class SSEStatus
// Dafny class SSEStatus compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class SSEStatus {
  public SSEStatus() {
  }
  private static final dafny.TypeDescriptor<SSEStatus> _TYPE = dafny.TypeDescriptor.<SSEStatus>referenceWithInitializer(SSEStatus.class, () -> SSEStatus.Default());
  public static dafny.TypeDescriptor<SSEStatus> _typeDescriptor() {
    return (dafny.TypeDescriptor<SSEStatus>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final SSEStatus theDefault = SSEStatus.create_ENABLING();
  public static SSEStatus Default() {
    return theDefault;
  }
  public static SSEStatus create_ENABLING() {
    return new SSEStatus_ENABLING();
  }
  public static SSEStatus create_ENABLED() {
    return new SSEStatus_ENABLED();
  }
  public static SSEStatus create_DISABLING() {
    return new SSEStatus_DISABLING();
  }
  public static SSEStatus create_DISABLED() {
    return new SSEStatus_DISABLED();
  }
  public static SSEStatus create_UPDATING() {
    return new SSEStatus_UPDATING();
  }
  public boolean is_ENABLING() { return this instanceof SSEStatus_ENABLING; }
  public boolean is_ENABLED() { return this instanceof SSEStatus_ENABLED; }
  public boolean is_DISABLING() { return this instanceof SSEStatus_DISABLING; }
  public boolean is_DISABLED() { return this instanceof SSEStatus_DISABLED; }
  public boolean is_UPDATING() { return this instanceof SSEStatus_UPDATING; }
  public static java.util.ArrayList<SSEStatus> AllSingletonConstructors() {
    java.util.ArrayList<SSEStatus> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new SSEStatus_ENABLING());
    singleton_iterator.add(new SSEStatus_ENABLED());
    singleton_iterator.add(new SSEStatus_DISABLING());
    singleton_iterator.add(new SSEStatus_DISABLED());
    singleton_iterator.add(new SSEStatus_UPDATING());
    return singleton_iterator;
  }
}
