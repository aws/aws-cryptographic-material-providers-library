// Class ExportType
// Dafny class ExportType compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class ExportType {
  public ExportType() {
  }
  private static final dafny.TypeDescriptor<ExportType> _TYPE = dafny.TypeDescriptor.<ExportType>referenceWithInitializer(ExportType.class, () -> ExportType.Default());
  public static dafny.TypeDescriptor<ExportType> _typeDescriptor() {
    return (dafny.TypeDescriptor<ExportType>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ExportType theDefault = ExportType.create_FULL__EXPORT();
  public static ExportType Default() {
    return theDefault;
  }
  public static ExportType create_FULL__EXPORT() {
    return new ExportType_FULL__EXPORT();
  }
  public static ExportType create_INCREMENTAL__EXPORT() {
    return new ExportType_INCREMENTAL__EXPORT();
  }
  public boolean is_FULL__EXPORT() { return this instanceof ExportType_FULL__EXPORT; }
  public boolean is_INCREMENTAL__EXPORT() { return this instanceof ExportType_INCREMENTAL__EXPORT; }
  public static java.util.ArrayList<ExportType> AllSingletonConstructors() {
    java.util.ArrayList<ExportType> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new ExportType_FULL__EXPORT());
    singleton_iterator.add(new ExportType_INCREMENTAL__EXPORT());
    return singleton_iterator;
  }
}
