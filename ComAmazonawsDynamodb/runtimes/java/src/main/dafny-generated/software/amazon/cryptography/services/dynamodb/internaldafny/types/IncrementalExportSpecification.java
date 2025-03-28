// Class IncrementalExportSpecification
// Dafny class IncrementalExportSpecification compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class IncrementalExportSpecification {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _ExportFromTime;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _ExportToTime;
  public Wrappers_Compile.Option<ExportViewType> _ExportViewType;
  public IncrementalExportSpecification (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ExportFromTime, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ExportToTime, Wrappers_Compile.Option<ExportViewType> ExportViewType) {
    this._ExportFromTime = ExportFromTime;
    this._ExportToTime = ExportToTime;
    this._ExportViewType = ExportViewType;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    IncrementalExportSpecification o = (IncrementalExportSpecification)other;
    return true && java.util.Objects.equals(this._ExportFromTime, o._ExportFromTime) && java.util.Objects.equals(this._ExportToTime, o._ExportToTime) && java.util.Objects.equals(this._ExportViewType, o._ExportViewType);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ExportFromTime);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ExportToTime);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ExportViewType);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.IncrementalExportSpecification.IncrementalExportSpecification");
    s.append("(");
    s.append(dafny.Helpers.toString(this._ExportFromTime));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ExportToTime));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ExportViewType));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<IncrementalExportSpecification> _TYPE = dafny.TypeDescriptor.<IncrementalExportSpecification>referenceWithInitializer(IncrementalExportSpecification.class, () -> IncrementalExportSpecification.Default());
  public static dafny.TypeDescriptor<IncrementalExportSpecification> _typeDescriptor() {
    return (dafny.TypeDescriptor<IncrementalExportSpecification>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final IncrementalExportSpecification theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.IncrementalExportSpecification.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<ExportViewType>Default(ExportViewType._typeDescriptor()));
  public static IncrementalExportSpecification Default() {
    return theDefault;
  }
  public static IncrementalExportSpecification create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ExportFromTime, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ExportToTime, Wrappers_Compile.Option<ExportViewType> ExportViewType) {
    return new IncrementalExportSpecification(ExportFromTime, ExportToTime, ExportViewType);
  }
  public static IncrementalExportSpecification create_IncrementalExportSpecification(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ExportFromTime, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ExportToTime, Wrappers_Compile.Option<ExportViewType> ExportViewType) {
    return create(ExportFromTime, ExportToTime, ExportViewType);
  }
  public boolean is_IncrementalExportSpecification() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_ExportFromTime() {
    return this._ExportFromTime;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_ExportToTime() {
    return this._ExportToTime;
  }
  public Wrappers_Compile.Option<ExportViewType> dtor_ExportViewType() {
    return this._ExportViewType;
  }
}
