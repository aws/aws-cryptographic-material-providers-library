// Class CustomKeyStoreType
// Dafny class CustomKeyStoreType compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class CustomKeyStoreType {
  public CustomKeyStoreType() {
  }
  private static final dafny.TypeDescriptor<CustomKeyStoreType> _TYPE = dafny.TypeDescriptor.<CustomKeyStoreType>referenceWithInitializer(CustomKeyStoreType.class, () -> CustomKeyStoreType.Default());
  public static dafny.TypeDescriptor<CustomKeyStoreType> _typeDescriptor() {
    return (dafny.TypeDescriptor<CustomKeyStoreType>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final CustomKeyStoreType theDefault = CustomKeyStoreType.create_AWS__CLOUDHSM();
  public static CustomKeyStoreType Default() {
    return theDefault;
  }
  public static CustomKeyStoreType create_AWS__CLOUDHSM() {
    return new CustomKeyStoreType_AWS__CLOUDHSM();
  }
  public static CustomKeyStoreType create_EXTERNAL__KEY__STORE() {
    return new CustomKeyStoreType_EXTERNAL__KEY__STORE();
  }
  public boolean is_AWS__CLOUDHSM() { return this instanceof CustomKeyStoreType_AWS__CLOUDHSM; }
  public boolean is_EXTERNAL__KEY__STORE() { return this instanceof CustomKeyStoreType_EXTERNAL__KEY__STORE; }
  public static java.util.ArrayList<CustomKeyStoreType> AllSingletonConstructors() {
    java.util.ArrayList<CustomKeyStoreType> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new CustomKeyStoreType_AWS__CLOUDHSM());
    singleton_iterator.add(new CustomKeyStoreType_EXTERNAL__KEY__STORE());
    return singleton_iterator;
  }
}
