// Class Select
// Dafny class Select compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public abstract class Select {
  public Select() {
  }
  private static final dafny.TypeDescriptor<Select> _TYPE = dafny.TypeDescriptor.<Select>referenceWithInitializer(Select.class, () -> Select.Default());
  public static dafny.TypeDescriptor<Select> _typeDescriptor() {
    return (dafny.TypeDescriptor<Select>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final Select theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.Select.create_ALL__ATTRIBUTES();
  public static Select Default() {
    return theDefault;
  }
  public static Select create_ALL__ATTRIBUTES() {
    return new Select_ALL__ATTRIBUTES();
  }
  public static Select create_ALL__PROJECTED__ATTRIBUTES() {
    return new Select_ALL__PROJECTED__ATTRIBUTES();
  }
  public static Select create_SPECIFIC__ATTRIBUTES() {
    return new Select_SPECIFIC__ATTRIBUTES();
  }
  public static Select create_COUNT() {
    return new Select_COUNT();
  }
  public boolean is_ALL__ATTRIBUTES() { return this instanceof Select_ALL__ATTRIBUTES; }
  public boolean is_ALL__PROJECTED__ATTRIBUTES() { return this instanceof Select_ALL__PROJECTED__ATTRIBUTES; }
  public boolean is_SPECIFIC__ATTRIBUTES() { return this instanceof Select_SPECIFIC__ATTRIBUTES; }
  public boolean is_COUNT() { return this instanceof Select_COUNT; }
  public static java.util.ArrayList<Select> AllSingletonConstructors() {
    java.util.ArrayList<Select> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new Select_ALL__ATTRIBUTES());
    singleton_iterator.add(new Select_ALL__PROJECTED__ATTRIBUTES());
    singleton_iterator.add(new Select_SPECIFIC__ATTRIBUTES());
    singleton_iterator.add(new Select_COUNT());
    return singleton_iterator;
  }
}
