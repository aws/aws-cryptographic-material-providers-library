// Class ListKeysResponse
// Dafny class ListKeysResponse compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ListKeysResponse {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends KeyListEntry>> _Keys;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _NextMarker;
  public Wrappers_Compile.Option<Boolean> _Truncated;
  public ListKeysResponse (Wrappers_Compile.Option<dafny.DafnySequence<? extends KeyListEntry>> Keys, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> NextMarker, Wrappers_Compile.Option<Boolean> Truncated) {
    this._Keys = Keys;
    this._NextMarker = NextMarker;
    this._Truncated = Truncated;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ListKeysResponse o = (ListKeysResponse)other;
    return true && java.util.Objects.equals(this._Keys, o._Keys) && java.util.Objects.equals(this._NextMarker, o._NextMarker) && java.util.Objects.equals(this._Truncated, o._Truncated);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Keys);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._NextMarker);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Truncated);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.ListKeysResponse.ListKeysResponse");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Keys));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._NextMarker));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Truncated));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ListKeysResponse> _TYPE = dafny.TypeDescriptor.<ListKeysResponse>referenceWithInitializer(ListKeysResponse.class, () -> ListKeysResponse.Default());
  public static dafny.TypeDescriptor<ListKeysResponse> _typeDescriptor() {
    return (dafny.TypeDescriptor<ListKeysResponse>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ListKeysResponse theDefault = ListKeysResponse.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends KeyListEntry>>Default(dafny.DafnySequence.<KeyListEntry>_typeDescriptor(KeyListEntry._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(MarkerType._typeDescriptor()), Wrappers_Compile.Option.<Boolean>Default(dafny.TypeDescriptor.BOOLEAN));
  public static ListKeysResponse Default() {
    return theDefault;
  }
  public static ListKeysResponse create(Wrappers_Compile.Option<dafny.DafnySequence<? extends KeyListEntry>> Keys, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> NextMarker, Wrappers_Compile.Option<Boolean> Truncated) {
    return new ListKeysResponse(Keys, NextMarker, Truncated);
  }
  public static ListKeysResponse create_ListKeysResponse(Wrappers_Compile.Option<dafny.DafnySequence<? extends KeyListEntry>> Keys, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> NextMarker, Wrappers_Compile.Option<Boolean> Truncated) {
    return create(Keys, NextMarker, Truncated);
  }
  public boolean is_ListKeysResponse() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends KeyListEntry>> dtor_Keys() {
    return this._Keys;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_NextMarker() {
    return this._NextMarker;
  }
  public Wrappers_Compile.Option<Boolean> dtor_Truncated() {
    return this._Truncated;
  }
}
