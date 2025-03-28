// Class SourceTableDetails
// Dafny class SourceTableDetails compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class SourceTableDetails {
  public dafny.DafnySequence<? extends Character> _TableName;
  public dafny.DafnySequence<? extends Character> _TableId;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _TableArn;
  public Wrappers_Compile.Option<java.lang.Long> _TableSizeBytes;
  public dafny.DafnySequence<? extends KeySchemaElement> _KeySchema;
  public dafny.DafnySequence<? extends Character> _TableCreationDateTime;
  public ProvisionedThroughput _ProvisionedThroughput;
  public Wrappers_Compile.Option<OnDemandThroughput> _OnDemandThroughput;
  public Wrappers_Compile.Option<java.lang.Long> _ItemCount;
  public Wrappers_Compile.Option<BillingMode> _BillingMode;
  public SourceTableDetails (dafny.DafnySequence<? extends Character> TableName, dafny.DafnySequence<? extends Character> TableId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableArn, Wrappers_Compile.Option<java.lang.Long> TableSizeBytes, dafny.DafnySequence<? extends KeySchemaElement> KeySchema, dafny.DafnySequence<? extends Character> TableCreationDateTime, ProvisionedThroughput ProvisionedThroughput, Wrappers_Compile.Option<OnDemandThroughput> OnDemandThroughput, Wrappers_Compile.Option<java.lang.Long> ItemCount, Wrappers_Compile.Option<BillingMode> BillingMode) {
    this._TableName = TableName;
    this._TableId = TableId;
    this._TableArn = TableArn;
    this._TableSizeBytes = TableSizeBytes;
    this._KeySchema = KeySchema;
    this._TableCreationDateTime = TableCreationDateTime;
    this._ProvisionedThroughput = ProvisionedThroughput;
    this._OnDemandThroughput = OnDemandThroughput;
    this._ItemCount = ItemCount;
    this._BillingMode = BillingMode;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    SourceTableDetails o = (SourceTableDetails)other;
    return true && java.util.Objects.equals(this._TableName, o._TableName) && java.util.Objects.equals(this._TableId, o._TableId) && java.util.Objects.equals(this._TableArn, o._TableArn) && java.util.Objects.equals(this._TableSizeBytes, o._TableSizeBytes) && java.util.Objects.equals(this._KeySchema, o._KeySchema) && java.util.Objects.equals(this._TableCreationDateTime, o._TableCreationDateTime) && java.util.Objects.equals(this._ProvisionedThroughput, o._ProvisionedThroughput) && java.util.Objects.equals(this._OnDemandThroughput, o._OnDemandThroughput) && java.util.Objects.equals(this._ItemCount, o._ItemCount) && java.util.Objects.equals(this._BillingMode, o._BillingMode);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableArn);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableSizeBytes);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeySchema);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableCreationDateTime);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ProvisionedThroughput);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._OnDemandThroughput);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ItemCount);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._BillingMode);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.SourceTableDetails.SourceTableDetails");
    s.append("(");
    s.append(dafny.Helpers.toString(this._TableName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._TableId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._TableArn));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._TableSizeBytes));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._KeySchema));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._TableCreationDateTime));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ProvisionedThroughput));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._OnDemandThroughput));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ItemCount));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._BillingMode));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<SourceTableDetails> _TYPE = dafny.TypeDescriptor.<SourceTableDetails>referenceWithInitializer(SourceTableDetails.class, () -> SourceTableDetails.Default());
  public static dafny.TypeDescriptor<SourceTableDetails> _typeDescriptor() {
    return (dafny.TypeDescriptor<SourceTableDetails>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final SourceTableDetails theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.SourceTableDetails.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(TableArn._typeDescriptor()), Wrappers_Compile.Option.<java.lang.Long>Default(BoundedInts_Compile.int64._typeDescriptor()), dafny.DafnySequence.<KeySchemaElement> empty(KeySchemaElement._typeDescriptor()), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), ProvisionedThroughput.Default(), Wrappers_Compile.Option.<OnDemandThroughput>Default(OnDemandThroughput._typeDescriptor()), Wrappers_Compile.Option.<java.lang.Long>Default(ItemCount._typeDescriptor()), Wrappers_Compile.Option.<BillingMode>Default(BillingMode._typeDescriptor()));
  public static SourceTableDetails Default() {
    return theDefault;
  }
  public static SourceTableDetails create(dafny.DafnySequence<? extends Character> TableName, dafny.DafnySequence<? extends Character> TableId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableArn, Wrappers_Compile.Option<java.lang.Long> TableSizeBytes, dafny.DafnySequence<? extends KeySchemaElement> KeySchema, dafny.DafnySequence<? extends Character> TableCreationDateTime, ProvisionedThroughput ProvisionedThroughput, Wrappers_Compile.Option<OnDemandThroughput> OnDemandThroughput, Wrappers_Compile.Option<java.lang.Long> ItemCount, Wrappers_Compile.Option<BillingMode> BillingMode) {
    return new SourceTableDetails(TableName, TableId, TableArn, TableSizeBytes, KeySchema, TableCreationDateTime, ProvisionedThroughput, OnDemandThroughput, ItemCount, BillingMode);
  }
  public static SourceTableDetails create_SourceTableDetails(dafny.DafnySequence<? extends Character> TableName, dafny.DafnySequence<? extends Character> TableId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableArn, Wrappers_Compile.Option<java.lang.Long> TableSizeBytes, dafny.DafnySequence<? extends KeySchemaElement> KeySchema, dafny.DafnySequence<? extends Character> TableCreationDateTime, ProvisionedThroughput ProvisionedThroughput, Wrappers_Compile.Option<OnDemandThroughput> OnDemandThroughput, Wrappers_Compile.Option<java.lang.Long> ItemCount, Wrappers_Compile.Option<BillingMode> BillingMode) {
    return create(TableName, TableId, TableArn, TableSizeBytes, KeySchema, TableCreationDateTime, ProvisionedThroughput, OnDemandThroughput, ItemCount, BillingMode);
  }
  public boolean is_SourceTableDetails() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_TableName() {
    return this._TableName;
  }
  public dafny.DafnySequence<? extends Character> dtor_TableId() {
    return this._TableId;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_TableArn() {
    return this._TableArn;
  }
  public Wrappers_Compile.Option<java.lang.Long> dtor_TableSizeBytes() {
    return this._TableSizeBytes;
  }
  public dafny.DafnySequence<? extends KeySchemaElement> dtor_KeySchema() {
    return this._KeySchema;
  }
  public dafny.DafnySequence<? extends Character> dtor_TableCreationDateTime() {
    return this._TableCreationDateTime;
  }
  public ProvisionedThroughput dtor_ProvisionedThroughput() {
    return this._ProvisionedThroughput;
  }
  public Wrappers_Compile.Option<OnDemandThroughput> dtor_OnDemandThroughput() {
    return this._OnDemandThroughput;
  }
  public Wrappers_Compile.Option<java.lang.Long> dtor_ItemCount() {
    return this._ItemCount;
  }
  public Wrappers_Compile.Option<BillingMode> dtor_BillingMode() {
    return this._BillingMode;
  }
}
