// Class ReturnValue
// Dafny class ReturnValue compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public abstract class ReturnValue {
  public ReturnValue() {
  }
  private static final dafny.TypeDescriptor<ReturnValue> _TYPE = dafny.TypeDescriptor.<ReturnValue>referenceWithInitializer(ReturnValue.class, () -> ReturnValue.Default());
  public static dafny.TypeDescriptor<ReturnValue> _typeDescriptor() {
    return (dafny.TypeDescriptor<ReturnValue>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ReturnValue theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.ReturnValue.create_NONE();
  public static ReturnValue Default() {
    return theDefault;
  }
  public static ReturnValue create_NONE() {
    return new ReturnValue_NONE();
  }
  public static ReturnValue create_ALL__OLD() {
    return new ReturnValue_ALL__OLD();
  }
  public static ReturnValue create_UPDATED__OLD() {
    return new ReturnValue_UPDATED__OLD();
  }
  public static ReturnValue create_ALL__NEW() {
    return new ReturnValue_ALL__NEW();
  }
  public static ReturnValue create_UPDATED__NEW() {
    return new ReturnValue_UPDATED__NEW();
  }
  public boolean is_NONE() { return this instanceof ReturnValue_NONE; }
  public boolean is_ALL__OLD() { return this instanceof ReturnValue_ALL__OLD; }
  public boolean is_UPDATED__OLD() { return this instanceof ReturnValue_UPDATED__OLD; }
  public boolean is_ALL__NEW() { return this instanceof ReturnValue_ALL__NEW; }
  public boolean is_UPDATED__NEW() { return this instanceof ReturnValue_UPDATED__NEW; }
  public static java.util.ArrayList<ReturnValue> AllSingletonConstructors() {
    java.util.ArrayList<ReturnValue> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new ReturnValue_NONE());
    singleton_iterator.add(new ReturnValue_ALL__OLD());
    singleton_iterator.add(new ReturnValue_UPDATED__OLD());
    singleton_iterator.add(new ReturnValue_ALL__NEW());
    singleton_iterator.add(new ReturnValue_UPDATED__NEW());
    return singleton_iterator;
  }
}
