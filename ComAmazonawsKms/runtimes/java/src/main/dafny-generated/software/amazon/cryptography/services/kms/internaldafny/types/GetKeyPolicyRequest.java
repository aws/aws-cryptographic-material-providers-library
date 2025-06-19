// Class GetKeyPolicyRequest
// Dafny class GetKeyPolicyRequest compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class GetKeyPolicyRequest {
  public dafny.DafnySequence<? extends Character> _KeyId;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _PolicyName;
  public GetKeyPolicyRequest (dafny.DafnySequence<? extends Character> KeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> PolicyName) {
    this._KeyId = KeyId;
    this._PolicyName = PolicyName;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GetKeyPolicyRequest o = (GetKeyPolicyRequest)other;
    return true && java.util.Objects.equals(this._KeyId, o._KeyId) && java.util.Objects.equals(this._PolicyName, o._PolicyName);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._PolicyName);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.GetKeyPolicyRequest.GetKeyPolicyRequest");
    s.append("(");
    s.append(dafny.Helpers.toString(this._KeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._PolicyName));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<GetKeyPolicyRequest> _TYPE = dafny.TypeDescriptor.<GetKeyPolicyRequest>referenceWithInitializer(GetKeyPolicyRequest.class, () -> GetKeyPolicyRequest.Default());
  public static dafny.TypeDescriptor<GetKeyPolicyRequest> _typeDescriptor() {
    return (dafny.TypeDescriptor<GetKeyPolicyRequest>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GetKeyPolicyRequest theDefault = GetKeyPolicyRequest.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(PolicyNameType._typeDescriptor()));
  public static GetKeyPolicyRequest Default() {
    return theDefault;
  }
  public static GetKeyPolicyRequest create(dafny.DafnySequence<? extends Character> KeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> PolicyName) {
    return new GetKeyPolicyRequest(KeyId, PolicyName);
  }
  public static GetKeyPolicyRequest create_GetKeyPolicyRequest(dafny.DafnySequence<? extends Character> KeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> PolicyName) {
    return create(KeyId, PolicyName);
  }
  public boolean is_GetKeyPolicyRequest() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_KeyId() {
    return this._KeyId;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_PolicyName() {
    return this._PolicyName;
  }
}
