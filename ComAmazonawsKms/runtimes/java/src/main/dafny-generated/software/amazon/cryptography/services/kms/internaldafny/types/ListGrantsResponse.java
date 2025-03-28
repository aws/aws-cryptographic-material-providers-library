// Class ListGrantsResponse
// Dafny class ListGrantsResponse compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ListGrantsResponse {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends GrantListEntry>> _Grants;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _NextMarker;
  public Wrappers_Compile.Option<Boolean> _Truncated;
  public ListGrantsResponse (Wrappers_Compile.Option<dafny.DafnySequence<? extends GrantListEntry>> Grants, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> NextMarker, Wrappers_Compile.Option<Boolean> Truncated) {
    this._Grants = Grants;
    this._NextMarker = NextMarker;
    this._Truncated = Truncated;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ListGrantsResponse o = (ListGrantsResponse)other;
    return true && java.util.Objects.equals(this._Grants, o._Grants) && java.util.Objects.equals(this._NextMarker, o._NextMarker) && java.util.Objects.equals(this._Truncated, o._Truncated);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Grants);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._NextMarker);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Truncated);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.ListGrantsResponse.ListGrantsResponse");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Grants));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._NextMarker));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Truncated));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ListGrantsResponse> _TYPE = dafny.TypeDescriptor.<ListGrantsResponse>referenceWithInitializer(ListGrantsResponse.class, () -> ListGrantsResponse.Default());
  public static dafny.TypeDescriptor<ListGrantsResponse> _typeDescriptor() {
    return (dafny.TypeDescriptor<ListGrantsResponse>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ListGrantsResponse theDefault = software.amazon.cryptography.services.kms.internaldafny.types.ListGrantsResponse.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends GrantListEntry>>Default(dafny.DafnySequence.<GrantListEntry>_typeDescriptor(GrantListEntry._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(MarkerType._typeDescriptor()), Wrappers_Compile.Option.<Boolean>Default(dafny.TypeDescriptor.BOOLEAN));
  public static ListGrantsResponse Default() {
    return theDefault;
  }
  public static ListGrantsResponse create(Wrappers_Compile.Option<dafny.DafnySequence<? extends GrantListEntry>> Grants, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> NextMarker, Wrappers_Compile.Option<Boolean> Truncated) {
    return new ListGrantsResponse(Grants, NextMarker, Truncated);
  }
  public static ListGrantsResponse create_ListGrantsResponse(Wrappers_Compile.Option<dafny.DafnySequence<? extends GrantListEntry>> Grants, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> NextMarker, Wrappers_Compile.Option<Boolean> Truncated) {
    return create(Grants, NextMarker, Truncated);
  }
  public boolean is_ListGrantsResponse() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends GrantListEntry>> dtor_Grants() {
    return this._Grants;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_NextMarker() {
    return this._NextMarker;
  }
  public Wrappers_Compile.Option<Boolean> dtor_Truncated() {
    return this._Truncated;
  }
}
