// Class DecryptResponse
// Dafny class DecryptResponse compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class DecryptResponse {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _KeyId;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _Plaintext;
  public Wrappers_Compile.Option<EncryptionAlgorithmSpec> _EncryptionAlgorithm;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _CiphertextForRecipient;
  public DecryptResponse (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> Plaintext, Wrappers_Compile.Option<EncryptionAlgorithmSpec> EncryptionAlgorithm, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> CiphertextForRecipient) {
    this._KeyId = KeyId;
    this._Plaintext = Plaintext;
    this._EncryptionAlgorithm = EncryptionAlgorithm;
    this._CiphertextForRecipient = CiphertextForRecipient;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    DecryptResponse o = (DecryptResponse)other;
    return true && java.util.Objects.equals(this._KeyId, o._KeyId) && java.util.Objects.equals(this._Plaintext, o._Plaintext) && java.util.Objects.equals(this._EncryptionAlgorithm, o._EncryptionAlgorithm) && java.util.Objects.equals(this._CiphertextForRecipient, o._CiphertextForRecipient);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Plaintext);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._EncryptionAlgorithm);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._CiphertextForRecipient);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.DecryptResponse.DecryptResponse");
    s.append("(");
    s.append(dafny.Helpers.toString(this._KeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Plaintext));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._EncryptionAlgorithm));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._CiphertextForRecipient));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<DecryptResponse> _TYPE = dafny.TypeDescriptor.<DecryptResponse>referenceWithInitializer(DecryptResponse.class, () -> DecryptResponse.Default());
  public static dafny.TypeDescriptor<DecryptResponse> _typeDescriptor() {
    return (dafny.TypeDescriptor<DecryptResponse>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final DecryptResponse theDefault = software.amazon.cryptography.services.kms.internaldafny.types.DecryptResponse.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(KeyIdType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(PlaintextType._typeDescriptor()), Wrappers_Compile.Option.<EncryptionAlgorithmSpec>Default(EncryptionAlgorithmSpec._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(CiphertextType._typeDescriptor()));
  public static DecryptResponse Default() {
    return theDefault;
  }
  public static DecryptResponse create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> Plaintext, Wrappers_Compile.Option<EncryptionAlgorithmSpec> EncryptionAlgorithm, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> CiphertextForRecipient) {
    return new DecryptResponse(KeyId, Plaintext, EncryptionAlgorithm, CiphertextForRecipient);
  }
  public static DecryptResponse create_DecryptResponse(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> Plaintext, Wrappers_Compile.Option<EncryptionAlgorithmSpec> EncryptionAlgorithm, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> CiphertextForRecipient) {
    return create(KeyId, Plaintext, EncryptionAlgorithm, CiphertextForRecipient);
  }
  public boolean is_DecryptResponse() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_KeyId() {
    return this._KeyId;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> dtor_Plaintext() {
    return this._Plaintext;
  }
  public Wrappers_Compile.Option<EncryptionAlgorithmSpec> dtor_EncryptionAlgorithm() {
    return this._EncryptionAlgorithm;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> dtor_CiphertextForRecipient() {
    return this._CiphertextForRecipient;
  }
}
