// Class GenerateDataKeyPairWithoutPlaintextResponse
// Dafny class GenerateDataKeyPairWithoutPlaintextResponse compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;


@SuppressWarnings({"unchecked", "deprecation"})
public class GenerateDataKeyPairWithoutPlaintextResponse {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _PrivateKeyCiphertextBlob;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _PublicKey;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _KeyId;
  public Wrappers_Compile.Option<DataKeyPairSpec> _KeyPairSpec;
  public GenerateDataKeyPairWithoutPlaintextResponse (Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> PrivateKeyCiphertextBlob, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> PublicKey, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId, Wrappers_Compile.Option<DataKeyPairSpec> KeyPairSpec) {
    this._PrivateKeyCiphertextBlob = PrivateKeyCiphertextBlob;
    this._PublicKey = PublicKey;
    this._KeyId = KeyId;
    this._KeyPairSpec = KeyPairSpec;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    GenerateDataKeyPairWithoutPlaintextResponse o = (GenerateDataKeyPairWithoutPlaintextResponse)other;
    return true && java.util.Objects.equals(this._PrivateKeyCiphertextBlob, o._PrivateKeyCiphertextBlob) && java.util.Objects.equals(this._PublicKey, o._PublicKey) && java.util.Objects.equals(this._KeyId, o._KeyId) && java.util.Objects.equals(this._KeyPairSpec, o._KeyPairSpec);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._PrivateKeyCiphertextBlob);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._PublicKey);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyPairSpec);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.GenerateDataKeyPairWithoutPlaintextResponse.GenerateDataKeyPairWithoutPlaintextResponse");
    s.append("(");
    s.append(dafny.Helpers.toString(this._PrivateKeyCiphertextBlob));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._PublicKey));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._KeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._KeyPairSpec));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<GenerateDataKeyPairWithoutPlaintextResponse> _TYPE = dafny.TypeDescriptor.<GenerateDataKeyPairWithoutPlaintextResponse>referenceWithInitializer(GenerateDataKeyPairWithoutPlaintextResponse.class, () -> GenerateDataKeyPairWithoutPlaintextResponse.Default());
  public static dafny.TypeDescriptor<GenerateDataKeyPairWithoutPlaintextResponse> _typeDescriptor() {
    return (dafny.TypeDescriptor<GenerateDataKeyPairWithoutPlaintextResponse>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final GenerateDataKeyPairWithoutPlaintextResponse theDefault = software.amazon.cryptography.services.kms.internaldafny.types.GenerateDataKeyPairWithoutPlaintextResponse.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(CiphertextType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(PublicKeyType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(KeyIdType._typeDescriptor()), Wrappers_Compile.Option.<DataKeyPairSpec>Default(DataKeyPairSpec._typeDescriptor()));
  public static GenerateDataKeyPairWithoutPlaintextResponse Default() {
    return theDefault;
  }
  public static GenerateDataKeyPairWithoutPlaintextResponse create(Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> PrivateKeyCiphertextBlob, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> PublicKey, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId, Wrappers_Compile.Option<DataKeyPairSpec> KeyPairSpec) {
    return new GenerateDataKeyPairWithoutPlaintextResponse(PrivateKeyCiphertextBlob, PublicKey, KeyId, KeyPairSpec);
  }
  public static GenerateDataKeyPairWithoutPlaintextResponse create_GenerateDataKeyPairWithoutPlaintextResponse(Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> PrivateKeyCiphertextBlob, Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> PublicKey, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> KeyId, Wrappers_Compile.Option<DataKeyPairSpec> KeyPairSpec) {
    return create(PrivateKeyCiphertextBlob, PublicKey, KeyId, KeyPairSpec);
  }
  public boolean is_GenerateDataKeyPairWithoutPlaintextResponse() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> dtor_PrivateKeyCiphertextBlob() {
    return this._PrivateKeyCiphertextBlob;
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
}
