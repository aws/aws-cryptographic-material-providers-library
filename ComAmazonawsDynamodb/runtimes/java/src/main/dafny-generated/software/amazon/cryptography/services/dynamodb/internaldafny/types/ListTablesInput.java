// Class ListTablesInput
// Dafny class ListTablesInput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ListTablesInput {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _ExclusiveStartTableName;
  public Wrappers_Compile.Option<java.lang.Integer> _Limit;
  public ListTablesInput (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ExclusiveStartTableName, Wrappers_Compile.Option<java.lang.Integer> Limit) {
    this._ExclusiveStartTableName = ExclusiveStartTableName;
    this._Limit = Limit;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ListTablesInput o = (ListTablesInput)other;
    return true && java.util.Objects.equals(this._ExclusiveStartTableName, o._ExclusiveStartTableName) && java.util.Objects.equals(this._Limit, o._Limit);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ExclusiveStartTableName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Limit);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ListTablesInput.ListTablesInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._ExclusiveStartTableName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Limit));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ListTablesInput> _TYPE = dafny.TypeDescriptor.<ListTablesInput>referenceWithInitializer(ListTablesInput.class, () -> ListTablesInput.Default());
  public static dafny.TypeDescriptor<ListTablesInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<ListTablesInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ListTablesInput theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.ListTablesInput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(TableName._typeDescriptor()), Wrappers_Compile.Option.<java.lang.Integer>Default(ListTablesInputLimit._typeDescriptor()));
  public static ListTablesInput Default() {
    return theDefault;
  }
  public static ListTablesInput create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ExclusiveStartTableName, Wrappers_Compile.Option<java.lang.Integer> Limit) {
    return new ListTablesInput(ExclusiveStartTableName, Limit);
  }
  public static ListTablesInput create_ListTablesInput(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ExclusiveStartTableName, Wrappers_Compile.Option<java.lang.Integer> Limit) {
    return create(ExclusiveStartTableName, Limit);
  }
  public boolean is_ListTablesInput() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_ExclusiveStartTableName() {
    return this._ExclusiveStartTableName;
  }
  public Wrappers_Compile.Option<java.lang.Integer> dtor_Limit() {
    return this._Limit;
  }
}
