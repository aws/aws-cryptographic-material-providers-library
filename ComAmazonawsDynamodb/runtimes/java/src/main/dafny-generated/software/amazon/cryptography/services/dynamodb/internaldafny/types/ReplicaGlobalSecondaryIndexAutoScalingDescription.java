// Class ReplicaGlobalSecondaryIndexAutoScalingDescription
// Dafny class ReplicaGlobalSecondaryIndexAutoScalingDescription compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ReplicaGlobalSecondaryIndexAutoScalingDescription {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _IndexName;
  public Wrappers_Compile.Option<IndexStatus> _IndexStatus;
  public Wrappers_Compile.Option<AutoScalingSettingsDescription> _ProvisionedReadCapacityAutoScalingSettings;
  public Wrappers_Compile.Option<AutoScalingSettingsDescription> _ProvisionedWriteCapacityAutoScalingSettings;
  public ReplicaGlobalSecondaryIndexAutoScalingDescription (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> IndexName, Wrappers_Compile.Option<IndexStatus> IndexStatus, Wrappers_Compile.Option<AutoScalingSettingsDescription> ProvisionedReadCapacityAutoScalingSettings, Wrappers_Compile.Option<AutoScalingSettingsDescription> ProvisionedWriteCapacityAutoScalingSettings) {
    this._IndexName = IndexName;
    this._IndexStatus = IndexStatus;
    this._ProvisionedReadCapacityAutoScalingSettings = ProvisionedReadCapacityAutoScalingSettings;
    this._ProvisionedWriteCapacityAutoScalingSettings = ProvisionedWriteCapacityAutoScalingSettings;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ReplicaGlobalSecondaryIndexAutoScalingDescription o = (ReplicaGlobalSecondaryIndexAutoScalingDescription)other;
    return true && java.util.Objects.equals(this._IndexName, o._IndexName) && java.util.Objects.equals(this._IndexStatus, o._IndexStatus) && java.util.Objects.equals(this._ProvisionedReadCapacityAutoScalingSettings, o._ProvisionedReadCapacityAutoScalingSettings) && java.util.Objects.equals(this._ProvisionedWriteCapacityAutoScalingSettings, o._ProvisionedWriteCapacityAutoScalingSettings);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._IndexName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._IndexStatus);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ProvisionedReadCapacityAutoScalingSettings);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ProvisionedWriteCapacityAutoScalingSettings);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ReplicaGlobalSecondaryIndexAutoScalingDescription.ReplicaGlobalSecondaryIndexAutoScalingDescription");
    s.append("(");
    s.append(dafny.Helpers.toString(this._IndexName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._IndexStatus));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ProvisionedReadCapacityAutoScalingSettings));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ProvisionedWriteCapacityAutoScalingSettings));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ReplicaGlobalSecondaryIndexAutoScalingDescription> _TYPE = dafny.TypeDescriptor.<ReplicaGlobalSecondaryIndexAutoScalingDescription>referenceWithInitializer(ReplicaGlobalSecondaryIndexAutoScalingDescription.class, () -> ReplicaGlobalSecondaryIndexAutoScalingDescription.Default());
  public static dafny.TypeDescriptor<ReplicaGlobalSecondaryIndexAutoScalingDescription> _typeDescriptor() {
    return (dafny.TypeDescriptor<ReplicaGlobalSecondaryIndexAutoScalingDescription>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ReplicaGlobalSecondaryIndexAutoScalingDescription theDefault = ReplicaGlobalSecondaryIndexAutoScalingDescription.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(IndexName._typeDescriptor()), Wrappers_Compile.Option.<IndexStatus>Default(IndexStatus._typeDescriptor()), Wrappers_Compile.Option.<AutoScalingSettingsDescription>Default(AutoScalingSettingsDescription._typeDescriptor()), Wrappers_Compile.Option.<AutoScalingSettingsDescription>Default(AutoScalingSettingsDescription._typeDescriptor()));
  public static ReplicaGlobalSecondaryIndexAutoScalingDescription Default() {
    return theDefault;
  }
  public static ReplicaGlobalSecondaryIndexAutoScalingDescription create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> IndexName, Wrappers_Compile.Option<IndexStatus> IndexStatus, Wrappers_Compile.Option<AutoScalingSettingsDescription> ProvisionedReadCapacityAutoScalingSettings, Wrappers_Compile.Option<AutoScalingSettingsDescription> ProvisionedWriteCapacityAutoScalingSettings) {
    return new ReplicaGlobalSecondaryIndexAutoScalingDescription(IndexName, IndexStatus, ProvisionedReadCapacityAutoScalingSettings, ProvisionedWriteCapacityAutoScalingSettings);
  }
  public static ReplicaGlobalSecondaryIndexAutoScalingDescription create_ReplicaGlobalSecondaryIndexAutoScalingDescription(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> IndexName, Wrappers_Compile.Option<IndexStatus> IndexStatus, Wrappers_Compile.Option<AutoScalingSettingsDescription> ProvisionedReadCapacityAutoScalingSettings, Wrappers_Compile.Option<AutoScalingSettingsDescription> ProvisionedWriteCapacityAutoScalingSettings) {
    return create(IndexName, IndexStatus, ProvisionedReadCapacityAutoScalingSettings, ProvisionedWriteCapacityAutoScalingSettings);
  }
  public boolean is_ReplicaGlobalSecondaryIndexAutoScalingDescription() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_IndexName() {
    return this._IndexName;
  }
  public Wrappers_Compile.Option<IndexStatus> dtor_IndexStatus() {
    return this._IndexStatus;
  }
  public Wrappers_Compile.Option<AutoScalingSettingsDescription> dtor_ProvisionedReadCapacityAutoScalingSettings() {
    return this._ProvisionedReadCapacityAutoScalingSettings;
  }
  public Wrappers_Compile.Option<AutoScalingSettingsDescription> dtor_ProvisionedWriteCapacityAutoScalingSettings() {
    return this._ProvisionedWriteCapacityAutoScalingSettings;
  }
}
