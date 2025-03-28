// Class DescribeImportOutput
// Dafny class DescribeImportOutput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class DescribeImportOutput {
  public ImportTableDescription _ImportTableDescription;
  public DescribeImportOutput (ImportTableDescription ImportTableDescription) {
    this._ImportTableDescription = ImportTableDescription;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DescribeImportOutput o = (DescribeImportOutput)other;
    return true && java.util.Objects.equals(this._ImportTableDescription, o._ImportTableDescription);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ImportTableDescription);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.DescribeImportOutput.DescribeImportOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._ImportTableDescription));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DescribeImportOutput> _TYPE = dafny.TypeDescriptor.<DescribeImportOutput>referenceWithInitializer(DescribeImportOutput.class, () -> DescribeImportOutput.Default());
  public static dafny.TypeDescriptor<DescribeImportOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<DescribeImportOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DescribeImportOutput theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.DescribeImportOutput.create(ImportTableDescription.Default());
  public static DescribeImportOutput Default() {
    return theDefault;
  }
  public static DescribeImportOutput create(ImportTableDescription ImportTableDescription) {
    return new DescribeImportOutput(ImportTableDescription);
  }
  public static DescribeImportOutput create_DescribeImportOutput(ImportTableDescription ImportTableDescription) {
    return create(ImportTableDescription);
  }
  public boolean is_DescribeImportOutput() { return true; }
  public ImportTableDescription dtor_ImportTableDescription() {
    return this._ImportTableDescription;
  }
}
