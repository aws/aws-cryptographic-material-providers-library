// Class UpdateTableReplicaAutoScalingOutput
// Dafny class UpdateTableReplicaAutoScalingOutput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class UpdateTableReplicaAutoScalingOutput {
  public Wrappers_Compile.Option<TableAutoScalingDescription> _TableAutoScalingDescription;
  public UpdateTableReplicaAutoScalingOutput (Wrappers_Compile.Option<TableAutoScalingDescription> TableAutoScalingDescription) {
    this._TableAutoScalingDescription = TableAutoScalingDescription;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    UpdateTableReplicaAutoScalingOutput o = (UpdateTableReplicaAutoScalingOutput)other;
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
    s.append("ComAmazonawsDynamodbTypes.UpdateTableReplicaAutoScalingOutput.UpdateTableReplicaAutoScalingOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._TableAutoScalingDescription));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<UpdateTableReplicaAutoScalingOutput> _TYPE = dafny.TypeDescriptor.<UpdateTableReplicaAutoScalingOutput>referenceWithInitializer(UpdateTableReplicaAutoScalingOutput.class, () -> UpdateTableReplicaAutoScalingOutput.Default());
  public static dafny.TypeDescriptor<UpdateTableReplicaAutoScalingOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<UpdateTableReplicaAutoScalingOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final UpdateTableReplicaAutoScalingOutput theDefault = UpdateTableReplicaAutoScalingOutput.create(Wrappers_Compile.Option.<TableAutoScalingDescription>Default(TableAutoScalingDescription._typeDescriptor()));
  public static UpdateTableReplicaAutoScalingOutput Default() {
    return theDefault;
  }
  public static UpdateTableReplicaAutoScalingOutput create(Wrappers_Compile.Option<TableAutoScalingDescription> TableAutoScalingDescription) {
    return new UpdateTableReplicaAutoScalingOutput(TableAutoScalingDescription);
  }
  public static UpdateTableReplicaAutoScalingOutput create_UpdateTableReplicaAutoScalingOutput(Wrappers_Compile.Option<TableAutoScalingDescription> TableAutoScalingDescription) {
    return create(TableAutoScalingDescription);
  }
  public boolean is_UpdateTableReplicaAutoScalingOutput() { return true; }
  public Wrappers_Compile.Option<TableAutoScalingDescription> dtor_TableAutoScalingDescription() {
    return this._TableAutoScalingDescription;
  }
}
