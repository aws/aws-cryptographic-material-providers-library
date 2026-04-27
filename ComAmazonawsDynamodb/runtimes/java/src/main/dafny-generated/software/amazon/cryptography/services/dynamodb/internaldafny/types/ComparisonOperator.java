// Class ComparisonOperator
// Dafny class ComparisonOperator compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class ComparisonOperator {
  public ComparisonOperator() {
  }
  private static final dafny.TypeDescriptor<ComparisonOperator> _TYPE = dafny.TypeDescriptor.<ComparisonOperator>referenceWithInitializer(ComparisonOperator.class, () -> ComparisonOperator.Default());
  public static dafny.TypeDescriptor<ComparisonOperator> _typeDescriptor() {
    return (dafny.TypeDescriptor<ComparisonOperator>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ComparisonOperator theDefault = ComparisonOperator.create_EQ();
  public static ComparisonOperator Default() {
    return theDefault;
  }
  public static ComparisonOperator create_EQ() {
    return new ComparisonOperator_EQ();
  }
  public static ComparisonOperator create_NE() {
    return new ComparisonOperator_NE();
  }
  public static ComparisonOperator create_IN() {
    return new ComparisonOperator_IN();
  }
  public static ComparisonOperator create_LE() {
    return new ComparisonOperator_LE();
  }
  public static ComparisonOperator create_LT() {
    return new ComparisonOperator_LT();
  }
  public static ComparisonOperator create_GE() {
    return new ComparisonOperator_GE();
  }
  public static ComparisonOperator create_GT() {
    return new ComparisonOperator_GT();
  }
  public static ComparisonOperator create_BETWEEN() {
    return new ComparisonOperator_BETWEEN();
  }
  public static ComparisonOperator create_NOT__NULL() {
    return new ComparisonOperator_NOT__NULL();
  }
  public static ComparisonOperator create_NULL() {
    return new ComparisonOperator_NULL();
  }
  public static ComparisonOperator create_CONTAINS() {
    return new ComparisonOperator_CONTAINS();
  }
  public static ComparisonOperator create_NOT__CONTAINS() {
    return new ComparisonOperator_NOT__CONTAINS();
  }
  public static ComparisonOperator create_BEGINS__WITH() {
    return new ComparisonOperator_BEGINS__WITH();
  }
  public boolean is_EQ() { return this instanceof ComparisonOperator_EQ; }
  public boolean is_NE() { return this instanceof ComparisonOperator_NE; }
  public boolean is_IN() { return this instanceof ComparisonOperator_IN; }
  public boolean is_LE() { return this instanceof ComparisonOperator_LE; }
  public boolean is_LT() { return this instanceof ComparisonOperator_LT; }
  public boolean is_GE() { return this instanceof ComparisonOperator_GE; }
  public boolean is_GT() { return this instanceof ComparisonOperator_GT; }
  public boolean is_BETWEEN() { return this instanceof ComparisonOperator_BETWEEN; }
  public boolean is_NOT__NULL() { return this instanceof ComparisonOperator_NOT__NULL; }
  public boolean is_NULL() { return this instanceof ComparisonOperator_NULL; }
  public boolean is_CONTAINS() { return this instanceof ComparisonOperator_CONTAINS; }
  public boolean is_NOT__CONTAINS() { return this instanceof ComparisonOperator_NOT__CONTAINS; }
  public boolean is_BEGINS__WITH() { return this instanceof ComparisonOperator_BEGINS__WITH; }
  public static java.util.ArrayList<ComparisonOperator> AllSingletonConstructors() {
    java.util.ArrayList<ComparisonOperator> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new ComparisonOperator_EQ());
    singleton_iterator.add(new ComparisonOperator_NE());
    singleton_iterator.add(new ComparisonOperator_IN());
    singleton_iterator.add(new ComparisonOperator_LE());
    singleton_iterator.add(new ComparisonOperator_LT());
    singleton_iterator.add(new ComparisonOperator_GE());
    singleton_iterator.add(new ComparisonOperator_GT());
    singleton_iterator.add(new ComparisonOperator_BETWEEN());
    singleton_iterator.add(new ComparisonOperator_NOT__NULL());
    singleton_iterator.add(new ComparisonOperator_NULL());
    singleton_iterator.add(new ComparisonOperator_CONTAINS());
    singleton_iterator.add(new ComparisonOperator_NOT__CONTAINS());
    singleton_iterator.add(new ComparisonOperator_BEGINS__WITH());
    return singleton_iterator;
  }
}
