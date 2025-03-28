// Class ReplicaSettingsUpdate
// Dafny class ReplicaSettingsUpdate compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ReplicaSettingsUpdate {
  public dafny.DafnySequence<? extends Character> _RegionName;
  public Wrappers_Compile.Option<java.lang.Long> _ReplicaProvisionedReadCapacityUnits;
  public Wrappers_Compile.Option<AutoScalingSettingsUpdate> _ReplicaProvisionedReadCapacityAutoScalingSettingsUpdate;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaGlobalSecondaryIndexSettingsUpdate>> _ReplicaGlobalSecondaryIndexSettingsUpdate;
  public Wrappers_Compile.Option<TableClass> _ReplicaTableClass;
  public ReplicaSettingsUpdate (dafny.DafnySequence<? extends Character> RegionName, Wrappers_Compile.Option<java.lang.Long> ReplicaProvisionedReadCapacityUnits, Wrappers_Compile.Option<AutoScalingSettingsUpdate> ReplicaProvisionedReadCapacityAutoScalingSettingsUpdate, Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaGlobalSecondaryIndexSettingsUpdate>> ReplicaGlobalSecondaryIndexSettingsUpdate, Wrappers_Compile.Option<TableClass> ReplicaTableClass) {
    this._RegionName = RegionName;
    this._ReplicaProvisionedReadCapacityUnits = ReplicaProvisionedReadCapacityUnits;
    this._ReplicaProvisionedReadCapacityAutoScalingSettingsUpdate = ReplicaProvisionedReadCapacityAutoScalingSettingsUpdate;
    this._ReplicaGlobalSecondaryIndexSettingsUpdate = ReplicaGlobalSecondaryIndexSettingsUpdate;
    this._ReplicaTableClass = ReplicaTableClass;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ReplicaSettingsUpdate o = (ReplicaSettingsUpdate)other;
    return true && java.util.Objects.equals(this._RegionName, o._RegionName) && java.util.Objects.equals(this._ReplicaProvisionedReadCapacityUnits, o._ReplicaProvisionedReadCapacityUnits) && java.util.Objects.equals(this._ReplicaProvisionedReadCapacityAutoScalingSettingsUpdate, o._ReplicaProvisionedReadCapacityAutoScalingSettingsUpdate) && java.util.Objects.equals(this._ReplicaGlobalSecondaryIndexSettingsUpdate, o._ReplicaGlobalSecondaryIndexSettingsUpdate) && java.util.Objects.equals(this._ReplicaTableClass, o._ReplicaTableClass);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._RegionName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReplicaProvisionedReadCapacityUnits);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReplicaProvisionedReadCapacityAutoScalingSettingsUpdate);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReplicaGlobalSecondaryIndexSettingsUpdate);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReplicaTableClass);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ReplicaSettingsUpdate.ReplicaSettingsUpdate");
    s.append("(");
    s.append(dafny.Helpers.toString(this._RegionName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ReplicaProvisionedReadCapacityUnits));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ReplicaProvisionedReadCapacityAutoScalingSettingsUpdate));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ReplicaGlobalSecondaryIndexSettingsUpdate));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ReplicaTableClass));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ReplicaSettingsUpdate> _TYPE = dafny.TypeDescriptor.<ReplicaSettingsUpdate>referenceWithInitializer(ReplicaSettingsUpdate.class, () -> ReplicaSettingsUpdate.Default());
  public static dafny.TypeDescriptor<ReplicaSettingsUpdate> _typeDescriptor() {
    return (dafny.TypeDescriptor<ReplicaSettingsUpdate>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ReplicaSettingsUpdate theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.ReplicaSettingsUpdate.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<java.lang.Long>Default(PositiveLongObject._typeDescriptor()), Wrappers_Compile.Option.<AutoScalingSettingsUpdate>Default(AutoScalingSettingsUpdate._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends ReplicaGlobalSecondaryIndexSettingsUpdate>>Default(ReplicaGlobalSecondaryIndexSettingsUpdateList._typeDescriptor()), Wrappers_Compile.Option.<TableClass>Default(TableClass._typeDescriptor()));
  public static ReplicaSettingsUpdate Default() {
    return theDefault;
  }
  public static ReplicaSettingsUpdate create(dafny.DafnySequence<? extends Character> RegionName, Wrappers_Compile.Option<java.lang.Long> ReplicaProvisionedReadCapacityUnits, Wrappers_Compile.Option<AutoScalingSettingsUpdate> ReplicaProvisionedReadCapacityAutoScalingSettingsUpdate, Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaGlobalSecondaryIndexSettingsUpdate>> ReplicaGlobalSecondaryIndexSettingsUpdate, Wrappers_Compile.Option<TableClass> ReplicaTableClass) {
    return new ReplicaSettingsUpdate(RegionName, ReplicaProvisionedReadCapacityUnits, ReplicaProvisionedReadCapacityAutoScalingSettingsUpdate, ReplicaGlobalSecondaryIndexSettingsUpdate, ReplicaTableClass);
  }
  public static ReplicaSettingsUpdate create_ReplicaSettingsUpdate(dafny.DafnySequence<? extends Character> RegionName, Wrappers_Compile.Option<java.lang.Long> ReplicaProvisionedReadCapacityUnits, Wrappers_Compile.Option<AutoScalingSettingsUpdate> ReplicaProvisionedReadCapacityAutoScalingSettingsUpdate, Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaGlobalSecondaryIndexSettingsUpdate>> ReplicaGlobalSecondaryIndexSettingsUpdate, Wrappers_Compile.Option<TableClass> ReplicaTableClass) {
    return create(RegionName, ReplicaProvisionedReadCapacityUnits, ReplicaProvisionedReadCapacityAutoScalingSettingsUpdate, ReplicaGlobalSecondaryIndexSettingsUpdate, ReplicaTableClass);
  }
  public boolean is_ReplicaSettingsUpdate() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_RegionName() {
    return this._RegionName;
  }
  public Wrappers_Compile.Option<java.lang.Long> dtor_ReplicaProvisionedReadCapacityUnits() {
    return this._ReplicaProvisionedReadCapacityUnits;
  }
  public Wrappers_Compile.Option<AutoScalingSettingsUpdate> dtor_ReplicaProvisionedReadCapacityAutoScalingSettingsUpdate() {
    return this._ReplicaProvisionedReadCapacityAutoScalingSettingsUpdate;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaGlobalSecondaryIndexSettingsUpdate>> dtor_ReplicaGlobalSecondaryIndexSettingsUpdate() {
    return this._ReplicaGlobalSecondaryIndexSettingsUpdate;
  }
  public Wrappers_Compile.Option<TableClass> dtor_ReplicaTableClass() {
    return this._ReplicaTableClass;
  }
}
