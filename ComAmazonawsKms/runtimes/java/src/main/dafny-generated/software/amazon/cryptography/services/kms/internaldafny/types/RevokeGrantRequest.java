// Class RevokeGrantRequest
// Dafny class RevokeGrantRequest compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class RevokeGrantRequest {
  public dafny.DafnySequence<? extends Character> _KeyId;
  public dafny.DafnySequence<? extends Character> _GrantId;
  public Wrappers_Compile.Option<Boolean> _DryRun;
  public RevokeGrantRequest (dafny.DafnySequence<? extends Character> KeyId, dafny.DafnySequence<? extends Character> GrantId, Wrappers_Compile.Option<Boolean> DryRun) {
    this._KeyId = KeyId;
    this._GrantId = GrantId;
    this._DryRun = DryRun;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    RevokeGrantRequest o = (RevokeGrantRequest)other;
    return true && java.util.Objects.equals(this._KeyId, o._KeyId) && java.util.Objects.equals(this._GrantId, o._GrantId) && java.util.Objects.equals(this._DryRun, o._DryRun);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._GrantId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._DryRun);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.RevokeGrantRequest.RevokeGrantRequest");
    s.append("(");
    s.append(dafny.Helpers.toString(this._KeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._GrantId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._DryRun));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<RevokeGrantRequest> _TYPE = dafny.TypeDescriptor.<RevokeGrantRequest>referenceWithInitializer(RevokeGrantRequest.class, () -> RevokeGrantRequest.Default());
  public static dafny.TypeDescriptor<RevokeGrantRequest> _typeDescriptor() {
    return (dafny.TypeDescriptor<RevokeGrantRequest>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final RevokeGrantRequest theDefault = software.amazon.cryptography.services.kms.internaldafny.types.RevokeGrantRequest.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<Boolean>Default(dafny.TypeDescriptor.BOOLEAN));
  public static RevokeGrantRequest Default() {
    return theDefault;
  }
  public static RevokeGrantRequest create(dafny.DafnySequence<? extends Character> KeyId, dafny.DafnySequence<? extends Character> GrantId, Wrappers_Compile.Option<Boolean> DryRun) {
    return new RevokeGrantRequest(KeyId, GrantId, DryRun);
  }
  public static RevokeGrantRequest create_RevokeGrantRequest(dafny.DafnySequence<? extends Character> KeyId, dafny.DafnySequence<? extends Character> GrantId, Wrappers_Compile.Option<Boolean> DryRun) {
    return create(KeyId, GrantId, DryRun);
  }
  public boolean is_RevokeGrantRequest() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_KeyId() {
    return this._KeyId;
  }
  public dafny.DafnySequence<? extends Character> dtor_GrantId() {
    return this._GrantId;
  }
  public Wrappers_Compile.Option<Boolean> dtor_DryRun() {
    return this._DryRun;
  }
}
