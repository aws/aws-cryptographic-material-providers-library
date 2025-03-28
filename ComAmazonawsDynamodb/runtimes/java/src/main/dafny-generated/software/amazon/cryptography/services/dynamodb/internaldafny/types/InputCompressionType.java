// Class InputCompressionType
// Dafny class InputCompressionType compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public abstract class InputCompressionType {
  public InputCompressionType() {
  }
  private static final dafny.TypeDescriptor<InputCompressionType> _TYPE = dafny.TypeDescriptor.<InputCompressionType>referenceWithInitializer(InputCompressionType.class, () -> InputCompressionType.Default());
  public static dafny.TypeDescriptor<InputCompressionType> _typeDescriptor() {
    return (dafny.TypeDescriptor<InputCompressionType>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final InputCompressionType theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.InputCompressionType.create_GZIP();
  public static InputCompressionType Default() {
    return theDefault;
  }
  public static InputCompressionType create_GZIP() {
    return new InputCompressionType_GZIP();
  }
  public static InputCompressionType create_ZSTD() {
    return new InputCompressionType_ZSTD();
  }
  public static InputCompressionType create_NONE() {
    return new InputCompressionType_NONE();
  }
  public boolean is_GZIP() { return this instanceof InputCompressionType_GZIP; }
  public boolean is_ZSTD() { return this instanceof InputCompressionType_ZSTD; }
  public boolean is_NONE() { return this instanceof InputCompressionType_NONE; }
  public static java.util.ArrayList<InputCompressionType> AllSingletonConstructors() {
    java.util.ArrayList<InputCompressionType> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new InputCompressionType_GZIP());
    singleton_iterator.add(new InputCompressionType_ZSTD());
    singleton_iterator.add(new InputCompressionType_NONE());
    return singleton_iterator;
  }
}
