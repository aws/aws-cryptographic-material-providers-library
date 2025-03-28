// Class BackupType
// Dafny class BackupType compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public abstract class BackupType {
  public BackupType() {
  }
  private static final dafny.TypeDescriptor<BackupType> _TYPE = dafny.TypeDescriptor.<BackupType>referenceWithInitializer(BackupType.class, () -> BackupType.Default());
  public static dafny.TypeDescriptor<BackupType> _typeDescriptor() {
    return (dafny.TypeDescriptor<BackupType>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final BackupType theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.BackupType.create_USER();
  public static BackupType Default() {
    return theDefault;
  }
  public static BackupType create_USER() {
    return new BackupType_USER();
  }
  public static BackupType create_SYSTEM() {
    return new BackupType_SYSTEM();
  }
  public static BackupType create_AWS__BACKUP() {
    return new BackupType_AWS__BACKUP();
  }
  public boolean is_USER() { return this instanceof BackupType_USER; }
  public boolean is_SYSTEM() { return this instanceof BackupType_SYSTEM; }
  public boolean is_AWS__BACKUP() { return this instanceof BackupType_AWS__BACKUP; }
  public static java.util.ArrayList<BackupType> AllSingletonConstructors() {
    java.util.ArrayList<BackupType> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new BackupType_USER());
    singleton_iterator.add(new BackupType_SYSTEM());
    singleton_iterator.add(new BackupType_AWS__BACKUP());
    return singleton_iterator;
  }
}
