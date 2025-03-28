// Class GetPublicKeyRequest
// Dafny class GetPublicKeyRequest compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class GetPublicKeyRequest {
  public dafny.DafnySequence<? extends Character> _KeyId;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> _GrantTokens;
  public GetPublicKeyRequest (dafny.DafnySequence<? extends Character> KeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> GrantTokens) {
    this._KeyId = KeyId;
    this._GrantTokens = GrantTokens;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GetPublicKeyRequest o = (GetPublicKeyRequest)other;
    return true && java.util.Objects.equals(this._KeyId, o._KeyId) && java.util.Objects.equals(this._GrantTokens, o._GrantTokens);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._GrantTokens);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.GetPublicKeyRequest.GetPublicKeyRequest");
    s.append("(");
    s.append(dafny.Helpers.toString(this._KeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._GrantTokens));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<GetPublicKeyRequest> _TYPE = dafny.TypeDescriptor.<GetPublicKeyRequest>referenceWithInitializer(GetPublicKeyRequest.class, () -> GetPublicKeyRequest.Default());
  public static dafny.TypeDescriptor<GetPublicKeyRequest> _typeDescriptor() {
    return (dafny.TypeDescriptor<GetPublicKeyRequest>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GetPublicKeyRequest theDefault = software.amazon.cryptography.services.kms.internaldafny.types.GetPublicKeyRequest.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>Default(GrantTokenList._typeDescriptor()));
  public static GetPublicKeyRequest Default() {
    return theDefault;
  }
  public static GetPublicKeyRequest create(dafny.DafnySequence<? extends Character> KeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> GrantTokens) {
    return new GetPublicKeyRequest(KeyId, GrantTokens);
  }
  public static GetPublicKeyRequest create_GetPublicKeyRequest(dafny.DafnySequence<? extends Character> KeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> GrantTokens) {
    return create(KeyId, GrantTokens);
  }
  public boolean is_GetPublicKeyRequest() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_KeyId() {
    return this._KeyId;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> dtor_GrantTokens() {
    return this._GrantTokens;
  }
}
