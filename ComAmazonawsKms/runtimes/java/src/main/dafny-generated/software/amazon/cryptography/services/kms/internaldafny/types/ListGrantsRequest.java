// Class ListGrantsRequest
// Dafny class ListGrantsRequest compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ListGrantsRequest {
  public Wrappers_Compile.Option<java.lang.Integer> _Limit;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _Marker;
  public dafny.DafnySequence<? extends Character> _KeyId;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _GrantId;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _GranteePrincipal;
  public ListGrantsRequest (Wrappers_Compile.Option<java.lang.Integer> Limit, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Marker, dafny.DafnySequence<? extends Character> KeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> GrantId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> GranteePrincipal) {
    this._Limit = Limit;
    this._Marker = Marker;
    this._KeyId = KeyId;
    this._GrantId = GrantId;
    this._GranteePrincipal = GranteePrincipal;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ListGrantsRequest o = (ListGrantsRequest)other;
    return true && java.util.Objects.equals(this._Limit, o._Limit) && java.util.Objects.equals(this._Marker, o._Marker) && java.util.Objects.equals(this._KeyId, o._KeyId) && java.util.Objects.equals(this._GrantId, o._GrantId) && java.util.Objects.equals(this._GranteePrincipal, o._GranteePrincipal);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Limit);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Marker);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._GrantId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._GranteePrincipal);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.ListGrantsRequest.ListGrantsRequest");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Limit));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Marker));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._KeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._GrantId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._GranteePrincipal));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ListGrantsRequest> _TYPE = dafny.TypeDescriptor.<ListGrantsRequest>referenceWithInitializer(ListGrantsRequest.class, () -> ListGrantsRequest.Default());
  public static dafny.TypeDescriptor<ListGrantsRequest> _typeDescriptor() {
    return (dafny.TypeDescriptor<ListGrantsRequest>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ListGrantsRequest theDefault = ListGrantsRequest.create(Wrappers_Compile.Option.<java.lang.Integer>Default(LimitType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(MarkerType._typeDescriptor()), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(GrantIdType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(PrincipalIdType._typeDescriptor()));
  public static ListGrantsRequest Default() {
    return theDefault;
  }
  public static ListGrantsRequest create(Wrappers_Compile.Option<java.lang.Integer> Limit, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Marker, dafny.DafnySequence<? extends Character> KeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> GrantId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> GranteePrincipal) {
    return new ListGrantsRequest(Limit, Marker, KeyId, GrantId, GranteePrincipal);
  }
  public static ListGrantsRequest create_ListGrantsRequest(Wrappers_Compile.Option<java.lang.Integer> Limit, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Marker, dafny.DafnySequence<? extends Character> KeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> GrantId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> GranteePrincipal) {
    return create(Limit, Marker, KeyId, GrantId, GranteePrincipal);
  }
  public boolean is_ListGrantsRequest() { return true; }
  public Wrappers_Compile.Option<java.lang.Integer> dtor_Limit() {
    return this._Limit;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_Marker() {
    return this._Marker;
  }
  public dafny.DafnySequence<? extends Character> dtor_KeyId() {
    return this._KeyId;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_GrantId() {
    return this._GrantId;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_GranteePrincipal() {
    return this._GranteePrincipal;
  }
}
