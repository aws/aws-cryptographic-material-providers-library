// Class ReplicaSettingsDescription
// Dafny class ReplicaSettingsDescription compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ReplicaSettingsDescription {
  public dafny.DafnySequence<? extends Character> _RegionName;
  public Wrappers_Compile.Option<ReplicaStatus> _ReplicaStatus;
  public Wrappers_Compile.Option<BillingModeSummary> _ReplicaBillingModeSummary;
  public Wrappers_Compile.Option<java.lang.Long> _ReplicaProvisionedReadCapacityUnits;
  public Wrappers_Compile.Option<AutoScalingSettingsDescription> _ReplicaProvisionedReadCapacityAutoScalingSettings;
  public Wrappers_Compile.Option<java.lang.Long> _ReplicaProvisionedWriteCapacityUnits;
  public Wrappers_Compile.Option<AutoScalingSettingsDescription> _ReplicaProvisionedWriteCapacityAutoScalingSettings;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaGlobalSecondaryIndexSettingsDescription>> _ReplicaGlobalSecondaryIndexSettings;
  public Wrappers_Compile.Option<TableClassSummary> _ReplicaTableClassSummary;
  public ReplicaSettingsDescription (dafny.DafnySequence<? extends Character> RegionName, Wrappers_Compile.Option<ReplicaStatus> ReplicaStatus, Wrappers_Compile.Option<BillingModeSummary> ReplicaBillingModeSummary, Wrappers_Compile.Option<java.lang.Long> ReplicaProvisionedReadCapacityUnits, Wrappers_Compile.Option<AutoScalingSettingsDescription> ReplicaProvisionedReadCapacityAutoScalingSettings, Wrappers_Compile.Option<java.lang.Long> ReplicaProvisionedWriteCapacityUnits, Wrappers_Compile.Option<AutoScalingSettingsDescription> ReplicaProvisionedWriteCapacityAutoScalingSettings, Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaGlobalSecondaryIndexSettingsDescription>> ReplicaGlobalSecondaryIndexSettings, Wrappers_Compile.Option<TableClassSummary> ReplicaTableClassSummary) {
    this._RegionName = RegionName;
    this._ReplicaStatus = ReplicaStatus;
    this._ReplicaBillingModeSummary = ReplicaBillingModeSummary;
    this._ReplicaProvisionedReadCapacityUnits = ReplicaProvisionedReadCapacityUnits;
    this._ReplicaProvisionedReadCapacityAutoScalingSettings = ReplicaProvisionedReadCapacityAutoScalingSettings;
    this._ReplicaProvisionedWriteCapacityUnits = ReplicaProvisionedWriteCapacityUnits;
    this._ReplicaProvisionedWriteCapacityAutoScalingSettings = ReplicaProvisionedWriteCapacityAutoScalingSettings;
    this._ReplicaGlobalSecondaryIndexSettings = ReplicaGlobalSecondaryIndexSettings;
    this._ReplicaTableClassSummary = ReplicaTableClassSummary;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ReplicaSettingsDescription o = (ReplicaSettingsDescription)other;
    return true && java.util.Objects.equals(this._RegionName, o._RegionName) && java.util.Objects.equals(this._ReplicaStatus, o._ReplicaStatus) && java.util.Objects.equals(this._ReplicaBillingModeSummary, o._ReplicaBillingModeSummary) && java.util.Objects.equals(this._ReplicaProvisionedReadCapacityUnits, o._ReplicaProvisionedReadCapacityUnits) && java.util.Objects.equals(this._ReplicaProvisionedReadCapacityAutoScalingSettings, o._ReplicaProvisionedReadCapacityAutoScalingSettings) && java.util.Objects.equals(this._ReplicaProvisionedWriteCapacityUnits, o._ReplicaProvisionedWriteCapacityUnits) && java.util.Objects.equals(this._ReplicaProvisionedWriteCapacityAutoScalingSettings, o._ReplicaProvisionedWriteCapacityAutoScalingSettings) && java.util.Objects.equals(this._ReplicaGlobalSecondaryIndexSettings, o._ReplicaGlobalSecondaryIndexSettings) && java.util.Objects.equals(this._ReplicaTableClassSummary, o._ReplicaTableClassSummary);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._RegionName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReplicaStatus);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReplicaBillingModeSummary);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReplicaProvisionedReadCapacityUnits);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReplicaProvisionedReadCapacityAutoScalingSettings);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReplicaProvisionedWriteCapacityUnits);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReplicaProvisionedWriteCapacityAutoScalingSettings);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReplicaGlobalSecondaryIndexSettings);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReplicaTableClassSummary);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ReplicaSettingsDescription.ReplicaSettingsDescription");
    s.append("(");
    s.append(dafny.Helpers.toString(this._RegionName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ReplicaStatus));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ReplicaBillingModeSummary));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ReplicaProvisionedReadCapacityUnits));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ReplicaProvisionedReadCapacityAutoScalingSettings));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ReplicaProvisionedWriteCapacityUnits));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ReplicaProvisionedWriteCapacityAutoScalingSettings));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ReplicaGlobalSecondaryIndexSettings));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ReplicaTableClassSummary));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ReplicaSettingsDescription> _TYPE = dafny.TypeDescriptor.<ReplicaSettingsDescription>referenceWithInitializer(ReplicaSettingsDescription.class, () -> ReplicaSettingsDescription.Default());
  public static dafny.TypeDescriptor<ReplicaSettingsDescription> _typeDescriptor() {
    return (dafny.TypeDescriptor<ReplicaSettingsDescription>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ReplicaSettingsDescription theDefault = ReplicaSettingsDescription.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<ReplicaStatus>Default(ReplicaStatus._typeDescriptor()), Wrappers_Compile.Option.<BillingModeSummary>Default(BillingModeSummary._typeDescriptor()), Wrappers_Compile.Option.<java.lang.Long>Default(NonNegativeLongObject._typeDescriptor()), Wrappers_Compile.Option.<AutoScalingSettingsDescription>Default(AutoScalingSettingsDescription._typeDescriptor()), Wrappers_Compile.Option.<java.lang.Long>Default(NonNegativeLongObject._typeDescriptor()), Wrappers_Compile.Option.<AutoScalingSettingsDescription>Default(AutoScalingSettingsDescription._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends ReplicaGlobalSecondaryIndexSettingsDescription>>Default(dafny.DafnySequence.<ReplicaGlobalSecondaryIndexSettingsDescription>_typeDescriptor(ReplicaGlobalSecondaryIndexSettingsDescription._typeDescriptor())), Wrappers_Compile.Option.<TableClassSummary>Default(TableClassSummary._typeDescriptor()));
  public static ReplicaSettingsDescription Default() {
    return theDefault;
  }
  public static ReplicaSettingsDescription create(dafny.DafnySequence<? extends Character> RegionName, Wrappers_Compile.Option<ReplicaStatus> ReplicaStatus, Wrappers_Compile.Option<BillingModeSummary> ReplicaBillingModeSummary, Wrappers_Compile.Option<java.lang.Long> ReplicaProvisionedReadCapacityUnits, Wrappers_Compile.Option<AutoScalingSettingsDescription> ReplicaProvisionedReadCapacityAutoScalingSettings, Wrappers_Compile.Option<java.lang.Long> ReplicaProvisionedWriteCapacityUnits, Wrappers_Compile.Option<AutoScalingSettingsDescription> ReplicaProvisionedWriteCapacityAutoScalingSettings, Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaGlobalSecondaryIndexSettingsDescription>> ReplicaGlobalSecondaryIndexSettings, Wrappers_Compile.Option<TableClassSummary> ReplicaTableClassSummary) {
    return new ReplicaSettingsDescription(RegionName, ReplicaStatus, ReplicaBillingModeSummary, ReplicaProvisionedReadCapacityUnits, ReplicaProvisionedReadCapacityAutoScalingSettings, ReplicaProvisionedWriteCapacityUnits, ReplicaProvisionedWriteCapacityAutoScalingSettings, ReplicaGlobalSecondaryIndexSettings, ReplicaTableClassSummary);
  }
  public static ReplicaSettingsDescription create_ReplicaSettingsDescription(dafny.DafnySequence<? extends Character> RegionName, Wrappers_Compile.Option<ReplicaStatus> ReplicaStatus, Wrappers_Compile.Option<BillingModeSummary> ReplicaBillingModeSummary, Wrappers_Compile.Option<java.lang.Long> ReplicaProvisionedReadCapacityUnits, Wrappers_Compile.Option<AutoScalingSettingsDescription> ReplicaProvisionedReadCapacityAutoScalingSettings, Wrappers_Compile.Option<java.lang.Long> ReplicaProvisionedWriteCapacityUnits, Wrappers_Compile.Option<AutoScalingSettingsDescription> ReplicaProvisionedWriteCapacityAutoScalingSettings, Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaGlobalSecondaryIndexSettingsDescription>> ReplicaGlobalSecondaryIndexSettings, Wrappers_Compile.Option<TableClassSummary> ReplicaTableClassSummary) {
    return create(RegionName, ReplicaStatus, ReplicaBillingModeSummary, ReplicaProvisionedReadCapacityUnits, ReplicaProvisionedReadCapacityAutoScalingSettings, ReplicaProvisionedWriteCapacityUnits, ReplicaProvisionedWriteCapacityAutoScalingSettings, ReplicaGlobalSecondaryIndexSettings, ReplicaTableClassSummary);
  }
  public boolean is_ReplicaSettingsDescription() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_RegionName() {
    return this._RegionName;
  }
  public Wrappers_Compile.Option<ReplicaStatus> dtor_ReplicaStatus() {
    return this._ReplicaStatus;
  }
  public Wrappers_Compile.Option<BillingModeSummary> dtor_ReplicaBillingModeSummary() {
    return this._ReplicaBillingModeSummary;
  }
  public Wrappers_Compile.Option<java.lang.Long> dtor_ReplicaProvisionedReadCapacityUnits() {
    return this._ReplicaProvisionedReadCapacityUnits;
  }
  public Wrappers_Compile.Option<AutoScalingSettingsDescription> dtor_ReplicaProvisionedReadCapacityAutoScalingSettings() {
    return this._ReplicaProvisionedReadCapacityAutoScalingSettings;
  }
  public Wrappers_Compile.Option<java.lang.Long> dtor_ReplicaProvisionedWriteCapacityUnits() {
    return this._ReplicaProvisionedWriteCapacityUnits;
  }
  public Wrappers_Compile.Option<AutoScalingSettingsDescription> dtor_ReplicaProvisionedWriteCapacityAutoScalingSettings() {
    return this._ReplicaProvisionedWriteCapacityAutoScalingSettings;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaGlobalSecondaryIndexSettingsDescription>> dtor_ReplicaGlobalSecondaryIndexSettings() {
    return this._ReplicaGlobalSecondaryIndexSettings;
  }
  public Wrappers_Compile.Option<TableClassSummary> dtor_ReplicaTableClassSummary() {
    return this._ReplicaTableClassSummary;
  }
}
