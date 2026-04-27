// Class DescribeGlobalTableOutput
// Dafny class DescribeGlobalTableOutput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class DescribeGlobalTableOutput {
  public Wrappers_Compile.Option<GlobalTableDescription> _GlobalTableDescription;
  public DescribeGlobalTableOutput (Wrappers_Compile.Option<GlobalTableDescription> GlobalTableDescription) {
    this._GlobalTableDescription = GlobalTableDescription;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DescribeGlobalTableOutput o = (DescribeGlobalTableOutput)other;
    return true && java.util.Objects.equals(this._GlobalTableDescription, o._GlobalTableDescription);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._GlobalTableDescription);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.DescribeGlobalTableOutput.DescribeGlobalTableOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._GlobalTableDescription));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DescribeGlobalTableOutput> _TYPE = dafny.TypeDescriptor.<DescribeGlobalTableOutput>referenceWithInitializer(DescribeGlobalTableOutput.class, () -> DescribeGlobalTableOutput.Default());
  public static dafny.TypeDescriptor<DescribeGlobalTableOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<DescribeGlobalTableOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DescribeGlobalTableOutput theDefault = DescribeGlobalTableOutput.create(Wrappers_Compile.Option.<GlobalTableDescription>Default(GlobalTableDescription._typeDescriptor()));
  public static DescribeGlobalTableOutput Default() {
    return theDefault;
  }
  public static DescribeGlobalTableOutput create(Wrappers_Compile.Option<GlobalTableDescription> GlobalTableDescription) {
    return new DescribeGlobalTableOutput(GlobalTableDescription);
  }
  public static DescribeGlobalTableOutput create_DescribeGlobalTableOutput(Wrappers_Compile.Option<GlobalTableDescription> GlobalTableDescription) {
    return create(GlobalTableDescription);
  }
  public boolean is_DescribeGlobalTableOutput() { return true; }
  public Wrappers_Compile.Option<GlobalTableDescription> dtor_GlobalTableDescription() {
    return this._GlobalTableDescription;
  }
}
