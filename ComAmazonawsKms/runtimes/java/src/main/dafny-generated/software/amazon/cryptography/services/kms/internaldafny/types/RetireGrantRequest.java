// Class RetireGrantRequest
// Dafny class RetireGrantRequest compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class RetireGrantRequest {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _GrantToken;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _KeyId;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _GrantId;
  public Wrappers_Compile.Option<Boolean> _DryRun;
  public RetireGrantRequest (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> GrantToken, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> GrantId, Wrappers_Compile.Option<Boolean> DryRun) {
    this._GrantToken = GrantToken;
    this._KeyId = KeyId;
    this._GrantId = GrantId;
    this._DryRun = DryRun;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    RetireGrantRequest o = (RetireGrantRequest)other;
    return true && java.util.Objects.equals(this._GrantToken, o._GrantToken) && java.util.Objects.equals(this._KeyId, o._KeyId) && java.util.Objects.equals(this._GrantId, o._GrantId) && java.util.Objects.equals(this._DryRun, o._DryRun);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._GrantToken);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._GrantId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._DryRun);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.RetireGrantRequest.RetireGrantRequest");
    s.append("(");
    s.append(dafny.Helpers.toString(this._GrantToken));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._KeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._GrantId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._DryRun));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<RetireGrantRequest> _TYPE = dafny.TypeDescriptor.<RetireGrantRequest>referenceWithInitializer(RetireGrantRequest.class, () -> RetireGrantRequest.Default());
  public static dafny.TypeDescriptor<RetireGrantRequest> _typeDescriptor() {
    return (dafny.TypeDescriptor<RetireGrantRequest>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final RetireGrantRequest theDefault = software.amazon.cryptography.services.kms.internaldafny.types.RetireGrantRequest.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(GrantTokenType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(KeyIdType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(GrantIdType._typeDescriptor()), Wrappers_Compile.Option.<Boolean>Default(dafny.TypeDescriptor.BOOLEAN));
  public static RetireGrantRequest Default() {
    return theDefault;
  }
  public static RetireGrantRequest create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> GrantToken, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> GrantId, Wrappers_Compile.Option<Boolean> DryRun) {
    return new RetireGrantRequest(GrantToken, KeyId, GrantId, DryRun);
  }
  public static RetireGrantRequest create_RetireGrantRequest(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> GrantToken, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> GrantId, Wrappers_Compile.Option<Boolean> DryRun) {
    return create(GrantToken, KeyId, GrantId, DryRun);
  }
  public boolean is_RetireGrantRequest() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_GrantToken() {
    return this._GrantToken;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_KeyId() {
    return this._KeyId;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_GrantId() {
    return this._GrantId;
  }
  public Wrappers_Compile.Option<Boolean> dtor_DryRun() {
    return this._DryRun;
  }
}
