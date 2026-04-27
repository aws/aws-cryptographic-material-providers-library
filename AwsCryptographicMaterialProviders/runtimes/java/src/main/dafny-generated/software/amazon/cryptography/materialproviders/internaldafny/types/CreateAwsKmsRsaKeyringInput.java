// Class CreateAwsKmsRsaKeyringInput
// Dafny class CreateAwsKmsRsaKeyringInput compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class CreateAwsKmsRsaKeyringInput {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> _publicKey;
  public dafny.DafnySequence<? extends Character> _kmsKeyId;
  public software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec _encryptionAlgorithm;
  public Wrappers_Compile.Option<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient> _kmsClient;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> _grantTokens;
  public CreateAwsKmsRsaKeyringInput (Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> publicKey, dafny.DafnySequence<? extends Character> kmsKeyId, software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec encryptionAlgorithm, Wrappers_Compile.Option<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient> kmsClient, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> grantTokens) {
    this._publicKey = publicKey;
    this._kmsKeyId = kmsKeyId;
    this._encryptionAlgorithm = encryptionAlgorithm;
    this._kmsClient = kmsClient;
    this._grantTokens = grantTokens;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CreateAwsKmsRsaKeyringInput o = (CreateAwsKmsRsaKeyringInput)other;
    return true && java.util.Objects.equals(this._publicKey, o._publicKey) && java.util.Objects.equals(this._kmsKeyId, o._kmsKeyId) && java.util.Objects.equals(this._encryptionAlgorithm, o._encryptionAlgorithm) && java.util.Objects.equals(this._kmsClient, o._kmsClient) && java.util.Objects.equals(this._grantTokens, o._grantTokens);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._publicKey);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._kmsKeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._encryptionAlgorithm);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._kmsClient);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._grantTokens);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.CreateAwsKmsRsaKeyringInput.CreateAwsKmsRsaKeyringInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._publicKey));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._kmsKeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._encryptionAlgorithm));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._kmsClient));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._grantTokens));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<CreateAwsKmsRsaKeyringInput> _TYPE = dafny.TypeDescriptor.<CreateAwsKmsRsaKeyringInput>referenceWithInitializer(CreateAwsKmsRsaKeyringInput.class, () -> CreateAwsKmsRsaKeyringInput.Default());
  public static dafny.TypeDescriptor<CreateAwsKmsRsaKeyringInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<CreateAwsKmsRsaKeyringInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final CreateAwsKmsRsaKeyringInput theDefault = CreateAwsKmsRsaKeyringInput.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends java.lang.Byte>>Default(dafny.DafnySequence.<java.lang.Byte>_typeDescriptor(BoundedInts_Compile.uint8._typeDescriptor())), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec.Default(), Wrappers_Compile.Option.<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>Default(((dafny.TypeDescriptor<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient>)(java.lang.Object)dafny.TypeDescriptor.reference(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient.class))), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>Default(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))));
  public static CreateAwsKmsRsaKeyringInput Default() {
    return theDefault;
  }
  public static CreateAwsKmsRsaKeyringInput create(Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> publicKey, dafny.DafnySequence<? extends Character> kmsKeyId, software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec encryptionAlgorithm, Wrappers_Compile.Option<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient> kmsClient, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> grantTokens) {
    return new CreateAwsKmsRsaKeyringInput(publicKey, kmsKeyId, encryptionAlgorithm, kmsClient, grantTokens);
  }
  public static CreateAwsKmsRsaKeyringInput create_CreateAwsKmsRsaKeyringInput(Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> publicKey, dafny.DafnySequence<? extends Character> kmsKeyId, software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec encryptionAlgorithm, Wrappers_Compile.Option<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient> kmsClient, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> grantTokens) {
    return create(publicKey, kmsKeyId, encryptionAlgorithm, kmsClient, grantTokens);
  }
  public boolean is_CreateAwsKmsRsaKeyringInput() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends java.lang.Byte>> dtor_publicKey() {
    return this._publicKey;
  }
  public dafny.DafnySequence<? extends Character> dtor_kmsKeyId() {
    return this._kmsKeyId;
  }
  public software.amazon.cryptography.services.kms.internaldafny.types.EncryptionAlgorithmSpec dtor_encryptionAlgorithm() {
    return this._encryptionAlgorithm;
  }
  public Wrappers_Compile.Option<software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient> dtor_kmsClient() {
    return this._kmsClient;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> dtor_grantTokens() {
    return this._grantTokens;
  }
}
