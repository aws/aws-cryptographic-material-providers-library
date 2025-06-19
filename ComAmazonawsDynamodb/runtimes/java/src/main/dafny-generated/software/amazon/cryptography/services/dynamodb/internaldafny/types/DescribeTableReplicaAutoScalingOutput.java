// Class DescribeTableReplicaAutoScalingOutput
// Dafny class DescribeTableReplicaAutoScalingOutput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class DescribeTableReplicaAutoScalingOutput {
  public Wrappers_Compile.Option<TableAutoScalingDescription> _TableAutoScalingDescription;
  public DescribeTableReplicaAutoScalingOutput (Wrappers_Compile.Option<TableAutoScalingDescription> TableAutoScalingDescription) {
    this._TableAutoScalingDescription = TableAutoScalingDescription;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DescribeTableReplicaAutoScalingOutput o = (DescribeTableReplicaAutoScalingOutput)other;
    return true && java.util.Objects.equals(this._TableAutoScalingDescription, o._TableAutoScalingDescription);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableAutoScalingDescription);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.DescribeTableReplicaAutoScalingOutput.DescribeTableReplicaAutoScalingOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._TableAutoScalingDescription));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DescribeTableReplicaAutoScalingOutput> _TYPE = dafny.TypeDescriptor.<DescribeTableReplicaAutoScalingOutput>referenceWithInitializer(DescribeTableReplicaAutoScalingOutput.class, () -> DescribeTableReplicaAutoScalingOutput.Default());
  public static dafny.TypeDescriptor<DescribeTableReplicaAutoScalingOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<DescribeTableReplicaAutoScalingOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DescribeTableReplicaAutoScalingOutput theDefault = DescribeTableReplicaAutoScalingOutput.create(Wrappers_Compile.Option.<TableAutoScalingDescription>Default(TableAutoScalingDescription._typeDescriptor()));
  public static DescribeTableReplicaAutoScalingOutput Default() {
    return theDefault;
  }
  public static DescribeTableReplicaAutoScalingOutput create(Wrappers_Compile.Option<TableAutoScalingDescription> TableAutoScalingDescription) {
    return new DescribeTableReplicaAutoScalingOutput(TableAutoScalingDescription);
  }
  public static DescribeTableReplicaAutoScalingOutput create_DescribeTableReplicaAutoScalingOutput(Wrappers_Compile.Option<TableAutoScalingDescription> TableAutoScalingDescription) {
    return create(TableAutoScalingDescription);
  }
  public boolean is_DescribeTableReplicaAutoScalingOutput() { return true; }
  public Wrappers_Compile.Option<TableAutoScalingDescription> dtor_TableAutoScalingDescription() {
    return this._TableAutoScalingDescription;
  }
}
