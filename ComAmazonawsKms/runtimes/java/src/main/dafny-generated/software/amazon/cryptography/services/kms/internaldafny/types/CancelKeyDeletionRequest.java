// Class CancelKeyDeletionRequest
// Dafny class CancelKeyDeletionRequest compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class CancelKeyDeletionRequest {
  public dafny.DafnySequence<? extends Character> _KeyId;
  public CancelKeyDeletionRequest (dafny.DafnySequence<? extends Character> KeyId) {
    this._KeyId = KeyId;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CancelKeyDeletionRequest o = (CancelKeyDeletionRequest)other;
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
    s.append("ComAmazonawsKmsTypes.CancelKeyDeletionRequest.CancelKeyDeletionRequest");
    s.append("(");
    s.append(dafny.Helpers.toString(this._KeyId));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<CancelKeyDeletionRequest> _TYPE = dafny.TypeDescriptor.<CancelKeyDeletionRequest>referenceWithInitializer(CancelKeyDeletionRequest.class, () -> CancelKeyDeletionRequest.Default());
  public static dafny.TypeDescriptor<CancelKeyDeletionRequest> _typeDescriptor() {
    return (dafny.TypeDescriptor<CancelKeyDeletionRequest>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final CancelKeyDeletionRequest theDefault = CancelKeyDeletionRequest.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static CancelKeyDeletionRequest Default() {
    return theDefault;
  }
  public static CancelKeyDeletionRequest create(dafny.DafnySequence<? extends Character> KeyId) {
    return new CancelKeyDeletionRequest(KeyId);
  }
  public static CancelKeyDeletionRequest create_CancelKeyDeletionRequest(dafny.DafnySequence<? extends Character> KeyId) {
    return create(KeyId);
  }
  public boolean is_CancelKeyDeletionRequest() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_KeyId() {
    return this._KeyId;
  }
}
