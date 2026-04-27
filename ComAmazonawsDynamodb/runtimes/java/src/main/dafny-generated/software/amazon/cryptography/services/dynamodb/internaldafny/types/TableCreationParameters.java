// Class TableCreationParameters
// Dafny class TableCreationParameters compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class TableCreationParameters {
  public dafny.DafnySequence<? extends Character> _TableName;
  public dafny.DafnySequence<? extends AttributeDefinition> _AttributeDefinitions;
  public dafny.DafnySequence<? extends KeySchemaElement> _KeySchema;
  public Wrappers_Compile.Option<BillingMode> _BillingMode;
  public Wrappers_Compile.Option<ProvisionedThroughput> _ProvisionedThroughput;
  public Wrappers_Compile.Option<OnDemandThroughput> _OnDemandThroughput;
  public Wrappers_Compile.Option<SSESpecification> _SSESpecification;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends GlobalSecondaryIndex>> _GlobalSecondaryIndexes;
  public TableCreationParameters (dafny.DafnySequence<? extends Character> TableName, dafny.DafnySequence<? extends AttributeDefinition> AttributeDefinitions, dafny.DafnySequence<? extends KeySchemaElement> KeySchema, Wrappers_Compile.Option<BillingMode> BillingMode, Wrappers_Compile.Option<ProvisionedThroughput> ProvisionedThroughput, Wrappers_Compile.Option<OnDemandThroughput> OnDemandThroughput, Wrappers_Compile.Option<SSESpecification> SSESpecification, Wrappers_Compile.Option<dafny.DafnySequence<? extends GlobalSecondaryIndex>> GlobalSecondaryIndexes) {
    this._TableName = TableName;
    this._AttributeDefinitions = AttributeDefinitions;
    this._KeySchema = KeySchema;
    this._BillingMode = BillingMode;
    this._ProvisionedThroughput = ProvisionedThroughput;
    this._OnDemandThroughput = OnDemandThroughput;
    this._SSESpecification = SSESpecification;
    this._GlobalSecondaryIndexes = GlobalSecondaryIndexes;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    TableCreationParameters o = (TableCreationParameters)other;
    return true && java.util.Objects.equals(this._TableName, o._TableName) && java.util.Objects.equals(this._AttributeDefinitions, o._AttributeDefinitions) && java.util.Objects.equals(this._KeySchema, o._KeySchema) && java.util.Objects.equals(this._BillingMode, o._BillingMode) && java.util.Objects.equals(this._ProvisionedThroughput, o._ProvisionedThroughput) && java.util.Objects.equals(this._OnDemandThroughput, o._OnDemandThroughput) && java.util.Objects.equals(this._SSESpecification, o._SSESpecification) && java.util.Objects.equals(this._GlobalSecondaryIndexes, o._GlobalSecondaryIndexes);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._AttributeDefinitions);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeySchema);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._BillingMode);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ProvisionedThroughput);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._OnDemandThroughput);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._SSESpecification);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._GlobalSecondaryIndexes);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.TableCreationParameters.TableCreationParameters");
    s.append("(");
    s.append(dafny.Helpers.toString(this._TableName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._AttributeDefinitions));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._KeySchema));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._BillingMode));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ProvisionedThroughput));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._OnDemandThroughput));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._SSESpecification));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._GlobalSecondaryIndexes));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<TableCreationParameters> _TYPE = dafny.TypeDescriptor.<TableCreationParameters>referenceWithInitializer(TableCreationParameters.class, () -> TableCreationParameters.Default());
  public static dafny.TypeDescriptor<TableCreationParameters> _typeDescriptor() {
    return (dafny.TypeDescriptor<TableCreationParameters>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final TableCreationParameters theDefault = TableCreationParameters.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<AttributeDefinition> empty(AttributeDefinition._typeDescriptor()), dafny.DafnySequence.<KeySchemaElement> empty(KeySchemaElement._typeDescriptor()), Wrappers_Compile.Option.<BillingMode>Default(BillingMode._typeDescriptor()), Wrappers_Compile.Option.<ProvisionedThroughput>Default(ProvisionedThroughput._typeDescriptor()), Wrappers_Compile.Option.<OnDemandThroughput>Default(OnDemandThroughput._typeDescriptor()), Wrappers_Compile.Option.<SSESpecification>Default(SSESpecification._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends GlobalSecondaryIndex>>Default(dafny.DafnySequence.<GlobalSecondaryIndex>_typeDescriptor(GlobalSecondaryIndex._typeDescriptor())));
  public static TableCreationParameters Default() {
    return theDefault;
  }
  public static TableCreationParameters create(dafny.DafnySequence<? extends Character> TableName, dafny.DafnySequence<? extends AttributeDefinition> AttributeDefinitions, dafny.DafnySequence<? extends KeySchemaElement> KeySchema, Wrappers_Compile.Option<BillingMode> BillingMode, Wrappers_Compile.Option<ProvisionedThroughput> ProvisionedThroughput, Wrappers_Compile.Option<OnDemandThroughput> OnDemandThroughput, Wrappers_Compile.Option<SSESpecification> SSESpecification, Wrappers_Compile.Option<dafny.DafnySequence<? extends GlobalSecondaryIndex>> GlobalSecondaryIndexes) {
    return new TableCreationParameters(TableName, AttributeDefinitions, KeySchema, BillingMode, ProvisionedThroughput, OnDemandThroughput, SSESpecification, GlobalSecondaryIndexes);
  }
  public static TableCreationParameters create_TableCreationParameters(dafny.DafnySequence<? extends Character> TableName, dafny.DafnySequence<? extends AttributeDefinition> AttributeDefinitions, dafny.DafnySequence<? extends KeySchemaElement> KeySchema, Wrappers_Compile.Option<BillingMode> BillingMode, Wrappers_Compile.Option<ProvisionedThroughput> ProvisionedThroughput, Wrappers_Compile.Option<OnDemandThroughput> OnDemandThroughput, Wrappers_Compile.Option<SSESpecification> SSESpecification, Wrappers_Compile.Option<dafny.DafnySequence<? extends GlobalSecondaryIndex>> GlobalSecondaryIndexes) {
    return create(TableName, AttributeDefinitions, KeySchema, BillingMode, ProvisionedThroughput, OnDemandThroughput, SSESpecification, GlobalSecondaryIndexes);
  }
  public boolean is_TableCreationParameters() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_TableName() {
    return this._TableName;
  }
  public dafny.DafnySequence<? extends AttributeDefinition> dtor_AttributeDefinitions() {
    return this._AttributeDefinitions;
  }
  public dafny.DafnySequence<? extends KeySchemaElement> dtor_KeySchema() {
    return this._KeySchema;
  }
  public Wrappers_Compile.Option<BillingMode> dtor_BillingMode() {
    return this._BillingMode;
  }
  public Wrappers_Compile.Option<ProvisionedThroughput> dtor_ProvisionedThroughput() {
    return this._ProvisionedThroughput;
  }
  public Wrappers_Compile.Option<OnDemandThroughput> dtor_OnDemandThroughput() {
    return this._OnDemandThroughput;
  }
  public Wrappers_Compile.Option<SSESpecification> dtor_SSESpecification() {
    return this._SSESpecification;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends GlobalSecondaryIndex>> dtor_GlobalSecondaryIndexes() {
    return this._GlobalSecondaryIndexes;
  }
}
