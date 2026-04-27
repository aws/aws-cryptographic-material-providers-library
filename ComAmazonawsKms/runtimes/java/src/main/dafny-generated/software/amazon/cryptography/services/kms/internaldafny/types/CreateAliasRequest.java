// Class CreateAliasRequest
// Dafny class CreateAliasRequest compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class CreateAliasRequest {
  public dafny.DafnySequence<? extends Character> _AliasName;
  public dafny.DafnySequence<? extends Character> _TargetKeyId;
  public CreateAliasRequest (dafny.DafnySequence<? extends Character> AliasName, dafny.DafnySequence<? extends Character> TargetKeyId) {
    this._AliasName = AliasName;
    this._TargetKeyId = TargetKeyId;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CreateAliasRequest o = (CreateAliasRequest)other;
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
    s.append("ComAmazonawsKmsTypes.CreateAliasRequest.CreateAliasRequest");
    s.append("(");
    s.append(dafny.Helpers.toString(this._AliasName));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._TargetKeyId));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<CreateAliasRequest> _TYPE = dafny.TypeDescriptor.<CreateAliasRequest>referenceWithInitializer(CreateAliasRequest.class, () -> CreateAliasRequest.Default());
  public static dafny.TypeDescriptor<CreateAliasRequest> _typeDescriptor() {
    return (dafny.TypeDescriptor<CreateAliasRequest>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final CreateAliasRequest theDefault = CreateAliasRequest.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static CreateAliasRequest Default() {
    return theDefault;
  }
  public static CreateAliasRequest create(dafny.DafnySequence<? extends Character> AliasName, dafny.DafnySequence<? extends Character> TargetKeyId) {
    return new CreateAliasRequest(AliasName, TargetKeyId);
  }
  public static CreateAliasRequest create_CreateAliasRequest(dafny.DafnySequence<? extends Character> AliasName, dafny.DafnySequence<? extends Character> TargetKeyId) {
    return create(AliasName, TargetKeyId);
  }
  public boolean is_CreateAliasRequest() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_AliasName() {
    return this._AliasName;
  }
  public dafny.DafnySequence<? extends Character> dtor_TargetKeyId() {
    return this._TargetKeyId;
  }
}
