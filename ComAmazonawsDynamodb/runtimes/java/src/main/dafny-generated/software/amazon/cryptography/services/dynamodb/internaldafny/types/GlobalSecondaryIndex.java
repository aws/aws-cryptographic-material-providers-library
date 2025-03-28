// Class GlobalSecondaryIndex
// Dafny class GlobalSecondaryIndex compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class GlobalSecondaryIndex {
  public dafny.DafnySequence<? extends Character> _IndexName;
  public dafny.DafnySequence<? extends KeySchemaElement> _KeySchema;
  public Projection _Projection;
  public Wrappers_Compile.Option<ProvisionedThroughput> _ProvisionedThroughput;
  public Wrappers_Compile.Option<OnDemandThroughput> _OnDemandThroughput;
  public GlobalSecondaryIndex (dafny.DafnySequence<? extends Character> IndexName, dafny.DafnySequence<? extends KeySchemaElement> KeySchema, Projection Projection, Wrappers_Compile.Option<ProvisionedThroughput> ProvisionedThroughput, Wrappers_Compile.Option<OnDemandThroughput> OnDemandThroughput) {
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
    GlobalSecondaryIndex o = (GlobalSecondaryIndex)other;
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
    s.append("ComAmazonawsDynamodbTypes.GlobalSecondaryIndex.GlobalSecondaryIndex");
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
  private static final dafny.TypeDescriptor<GlobalSecondaryIndex> _TYPE = dafny.TypeDescriptor.<GlobalSecondaryIndex>referenceWithInitializer(GlobalSecondaryIndex.class, () -> GlobalSecondaryIndex.Default());
  public static dafny.TypeDescriptor<GlobalSecondaryIndex> _typeDescriptor() {
    return (dafny.TypeDescriptor<GlobalSecondaryIndex>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GlobalSecondaryIndex theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.GlobalSecondaryIndex.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<KeySchemaElement> empty(KeySchemaElement._typeDescriptor()), Projection.Default(), Wrappers_Compile.Option.<ProvisionedThroughput>Default(ProvisionedThroughput._typeDescriptor()), Wrappers_Compile.Option.<OnDemandThroughput>Default(OnDemandThroughput._typeDescriptor()));
  public static GlobalSecondaryIndex Default() {
    return theDefault;
  }
  public static GlobalSecondaryIndex create(dafny.DafnySequence<? extends Character> IndexName, dafny.DafnySequence<? extends KeySchemaElement> KeySchema, Projection Projection, Wrappers_Compile.Option<ProvisionedThroughput> ProvisionedThroughput, Wrappers_Compile.Option<OnDemandThroughput> OnDemandThroughput) {
    return new GlobalSecondaryIndex(IndexName, KeySchema, Projection, ProvisionedThroughput, OnDemandThroughput);
  }
  public static GlobalSecondaryIndex create_GlobalSecondaryIndex(dafny.DafnySequence<? extends Character> IndexName, dafny.DafnySequence<? extends KeySchemaElement> KeySchema, Projection Projection, Wrappers_Compile.Option<ProvisionedThroughput> ProvisionedThroughput, Wrappers_Compile.Option<OnDemandThroughput> OnDemandThroughput) {
    return create(IndexName, KeySchema, Projection, ProvisionedThroughput, OnDemandThroughput);
  }
  public boolean is_GlobalSecondaryIndex() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_IndexName() {
    return this._IndexName;
  }
  public dafny.DafnySequence<? extends KeySchemaElement> dtor_KeySchema() {
    return this._KeySchema;
  }
  public Projection dtor_Projection() {
    return this._Projection;
  }
  public Wrappers_Compile.Option<ProvisionedThroughput> dtor_ProvisionedThroughput() {
    return this._ProvisionedThroughput;
  }
  public Wrappers_Compile.Option<OnDemandThroughput> dtor_OnDemandThroughput() {
    return this._OnDemandThroughput;
  }
}
