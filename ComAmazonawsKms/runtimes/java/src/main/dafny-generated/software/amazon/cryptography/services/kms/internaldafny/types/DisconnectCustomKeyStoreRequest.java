// Class DisconnectCustomKeyStoreRequest
// Dafny class DisconnectCustomKeyStoreRequest compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class DisconnectCustomKeyStoreRequest {
  public dafny.DafnySequence<? extends Character> _CustomKeyStoreId;
  public DisconnectCustomKeyStoreRequest (dafny.DafnySequence<? extends Character> CustomKeyStoreId) {
    this._CustomKeyStoreId = CustomKeyStoreId;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DisconnectCustomKeyStoreRequest o = (DisconnectCustomKeyStoreRequest)other;
    return true && java.util.Objects.equals(this._CustomKeyStoreId, o._CustomKeyStoreId);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._CustomKeyStoreId);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.DisconnectCustomKeyStoreRequest.DisconnectCustomKeyStoreRequest");
    s.append("(");
    s.append(dafny.Helpers.toString(this._CustomKeyStoreId));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DisconnectCustomKeyStoreRequest> _TYPE = dafny.TypeDescriptor.<DisconnectCustomKeyStoreRequest>referenceWithInitializer(DisconnectCustomKeyStoreRequest.class, () -> DisconnectCustomKeyStoreRequest.Default());
  public static dafny.TypeDescriptor<DisconnectCustomKeyStoreRequest> _typeDescriptor() {
    return (dafny.TypeDescriptor<DisconnectCustomKeyStoreRequest>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DisconnectCustomKeyStoreRequest theDefault = DisconnectCustomKeyStoreRequest.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static DisconnectCustomKeyStoreRequest Default() {
    return theDefault;
  }
  public static DisconnectCustomKeyStoreRequest create(dafny.DafnySequence<? extends Character> CustomKeyStoreId) {
    return new DisconnectCustomKeyStoreRequest(CustomKeyStoreId);
  }
  public static DisconnectCustomKeyStoreRequest create_DisconnectCustomKeyStoreRequest(dafny.DafnySequence<? extends Character> CustomKeyStoreId) {
    return create(CustomKeyStoreId);
  }
  public boolean is_DisconnectCustomKeyStoreRequest() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_CustomKeyStoreId() {
    return this._CustomKeyStoreId;
  }
}
