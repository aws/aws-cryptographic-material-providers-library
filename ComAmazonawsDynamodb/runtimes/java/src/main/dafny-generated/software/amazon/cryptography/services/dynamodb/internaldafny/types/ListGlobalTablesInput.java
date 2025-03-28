// Class ListGlobalTablesInput
// Dafny class ListGlobalTablesInput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ListGlobalTablesInput {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _ExclusiveStartGlobalTableName;
  public Wrappers_Compile.Option<java.lang.Integer> _Limit;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _RegionName;
  public ListGlobalTablesInput (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ExclusiveStartGlobalTableName, Wrappers_Compile.Option<java.lang.Integer> Limit, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> RegionName) {
    this._ExclusiveStartGlobalTableName = ExclusiveStartGlobalTableName;
    this._Limit = Limit;
    this._RegionName = RegionName;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ListGlobalTablesInput o = (ListGlobalTablesInput)other;
    return true && java.util.Objects.equals(this._ExclusiveStartGlobalTableName, o._ExclusiveStartGlobalTableName) && java.util.Objects.equals(this._Limit, o._Limit) && java.util.Objects.equals(this._RegionName, o._RegionName);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ExclusiveStartGlobalTableName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Limit);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._RegionName);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ListGlobalTablesInput.ListGlobalTablesInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._ExclusiveStartGlobalTableName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Limit));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._RegionName));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ListGlobalTablesInput> _TYPE = dafny.TypeDescriptor.<ListGlobalTablesInput>referenceWithInitializer(ListGlobalTablesInput.class, () -> ListGlobalTablesInput.Default());
  public static dafny.TypeDescriptor<ListGlobalTablesInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<ListGlobalTablesInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ListGlobalTablesInput theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.ListGlobalTablesInput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(TableName._typeDescriptor()), Wrappers_Compile.Option.<java.lang.Integer>Default(PositiveIntegerObject._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)));
  public static ListGlobalTablesInput Default() {
    return theDefault;
  }
  public static ListGlobalTablesInput create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ExclusiveStartGlobalTableName, Wrappers_Compile.Option<java.lang.Integer> Limit, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> RegionName) {
    return new ListGlobalTablesInput(ExclusiveStartGlobalTableName, Limit, RegionName);
  }
  public static ListGlobalTablesInput create_ListGlobalTablesInput(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ExclusiveStartGlobalTableName, Wrappers_Compile.Option<java.lang.Integer> Limit, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> RegionName) {
    return create(ExclusiveStartGlobalTableName, Limit, RegionName);
  }
  public boolean is_ListGlobalTablesInput() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_ExclusiveStartGlobalTableName() {
    return this._ExclusiveStartGlobalTableName;
  }
  public Wrappers_Compile.Option<java.lang.Integer> dtor_Limit() {
    return this._Limit;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_RegionName() {
    return this._RegionName;
  }
}
