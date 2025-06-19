// Class CancelKeyDeletionResponse
// Dafny class CancelKeyDeletionResponse compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class CancelKeyDeletionResponse {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _KeyId;
  public CancelKeyDeletionResponse (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId) {
    this._KeyId = KeyId;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CancelKeyDeletionResponse o = (CancelKeyDeletionResponse)other;
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
    s.append("ComAmazonawsKmsTypes.CancelKeyDeletionResponse.CancelKeyDeletionResponse");
    s.append("(");
    s.append(dafny.Helpers.toString(this._KeyId));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<CancelKeyDeletionResponse> _TYPE = dafny.TypeDescriptor.<CancelKeyDeletionResponse>referenceWithInitializer(CancelKeyDeletionResponse.class, () -> CancelKeyDeletionResponse.Default());
  public static dafny.TypeDescriptor<CancelKeyDeletionResponse> _typeDescriptor() {
    return (dafny.TypeDescriptor<CancelKeyDeletionResponse>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final CancelKeyDeletionResponse theDefault = CancelKeyDeletionResponse.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(KeyIdType._typeDescriptor()));
  public static CancelKeyDeletionResponse Default() {
    return theDefault;
  }
  public static CancelKeyDeletionResponse create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId) {
    return new CancelKeyDeletionResponse(KeyId);
  }
  public static CancelKeyDeletionResponse create_CancelKeyDeletionResponse(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId) {
    return create(KeyId);
  }
  public boolean is_CancelKeyDeletionResponse() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_KeyId() {
    return this._KeyId;
  }
}
