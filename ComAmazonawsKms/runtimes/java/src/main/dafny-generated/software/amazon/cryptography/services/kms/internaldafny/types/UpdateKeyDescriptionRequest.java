// Class UpdateKeyDescriptionRequest
// Dafny class UpdateKeyDescriptionRequest compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class UpdateKeyDescriptionRequest {
  public dafny.DafnySequence<? extends Character> _KeyId;
  public dafny.DafnySequence<? extends Character> _Description;
  public UpdateKeyDescriptionRequest (dafny.DafnySequence<? extends Character> KeyId, dafny.DafnySequence<? extends Character> Description) {
    this._KeyId = KeyId;
    this._Description = Description;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    UpdateKeyDescriptionRequest o = (UpdateKeyDescriptionRequest)other;
    return true && java.util.Objects.equals(this._KeyId, o._KeyId) && java.util.Objects.equals(this._Description, o._Description);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Description);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.UpdateKeyDescriptionRequest.UpdateKeyDescriptionRequest");
    s.append("(");
    s.append(dafny.Helpers.toString(this._KeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Description));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<UpdateKeyDescriptionRequest> _TYPE = dafny.TypeDescriptor.<UpdateKeyDescriptionRequest>referenceWithInitializer(UpdateKeyDescriptionRequest.class, () -> UpdateKeyDescriptionRequest.Default());
  public static dafny.TypeDescriptor<UpdateKeyDescriptionRequest> _typeDescriptor() {
    return (dafny.TypeDescriptor<UpdateKeyDescriptionRequest>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final UpdateKeyDescriptionRequest theDefault = UpdateKeyDescriptionRequest.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static UpdateKeyDescriptionRequest Default() {
    return theDefault;
  }
  public static UpdateKeyDescriptionRequest create(dafny.DafnySequence<? extends Character> KeyId, dafny.DafnySequence<? extends Character> Description) {
    return new UpdateKeyDescriptionRequest(KeyId, Description);
  }
  public static UpdateKeyDescriptionRequest create_UpdateKeyDescriptionRequest(dafny.DafnySequence<? extends Character> KeyId, dafny.DafnySequence<? extends Character> Description) {
    return create(KeyId, Description);
  }
  public boolean is_UpdateKeyDescriptionRequest() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_KeyId() {
    return this._KeyId;
  }
  public dafny.DafnySequence<? extends Character> dtor_Description() {
    return this._Description;
  }
}
