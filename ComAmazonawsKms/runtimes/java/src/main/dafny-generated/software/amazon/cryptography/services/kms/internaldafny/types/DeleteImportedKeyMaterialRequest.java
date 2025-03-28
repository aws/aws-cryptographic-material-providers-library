// Class DeleteImportedKeyMaterialRequest
// Dafny class DeleteImportedKeyMaterialRequest compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class DeleteImportedKeyMaterialRequest {
  public dafny.DafnySequence<? extends Character> _KeyId;
  public DeleteImportedKeyMaterialRequest (dafny.DafnySequence<? extends Character> KeyId) {
    this._KeyId = KeyId;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DeleteImportedKeyMaterialRequest o = (DeleteImportedKeyMaterialRequest)other;
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
    s.append("ComAmazonawsKmsTypes.DeleteImportedKeyMaterialRequest.DeleteImportedKeyMaterialRequest");
    s.append("(");
    s.append(dafny.Helpers.toString(this._KeyId));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DeleteImportedKeyMaterialRequest> _TYPE = dafny.TypeDescriptor.<DeleteImportedKeyMaterialRequest>referenceWithInitializer(DeleteImportedKeyMaterialRequest.class, () -> DeleteImportedKeyMaterialRequest.Default());
  public static dafny.TypeDescriptor<DeleteImportedKeyMaterialRequest> _typeDescriptor() {
    return (dafny.TypeDescriptor<DeleteImportedKeyMaterialRequest>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DeleteImportedKeyMaterialRequest theDefault = software.amazon.cryptography.services.kms.internaldafny.types.DeleteImportedKeyMaterialRequest.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static DeleteImportedKeyMaterialRequest Default() {
    return theDefault;
  }
  public static DeleteImportedKeyMaterialRequest create(dafny.DafnySequence<? extends Character> KeyId) {
    return new DeleteImportedKeyMaterialRequest(KeyId);
  }
  public static DeleteImportedKeyMaterialRequest create_DeleteImportedKeyMaterialRequest(dafny.DafnySequence<? extends Character> KeyId) {
    return create(KeyId);
  }
  public boolean is_DeleteImportedKeyMaterialRequest() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_KeyId() {
    return this._KeyId;
  }
}
