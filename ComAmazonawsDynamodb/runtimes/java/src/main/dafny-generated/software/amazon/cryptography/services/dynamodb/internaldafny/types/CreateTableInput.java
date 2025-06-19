// Class CreateTableInput
// Dafny class CreateTableInput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class CreateTableInput {
  public dafny.DafnySequence<? extends AttributeDefinition> _AttributeDefinitions;
  public dafny.DafnySequence<? extends Character> _TableName;
  public dafny.DafnySequence<? extends KeySchemaElement> _KeySchema;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends LocalSecondaryIndex>> _LocalSecondaryIndexes;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends GlobalSecondaryIndex>> _GlobalSecondaryIndexes;
  public Wrappers_Compile.Option<BillingMode> _BillingMode;
  public Wrappers_Compile.Option<ProvisionedThroughput> _ProvisionedThroughput;
  public Wrappers_Compile.Option<StreamSpecification> _StreamSpecification;
  public Wrappers_Compile.Option<SSESpecification> _SSESpecification;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Tag>> _Tags;
  public Wrappers_Compile.Option<TableClass> _TableClass;
  public Wrappers_Compile.Option<Boolean> _DeletionProtectionEnabled;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _ResourcePolicy;
  public Wrappers_Compile.Option<OnDemandThroughput> _OnDemandThroughput;
  public CreateTableInput (dafny.DafnySequence<? extends AttributeDefinition> AttributeDefinitions, dafny.DafnySequence<? extends Character> TableName, dafny.DafnySequence<? extends KeySchemaElement> KeySchema, Wrappers_Compile.Option<dafny.DafnySequence<? extends LocalSecondaryIndex>> LocalSecondaryIndexes, Wrappers_Compile.Option<dafny.DafnySequence<? extends GlobalSecondaryIndex>> GlobalSecondaryIndexes, Wrappers_Compile.Option<BillingMode> BillingMode, Wrappers_Compile.Option<ProvisionedThroughput> ProvisionedThroughput, Wrappers_Compile.Option<StreamSpecification> StreamSpecification, Wrappers_Compile.Option<SSESpecification> SSESpecification, Wrappers_Compile.Option<dafny.DafnySequence<? extends Tag>> Tags, Wrappers_Compile.Option<TableClass> TableClass, Wrappers_Compile.Option<Boolean> DeletionProtectionEnabled, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ResourcePolicy, Wrappers_Compile.Option<OnDemandThroughput> OnDemandThroughput) {
    this._AttributeDefinitions = AttributeDefinitions;
    this._TableName = TableName;
    this._KeySchema = KeySchema;
    this._LocalSecondaryIndexes = LocalSecondaryIndexes;
    this._GlobalSecondaryIndexes = GlobalSecondaryIndexes;
    this._BillingMode = BillingMode;
    this._ProvisionedThroughput = ProvisionedThroughput;
    this._StreamSpecification = StreamSpecification;
    this._SSESpecification = SSESpecification;
    this._Tags = Tags;
    this._TableClass = TableClass;
    this._DeletionProtectionEnabled = DeletionProtectionEnabled;
    this._ResourcePolicy = ResourcePolicy;
    this._OnDemandThroughput = OnDemandThroughput;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CreateTableInput o = (CreateTableInput)other;
    return true && java.util.Objects.equals(this._AttributeDefinitions, o._AttributeDefinitions) && java.util.Objects.equals(this._TableName, o._TableName) && java.util.Objects.equals(this._KeySchema, o._KeySchema) && java.util.Objects.equals(this._LocalSecondaryIndexes, o._LocalSecondaryIndexes) && java.util.Objects.equals(this._GlobalSecondaryIndexes, o._GlobalSecondaryIndexes) && java.util.Objects.equals(this._BillingMode, o._BillingMode) && java.util.Objects.equals(this._ProvisionedThroughput, o._ProvisionedThroughput) && java.util.Objects.equals(this._StreamSpecification, o._StreamSpecification) && java.util.Objects.equals(this._SSESpecification, o._SSESpecification) && java.util.Objects.equals(this._Tags, o._Tags) && java.util.Objects.equals(this._TableClass, o._TableClass) && java.util.Objects.equals(this._DeletionProtectionEnabled, o._DeletionProtectionEnabled) && java.util.Objects.equals(this._ResourcePolicy, o._ResourcePolicy) && java.util.Objects.equals(this._OnDemandThroughput, o._OnDemandThroughput);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._AttributeDefinitions);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeySchema);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._LocalSecondaryIndexes);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._GlobalSecondaryIndexes);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._BillingMode);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ProvisionedThroughput);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._StreamSpecification);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._SSESpecification);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Tags);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableClass);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._DeletionProtectionEnabled);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ResourcePolicy);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._OnDemandThroughput);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.CreateTableInput.CreateTableInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._AttributeDefinitions));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._TableName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._KeySchema));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._LocalSecondaryIndexes));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._GlobalSecondaryIndexes));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._BillingMode));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ProvisionedThroughput));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._StreamSpecification));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._SSESpecification));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Tags));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._TableClass));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._DeletionProtectionEnabled));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ResourcePolicy));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._OnDemandThroughput));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<CreateTableInput> _TYPE = dafny.TypeDescriptor.<CreateTableInput>referenceWithInitializer(CreateTableInput.class, () -> CreateTableInput.Default());
  public static dafny.TypeDescriptor<CreateTableInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<CreateTableInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final CreateTableInput theDefault = CreateTableInput.create(dafny.DafnySequence.<AttributeDefinition> empty(AttributeDefinition._typeDescriptor()), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<KeySchemaElement> empty(KeySchemaElement._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends LocalSecondaryIndex>>Default(dafny.DafnySequence.<LocalSecondaryIndex>_typeDescriptor(LocalSecondaryIndex._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends GlobalSecondaryIndex>>Default(dafny.DafnySequence.<GlobalSecondaryIndex>_typeDescriptor(GlobalSecondaryIndex._typeDescriptor())), Wrappers_Compile.Option.<BillingMode>Default(BillingMode._typeDescriptor()), Wrappers_Compile.Option.<ProvisionedThroughput>Default(ProvisionedThroughput._typeDescriptor()), Wrappers_Compile.Option.<StreamSpecification>Default(StreamSpecification._typeDescriptor()), Wrappers_Compile.Option.<SSESpecification>Default(SSESpecification._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Tag>>Default(dafny.DafnySequence.<Tag>_typeDescriptor(Tag._typeDescriptor())), Wrappers_Compile.Option.<TableClass>Default(TableClass._typeDescriptor()), Wrappers_Compile.Option.<Boolean>Default(dafny.TypeDescriptor.BOOLEAN), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<OnDemandThroughput>Default(OnDemandThroughput._typeDescriptor()));
  public static CreateTableInput Default() {
    return theDefault;
  }
  public static CreateTableInput create(dafny.DafnySequence<? extends AttributeDefinition> AttributeDefinitions, dafny.DafnySequence<? extends Character> TableName, dafny.DafnySequence<? extends KeySchemaElement> KeySchema, Wrappers_Compile.Option<dafny.DafnySequence<? extends LocalSecondaryIndex>> LocalSecondaryIndexes, Wrappers_Compile.Option<dafny.DafnySequence<? extends GlobalSecondaryIndex>> GlobalSecondaryIndexes, Wrappers_Compile.Option<BillingMode> BillingMode, Wrappers_Compile.Option<ProvisionedThroughput> ProvisionedThroughput, Wrappers_Compile.Option<StreamSpecification> StreamSpecification, Wrappers_Compile.Option<SSESpecification> SSESpecification, Wrappers_Compile.Option<dafny.DafnySequence<? extends Tag>> Tags, Wrappers_Compile.Option<TableClass> TableClass, Wrappers_Compile.Option<Boolean> DeletionProtectionEnabled, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ResourcePolicy, Wrappers_Compile.Option<OnDemandThroughput> OnDemandThroughput) {
    return new CreateTableInput(AttributeDefinitions, TableName, KeySchema, LocalSecondaryIndexes, GlobalSecondaryIndexes, BillingMode, ProvisionedThroughput, StreamSpecification, SSESpecification, Tags, TableClass, DeletionProtectionEnabled, ResourcePolicy, OnDemandThroughput);
  }
  public static CreateTableInput create_CreateTableInput(dafny.DafnySequence<? extends AttributeDefinition> AttributeDefinitions, dafny.DafnySequence<? extends Character> TableName, dafny.DafnySequence<? extends KeySchemaElement> KeySchema, Wrappers_Compile.Option<dafny.DafnySequence<? extends LocalSecondaryIndex>> LocalSecondaryIndexes, Wrappers_Compile.Option<dafny.DafnySequence<? extends GlobalSecondaryIndex>> GlobalSecondaryIndexes, Wrappers_Compile.Option<BillingMode> BillingMode, Wrappers_Compile.Option<ProvisionedThroughput> ProvisionedThroughput, Wrappers_Compile.Option<StreamSpecification> StreamSpecification, Wrappers_Compile.Option<SSESpecification> SSESpecification, Wrappers_Compile.Option<dafny.DafnySequence<? extends Tag>> Tags, Wrappers_Compile.Option<TableClass> TableClass, Wrappers_Compile.Option<Boolean> DeletionProtectionEnabled, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ResourcePolicy, Wrappers_Compile.Option<OnDemandThroughput> OnDemandThroughput) {
    return create(AttributeDefinitions, TableName, KeySchema, LocalSecondaryIndexes, GlobalSecondaryIndexes, BillingMode, ProvisionedThroughput, StreamSpecification, SSESpecification, Tags, TableClass, DeletionProtectionEnabled, ResourcePolicy, OnDemandThroughput);
  }
  public boolean is_CreateTableInput() { return true; }
  public dafny.DafnySequence<? extends AttributeDefinition> dtor_AttributeDefinitions() {
    return this._AttributeDefinitions;
  }
  public dafny.DafnySequence<? extends Character> dtor_TableName() {
    return this._TableName;
  }
  public dafny.DafnySequence<? extends KeySchemaElement> dtor_KeySchema() {
    return this._KeySchema;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends LocalSecondaryIndex>> dtor_LocalSecondaryIndexes() {
    return this._LocalSecondaryIndexes;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends GlobalSecondaryIndex>> dtor_GlobalSecondaryIndexes() {
    return this._GlobalSecondaryIndexes;
  }
  public Wrappers_Compile.Option<BillingMode> dtor_BillingMode() {
    return this._BillingMode;
  }
  public Wrappers_Compile.Option<ProvisionedThroughput> dtor_ProvisionedThroughput() {
    return this._ProvisionedThroughput;
  }
  public Wrappers_Compile.Option<StreamSpecification> dtor_StreamSpecification() {
    return this._StreamSpecification;
  }
  public Wrappers_Compile.Option<SSESpecification> dtor_SSESpecification() {
    return this._SSESpecification;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Tag>> dtor_Tags() {
    return this._Tags;
  }
  public Wrappers_Compile.Option<TableClass> dtor_TableClass() {
    return this._TableClass;
  }
  public Wrappers_Compile.Option<Boolean> dtor_DeletionProtectionEnabled() {
    return this._DeletionProtectionEnabled;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_ResourcePolicy() {
    return this._ResourcePolicy;
  }
  public Wrappers_Compile.Option<OnDemandThroughput> dtor_OnDemandThroughput() {
    return this._OnDemandThroughput;
  }
}
