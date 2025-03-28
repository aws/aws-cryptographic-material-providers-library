// Class BackupStatus
// Dafny class BackupStatus compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public abstract class BackupStatus {
  public BackupStatus() {
  }
  private static final dafny.TypeDescriptor<BackupStatus> _TYPE = dafny.TypeDescriptor.<BackupStatus>referenceWithInitializer(BackupStatus.class, () -> BackupStatus.Default());
  public static dafny.TypeDescriptor<BackupStatus> _typeDescriptor() {
    return (dafny.TypeDescriptor<BackupStatus>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final BackupStatus theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.BackupStatus.create_CREATING();
  public static BackupStatus Default() {
    return theDefault;
  }
  public static BackupStatus create_CREATING() {
    return new BackupStatus_CREATING();
  }
  public static BackupStatus create_DELETED() {
    return new BackupStatus_DELETED();
  }
  public static BackupStatus create_AVAILABLE() {
    return new BackupStatus_AVAILABLE();
  }
  public boolean is_CREATING() { return this instanceof BackupStatus_CREATING; }
  public boolean is_DELETED() { return this instanceof BackupStatus_DELETED; }
  public boolean is_AVAILABLE() { return this instanceof BackupStatus_AVAILABLE; }
  public static java.util.ArrayList<BackupStatus> AllSingletonConstructors() {
    java.util.ArrayList<BackupStatus> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new BackupStatus_CREATING());
    singleton_iterator.add(new BackupStatus_DELETED());
    singleton_iterator.add(new BackupStatus_AVAILABLE());
    return singleton_iterator;
  }
}
