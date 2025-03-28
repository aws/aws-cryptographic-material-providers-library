// Class TableStatus
// Dafny class TableStatus compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public abstract class TableStatus {
  public TableStatus() {
  }
  private static final dafny.TypeDescriptor<TableStatus> _TYPE = dafny.TypeDescriptor.<TableStatus>referenceWithInitializer(TableStatus.class, () -> TableStatus.Default());
  public static dafny.TypeDescriptor<TableStatus> _typeDescriptor() {
    return (dafny.TypeDescriptor<TableStatus>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final TableStatus theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.TableStatus.create_CREATING();
  public static TableStatus Default() {
    return theDefault;
  }
  public static TableStatus create_CREATING() {
    return new TableStatus_CREATING();
  }
  public static TableStatus create_UPDATING() {
    return new TableStatus_UPDATING();
  }
  public static TableStatus create_DELETING() {
    return new TableStatus_DELETING();
  }
  public static TableStatus create_ACTIVE() {
    return new TableStatus_ACTIVE();
  }
  public static TableStatus create_INACCESSIBLE__ENCRYPTION__CREDENTIALS() {
    return new TableStatus_INACCESSIBLE__ENCRYPTION__CREDENTIALS();
  }
  public static TableStatus create_ARCHIVING() {
    return new TableStatus_ARCHIVING();
  }
  public static TableStatus create_ARCHIVED() {
    return new TableStatus_ARCHIVED();
  }
  public boolean is_CREATING() { return this instanceof TableStatus_CREATING; }
  public boolean is_UPDATING() { return this instanceof TableStatus_UPDATING; }
  public boolean is_DELETING() { return this instanceof TableStatus_DELETING; }
  public boolean is_ACTIVE() { return this instanceof TableStatus_ACTIVE; }
  public boolean is_INACCESSIBLE__ENCRYPTION__CREDENTIALS() { return this instanceof TableStatus_INACCESSIBLE__ENCRYPTION__CREDENTIALS; }
  public boolean is_ARCHIVING() { return this instanceof TableStatus_ARCHIVING; }
  public boolean is_ARCHIVED() { return this instanceof TableStatus_ARCHIVED; }
  public static java.util.ArrayList<TableStatus> AllSingletonConstructors() {
    java.util.ArrayList<TableStatus> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new TableStatus_CREATING());
    singleton_iterator.add(new TableStatus_UPDATING());
    singleton_iterator.add(new TableStatus_DELETING());
    singleton_iterator.add(new TableStatus_ACTIVE());
    singleton_iterator.add(new TableStatus_INACCESSIBLE__ENCRYPTION__CREDENTIALS());
    singleton_iterator.add(new TableStatus_ARCHIVING());
    singleton_iterator.add(new TableStatus_ARCHIVED());
    return singleton_iterator;
  }
}
