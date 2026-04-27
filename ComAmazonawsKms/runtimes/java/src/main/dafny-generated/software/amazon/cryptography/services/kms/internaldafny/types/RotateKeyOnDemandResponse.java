// Class RotateKeyOnDemandResponse
// Dafny class RotateKeyOnDemandResponse compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class RotateKeyOnDemandResponse {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _KeyId;
  public RotateKeyOnDemandResponse (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId) {
    this._KeyId = KeyId;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    RotateKeyOnDemandResponse o = (RotateKeyOnDemandResponse)other;
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
    s.append("ComAmazonawsKmsTypes.RotateKeyOnDemandResponse.RotateKeyOnDemandResponse");
    s.append("(");
    s.append(dafny.Helpers.toString(this._KeyId));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<RotateKeyOnDemandResponse> _TYPE = dafny.TypeDescriptor.<RotateKeyOnDemandResponse>referenceWithInitializer(RotateKeyOnDemandResponse.class, () -> RotateKeyOnDemandResponse.Default());
  public static dafny.TypeDescriptor<RotateKeyOnDemandResponse> _typeDescriptor() {
    return (dafny.TypeDescriptor<RotateKeyOnDemandResponse>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final RotateKeyOnDemandResponse theDefault = RotateKeyOnDemandResponse.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(KeyIdType._typeDescriptor()));
  public static RotateKeyOnDemandResponse Default() {
    return theDefault;
  }
  public static RotateKeyOnDemandResponse create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId) {
    return new RotateKeyOnDemandResponse(KeyId);
  }
  public static RotateKeyOnDemandResponse create_RotateKeyOnDemandResponse(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId) {
    return create(KeyId);
  }
  public boolean is_RotateKeyOnDemandResponse() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_KeyId() {
    return this._KeyId;
  }
}
