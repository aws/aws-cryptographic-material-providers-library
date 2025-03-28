// Class SSEType
// Dafny class SSEType compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public abstract class SSEType {
  public SSEType() {
  }
  private static final dafny.TypeDescriptor<SSEType> _TYPE = dafny.TypeDescriptor.<SSEType>referenceWithInitializer(SSEType.class, () -> SSEType.Default());
  public static dafny.TypeDescriptor<SSEType> _typeDescriptor() {
    return (dafny.TypeDescriptor<SSEType>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final SSEType theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.SSEType.create_AES256();
  public static SSEType Default() {
    return theDefault;
  }
  public static SSEType create_AES256() {
    return new SSEType_AES256();
  }
  public static SSEType create_KMS() {
    return new SSEType_KMS();
  }
  public boolean is_AES256() { return this instanceof SSEType_AES256; }
  public boolean is_KMS() { return this instanceof SSEType_KMS; }
  public static java.util.ArrayList<SSEType> AllSingletonConstructors() {
    java.util.ArrayList<SSEType> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new SSEType_AES256());
    singleton_iterator.add(new SSEType_KMS());
    return singleton_iterator;
  }
}
