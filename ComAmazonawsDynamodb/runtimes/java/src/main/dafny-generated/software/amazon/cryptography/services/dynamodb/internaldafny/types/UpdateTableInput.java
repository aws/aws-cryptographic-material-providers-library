// Class UpdateTableInput
// Dafny class UpdateTableInput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class UpdateTableInput {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends AttributeDefinition>> _AttributeDefinitions;
  public dafny.DafnySequence<? extends Character> _TableName;
  public Wrappers_Compile.Option<BillingMode> _BillingMode;
  public Wrappers_Compile.Option<ProvisionedThroughput> _ProvisionedThroughput;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends GlobalSecondaryIndexUpdate>> _GlobalSecondaryIndexUpdates;
  public Wrappers_Compile.Option<StreamSpecification> _StreamSpecification;
  public Wrappers_Compile.Option<SSESpecification> _SSESpecification;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicationGroupUpdate>> _ReplicaUpdates;
  public Wrappers_Compile.Option<TableClass> _TableClass;
  public Wrappers_Compile.Option<Boolean> _DeletionProtectionEnabled;
  public Wrappers_Compile.Option<OnDemandThroughput> _OnDemandThroughput;
  public UpdateTableInput (Wrappers_Compile.Option<dafny.DafnySequence<? extends AttributeDefinition>> AttributeDefinitions, dafny.DafnySequence<? extends Character> TableName, Wrappers_Compile.Option<BillingMode> BillingMode, Wrappers_Compile.Option<ProvisionedThroughput> ProvisionedThroughput, Wrappers_Compile.Option<dafny.DafnySequence<? extends GlobalSecondaryIndexUpdate>> GlobalSecondaryIndexUpdates, Wrappers_Compile.Option<StreamSpecification> StreamSpecification, Wrappers_Compile.Option<SSESpecification> SSESpecification, Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicationGroupUpdate>> ReplicaUpdates, Wrappers_Compile.Option<TableClass> TableClass, Wrappers_Compile.Option<Boolean> DeletionProtectionEnabled, Wrappers_Compile.Option<OnDemandThroughput> OnDemandThroughput) {
    this._AttributeDefinitions = AttributeDefinitions;
    this._TableName = TableName;
    this._BillingMode = BillingMode;
    this._ProvisionedThroughput = ProvisionedThroughput;
    this._GlobalSecondaryIndexUpdates = GlobalSecondaryIndexUpdates;
    this._StreamSpecification = StreamSpecification;
    this._SSESpecification = SSESpecification;
    this._ReplicaUpdates = ReplicaUpdates;
    this._TableClass = TableClass;
    this._DeletionProtectionEnabled = DeletionProtectionEnabled;
    this._OnDemandThroughput = OnDemandThroughput;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    UpdateTableInput o = (UpdateTableInput)other;
    return true && java.util.Objects.equals(this._AttributeDefinitions, o._AttributeDefinitions) && java.util.Objects.equals(this._TableName, o._TableName) && java.util.Objects.equals(this._BillingMode, o._BillingMode) && java.util.Objects.equals(this._ProvisionedThroughput, o._ProvisionedThroughput) && java.util.Objects.equals(this._GlobalSecondaryIndexUpdates, o._GlobalSecondaryIndexUpdates) && java.util.Objects.equals(this._StreamSpecification, o._StreamSpecification) && java.util.Objects.equals(this._SSESpecification, o._SSESpecification) && java.util.Objects.equals(this._ReplicaUpdates, o._ReplicaUpdates) && java.util.Objects.equals(this._TableClass, o._TableClass) && java.util.Objects.equals(this._DeletionProtectionEnabled, o._DeletionProtectionEnabled) && java.util.Objects.equals(this._OnDemandThroughput, o._OnDemandThroughput);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._AttributeDefinitions);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._BillingMode);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ProvisionedThroughput);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._GlobalSecondaryIndexUpdates);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._StreamSpecification);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._SSESpecification);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReplicaUpdates);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableClass);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._DeletionProtectionEnabled);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._OnDemandThroughput);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.UpdateTableInput.UpdateTableInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._AttributeDefinitions));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._TableName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._BillingMode));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ProvisionedThroughput));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._GlobalSecondaryIndexUpdates));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._StreamSpecification));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._SSESpecification));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ReplicaUpdates));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._TableClass));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._DeletionProtectionEnabled));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._OnDemandThroughput));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<UpdateTableInput> _TYPE = dafny.TypeDescriptor.<UpdateTableInput>referenceWithInitializer(UpdateTableInput.class, () -> UpdateTableInput.Default());
  public static dafny.TypeDescriptor<UpdateTableInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<UpdateTableInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final UpdateTableInput theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.UpdateTableInput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends AttributeDefinition>>Default(dafny.DafnySequence.<AttributeDefinition>_typeDescriptor(AttributeDefinition._typeDescriptor())), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<BillingMode>Default(BillingMode._typeDescriptor()), Wrappers_Compile.Option.<ProvisionedThroughput>Default(ProvisionedThroughput._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends GlobalSecondaryIndexUpdate>>Default(dafny.DafnySequence.<GlobalSecondaryIndexUpdate>_typeDescriptor(GlobalSecondaryIndexUpdate._typeDescriptor())), Wrappers_Compile.Option.<StreamSpecification>Default(StreamSpecification._typeDescriptor()), Wrappers_Compile.Option.<SSESpecification>Default(SSESpecification._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends ReplicationGroupUpdate>>Default(ReplicationGroupUpdateList._typeDescriptor()), Wrappers_Compile.Option.<TableClass>Default(TableClass._typeDescriptor()), Wrappers_Compile.Option.<Boolean>Default(dafny.TypeDescriptor.BOOLEAN), Wrappers_Compile.Option.<OnDemandThroughput>Default(OnDemandThroughput._typeDescriptor()));
  public static UpdateTableInput Default() {
    return theDefault;
  }
  public static UpdateTableInput create(Wrappers_Compile.Option<dafny.DafnySequence<? extends AttributeDefinition>> AttributeDefinitions, dafny.DafnySequence<? extends Character> TableName, Wrappers_Compile.Option<BillingMode> BillingMode, Wrappers_Compile.Option<ProvisionedThroughput> ProvisionedThroughput, Wrappers_Compile.Option<dafny.DafnySequence<? extends GlobalSecondaryIndexUpdate>> GlobalSecondaryIndexUpdates, Wrappers_Compile.Option<StreamSpecification> StreamSpecification, Wrappers_Compile.Option<SSESpecification> SSESpecification, Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicationGroupUpdate>> ReplicaUpdates, Wrappers_Compile.Option<TableClass> TableClass, Wrappers_Compile.Option<Boolean> DeletionProtectionEnabled, Wrappers_Compile.Option<OnDemandThroughput> OnDemandThroughput) {
    return new UpdateTableInput(AttributeDefinitions, TableName, BillingMode, ProvisionedThroughput, GlobalSecondaryIndexUpdates, StreamSpecification, SSESpecification, ReplicaUpdates, TableClass, DeletionProtectionEnabled, OnDemandThroughput);
  }
  public static UpdateTableInput create_UpdateTableInput(Wrappers_Compile.Option<dafny.DafnySequence<? extends AttributeDefinition>> AttributeDefinitions, dafny.DafnySequence<? extends Character> TableName, Wrappers_Compile.Option<BillingMode> BillingMode, Wrappers_Compile.Option<ProvisionedThroughput> ProvisionedThroughput, Wrappers_Compile.Option<dafny.DafnySequence<? extends GlobalSecondaryIndexUpdate>> GlobalSecondaryIndexUpdates, Wrappers_Compile.Option<StreamSpecification> StreamSpecification, Wrappers_Compile.Option<SSESpecification> SSESpecification, Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicationGroupUpdate>> ReplicaUpdates, Wrappers_Compile.Option<TableClass> TableClass, Wrappers_Compile.Option<Boolean> DeletionProtectionEnabled, Wrappers_Compile.Option<OnDemandThroughput> OnDemandThroughput) {
    return create(AttributeDefinitions, TableName, BillingMode, ProvisionedThroughput, GlobalSecondaryIndexUpdates, StreamSpecification, SSESpecification, ReplicaUpdates, TableClass, DeletionProtectionEnabled, OnDemandThroughput);
  }
  public boolean is_UpdateTableInput() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends AttributeDefinition>> dtor_AttributeDefinitions() {
    return this._AttributeDefinitions;
  }
  public dafny.DafnySequence<? extends Character> dtor_TableName() {
    return this._TableName;
  }
  public Wrappers_Compile.Option<BillingMode> dtor_BillingMode() {
    return this._BillingMode;
  }
  public Wrappers_Compile.Option<ProvisionedThroughput> dtor_ProvisionedThroughput() {
    return this._ProvisionedThroughput;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends GlobalSecondaryIndexUpdate>> dtor_GlobalSecondaryIndexUpdates() {
    return this._GlobalSecondaryIndexUpdates;
  }
  public Wrappers_Compile.Option<StreamSpecification> dtor_StreamSpecification() {
    return this._StreamSpecification;
  }
  public Wrappers_Compile.Option<SSESpecification> dtor_SSESpecification() {
    return this._SSESpecification;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends ReplicationGroupUpdate>> dtor_ReplicaUpdates() {
    return this._ReplicaUpdates;
  }
  public Wrappers_Compile.Option<TableClass> dtor_TableClass() {
    return this._TableClass;
  }
  public Wrappers_Compile.Option<Boolean> dtor_DeletionProtectionEnabled() {
    return this._DeletionProtectionEnabled;
  }
  public Wrappers_Compile.Option<OnDemandThroughput> dtor_OnDemandThroughput() {
    return this._OnDemandThroughput;
  }
}
