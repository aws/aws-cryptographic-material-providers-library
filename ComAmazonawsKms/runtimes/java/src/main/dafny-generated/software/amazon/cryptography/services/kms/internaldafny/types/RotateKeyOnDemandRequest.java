// Class RotateKeyOnDemandRequest
// Dafny class RotateKeyOnDemandRequest compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class RotateKeyOnDemandRequest {
  public dafny.DafnySequence<? extends Character> _KeyId;
  public RotateKeyOnDemandRequest (dafny.DafnySequence<? extends Character> KeyId) {
    this._KeyId = KeyId;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    RotateKeyOnDemandRequest o = (RotateKeyOnDemandRequest)other;
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
    s.append("ComAmazonawsKmsTypes.RotateKeyOnDemandRequest.RotateKeyOnDemandRequest");
    s.append("(");
    s.append(dafny.Helpers.toString(this._KeyId));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<RotateKeyOnDemandRequest> _TYPE = dafny.TypeDescriptor.<RotateKeyOnDemandRequest>referenceWithInitializer(RotateKeyOnDemandRequest.class, () -> RotateKeyOnDemandRequest.Default());
  public static dafny.TypeDescriptor<RotateKeyOnDemandRequest> _typeDescriptor() {
    return (dafny.TypeDescriptor<RotateKeyOnDemandRequest>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final RotateKeyOnDemandRequest theDefault = RotateKeyOnDemandRequest.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static RotateKeyOnDemandRequest Default() {
    return theDefault;
  }
  public static RotateKeyOnDemandRequest create(dafny.DafnySequence<? extends Character> KeyId) {
    return new RotateKeyOnDemandRequest(KeyId);
  }
  public static RotateKeyOnDemandRequest create_RotateKeyOnDemandRequest(dafny.DafnySequence<? extends Character> KeyId) {
    return create(KeyId);
  }
  public boolean is_RotateKeyOnDemandRequest() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_KeyId() {
    return this._KeyId;
  }
}
