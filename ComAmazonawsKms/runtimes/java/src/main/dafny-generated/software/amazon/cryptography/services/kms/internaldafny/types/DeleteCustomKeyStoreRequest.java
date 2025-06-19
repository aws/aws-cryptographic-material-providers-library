// Class DeleteCustomKeyStoreRequest
// Dafny class DeleteCustomKeyStoreRequest compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class DeleteCustomKeyStoreRequest {
  public dafny.DafnySequence<? extends Character> _CustomKeyStoreId;
  public DeleteCustomKeyStoreRequest (dafny.DafnySequence<? extends Character> CustomKeyStoreId) {
    this._CustomKeyStoreId = CustomKeyStoreId;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DeleteCustomKeyStoreRequest o = (DeleteCustomKeyStoreRequest)other;
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
    s.append("ComAmazonawsKmsTypes.DeleteCustomKeyStoreRequest.DeleteCustomKeyStoreRequest");
    s.append("(");
    s.append(dafny.Helpers.toString(this._CustomKeyStoreId));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DeleteCustomKeyStoreRequest> _TYPE = dafny.TypeDescriptor.<DeleteCustomKeyStoreRequest>referenceWithInitializer(DeleteCustomKeyStoreRequest.class, () -> DeleteCustomKeyStoreRequest.Default());
  public static dafny.TypeDescriptor<DeleteCustomKeyStoreRequest> _typeDescriptor() {
    return (dafny.TypeDescriptor<DeleteCustomKeyStoreRequest>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DeleteCustomKeyStoreRequest theDefault = DeleteCustomKeyStoreRequest.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static DeleteCustomKeyStoreRequest Default() {
    return theDefault;
  }
  public static DeleteCustomKeyStoreRequest create(dafny.DafnySequence<? extends Character> CustomKeyStoreId) {
    return new DeleteCustomKeyStoreRequest(CustomKeyStoreId);
  }
  public static DeleteCustomKeyStoreRequest create_DeleteCustomKeyStoreRequest(dafny.DafnySequence<? extends Character> CustomKeyStoreId) {
    return create(CustomKeyStoreId);
  }
  public boolean is_DeleteCustomKeyStoreRequest() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_CustomKeyStoreId() {
    return this._CustomKeyStoreId;
  }
}
