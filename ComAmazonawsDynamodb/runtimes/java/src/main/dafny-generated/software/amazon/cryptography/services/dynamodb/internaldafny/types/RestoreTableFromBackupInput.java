// Class RestoreTableFromBackupInput
// Dafny class RestoreTableFromBackupInput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class RestoreTableFromBackupInput {
  public dafny.DafnySequence<? extends Character> _TargetTableName;
  public dafny.DafnySequence<? extends Character> _BackupArn;
  public Wrappers_Compile.Option<BillingMode> _BillingModeOverride;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends GlobalSecondaryIndex>> _GlobalSecondaryIndexOverride;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends LocalSecondaryIndex>> _LocalSecondaryIndexOverride;
  public Wrappers_Compile.Option<ProvisionedThroughput> _ProvisionedThroughputOverride;
  public Wrappers_Compile.Option<OnDemandThroughput> _OnDemandThroughputOverride;
  public Wrappers_Compile.Option<SSESpecification> _SSESpecificationOverride;
  public RestoreTableFromBackupInput (dafny.DafnySequence<? extends Character> TargetTableName, dafny.DafnySequence<? extends Character> BackupArn, Wrappers_Compile.Option<BillingMode> BillingModeOverride, Wrappers_Compile.Option<dafny.DafnySequence<? extends GlobalSecondaryIndex>> GlobalSecondaryIndexOverride, Wrappers_Compile.Option<dafny.DafnySequence<? extends LocalSecondaryIndex>> LocalSecondaryIndexOverride, Wrappers_Compile.Option<ProvisionedThroughput> ProvisionedThroughputOverride, Wrappers_Compile.Option<OnDemandThroughput> OnDemandThroughputOverride, Wrappers_Compile.Option<SSESpecification> SSESpecificationOverride) {
    this._TargetTableName = TargetTableName;
    this._BackupArn = BackupArn;
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
    RestoreTableFromBackupInput o = (RestoreTableFromBackupInput)other;
    return true && java.util.Objects.equals(this._TargetTableName, o._TargetTableName) && java.util.Objects.equals(this._BackupArn, o._BackupArn) && java.util.Objects.equals(this._BillingModeOverride, o._BillingModeOverride) && java.util.Objects.equals(this._GlobalSecondaryIndexOverride, o._GlobalSecondaryIndexOverride) && java.util.Objects.equals(this._LocalSecondaryIndexOverride, o._LocalSecondaryIndexOverride) && java.util.Objects.equals(this._ProvisionedThroughputOverride, o._ProvisionedThroughputOverride) && java.util.Objects.equals(this._OnDemandThroughputOverride, o._OnDemandThroughputOverride) && java.util.Objects.equals(this._SSESpecificationOverride, o._SSESpecificationOverride);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TargetTableName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._BackupArn);
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
    s.append("ComAmazonawsDynamodbTypes.RestoreTableFromBackupInput.RestoreTableFromBackupInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._TargetTableName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._BackupArn));
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
  private static final dafny.TypeDescriptor<RestoreTableFromBackupInput> _TYPE = dafny.TypeDescriptor.<RestoreTableFromBackupInput>referenceWithInitializer(RestoreTableFromBackupInput.class, () -> RestoreTableFromBackupInput.Default());
  public static dafny.TypeDescriptor<RestoreTableFromBackupInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<RestoreTableFromBackupInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final RestoreTableFromBackupInput theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.RestoreTableFromBackupInput.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<BillingMode>Default(BillingMode._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends GlobalSecondaryIndex>>Default(dafny.DafnySequence.<GlobalSecondaryIndex>_typeDescriptor(GlobalSecondaryIndex._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends LocalSecondaryIndex>>Default(dafny.DafnySequence.<LocalSecondaryIndex>_typeDescriptor(LocalSecondaryIndex._typeDescriptor())), Wrappers_Compile.Option.<ProvisionedThroughput>Default(ProvisionedThroughput._typeDescriptor()), Wrappers_Compile.Option.<OnDemandThroughput>Default(OnDemandThroughput._typeDescriptor()), Wrappers_Compile.Option.<SSESpecification>Default(SSESpecification._typeDescriptor()));
  public static RestoreTableFromBackupInput Default() {
    return theDefault;
  }
  public static RestoreTableFromBackupInput create(dafny.DafnySequence<? extends Character> TargetTableName, dafny.DafnySequence<? extends Character> BackupArn, Wrappers_Compile.Option<BillingMode> BillingModeOverride, Wrappers_Compile.Option<dafny.DafnySequence<? extends GlobalSecondaryIndex>> GlobalSecondaryIndexOverride, Wrappers_Compile.Option<dafny.DafnySequence<? extends LocalSecondaryIndex>> LocalSecondaryIndexOverride, Wrappers_Compile.Option<ProvisionedThroughput> ProvisionedThroughputOverride, Wrappers_Compile.Option<OnDemandThroughput> OnDemandThroughputOverride, Wrappers_Compile.Option<SSESpecification> SSESpecificationOverride) {
    return new RestoreTableFromBackupInput(TargetTableName, BackupArn, BillingModeOverride, GlobalSecondaryIndexOverride, LocalSecondaryIndexOverride, ProvisionedThroughputOverride, OnDemandThroughputOverride, SSESpecificationOverride);
  }
  public static RestoreTableFromBackupInput create_RestoreTableFromBackupInput(dafny.DafnySequence<? extends Character> TargetTableName, dafny.DafnySequence<? extends Character> BackupArn, Wrappers_Compile.Option<BillingMode> BillingModeOverride, Wrappers_Compile.Option<dafny.DafnySequence<? extends GlobalSecondaryIndex>> GlobalSecondaryIndexOverride, Wrappers_Compile.Option<dafny.DafnySequence<? extends LocalSecondaryIndex>> LocalSecondaryIndexOverride, Wrappers_Compile.Option<ProvisionedThroughput> ProvisionedThroughputOverride, Wrappers_Compile.Option<OnDemandThroughput> OnDemandThroughputOverride, Wrappers_Compile.Option<SSESpecification> SSESpecificationOverride) {
    return create(TargetTableName, BackupArn, BillingModeOverride, GlobalSecondaryIndexOverride, LocalSecondaryIndexOverride, ProvisionedThroughputOverride, OnDemandThroughputOverride, SSESpecificationOverride);
  }
  public boolean is_RestoreTableFromBackupInput() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_TargetTableName() {
    return this._TargetTableName;
  }
  public dafny.DafnySequence<? extends Character> dtor_BackupArn() {
    return this._BackupArn;
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
