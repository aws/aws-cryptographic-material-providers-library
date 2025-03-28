// Class InputFormat
// Dafny class InputFormat compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public abstract class InputFormat {
  public InputFormat() {
  }
  private static final dafny.TypeDescriptor<InputFormat> _TYPE = dafny.TypeDescriptor.<InputFormat>referenceWithInitializer(InputFormat.class, () -> InputFormat.Default());
  public static dafny.TypeDescriptor<InputFormat> _typeDescriptor() {
    return (dafny.TypeDescriptor<InputFormat>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final InputFormat theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.InputFormat.create_DYNAMODB__JSON();
  public static InputFormat Default() {
    return theDefault;
  }
  public static InputFormat create_DYNAMODB__JSON() {
    return new InputFormat_DYNAMODB__JSON();
  }
  public static InputFormat create_ION() {
    return new InputFormat_ION();
  }
  public static InputFormat create_CSV() {
    return new InputFormat_CSV();
  }
  public boolean is_DYNAMODB__JSON() { return this instanceof InputFormat_DYNAMODB__JSON; }
  public boolean is_ION() { return this instanceof InputFormat_ION; }
  public boolean is_CSV() { return this instanceof InputFormat_CSV; }
  public static java.util.ArrayList<InputFormat> AllSingletonConstructors() {
    java.util.ArrayList<InputFormat> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new InputFormat_DYNAMODB__JSON());
    singleton_iterator.add(new InputFormat_ION());
    singleton_iterator.add(new InputFormat_CSV());
    return singleton_iterator;
  }
}
