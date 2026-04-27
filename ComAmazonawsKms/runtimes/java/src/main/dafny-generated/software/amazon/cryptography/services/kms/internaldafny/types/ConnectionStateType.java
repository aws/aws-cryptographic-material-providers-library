// Class ConnectionStateType
// Dafny class ConnectionStateType compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class ConnectionStateType {
  public ConnectionStateType() {
  }
  private static final dafny.TypeDescriptor<ConnectionStateType> _TYPE = dafny.TypeDescriptor.<ConnectionStateType>referenceWithInitializer(ConnectionStateType.class, () -> ConnectionStateType.Default());
  public static dafny.TypeDescriptor<ConnectionStateType> _typeDescriptor() {
    return (dafny.TypeDescriptor<ConnectionStateType>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ConnectionStateType theDefault = ConnectionStateType.create_CONNECTED();
  public static ConnectionStateType Default() {
    return theDefault;
  }
  public static ConnectionStateType create_CONNECTED() {
    return new ConnectionStateType_CONNECTED();
  }
  public static ConnectionStateType create_CONNECTING() {
    return new ConnectionStateType_CONNECTING();
  }
  public static ConnectionStateType create_FAILED() {
    return new ConnectionStateType_FAILED();
  }
  public static ConnectionStateType create_DISCONNECTED() {
    return new ConnectionStateType_DISCONNECTED();
  }
  public static ConnectionStateType create_DISCONNECTING() {
    return new ConnectionStateType_DISCONNECTING();
  }
  public boolean is_CONNECTED() { return this instanceof ConnectionStateType_CONNECTED; }
  public boolean is_CONNECTING() { return this instanceof ConnectionStateType_CONNECTING; }
  public boolean is_FAILED() { return this instanceof ConnectionStateType_FAILED; }
  public boolean is_DISCONNECTED() { return this instanceof ConnectionStateType_DISCONNECTED; }
  public boolean is_DISCONNECTING() { return this instanceof ConnectionStateType_DISCONNECTING; }
  public static java.util.ArrayList<ConnectionStateType> AllSingletonConstructors() {
    java.util.ArrayList<ConnectionStateType> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new ConnectionStateType_CONNECTED());
    singleton_iterator.add(new ConnectionStateType_CONNECTING());
    singleton_iterator.add(new ConnectionStateType_FAILED());
    singleton_iterator.add(new ConnectionStateType_DISCONNECTED());
    singleton_iterator.add(new ConnectionStateType_DISCONNECTING());
    return singleton_iterator;
  }
}
