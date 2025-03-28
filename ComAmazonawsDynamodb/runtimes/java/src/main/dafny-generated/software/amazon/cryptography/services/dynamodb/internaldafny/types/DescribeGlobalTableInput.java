// Class DescribeGlobalTableInput
// Dafny class DescribeGlobalTableInput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class DescribeGlobalTableInput {
  public dafny.DafnySequence<? extends Character> _GlobalTableName;
  public DescribeGlobalTableInput (dafny.DafnySequence<? extends Character> GlobalTableName) {
    this._GlobalTableName = GlobalTableName;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DescribeGlobalTableInput o = (DescribeGlobalTableInput)other;
    return true && java.util.Objects.equals(this._GlobalTableName, o._GlobalTableName);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._GlobalTableName);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.DescribeGlobalTableInput.DescribeGlobalTableInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._GlobalTableName));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DescribeGlobalTableInput> _TYPE = dafny.TypeDescriptor.<DescribeGlobalTableInput>referenceWithInitializer(DescribeGlobalTableInput.class, () -> DescribeGlobalTableInput.Default());
  public static dafny.TypeDescriptor<DescribeGlobalTableInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<DescribeGlobalTableInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DescribeGlobalTableInput theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.DescribeGlobalTableInput.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static DescribeGlobalTableInput Default() {
    return theDefault;
  }
  public static DescribeGlobalTableInput create(dafny.DafnySequence<? extends Character> GlobalTableName) {
    return new DescribeGlobalTableInput(GlobalTableName);
  }
  public static DescribeGlobalTableInput create_DescribeGlobalTableInput(dafny.DafnySequence<? extends Character> GlobalTableName) {
    return create(GlobalTableName);
  }
  public boolean is_DescribeGlobalTableInput() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_GlobalTableName() {
    return this._GlobalTableName;
  }
}
