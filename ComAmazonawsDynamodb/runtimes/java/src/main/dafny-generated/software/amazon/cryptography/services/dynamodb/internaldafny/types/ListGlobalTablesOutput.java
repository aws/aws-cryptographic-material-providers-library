// Class ListGlobalTablesOutput
// Dafny class ListGlobalTablesOutput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ListGlobalTablesOutput {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends GlobalTable>> _GlobalTables;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _LastEvaluatedGlobalTableName;
  public ListGlobalTablesOutput (Wrappers_Compile.Option<dafny.DafnySequence<? extends GlobalTable>> GlobalTables, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> LastEvaluatedGlobalTableName) {
    this._GlobalTables = GlobalTables;
    this._LastEvaluatedGlobalTableName = LastEvaluatedGlobalTableName;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ListGlobalTablesOutput o = (ListGlobalTablesOutput)other;
    return true && java.util.Objects.equals(this._GlobalTables, o._GlobalTables) && java.util.Objects.equals(this._LastEvaluatedGlobalTableName, o._LastEvaluatedGlobalTableName);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._GlobalTables);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._LastEvaluatedGlobalTableName);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ListGlobalTablesOutput.ListGlobalTablesOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._GlobalTables));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._LastEvaluatedGlobalTableName));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ListGlobalTablesOutput> _TYPE = dafny.TypeDescriptor.<ListGlobalTablesOutput>referenceWithInitializer(ListGlobalTablesOutput.class, () -> ListGlobalTablesOutput.Default());
  public static dafny.TypeDescriptor<ListGlobalTablesOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<ListGlobalTablesOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ListGlobalTablesOutput theDefault = ListGlobalTablesOutput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends GlobalTable>>Default(dafny.DafnySequence.<GlobalTable>_typeDescriptor(GlobalTable._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(TableName._typeDescriptor()));
  public static ListGlobalTablesOutput Default() {
    return theDefault;
  }
  public static ListGlobalTablesOutput create(Wrappers_Compile.Option<dafny.DafnySequence<? extends GlobalTable>> GlobalTables, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> LastEvaluatedGlobalTableName) {
    return new ListGlobalTablesOutput(GlobalTables, LastEvaluatedGlobalTableName);
  }
  public static ListGlobalTablesOutput create_ListGlobalTablesOutput(Wrappers_Compile.Option<dafny.DafnySequence<? extends GlobalTable>> GlobalTables, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> LastEvaluatedGlobalTableName) {
    return create(GlobalTables, LastEvaluatedGlobalTableName);
  }
  public boolean is_ListGlobalTablesOutput() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends GlobalTable>> dtor_GlobalTables() {
    return this._GlobalTables;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_LastEvaluatedGlobalTableName() {
    return this._LastEvaluatedGlobalTableName;
  }
}
