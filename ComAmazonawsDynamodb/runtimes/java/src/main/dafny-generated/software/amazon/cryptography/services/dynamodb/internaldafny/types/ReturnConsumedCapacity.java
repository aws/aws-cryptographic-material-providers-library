// Class ReturnConsumedCapacity
// Dafny class ReturnConsumedCapacity compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class ReturnConsumedCapacity {
  public ReturnConsumedCapacity() {
  }
  private static final dafny.TypeDescriptor<ReturnConsumedCapacity> _TYPE = dafny.TypeDescriptor.<ReturnConsumedCapacity>referenceWithInitializer(ReturnConsumedCapacity.class, () -> ReturnConsumedCapacity.Default());
  public static dafny.TypeDescriptor<ReturnConsumedCapacity> _typeDescriptor() {
    return (dafny.TypeDescriptor<ReturnConsumedCapacity>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ReturnConsumedCapacity theDefault = ReturnConsumedCapacity.create_INDEXES();
  public static ReturnConsumedCapacity Default() {
    return theDefault;
  }
  public static ReturnConsumedCapacity create_INDEXES() {
    return new ReturnConsumedCapacity_INDEXES();
  }
  public static ReturnConsumedCapacity create_TOTAL() {
    return new ReturnConsumedCapacity_TOTAL();
  }
  public static ReturnConsumedCapacity create_NONE() {
    return new ReturnConsumedCapacity_NONE();
  }
  public boolean is_INDEXES() { return this instanceof ReturnConsumedCapacity_INDEXES; }
  public boolean is_TOTAL() { return this instanceof ReturnConsumedCapacity_TOTAL; }
  public boolean is_NONE() { return this instanceof ReturnConsumedCapacity_NONE; }
  public static java.util.ArrayList<ReturnConsumedCapacity> AllSingletonConstructors() {
    java.util.ArrayList<ReturnConsumedCapacity> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new ReturnConsumedCapacity_INDEXES());
    singleton_iterator.add(new ReturnConsumedCapacity_TOTAL());
    singleton_iterator.add(new ReturnConsumedCapacity_NONE());
    return singleton_iterator;
  }
}
