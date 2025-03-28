// Class ReplicateKeyRequest
// Dafny class ReplicateKeyRequest compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ReplicateKeyRequest {
  public dafny.DafnySequence<? extends Character> _KeyId;
  public dafny.DafnySequence<? extends Character> _ReplicaRegion;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _Policy;
  public Wrappers_Compile.Option<Boolean> _BypassPolicyLockoutSafetyCheck;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _Description;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Tag>> _Tags;
  public ReplicateKeyRequest (dafny.DafnySequence<? extends Character> KeyId, dafny.DafnySequence<? extends Character> ReplicaRegion, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Policy, Wrappers_Compile.Option<Boolean> BypassPolicyLockoutSafetyCheck, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Description, Wrappers_Compile.Option<dafny.DafnySequence<? extends Tag>> Tags) {
    this._KeyId = KeyId;
    this._ReplicaRegion = ReplicaRegion;
    this._Policy = Policy;
    this._BypassPolicyLockoutSafetyCheck = BypassPolicyLockoutSafetyCheck;
    this._Description = Description;
    this._Tags = Tags;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ReplicateKeyRequest o = (ReplicateKeyRequest)other;
    return true && java.util.Objects.equals(this._KeyId, o._KeyId) && java.util.Objects.equals(this._ReplicaRegion, o._ReplicaRegion) && java.util.Objects.equals(this._Policy, o._Policy) && java.util.Objects.equals(this._BypassPolicyLockoutSafetyCheck, o._BypassPolicyLockoutSafetyCheck) && java.util.Objects.equals(this._Description, o._Description) && java.util.Objects.equals(this._Tags, o._Tags);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ReplicaRegion);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Policy);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._BypassPolicyLockoutSafetyCheck);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Description);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Tags);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.ReplicateKeyRequest.ReplicateKeyRequest");
    s.append("(");
    s.append(dafny.Helpers.toString(this._KeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ReplicaRegion));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Policy));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._BypassPolicyLockoutSafetyCheck));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Description));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Tags));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ReplicateKeyRequest> _TYPE = dafny.TypeDescriptor.<ReplicateKeyRequest>referenceWithInitializer(ReplicateKeyRequest.class, () -> ReplicateKeyRequest.Default());
  public static dafny.TypeDescriptor<ReplicateKeyRequest> _typeDescriptor() {
    return (dafny.TypeDescriptor<ReplicateKeyRequest>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ReplicateKeyRequest theDefault = software.amazon.cryptography.services.kms.internaldafny.types.ReplicateKeyRequest.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(PolicyType._typeDescriptor()), Wrappers_Compile.Option.<Boolean>Default(dafny.TypeDescriptor.BOOLEAN), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(DescriptionType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Tag>>Default(dafny.DafnySequence.<Tag>_typeDescriptor(Tag._typeDescriptor())));
  public static ReplicateKeyRequest Default() {
    return theDefault;
  }
  public static ReplicateKeyRequest create(dafny.DafnySequence<? extends Character> KeyId, dafny.DafnySequence<? extends Character> ReplicaRegion, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Policy, Wrappers_Compile.Option<Boolean> BypassPolicyLockoutSafetyCheck, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Description, Wrappers_Compile.Option<dafny.DafnySequence<? extends Tag>> Tags) {
    return new ReplicateKeyRequest(KeyId, ReplicaRegion, Policy, BypassPolicyLockoutSafetyCheck, Description, Tags);
  }
  public static ReplicateKeyRequest create_ReplicateKeyRequest(dafny.DafnySequence<? extends Character> KeyId, dafny.DafnySequence<? extends Character> ReplicaRegion, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Policy, Wrappers_Compile.Option<Boolean> BypassPolicyLockoutSafetyCheck, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Description, Wrappers_Compile.Option<dafny.DafnySequence<? extends Tag>> Tags) {
    return create(KeyId, ReplicaRegion, Policy, BypassPolicyLockoutSafetyCheck, Description, Tags);
  }
  public boolean is_ReplicateKeyRequest() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_KeyId() {
    return this._KeyId;
  }
  public dafny.DafnySequence<? extends Character> dtor_ReplicaRegion() {
    return this._ReplicaRegion;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_Policy() {
    return this._Policy;
  }
  public Wrappers_Compile.Option<Boolean> dtor_BypassPolicyLockoutSafetyCheck() {
    return this._BypassPolicyLockoutSafetyCheck;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_Description() {
    return this._Description;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Tag>> dtor_Tags() {
    return this._Tags;
  }
}
