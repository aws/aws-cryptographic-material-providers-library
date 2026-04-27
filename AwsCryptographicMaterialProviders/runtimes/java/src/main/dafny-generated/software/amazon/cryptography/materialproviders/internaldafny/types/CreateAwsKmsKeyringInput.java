// Class CreateAwsKmsKeyringInput
// Dafny class CreateAwsKmsKeyringInput compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class CreateAwsKmsKeyringInput {
  public dafny.DafnySequence<? extends Character> _kmsKeyId;
  public software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _kmsClient;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> _grantTokens;
  public CreateAwsKmsKeyringInput (dafny.DafnySequence<? extends Character> kmsKeyId, software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient kmsClient, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> grantTokens) {
    this._kmsKeyId = kmsKeyId;
    this._kmsClient = kmsClient;
    this._grantTokens = grantTokens;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CreateAwsKmsKeyringInput o = (CreateAwsKmsKeyringInput)other;
    return true && java.util.Objects.equals(this._kmsKeyId, o._kmsKeyId) && this._kmsClient == o._kmsClient && java.util.Objects.equals(this._grantTokens, o._grantTokens);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._kmsKeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._kmsClient);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._grantTokens);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.CreateAwsKmsKeyringInput.CreateAwsKmsKeyringInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._kmsKeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._kmsClient));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._grantTokens));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<CreateAwsKmsKeyringInput> _TYPE = dafny.TypeDescriptor.<CreateAwsKmsKeyringInput>referenceWithInitializer(CreateAwsKmsKeyringInput.class, () -> CreateAwsKmsKeyringInput.Default());
  public static dafny.TypeDescriptor<CreateAwsKmsKeyringInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<CreateAwsKmsKeyringInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final CreateAwsKmsKeyringInput theDefault = CreateAwsKmsKeyringInput.create(dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), null, Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>Default(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))));
  public static CreateAwsKmsKeyringInput Default() {
    return theDefault;
  }
  public static CreateAwsKmsKeyringInput create(dafny.DafnySequence<? extends Character> kmsKeyId, software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient kmsClient, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> grantTokens) {
    return new CreateAwsKmsKeyringInput(kmsKeyId, kmsClient, grantTokens);
  }
  public static CreateAwsKmsKeyringInput create_CreateAwsKmsKeyringInput(dafny.DafnySequence<? extends Character> kmsKeyId, software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient kmsClient, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> grantTokens) {
    return create(kmsKeyId, kmsClient, grantTokens);
  }
  public boolean is_CreateAwsKmsKeyringInput() { return true; }
  public dafny.DafnySequence<? extends Character> dtor_kmsKeyId() {
    return this._kmsKeyId;
  }
  public software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient dtor_kmsClient() {
    return this._kmsClient;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> dtor_grantTokens() {
    return this._grantTokens;
  }
}
