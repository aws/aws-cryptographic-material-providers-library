// Class TableDescription
// Dafny class TableDescription compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class TableDescription {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends AttributeDefinition>> _AttributeDefinitions;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _TableName;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends KeySchemaElement>> _KeySchema;
  public Wrappers_Compile.Option<TableStatus> _TableStatus;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _CreationDateTime;
  public Wrappers_Compile.Option<ProvisionedThroughputDescription> _ProvisionedThroughput;
  public Wrappers_Compile.Option<java.lang.Long> _TableSizeBytes;
  public Wrappers_Compile.Option<java.lang.Long> _ItemCount;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _TableArn;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _TableId;
  public Wrappers_Compile.Option<BillingModeSummary> _BillingModeSummary;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends LocalSecondaryIndexDescription>> _LocalSecondaryIndexes;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends GlobalSecondaryIndexDescription>> _GlobalSecondaryIndexes;
  public Wrappers_Compile.Option<StreamSpecification> _StreamSpecification;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _LatestStreamLabel;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _LatestStreamArn;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _GlobalTableVersion;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaDescription>> _Replicas;
  public Wrappers_Compile.Option<RestoreSummary> _RestoreSummary;
  public Wrappers_Compile.Option<SSEDescription> _SSEDescription;
  public Wrappers_Compile.Option<ArchivalSummary> _ArchivalSummary;
  public Wrappers_Compile.Option<TableClassSummary> _TableClassSummary;
  public Wrappers_Compile.Option<Boolean> _DeletionProtectionEnabled;
  public Wrappers_Compile.Option<OnDemandThroughput> _OnDemandThroughput;
  public TableDescription (Wrappers_Compile.Option<dafny.DafnySequence<? extends AttributeDefinition>> AttributeDefinitions, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableName, Wrappers_Compile.Option<dafny.DafnySequence<? extends KeySchemaElement>> KeySchema, Wrappers_Compile.Option<TableStatus> TableStatus, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CreationDateTime, Wrappers_Compile.Option<ProvisionedThroughputDescription> ProvisionedThroughput, Wrappers_Compile.Option<java.lang.Long> TableSizeBytes, Wrappers_Compile.Option<java.lang.Long> ItemCount, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableArn, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableId, Wrappers_Compile.Option<BillingModeSummary> BillingModeSummary, Wrappers_Compile.Option<dafny.DafnySequence<? extends LocalSecondaryIndexDescription>> LocalSecondaryIndexes, Wrappers_Compile.Option<dafny.DafnySequence<? extends GlobalSecondaryIndexDescription>> GlobalSecondaryIndexes, Wrappers_Compile.Option<StreamSpecification> StreamSpecification, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> LatestStreamLabel, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> LatestStreamArn, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> GlobalTableVersion, Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaDescription>> Replicas, Wrappers_Compile.Option<RestoreSummary> RestoreSummary, Wrappers_Compile.Option<SSEDescription> SSEDescription, Wrappers_Compile.Option<ArchivalSummary> ArchivalSummary, Wrappers_Compile.Option<TableClassSummary> TableClassSummary, Wrappers_Compile.Option<Boolean> DeletionProtectionEnabled, Wrappers_Compile.Option<OnDemandThroughput> OnDemandThroughput) {
    this._AttributeDefinitions = AttributeDefinitions;
    this._TableName = TableName;
    this._KeySchema = KeySchema;
    this._TableStatus = TableStatus;
    this._CreationDateTime = CreationDateTime;
    this._ProvisionedThroughput = ProvisionedThroughput;
    this._TableSizeBytes = TableSizeBytes;
    this._ItemCount = ItemCount;
    this._TableArn = TableArn;
    this._TableId = TableId;
    this._BillingModeSummary = BillingModeSummary;
    this._LocalSecondaryIndexes = LocalSecondaryIndexes;
    this._GlobalSecondaryIndexes = GlobalSecondaryIndexes;
    this._StreamSpecification = StreamSpecification;
    this._LatestStreamLabel = LatestStreamLabel;
    this._LatestStreamArn = LatestStreamArn;
    this._GlobalTableVersion = GlobalTableVersion;
    this._Replicas = Replicas;
    this._RestoreSummary = RestoreSummary;
    this._SSEDescription = SSEDescription;
    this._ArchivalSummary = ArchivalSummary;
    this._TableClassSummary = TableClassSummary;
    this._DeletionProtectionEnabled = DeletionProtectionEnabled;
    this._OnDemandThroughput = OnDemandThroughput;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    TableDescription o = (TableDescription)other;
    return true && java.util.Objects.equals(this._AttributeDefinitions, o._AttributeDefinitions) && java.util.Objects.equals(this._TableName, o._TableName) && java.util.Objects.equals(this._KeySchema, o._KeySchema) && java.util.Objects.equals(this._TableStatus, o._TableStatus) && java.util.Objects.equals(this._CreationDateTime, o._CreationDateTime) && java.util.Objects.equals(this._ProvisionedThroughput, o._ProvisionedThroughput) && java.util.Objects.equals(this._TableSizeBytes, o._TableSizeBytes) && java.util.Objects.equals(this._ItemCount, o._ItemCount) && java.util.Objects.equals(this._TableArn, o._TableArn) && java.util.Objects.equals(this._TableId, o._TableId) && java.util.Objects.equals(this._BillingModeSummary, o._BillingModeSummary) && java.util.Objects.equals(this._LocalSecondaryIndexes, o._LocalSecondaryIndexes) && java.util.Objects.equals(this._GlobalSecondaryIndexes, o._GlobalSecondaryIndexes) && java.util.Objects.equals(this._StreamSpecification, o._StreamSpecification) && java.util.Objects.equals(this._LatestStreamLabel, o._LatestStreamLabel) && java.util.Objects.equals(this._LatestStreamArn, o._LatestStreamArn) && java.util.Objects.equals(this._GlobalTableVersion, o._GlobalTableVersion) && java.util.Objects.equals(this._Replicas, o._Replicas) && java.util.Objects.equals(this._RestoreSummary, o._RestoreSummary) && java.util.Objects.equals(this._SSEDescription, o._SSEDescription) && java.util.Objects.equals(this._ArchivalSummary, o._ArchivalSummary) && java.util.Objects.equals(this._TableClassSummary, o._TableClassSummary) && java.util.Objects.equals(this._DeletionProtectionEnabled, o._DeletionProtectionEnabled) && java.util.Objects.equals(this._OnDemandThroughput, o._OnDemandThroughput);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._AttributeDefinitions);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeySchema);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableStatus);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._CreationDateTime);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ProvisionedThroughput);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableSizeBytes);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ItemCount);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableArn);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._BillingModeSummary);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._LocalSecondaryIndexes);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._GlobalSecondaryIndexes);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._StreamSpecification);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._LatestStreamLabel);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._LatestStreamArn);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._GlobalTableVersion);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Replicas);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._RestoreSummary);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._SSEDescription);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ArchivalSummary);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableClassSummary);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._DeletionProtectionEnabled);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._OnDemandThroughput);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.TableDescription.TableDescription");
    s.append("(");
    s.append(dafny.Helpers.toString(this._AttributeDefinitions));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._TableName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._KeySchema));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._TableStatus));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._CreationDateTime));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ProvisionedThroughput));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._TableSizeBytes));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ItemCount));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._TableArn));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._TableId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._BillingModeSummary));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._LocalSecondaryIndexes));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._GlobalSecondaryIndexes));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._StreamSpecification));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._LatestStreamLabel));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._LatestStreamArn));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._GlobalTableVersion));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Replicas));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._RestoreSummary));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._SSEDescription));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ArchivalSummary));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._TableClassSummary));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._DeletionProtectionEnabled));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._OnDemandThroughput));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<TableDescription> _TYPE = dafny.TypeDescriptor.<TableDescription>referenceWithInitializer(TableDescription.class, () -> TableDescription.Default());
  public static dafny.TypeDescriptor<TableDescription> _typeDescriptor() {
    return (dafny.TypeDescriptor<TableDescription>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final TableDescription theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.TableDescription.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends AttributeDefinition>>Default(dafny.DafnySequence.<AttributeDefinition>_typeDescriptor(AttributeDefinition._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(TableName._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends KeySchemaElement>>Default(KeySchema._typeDescriptor()), Wrappers_Compile.Option.<TableStatus>Default(TableStatus._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<ProvisionedThroughputDescription>Default(ProvisionedThroughputDescription._typeDescriptor()), Wrappers_Compile.Option.<java.lang.Long>Default(BoundedInts_Compile.int64._typeDescriptor()), Wrappers_Compile.Option.<java.lang.Long>Default(BoundedInts_Compile.int64._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<BillingModeSummary>Default(BillingModeSummary._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends LocalSecondaryIndexDescription>>Default(dafny.DafnySequence.<LocalSecondaryIndexDescription>_typeDescriptor(LocalSecondaryIndexDescription._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends GlobalSecondaryIndexDescription>>Default(dafny.DafnySequence.<GlobalSecondaryIndexDescription>_typeDescriptor(GlobalSecondaryIndexDescription._typeDescriptor())), Wrappers_Compile.Option.<StreamSpecification>Default(StreamSpecification._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(StreamArn._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends ReplicaDescription>>Default(dafny.DafnySequence.<ReplicaDescription>_typeDescriptor(ReplicaDescription._typeDescriptor())), Wrappers_Compile.Option.<RestoreSummary>Default(RestoreSummary._typeDescriptor()), Wrappers_Compile.Option.<SSEDescription>Default(SSEDescription._typeDescriptor()), Wrappers_Compile.Option.<ArchivalSummary>Default(ArchivalSummary._typeDescriptor()), Wrappers_Compile.Option.<TableClassSummary>Default(TableClassSummary._typeDescriptor()), Wrappers_Compile.Option.<Boolean>Default(dafny.TypeDescriptor.BOOLEAN), Wrappers_Compile.Option.<OnDemandThroughput>Default(OnDemandThroughput._typeDescriptor()));
  public static TableDescription Default() {
    return theDefault;
  }
  public static TableDescription create(Wrappers_Compile.Option<dafny.DafnySequence<? extends AttributeDefinition>> AttributeDefinitions, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableName, Wrappers_Compile.Option<dafny.DafnySequence<? extends KeySchemaElement>> KeySchema, Wrappers_Compile.Option<TableStatus> TableStatus, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CreationDateTime, Wrappers_Compile.Option<ProvisionedThroughputDescription> ProvisionedThroughput, Wrappers_Compile.Option<java.lang.Long> TableSizeBytes, Wrappers_Compile.Option<java.lang.Long> ItemCount, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableArn, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableId, Wrappers_Compile.Option<BillingModeSummary> BillingModeSummary, Wrappers_Compile.Option<dafny.DafnySequence<? extends LocalSecondaryIndexDescription>> LocalSecondaryIndexes, Wrappers_Compile.Option<dafny.DafnySequence<? extends GlobalSecondaryIndexDescription>> GlobalSecondaryIndexes, Wrappers_Compile.Option<StreamSpecification> StreamSpecification, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> LatestStreamLabel, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> LatestStreamArn, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> GlobalTableVersion, Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaDescription>> Replicas, Wrappers_Compile.Option<RestoreSummary> RestoreSummary, Wrappers_Compile.Option<SSEDescription> SSEDescription, Wrappers_Compile.Option<ArchivalSummary> ArchivalSummary, Wrappers_Compile.Option<TableClassSummary> TableClassSummary, Wrappers_Compile.Option<Boolean> DeletionProtectionEnabled, Wrappers_Compile.Option<OnDemandThroughput> OnDemandThroughput) {
    return new TableDescription(AttributeDefinitions, TableName, KeySchema, TableStatus, CreationDateTime, ProvisionedThroughput, TableSizeBytes, ItemCount, TableArn, TableId, BillingModeSummary, LocalSecondaryIndexes, GlobalSecondaryIndexes, StreamSpecification, LatestStreamLabel, LatestStreamArn, GlobalTableVersion, Replicas, RestoreSummary, SSEDescription, ArchivalSummary, TableClassSummary, DeletionProtectionEnabled, OnDemandThroughput);
  }
  public static TableDescription create_TableDescription(Wrappers_Compile.Option<dafny.DafnySequence<? extends AttributeDefinition>> AttributeDefinitions, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableName, Wrappers_Compile.Option<dafny.DafnySequence<? extends KeySchemaElement>> KeySchema, Wrappers_Compile.Option<TableStatus> TableStatus, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CreationDateTime, Wrappers_Compile.Option<ProvisionedThroughputDescription> ProvisionedThroughput, Wrappers_Compile.Option<java.lang.Long> TableSizeBytes, Wrappers_Compile.Option<java.lang.Long> ItemCount, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableArn, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableId, Wrappers_Compile.Option<BillingModeSummary> BillingModeSummary, Wrappers_Compile.Option<dafny.DafnySequence<? extends LocalSecondaryIndexDescription>> LocalSecondaryIndexes, Wrappers_Compile.Option<dafny.DafnySequence<? extends GlobalSecondaryIndexDescription>> GlobalSecondaryIndexes, Wrappers_Compile.Option<StreamSpecification> StreamSpecification, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> LatestStreamLabel, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> LatestStreamArn, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> GlobalTableVersion, Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaDescription>> Replicas, Wrappers_Compile.Option<RestoreSummary> RestoreSummary, Wrappers_Compile.Option<SSEDescription> SSEDescription, Wrappers_Compile.Option<ArchivalSummary> ArchivalSummary, Wrappers_Compile.Option<TableClassSummary> TableClassSummary, Wrappers_Compile.Option<Boolean> DeletionProtectionEnabled, Wrappers_Compile.Option<OnDemandThroughput> OnDemandThroughput) {
    return create(AttributeDefinitions, TableName, KeySchema, TableStatus, CreationDateTime, ProvisionedThroughput, TableSizeBytes, ItemCount, TableArn, TableId, BillingModeSummary, LocalSecondaryIndexes, GlobalSecondaryIndexes, StreamSpecification, LatestStreamLabel, LatestStreamArn, GlobalTableVersion, Replicas, RestoreSummary, SSEDescription, ArchivalSummary, TableClassSummary, DeletionProtectionEnabled, OnDemandThroughput);
  }
  public boolean is_TableDescription() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends AttributeDefinition>> dtor_AttributeDefinitions() {
    return this._AttributeDefinitions;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_TableName() {
    return this._TableName;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends KeySchemaElement>> dtor_KeySchema() {
    return this._KeySchema;
  }
  public Wrappers_Compile.Option<TableStatus> dtor_TableStatus() {
    return this._TableStatus;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_CreationDateTime() {
    return this._CreationDateTime;
  }
  public Wrappers_Compile.Option<ProvisionedThroughputDescription> dtor_ProvisionedThroughput() {
    return this._ProvisionedThroughput;
  }
  public Wrappers_Compile.Option<java.lang.Long> dtor_TableSizeBytes() {
    return this._TableSizeBytes;
  }
  public Wrappers_Compile.Option<java.lang.Long> dtor_ItemCount() {
    return this._ItemCount;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_TableArn() {
    return this._TableArn;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_TableId() {
    return this._TableId;
  }
  public Wrappers_Compile.Option<BillingModeSummary> dtor_BillingModeSummary() {
    return this._BillingModeSummary;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends LocalSecondaryIndexDescription>> dtor_LocalSecondaryIndexes() {
    return this._LocalSecondaryIndexes;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends GlobalSecondaryIndexDescription>> dtor_GlobalSecondaryIndexes() {
    return this._GlobalSecondaryIndexes;
  }
  public Wrappers_Compile.Option<StreamSpecification> dtor_StreamSpecification() {
    return this._StreamSpecification;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_LatestStreamLabel() {
    return this._LatestStreamLabel;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_LatestStreamArn() {
    return this._LatestStreamArn;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_GlobalTableVersion() {
    return this._GlobalTableVersion;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicaDescription>> dtor_Replicas() {
    return this._Replicas;
  }
  public Wrappers_Compile.Option<RestoreSummary> dtor_RestoreSummary() {
    return this._RestoreSummary;
  }
  public Wrappers_Compile.Option<SSEDescription> dtor_SSEDescription() {
    return this._SSEDescription;
  }
  public Wrappers_Compile.Option<ArchivalSummary> dtor_ArchivalSummary() {
    return this._ArchivalSummary;
  }
  public Wrappers_Compile.Option<TableClassSummary> dtor_TableClassSummary() {
    return this._TableClassSummary;
  }
  public Wrappers_Compile.Option<Boolean> dtor_DeletionProtectionEnabled() {
    return this._DeletionProtectionEnabled;
  }
  public Wrappers_Compile.Option<OnDemandThroughput> dtor_OnDemandThroughput() {
    return this._OnDemandThroughput;
  }
}
