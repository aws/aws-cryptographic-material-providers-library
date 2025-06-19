// Class ExportSummary
// Dafny class ExportSummary compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ExportSummary {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _ExportArn;
  public Wrappers_Compile.Option<ExportStatus> _ExportStatus;
  public Wrappers_Compile.Option<ExportType> _ExportType;
  public ExportSummary (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ExportArn, Wrappers_Compile.Option<ExportStatus> ExportStatus, Wrappers_Compile.Option<ExportType> ExportType) {
    this._ExportArn = ExportArn;
    this._ExportStatus = ExportStatus;
    this._ExportType = ExportType;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ExportSummary o = (ExportSummary)other;
    return true && java.util.Objects.equals(this._ExportArn, o._ExportArn) && java.util.Objects.equals(this._ExportStatus, o._ExportStatus) && java.util.Objects.equals(this._ExportType, o._ExportType);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ExportArn);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ExportStatus);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ExportType);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ExportSummary.ExportSummary");
    s.append("(");
    s.append(dafny.Helpers.toString(this._ExportArn));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ExportStatus));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ExportType));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ExportSummary> _TYPE = dafny.TypeDescriptor.<ExportSummary>referenceWithInitializer(ExportSummary.class, () -> ExportSummary.Default());
  public static dafny.TypeDescriptor<ExportSummary> _typeDescriptor() {
    return (dafny.TypeDescriptor<ExportSummary>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ExportSummary theDefault = ExportSummary.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(ExportArn._typeDescriptor()), Wrappers_Compile.Option.<ExportStatus>Default(ExportStatus._typeDescriptor()), Wrappers_Compile.Option.<ExportType>Default(ExportType._typeDescriptor()));
  public static ExportSummary Default() {
    return theDefault;
  }
  public static ExportSummary create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ExportArn, Wrappers_Compile.Option<ExportStatus> ExportStatus, Wrappers_Compile.Option<ExportType> ExportType) {
    return new ExportSummary(ExportArn, ExportStatus, ExportType);
  }
  public static ExportSummary create_ExportSummary(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ExportArn, Wrappers_Compile.Option<ExportStatus> ExportStatus, Wrappers_Compile.Option<ExportType> ExportType) {
    return create(ExportArn, ExportStatus, ExportType);
  }
  public boolean is_ExportSummary() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_ExportArn() {
    return this._ExportArn;
  }
  public Wrappers_Compile.Option<ExportStatus> dtor_ExportStatus() {
    return this._ExportStatus;
  }
  public Wrappers_Compile.Option<ExportType> dtor_ExportType() {
    return this._ExportType;
  }
}
