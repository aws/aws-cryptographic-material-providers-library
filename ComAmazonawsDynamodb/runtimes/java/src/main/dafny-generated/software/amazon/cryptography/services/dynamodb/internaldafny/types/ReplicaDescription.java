// Class ReplicaDescription
// Dafny class ReplicaDescription compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ReplicaDescription {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _RegionName;
  public Wrappers_Compile.Option<ReplicaStatus> _ReplicaStatus;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _ReplicaStatusDescription;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _ReplicaStatusPercentProgress;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _KMSMasterKeyId;
  public Wrappers_Compile.Option<ProvisionedThroughputOverride> _ProvisionedThroughputOverride;
  public Wrappers_Compile.Option<OnDemandThroughputOverride> _OnDemandThroughputOverride;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaGlobalSecondaryIndexDescription>> _GlobalSecondaryIndexes;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _ReplicaInaccessibleDateTime;
  public Wrappers_Compile.Option<TableClassSummary> _ReplicaTableClassSummary;
  public ReplicaDescription (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> RegionName, Wrappers_Compile.Option<ReplicaStatus> ReplicaStatus, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ReplicaStatusDescription, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ReplicaStatusPercentProgress, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KMSMasterKeyId, Wrappers_Compile.Option<ProvisionedThroughputOverride> ProvisionedThroughputOverride, Wrappers_Compile.Option<OnDemandThroughputOverride> OnDemandThroughputOverride, Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaGlobalSecondaryIndexDescription>> GlobalSecondaryIndexes, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ReplicaInaccessibleDateTime, Wrappers_Compile.Option<TableClassSummary> ReplicaTableClassSummary) {
    this._RegionName = RegionName;
    this._ReplicaStatus = ReplicaStatus;
    this._ReplicaStatusDescription = ReplicaStatusDescription;
    this._ReplicaStatusPercentProgress = ReplicaStatusPercentProgress;
    this._KMSMasterKeyId = KMSMasterKeyId;
    this._ProvisionedThroughputOverride = ProvisionedThroughputOverride;
    this._OnDemandThroughputOverride = OnDemandThroughputOverride;
    this._GlobalSecondaryIndexes = GlobalSecondaryIndexes;
    this._ReplicaInaccessibleDateTime = ReplicaInaccessibleDateTime;
    this._ReplicaTableClassSummary = ReplicaTableClassSummary;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ReplicaDescription o = (ReplicaDescription)other;
    return true && java.util.Objects.equals(this._RegionName, o._RegionName) && java.util.Objects.equals(this._ReplicaStatus, o._ReplicaStatus) && java.util.Objects.equals(this._ReplicaStatusDescription, o._ReplicaStatusDescription) && java.util.Objects.equals(this._ReplicaStatusPercentProgress, o._ReplicaStatusPercentProgress) && java.util.Objects.equals(this._KMSMasterKeyId, o._KMSMasterKeyId) && java.util.Objects.equals(this._ProvisionedThroughputOverride, o._ProvisionedThroughputOverride) && java.util.Objects.equals(this._OnDemandThroughputOverride, o._OnDemandThroughputOverride) && java.util.Objects.equals(this._GlobalSecondaryIndexes, o._GlobalSecondaryIndexes) && java.util.Objects.equals(this._ReplicaInaccessibleDateTime, o._ReplicaInaccessibleDateTime) && java.util.Objects.equals(this._ReplicaTableClassSummary, o._ReplicaTableClassSummary);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._RegionName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReplicaStatus);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReplicaStatusDescription);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReplicaStatusPercentProgress);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KMSMasterKeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ProvisionedThroughputOverride);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._OnDemandThroughputOverride);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._GlobalSecondaryIndexes);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReplicaInaccessibleDateTime);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReplicaTableClassSummary);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ReplicaDescription.ReplicaDescription");
    s.append("(");
    s.append(dafny.Helpers.toString(this._RegionName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ReplicaStatus));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ReplicaStatusDescription));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ReplicaStatusPercentProgress));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._KMSMasterKeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ProvisionedThroughputOverride));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._OnDemandThroughputOverride));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._GlobalSecondaryIndexes));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ReplicaInaccessibleDateTime));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ReplicaTableClassSummary));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ReplicaDescription> _TYPE = dafny.TypeDescriptor.<ReplicaDescription>referenceWithInitializer(ReplicaDescription.class, () -> ReplicaDescription.Default());
  public static dafny.TypeDescriptor<ReplicaDescription> _typeDescriptor() {
    return (dafny.TypeDescriptor<ReplicaDescription>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ReplicaDescription theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.ReplicaDescription.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<ReplicaStatus>Default(ReplicaStatus._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<ProvisionedThroughputOverride>Default(ProvisionedThroughputOverride._typeDescriptor()), Wrappers_Compile.Option.<OnDemandThroughputOverride>Default(OnDemandThroughputOverride._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends ReplicaGlobalSecondaryIndexDescription>>Default(dafny.DafnySequence.<ReplicaGlobalSecondaryIndexDescription>_typeDescriptor(ReplicaGlobalSecondaryIndexDescription._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<TableClassSummary>Default(TableClassSummary._typeDescriptor()));
  public static ReplicaDescription Default() {
    return theDefault;
  }
  public static ReplicaDescription create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> RegionName, Wrappers_Compile.Option<ReplicaStatus> ReplicaStatus, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ReplicaStatusDescription, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ReplicaStatusPercentProgress, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KMSMasterKeyId, Wrappers_Compile.Option<ProvisionedThroughputOverride> ProvisionedThroughputOverride, Wrappers_Compile.Option<OnDemandThroughputOverride> OnDemandThroughputOverride, Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaGlobalSecondaryIndexDescription>> GlobalSecondaryIndexes, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ReplicaInaccessibleDateTime, Wrappers_Compile.Option<TableClassSummary> ReplicaTableClassSummary) {
    return new ReplicaDescription(RegionName, ReplicaStatus, ReplicaStatusDescription, ReplicaStatusPercentProgress, KMSMasterKeyId, ProvisionedThroughputOverride, OnDemandThroughputOverride, GlobalSecondaryIndexes, ReplicaInaccessibleDateTime, ReplicaTableClassSummary);
  }
  public static ReplicaDescription create_ReplicaDescription(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> RegionName, Wrappers_Compile.Option<ReplicaStatus> ReplicaStatus, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ReplicaStatusDescription, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ReplicaStatusPercentProgress, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KMSMasterKeyId, Wrappers_Compile.Option<ProvisionedThroughputOverride> ProvisionedThroughputOverride, Wrappers_Compile.Option<OnDemandThroughputOverride> OnDemandThroughputOverride, Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaGlobalSecondaryIndexDescription>> GlobalSecondaryIndexes, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ReplicaInaccessibleDateTime, Wrappers_Compile.Option<TableClassSummary> ReplicaTableClassSummary) {
    return create(RegionName, ReplicaStatus, ReplicaStatusDescription, ReplicaStatusPercentProgress, KMSMasterKeyId, ProvisionedThroughputOverride, OnDemandThroughputOverride, GlobalSecondaryIndexes, ReplicaInaccessibleDateTime, ReplicaTableClassSummary);
  }
  public boolean is_ReplicaDescription() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_RegionName() {
    return this._RegionName;
  }
  public Wrappers_Compile.Option<ReplicaStatus> dtor_ReplicaStatus() {
    return this._ReplicaStatus;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_ReplicaStatusDescription() {
    return this._ReplicaStatusDescription;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_ReplicaStatusPercentProgress() {
    return this._ReplicaStatusPercentProgress;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_KMSMasterKeyId() {
    return this._KMSMasterKeyId;
  }
  public Wrappers_Compile.Option<ProvisionedThroughputOverride> dtor_ProvisionedThroughputOverride() {
    return this._ProvisionedThroughputOverride;
  }
  public Wrappers_Compile.Option<OnDemandThroughputOverride> dtor_OnDemandThroughputOverride() {
    return this._OnDemandThroughputOverride;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaGlobalSecondaryIndexDescription>> dtor_GlobalSecondaryIndexes() {
    return this._GlobalSecondaryIndexes;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_ReplicaInaccessibleDateTime() {
    return this._ReplicaInaccessibleDateTime;
  }
  public Wrappers_Compile.Option<TableClassSummary> dtor_ReplicaTableClassSummary() {
    return this._ReplicaTableClassSummary;
  }
}
