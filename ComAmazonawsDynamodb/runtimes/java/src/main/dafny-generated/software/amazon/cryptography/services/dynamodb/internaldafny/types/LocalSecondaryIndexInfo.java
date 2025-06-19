// Class LocalSecondaryIndexInfo
// Dafny class LocalSecondaryIndexInfo compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class LocalSecondaryIndexInfo {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _IndexName;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends KeySchemaElement>> _KeySchema;
  public Wrappers_Compile.Option<Projection> _Projection;
  public LocalSecondaryIndexInfo (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> IndexName, Wrappers_Compile.Option<dafny.DafnySequence<? extends KeySchemaElement>> KeySchema, Wrappers_Compile.Option<Projection> Projection) {
    this._IndexName = IndexName;
    this._KeySchema = KeySchema;
    this._Projection = Projection;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    LocalSecondaryIndexInfo o = (LocalSecondaryIndexInfo)other;
    return true && java.util.Objects.equals(this._IndexName, o._IndexName) && java.util.Objects.equals(this._KeySchema, o._KeySchema) && java.util.Objects.equals(this._Projection, o._Projection);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._IndexName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeySchema);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Projection);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.LocalSecondaryIndexInfo.LocalSecondaryIndexInfo");
    s.append("(");
    s.append(dafny.Helpers.toString(this._IndexName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._KeySchema));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Projection));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<LocalSecondaryIndexInfo> _TYPE = dafny.TypeDescriptor.<LocalSecondaryIndexInfo>referenceWithInitializer(LocalSecondaryIndexInfo.class, () -> LocalSecondaryIndexInfo.Default());
  public static dafny.TypeDescriptor<LocalSecondaryIndexInfo> _typeDescriptor() {
    return (dafny.TypeDescriptor<LocalSecondaryIndexInfo>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final LocalSecondaryIndexInfo theDefault = LocalSecondaryIndexInfo.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(IndexName._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends KeySchemaElement>>Default(KeySchema._typeDescriptor()), Wrappers_Compile.Option.<Projection>Default(Projection._typeDescriptor()));
  public static LocalSecondaryIndexInfo Default() {
    return theDefault;
  }
  public static LocalSecondaryIndexInfo create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> IndexName, Wrappers_Compile.Option<dafny.DafnySequence<? extends KeySchemaElement>> KeySchema, Wrappers_Compile.Option<Projection> Projection) {
    return new LocalSecondaryIndexInfo(IndexName, KeySchema, Projection);
  }
  public static LocalSecondaryIndexInfo create_LocalSecondaryIndexInfo(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> IndexName, Wrappers_Compile.Option<dafny.DafnySequence<? extends KeySchemaElement>> KeySchema, Wrappers_Compile.Option<Projection> Projection) {
    return create(IndexName, KeySchema, Projection);
  }
  public boolean is_LocalSecondaryIndexInfo() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_IndexName() {
    return this._IndexName;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends KeySchemaElement>> dtor_KeySchema() {
    return this._KeySchema;
  }
  public Wrappers_Compile.Option<Projection> dtor_Projection() {
    return this._Projection;
  }
}
