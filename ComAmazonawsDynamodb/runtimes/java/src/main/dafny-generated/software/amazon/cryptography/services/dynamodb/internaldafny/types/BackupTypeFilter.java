// Class BackupTypeFilter
// Dafny class BackupTypeFilter compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class BackupTypeFilter {
  public BackupTypeFilter() {
  }
  private static final dafny.TypeDescriptor<BackupTypeFilter> _TYPE = dafny.TypeDescriptor.<BackupTypeFilter>referenceWithInitializer(BackupTypeFilter.class, () -> BackupTypeFilter.Default());
  public static dafny.TypeDescriptor<BackupTypeFilter> _typeDescriptor() {
    return (dafny.TypeDescriptor<BackupTypeFilter>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final BackupTypeFilter theDefault = BackupTypeFilter.create_USER();
  public static BackupTypeFilter Default() {
    return theDefault;
  }
  public static BackupTypeFilter create_USER() {
    return new BackupTypeFilter_USER();
  }
  public static BackupTypeFilter create_SYSTEM() {
    return new BackupTypeFilter_SYSTEM();
  }
  public static BackupTypeFilter create_AWS__BACKUP() {
    return new BackupTypeFilter_AWS__BACKUP();
  }
  public static BackupTypeFilter create_ALL() {
    return new BackupTypeFilter_ALL();
  }
  public boolean is_USER() { return this instanceof BackupTypeFilter_USER; }
  public boolean is_SYSTEM() { return this instanceof BackupTypeFilter_SYSTEM; }
  public boolean is_AWS__BACKUP() { return this instanceof BackupTypeFilter_AWS__BACKUP; }
  public boolean is_ALL() { return this instanceof BackupTypeFilter_ALL; }
  public static java.util.ArrayList<BackupTypeFilter> AllSingletonConstructors() {
    java.util.ArrayList<BackupTypeFilter> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new BackupTypeFilter_USER());
    singleton_iterator.add(new BackupTypeFilter_SYSTEM());
    singleton_iterator.add(new BackupTypeFilter_AWS__BACKUP());
    singleton_iterator.add(new BackupTypeFilter_ALL());
    return singleton_iterator;
  }
}
