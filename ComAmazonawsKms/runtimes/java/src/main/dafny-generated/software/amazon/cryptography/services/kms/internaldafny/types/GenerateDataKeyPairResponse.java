// Class GenerateDataKeyPairResponse
// Dafny class GenerateDataKeyPairResponse compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class GenerateDataKeyPairResponse {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _PrivateKeyCiphertextBlob;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _PrivateKeyPlaintext;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _PublicKey;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _KeyId;
  public Wrappers_Compile.Option<DataKeyPairSpec> _KeyPairSpec;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _CiphertextForRecipient;
  public GenerateDataKeyPairResponse (Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> PrivateKeyCiphertextBlob, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> PrivateKeyPlaintext, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> PublicKey, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId, Wrappers_Compile.Option<DataKeyPairSpec> KeyPairSpec, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> CiphertextForRecipient) {
    this._PrivateKeyCiphertextBlob = PrivateKeyCiphertextBlob;
    this._PrivateKeyPlaintext = PrivateKeyPlaintext;
    this._PublicKey = PublicKey;
    this._KeyId = KeyId;
    this._KeyPairSpec = KeyPairSpec;
    this._CiphertextForRecipient = CiphertextForRecipient;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GenerateDataKeyPairResponse o = (GenerateDataKeyPairResponse)other;
    return true && java.util.Objects.equals(this._PrivateKeyCiphertextBlob, o._PrivateKeyCiphertextBlob) && java.util.Objects.equals(this._PrivateKeyPlaintext, o._PrivateKeyPlaintext) && java.util.Objects.equals(this._PublicKey, o._PublicKey) && java.util.Objects.equals(this._KeyId, o._KeyId) && java.util.Objects.equals(this._KeyPairSpec, o._KeyPairSpec) && java.util.Objects.equals(this._CiphertextForRecipient, o._CiphertextForRecipient);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._PrivateKeyCiphertextBlob);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._PrivateKeyPlaintext);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._PublicKey);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyPairSpec);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._CiphertextForRecipient);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.GenerateDataKeyPairResponse.GenerateDataKeyPairResponse");
    s.append("(");
    s.append(dafny.Helpers.toString(this._PrivateKeyCiphertextBlob));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._PrivateKeyPlaintext));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._PublicKey));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._KeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._KeyPairSpec));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._CiphertextForRecipient));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<GenerateDataKeyPairResponse> _TYPE = dafny.TypeDescriptor.<GenerateDataKeyPairResponse>referenceWithInitializer(GenerateDataKeyPairResponse.class, () -> GenerateDataKeyPairResponse.Default());
  public static dafny.TypeDescriptor<GenerateDataKeyPairResponse> _typeDescriptor() {
    return (dafny.TypeDescriptor<GenerateDataKeyPairResponse>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GenerateDataKeyPairResponse theDefault = GenerateDataKeyPairResponse.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(CiphertextType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(PlaintextType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(PublicKeyType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(KeyIdType._typeDescriptor()), Wrappers_Compile.Option.<DataKeyPairSpec>Default(DataKeyPairSpec._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(CiphertextType._typeDescriptor()));
  public static GenerateDataKeyPairResponse Default() {
    return theDefault;
  }
  public static GenerateDataKeyPairResponse create(Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> PrivateKeyCiphertextBlob, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> PrivateKeyPlaintext, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> PublicKey, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId, Wrappers_Compile.Option<DataKeyPairSpec> KeyPairSpec, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> CiphertextForRecipient) {
    return new GenerateDataKeyPairResponse(PrivateKeyCiphertextBlob, PrivateKeyPlaintext, PublicKey, KeyId, KeyPairSpec, CiphertextForRecipient);
  }
  public static GenerateDataKeyPairResponse create_GenerateDataKeyPairResponse(Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> PrivateKeyCiphertextBlob, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> PrivateKeyPlaintext, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> PublicKey, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId, Wrappers_Compile.Option<DataKeyPairSpec> KeyPairSpec, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> CiphertextForRecipient) {
    return create(PrivateKeyCiphertextBlob, PrivateKeyPlaintext, PublicKey, KeyId, KeyPairSpec, CiphertextForRecipient);
  }
  public boolean is_GenerateDataKeyPairResponse() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> dtor_PrivateKeyCiphertextBlob() {
    return this._PrivateKeyCiphertextBlob;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> dtor_PrivateKeyPlaintext() {
    return this._PrivateKeyPlaintext;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> dtor_PublicKey() {
    return this._PublicKey;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_KeyId() {
    return this._KeyId;
  }
  public Wrappers_Compile.Option<DataKeyPairSpec> dtor_KeyPairSpec() {
    return this._KeyPairSpec;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> dtor_CiphertextForRecipient() {
    return this._CiphertextForRecipient;
  }
}
