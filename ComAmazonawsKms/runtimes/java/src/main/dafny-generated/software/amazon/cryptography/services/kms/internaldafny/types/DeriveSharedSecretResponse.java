// Class DeriveSharedSecretResponse
// Dafny class DeriveSharedSecretResponse compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class DeriveSharedSecretResponse {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _KeyId;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _SharedSecret;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _CiphertextForRecipient;
  public Wrappers_Compile.Option<KeyAgreementAlgorithmSpec> _KeyAgreementAlgorithm;
  public Wrappers_Compile.Option<OriginType> _KeyOrigin;
  public DeriveSharedSecretResponse (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> SharedSecret, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> CiphertextForRecipient, Wrappers_Compile.Option<KeyAgreementAlgorithmSpec> KeyAgreementAlgorithm, Wrappers_Compile.Option<OriginType> KeyOrigin) {
    this._KeyId = KeyId;
    this._SharedSecret = SharedSecret;
    this._CiphertextForRecipient = CiphertextForRecipient;
    this._KeyAgreementAlgorithm = KeyAgreementAlgorithm;
    this._KeyOrigin = KeyOrigin;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DeriveSharedSecretResponse o = (DeriveSharedSecretResponse)other;
    return true && java.util.Objects.equals(this._KeyId, o._KeyId) && java.util.Objects.equals(this._SharedSecret, o._SharedSecret) && java.util.Objects.equals(this._CiphertextForRecipient, o._CiphertextForRecipient) && java.util.Objects.equals(this._KeyAgreementAlgorithm, o._KeyAgreementAlgorithm) && java.util.Objects.equals(this._KeyOrigin, o._KeyOrigin);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._SharedSecret);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._CiphertextForRecipient);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyAgreementAlgorithm);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyOrigin);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.DeriveSharedSecretResponse.DeriveSharedSecretResponse");
    s.append("(");
    s.append(dafny.Helpers.toString(this._KeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._SharedSecret));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._CiphertextForRecipient));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._KeyAgreementAlgorithm));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._KeyOrigin));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DeriveSharedSecretResponse> _TYPE = dafny.TypeDescriptor.<DeriveSharedSecretResponse>referenceWithInitializer(DeriveSharedSecretResponse.class, () -> DeriveSharedSecretResponse.Default());
  public static dafny.TypeDescriptor<DeriveSharedSecretResponse> _typeDescriptor() {
    return (dafny.TypeDescriptor<DeriveSharedSecretResponse>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DeriveSharedSecretResponse theDefault = DeriveSharedSecretResponse.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(KeyIdType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(PlaintextType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(CiphertextType._typeDescriptor()), Wrappers_Compile.Option.<KeyAgreementAlgorithmSpec>Default(KeyAgreementAlgorithmSpec._typeDescriptor()), Wrappers_Compile.Option.<OriginType>Default(OriginType._typeDescriptor()));
  public static DeriveSharedSecretResponse Default() {
    return theDefault;
  }
  public static DeriveSharedSecretResponse create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> SharedSecret, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> CiphertextForRecipient, Wrappers_Compile.Option<KeyAgreementAlgorithmSpec> KeyAgreementAlgorithm, Wrappers_Compile.Option<OriginType> KeyOrigin) {
    return new DeriveSharedSecretResponse(KeyId, SharedSecret, CiphertextForRecipient, KeyAgreementAlgorithm, KeyOrigin);
  }
  public static DeriveSharedSecretResponse create_DeriveSharedSecretResponse(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> SharedSecret, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> CiphertextForRecipient, Wrappers_Compile.Option<KeyAgreementAlgorithmSpec> KeyAgreementAlgorithm, Wrappers_Compile.Option<OriginType> KeyOrigin) {
    return create(KeyId, SharedSecret, CiphertextForRecipient, KeyAgreementAlgorithm, KeyOrigin);
  }
  public boolean is_DeriveSharedSecretResponse() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_KeyId() {
    return this._KeyId;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> dtor_SharedSecret() {
    return this._SharedSecret;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> dtor_CiphertextForRecipient() {
    return this._CiphertextForRecipient;
  }
  public Wrappers_Compile.Option<KeyAgreementAlgorithmSpec> dtor_KeyAgreementAlgorithm() {
    return this._KeyAgreementAlgorithm;
  }
  public Wrappers_Compile.Option<OriginType> dtor_KeyOrigin() {
    return this._KeyOrigin;
  }
}
