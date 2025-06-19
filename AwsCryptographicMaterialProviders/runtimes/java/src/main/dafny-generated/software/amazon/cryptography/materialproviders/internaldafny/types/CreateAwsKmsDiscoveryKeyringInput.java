// Class CreateAwsKmsDiscoveryKeyringInput
// Dafny class CreateAwsKmsDiscoveryKeyringInput compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class CreateAwsKmsDiscoveryKeyringInput {
  public software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _kmsClient;
  public Wrappers_Compile.Option<DiscoveryFilter> _discoveryFilter;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> _grantTokens;
  public CreateAwsKmsDiscoveryKeyringInput (software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient kmsClient, Wrappers_Compile.Option<DiscoveryFilter> discoveryFilter, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> grantTokens) {
    this._kmsClient = kmsClient;
    this._discoveryFilter = discoveryFilter;
    this._grantTokens = grantTokens;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CreateAwsKmsDiscoveryKeyringInput o = (CreateAwsKmsDiscoveryKeyringInput)other;
    return true && this._kmsClient == o._kmsClient && java.util.Objects.equals(this._discoveryFilter, o._discoveryFilter) && java.util.Objects.equals(this._grantTokens, o._grantTokens);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._kmsClient);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._discoveryFilter);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._grantTokens);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.CreateAwsKmsDiscoveryKeyringInput.CreateAwsKmsDiscoveryKeyringInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._kmsClient));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._discoveryFilter));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._grantTokens));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<CreateAwsKmsDiscoveryKeyringInput> _TYPE = dafny.TypeDescriptor.<CreateAwsKmsDiscoveryKeyringInput>referenceWithInitializer(CreateAwsKmsDiscoveryKeyringInput.class, () -> CreateAwsKmsDiscoveryKeyringInput.Default());
  public static dafny.TypeDescriptor<CreateAwsKmsDiscoveryKeyringInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<CreateAwsKmsDiscoveryKeyringInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final CreateAwsKmsDiscoveryKeyringInput theDefault = CreateAwsKmsDiscoveryKeyringInput.create(null, Wrappers_Compile.Option.<DiscoveryFilter>Default(DiscoveryFilter._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>Default(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))));
  public static CreateAwsKmsDiscoveryKeyringInput Default() {
    return theDefault;
  }
  public static CreateAwsKmsDiscoveryKeyringInput create(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient kmsClient, Wrappers_Compile.Option<DiscoveryFilter> discoveryFilter, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> grantTokens) {
    return new CreateAwsKmsDiscoveryKeyringInput(kmsClient, discoveryFilter, grantTokens);
  }
  public static CreateAwsKmsDiscoveryKeyringInput create_CreateAwsKmsDiscoveryKeyringInput(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient kmsClient, Wrappers_Compile.Option<DiscoveryFilter> discoveryFilter, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> grantTokens) {
    return create(kmsClient, discoveryFilter, grantTokens);
  }
  public boolean is_CreateAwsKmsDiscoveryKeyringInput() { return true; }
  public software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient dtor_kmsClient() {
    return this._kmsClient;
  }
  public Wrappers_Compile.Option<DiscoveryFilter> dtor_discoveryFilter() {
    return this._discoveryFilter;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> dtor_grantTokens() {
    return this._grantTokens;
  }
}
