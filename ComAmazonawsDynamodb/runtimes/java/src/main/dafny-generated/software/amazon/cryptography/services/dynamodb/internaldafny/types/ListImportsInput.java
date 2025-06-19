// Class ListImportsInput
// Dafny class ListImportsInput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ListImportsInput {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _TableArn;
  public Wrappers_Compile.Option<java.lang.Integer> _PageSize;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _NextToken;
  public ListImportsInput (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableArn, Wrappers_Compile.Option<java.lang.Integer> PageSize, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> NextToken) {
    this._TableArn = TableArn;
    this._PageSize = PageSize;
    this._NextToken = NextToken;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ListImportsInput o = (ListImportsInput)other;
    return true && java.util.Objects.equals(this._TableArn, o._TableArn) && java.util.Objects.equals(this._PageSize, o._PageSize) && java.util.Objects.equals(this._NextToken, o._NextToken);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TableArn);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._PageSize);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._NextToken);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ListImportsInput.ListImportsInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._TableArn));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._PageSize));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._NextToken));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ListImportsInput> _TYPE = dafny.TypeDescriptor.<ListImportsInput>referenceWithInitializer(ListImportsInput.class, () -> ListImportsInput.Default());
  public static dafny.TypeDescriptor<ListImportsInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<ListImportsInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ListImportsInput theDefault = ListImportsInput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(TableArn._typeDescriptor()), Wrappers_Compile.Option.<java.lang.Integer>Default(ListImportsMaxLimit._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(ImportNextToken._typeDescriptor()));
  public static ListImportsInput Default() {
    return theDefault;
  }
  public static ListImportsInput create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableArn, Wrappers_Compile.Option<java.lang.Integer> PageSize, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> NextToken) {
    return new ListImportsInput(TableArn, PageSize, NextToken);
  }
  public static ListImportsInput create_ListImportsInput(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> TableArn, Wrappers_Compile.Option<java.lang.Integer> PageSize, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> NextToken) {
    return create(TableArn, PageSize, NextToken);
  }
  public boolean is_ListImportsInput() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_TableArn() {
    return this._TableArn;
  }
  public Wrappers_Compile.Option<java.lang.Integer> dtor_PageSize() {
    return this._PageSize;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_NextToken() {
    return this._NextToken;
  }
}
