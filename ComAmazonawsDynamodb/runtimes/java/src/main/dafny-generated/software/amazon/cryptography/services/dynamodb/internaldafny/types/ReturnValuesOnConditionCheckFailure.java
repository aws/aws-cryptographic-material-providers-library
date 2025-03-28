// Class ReturnValuesOnConditionCheckFailure
// Dafny class ReturnValuesOnConditionCheckFailure compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public abstract class ReturnValuesOnConditionCheckFailure {
  public ReturnValuesOnConditionCheckFailure() {
  }
  private static final dafny.TypeDescriptor<ReturnValuesOnConditionCheckFailure> _TYPE = dafny.TypeDescriptor.<ReturnValuesOnConditionCheckFailure>referenceWithInitializer(ReturnValuesOnConditionCheckFailure.class, () -> ReturnValuesOnConditionCheckFailure.Default());
  public static dafny.TypeDescriptor<ReturnValuesOnConditionCheckFailure> _typeDescriptor() {
    return (dafny.TypeDescriptor<ReturnValuesOnConditionCheckFailure>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ReturnValuesOnConditionCheckFailure theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.ReturnValuesOnConditionCheckFailure.create_ALL__OLD();
  public static ReturnValuesOnConditionCheckFailure Default() {
    return theDefault;
  }
  public static ReturnValuesOnConditionCheckFailure create_ALL__OLD() {
    return new ReturnValuesOnConditionCheckFailure_ALL__OLD();
  }
  public static ReturnValuesOnConditionCheckFailure create_NONE() {
    return new ReturnValuesOnConditionCheckFailure_NONE();
  }
  public boolean is_ALL__OLD() { return this instanceof ReturnValuesOnConditionCheckFailure_ALL__OLD; }
  public boolean is_NONE() { return this instanceof ReturnValuesOnConditionCheckFailure_NONE; }
  public static java.util.ArrayList<ReturnValuesOnConditionCheckFailure> AllSingletonConstructors() {
    java.util.ArrayList<ReturnValuesOnConditionCheckFailure> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new ReturnValuesOnConditionCheckFailure_ALL__OLD());
    singleton_iterator.add(new ReturnValuesOnConditionCheckFailure_NONE());
    return singleton_iterator;
  }
}
