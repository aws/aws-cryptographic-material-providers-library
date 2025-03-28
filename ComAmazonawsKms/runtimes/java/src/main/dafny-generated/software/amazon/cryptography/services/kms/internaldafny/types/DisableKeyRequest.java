// Class DisableKeyRequest
// Dafny class DisableKeyRequest compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class DisableKeyRequest {
  public dafny.DafnySequence<? extends Character> _KeyId;
  public DisableKeyRequest (dafny.DafnySequence<? extends Character> KeyId) {
    this._KeyId = KeyId;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DisableKeyRequest o = (DisableKeyRequest)other;
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
    s.append("ComAmazonawsKmsTypes.DisableKeyRequest.DisableKeyRequest");
    s.append("(");
    s.append(dafny.Helpers.toString(this._KeyId));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DisableKeyRequest> _TYPE = dafny.TypeDescriptor.<DisableKeyRequest>referenceWithInitializer(DisableKeyRequest.class, () -> DisableKeyRequest.Default());
  public static dafny.TypeDescriptor<DisableKeyRequest> _typeDescriptor() {
    return (dafny.TypeDescriptor<DisableKeyRequest>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DisableKeyRequest theDefault = software.amazon.cryptography.services.kms.internaldafny.types.DisableKeyRequest.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static DisableKeyRequest Default() {
    return theDefault;
  }
  public static DisableKeyRequest create(dafny.DafnySequence<? extends Character> KeyId) {
    return new DisableKeyRequest(KeyId);
  }
  public static DisableKeyRequest create_DisableKeyRequest(dafny.DafnySequence<? extends Character> KeyId) {
    return create(KeyId);
  }
  public boolean is_DisableKeyRequest() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_KeyId() {
    return this._KeyId;
  }
}
