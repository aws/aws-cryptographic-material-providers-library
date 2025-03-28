// Class GlobalSecondaryIndexDescription
// Dafny class GlobalSecondaryIndexDescription compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class GlobalSecondaryIndexDescription {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _IndexName;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends KeySchemaElement>> _KeySchema;
  public Wrappers_Compile.Option<Projection> _Projection;
  public Wrappers_Compile.Option<IndexStatus> _IndexStatus;
  public Wrappers_Compile.Option<Boolean> _Backfilling;
  public Wrappers_Compile.Option<ProvisionedThroughputDescription> _ProvisionedThroughput;
  public Wrappers_Compile.Option<java.lang.Long> _IndexSizeBytes;
  public Wrappers_Compile.Option<java.lang.Long> _ItemCount;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _IndexArn;
  public Wrappers_Compile.Option<OnDemandThroughput> _OnDemandThroughput;
  public GlobalSecondaryIndexDescription (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> IndexName, Wrappers_Compile.Option<dafny.DafnySequence<? extends KeySchemaElement>> KeySchema, Wrappers_Compile.Option<Projection> Projection, Wrappers_Compile.Option<IndexStatus> IndexStatus, Wrappers_Compile.Option<Boolean> Backfilling, Wrappers_Compile.Option<ProvisionedThroughputDescription> ProvisionedThroughput, Wrappers_Compile.Option<java.lang.Long> IndexSizeBytes, Wrappers_Compile.Option<java.lang.Long> ItemCount, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> IndexArn, Wrappers_Compile.Option<OnDemandThroughput> OnDemandThroughput) {
    this._IndexName = IndexName;
    this._KeySchema = KeySchema;
    this._Projection = Projection;
    this._IndexStatus = IndexStatus;
    this._Backfilling = Backfilling;
    this._ProvisionedThroughput = ProvisionedThroughput;
    this._IndexSizeBytes = IndexSizeBytes;
    this._ItemCount = ItemCount;
    this._IndexArn = IndexArn;
    this._OnDemandThroughput = OnDemandThroughput;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GlobalSecondaryIndexDescription o = (GlobalSecondaryIndexDescription)other;
    return true && java.util.Objects.equals(this._IndexName, o._IndexName) && java.util.Objects.equals(this._KeySchema, o._KeySchema) && java.util.Objects.equals(this._Projection, o._Projection) && java.util.Objects.equals(this._IndexStatus, o._IndexStatus) && java.util.Objects.equals(this._Backfilling, o._Backfilling) && java.util.Objects.equals(this._ProvisionedThroughput, o._ProvisionedThroughput) && java.util.Objects.equals(this._IndexSizeBytes, o._IndexSizeBytes) && java.util.Objects.equals(this._ItemCount, o._ItemCount) && java.util.Objects.equals(this._IndexArn, o._IndexArn) && java.util.Objects.equals(this._OnDemandThroughput, o._OnDemandThroughput);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._IndexName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeySchema);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Projection);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._IndexStatus);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Backfilling);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ProvisionedThroughput);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._IndexSizeBytes);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ItemCount);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._IndexArn);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._OnDemandThroughput);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.GlobalSecondaryIndexDescription.GlobalSecondaryIndexDescription");
    s.append("(");
    s.append(dafny.Helpers.toString(this._IndexName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._KeySchema));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Projection));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._IndexStatus));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Backfilling));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ProvisionedThroughput));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._IndexSizeBytes));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ItemCount));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._IndexArn));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._OnDemandThroughput));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<GlobalSecondaryIndexDescription> _TYPE = dafny.TypeDescriptor.<GlobalSecondaryIndexDescription>referenceWithInitializer(GlobalSecondaryIndexDescription.class, () -> GlobalSecondaryIndexDescription.Default());
  public static dafny.TypeDescriptor<GlobalSecondaryIndexDescription> _typeDescriptor() {
    return (dafny.TypeDescriptor<GlobalSecondaryIndexDescription>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GlobalSecondaryIndexDescription theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.GlobalSecondaryIndexDescription.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(IndexName._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends KeySchemaElement>>Default(KeySchema._typeDescriptor()), Wrappers_Compile.Option.<Projection>Default(Projection._typeDescriptor()), Wrappers_Compile.Option.<IndexStatus>Default(IndexStatus._typeDescriptor()), Wrappers_Compile.Option.<Boolean>Default(dafny.TypeDescriptor.BOOLEAN), Wrappers_Compile.Option.<ProvisionedThroughputDescription>Default(ProvisionedThroughputDescription._typeDescriptor()), Wrappers_Compile.Option.<java.lang.Long>Default(BoundedInts_Compile.int64._typeDescriptor()), Wrappers_Compile.Option.<java.lang.Long>Default(BoundedInts_Compile.int64._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<OnDemandThroughput>Default(OnDemandThroughput._typeDescriptor()));
  public static GlobalSecondaryIndexDescription Default() {
    return theDefault;
  }
  public static GlobalSecondaryIndexDescription create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> IndexName, Wrappers_Compile.Option<dafny.DafnySequence<? extends KeySchemaElement>> KeySchema, Wrappers_Compile.Option<Projection> Projection, Wrappers_Compile.Option<IndexStatus> IndexStatus, Wrappers_Compile.Option<Boolean> Backfilling, Wrappers_Compile.Option<ProvisionedThroughputDescription> ProvisionedThroughput, Wrappers_Compile.Option<java.lang.Long> IndexSizeBytes, Wrappers_Compile.Option<java.lang.Long> ItemCount, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> IndexArn, Wrappers_Compile.Option<OnDemandThroughput> OnDemandThroughput) {
    return new GlobalSecondaryIndexDescription(IndexName, KeySchema, Projection, IndexStatus, Backfilling, ProvisionedThroughput, IndexSizeBytes, ItemCount, IndexArn, OnDemandThroughput);
  }
  public static GlobalSecondaryIndexDescription create_GlobalSecondaryIndexDescription(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> IndexName, Wrappers_Compile.Option<dafny.DafnySequence<? extends KeySchemaElement>> KeySchema, Wrappers_Compile.Option<Projection> Projection, Wrappers_Compile.Option<IndexStatus> IndexStatus, Wrappers_Compile.Option<Boolean> Backfilling, Wrappers_Compile.Option<ProvisionedThroughputDescription> ProvisionedThroughput, Wrappers_Compile.Option<java.lang.Long> IndexSizeBytes, Wrappers_Compile.Option<java.lang.Long> ItemCount, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> IndexArn, Wrappers_Compile.Option<OnDemandThroughput> OnDemandThroughput) {
    return create(IndexName, KeySchema, Projection, IndexStatus, Backfilling, ProvisionedThroughput, IndexSizeBytes, ItemCount, IndexArn, OnDemandThroughput);
  }
  public boolean is_GlobalSecondaryIndexDescription() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_IndexName() {
    return this._IndexName;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends KeySchemaElement>> dtor_KeySchema() {
    return this._KeySchema;
  }
  public Wrappers_Compile.Option<Projection> dtor_Projection() {
    return this._Projection;
  }
  public Wrappers_Compile.Option<IndexStatus> dtor_IndexStatus() {
    return this._IndexStatus;
  }
  public Wrappers_Compile.Option<Boolean> dtor_Backfilling() {
    return this._Backfilling;
  }
  public Wrappers_Compile.Option<ProvisionedThroughputDescription> dtor_ProvisionedThroughput() {
    return this._ProvisionedThroughput;
  }
  public Wrappers_Compile.Option<java.lang.Long> dtor_IndexSizeBytes() {
    return this._IndexSizeBytes;
  }
  public Wrappers_Compile.Option<java.lang.Long> dtor_ItemCount() {
    return this._ItemCount;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_IndexArn() {
    return this._IndexArn;
  }
  public Wrappers_Compile.Option<OnDemandThroughput> dtor_OnDemandThroughput() {
    return this._OnDemandThroughput;
  }
}
