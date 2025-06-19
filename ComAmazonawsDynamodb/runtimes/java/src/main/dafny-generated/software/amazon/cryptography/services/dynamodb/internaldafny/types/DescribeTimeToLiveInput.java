// Class DescribeTimeToLiveInput
// Dafny class DescribeTimeToLiveInput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class DescribeTimeToLiveInput {
  public dafny.DafnySequence<? extends Character> _TableName;
  public DescribeTimeToLiveInput (dafny.DafnySequence<? extends Character> TableName) {
    this._TableName = TableName;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DescribeTimeToLiveInput o = (DescribeTimeToLiveInput)other;
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
    s.append("ComAmazonawsDynamodbTypes.DescribeTimeToLiveInput.DescribeTimeToLiveInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._TableName));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DescribeTimeToLiveInput> _TYPE = dafny.TypeDescriptor.<DescribeTimeToLiveInput>referenceWithInitializer(DescribeTimeToLiveInput.class, () -> DescribeTimeToLiveInput.Default());
  public static dafny.TypeDescriptor<DescribeTimeToLiveInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<DescribeTimeToLiveInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DescribeTimeToLiveInput theDefault = DescribeTimeToLiveInput.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static DescribeTimeToLiveInput Default() {
    return theDefault;
  }
  public static DescribeTimeToLiveInput create(dafny.DafnySequence<? extends Character> TableName) {
    return new DescribeTimeToLiveInput(TableName);
  }
  public static DescribeTimeToLiveInput create_DescribeTimeToLiveInput(dafny.DafnySequence<? extends Character> TableName) {
    return create(TableName);
  }
  public boolean is_DescribeTimeToLiveInput() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_TableName() {
    return this._TableName;
  }
}
