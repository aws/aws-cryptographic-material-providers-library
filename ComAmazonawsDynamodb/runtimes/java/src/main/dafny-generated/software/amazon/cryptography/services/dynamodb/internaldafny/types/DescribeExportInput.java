// Class DescribeExportInput
// Dafny class DescribeExportInput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class DescribeExportInput {
  public dafny.DafnySequence<? extends Character> _ExportArn;
  public DescribeExportInput (dafny.DafnySequence<? extends Character> ExportArn) {
    this._ExportArn = ExportArn;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DescribeExportInput o = (DescribeExportInput)other;
    return true && java.util.Objects.equals(this._ExportArn, o._ExportArn);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ExportArn);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.DescribeExportInput.DescribeExportInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._ExportArn));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DescribeExportInput> _TYPE = dafny.TypeDescriptor.<DescribeExportInput>referenceWithInitializer(DescribeExportInput.class, () -> DescribeExportInput.Default());
  public static dafny.TypeDescriptor<DescribeExportInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<DescribeExportInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DescribeExportInput theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.DescribeExportInput.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static DescribeExportInput Default() {
    return theDefault;
  }
  public static DescribeExportInput create(dafny.DafnySequence<? extends Character> ExportArn) {
    return new DescribeExportInput(ExportArn);
  }
  public static DescribeExportInput create_DescribeExportInput(dafny.DafnySequence<? extends Character> ExportArn) {
    return create(ExportArn);
  }
  public boolean is_DescribeExportInput() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_ExportArn() {
    return this._ExportArn;
  }
}
