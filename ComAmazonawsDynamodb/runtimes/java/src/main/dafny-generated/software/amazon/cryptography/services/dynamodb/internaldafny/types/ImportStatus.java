// Class ImportStatus
// Dafny class ImportStatus compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class ImportStatus {
  public ImportStatus() {
  }
  private static final dafny.TypeDescriptor<ImportStatus> _TYPE = dafny.TypeDescriptor.<ImportStatus>referenceWithInitializer(ImportStatus.class, () -> ImportStatus.Default());
  public static dafny.TypeDescriptor<ImportStatus> _typeDescriptor() {
    return (dafny.TypeDescriptor<ImportStatus>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ImportStatus theDefault = ImportStatus.create_IN__PROGRESS();
  public static ImportStatus Default() {
    return theDefault;
  }
  public static ImportStatus create_IN__PROGRESS() {
    return new ImportStatus_IN__PROGRESS();
  }
  public static ImportStatus create_COMPLETED() {
    return new ImportStatus_COMPLETED();
  }
  public static ImportStatus create_CANCELLING() {
    return new ImportStatus_CANCELLING();
  }
  public static ImportStatus create_CANCELLED() {
    return new ImportStatus_CANCELLED();
  }
  public static ImportStatus create_FAILED() {
    return new ImportStatus_FAILED();
  }
  public boolean is_IN__PROGRESS() { return this instanceof ImportStatus_IN__PROGRESS; }
  public boolean is_COMPLETED() { return this instanceof ImportStatus_COMPLETED; }
  public boolean is_CANCELLING() { return this instanceof ImportStatus_CANCELLING; }
  public boolean is_CANCELLED() { return this instanceof ImportStatus_CANCELLED; }
  public boolean is_FAILED() { return this instanceof ImportStatus_FAILED; }
  public static java.util.ArrayList<ImportStatus> AllSingletonConstructors() {
    java.util.ArrayList<ImportStatus> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new ImportStatus_IN__PROGRESS());
    singleton_iterator.add(new ImportStatus_COMPLETED());
    singleton_iterator.add(new ImportStatus_CANCELLING());
    singleton_iterator.add(new ImportStatus_CANCELLED());
    singleton_iterator.add(new ImportStatus_FAILED());
    return singleton_iterator;
  }
}
