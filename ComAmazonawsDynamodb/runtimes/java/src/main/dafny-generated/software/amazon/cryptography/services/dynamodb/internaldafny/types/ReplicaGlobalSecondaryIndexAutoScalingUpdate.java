// Class ReplicaGlobalSecondaryIndexAutoScalingUpdate
// Dafny class ReplicaGlobalSecondaryIndexAutoScalingUpdate compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ReplicaGlobalSecondaryIndexAutoScalingUpdate {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _IndexName;
  public Wrappers_Compile.Option<AutoScalingSettingsUpdate> _ProvisionedReadCapacityAutoScalingUpdate;
  public ReplicaGlobalSecondaryIndexAutoScalingUpdate (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> IndexName, Wrappers_Compile.Option<AutoScalingSettingsUpdate> ProvisionedReadCapacityAutoScalingUpdate) {
    this._IndexName = IndexName;
    this._ProvisionedReadCapacityAutoScalingUpdate = ProvisionedReadCapacityAutoScalingUpdate;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ReplicaGlobalSecondaryIndexAutoScalingUpdate o = (ReplicaGlobalSecondaryIndexAutoScalingUpdate)other;
    return true && java.util.Objects.equals(this._IndexName, o._IndexName) && java.util.Objects.equals(this._ProvisionedReadCapacityAutoScalingUpdate, o._ProvisionedReadCapacityAutoScalingUpdate);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._IndexName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ProvisionedReadCapacityAutoScalingUpdate);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ReplicaGlobalSecondaryIndexAutoScalingUpdate.ReplicaGlobalSecondaryIndexAutoScalingUpdate");
    s.append("(");
    s.append(dafny.Helpers.toString(this._IndexName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ProvisionedReadCapacityAutoScalingUpdate));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ReplicaGlobalSecondaryIndexAutoScalingUpdate> _TYPE = dafny.TypeDescriptor.<ReplicaGlobalSecondaryIndexAutoScalingUpdate>referenceWithInitializer(ReplicaGlobalSecondaryIndexAutoScalingUpdate.class, () -> ReplicaGlobalSecondaryIndexAutoScalingUpdate.Default());
  public static dafny.TypeDescriptor<ReplicaGlobalSecondaryIndexAutoScalingUpdate> _typeDescriptor() {
    return (dafny.TypeDescriptor<ReplicaGlobalSecondaryIndexAutoScalingUpdate>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ReplicaGlobalSecondaryIndexAutoScalingUpdate theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.ReplicaGlobalSecondaryIndexAutoScalingUpdate.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(IndexName._typeDescriptor()), Wrappers_Compile.Option.<AutoScalingSettingsUpdate>Default(AutoScalingSettingsUpdate._typeDescriptor()));
  public static ReplicaGlobalSecondaryIndexAutoScalingUpdate Default() {
    return theDefault;
  }
  public static ReplicaGlobalSecondaryIndexAutoScalingUpdate create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> IndexName, Wrappers_Compile.Option<AutoScalingSettingsUpdate> ProvisionedReadCapacityAutoScalingUpdate) {
    return new ReplicaGlobalSecondaryIndexAutoScalingUpdate(IndexName, ProvisionedReadCapacityAutoScalingUpdate);
  }
  public static ReplicaGlobalSecondaryIndexAutoScalingUpdate create_ReplicaGlobalSecondaryIndexAutoScalingUpdate(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> IndexName, Wrappers_Compile.Option<AutoScalingSettingsUpdate> ProvisionedReadCapacityAutoScalingUpdate) {
    return create(IndexName, ProvisionedReadCapacityAutoScalingUpdate);
  }
  public boolean is_ReplicaGlobalSecondaryIndexAutoScalingUpdate() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_IndexName() {
    return this._IndexName;
  }
  public Wrappers_Compile.Option<AutoScalingSettingsUpdate> dtor_ProvisionedReadCapacityAutoScalingUpdate() {
    return this._ProvisionedReadCapacityAutoScalingUpdate;
  }
}
