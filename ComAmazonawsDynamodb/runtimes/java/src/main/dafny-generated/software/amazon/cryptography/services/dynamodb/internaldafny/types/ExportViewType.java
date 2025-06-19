// Class ExportViewType
// Dafny class ExportViewType compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public abstract class ExportViewType {
  public ExportViewType() {
  }
  private static final dafny.TypeDescriptor<ExportViewType> _TYPE = dafny.TypeDescriptor.<ExportViewType>referenceWithInitializer(ExportViewType.class, () -> ExportViewType.Default());
  public static dafny.TypeDescriptor<ExportViewType> _typeDescriptor() {
    return (dafny.TypeDescriptor<ExportViewType>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ExportViewType theDefault = ExportViewType.create_NEW__IMAGE();
  public static ExportViewType Default() {
    return theDefault;
  }
  public static ExportViewType create_NEW__IMAGE() {
    return new ExportViewType_NEW__IMAGE();
  }
  public static ExportViewType create_NEW__AND__OLD__IMAGES() {
    return new ExportViewType_NEW__AND__OLD__IMAGES();
  }
  public boolean is_NEW__IMAGE() { return this instanceof ExportViewType_NEW__IMAGE; }
  public boolean is_NEW__AND__OLD__IMAGES() { return this instanceof ExportViewType_NEW__AND__OLD__IMAGES; }
  public static java.util.ArrayList<ExportViewType> AllSingletonConstructors() {
    java.util.ArrayList<ExportViewType> singleton_iterator = new java.util.ArrayList<>();
    singleton_iterator.add(new ExportViewType_NEW__IMAGE());
    singleton_iterator.add(new ExportViewType_NEW__AND__OLD__IMAGES());
    return singleton_iterator;
  }
}
