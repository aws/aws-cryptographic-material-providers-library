// Class PutKeyPolicyRequest
// Dafny class PutKeyPolicyRequest compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class PutKeyPolicyRequest {
  public dafny.DafnySequence<? extends Character> _KeyId;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _PolicyName;
  public dafny.DafnySequence<? extends Character> _Policy;
  public Wrappers_Compile.Option<Boolean> _BypassPolicyLockoutSafetyCheck;
  public PutKeyPolicyRequest (dafny.DafnySequence<? extends Character> KeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> PolicyName, dafny.DafnySequence<? extends Character> Policy, Wrappers_Compile.Option<Boolean> BypassPolicyLockoutSafetyCheck) {
    this._KeyId = KeyId;
    this._PolicyName = PolicyName;
    this._Policy = Policy;
    this._BypassPolicyLockoutSafetyCheck = BypassPolicyLockoutSafetyCheck;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    PutKeyPolicyRequest o = (PutKeyPolicyRequest)other;
    return true && java.util.Objects.equals(this._KeyId, o._KeyId) && java.util.Objects.equals(this._PolicyName, o._PolicyName) && java.util.Objects.equals(this._Policy, o._Policy) && java.util.Objects.equals(this._BypassPolicyLockoutSafetyCheck, o._BypassPolicyLockoutSafetyCheck);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._PolicyName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Policy);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._BypassPolicyLockoutSafetyCheck);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.PutKeyPolicyRequest.PutKeyPolicyRequest");
    s.append("(");
    s.append(dafny.Helpers.toString(this._KeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._PolicyName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Policy));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._BypassPolicyLockoutSafetyCheck));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<PutKeyPolicyRequest> _TYPE = dafny.TypeDescriptor.<PutKeyPolicyRequest>referenceWithInitializer(PutKeyPolicyRequest.class, () -> PutKeyPolicyRequest.Default());
  public static dafny.TypeDescriptor<PutKeyPolicyRequest> _typeDescriptor() {
    return (dafny.TypeDescriptor<PutKeyPolicyRequest>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final PutKeyPolicyRequest theDefault = PutKeyPolicyRequest.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(PolicyNameType._typeDescriptor()), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<Boolean>Default(dafny.TypeDescriptor.BOOLEAN));
  public static PutKeyPolicyRequest Default() {
    return theDefault;
  }
  public static PutKeyPolicyRequest create(dafny.DafnySequence<? extends Character> KeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> PolicyName, dafny.DafnySequence<? extends Character> Policy, Wrappers_Compile.Option<Boolean> BypassPolicyLockoutSafetyCheck) {
    return new PutKeyPolicyRequest(KeyId, PolicyName, Policy, BypassPolicyLockoutSafetyCheck);
  }
  public static PutKeyPolicyRequest create_PutKeyPolicyRequest(dafny.DafnySequence<? extends Character> KeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> PolicyName, dafny.DafnySequence<? extends Character> Policy, Wrappers_Compile.Option<Boolean> BypassPolicyLockoutSafetyCheck) {
    return create(KeyId, PolicyName, Policy, BypassPolicyLockoutSafetyCheck);
  }
  public boolean is_PutKeyPolicyRequest() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_KeyId() {
    return this._KeyId;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_PolicyName() {
    return this._PolicyName;
  }
  public dafny.DafnySequence<? extends Character> dtor_Policy() {
    return this._Policy;
  }
  public Wrappers_Compile.Option<Boolean> dtor_BypassPolicyLockoutSafetyCheck() {
    return this._BypassPolicyLockoutSafetyCheck;
  }
}
