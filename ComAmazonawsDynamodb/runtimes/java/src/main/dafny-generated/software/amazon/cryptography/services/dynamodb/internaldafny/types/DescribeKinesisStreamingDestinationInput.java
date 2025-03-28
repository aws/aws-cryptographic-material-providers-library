// Class DescribeKinesisStreamingDestinationInput
// Dafny class DescribeKinesisStreamingDestinationInput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class DescribeKinesisStreamingDestinationInput {
  public dafny.DafnySequence<? extends Character> _TableName;
  public DescribeKinesisStreamingDestinationInput (dafny.DafnySequence<? extends Character> TableName) {
    this._TableName = TableName;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DescribeKinesisStreamingDestinationInput o = (DescribeKinesisStreamingDestinationInput)other;
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
    s.append("ComAmazonawsDynamodbTypes.DescribeKinesisStreamingDestinationInput.DescribeKinesisStreamingDestinationInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._TableName));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DescribeKinesisStreamingDestinationInput> _TYPE = dafny.TypeDescriptor.<DescribeKinesisStreamingDestinationInput>referenceWithInitializer(DescribeKinesisStreamingDestinationInput.class, () -> DescribeKinesisStreamingDestinationInput.Default());
  public static dafny.TypeDescriptor<DescribeKinesisStreamingDestinationInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<DescribeKinesisStreamingDestinationInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DescribeKinesisStreamingDestinationInput theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.DescribeKinesisStreamingDestinationInput.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static DescribeKinesisStreamingDestinationInput Default() {
    return theDefault;
  }
  public static DescribeKinesisStreamingDestinationInput create(dafny.DafnySequence<? extends Character> TableName) {
    return new DescribeKinesisStreamingDestinationInput(TableName);
  }
  public static DescribeKinesisStreamingDestinationInput create_DescribeKinesisStreamingDestinationInput(dafny.DafnySequence<? extends Character> TableName) {
    return create(TableName);
  }
  public boolean is_DescribeKinesisStreamingDestinationInput() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_TableName() {
    return this._TableName;
  }
}
