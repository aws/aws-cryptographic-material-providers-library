// Class KeyType
// Dafny class KeyType compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public abstract class KeyType {
  public KeyType() {
  }
  private static final dafny.TypeDescriptor<KeyType> _TYPE = dafny.TypeDescriptor.<KeyType>referenceWithInitializer(KeyType.class, () -> KeyType.Default());
  public static dafny.TypeDescriptor<KeyType> _typeDescriptor() {
    return (dafny.TypeDescriptor<KeyType>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final KeyType theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.KeyType.create_HASH();
  public static KeyType Default() {
    return theDefault;
  }
  public static KeyType create_HASH() {
    return new KeyType_HASH();
  }
  public static KeyType create_RANGE() {
    return new KeyType_RANGE();
  }
  public boolean is_HASH() { return this instanceof KeyType_HASH; }
  public boolean is_RANGE() { return this instanceof KeyType_RANGE; }
  public static java.util.ArrayList<KeyType> AllSingletonConstructors() {
    java.util.ArrayList<KeyType> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new KeyType_HASH());
    singleton_iterator.add(new KeyType_RANGE());
    return singleton_iterator;
  }
}
