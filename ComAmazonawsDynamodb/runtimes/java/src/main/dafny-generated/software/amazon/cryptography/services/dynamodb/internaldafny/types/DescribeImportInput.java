// Class DescribeImportInput
// Dafny class DescribeImportInput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class DescribeImportInput {
  public dafny.DafnySequence<? extends Character> _ImportArn;
  public DescribeImportInput (dafny.DafnySequence<? extends Character> ImportArn) {
    this._ImportArn = ImportArn;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DescribeImportInput o = (DescribeImportInput)other;
    return true && java.util.Objects.equals(this._ImportArn, o._ImportArn);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ImportArn);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.DescribeImportInput.DescribeImportInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._ImportArn));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DescribeImportInput> _TYPE = dafny.TypeDescriptor.<DescribeImportInput>referenceWithInitializer(DescribeImportInput.class, () -> DescribeImportInput.Default());
  public static dafny.TypeDescriptor<DescribeImportInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<DescribeImportInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DescribeImportInput theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.DescribeImportInput.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static DescribeImportInput Default() {
    return theDefault;
  }
  public static DescribeImportInput create(dafny.DafnySequence<? extends Character> ImportArn) {
    return new DescribeImportInput(ImportArn);
  }
  public static DescribeImportInput create_DescribeImportInput(dafny.DafnySequence<? extends Character> ImportArn) {
    return create(ImportArn);
  }
  public boolean is_DescribeImportInput() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_ImportArn() {
    return this._ImportArn;
  }
}
