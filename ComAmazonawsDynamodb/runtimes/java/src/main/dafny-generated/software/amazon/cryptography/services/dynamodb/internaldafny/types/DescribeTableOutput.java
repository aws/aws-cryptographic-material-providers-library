// Class DescribeTableOutput
// Dafny class DescribeTableOutput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class DescribeTableOutput {
  public Wrappers_Compile.Option<TableDescription> _Table;
  public DescribeTableOutput (Wrappers_Compile.Option<TableDescription> Table) {
    this._Table = Table;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DescribeTableOutput o = (DescribeTableOutput)other;
    return true && java.util.Objects.equals(this._Table, o._Table);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Table);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.DescribeTableOutput.DescribeTableOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Table));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DescribeTableOutput> _TYPE = dafny.TypeDescriptor.<DescribeTableOutput>referenceWithInitializer(DescribeTableOutput.class, () -> DescribeTableOutput.Default());
  public static dafny.TypeDescriptor<DescribeTableOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<DescribeTableOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DescribeTableOutput theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.DescribeTableOutput.create(Wrappers_Compile.Option.<TableDescription>Default(TableDescription._typeDescriptor()));
  public static DescribeTableOutput Default() {
    return theDefault;
  }
  public static DescribeTableOutput create(Wrappers_Compile.Option<TableDescription> Table) {
    return new DescribeTableOutput(Table);
  }
  public static DescribeTableOutput create_DescribeTableOutput(Wrappers_Compile.Option<TableDescription> Table) {
    return create(Table);
  }
  public boolean is_DescribeTableOutput() { return true; }
  public Wrappers_Compile.Option<TableDescription> dtor_Table() {
    return this._Table;
  }
}
