// Class LocalSecondaryIndex
// Dafny class LocalSecondaryIndex compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class LocalSecondaryIndex {
  public dafny.DafnySequence<? extends Character> _IndexName;
  public dafny.DafnySequence<? extends KeySchemaElement> _KeySchema;
  public Projection _Projection;
  public LocalSecondaryIndex (dafny.DafnySequence<? extends Character> IndexName, dafny.DafnySequence<? extends KeySchemaElement> KeySchema, Projection Projection) {
    this._IndexName = IndexName;
    this._KeySchema = KeySchema;
    this._Projection = Projection;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    LocalSecondaryIndex o = (LocalSecondaryIndex)other;
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
    s.append("ComAmazonawsDynamodbTypes.LocalSecondaryIndex.LocalSecondaryIndex");
    s.append("(");
    s.append(dafny.Helpers.toString(this._IndexName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._KeySchema));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Projection));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<LocalSecondaryIndex> _TYPE = dafny.TypeDescriptor.<LocalSecondaryIndex>referenceWithInitializer(LocalSecondaryIndex.class, () -> LocalSecondaryIndex.Default());
  public static dafny.TypeDescriptor<LocalSecondaryIndex> _typeDescriptor() {
    return (dafny.TypeDescriptor<LocalSecondaryIndex>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final LocalSecondaryIndex theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.LocalSecondaryIndex.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<KeySchemaElement> empty(KeySchemaElement._typeDescriptor()), Projection.Default());
  public static LocalSecondaryIndex Default() {
    return theDefault;
  }
  public static LocalSecondaryIndex create(dafny.DafnySequence<? extends Character> IndexName, dafny.DafnySequence<? extends KeySchemaElement> KeySchema, Projection Projection) {
    return new LocalSecondaryIndex(IndexName, KeySchema, Projection);
  }
  public static LocalSecondaryIndex create_LocalSecondaryIndex(dafny.DafnySequence<? extends Character> IndexName, dafny.DafnySequence<? extends KeySchemaElement> KeySchema, Projection Projection) {
    return create(IndexName, KeySchema, Projection);
  }
  public boolean is_LocalSecondaryIndex() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_IndexName() {
    return this._IndexName;
  }
  public dafny.DafnySequence<? extends KeySchemaElement> dtor_KeySchema() {
    return this._KeySchema;
  }
  public Projection dtor_Projection() {
    return this._Projection;
  }
}
