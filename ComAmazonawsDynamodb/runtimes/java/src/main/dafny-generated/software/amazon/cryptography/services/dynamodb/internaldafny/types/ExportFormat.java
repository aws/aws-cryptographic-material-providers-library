// Class ExportFormat
// Dafny class ExportFormat compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public abstract class ExportFormat {
  public ExportFormat() {
  }
  private static final dafny.TypeDescriptor<ExportFormat> _TYPE = dafny.TypeDescriptor.<ExportFormat>referenceWithInitializer(ExportFormat.class, () -> ExportFormat.Default());
  public static dafny.TypeDescriptor<ExportFormat> _typeDescriptor() {
    return (dafny.TypeDescriptor<ExportFormat>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ExportFormat theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.ExportFormat.create_DYNAMODB__JSON();
  public static ExportFormat Default() {
    return theDefault;
  }
  public static ExportFormat create_DYNAMODB__JSON() {
    return new ExportFormat_DYNAMODB__JSON();
  }
  public static ExportFormat create_ION() {
    return new ExportFormat_ION();
  }
  public boolean is_DYNAMODB__JSON() { return this instanceof ExportFormat_DYNAMODB__JSON; }
  public boolean is_ION() { return this instanceof ExportFormat_ION; }
  public static java.util.ArrayList<ExportFormat> AllSingletonConstructors() {
    java.util.ArrayList<ExportFormat> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new ExportFormat_DYNAMODB__JSON());
    singleton_iterator.add(new ExportFormat_ION());
    return singleton_iterator;
  }
}
