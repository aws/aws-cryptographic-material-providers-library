// Class ReplicaGlobalSecondaryIndexSettingsUpdate
// Dafny class ReplicaGlobalSecondaryIndexSettingsUpdate compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ReplicaGlobalSecondaryIndexSettingsUpdate {
  public dafny.DafnySequence<? extends Character> _IndexName;
  public Wrappers_Compile.Option<java.lang.Long> _ProvisionedReadCapacityUnits;
  public Wrappers_Compile.Option<AutoScalingSettingsUpdate> _ProvisionedReadCapacityAutoScalingSettingsUpdate;
  public ReplicaGlobalSecondaryIndexSettingsUpdate (dafny.DafnySequence<? extends Character> IndexName, Wrappers_Compile.Option<java.lang.Long> ProvisionedReadCapacityUnits, Wrappers_Compile.Option<AutoScalingSettingsUpdate> ProvisionedReadCapacityAutoScalingSettingsUpdate) {
    this._IndexName = IndexName;
    this._ProvisionedReadCapacityUnits = ProvisionedReadCapacityUnits;
    this._ProvisionedReadCapacityAutoScalingSettingsUpdate = ProvisionedReadCapacityAutoScalingSettingsUpdate;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ReplicaGlobalSecondaryIndexSettingsUpdate o = (ReplicaGlobalSecondaryIndexSettingsUpdate)other;
    return true && java.util.Objects.equals(this._IndexName, o._IndexName) && java.util.Objects.equals(this._ProvisionedReadCapacityUnits, o._ProvisionedReadCapacityUnits) && java.util.Objects.equals(this._ProvisionedReadCapacityAutoScalingSettingsUpdate, o._ProvisionedReadCapacityAutoScalingSettingsUpdate);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._IndexName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ProvisionedReadCapacityUnits);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ProvisionedReadCapacityAutoScalingSettingsUpdate);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ReplicaGlobalSecondaryIndexSettingsUpdate.ReplicaGlobalSecondaryIndexSettingsUpdate");
    s.append("(");
    s.append(dafny.Helpers.toString(this._IndexName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ProvisionedReadCapacityUnits));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ProvisionedReadCapacityAutoScalingSettingsUpdate));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ReplicaGlobalSecondaryIndexSettingsUpdate> _TYPE = dafny.TypeDescriptor.<ReplicaGlobalSecondaryIndexSettingsUpdate>referenceWithInitializer(ReplicaGlobalSecondaryIndexSettingsUpdate.class, () -> ReplicaGlobalSecondaryIndexSettingsUpdate.Default());
  public static dafny.TypeDescriptor<ReplicaGlobalSecondaryIndexSettingsUpdate> _typeDescriptor() {
    return (dafny.TypeDescriptor<ReplicaGlobalSecondaryIndexSettingsUpdate>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ReplicaGlobalSecondaryIndexSettingsUpdate theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.ReplicaGlobalSecondaryIndexSettingsUpdate.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<java.lang.Long>Default(PositiveLongObject._typeDescriptor()), Wrappers_Compile.Option.<AutoScalingSettingsUpdate>Default(AutoScalingSettingsUpdate._typeDescriptor()));
  public static ReplicaGlobalSecondaryIndexSettingsUpdate Default() {
    return theDefault;
  }
  public static ReplicaGlobalSecondaryIndexSettingsUpdate create(dafny.DafnySequence<? extends Character> IndexName, Wrappers_Compile.Option<java.lang.Long> ProvisionedReadCapacityUnits, Wrappers_Compile.Option<AutoScalingSettingsUpdate> ProvisionedReadCapacityAutoScalingSettingsUpdate) {
    return new ReplicaGlobalSecondaryIndexSettingsUpdate(IndexName, ProvisionedReadCapacityUnits, ProvisionedReadCapacityAutoScalingSettingsUpdate);
  }
  public static ReplicaGlobalSecondaryIndexSettingsUpdate create_ReplicaGlobalSecondaryIndexSettingsUpdate(dafny.DafnySequence<? extends Character> IndexName, Wrappers_Compile.Option<java.lang.Long> ProvisionedReadCapacityUnits, Wrappers_Compile.Option<AutoScalingSettingsUpdate> ProvisionedReadCapacityAutoScalingSettingsUpdate) {
    return create(IndexName, ProvisionedReadCapacityUnits, ProvisionedReadCapacityAutoScalingSettingsUpdate);
  }
  public boolean is_ReplicaGlobalSecondaryIndexSettingsUpdate() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_IndexName() {
    return this._IndexName;
  }
  public Wrappers_Compile.Option<java.lang.Long> dtor_ProvisionedReadCapacityUnits() {
    return this._ProvisionedReadCapacityUnits;
  }
  public Wrappers_Compile.Option<AutoScalingSettingsUpdate> dtor_ProvisionedReadCapacityAutoScalingSettingsUpdate() {
    return this._ProvisionedReadCapacityAutoScalingSettingsUpdate;
  }
}
