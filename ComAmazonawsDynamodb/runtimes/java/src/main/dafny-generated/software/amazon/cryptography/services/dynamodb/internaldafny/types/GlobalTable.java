// Class GlobalTable
// Dafny class GlobalTable compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class GlobalTable {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _GlobalTableName;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Replica>> _ReplicationGroup;
  public GlobalTable (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> GlobalTableName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Replica>> ReplicationGroup) {
    this._GlobalTableName = GlobalTableName;
    this._ReplicationGroup = ReplicationGroup;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GlobalTable o = (GlobalTable)other;
    return true && java.util.Objects.equals(this._GlobalTableName, o._GlobalTableName) && java.util.Objects.equals(this._ReplicationGroup, o._ReplicationGroup);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._GlobalTableName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReplicationGroup);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.GlobalTable.GlobalTable");
    s.append("(");
    s.append(dafny.Helpers.toString(this._GlobalTableName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ReplicationGroup));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<GlobalTable> _TYPE = dafny.TypeDescriptor.<GlobalTable>referenceWithInitializer(GlobalTable.class, () -> GlobalTable.Default());
  public static dafny.TypeDescriptor<GlobalTable> _typeDescriptor() {
    return (dafny.TypeDescriptor<GlobalTable>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GlobalTable theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.GlobalTable.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(TableName._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Replica>>Default(dafny.DafnySequence.<Replica>_typeDescriptor(Replica._typeDescriptor())));
  public static GlobalTable Default() {
    return theDefault;
  }
  public static GlobalTable create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> GlobalTableName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Replica>> ReplicationGroup) {
    return new GlobalTable(GlobalTableName, ReplicationGroup);
  }
  public static GlobalTable create_GlobalTable(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> GlobalTableName, Wrappers_Compile.Option<dafny.DafnySequence<? extends Replica>> ReplicationGroup) {
    return create(GlobalTableName, ReplicationGroup);
  }
  public boolean is_GlobalTable() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_GlobalTableName() {
    return this._GlobalTableName;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Replica>> dtor_ReplicationGroup() {
    return this._ReplicationGroup;
  }
}
