// Class ListTablesOutput
// Dafny class ListTablesOutput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ListTablesOutput {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> _TableNames;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _LastEvaluatedTableName;
  public ListTablesOutput (Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> TableNames, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> LastEvaluatedTableName) {
    this._TableNames = TableNames;
    this._LastEvaluatedTableName = LastEvaluatedTableName;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ListTablesOutput o = (ListTablesOutput)other;
    return true && java.util.Objects.equals(this._TableNames, o._TableNames) && java.util.Objects.equals(this._LastEvaluatedTableName, o._LastEvaluatedTableName);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableNames);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._LastEvaluatedTableName);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ListTablesOutput.ListTablesOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._TableNames));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._LastEvaluatedTableName));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ListTablesOutput> _TYPE = dafny.TypeDescriptor.<ListTablesOutput>referenceWithInitializer(ListTablesOutput.class, () -> ListTablesOutput.Default());
  public static dafny.TypeDescriptor<ListTablesOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<ListTablesOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ListTablesOutput theDefault = ListTablesOutput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>Default(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(TableName._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(TableName._typeDescriptor()));
  public static ListTablesOutput Default() {
    return theDefault;
  }
  public static ListTablesOutput create(Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> TableNames, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> LastEvaluatedTableName) {
    return new ListTablesOutput(TableNames, LastEvaluatedTableName);
  }
  public static ListTablesOutput create_ListTablesOutput(Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> TableNames, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> LastEvaluatedTableName) {
    return create(TableNames, LastEvaluatedTableName);
  }
  public boolean is_ListTablesOutput() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> dtor_TableNames() {
    return this._TableNames;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_LastEvaluatedTableName() {
    return this._LastEvaluatedTableName;
  }
}
