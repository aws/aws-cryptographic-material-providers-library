// Class DescribeTableInput
// Dafny class DescribeTableInput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class DescribeTableInput {
  public dafny.DafnySequence<? extends Character> _TableName;
  public DescribeTableInput (dafny.DafnySequence<? extends Character> TableName) {
    this._TableName = TableName;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DescribeTableInput o = (DescribeTableInput)other;
    return true && java.util.Objects.equals(this._TableName, o._TableName);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableName);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.DescribeTableInput.DescribeTableInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._TableName));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DescribeTableInput> _TYPE = dafny.TypeDescriptor.<DescribeTableInput>referenceWithInitializer(DescribeTableInput.class, () -> DescribeTableInput.Default());
  public static dafny.TypeDescriptor<DescribeTableInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<DescribeTableInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DescribeTableInput theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.DescribeTableInput.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static DescribeTableInput Default() {
    return theDefault;
  }
  public static DescribeTableInput create(dafny.DafnySequence<? extends Character> TableName) {
    return new DescribeTableInput(TableName);
  }
  public static DescribeTableInput create_DescribeTableInput(dafny.DafnySequence<? extends Character> TableName) {
    return create(TableName);
  }
  public boolean is_DescribeTableInput() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_TableName() {
    return this._TableName;
  }
}
