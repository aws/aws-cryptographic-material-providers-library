// Class AttributeAction
// Dafny class AttributeAction compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public abstract class AttributeAction {
  public AttributeAction() {
  }
  private static final dafny.TypeDescriptor<AttributeAction> _TYPE = dafny.TypeDescriptor.<AttributeAction>referenceWithInitializer(AttributeAction.class, () -> AttributeAction.Default());
  public static dafny.TypeDescriptor<AttributeAction> _typeDescriptor() {
    return (dafny.TypeDescriptor<AttributeAction>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final AttributeAction theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.AttributeAction.create_ADD();
  public static AttributeAction Default() {
    return theDefault;
  }
  public static AttributeAction create_ADD() {
    return new AttributeAction_ADD();
  }
  public static AttributeAction create_PUT() {
    return new AttributeAction_PUT();
  }
  public static AttributeAction create_DELETE() {
    return new AttributeAction_DELETE();
  }
  public boolean is_ADD() { return this instanceof AttributeAction_ADD; }
  public boolean is_PUT() { return this instanceof AttributeAction_PUT; }
  public boolean is_DELETE() { return this instanceof AttributeAction_DELETE; }
  public static java.util.ArrayList<AttributeAction> AllSingletonConstructors() {
    java.util.ArrayList<AttributeAction> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new AttributeAction_ADD());
    singleton_iterator.add(new AttributeAction_PUT());
    singleton_iterator.add(new AttributeAction_DELETE());
    return singleton_iterator;
  }
}
