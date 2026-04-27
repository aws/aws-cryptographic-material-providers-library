// Class ReplicaAutoScalingDescription
// Dafny class ReplicaAutoScalingDescription compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ReplicaAutoScalingDescription {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _RegionName;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaGlobalSecondaryIndexAutoScalingDescription>> _GlobalSecondaryIndexes;
  public Wrappers_Compile.Option<AutoScalingSettingsDescription> _ReplicaProvisionedReadCapacityAutoScalingSettings;
  public Wrappers_Compile.Option<AutoScalingSettingsDescription> _ReplicaProvisionedWriteCapacityAutoScalingSettings;
  public Wrappers_Compile.Option<ReplicaStatus> _ReplicaStatus;
  public ReplicaAutoScalingDescription (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> RegionName, Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaGlobalSecondaryIndexAutoScalingDescription>> GlobalSecondaryIndexes, Wrappers_Compile.Option<AutoScalingSettingsDescription> ReplicaProvisionedReadCapacityAutoScalingSettings, Wrappers_Compile.Option<AutoScalingSettingsDescription> ReplicaProvisionedWriteCapacityAutoScalingSettings, Wrappers_Compile.Option<ReplicaStatus> ReplicaStatus) {
    this._RegionName = RegionName;
    this._GlobalSecondaryIndexes = GlobalSecondaryIndexes;
    this._ReplicaProvisionedReadCapacityAutoScalingSettings = ReplicaProvisionedReadCapacityAutoScalingSettings;
    this._ReplicaProvisionedWriteCapacityAutoScalingSettings = ReplicaProvisionedWriteCapacityAutoScalingSettings;
    this._ReplicaStatus = ReplicaStatus;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ReplicaAutoScalingDescription o = (ReplicaAutoScalingDescription)other;
    return true && java.util.Objects.equals(this._RegionName, o._RegionName) && java.util.Objects.equals(this._GlobalSecondaryIndexes, o._GlobalSecondaryIndexes) && java.util.Objects.equals(this._ReplicaProvisionedReadCapacityAutoScalingSettings, o._ReplicaProvisionedReadCapacityAutoScalingSettings) && java.util.Objects.equals(this._ReplicaProvisionedWriteCapacityAutoScalingSettings, o._ReplicaProvisionedWriteCapacityAutoScalingSettings) && java.util.Objects.equals(this._ReplicaStatus, o._ReplicaStatus);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._RegionName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._GlobalSecondaryIndexes);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReplicaProvisionedReadCapacityAutoScalingSettings);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReplicaProvisionedWriteCapacityAutoScalingSettings);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReplicaStatus);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ReplicaAutoScalingDescription.ReplicaAutoScalingDescription");
    s.append("(");
    s.append(dafny.Helpers.toString(this._RegionName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._GlobalSecondaryIndexes));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ReplicaProvisionedReadCapacityAutoScalingSettings));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ReplicaProvisionedWriteCapacityAutoScalingSettings));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ReplicaStatus));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ReplicaAutoScalingDescription> _TYPE = dafny.TypeDescriptor.<ReplicaAutoScalingDescription>referenceWithInitializer(ReplicaAutoScalingDescription.class, () -> ReplicaAutoScalingDescription.Default());
  public static dafny.TypeDescriptor<ReplicaAutoScalingDescription> _typeDescriptor() {
    return (dafny.TypeDescriptor<ReplicaAutoScalingDescription>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ReplicaAutoScalingDescription theDefault = ReplicaAutoScalingDescription.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends ReplicaGlobalSecondaryIndexAutoScalingDescription>>Default(dafny.DafnySequence.<ReplicaGlobalSecondaryIndexAutoScalingDescription>_typeDescriptor(ReplicaGlobalSecondaryIndexAutoScalingDescription._typeDescriptor())), Wrappers_Compile.Option.<AutoScalingSettingsDescription>Default(AutoScalingSettingsDescription._typeDescriptor()), Wrappers_Compile.Option.<AutoScalingSettingsDescription>Default(AutoScalingSettingsDescription._typeDescriptor()), Wrappers_Compile.Option.<ReplicaStatus>Default(ReplicaStatus._typeDescriptor()));
  public static ReplicaAutoScalingDescription Default() {
    return theDefault;
  }
  public static ReplicaAutoScalingDescription create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> RegionName, Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaGlobalSecondaryIndexAutoScalingDescription>> GlobalSecondaryIndexes, Wrappers_Compile.Option<AutoScalingSettingsDescription> ReplicaProvisionedReadCapacityAutoScalingSettings, Wrappers_Compile.Option<AutoScalingSettingsDescription> ReplicaProvisionedWriteCapacityAutoScalingSettings, Wrappers_Compile.Option<ReplicaStatus> ReplicaStatus) {
    return new ReplicaAutoScalingDescription(RegionName, GlobalSecondaryIndexes, ReplicaProvisionedReadCapacityAutoScalingSettings, ReplicaProvisionedWriteCapacityAutoScalingSettings, ReplicaStatus);
  }
  public static ReplicaAutoScalingDescription create_ReplicaAutoScalingDescription(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> RegionName, Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaGlobalSecondaryIndexAutoScalingDescription>> GlobalSecondaryIndexes, Wrappers_Compile.Option<AutoScalingSettingsDescription> ReplicaProvisionedReadCapacityAutoScalingSettings, Wrappers_Compile.Option<AutoScalingSettingsDescription> ReplicaProvisionedWriteCapacityAutoScalingSettings, Wrappers_Compile.Option<ReplicaStatus> ReplicaStatus) {
    return create(RegionName, GlobalSecondaryIndexes, ReplicaProvisionedReadCapacityAutoScalingSettings, ReplicaProvisionedWriteCapacityAutoScalingSettings, ReplicaStatus);
  }
  public boolean is_ReplicaAutoScalingDescription() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_RegionName() {
    return this._RegionName;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaGlobalSecondaryIndexAutoScalingDescription>> dtor_GlobalSecondaryIndexes() {
    return this._GlobalSecondaryIndexes;
  }
  public Wrappers_Compile.Option<AutoScalingSettingsDescription> dtor_ReplicaProvisionedReadCapacityAutoScalingSettings() {
    return this._ReplicaProvisionedReadCapacityAutoScalingSettings;
  }
  public Wrappers_Compile.Option<AutoScalingSettingsDescription> dtor_ReplicaProvisionedWriteCapacityAutoScalingSettings() {
    return this._ReplicaProvisionedWriteCapacityAutoScalingSettings;
  }
  public Wrappers_Compile.Option<ReplicaStatus> dtor_ReplicaStatus() {
    return this._ReplicaStatus;
  }
}
