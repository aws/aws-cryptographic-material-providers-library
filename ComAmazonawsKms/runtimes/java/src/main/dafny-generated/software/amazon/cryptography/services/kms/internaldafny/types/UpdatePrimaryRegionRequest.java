// Class UpdatePrimaryRegionRequest
// Dafny class UpdatePrimaryRegionRequest compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class UpdatePrimaryRegionRequest {
  public dafny.DafnySequence<? extends Character> _KeyId;
  public dafny.DafnySequence<? extends Character> _PrimaryRegion;
  public UpdatePrimaryRegionRequest (dafny.DafnySequence<? extends Character> KeyId, dafny.DafnySequence<? extends Character> PrimaryRegion) {
    this._KeyId = KeyId;
    this._PrimaryRegion = PrimaryRegion;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    UpdatePrimaryRegionRequest o = (UpdatePrimaryRegionRequest)other;
    return true && java.util.Objects.equals(this._KeyId, o._KeyId) && java.util.Objects.equals(this._PrimaryRegion, o._PrimaryRegion);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._PrimaryRegion);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.UpdatePrimaryRegionRequest.UpdatePrimaryRegionRequest");
    s.append("(");
    s.append(dafny.Helpers.toString(this._KeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._PrimaryRegion));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<UpdatePrimaryRegionRequest> _TYPE = dafny.TypeDescriptor.<UpdatePrimaryRegionRequest>referenceWithInitializer(UpdatePrimaryRegionRequest.class, () -> UpdatePrimaryRegionRequest.Default());
  public static dafny.TypeDescriptor<UpdatePrimaryRegionRequest> _typeDescriptor() {
    return (dafny.TypeDescriptor<UpdatePrimaryRegionRequest>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final UpdatePrimaryRegionRequest theDefault = software.amazon.cryptography.services.kms.internaldafny.types.UpdatePrimaryRegionRequest.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static UpdatePrimaryRegionRequest Default() {
    return theDefault;
  }
  public static UpdatePrimaryRegionRequest create(dafny.DafnySequence<? extends Character> KeyId, dafny.DafnySequence<? extends Character> PrimaryRegion) {
    return new UpdatePrimaryRegionRequest(KeyId, PrimaryRegion);
  }
  public static UpdatePrimaryRegionRequest create_UpdatePrimaryRegionRequest(dafny.DafnySequence<? extends Character> KeyId, dafny.DafnySequence<? extends Character> PrimaryRegion) {
    return create(KeyId, PrimaryRegion);
  }
  public boolean is_UpdatePrimaryRegionRequest() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_KeyId() {
    return this._KeyId;
  }
  public dafny.DafnySequence<? extends Character> dtor_PrimaryRegion() {
    return this._PrimaryRegion;
  }
}
