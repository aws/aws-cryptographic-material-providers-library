// Class GetKeyRotationStatusRequest
// Dafny class GetKeyRotationStatusRequest compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class GetKeyRotationStatusRequest {
  public dafny.DafnySequence<? extends Character> _KeyId;
  public GetKeyRotationStatusRequest (dafny.DafnySequence<? extends Character> KeyId) {
    this._KeyId = KeyId;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GetKeyRotationStatusRequest o = (GetKeyRotationStatusRequest)other;
    return true && java.util.Objects.equals(this._KeyId, o._KeyId);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyId);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.GetKeyRotationStatusRequest.GetKeyRotationStatusRequest");
    s.append("(");
    s.append(dafny.Helpers.toString(this._KeyId));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<GetKeyRotationStatusRequest> _TYPE = dafny.TypeDescriptor.<GetKeyRotationStatusRequest>referenceWithInitializer(GetKeyRotationStatusRequest.class, () -> GetKeyRotationStatusRequest.Default());
  public static dafny.TypeDescriptor<GetKeyRotationStatusRequest> _typeDescriptor() {
    return (dafny.TypeDescriptor<GetKeyRotationStatusRequest>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GetKeyRotationStatusRequest theDefault = software.amazon.cryptography.services.kms.internaldafny.types.GetKeyRotationStatusRequest.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static GetKeyRotationStatusRequest Default() {
    return theDefault;
  }
  public static GetKeyRotationStatusRequest create(dafny.DafnySequence<? extends Character> KeyId) {
    return new GetKeyRotationStatusRequest(KeyId);
  }
  public static GetKeyRotationStatusRequest create_GetKeyRotationStatusRequest(dafny.DafnySequence<? extends Character> KeyId) {
    return create(KeyId);
  }
  public boolean is_GetKeyRotationStatusRequest() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_KeyId() {
    return this._KeyId;
  }
}
