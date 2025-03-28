// Class ConnectionErrorCodeType
// Dafny class ConnectionErrorCodeType compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public abstract class ConnectionErrorCodeType {
  public ConnectionErrorCodeType() {
  }
  private static final dafny.TypeDescriptor<ConnectionErrorCodeType> _TYPE = dafny.TypeDescriptor.<ConnectionErrorCodeType>referenceWithInitializer(ConnectionErrorCodeType.class, () -> ConnectionErrorCodeType.Default());
  public static dafny.TypeDescriptor<ConnectionErrorCodeType> _typeDescriptor() {
    return (dafny.TypeDescriptor<ConnectionErrorCodeType>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ConnectionErrorCodeType theDefault = software.amazon.cryptography.services.kms.internaldafny.types.ConnectionErrorCodeType.create_INVALID__CREDENTIALS();
  public static ConnectionErrorCodeType Default() {
    return theDefault;
  }
  public static ConnectionErrorCodeType create_INVALID__CREDENTIALS() {
    return new ConnectionErrorCodeType_INVALID__CREDENTIALS();
  }
  public static ConnectionErrorCodeType create_CLUSTER__NOT__FOUND() {
    return new ConnectionErrorCodeType_CLUSTER__NOT__FOUND();
  }
  public static ConnectionErrorCodeType create_NETWORK__ERRORS() {
    return new ConnectionErrorCodeType_NETWORK__ERRORS();
  }
  public static ConnectionErrorCodeType create_INTERNAL__ERROR() {
    return new ConnectionErrorCodeType_INTERNAL__ERROR();
  }
  public static ConnectionErrorCodeType create_INSUFFICIENT__CLOUDHSM__HSMS() {
    return new ConnectionErrorCodeType_INSUFFICIENT__CLOUDHSM__HSMS();
  }
  public static ConnectionErrorCodeType create_USER__LOCKED__OUT() {
    return new ConnectionErrorCodeType_USER__LOCKED__OUT();
  }
  public static ConnectionErrorCodeType create_USER__NOT__FOUND() {
    return new ConnectionErrorCodeType_USER__NOT__FOUND();
  }
  public static ConnectionErrorCodeType create_USER__LOGGED__IN() {
    return new ConnectionErrorCodeType_USER__LOGGED__IN();
  }
  public static ConnectionErrorCodeType create_SUBNET__NOT__FOUND() {
    return new ConnectionErrorCodeType_SUBNET__NOT__FOUND();
  }
  public static ConnectionErrorCodeType create_INSUFFICIENT__FREE__ADDRESSES__IN__SUBNET() {
    return new ConnectionErrorCodeType_INSUFFICIENT__FREE__ADDRESSES__IN__SUBNET();
  }
  public static ConnectionErrorCodeType create_XKS__PROXY__ACCESS__DENIED() {
    return new ConnectionErrorCodeType_XKS__PROXY__ACCESS__DENIED();
  }
  public static ConnectionErrorCodeType create_XKS__PROXY__NOT__REACHABLE() {
    return new ConnectionErrorCodeType_XKS__PROXY__NOT__REACHABLE();
  }
  public static ConnectionErrorCodeType create_XKS__VPC__ENDPOINT__SERVICE__NOT__FOUND() {
    return new ConnectionErrorCodeType_XKS__VPC__ENDPOINT__SERVICE__NOT__FOUND();
  }
  public static ConnectionErrorCodeType create_XKS__PROXY__INVALID__RESPONSE() {
    return new ConnectionErrorCodeType_XKS__PROXY__INVALID__RESPONSE();
  }
  public static ConnectionErrorCodeType create_XKS__PROXY__INVALID__CONFIGURATION() {
    return new ConnectionErrorCodeType_XKS__PROXY__INVALID__CONFIGURATION();
  }
  public static ConnectionErrorCodeType create_XKS__VPC__ENDPOINT__SERVICE__INVALID__CONFIGURATION() {
    return new ConnectionErrorCodeType_XKS__VPC__ENDPOINT__SERVICE__INVALID__CONFIGURATION();
  }
  public static ConnectionErrorCodeType create_XKS__PROXY__TIMED__OUT() {
    return new ConnectionErrorCodeType_XKS__PROXY__TIMED__OUT();
  }
  public static ConnectionErrorCodeType create_XKS__PROXY__INVALID__TLS__CONFIGURATION() {
    return new ConnectionErrorCodeType_XKS__PROXY__INVALID__TLS__CONFIGURATION();
  }
  public boolean is_INVALID__CREDENTIALS() { return this instanceof ConnectionErrorCodeType_INVALID__CREDENTIALS; }
  public boolean is_CLUSTER__NOT__FOUND() { return this instanceof ConnectionErrorCodeType_CLUSTER__NOT__FOUND; }
  public boolean is_NETWORK__ERRORS() { return this instanceof ConnectionErrorCodeType_NETWORK__ERRORS; }
  public boolean is_INTERNAL__ERROR() { return this instanceof ConnectionErrorCodeType_INTERNAL__ERROR; }
  public boolean is_INSUFFICIENT__CLOUDHSM__HSMS() { return this instanceof ConnectionErrorCodeType_INSUFFICIENT__CLOUDHSM__HSMS; }
  public boolean is_USER__LOCKED__OUT() { return this instanceof ConnectionErrorCodeType_USER__LOCKED__OUT; }
  public boolean is_USER__NOT__FOUND() { return this instanceof ConnectionErrorCodeType_USER__NOT__FOUND; }
  public boolean is_USER__LOGGED__IN() { return this instanceof ConnectionErrorCodeType_USER__LOGGED__IN; }
  public boolean is_SUBNET__NOT__FOUND() { return this instanceof ConnectionErrorCodeType_SUBNET__NOT__FOUND; }
  public boolean is_INSUFFICIENT__FREE__ADDRESSES__IN__SUBNET() { return this instanceof ConnectionErrorCodeType_INSUFFICIENT__FREE__ADDRESSES__IN__SUBNET; }
  public boolean is_XKS__PROXY__ACCESS__DENIED() { return this instanceof ConnectionErrorCodeType_XKS__PROXY__ACCESS__DENIED; }
  public boolean is_XKS__PROXY__NOT__REACHABLE() { return this instanceof ConnectionErrorCodeType_XKS__PROXY__NOT__REACHABLE; }
  public boolean is_XKS__VPC__ENDPOINT__SERVICE__NOT__FOUND() { return this instanceof ConnectionErrorCodeType_XKS__VPC__ENDPOINT__SERVICE__NOT__FOUND; }
  public boolean is_XKS__PROXY__INVALID__RESPONSE() { return this instanceof ConnectionErrorCodeType_XKS__PROXY__INVALID__RESPONSE; }
  public boolean is_XKS__PROXY__INVALID__CONFIGURATION() { return this instanceof ConnectionErrorCodeType_XKS__PROXY__INVALID__CONFIGURATION; }
  public boolean is_XKS__VPC__ENDPOINT__SERVICE__INVALID__CONFIGURATION() { return this instanceof ConnectionErrorCodeType_XKS__VPC__ENDPOINT__SERVICE__INVALID__CONFIGURATION; }
  public boolean is_XKS__PROXY__TIMED__OUT() { return this instanceof ConnectionErrorCodeType_XKS__PROXY__TIMED__OUT; }
  public boolean is_XKS__PROXY__INVALID__TLS__CONFIGURATION() { return this instanceof ConnectionErrorCodeType_XKS__PROXY__INVALID__TLS__CONFIGURATION; }
  public static java.util.ArrayList<ConnectionErrorCodeType> AllSingletonConstructors() {
    java.util.ArrayList<ConnectionErrorCodeType> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new ConnectionErrorCodeType_INVALID__CREDENTIALS());
    singleton_iterator.add(new ConnectionErrorCodeType_CLUSTER__NOT__FOUND());
    singleton_iterator.add(new ConnectionErrorCodeType_NETWORK__ERRORS());
    singleton_iterator.add(new ConnectionErrorCodeType_INTERNAL__ERROR());
    singleton_iterator.add(new ConnectionErrorCodeType_INSUFFICIENT__CLOUDHSM__HSMS());
    singleton_iterator.add(new ConnectionErrorCodeType_USER__LOCKED__OUT());
    singleton_iterator.add(new ConnectionErrorCodeType_USER__NOT__FOUND());
    singleton_iterator.add(new ConnectionErrorCodeType_USER__LOGGED__IN());
    singleton_iterator.add(new ConnectionErrorCodeType_SUBNET__NOT__FOUND());
    singleton_iterator.add(new ConnectionErrorCodeType_INSUFFICIENT__FREE__ADDRESSES__IN__SUBNET());
    singleton_iterator.add(new ConnectionErrorCodeType_XKS__PROXY__ACCESS__DENIED());
    singleton_iterator.add(new ConnectionErrorCodeType_XKS__PROXY__NOT__REACHABLE());
    singleton_iterator.add(new ConnectionErrorCodeType_XKS__VPC__ENDPOINT__SERVICE__NOT__FOUND());
    singleton_iterator.add(new ConnectionErrorCodeType_XKS__PROXY__INVALID__RESPONSE());
    singleton_iterator.add(new ConnectionErrorCodeType_XKS__PROXY__INVALID__CONFIGURATION());
    singleton_iterator.add(new ConnectionErrorCodeType_XKS__VPC__ENDPOINT__SERVICE__INVALID__CONFIGURATION());
    singleton_iterator.add(new ConnectionErrorCodeType_XKS__PROXY__TIMED__OUT());
    singleton_iterator.add(new ConnectionErrorCodeType_XKS__PROXY__INVALID__TLS__CONFIGURATION());
    return singleton_iterator;
  }
}
