// Class DisableKeyRotationRequest
// Dafny class DisableKeyRotationRequest compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class DisableKeyRotationRequest {
  public dafny.DafnySequence<? extends Character> _KeyId;
  public DisableKeyRotationRequest (dafny.DafnySequence<? extends Character> KeyId) {
    this._KeyId = KeyId;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DisableKeyRotationRequest o = (DisableKeyRotationRequest)other;
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
    s.append("ComAmazonawsKmsTypes.DisableKeyRotationRequest.DisableKeyRotationRequest");
    s.append("(");
    s.append(dafny.Helpers.toString(this._KeyId));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DisableKeyRotationRequest> _TYPE = dafny.TypeDescriptor.<DisableKeyRotationRequest>referenceWithInitializer(DisableKeyRotationRequest.class, () -> DisableKeyRotationRequest.Default());
  public static dafny.TypeDescriptor<DisableKeyRotationRequest> _typeDescriptor() {
    return (dafny.TypeDescriptor<DisableKeyRotationRequest>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DisableKeyRotationRequest theDefault = software.amazon.cryptography.services.kms.internaldafny.types.DisableKeyRotationRequest.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static DisableKeyRotationRequest Default() {
    return theDefault;
  }
  public static DisableKeyRotationRequest create(dafny.DafnySequence<? extends Character> KeyId) {
    return new DisableKeyRotationRequest(KeyId);
  }
  public static DisableKeyRotationRequest create_DisableKeyRotationRequest(dafny.DafnySequence<? extends Character> KeyId) {
    return create(KeyId);
  }
  public boolean is_DisableKeyRotationRequest() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_KeyId() {
    return this._KeyId;
  }
}
