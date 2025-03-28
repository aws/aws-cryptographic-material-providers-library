// Class GlobalTableStatus
// Dafny class GlobalTableStatus compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public abstract class GlobalTableStatus {
  public GlobalTableStatus() {
  }
  private static final dafny.TypeDescriptor<GlobalTableStatus> _TYPE = dafny.TypeDescriptor.<GlobalTableStatus>referenceWithInitializer(GlobalTableStatus.class, () -> GlobalTableStatus.Default());
  public static dafny.TypeDescriptor<GlobalTableStatus> _typeDescriptor() {
    return (dafny.TypeDescriptor<GlobalTableStatus>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GlobalTableStatus theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.GlobalTableStatus.create_CREATING();
  public static GlobalTableStatus Default() {
    return theDefault;
  }
  public static GlobalTableStatus create_CREATING() {
    return new GlobalTableStatus_CREATING();
  }
  public static GlobalTableStatus create_ACTIVE() {
    return new GlobalTableStatus_ACTIVE();
  }
  public static GlobalTableStatus create_DELETING() {
    return new GlobalTableStatus_DELETING();
  }
  public static GlobalTableStatus create_UPDATING() {
    return new GlobalTableStatus_UPDATING();
  }
  public boolean is_CREATING() { return this instanceof GlobalTableStatus_CREATING; }
  public boolean is_ACTIVE() { return this instanceof GlobalTableStatus_ACTIVE; }
  public boolean is_DELETING() { return this instanceof GlobalTableStatus_DELETING; }
  public boolean is_UPDATING() { return this instanceof GlobalTableStatus_UPDATING; }
  public static java.util.ArrayList<GlobalTableStatus> AllSingletonConstructors() {
    java.util.ArrayList<GlobalTableStatus> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new GlobalTableStatus_CREATING());
    singleton_iterator.add(new GlobalTableStatus_ACTIVE());
    singleton_iterator.add(new GlobalTableStatus_DELETING());
    singleton_iterator.add(new GlobalTableStatus_UPDATING());
    return singleton_iterator;
  }
}
