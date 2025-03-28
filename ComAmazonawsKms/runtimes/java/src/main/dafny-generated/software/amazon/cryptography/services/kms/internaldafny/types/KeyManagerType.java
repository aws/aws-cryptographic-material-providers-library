// Class KeyManagerType
// Dafny class KeyManagerType compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public abstract class KeyManagerType {
  public KeyManagerType() {
  }
  private static final dafny.TypeDescriptor<KeyManagerType> _TYPE = dafny.TypeDescriptor.<KeyManagerType>referenceWithInitializer(KeyManagerType.class, () -> KeyManagerType.Default());
  public static dafny.TypeDescriptor<KeyManagerType> _typeDescriptor() {
    return (dafny.TypeDescriptor<KeyManagerType>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final KeyManagerType theDefault = software.amazon.cryptography.services.kms.internaldafny.types.KeyManagerType.create_AWS();
  public static KeyManagerType Default() {
    return theDefault;
  }
  public static KeyManagerType create_AWS() {
    return new KeyManagerType_AWS();
  }
  public static KeyManagerType create_CUSTOMER() {
    return new KeyManagerType_CUSTOMER();
  }
  public boolean is_AWS() { return this instanceof KeyManagerType_AWS; }
  public boolean is_CUSTOMER() { return this instanceof KeyManagerType_CUSTOMER; }
  public static java.util.ArrayList<KeyManagerType> AllSingletonConstructors() {
    java.util.ArrayList<KeyManagerType> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new KeyManagerType_AWS());
    singleton_iterator.add(new KeyManagerType_CUSTOMER());
    return singleton_iterator;
  }
}
