// Class GlobalSecondaryIndexInfo
// Dafny class GlobalSecondaryIndexInfo compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class GlobalSecondaryIndexInfo {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _IndexName;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends KeySchemaElement>> _KeySchema;
  public Wrappers_Compile.Option<Projection> _Projection;
  public Wrappers_Compile.Option<ProvisionedThroughput> _ProvisionedThroughput;
  public Wrappers_Compile.Option<OnDemandThroughput> _OnDemandThroughput;
  public GlobalSecondaryIndexInfo (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> IndexName, Wrappers_Compile.Option<dafny.DafnySequence<? extends KeySchemaElement>> KeySchema, Wrappers_Compile.Option<Projection> Projection, Wrappers_Compile.Option<ProvisionedThroughput> ProvisionedThroughput, Wrappers_Compile.Option<OnDemandThroughput> OnDemandThroughput) {
    this._IndexName = IndexName;
    this._KeySchema = KeySchema;
    this._Projection = Projection;
    this._ProvisionedThroughput = ProvisionedThroughput;
    this._OnDemandThroughput = OnDemandThroughput;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GlobalSecondaryIndexInfo o = (GlobalSecondaryIndexInfo)other;
    return true && java.util.Objects.equals(this._IndexName, o._IndexName) && java.util.Objects.equals(this._KeySchema, o._KeySchema) && java.util.Objects.equals(this._Projection, o._Projection) && java.util.Objects.equals(this._ProvisionedThroughput, o._ProvisionedThroughput) && java.util.Objects.equals(this._OnDemandThroughput, o._OnDemandThroughput);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._IndexName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeySchema);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Projection);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ProvisionedThroughput);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._OnDemandThroughput);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.GlobalSecondaryIndexInfo.GlobalSecondaryIndexInfo");
    s.append("(");
    s.append(dafny.Helpers.toString(this._IndexName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._KeySchema));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Projection));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ProvisionedThroughput));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._OnDemandThroughput));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<GlobalSecondaryIndexInfo> _TYPE = dafny.TypeDescriptor.<GlobalSecondaryIndexInfo>referenceWithInitializer(GlobalSecondaryIndexInfo.class, () -> GlobalSecondaryIndexInfo.Default());
  public static dafny.TypeDescriptor<GlobalSecondaryIndexInfo> _typeDescriptor() {
    return (dafny.TypeDescriptor<GlobalSecondaryIndexInfo>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GlobalSecondaryIndexInfo theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.GlobalSecondaryIndexInfo.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(IndexName._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends KeySchemaElement>>Default(KeySchema._typeDescriptor()), Wrappers_Compile.Option.<Projection>Default(Projection._typeDescriptor()), Wrappers_Compile.Option.<ProvisionedThroughput>Default(ProvisionedThroughput._typeDescriptor()), Wrappers_Compile.Option.<OnDemandThroughput>Default(OnDemandThroughput._typeDescriptor()));
  public static GlobalSecondaryIndexInfo Default() {
    return theDefault;
  }
  public static GlobalSecondaryIndexInfo create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> IndexName, Wrappers_Compile.Option<dafny.DafnySequence<? extends KeySchemaElement>> KeySchema, Wrappers_Compile.Option<Projection> Projection, Wrappers_Compile.Option<ProvisionedThroughput> ProvisionedThroughput, Wrappers_Compile.Option<OnDemandThroughput> OnDemandThroughput) {
    return new GlobalSecondaryIndexInfo(IndexName, KeySchema, Projection, ProvisionedThroughput, OnDemandThroughput);
  }
  public static GlobalSecondaryIndexInfo create_GlobalSecondaryIndexInfo(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> IndexName, Wrappers_Compile.Option<dafny.DafnySequence<? extends KeySchemaElement>> KeySchema, Wrappers_Compile.Option<Projection> Projection, Wrappers_Compile.Option<ProvisionedThroughput> ProvisionedThroughput, Wrappers_Compile.Option<OnDemandThroughput> OnDemandThroughput) {
    return create(IndexName, KeySchema, Projection, ProvisionedThroughput, OnDemandThroughput);
  }
  public boolean is_GlobalSecondaryIndexInfo() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_IndexName() {
    return this._IndexName;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends KeySchemaElement>> dtor_KeySchema() {
    return this._KeySchema;
  }
  public Wrappers_Compile.Option<Projection> dtor_Projection() {
    return this._Projection;
  }
  public Wrappers_Compile.Option<ProvisionedThroughput> dtor_ProvisionedThroughput() {
    return this._ProvisionedThroughput;
  }
  public Wrappers_Compile.Option<OnDemandThroughput> dtor_OnDemandThroughput() {
    return this._OnDemandThroughput;
  }
}
