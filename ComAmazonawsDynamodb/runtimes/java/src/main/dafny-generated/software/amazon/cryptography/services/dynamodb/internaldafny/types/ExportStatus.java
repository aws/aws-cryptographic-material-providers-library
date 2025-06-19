// Class ExportStatus
// Dafny class ExportStatus compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class ExportStatus {
  public ExportStatus() {
  }
  private static final dafny.TypeDescriptor<ExportStatus> _TYPE = dafny.TypeDescriptor.<ExportStatus>referenceWithInitializer(ExportStatus.class, () -> ExportStatus.Default());
  public static dafny.TypeDescriptor<ExportStatus> _typeDescriptor() {
    return (dafny.TypeDescriptor<ExportStatus>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ExportStatus theDefault = ExportStatus.create_IN__PROGRESS();
  public static ExportStatus Default() {
    return theDefault;
  }
  public static ExportStatus create_IN__PROGRESS() {
    return new ExportStatus_IN__PROGRESS();
  }
  public static ExportStatus create_COMPLETED() {
    return new ExportStatus_COMPLETED();
  }
  public static ExportStatus create_FAILED() {
    return new ExportStatus_FAILED();
  }
  public boolean is_IN__PROGRESS() { return this instanceof ExportStatus_IN__PROGRESS; }
  public boolean is_COMPLETED() { return this instanceof ExportStatus_COMPLETED; }
  public boolean is_FAILED() { return this instanceof ExportStatus_FAILED; }
  public static java.util.ArrayList<ExportStatus> AllSingletonConstructors() {
    java.util.ArrayList<ExportStatus> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new ExportStatus_IN__PROGRESS());
    singleton_iterator.add(new ExportStatus_COMPLETED());
    singleton_iterator.add(new ExportStatus_FAILED());
    return singleton_iterator;
  }
}
