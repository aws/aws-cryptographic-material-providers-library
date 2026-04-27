// Class ListTagsOfResourceOutput
// Dafny class ListTagsOfResourceOutput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ListTagsOfResourceOutput {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Tag>> _Tags;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _NextToken;
  public ListTagsOfResourceOutput (Wrappers_Compile.Option<dafny.DafnySequence<? extends Tag>> Tags, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> NextToken) {
    this._Tags = Tags;
    this._NextToken = NextToken;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ListTagsOfResourceOutput o = (ListTagsOfResourceOutput)other;
    return true && java.util.Objects.equals(this._Tags, o._Tags) && java.util.Objects.equals(this._NextToken, o._NextToken);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Tags);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._NextToken);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ListTagsOfResourceOutput.ListTagsOfResourceOutput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Tags));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._NextToken));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ListTagsOfResourceOutput> _TYPE = dafny.TypeDescriptor.<ListTagsOfResourceOutput>referenceWithInitializer(ListTagsOfResourceOutput.class, () -> ListTagsOfResourceOutput.Default());
  public static dafny.TypeDescriptor<ListTagsOfResourceOutput> _typeDescriptor() {
    return (dafny.TypeDescriptor<ListTagsOfResourceOutput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ListTagsOfResourceOutput theDefault = ListTagsOfResourceOutput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Tag>>Default(dafny.DafnySequence.<Tag>_typeDescriptor(Tag._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)));
  public static ListTagsOfResourceOutput Default() {
    return theDefault;
  }
  public static ListTagsOfResourceOutput create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Tag>> Tags, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> NextToken) {
    return new ListTagsOfResourceOutput(Tags, NextToken);
  }
  public static ListTagsOfResourceOutput create_ListTagsOfResourceOutput(Wrappers_Compile.Option<dafny.DafnySequence<? extends Tag>> Tags, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> NextToken) {
    return create(Tags, NextToken);
  }
  public boolean is_ListTagsOfResourceOutput() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Tag>> dtor_Tags() {
    return this._Tags;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_NextToken() {
    return this._NextToken;
  }
}
