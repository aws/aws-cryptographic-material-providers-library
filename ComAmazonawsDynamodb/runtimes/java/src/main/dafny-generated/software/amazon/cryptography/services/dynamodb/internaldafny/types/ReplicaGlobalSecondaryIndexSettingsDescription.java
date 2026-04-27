// Class ReplicaGlobalSecondaryIndexSettingsDescription
// Dafny class ReplicaGlobalSecondaryIndexSettingsDescription compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ReplicaGlobalSecondaryIndexSettingsDescription {
  public dafny.DafnySequence<? extends Character> _IndexName;
  public Wrappers_Compile.Option<IndexStatus> _IndexStatus;
  public Wrappers_Compile.Option<java.lang.Long> _ProvisionedReadCapacityUnits;
  public Wrappers_Compile.Option<AutoScalingSettingsDescription> _ProvisionedReadCapacityAutoScalingSettings;
  public Wrappers_Compile.Option<java.lang.Long> _ProvisionedWriteCapacityUnits;
  public Wrappers_Compile.Option<AutoScalingSettingsDescription> _ProvisionedWriteCapacityAutoScalingSettings;
  public ReplicaGlobalSecondaryIndexSettingsDescription (dafny.DafnySequence<? extends Character> IndexName, Wrappers_Compile.Option<IndexStatus> IndexStatus, Wrappers_Compile.Option<java.lang.Long> ProvisionedReadCapacityUnits, Wrappers_Compile.Option<AutoScalingSettingsDescription> ProvisionedReadCapacityAutoScalingSettings, Wrappers_Compile.Option<java.lang.Long> ProvisionedWriteCapacityUnits, Wrappers_Compile.Option<AutoScalingSettingsDescription> ProvisionedWriteCapacityAutoScalingSettings) {
    this._IndexName = IndexName;
    this._IndexStatus = IndexStatus;
    this._ProvisionedReadCapacityUnits = ProvisionedReadCapacityUnits;
    this._ProvisionedReadCapacityAutoScalingSettings = ProvisionedReadCapacityAutoScalingSettings;
    this._ProvisionedWriteCapacityUnits = ProvisionedWriteCapacityUnits;
    this._ProvisionedWriteCapacityAutoScalingSettings = ProvisionedWriteCapacityAutoScalingSettings;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ReplicaGlobalSecondaryIndexSettingsDescription o = (ReplicaGlobalSecondaryIndexSettingsDescription)other;
    return true && java.util.Objects.equals(this._IndexName, o._IndexName) && java.util.Objects.equals(this._IndexStatus, o._IndexStatus) && java.util.Objects.equals(this._ProvisionedReadCapacityUnits, o._ProvisionedReadCapacityUnits) && java.util.Objects.equals(this._ProvisionedReadCapacityAutoScalingSettings, o._ProvisionedReadCapacityAutoScalingSettings) && java.util.Objects.equals(this._ProvisionedWriteCapacityUnits, o._ProvisionedWriteCapacityUnits) && java.util.Objects.equals(this._ProvisionedWriteCapacityAutoScalingSettings, o._ProvisionedWriteCapacityAutoScalingSettings);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._IndexName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._IndexStatus);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ProvisionedReadCapacityUnits);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ProvisionedReadCapacityAutoScalingSettings);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ProvisionedWriteCapacityUnits);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ProvisionedWriteCapacityAutoScalingSettings);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ReplicaGlobalSecondaryIndexSettingsDescription.ReplicaGlobalSecondaryIndexSettingsDescription");
    s.append("(");
    s.append(dafny.Helpers.toString(this._IndexName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._IndexStatus));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ProvisionedReadCapacityUnits));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ProvisionedReadCapacityAutoScalingSettings));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ProvisionedWriteCapacityUnits));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ProvisionedWriteCapacityAutoScalingSettings));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ReplicaGlobalSecondaryIndexSettingsDescription> _TYPE = dafny.TypeDescriptor.<ReplicaGlobalSecondaryIndexSettingsDescription>referenceWithInitializer(ReplicaGlobalSecondaryIndexSettingsDescription.class, () -> ReplicaGlobalSecondaryIndexSettingsDescription.Default());
  public static dafny.TypeDescriptor<ReplicaGlobalSecondaryIndexSettingsDescription> _typeDescriptor() {
    return (dafny.TypeDescriptor<ReplicaGlobalSecondaryIndexSettingsDescription>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ReplicaGlobalSecondaryIndexSettingsDescription theDefault = ReplicaGlobalSecondaryIndexSettingsDescription.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<IndexStatus>Default(IndexStatus._typeDescriptor()), Wrappers_Compile.Option.<java.lang.Long>Default(PositiveLongObject._typeDescriptor()), Wrappers_Compile.Option.<AutoScalingSettingsDescription>Default(AutoScalingSettingsDescription._typeDescriptor()), Wrappers_Compile.Option.<java.lang.Long>Default(PositiveLongObject._typeDescriptor()), Wrappers_Compile.Option.<AutoScalingSettingsDescription>Default(AutoScalingSettingsDescription._typeDescriptor()));
  public static ReplicaGlobalSecondaryIndexSettingsDescription Default() {
    return theDefault;
  }
  public static ReplicaGlobalSecondaryIndexSettingsDescription create(dafny.DafnySequence<? extends Character> IndexName, Wrappers_Compile.Option<IndexStatus> IndexStatus, Wrappers_Compile.Option<java.lang.Long> ProvisionedReadCapacityUnits, Wrappers_Compile.Option<AutoScalingSettingsDescription> ProvisionedReadCapacityAutoScalingSettings, Wrappers_Compile.Option<java.lang.Long> ProvisionedWriteCapacityUnits, Wrappers_Compile.Option<AutoScalingSettingsDescription> ProvisionedWriteCapacityAutoScalingSettings) {
    return new ReplicaGlobalSecondaryIndexSettingsDescription(IndexName, IndexStatus, ProvisionedReadCapacityUnits, ProvisionedReadCapacityAutoScalingSettings, ProvisionedWriteCapacityUnits, ProvisionedWriteCapacityAutoScalingSettings);
  }
  public static ReplicaGlobalSecondaryIndexSettingsDescription create_ReplicaGlobalSecondaryIndexSettingsDescription(dafny.DafnySequence<? extends Character> IndexName, Wrappers_Compile.Option<IndexStatus> IndexStatus, Wrappers_Compile.Option<java.lang.Long> ProvisionedReadCapacityUnits, Wrappers_Compile.Option<AutoScalingSettingsDescription> ProvisionedReadCapacityAutoScalingSettings, Wrappers_Compile.Option<java.lang.Long> ProvisionedWriteCapacityUnits, Wrappers_Compile.Option<AutoScalingSettingsDescription> ProvisionedWriteCapacityAutoScalingSettings) {
    return create(IndexName, IndexStatus, ProvisionedReadCapacityUnits, ProvisionedReadCapacityAutoScalingSettings, ProvisionedWriteCapacityUnits, ProvisionedWriteCapacityAutoScalingSettings);
  }
  public boolean is_ReplicaGlobalSecondaryIndexSettingsDescription() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_IndexName() {
    return this._IndexName;
  }
  public Wrappers_Compile.Option<IndexStatus> dtor_IndexStatus() {
    return this._IndexStatus;
  }
  public Wrappers_Compile.Option<java.lang.Long> dtor_ProvisionedReadCapacityUnits() {
    return this._ProvisionedReadCapacityUnits;
  }
  public Wrappers_Compile.Option<AutoScalingSettingsDescription> dtor_ProvisionedReadCapacityAutoScalingSettings() {
    return this._ProvisionedReadCapacityAutoScalingSettings;
  }
  public Wrappers_Compile.Option<java.lang.Long> dtor_ProvisionedWriteCapacityUnits() {
    return this._ProvisionedWriteCapacityUnits;
  }
  public Wrappers_Compile.Option<AutoScalingSettingsDescription> dtor_ProvisionedWriteCapacityAutoScalingSettings() {
    return this._ProvisionedWriteCapacityAutoScalingSettings;
  }
}
