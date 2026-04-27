// Class DeleteAliasRequest
// Dafny class DeleteAliasRequest compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class DeleteAliasRequest {
  public dafny.DafnySequence<? extends Character> _AliasName;
  public DeleteAliasRequest (dafny.DafnySequence<? extends Character> AliasName) {
    this._AliasName = AliasName;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DeleteAliasRequest o = (DeleteAliasRequest)other;
    return true && java.util.Objects.equals(this._AliasName, o._AliasName);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._AliasName);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.DeleteAliasRequest.DeleteAliasRequest");
    s.append("(");
    s.append(dafny.Helpers.toString(this._AliasName));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DeleteAliasRequest> _TYPE = dafny.TypeDescriptor.<DeleteAliasRequest>referenceWithInitializer(DeleteAliasRequest.class, () -> DeleteAliasRequest.Default());
  public static dafny.TypeDescriptor<DeleteAliasRequest> _typeDescriptor() {
    return (dafny.TypeDescriptor<DeleteAliasRequest>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DeleteAliasRequest theDefault = DeleteAliasRequest.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static DeleteAliasRequest Default() {
    return theDefault;
  }
  public static DeleteAliasRequest create(dafny.DafnySequence<? extends Character> AliasName) {
    return new DeleteAliasRequest(AliasName);
  }
  public static DeleteAliasRequest create_DeleteAliasRequest(dafny.DafnySequence<? extends Character> AliasName) {
    return create(AliasName);
  }
  public boolean is_DeleteAliasRequest() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_AliasName() {
    return this._AliasName;
  }
}
