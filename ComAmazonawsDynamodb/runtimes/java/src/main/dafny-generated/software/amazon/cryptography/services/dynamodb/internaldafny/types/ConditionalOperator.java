// Class ConditionalOperator
// Dafny class ConditionalOperator compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public abstract class ConditionalOperator {
  public ConditionalOperator() {
  }
  private static final dafny.TypeDescriptor<ConditionalOperator> _TYPE = dafny.TypeDescriptor.<ConditionalOperator>referenceWithInitializer(ConditionalOperator.class, () -> ConditionalOperator.Default());
  public static dafny.TypeDescriptor<ConditionalOperator> _typeDescriptor() {
    return (dafny.TypeDescriptor<ConditionalOperator>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ConditionalOperator theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.ConditionalOperator.create_AND();
  public static ConditionalOperator Default() {
    return theDefault;
  }
  public static ConditionalOperator create_AND() {
    return new ConditionalOperator_AND();
  }
  public static ConditionalOperator create_OR() {
    return new ConditionalOperator_OR();
  }
  public boolean is_AND() { return this instanceof ConditionalOperator_AND; }
  public boolean is_OR() { return this instanceof ConditionalOperator_OR; }
  public static java.util.ArrayList<ConditionalOperator> AllSingletonConstructors() {
    java.util.ArrayList<ConditionalOperator> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new ConditionalOperator_AND());
    singleton_iterator.add(new ConditionalOperator_OR());
    return singleton_iterator;
  }
}
