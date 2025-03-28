// Class UpdateAliasRequest
// Dafny class UpdateAliasRequest compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class UpdateAliasRequest {
  public dafny.DafnySequence<? extends Character> _AliasName;
  public dafny.DafnySequence<? extends Character> _TargetKeyId;
  public UpdateAliasRequest (dafny.DafnySequence<? extends Character> AliasName, dafny.DafnySequence<? extends Character> TargetKeyId) {
    this._AliasName = AliasName;
    this._TargetKeyId = TargetKeyId;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    UpdateAliasRequest o = (UpdateAliasRequest)other;
    return true && java.util.Objects.equals(this._AliasName, o._AliasName) && java.util.Objects.equals(this._TargetKeyId, o._TargetKeyId);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._AliasName);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._TargetKeyId);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.UpdateAliasRequest.UpdateAliasRequest");
    s.append("(");
    s.append(dafny.Helpers.toString(this._AliasName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._TargetKeyId));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<UpdateAliasRequest> _TYPE = dafny.TypeDescriptor.<UpdateAliasRequest>referenceWithInitializer(UpdateAliasRequest.class, () -> UpdateAliasRequest.Default());
  public static dafny.TypeDescriptor<UpdateAliasRequest> _typeDescriptor() {
    return (dafny.TypeDescriptor<UpdateAliasRequest>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final UpdateAliasRequest theDefault = software.amazon.cryptography.services.kms.internaldafny.types.UpdateAliasRequest.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static UpdateAliasRequest Default() {
    return theDefault;
  }
  public static UpdateAliasRequest create(dafny.DafnySequence<? extends Character> AliasName, dafny.DafnySequence<? extends Character> TargetKeyId) {
    return new UpdateAliasRequest(AliasName, TargetKeyId);
  }
  public static UpdateAliasRequest create_UpdateAliasRequest(dafny.DafnySequence<? extends Character> AliasName, dafny.DafnySequence<? extends Character> TargetKeyId) {
    return create(AliasName, TargetKeyId);
  }
  public boolean is_UpdateAliasRequest() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_AliasName() {
    return this._AliasName;
  }
  public dafny.DafnySequence<? extends Character> dtor_TargetKeyId() {
    return this._TargetKeyId;
  }
}
