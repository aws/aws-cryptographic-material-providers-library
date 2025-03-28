// Class DescribeExportOutput
// Dafny class DescribeExportOutput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class DescribeExportOutput {
  public Wrappers_Compile.Option<ExportDescription> _ExportDescription;
  public DescribeExportOutput (Wrappers_Compile.Option<ExportDescription> ExportDescription) {
    this._ExportDescription = ExportDescription;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DescribeExportOutput o = (DescribeExportOutput)other;
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
    s.append("ComAmazonawsDynamodbTypes.DescribeExportOutput.DescribeExportOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._ExportDescription));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DescribeExportOutput> _TYPE = dafny.TypeDescriptor.<DescribeExportOutput>referenceWithInitializer(DescribeExportOutput.class, () -> DescribeExportOutput.Default());
  public static dafny.TypeDescriptor<DescribeExportOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<DescribeExportOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DescribeExportOutput theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.DescribeExportOutput.create(Wrappers_Compile.Option.<ExportDescription>Default(ExportDescription._typeDescriptor()));
  public static DescribeExportOutput Default() {
    return theDefault;
  }
  public static DescribeExportOutput create(Wrappers_Compile.Option<ExportDescription> ExportDescription) {
    return new DescribeExportOutput(ExportDescription);
  }
  public static DescribeExportOutput create_DescribeExportOutput(Wrappers_Compile.Option<ExportDescription> ExportDescription) {
    return create(ExportDescription);
  }
  public boolean is_DescribeExportOutput() { return true; }
  public Wrappers_Compile.Option<ExportDescription> dtor_ExportDescription() {
    return this._ExportDescription;
  }
}
