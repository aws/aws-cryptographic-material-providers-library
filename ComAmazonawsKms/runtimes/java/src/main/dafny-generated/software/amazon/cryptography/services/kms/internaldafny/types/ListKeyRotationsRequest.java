// Class ListKeyRotationsRequest
// Dafny class ListKeyRotationsRequest compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ListKeyRotationsRequest {
  public dafny.DafnySequence<? extends Character> _KeyId;
  public Wrappers_Compile.Option<java.lang.Integer> _Limit;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _Marker;
  public ListKeyRotationsRequest (dafny.DafnySequence<? extends Character> KeyId, Wrappers_Compile.Option<java.lang.Integer> Limit, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Marker) {
    this._KeyId = KeyId;
    this._Limit = Limit;
    this._Marker = Marker;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ListKeyRotationsRequest o = (ListKeyRotationsRequest)other;
    return true && java.util.Objects.equals(this._KeyId, o._KeyId) && java.util.Objects.equals(this._Limit, o._Limit) && java.util.Objects.equals(this._Marker, o._Marker);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Limit);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Marker);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.ListKeyRotationsRequest.ListKeyRotationsRequest");
    s.append("(");
    s.append(dafny.Helpers.toString(this._KeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Limit));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Marker));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ListKeyRotationsRequest> _TYPE = dafny.TypeDescriptor.<ListKeyRotationsRequest>referenceWithInitializer(ListKeyRotationsRequest.class, () -> ListKeyRotationsRequest.Default());
  public static dafny.TypeDescriptor<ListKeyRotationsRequest> _typeDescriptor() {
    return (dafny.TypeDescriptor<ListKeyRotationsRequest>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ListKeyRotationsRequest theDefault = ListKeyRotationsRequest.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<java.lang.Integer>Default(LimitType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(MarkerType._typeDescriptor()));
  public static ListKeyRotationsRequest Default() {
    return theDefault;
  }
  public static ListKeyRotationsRequest create(dafny.DafnySequence<? extends Character> KeyId, Wrappers_Compile.Option<java.lang.Integer> Limit, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Marker) {
    return new ListKeyRotationsRequest(KeyId, Limit, Marker);
  }
  public static ListKeyRotationsRequest create_ListKeyRotationsRequest(dafny.DafnySequence<? extends Character> KeyId, Wrappers_Compile.Option<java.lang.Integer> Limit, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Marker) {
    return create(KeyId, Limit, Marker);
  }
  public boolean is_ListKeyRotationsRequest() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_KeyId() {
    return this._KeyId;
  }
  public Wrappers_Compile.Option<java.lang.Integer> dtor_Limit() {
    return this._Limit;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_Marker() {
    return this._Marker;
  }
}
