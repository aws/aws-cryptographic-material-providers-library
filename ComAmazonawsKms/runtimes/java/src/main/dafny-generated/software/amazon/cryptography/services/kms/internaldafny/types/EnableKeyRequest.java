// Class EnableKeyRequest
// Dafny class EnableKeyRequest compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class EnableKeyRequest {
  public dafny.DafnySequence<? extends Character> _KeyId;
  public EnableKeyRequest (dafny.DafnySequence<? extends Character> KeyId) {
    this._KeyId = KeyId;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    EnableKeyRequest o = (EnableKeyRequest)other;
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
    s.append("ComAmazonawsKmsTypes.EnableKeyRequest.EnableKeyRequest");
    s.append("(");
    s.append(dafny.Helpers.toString(this._KeyId));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<EnableKeyRequest> _TYPE = dafny.TypeDescriptor.<EnableKeyRequest>referenceWithInitializer(EnableKeyRequest.class, () -> EnableKeyRequest.Default());
  public static dafny.TypeDescriptor<EnableKeyRequest> _typeDescriptor() {
    return (dafny.TypeDescriptor<EnableKeyRequest>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final EnableKeyRequest theDefault = EnableKeyRequest.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static EnableKeyRequest Default() {
    return theDefault;
  }
  public static EnableKeyRequest create(dafny.DafnySequence<? extends Character> KeyId) {
    return new EnableKeyRequest(KeyId);
  }
  public static EnableKeyRequest create_EnableKeyRequest(dafny.DafnySequence<? extends Character> KeyId) {
    return create(KeyId);
  }
  public boolean is_EnableKeyRequest() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_KeyId() {
    return this._KeyId;
  }
}
