// Class ExportTableToPointInTimeOutput
// Dafny class ExportTableToPointInTimeOutput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ExportTableToPointInTimeOutput {
  public Wrappers_Compile.Option<ExportDescription> _ExportDescription;
  public ExportTableToPointInTimeOutput (Wrappers_Compile.Option<ExportDescription> ExportDescription) {
    this._ExportDescription = ExportDescription;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ExportTableToPointInTimeOutput o = (ExportTableToPointInTimeOutput)other;
    return true && java.util.Objects.equals(this._ExportDescription, o._ExportDescription);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ExportDescription);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ExportTableToPointInTimeOutput.ExportTableToPointInTimeOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._ExportDescription));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ExportTableToPointInTimeOutput> _TYPE = dafny.TypeDescriptor.<ExportTableToPointInTimeOutput>referenceWithInitializer(ExportTableToPointInTimeOutput.class, () -> ExportTableToPointInTimeOutput.Default());
  public static dafny.TypeDescriptor<ExportTableToPointInTimeOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<ExportTableToPointInTimeOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ExportTableToPointInTimeOutput theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.ExportTableToPointInTimeOutput.create(Wrappers_Compile.Option.<ExportDescription>Default(ExportDescription._typeDescriptor()));
  public static ExportTableToPointInTimeOutput Default() {
    return theDefault;
  }
  public static ExportTableToPointInTimeOutput create(Wrappers_Compile.Option<ExportDescription> ExportDescription) {
    return new ExportTableToPointInTimeOutput(ExportDescription);
  }
  public static ExportTableToPointInTimeOutput create_ExportTableToPointInTimeOutput(Wrappers_Compile.Option<ExportDescription> ExportDescription) {
    return create(ExportDescription);
  }
  public boolean is_ExportTableToPointInTimeOutput() { return true; }
  public Wrappers_Compile.Option<ExportDescription> dtor_ExportDescription() {
    return this._ExportDescription;
  }
}
