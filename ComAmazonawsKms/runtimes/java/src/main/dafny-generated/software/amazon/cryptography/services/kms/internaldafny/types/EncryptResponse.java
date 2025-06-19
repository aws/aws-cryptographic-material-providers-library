// Class EncryptResponse
// Dafny class EncryptResponse compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class EncryptResponse {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _CiphertextBlob;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _KeyId;
  public Wrappers_Compile.Option<EncryptionAlgorithmSpec> _EncryptionAlgorithm;
  public EncryptResponse (Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> CiphertextBlob, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId, Wrappers_Compile.Option<EncryptionAlgorithmSpec> EncryptionAlgorithm) {
    this._CiphertextBlob = CiphertextBlob;
    this._KeyId = KeyId;
    this._EncryptionAlgorithm = EncryptionAlgorithm;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    EncryptResponse o = (EncryptResponse)other;
    return true && java.util.Objects.equals(this._CiphertextBlob, o._CiphertextBlob) && java.util.Objects.equals(this._KeyId, o._KeyId) && java.util.Objects.equals(this._EncryptionAlgorithm, o._EncryptionAlgorithm);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._CiphertextBlob);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._EncryptionAlgorithm);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.EncryptResponse.EncryptResponse");
    s.append("(");
    s.append(dafny.Helpers.toString(this._CiphertextBlob));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._KeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._EncryptionAlgorithm));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<EncryptResponse> _TYPE = dafny.TypeDescriptor.<EncryptResponse>referenceWithInitializer(EncryptResponse.class, () -> EncryptResponse.Default());
  public static dafny.TypeDescriptor<EncryptResponse> _typeDescriptor() {
    return (dafny.TypeDescriptor<EncryptResponse>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final EncryptResponse theDefault = EncryptResponse.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(CiphertextType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(KeyIdType._typeDescriptor()), Wrappers_Compile.Option.<EncryptionAlgorithmSpec>Default(EncryptionAlgorithmSpec._typeDescriptor()));
  public static EncryptResponse Default() {
    return theDefault;
  }
  public static EncryptResponse create(Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> CiphertextBlob, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId, Wrappers_Compile.Option<EncryptionAlgorithmSpec> EncryptionAlgorithm) {
    return new EncryptResponse(CiphertextBlob, KeyId, EncryptionAlgorithm);
  }
  public static EncryptResponse create_EncryptResponse(Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> CiphertextBlob, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId, Wrappers_Compile.Option<EncryptionAlgorithmSpec> EncryptionAlgorithm) {
    return create(CiphertextBlob, KeyId, EncryptionAlgorithm);
  }
  public boolean is_EncryptResponse() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> dtor_CiphertextBlob() {
    return this._CiphertextBlob;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_KeyId() {
    return this._KeyId;
  }
  public Wrappers_Compile.Option<EncryptionAlgorithmSpec> dtor_EncryptionAlgorithm() {
    return this._EncryptionAlgorithm;
  }
}
