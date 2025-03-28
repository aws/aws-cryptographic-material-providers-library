// Class GetParametersForImportRequest
// Dafny class GetParametersForImportRequest compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class GetParametersForImportRequest {
  public dafny.DafnySequence<? extends Character> _KeyId;
  public AlgorithmSpec _WrappingAlgorithm;
  public WrappingKeySpec _WrappingKeySpec;
  public GetParametersForImportRequest (dafny.DafnySequence<? extends Character> KeyId, AlgorithmSpec WrappingAlgorithm, WrappingKeySpec WrappingKeySpec) {
    this._KeyId = KeyId;
    this._WrappingAlgorithm = WrappingAlgorithm;
    this._WrappingKeySpec = WrappingKeySpec;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GetParametersForImportRequest o = (GetParametersForImportRequest)other;
    return true && java.util.Objects.equals(this._KeyId, o._KeyId) && java.util.Objects.equals(this._WrappingAlgorithm, o._WrappingAlgorithm) && java.util.Objects.equals(this._WrappingKeySpec, o._WrappingKeySpec);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._WrappingAlgorithm);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._WrappingKeySpec);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.GetParametersForImportRequest.GetParametersForImportRequest");
    s.append("(");
    s.append(dafny.Helpers.toString(this._KeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._WrappingAlgorithm));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._WrappingKeySpec));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<GetParametersForImportRequest> _TYPE = dafny.TypeDescriptor.<GetParametersForImportRequest>referenceWithInitializer(GetParametersForImportRequest.class, () -> GetParametersForImportRequest.Default());
  public static dafny.TypeDescriptor<GetParametersForImportRequest> _typeDescriptor() {
    return (dafny.TypeDescriptor<GetParametersForImportRequest>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GetParametersForImportRequest theDefault = software.amazon.cryptography.services.kms.internaldafny.types.GetParametersForImportRequest.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), AlgorithmSpec.Default(), WrappingKeySpec.Default());
  public static GetParametersForImportRequest Default() {
    return theDefault;
  }
  public static GetParametersForImportRequest create(dafny.DafnySequence<? extends Character> KeyId, AlgorithmSpec WrappingAlgorithm, WrappingKeySpec WrappingKeySpec) {
    return new GetParametersForImportRequest(KeyId, WrappingAlgorithm, WrappingKeySpec);
  }
  public static GetParametersForImportRequest create_GetParametersForImportRequest(dafny.DafnySequence<? extends Character> KeyId, AlgorithmSpec WrappingAlgorithm, WrappingKeySpec WrappingKeySpec) {
    return create(KeyId, WrappingAlgorithm, WrappingKeySpec);
  }
  public boolean is_GetParametersForImportRequest() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_KeyId() {
    return this._KeyId;
  }
  public AlgorithmSpec dtor_WrappingAlgorithm() {
    return this._WrappingAlgorithm;
  }
  public WrappingKeySpec dtor_WrappingKeySpec() {
    return this._WrappingKeySpec;
  }
}
