// Class LocalSecondaryIndexDescription
// Dafny class LocalSecondaryIndexDescription compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class LocalSecondaryIndexDescription {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _IndexName;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends KeySchemaElement>> _KeySchema;
  public Wrappers_Compile.Option<Projection> _Projection;
  public Wrappers_Compile.Option<java.lang.Long> _IndexSizeBytes;
  public Wrappers_Compile.Option<java.lang.Long> _ItemCount;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _IndexArn;
  public LocalSecondaryIndexDescription (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> IndexName, Wrappers_Compile.Option<dafny.DafnySequence<? extends KeySchemaElement>> KeySchema, Wrappers_Compile.Option<Projection> Projection, Wrappers_Compile.Option<java.lang.Long> IndexSizeBytes, Wrappers_Compile.Option<java.lang.Long> ItemCount, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> IndexArn) {
    this._IndexName = IndexName;
    this._KeySchema = KeySchema;
    this._Projection = Projection;
    this._IndexSizeBytes = IndexSizeBytes;
    this._ItemCount = ItemCount;
    this._IndexArn = IndexArn;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    LocalSecondaryIndexDescription o = (LocalSecondaryIndexDescription)other;
    return true && java.util.Objects.equals(this._IndexName, o._IndexName) && java.util.Objects.equals(this._KeySchema, o._KeySchema) && java.util.Objects.equals(this._Projection, o._Projection) && java.util.Objects.equals(this._IndexSizeBytes, o._IndexSizeBytes) && java.util.Objects.equals(this._ItemCount, o._ItemCount) && java.util.Objects.equals(this._IndexArn, o._IndexArn);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._IndexName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeySchema);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Projection);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._IndexSizeBytes);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ItemCount);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._IndexArn);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.LocalSecondaryIndexDescription.LocalSecondaryIndexDescription");
    s.append("(");
    s.append(dafny.Helpers.toString(this._IndexName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._KeySchema));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Projection));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._IndexSizeBytes));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ItemCount));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._IndexArn));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<LocalSecondaryIndexDescription> _TYPE = dafny.TypeDescriptor.<LocalSecondaryIndexDescription>referenceWithInitializer(LocalSecondaryIndexDescription.class, () -> LocalSecondaryIndexDescription.Default());
  public static dafny.TypeDescriptor<LocalSecondaryIndexDescription> _typeDescriptor() {
    return (dafny.TypeDescriptor<LocalSecondaryIndexDescription>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final LocalSecondaryIndexDescription theDefault = LocalSecondaryIndexDescription.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(IndexName._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends KeySchemaElement>>Default(KeySchema._typeDescriptor()), Wrappers_Compile.Option.<Projection>Default(Projection._typeDescriptor()), Wrappers_Compile.Option.<java.lang.Long>Default(BoundedInts_Compile.int64._typeDescriptor()), Wrappers_Compile.Option.<java.lang.Long>Default(BoundedInts_Compile.int64._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)));
  public static LocalSecondaryIndexDescription Default() {
    return theDefault;
  }
  public static LocalSecondaryIndexDescription create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> IndexName, Wrappers_Compile.Option<dafny.DafnySequence<? extends KeySchemaElement>> KeySchema, Wrappers_Compile.Option<Projection> Projection, Wrappers_Compile.Option<java.lang.Long> IndexSizeBytes, Wrappers_Compile.Option<java.lang.Long> ItemCount, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> IndexArn) {
    return new LocalSecondaryIndexDescription(IndexName, KeySchema, Projection, IndexSizeBytes, ItemCount, IndexArn);
  }
  public static LocalSecondaryIndexDescription create_LocalSecondaryIndexDescription(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> IndexName, Wrappers_Compile.Option<dafny.DafnySequence<? extends KeySchemaElement>> KeySchema, Wrappers_Compile.Option<Projection> Projection, Wrappers_Compile.Option<java.lang.Long> IndexSizeBytes, Wrappers_Compile.Option<java.lang.Long> ItemCount, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> IndexArn) {
    return create(IndexName, KeySchema, Projection, IndexSizeBytes, ItemCount, IndexArn);
  }
  public boolean is_LocalSecondaryIndexDescription() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_IndexName() {
    return this._IndexName;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends KeySchemaElement>> dtor_KeySchema() {
    return this._KeySchema;
  }
  public Wrappers_Compile.Option<Projection> dtor_Projection() {
    return this._Projection;
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
}
