// Class ListTagsOfResourceInput
// Dafny class ListTagsOfResourceInput compiled into Java
package software.amazon.cryptography.services.dynamodb.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ListTagsOfResourceInput {
  public dafny.DafnySequence<? extends Character> _ResourceArn;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _NextToken;
  public ListTagsOfResourceInput (dafny.DafnySequence<? extends Character> ResourceArn, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> NextToken) {
    this._ResourceArn = ResourceArn;
    this._NextToken = NextToken;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ListTagsOfResourceInput o = (ListTagsOfResourceInput)other;
    return true && java.util.Objects.equals(this._ResourceArn, o._ResourceArn) && java.util.Objects.equals(this._NextToken, o._NextToken);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ResourceArn);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._NextToken);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsDynamodbTypes.ListTagsOfResourceInput.ListTagsOfResourceInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._ResourceArn));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._NextToken));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ListTagsOfResourceInput> _TYPE = dafny.TypeDescriptor.<ListTagsOfResourceInput>referenceWithInitializer(ListTagsOfResourceInput.class, () -> ListTagsOfResourceInput.Default());
  public static dafny.TypeDescriptor<ListTagsOfResourceInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<ListTagsOfResourceInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ListTagsOfResourceInput theDefault = ListTagsOfResourceInput.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)));
  public static ListTagsOfResourceInput Default() {
    return theDefault;
  }
  public static ListTagsOfResourceInput create(dafny.DafnySequence<? extends Character> ResourceArn, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> NextToken) {
    return new ListTagsOfResourceInput(ResourceArn, NextToken);
  }
  public static ListTagsOfResourceInput create_ListTagsOfResourceInput(dafny.DafnySequence<? extends Character> ResourceArn, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> NextToken) {
    return create(ResourceArn, NextToken);
  }
  public boolean is_ListTagsOfResourceInput() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_ResourceArn() {
    return this._ResourceArn;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_NextToken() {
    return this._NextToken;
  }
}
