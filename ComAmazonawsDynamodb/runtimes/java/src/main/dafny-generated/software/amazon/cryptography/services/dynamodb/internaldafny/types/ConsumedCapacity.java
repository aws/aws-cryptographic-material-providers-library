// Class ConsumedCapacity
// Dafny class ConsumedCapacity compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ConsumedCapacity {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _TableName;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _CapacityUnits;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _ReadCapacityUnits;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _WriteCapacityUnits;
  public Wrappers_Compile.Option<Capacity> _Table;
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Capacity>> _LocalSecondaryIndexes;
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Capacity>> _GlobalSecondaryIndexes;
  public ConsumedCapacity (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableName, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> CapacityUnits, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> ReadCapacityUnits, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> WriteCapacityUnits, Wrappers_Compile.Option<Capacity> Table, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Capacity>> LocalSecondaryIndexes, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Capacity>> GlobalSecondaryIndexes) {
    this._TableName = TableName;
    this._CapacityUnits = CapacityUnits;
    this._ReadCapacityUnits = ReadCapacityUnits;
    this._WriteCapacityUnits = WriteCapacityUnits;
    this._Table = Table;
    this._LocalSecondaryIndexes = LocalSecondaryIndexes;
    this._GlobalSecondaryIndexes = GlobalSecondaryIndexes;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ConsumedCapacity o = (ConsumedCapacity)other;
    return true && java.util.Objects.equals(this._TableName, o._TableName) && java.util.Objects.equals(this._CapacityUnits, o._CapacityUnits) && java.util.Objects.equals(this._ReadCapacityUnits, o._ReadCapacityUnits) && java.util.Objects.equals(this._WriteCapacityUnits, o._WriteCapacityUnits) && java.util.Objects.equals(this._Table, o._Table) && java.util.Objects.equals(this._LocalSecondaryIndexes, o._LocalSecondaryIndexes) && java.util.Objects.equals(this._GlobalSecondaryIndexes, o._GlobalSecondaryIndexes);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._CapacityUnits);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReadCapacityUnits);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._WriteCapacityUnits);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Table);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._LocalSecondaryIndexes);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._GlobalSecondaryIndexes);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ConsumedCapacity.ConsumedCapacity");
    s.append("(");
    s.append(dafny.Helpers.toString(this._TableName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._CapacityUnits));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ReadCapacityUnits));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._WriteCapacityUnits));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Table));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._LocalSecondaryIndexes));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._GlobalSecondaryIndexes));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ConsumedCapacity> _TYPE = dafny.TypeDescriptor.<ConsumedCapacity>referenceWithInitializer(ConsumedCapacity.class, () -> ConsumedCapacity.Default());
  public static dafny.TypeDescriptor<ConsumedCapacity> _typeDescriptor() {
    return (dafny.TypeDescriptor<ConsumedCapacity>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ConsumedCapacity theDefault = ConsumedCapacity.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(TableArn._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(ConsumedCapacityUnits._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(ConsumedCapacityUnits._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(ConsumedCapacityUnits._typeDescriptor()), Wrappers_Compile.Option.<Capacity>Default(Capacity._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Capacity>>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, Capacity>_typeDescriptor(IndexName._typeDescriptor(), Capacity._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Capacity>>Default(dafny.DafnyMap.<dafny.DafnySequence<? extends Character>, Capacity>_typeDescriptor(IndexName._typeDescriptor(), Capacity._typeDescriptor())));
  public static ConsumedCapacity Default() {
    return theDefault;
  }
  public static ConsumedCapacity create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableName, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> CapacityUnits, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> ReadCapacityUnits, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> WriteCapacityUnits, Wrappers_Compile.Option<Capacity> Table, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Capacity>> LocalSecondaryIndexes, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Capacity>> GlobalSecondaryIndexes) {
    return new ConsumedCapacity(TableName, CapacityUnits, ReadCapacityUnits, WriteCapacityUnits, Table, LocalSecondaryIndexes, GlobalSecondaryIndexes);
  }
  public static ConsumedCapacity create_ConsumedCapacity(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableName, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> CapacityUnits, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> ReadCapacityUnits, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> WriteCapacityUnits, Wrappers_Compile.Option<Capacity> Table, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Capacity>> LocalSecondaryIndexes, Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Capacity>> GlobalSecondaryIndexes) {
    return create(TableName, CapacityUnits, ReadCapacityUnits, WriteCapacityUnits, Table, LocalSecondaryIndexes, GlobalSecondaryIndexes);
  }
  public boolean is_ConsumedCapacity() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_TableName() {
    return this._TableName;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> dtor_CapacityUnits() {
    return this._CapacityUnits;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> dtor_ReadCapacityUnits() {
    return this._ReadCapacityUnits;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> dtor_WriteCapacityUnits() {
    return this._WriteCapacityUnits;
  }
  public Wrappers_Compile.Option<Capacity> dtor_Table() {
    return this._Table;
  }
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Capacity>> dtor_LocalSecondaryIndexes() {
    return this._LocalSecondaryIndexes;
  }
  public Wrappers_Compile.Option<dafny.DafnyMap<? extends dafny.DafnySequence<? extends Character>, ? extends Capacity>> dtor_GlobalSecondaryIndexes() {
    return this._GlobalSecondaryIndexes;
  }
}
