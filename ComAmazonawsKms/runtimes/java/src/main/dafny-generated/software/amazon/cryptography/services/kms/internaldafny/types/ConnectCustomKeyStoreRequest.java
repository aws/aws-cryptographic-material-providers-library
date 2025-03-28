// Class ConnectCustomKeyStoreRequest
// Dafny class ConnectCustomKeyStoreRequest compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class ConnectCustomKeyStoreRequest {
  public dafny.DafnySequence<? extends Character> _CustomKeyStoreId;
  public ConnectCustomKeyStoreRequest (dafny.DafnySequence<? extends Character> CustomKeyStoreId) {
    this._CustomKeyStoreId = CustomKeyStoreId;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ConnectCustomKeyStoreRequest o = (ConnectCustomKeyStoreRequest)other;
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
    s.append("ComAmazonawsKmsTypes.ConnectCustomKeyStoreRequest.ConnectCustomKeyStoreRequest");
    s.append("(");
    s.append(dafny.Helpers.toString(this._CustomKeyStoreId));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ConnectCustomKeyStoreRequest> _TYPE = dafny.TypeDescriptor.<ConnectCustomKeyStoreRequest>referenceWithInitializer(ConnectCustomKeyStoreRequest.class, () -> ConnectCustomKeyStoreRequest.Default());
  public static dafny.TypeDescriptor<ConnectCustomKeyStoreRequest> _typeDescriptor() {
    return (dafny.TypeDescriptor<ConnectCustomKeyStoreRequest>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ConnectCustomKeyStoreRequest theDefault = software.amazon.cryptography.services.kms.internaldafny.types.ConnectCustomKeyStoreRequest.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static ConnectCustomKeyStoreRequest Default() {
    return theDefault;
  }
  public static ConnectCustomKeyStoreRequest create(dafny.DafnySequence<? extends Character> CustomKeyStoreId) {
    return new ConnectCustomKeyStoreRequest(CustomKeyStoreId);
  }
  public static ConnectCustomKeyStoreRequest create_ConnectCustomKeyStoreRequest(dafny.DafnySequence<? extends Character> CustomKeyStoreId) {
    return create(CustomKeyStoreId);
  }
  public boolean is_ConnectCustomKeyStoreRequest() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_CustomKeyStoreId() {
    return this._CustomKeyStoreId;
  }
}
