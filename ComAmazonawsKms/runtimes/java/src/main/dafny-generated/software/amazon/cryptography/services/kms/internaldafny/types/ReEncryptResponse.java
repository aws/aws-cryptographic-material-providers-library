// Class ReEncryptResponse
// Dafny class ReEncryptResponse compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class ReEncryptResponse {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _CiphertextBlob;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _SourceKeyId;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _KeyId;
  public Wrappers_Compile.Option<EncryptionAlgorithmSpec> _SourceEncryptionAlgorithm;
  public Wrappers_Compile.Option<EncryptionAlgorithmSpec> _DestinationEncryptionAlgorithm;
  public ReEncryptResponse (Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> CiphertextBlob, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> SourceKeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId, Wrappers_Compile.Option<EncryptionAlgorithmSpec> SourceEncryptionAlgorithm, Wrappers_Compile.Option<EncryptionAlgorithmSpec> DestinationEncryptionAlgorithm) {
    this._CiphertextBlob = CiphertextBlob;
    this._SourceKeyId = SourceKeyId;
    this._KeyId = KeyId;
    this._SourceEncryptionAlgorithm = SourceEncryptionAlgorithm;
    this._DestinationEncryptionAlgorithm = DestinationEncryptionAlgorithm;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    ReEncryptResponse o = (ReEncryptResponse)other;
    return true && java.util.Objects.equals(this._CiphertextBlob, o._CiphertextBlob) && java.util.Objects.equals(this._SourceKeyId, o._SourceKeyId) && java.util.Objects.equals(this._KeyId, o._KeyId) && java.util.Objects.equals(this._SourceEncryptionAlgorithm, o._SourceEncryptionAlgorithm) && java.util.Objects.equals(this._DestinationEncryptionAlgorithm, o._DestinationEncryptionAlgorithm);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._CiphertextBlob);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._SourceKeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._SourceEncryptionAlgorithm);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._DestinationEncryptionAlgorithm);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.ReEncryptResponse.ReEncryptResponse");
    s.append("(");
    s.append(dafny.Helpers.toString(this._CiphertextBlob));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._SourceKeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._KeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._SourceEncryptionAlgorithm));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._DestinationEncryptionAlgorithm));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<ReEncryptResponse> _TYPE = dafny.TypeDescriptor.<ReEncryptResponse>referenceWithInitializer(ReEncryptResponse.class, () -> ReEncryptResponse.Default());
  public static dafny.TypeDescriptor<ReEncryptResponse> _typeDescriptor() {
    return (dafny.TypeDescriptor<ReEncryptResponse>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final ReEncryptResponse theDefault = ReEncryptResponse.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(CiphertextType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(KeyIdType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(KeyIdType._typeDescriptor()), Wrappers_Compile.Option.<EncryptionAlgorithmSpec>Default(EncryptionAlgorithmSpec._typeDescriptor()), Wrappers_Compile.Option.<EncryptionAlgorithmSpec>Default(EncryptionAlgorithmSpec._typeDescriptor()));
  public static ReEncryptResponse Default() {
    return theDefault;
  }
  public static ReEncryptResponse create(Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> CiphertextBlob, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> SourceKeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId, Wrappers_Compile.Option<EncryptionAlgorithmSpec> SourceEncryptionAlgorithm, Wrappers_Compile.Option<EncryptionAlgorithmSpec> DestinationEncryptionAlgorithm) {
    return new ReEncryptResponse(CiphertextBlob, SourceKeyId, KeyId, SourceEncryptionAlgorithm, DestinationEncryptionAlgorithm);
  }
  public static ReEncryptResponse create_ReEncryptResponse(Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> CiphertextBlob, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> SourceKeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId, Wrappers_Compile.Option<EncryptionAlgorithmSpec> SourceEncryptionAlgorithm, Wrappers_Compile.Option<EncryptionAlgorithmSpec> DestinationEncryptionAlgorithm) {
    return create(CiphertextBlob, SourceKeyId, KeyId, SourceEncryptionAlgorithm, DestinationEncryptionAlgorithm);
  }
  public boolean is_ReEncryptResponse() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> dtor_CiphertextBlob() {
    return this._CiphertextBlob;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_SourceKeyId() {
    return this._SourceKeyId;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_KeyId() {
    return this._KeyId;
  }
  public Wrappers_Compile.Option<EncryptionAlgorithmSpec> dtor_SourceEncryptionAlgorithm() {
    return this._SourceEncryptionAlgorithm;
  }
  public Wrappers_Compile.Option<EncryptionAlgorithmSpec> dtor_DestinationEncryptionAlgorithm() {
    return this._DestinationEncryptionAlgorithm;
  }
}
