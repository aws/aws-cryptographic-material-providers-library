// Class GetParametersForImportResponse
// Dafny class GetParametersForImportResponse compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class GetParametersForImportResponse {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _KeyId;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _ImportToken;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _PublicKey;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _ParametersValidTo;
  public GetParametersForImportResponse (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> ImportToken, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> PublicKey, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ParametersValidTo) {
    this._KeyId = KeyId;
    this._ImportToken = ImportToken;
    this._PublicKey = PublicKey;
    this._ParametersValidTo = ParametersValidTo;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GetParametersForImportResponse o = (GetParametersForImportResponse)other;
    return true && java.util.Objects.equals(this._KeyId, o._KeyId) && java.util.Objects.equals(this._ImportToken, o._ImportToken) && java.util.Objects.equals(this._PublicKey, o._PublicKey) && java.util.Objects.equals(this._ParametersValidTo, o._ParametersValidTo);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ImportToken);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._PublicKey);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ParametersValidTo);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.GetParametersForImportResponse.GetParametersForImportResponse");
    s.append("(");
    s.append(dafny.Helpers.toString(this._KeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ImportToken));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._PublicKey));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ParametersValidTo));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<GetParametersForImportResponse> _TYPE = dafny.TypeDescriptor.<GetParametersForImportResponse>referenceWithInitializer(GetParametersForImportResponse.class, () -> GetParametersForImportResponse.Default());
  public static dafny.TypeDescriptor<GetParametersForImportResponse> _typeDescriptor() {
    return (dafny.TypeDescriptor<GetParametersForImportResponse>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GetParametersForImportResponse theDefault = GetParametersForImportResponse.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(KeyIdType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(CiphertextType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(PlaintextType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)));
  public static GetParametersForImportResponse Default() {
    return theDefault;
  }
  public static GetParametersForImportResponse create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> ImportToken, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> PublicKey, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ParametersValidTo) {
    return new GetParametersForImportResponse(KeyId, ImportToken, PublicKey, ParametersValidTo);
  }
  public static GetParametersForImportResponse create_GetParametersForImportResponse(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> ImportToken, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> PublicKey, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ParametersValidTo) {
    return create(KeyId, ImportToken, PublicKey, ParametersValidTo);
  }
  public boolean is_GetParametersForImportResponse() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_KeyId() {
    return this._KeyId;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> dtor_ImportToken() {
    return this._ImportToken;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> dtor_PublicKey() {
    return this._PublicKey;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_ParametersValidTo() {
    return this._ParametersValidTo;
  }
}
