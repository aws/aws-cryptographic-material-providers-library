// Class CreateAwsKmsEcdhKeyringInput
// Dafny class CreateAwsKmsEcdhKeyringInput compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class CreateAwsKmsEcdhKeyringInput {
  public KmsEcdhStaticConfigurations _KeyAgreementScheme;
  public software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec _curveSpec;
  public software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _kmsClient;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> _grantTokens;
  public CreateAwsKmsEcdhKeyringInput (KmsEcdhStaticConfigurations KeyAgreementScheme, software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec curveSpec, software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient kmsClient, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> grantTokens) {
    this._KeyAgreementScheme = KeyAgreementScheme;
    this._curveSpec = curveSpec;
    this._kmsClient = kmsClient;
    this._grantTokens = grantTokens;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CreateAwsKmsEcdhKeyringInput o = (CreateAwsKmsEcdhKeyringInput)other;
    return true && java.util.Objects.equals(this._KeyAgreementScheme, o._KeyAgreementScheme) && java.util.Objects.equals(this._curveSpec, o._curveSpec) && this._kmsClient == o._kmsClient && java.util.Objects.equals(this._grantTokens, o._grantTokens);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyAgreementScheme);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._curveSpec);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._kmsClient);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._grantTokens);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.CreateAwsKmsEcdhKeyringInput.CreateAwsKmsEcdhKeyringInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._KeyAgreementScheme));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._curveSpec));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._kmsClient));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._grantTokens));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<CreateAwsKmsEcdhKeyringInput> _TYPE = dafny.TypeDescriptor.<CreateAwsKmsEcdhKeyringInput>referenceWithInitializer(CreateAwsKmsEcdhKeyringInput.class, () -> CreateAwsKmsEcdhKeyringInput.Default());
  public static dafny.TypeDescriptor<CreateAwsKmsEcdhKeyringInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<CreateAwsKmsEcdhKeyringInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final CreateAwsKmsEcdhKeyringInput theDefault = CreateAwsKmsEcdhKeyringInput.create(KmsEcdhStaticConfigurations.Default(), software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec.Default(), null, Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>Default(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))));
  public static CreateAwsKmsEcdhKeyringInput Default() {
    return theDefault;
  }
  public static CreateAwsKmsEcdhKeyringInput create(KmsEcdhStaticConfigurations KeyAgreementScheme, software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec curveSpec, software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient kmsClient, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> grantTokens) {
    return new CreateAwsKmsEcdhKeyringInput(KeyAgreementScheme, curveSpec, kmsClient, grantTokens);
  }
  public static CreateAwsKmsEcdhKeyringInput create_CreateAwsKmsEcdhKeyringInput(KmsEcdhStaticConfigurations KeyAgreementScheme, software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec curveSpec, software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient kmsClient, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> grantTokens) {
    return create(KeyAgreementScheme, curveSpec, kmsClient, grantTokens);
  }
  public boolean is_CreateAwsKmsEcdhKeyringInput() { return true; }
  public KmsEcdhStaticConfigurations dtor_KeyAgreementScheme() {
    return this._KeyAgreementScheme;
  }
  public software.amazon.cryptography.primitives.internaldafny.types.ECDHCurveSpec dtor_curveSpec() {
    return this._curveSpec;
  }
  public software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient dtor_kmsClient() {
    return this._kmsClient;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> dtor_grantTokens() {
    return this._grantTokens;
  }
}
