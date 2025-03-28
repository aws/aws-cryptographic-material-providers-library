// Class RestoreTableToPointInTimeInput
// Dafny class RestoreTableToPointInTimeInput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class RestoreTableToPointInTimeInput {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _SourceTableArn;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _SourceTableName;
  public dafny.DafnySequence<? extends Character> _TargetTableName;
  public Wrappers_Compile.Option<Boolean> _UseLatestRestorableTime;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _RestoreDateTime;
  public Wrappers_Compile.Option<BillingMode> _BillingModeOverride;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends GlobalSecondaryIndex>> _GlobalSecondaryIndexOverride;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends LocalSecondaryIndex>> _LocalSecondaryIndexOverride;
  public Wrappers_Compile.Option<ProvisionedThroughput> _ProvisionedThroughputOverride;
  public Wrappers_Compile.Option<OnDemandThroughput> _OnDemandThroughputOverride;
  public Wrappers_Compile.Option<SSESpecification> _SSESpecificationOverride;
  public RestoreTableToPointInTimeInput (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> SourceTableArn, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> SourceTableName, dafny.DafnySequence<? extends Character> TargetTableName, Wrappers_Compile.Option<Boolean> UseLatestRestorableTime, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> RestoreDateTime, Wrappers_Compile.Option<BillingMode> BillingModeOverride, Wrappers_Compile.Option<dafny.DafnySequence<? extends GlobalSecondaryIndex>> GlobalSecondaryIndexOverride, Wrappers_Compile.Option<dafny.DafnySequence<? extends LocalSecondaryIndex>> LocalSecondaryIndexOverride, Wrappers_Compile.Option<ProvisionedThroughput> ProvisionedThroughputOverride, Wrappers_Compile.Option<OnDemandThroughput> OnDemandThroughputOverride, Wrappers_Compile.Option<SSESpecification> SSESpecificationOverride) {
    this._SourceTableArn = SourceTableArn;
    this._SourceTableName = SourceTableName;
    this._TargetTableName = TargetTableName;
    this._UseLatestRestorableTime = UseLatestRestorableTime;
    this._RestoreDateTime = RestoreDateTime;
    this._BillingModeOverride = BillingModeOverride;
    this._GlobalSecondaryIndexOverride = GlobalSecondaryIndexOverride;
    this._LocalSecondaryIndexOverride = LocalSecondaryIndexOverride;
    this._ProvisionedThroughputOverride = ProvisionedThroughputOverride;
    this._OnDemandThroughputOverride = OnDemandThroughputOverride;
    this._SSESpecificationOverride = SSESpecificationOverride;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    RestoreTableToPointInTimeInput o = (RestoreTableToPointInTimeInput)other;
    return true && java.util.Objects.equals(this._SourceTableArn, o._SourceTableArn) && java.util.Objects.equals(this._SourceTableName, o._SourceTableName) && java.util.Objects.equals(this._TargetTableName, o._TargetTableName) && java.util.Objects.equals(this._UseLatestRestorableTime, o._UseLatestRestorableTime) && java.util.Objects.equals(this._RestoreDateTime, o._RestoreDateTime) && java.util.Objects.equals(this._BillingModeOverride, o._BillingModeOverride) && java.util.Objects.equals(this._GlobalSecondaryIndexOverride, o._GlobalSecondaryIndexOverride) && java.util.Objects.equals(this._LocalSecondaryIndexOverride, o._LocalSecondaryIndexOverride) && java.util.Objects.equals(this._ProvisionedThroughputOverride, o._ProvisionedThroughputOverride) && java.util.Objects.equals(this._OnDemandThroughputOverride, o._OnDemandThroughputOverride) && java.util.Objects.equals(this._SSESpecificationOverride, o._SSESpecificationOverride);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._SourceTableArn);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._SourceTableName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TargetTableName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._UseLatestRestorableTime);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._RestoreDateTime);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._BillingModeOverride);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._GlobalSecondaryIndexOverride);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._LocalSecondaryIndexOverride);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ProvisionedThroughputOverride);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._OnDemandThroughputOverride);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._SSESpecificationOverride);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.RestoreTableToPointInTimeInput.RestoreTableToPointInTimeInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._SourceTableArn));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._SourceTableName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._TargetTableName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._UseLatestRestorableTime));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._RestoreDateTime));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._BillingModeOverride));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._GlobalSecondaryIndexOverride));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._LocalSecondaryIndexOverride));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ProvisionedThroughputOverride));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._OnDemandThroughputOverride));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._SSESpecificationOverride));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<RestoreTableToPointInTimeInput> _TYPE = dafny.TypeDescriptor.<RestoreTableToPointInTimeInput>referenceWithInitializer(RestoreTableToPointInTimeInput.class, () -> RestoreTableToPointInTimeInput.Default());
  public static dafny.TypeDescriptor<RestoreTableToPointInTimeInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<RestoreTableToPointInTimeInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final RestoreTableToPointInTimeInput theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.RestoreTableToPointInTimeInput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(TableArn._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(TableName._typeDescriptor()), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<Boolean>Default(dafny.TypeDescriptor.BOOLEAN), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<BillingMode>Default(BillingMode._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends GlobalSecondaryIndex>>Default(dafny.DafnySequence.<GlobalSecondaryIndex>_typeDescriptor(GlobalSecondaryIndex._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends LocalSecondaryIndex>>Default(dafny.DafnySequence.<LocalSecondaryIndex>_typeDescriptor(LocalSecondaryIndex._typeDescriptor())), Wrappers_Compile.Option.<ProvisionedThroughput>Default(ProvisionedThroughput._typeDescriptor()), Wrappers_Compile.Option.<OnDemandThroughput>Default(OnDemandThroughput._typeDescriptor()), Wrappers_Compile.Option.<SSESpecification>Default(SSESpecification._typeDescriptor()));
  public static RestoreTableToPointInTimeInput Default() {
    return theDefault;
  }
  public static RestoreTableToPointInTimeInput create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> SourceTableArn, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> SourceTableName, dafny.DafnySequence<? extends Character> TargetTableName, Wrappers_Compile.Option<Boolean> UseLatestRestorableTime, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> RestoreDateTime, Wrappers_Compile.Option<BillingMode> BillingModeOverride, Wrappers_Compile.Option<dafny.DafnySequence<? extends GlobalSecondaryIndex>> GlobalSecondaryIndexOverride, Wrappers_Compile.Option<dafny.DafnySequence<? extends LocalSecondaryIndex>> LocalSecondaryIndexOverride, Wrappers_Compile.Option<ProvisionedThroughput> ProvisionedThroughputOverride, Wrappers_Compile.Option<OnDemandThroughput> OnDemandThroughputOverride, Wrappers_Compile.Option<SSESpecification> SSESpecificationOverride) {
    return new RestoreTableToPointInTimeInput(SourceTableArn, SourceTableName, TargetTableName, UseLatestRestorableTime, RestoreDateTime, BillingModeOverride, GlobalSecondaryIndexOverride, LocalSecondaryIndexOverride, ProvisionedThroughputOverride, OnDemandThroughputOverride, SSESpecificationOverride);
  }
  public static RestoreTableToPointInTimeInput create_RestoreTableToPointInTimeInput(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> SourceTableArn, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> SourceTableName, dafny.DafnySequence<? extends Character> TargetTableName, Wrappers_Compile.Option<Boolean> UseLatestRestorableTime, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> RestoreDateTime, Wrappers_Compile.Option<BillingMode> BillingModeOverride, Wrappers_Compile.Option<dafny.DafnySequence<? extends GlobalSecondaryIndex>> GlobalSecondaryIndexOverride, Wrappers_Compile.Option<dafny.DafnySequence<? extends LocalSecondaryIndex>> LocalSecondaryIndexOverride, Wrappers_Compile.Option<ProvisionedThroughput> ProvisionedThroughputOverride, Wrappers_Compile.Option<OnDemandThroughput> OnDemandThroughputOverride, Wrappers_Compile.Option<SSESpecification> SSESpecificationOverride) {
    return create(SourceTableArn, SourceTableName, TargetTableName, UseLatestRestorableTime, RestoreDateTime, BillingModeOverride, GlobalSecondaryIndexOverride, LocalSecondaryIndexOverride, ProvisionedThroughputOverride, OnDemandThroughputOverride, SSESpecificationOverride);
  }
  public boolean is_RestoreTableToPointInTimeInput() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_SourceTableArn() {
    return this._SourceTableArn;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_SourceTableName() {
    return this._SourceTableName;
  }
  public dafny.DafnySequence<? extends Character> dtor_TargetTableName() {
    return this._TargetTableName;
  }
  public Wrappers_Compile.Option<Boolean> dtor_UseLatestRestorableTime() {
    return this._UseLatestRestorableTime;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_RestoreDateTime() {
    return this._RestoreDateTime;
  }
  public Wrappers_Compile.Option<BillingMode> dtor_BillingModeOverride() {
    return this._BillingModeOverride;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends GlobalSecondaryIndex>> dtor_GlobalSecondaryIndexOverride() {
    return this._GlobalSecondaryIndexOverride;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends LocalSecondaryIndex>> dtor_LocalSecondaryIndexOverride() {
    return this._LocalSecondaryIndexOverride;
  }
  public Wrappers_Compile.Option<ProvisionedThroughput> dtor_ProvisionedThroughputOverride() {
    return this._ProvisionedThroughputOverride;
  }
  public Wrappers_Compile.Option<OnDemandThroughput> dtor_OnDemandThroughputOverride() {
    return this._OnDemandThroughputOverride;
  }
  public Wrappers_Compile.Option<SSESpecification> dtor_SSESpecificationOverride() {
    return this._SSESpecificationOverride;
  }
}
