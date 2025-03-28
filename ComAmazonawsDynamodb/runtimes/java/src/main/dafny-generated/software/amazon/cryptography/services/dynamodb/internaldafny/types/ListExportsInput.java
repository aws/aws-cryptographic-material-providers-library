// Class ListExportsInput
// Dafny class ListExportsInput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ListExportsInput {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _TableArn;
  public Wrappers_Compile.Option<java.lang.Integer> _MaxResults;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _NextToken;
  public ListExportsInput (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableArn, Wrappers_Compile.Option<java.lang.Integer> MaxResults, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> NextToken) {
    this._TableArn = TableArn;
    this._MaxResults = MaxResults;
    this._NextToken = NextToken;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ListExportsInput o = (ListExportsInput)other;
    return true && java.util.Objects.equals(this._TableArn, o._TableArn) && java.util.Objects.equals(this._MaxResults, o._MaxResults) && java.util.Objects.equals(this._NextToken, o._NextToken);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableArn);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._MaxResults);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._NextToken);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ListExportsInput.ListExportsInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._TableArn));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._MaxResults));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._NextToken));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ListExportsInput> _TYPE = dafny.TypeDescriptor.<ListExportsInput>referenceWithInitializer(ListExportsInput.class, () -> ListExportsInput.Default());
  public static dafny.TypeDescriptor<ListExportsInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<ListExportsInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ListExportsInput theDefault = software.amazon.cryptography.services.dynamodb.internaldafny.types.ListExportsInput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(TableArn._typeDescriptor()), Wrappers_Compile.Option.<java.lang.Integer>Default(ListExportsMaxLimit._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)));
  public static ListExportsInput Default() {
    return theDefault;
  }
  public static ListExportsInput create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableArn, Wrappers_Compile.Option<java.lang.Integer> MaxResults, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> NextToken) {
    return new ListExportsInput(TableArn, MaxResults, NextToken);
  }
  public static ListExportsInput create_ListExportsInput(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableArn, Wrappers_Compile.Option<java.lang.Integer> MaxResults, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> NextToken) {
    return create(TableArn, MaxResults, NextToken);
  }
  public boolean is_ListExportsInput() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_TableArn() {
    return this._TableArn;
  }
  public Wrappers_Compile.Option<java.lang.Integer> dtor_MaxResults() {
    return this._MaxResults;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_NextToken() {
    return this._NextToken;
  }
}
