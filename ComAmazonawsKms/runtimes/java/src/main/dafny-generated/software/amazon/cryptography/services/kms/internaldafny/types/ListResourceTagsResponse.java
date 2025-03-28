// Class ListResourceTagsResponse
// Dafny class ListResourceTagsResponse compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ListResourceTagsResponse {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Tag>> _Tags;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _NextMarker;
  public Wrappers_Compile.Option<Boolean> _Truncated;
  public ListResourceTagsResponse (Wrappers_Compile.Option<dafny.DafnySequence<? extends Tag>> Tags, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> NextMarker, Wrappers_Compile.Option<Boolean> Truncated) {
    this._Tags = Tags;
    this._NextMarker = NextMarker;
    this._Truncated = Truncated;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ListResourceTagsResponse o = (ListResourceTagsResponse)other;
    return true && java.util.Objects.equals(this._Tags, o._Tags) && java.util.Objects.equals(this._NextMarker, o._NextMarker) && java.util.Objects.equals(this._Truncated, o._Truncated);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Tags);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._NextMarker);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Truncated);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.ListResourceTagsResponse.ListResourceTagsResponse");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Tags));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._NextMarker));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Truncated));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ListResourceTagsResponse> _TYPE = dafny.TypeDescriptor.<ListResourceTagsResponse>referenceWithInitializer(ListResourceTagsResponse.class, () -> ListResourceTagsResponse.Default());
  public static dafny.TypeDescriptor<ListResourceTagsResponse> _typeDescriptor() {
    return (dafny.TypeDescriptor<ListResourceTagsResponse>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ListResourceTagsResponse theDefault = software.amazon.cryptography.services.kms.internaldafny.types.ListResourceTagsResponse.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Tag>>Default(dafny.DafnySequence.<Tag>_typeDescriptor(Tag._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(MarkerType._typeDescriptor()), Wrappers_Compile.Option.<Boolean>Default(dafny.TypeDescriptor.BOOLEAN));
  public static ListResourceTagsResponse Default() {
    return theDefault;
  }
  public static ListResourceTagsResponse create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Tag>> Tags, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> NextMarker, Wrappers_Compile.Option<Boolean> Truncated) {
    return new ListResourceTagsResponse(Tags, NextMarker, Truncated);
  }
  public static ListResourceTagsResponse create_ListResourceTagsResponse(Wrappers_Compile.Option<dafny.DafnySequence<? extends Tag>> Tags, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> NextMarker, Wrappers_Compile.Option<Boolean> Truncated) {
    return create(Tags, NextMarker, Truncated);
  }
  public boolean is_ListResourceTagsResponse() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Tag>> dtor_Tags() {
    return this._Tags;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_NextMarker() {
    return this._NextMarker;
  }
  public Wrappers_Compile.Option<Boolean> dtor_Truncated() {
    return this._Truncated;
  }
}
