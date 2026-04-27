// Class KeyUsageType
// Dafny class KeyUsageType compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class KeyUsageType {
  public KeyUsageType() {
  }
  private static final dafny.TypeDescriptor<KeyUsageType> _TYPE = dafny.TypeDescriptor.<KeyUsageType>referenceWithInitializer(KeyUsageType.class, () -> KeyUsageType.Default());
  public static dafny.TypeDescriptor<KeyUsageType> _typeDescriptor() {
    return (dafny.TypeDescriptor<KeyUsageType>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final KeyUsageType theDefault = KeyUsageType.create_SIGN__VERIFY();
  public static KeyUsageType Default() {
    return theDefault;
  }
  public static KeyUsageType create_SIGN__VERIFY() {
    return new KeyUsageType_SIGN__VERIFY();
  }
  public static KeyUsageType create_ENCRYPT__DECRYPT() {
    return new KeyUsageType_ENCRYPT__DECRYPT();
  }
  public static KeyUsageType create_GENERATE__VERIFY__MAC() {
    return new KeyUsageType_GENERATE__VERIFY__MAC();
  }
  public static KeyUsageType create_KEY__AGREEMENT() {
    return new KeyUsageType_KEY__AGREEMENT();
  }
  public boolean is_SIGN__VERIFY() { return this instanceof KeyUsageType_SIGN__VERIFY; }
  public boolean is_ENCRYPT__DECRYPT() { return this instanceof KeyUsageType_ENCRYPT__DECRYPT; }
  public boolean is_GENERATE__VERIFY__MAC() { return this instanceof KeyUsageType_GENERATE__VERIFY__MAC; }
  public boolean is_KEY__AGREEMENT() { return this instanceof KeyUsageType_KEY__AGREEMENT; }
  public static java.util.ArrayList<KeyUsageType> AllSingletonConstructors() {
    java.util.ArrayList<KeyUsageType> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new KeyUsageType_SIGN__VERIFY());
    singleton_iterator.add(new KeyUsageType_ENCRYPT__DECRYPT());
    singleton_iterator.add(new KeyUsageType_GENERATE__VERIFY__MAC());
    singleton_iterator.add(new KeyUsageType_KEY__AGREEMENT());
    return singleton_iterator;
  }
}
