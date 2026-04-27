// Class ReplicaAutoScalingUpdate
// Dafny class ReplicaAutoScalingUpdate compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ReplicaAutoScalingUpdate {
  public dafny.DafnySequence<? extends Character> _RegionName;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaGlobalSecondaryIndexAutoScalingUpdate>> _ReplicaGlobalSecondaryIndexUpdates;
  public Wrappers_Compile.Option<AutoScalingSettingsUpdate> _ReplicaProvisionedReadCapacityAutoScalingUpdate;
  public ReplicaAutoScalingUpdate (dafny.DafnySequence<? extends Character> RegionName, Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaGlobalSecondaryIndexAutoScalingUpdate>> ReplicaGlobalSecondaryIndexUpdates, Wrappers_Compile.Option<AutoScalingSettingsUpdate> ReplicaProvisionedReadCapacityAutoScalingUpdate) {
    this._RegionName = RegionName;
    this._ReplicaGlobalSecondaryIndexUpdates = ReplicaGlobalSecondaryIndexUpdates;
    this._ReplicaProvisionedReadCapacityAutoScalingUpdate = ReplicaProvisionedReadCapacityAutoScalingUpdate;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ReplicaAutoScalingUpdate o = (ReplicaAutoScalingUpdate)other;
    return true && java.util.Objects.equals(this._RegionName, o._RegionName) && java.util.Objects.equals(this._ReplicaGlobalSecondaryIndexUpdates, o._ReplicaGlobalSecondaryIndexUpdates) && java.util.Objects.equals(this._ReplicaProvisionedReadCapacityAutoScalingUpdate, o._ReplicaProvisionedReadCapacityAutoScalingUpdate);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._RegionName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReplicaGlobalSecondaryIndexUpdates);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReplicaProvisionedReadCapacityAutoScalingUpdate);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ReplicaAutoScalingUpdate.ReplicaAutoScalingUpdate");
    s.append("(");
    s.append(dafny.Helpers.toString(this._RegionName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ReplicaGlobalSecondaryIndexUpdates));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ReplicaProvisionedReadCapacityAutoScalingUpdate));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ReplicaAutoScalingUpdate> _TYPE = dafny.TypeDescriptor.<ReplicaAutoScalingUpdate>referenceWithInitializer(ReplicaAutoScalingUpdate.class, () -> ReplicaAutoScalingUpdate.Default());
  public static dafny.TypeDescriptor<ReplicaAutoScalingUpdate> _typeDescriptor() {
    return (dafny.TypeDescriptor<ReplicaAutoScalingUpdate>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ReplicaAutoScalingUpdate theDefault = ReplicaAutoScalingUpdate.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<dafny.DafnySequence<? extends ReplicaGlobalSecondaryIndexAutoScalingUpdate>>Default(dafny.DafnySequence.<ReplicaGlobalSecondaryIndexAutoScalingUpdate>_typeDescriptor(ReplicaGlobalSecondaryIndexAutoScalingUpdate._typeDescriptor())), Wrappers_Compile.Option.<AutoScalingSettingsUpdate>Default(AutoScalingSettingsUpdate._typeDescriptor()));
  public static ReplicaAutoScalingUpdate Default() {
    return theDefault;
  }
  public static ReplicaAutoScalingUpdate create(dafny.DafnySequence<? extends Character> RegionName, Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaGlobalSecondaryIndexAutoScalingUpdate>> ReplicaGlobalSecondaryIndexUpdates, Wrappers_Compile.Option<AutoScalingSettingsUpdate> ReplicaProvisionedReadCapacityAutoScalingUpdate) {
    return new ReplicaAutoScalingUpdate(RegionName, ReplicaGlobalSecondaryIndexUpdates, ReplicaProvisionedReadCapacityAutoScalingUpdate);
  }
  public static ReplicaAutoScalingUpdate create_ReplicaAutoScalingUpdate(dafny.DafnySequence<? extends Character> RegionName, Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaGlobalSecondaryIndexAutoScalingUpdate>> ReplicaGlobalSecondaryIndexUpdates, Wrappers_Compile.Option<AutoScalingSettingsUpdate> ReplicaProvisionedReadCapacityAutoScalingUpdate) {
    return create(RegionName, ReplicaGlobalSecondaryIndexUpdates, ReplicaProvisionedReadCapacityAutoScalingUpdate);
  }
  public boolean is_ReplicaAutoScalingUpdate() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_RegionName() {
    return this._RegionName;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaGlobalSecondaryIndexAutoScalingUpdate>> dtor_ReplicaGlobalSecondaryIndexUpdates() {
    return this._ReplicaGlobalSecondaryIndexUpdates;
  }
  public Wrappers_Compile.Option<AutoScalingSettingsUpdate> dtor_ReplicaProvisionedReadCapacityAutoScalingUpdate() {
    return this._ReplicaProvisionedReadCapacityAutoScalingUpdate;
  }
}
