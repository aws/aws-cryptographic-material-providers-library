// Class UpdateTableReplicaAutoScalingInput
// Dafny class UpdateTableReplicaAutoScalingInput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class UpdateTableReplicaAutoScalingInput {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends GlobalSecondaryIndexAutoScalingUpdate>> _GlobalSecondaryIndexUpdates;
  public dafny.DafnySequence<? extends Character> _TableName;
  public Wrappers_Compile.Option<AutoScalingSettingsUpdate> _ProvisionedWriteCapacityAutoScalingUpdate;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaAutoScalingUpdate>> _ReplicaUpdates;
  public UpdateTableReplicaAutoScalingInput (Wrappers_Compile.Option<dafny.DafnySequence<? extends GlobalSecondaryIndexAutoScalingUpdate>> GlobalSecondaryIndexUpdates, dafny.DafnySequence<? extends Character> TableName, Wrappers_Compile.Option<AutoScalingSettingsUpdate> ProvisionedWriteCapacityAutoScalingUpdate, Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaAutoScalingUpdate>> ReplicaUpdates) {
    this._GlobalSecondaryIndexUpdates = GlobalSecondaryIndexUpdates;
    this._TableName = TableName;
    this._ProvisionedWriteCapacityAutoScalingUpdate = ProvisionedWriteCapacityAutoScalingUpdate;
    this._ReplicaUpdates = ReplicaUpdates;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    UpdateTableReplicaAutoScalingInput o = (UpdateTableReplicaAutoScalingInput)other;
    return true && java.util.Objects.equals(this._GlobalSecondaryIndexUpdates, o._GlobalSecondaryIndexUpdates) && java.util.Objects.equals(this._TableName, o._TableName) && java.util.Objects.equals(this._ProvisionedWriteCapacityAutoScalingUpdate, o._ProvisionedWriteCapacityAutoScalingUpdate) && java.util.Objects.equals(this._ReplicaUpdates, o._ReplicaUpdates);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._GlobalSecondaryIndexUpdates);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ProvisionedWriteCapacityAutoScalingUpdate);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReplicaUpdates);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.UpdateTableReplicaAutoScalingInput.UpdateTableReplicaAutoScalingInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._GlobalSecondaryIndexUpdates));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._TableName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ProvisionedWriteCapacityAutoScalingUpdate));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ReplicaUpdates));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<UpdateTableReplicaAutoScalingInput> _TYPE = dafny.TypeDescriptor.<UpdateTableReplicaAutoScalingInput>referenceWithInitializer(UpdateTableReplicaAutoScalingInput.class, () -> UpdateTableReplicaAutoScalingInput.Default());
  public static dafny.TypeDescriptor<UpdateTableReplicaAutoScalingInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<UpdateTableReplicaAutoScalingInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final UpdateTableReplicaAutoScalingInput theDefault = UpdateTableReplicaAutoScalingInput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends GlobalSecondaryIndexAutoScalingUpdate>>Default(GlobalSecondaryIndexAutoScalingUpdateList._typeDescriptor()), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<AutoScalingSettingsUpdate>Default(AutoScalingSettingsUpdate._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends ReplicaAutoScalingUpdate>>Default(ReplicaAutoScalingUpdateList._typeDescriptor()));
  public static UpdateTableReplicaAutoScalingInput Default() {
    return theDefault;
  }
  public static UpdateTableReplicaAutoScalingInput create(Wrappers_Compile.Option<dafny.DafnySequence<? extends GlobalSecondaryIndexAutoScalingUpdate>> GlobalSecondaryIndexUpdates, dafny.DafnySequence<? extends Character> TableName, Wrappers_Compile.Option<AutoScalingSettingsUpdate> ProvisionedWriteCapacityAutoScalingUpdate, Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaAutoScalingUpdate>> ReplicaUpdates) {
    return new UpdateTableReplicaAutoScalingInput(GlobalSecondaryIndexUpdates, TableName, ProvisionedWriteCapacityAutoScalingUpdate, ReplicaUpdates);
  }
  public static UpdateTableReplicaAutoScalingInput create_UpdateTableReplicaAutoScalingInput(Wrappers_Compile.Option<dafny.DafnySequence<? extends GlobalSecondaryIndexAutoScalingUpdate>> GlobalSecondaryIndexUpdates, dafny.DafnySequence<? extends Character> TableName, Wrappers_Compile.Option<AutoScalingSettingsUpdate> ProvisionedWriteCapacityAutoScalingUpdate, Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaAutoScalingUpdate>> ReplicaUpdates) {
    return create(GlobalSecondaryIndexUpdates, TableName, ProvisionedWriteCapacityAutoScalingUpdate, ReplicaUpdates);
  }
  public boolean is_UpdateTableReplicaAutoScalingInput() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends GlobalSecondaryIndexAutoScalingUpdate>> dtor_GlobalSecondaryIndexUpdates() {
    return this._GlobalSecondaryIndexUpdates;
  }
  public dafny.DafnySequence<? extends Character> dtor_TableName() {
    return this._TableName;
  }
  public Wrappers_Compile.Option<AutoScalingSettingsUpdate> dtor_ProvisionedWriteCapacityAutoScalingUpdate() {
    return this._ProvisionedWriteCapacityAutoScalingUpdate;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaAutoScalingUpdate>> dtor_ReplicaUpdates() {
    return this._ReplicaUpdates;
  }
}
