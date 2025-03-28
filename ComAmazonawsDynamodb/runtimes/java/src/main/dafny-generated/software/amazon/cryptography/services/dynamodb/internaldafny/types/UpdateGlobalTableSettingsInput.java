// Class UpdateGlobalTableSettingsInput
// Dafny class UpdateGlobalTableSettingsInput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class UpdateGlobalTableSettingsInput {
  public dafny.DafnySequence<? extends Character> _GlobalTableName;
  public Wrappers_Compile.Option<BillingMode> _GlobalTableBillingMode;
  public Wrappers_Compile.Option<java.lang.Long> _GlobalTableProvisionedWriteCapacityUnits;
  public Wrappers_Compile.Option<AutoScalingSettingsUpdate> _GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends GlobalTableGlobalSecondaryIndexSettingsUpdate>> _GlobalTableGlobalSecondaryIndexSettingsUpdate;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaSettingsUpdate>> _ReplicaSettingsUpdate;
  public UpdateGlobalTableSettingsInput (dafny.DafnySequence<? extends Character> GlobalTableName, Wrappers_Compile.Option<BillingMode> GlobalTableBillingMode, Wrappers_Compile.Option<java.lang.Long> GlobalTableProvisionedWriteCapacityUnits, Wrappers_Compile.Option<AutoScalingSettingsUpdate> GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate, Wrappers_Compile.Option<dafny.DafnySequence<? extends GlobalTableGlobalSecondaryIndexSettingsUpdate>> GlobalTableGlobalSecondaryIndexSettingsUpdate, Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaSettingsUpdate>> ReplicaSettingsUpdate) {
    this._GlobalTableName = GlobalTableName;
    this._GlobalTableBillingMode = GlobalTableBillingMode;
    this._GlobalTableProvisionedWriteCapacityUnits = GlobalTableProvisionedWriteCapacityUnits;
    this._GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate = GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate;
    this._GlobalTableGlobalSecondaryIndexSettingsUpdate = GlobalTableGlobalSecondaryIndexSettingsUpdate;
    this._ReplicaSettingsUpdate = ReplicaSettingsUpdate;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    UpdateGlobalTableSettingsInput o = (UpdateGlobalTableSettingsInput)other;
    return true && java.util.Objects.equals(this._GlobalTableName, o._GlobalTableName) && java.util.Objects.equals(this._GlobalTableBillingMode, o._GlobalTableBillingMode) && java.util.Objects.equals(this._GlobalTableProvisionedWriteCapacityUnits, o._GlobalTableProvisionedWriteCapacityUnits) && java.util.Objects.equals(this._GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate, o._GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate) && java.util.Objects.equals(this._GlobalTableGlobalSecondaryIndexSettingsUpdate, o._GlobalTableGlobalSecondaryIndexSettingsUpdate) && java.util.Objects.equals(this._ReplicaSettingsUpdate, o._ReplicaSettingsUpdate);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._GlobalTableName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._GlobalTableBillingMode);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._GlobalTableProvisionedWriteCapacityUnits);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._GlobalTableGlobalSecondaryIndexSettingsUpdate);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReplicaSettingsUpdate);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.UpdateGlobalTableSettingsInput.UpdateGlobalTableSettingsInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._GlobalTableName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._GlobalTableBillingMode));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._GlobalTableProvisionedWriteCapacityUnits));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._GlobalTableGlobalSecondaryIndexSettingsUpdate));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ReplicaSettingsUpdate));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<UpdateGlobalTableSettingsInput> _TYPE = dafny.TypeDescriptor.<UpdateGlobalTableSettingsInput>referenceWithInitializer(UpdateGlobalTableSettingsInput.class, () -> UpdateGlobalTableSettingsInput.Default());
  public static dafny.TypeDescriptor<UpdateGlobalTableSettingsInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<UpdateGlobalTableSettingsInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final UpdateGlobalTableSettingsInput theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.UpdateGlobalTableSettingsInput.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<BillingMode>Default(BillingMode._typeDescriptor()), Wrappers_Compile.Option.<java.lang.Long>Default(PositiveLongObject._typeDescriptor()), Wrappers_Compile.Option.<AutoScalingSettingsUpdate>Default(AutoScalingSettingsUpdate._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends GlobalTableGlobalSecondaryIndexSettingsUpdate>>Default(GlobalTableGlobalSecondaryIndexSettingsUpdateList._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends ReplicaSettingsUpdate>>Default(ReplicaSettingsUpdateList._typeDescriptor()));
  public static UpdateGlobalTableSettingsInput Default() {
    return theDefault;
  }
  public static UpdateGlobalTableSettingsInput create(dafny.DafnySequence<? extends Character> GlobalTableName, Wrappers_Compile.Option<BillingMode> GlobalTableBillingMode, Wrappers_Compile.Option<java.lang.Long> GlobalTableProvisionedWriteCapacityUnits, Wrappers_Compile.Option<AutoScalingSettingsUpdate> GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate, Wrappers_Compile.Option<dafny.DafnySequence<? extends GlobalTableGlobalSecondaryIndexSettingsUpdate>> GlobalTableGlobalSecondaryIndexSettingsUpdate, Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaSettingsUpdate>> ReplicaSettingsUpdate) {
    return new UpdateGlobalTableSettingsInput(GlobalTableName, GlobalTableBillingMode, GlobalTableProvisionedWriteCapacityUnits, GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate, GlobalTableGlobalSecondaryIndexSettingsUpdate, ReplicaSettingsUpdate);
  }
  public static UpdateGlobalTableSettingsInput create_UpdateGlobalTableSettingsInput(dafny.DafnySequence<? extends Character> GlobalTableName, Wrappers_Compile.Option<BillingMode> GlobalTableBillingMode, Wrappers_Compile.Option<java.lang.Long> GlobalTableProvisionedWriteCapacityUnits, Wrappers_Compile.Option<AutoScalingSettingsUpdate> GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate, Wrappers_Compile.Option<dafny.DafnySequence<? extends GlobalTableGlobalSecondaryIndexSettingsUpdate>> GlobalTableGlobalSecondaryIndexSettingsUpdate, Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaSettingsUpdate>> ReplicaSettingsUpdate) {
    return create(GlobalTableName, GlobalTableBillingMode, GlobalTableProvisionedWriteCapacityUnits, GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate, GlobalTableGlobalSecondaryIndexSettingsUpdate, ReplicaSettingsUpdate);
  }
  public boolean is_UpdateGlobalTableSettingsInput() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_GlobalTableName() {
    return this._GlobalTableName;
  }
  public Wrappers_Compile.Option<BillingMode> dtor_GlobalTableBillingMode() {
    return this._GlobalTableBillingMode;
  }
  public Wrappers_Compile.Option<java.lang.Long> dtor_GlobalTableProvisionedWriteCapacityUnits() {
    return this._GlobalTableProvisionedWriteCapacityUnits;
  }
  public Wrappers_Compile.Option<AutoScalingSettingsUpdate> dtor_GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate() {
    return this._GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends GlobalTableGlobalSecondaryIndexSettingsUpdate>> dtor_GlobalTableGlobalSecondaryIndexSettingsUpdate() {
    return this._GlobalTableGlobalSecondaryIndexSettingsUpdate;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaSettingsUpdate>> dtor_ReplicaSettingsUpdate() {
    return this._ReplicaSettingsUpdate;
  }
}
