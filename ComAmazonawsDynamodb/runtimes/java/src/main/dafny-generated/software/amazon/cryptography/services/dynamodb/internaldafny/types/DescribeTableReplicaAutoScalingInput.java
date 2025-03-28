// Class DescribeTableReplicaAutoScalingInput
// Dafny class DescribeTableReplicaAutoScalingInput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class DescribeTableReplicaAutoScalingInput {
  public dafny.DafnySequence<? extends Character> _TableName;
  public DescribeTableReplicaAutoScalingInput (dafny.DafnySequence<? extends Character> TableName) {
    this._TableName = TableName;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DescribeTableReplicaAutoScalingInput o = (DescribeTableReplicaAutoScalingInput)other;
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
    s.append("ComAmazonawsDynamodbTypes.DescribeTableReplicaAutoScalingInput.DescribeTableReplicaAutoScalingInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._TableName));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DescribeTableReplicaAutoScalingInput> _TYPE = dafny.TypeDescriptor.<DescribeTableReplicaAutoScalingInput>referenceWithInitializer(DescribeTableReplicaAutoScalingInput.class, () -> DescribeTableReplicaAutoScalingInput.Default());
  public static dafny.TypeDescriptor<DescribeTableReplicaAutoScalingInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<DescribeTableReplicaAutoScalingInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DescribeTableReplicaAutoScalingInput theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.DescribeTableReplicaAutoScalingInput.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static DescribeTableReplicaAutoScalingInput Default() {
    return theDefault;
  }
  public static DescribeTableReplicaAutoScalingInput create(dafny.DafnySequence<? extends Character> TableName) {
    return new DescribeTableReplicaAutoScalingInput(TableName);
  }
  public static DescribeTableReplicaAutoScalingInput create_DescribeTableReplicaAutoScalingInput(dafny.DafnySequence<? extends Character> TableName) {
    return create(TableName);
  }
  public boolean is_DescribeTableReplicaAutoScalingInput() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_TableName() {
    return this._TableName;
  }
}
