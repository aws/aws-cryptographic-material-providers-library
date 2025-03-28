// Class TableClass
// Dafny class TableClass compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public abstract class TableClass {
  public TableClass() {
  }
  private static final dafny.TypeDescriptor<TableClass> _TYPE = dafny.TypeDescriptor.<TableClass>referenceWithInitializer(TableClass.class, () -> TableClass.Default());
  public static dafny.TypeDescriptor<TableClass> _typeDescriptor() {
    return (dafny.TypeDescriptor<TableClass>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final TableClass theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.TableClass.create_STANDARD();
  public static TableClass Default() {
    return theDefault;
  }
  public static TableClass create_STANDARD() {
    return new TableClass_STANDARD();
  }
  public static TableClass create_STANDARD__INFREQUENT__ACCESS() {
    return new TableClass_STANDARD__INFREQUENT__ACCESS();
  }
  public boolean is_STANDARD() { return this instanceof TableClass_STANDARD; }
  public boolean is_STANDARD__INFREQUENT__ACCESS() { return this instanceof TableClass_STANDARD__INFREQUENT__ACCESS; }
  public static java.util.ArrayList<TableClass> AllSingletonConstructors() {
    java.util.ArrayList<TableClass> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new TableClass_STANDARD());
    singleton_iterator.add(new TableClass_STANDARD__INFREQUENT__ACCESS());
    return singleton_iterator;
  }
}
