// Class ScalarAttributeType
// Dafny class ScalarAttributeType compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class ScalarAttributeType {
  public ScalarAttributeType() {
  }
  private static final dafny.TypeDescriptor<ScalarAttributeType> _TYPE = dafny.TypeDescriptor.<ScalarAttributeType>referenceWithInitializer(ScalarAttributeType.class, () -> ScalarAttributeType.Default());
  public static dafny.TypeDescriptor<ScalarAttributeType> _typeDescriptor() {
    return (dafny.TypeDescriptor<ScalarAttributeType>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ScalarAttributeType theDefault = ScalarAttributeType.create_S();
  public static ScalarAttributeType Default() {
    return theDefault;
  }
  public static ScalarAttributeType create_S() {
    return new ScalarAttributeType_S();
  }
  public static ScalarAttributeType create_N() {
    return new ScalarAttributeType_N();
  }
  public static ScalarAttributeType create_B() {
    return new ScalarAttributeType_B();
  }
  public boolean is_S() { return this instanceof ScalarAttributeType_S; }
  public boolean is_N() { return this instanceof ScalarAttributeType_N; }
  public boolean is_B() { return this instanceof ScalarAttributeType_B; }
  public static java.util.ArrayList<ScalarAttributeType> AllSingletonConstructors() {
    java.util.ArrayList<ScalarAttributeType> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new ScalarAttributeType_S());
    singleton_iterator.add(new ScalarAttributeType_N());
    singleton_iterator.add(new ScalarAttributeType_B());
    return singleton_iterator;
  }
}
