// Class GetKeyPolicyResponse
// Dafny class GetKeyPolicyResponse compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class GetKeyPolicyResponse {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _Policy;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _PolicyName;
  public GetKeyPolicyResponse (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Policy, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> PolicyName) {
    this._Policy = Policy;
    this._PolicyName = PolicyName;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GetKeyPolicyResponse o = (GetKeyPolicyResponse)other;
    return true && java.util.Objects.equals(this._Policy, o._Policy) && java.util.Objects.equals(this._PolicyName, o._PolicyName);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Policy);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._PolicyName);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.GetKeyPolicyResponse.GetKeyPolicyResponse");
    s.append("(");
    s.append(dafny.Helpers.toString(this._Policy));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._PolicyName));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<GetKeyPolicyResponse> _TYPE = dafny.TypeDescriptor.<GetKeyPolicyResponse>referenceWithInitializer(GetKeyPolicyResponse.class, () -> GetKeyPolicyResponse.Default());
  public static dafny.TypeDescriptor<GetKeyPolicyResponse> _typeDescriptor() {
    return (dafny.TypeDescriptor<GetKeyPolicyResponse>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GetKeyPolicyResponse theDefault = software.amazon.cryptography.services.kms.internaldafny.types.GetKeyPolicyResponse.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(PolicyType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(PolicyNameType._typeDescriptor()));
  public static GetKeyPolicyResponse Default() {
    return theDefault;
  }
  public static GetKeyPolicyResponse create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Policy, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> PolicyName) {
    return new GetKeyPolicyResponse(Policy, PolicyName);
  }
  public static GetKeyPolicyResponse create_GetKeyPolicyResponse(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Policy, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> PolicyName) {
    return create(Policy, PolicyName);
  }
  public boolean is_GetKeyPolicyResponse() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_Policy() {
    return this._Policy;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_PolicyName() {
    return this._PolicyName;
  }
}
