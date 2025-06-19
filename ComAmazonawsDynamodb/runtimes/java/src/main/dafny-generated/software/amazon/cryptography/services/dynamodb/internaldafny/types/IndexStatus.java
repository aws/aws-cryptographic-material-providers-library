// Class IndexStatus
// Dafny class IndexStatus compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class IndexStatus {
  public IndexStatus() {
  }
  private static final dafny.TypeDescriptor<IndexStatus> _TYPE = dafny.TypeDescriptor.<IndexStatus>referenceWithInitializer(IndexStatus.class, () -> IndexStatus.Default());
  public static dafny.TypeDescriptor<IndexStatus> _typeDescriptor() {
    return (dafny.TypeDescriptor<IndexStatus>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final IndexStatus theDefault = IndexStatus.create_CREATING();
  public static IndexStatus Default() {
    return theDefault;
  }
  public static IndexStatus create_CREATING() {
    return new IndexStatus_CREATING();
  }
  public static IndexStatus create_UPDATING() {
    return new IndexStatus_UPDATING();
  }
  public static IndexStatus create_DELETING() {
    return new IndexStatus_DELETING();
  }
  public static IndexStatus create_ACTIVE() {
    return new IndexStatus_ACTIVE();
  }
  public boolean is_CREATING() { return this instanceof IndexStatus_CREATING; }
  public boolean is_UPDATING() { return this instanceof IndexStatus_UPDATING; }
  public boolean is_DELETING() { return this instanceof IndexStatus_DELETING; }
  public boolean is_ACTIVE() { return this instanceof IndexStatus_ACTIVE; }
  public static java.util.ArrayList<IndexStatus> AllSingletonConstructors() {
    java.util.ArrayList<IndexStatus> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new IndexStatus_CREATING());
    singleton_iterator.add(new IndexStatus_UPDATING());
    singleton_iterator.add(new IndexStatus_DELETING());
    singleton_iterator.add(new IndexStatus_ACTIVE());
    return singleton_iterator;
  }
}
