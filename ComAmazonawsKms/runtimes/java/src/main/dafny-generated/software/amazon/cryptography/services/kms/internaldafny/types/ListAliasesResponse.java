// Class ListAliasesResponse
// Dafny class ListAliasesResponse compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ListAliasesResponse {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends AliasListEntry>> _Aliases;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _NextMarker;
  public Wrappers_Compile.Option<Boolean> _Truncated;
  public ListAliasesResponse (Wrappers_Compile.Option<dafny.DafnySequence<? extends AliasListEntry>> Aliases, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> NextMarker, Wrappers_Compile.Option<Boolean> Truncated) {
    this._Aliases = Aliases;
    this._NextMarker = NextMarker;
    this._Truncated = Truncated;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ListAliasesResponse o = (ListAliasesResponse)other;
    return true && java.util.Objects.equals(this._Aliases, o._Aliases) && java.util.Objects.equals(this._NextMarker, o._NextMarker) && java.util.Objects.equals(this._Truncated, o._Truncated);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Aliases);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._NextMarker);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Truncated);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.ListAliasesResponse.ListAliasesResponse");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Aliases));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._NextMarker));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Truncated));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ListAliasesResponse> _TYPE = dafny.TypeDescriptor.<ListAliasesResponse>referenceWithInitializer(ListAliasesResponse.class, () -> ListAliasesResponse.Default());
  public static dafny.TypeDescriptor<ListAliasesResponse> _typeDescriptor() {
    return (dafny.TypeDescriptor<ListAliasesResponse>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ListAliasesResponse theDefault = software.amazon.cryptography.services.kms.internaldafny.types.ListAliasesResponse.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends AliasListEntry>>Default(dafny.DafnySequence.<AliasListEntry>_typeDescriptor(AliasListEntry._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(MarkerType._typeDescriptor()), Wrappers_Compile.Option.<Boolean>Default(dafny.TypeDescriptor.BOOLEAN));
  public static ListAliasesResponse Default() {
    return theDefault;
  }
  public static ListAliasesResponse create(Wrappers_Compile.Option<dafny.DafnySequence<? extends AliasListEntry>> Aliases, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> NextMarker, Wrappers_Compile.Option<Boolean> Truncated) {
    return new ListAliasesResponse(Aliases, NextMarker, Truncated);
  }
  public static ListAliasesResponse create_ListAliasesResponse(Wrappers_Compile.Option<dafny.DafnySequence<? extends AliasListEntry>> Aliases, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> NextMarker, Wrappers_Compile.Option<Boolean> Truncated) {
    return create(Aliases, NextMarker, Truncated);
  }
  public boolean is_ListAliasesResponse() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends AliasListEntry>> dtor_Aliases() {
    return this._Aliases;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_NextMarker() {
    return this._NextMarker;
  }
  public Wrappers_Compile.Option<Boolean> dtor_Truncated() {
    return this._Truncated;
  }
}
