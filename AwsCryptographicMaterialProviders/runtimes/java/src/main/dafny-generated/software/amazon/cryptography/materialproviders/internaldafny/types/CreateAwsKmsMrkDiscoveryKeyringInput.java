// Class CreateAwsKmsMrkDiscoveryKeyringInput
// Dafny class CreateAwsKmsMrkDiscoveryKeyringInput compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class CreateAwsKmsMrkDiscoveryKeyringInput {
  public software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient _kmsClient;
  public Wrappers_Compile.Option<DiscoveryFilter> _discoveryFilter;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> _grantTokens;
  public dafny.DafnySequence<? extends Character> _region;
  public CreateAwsKmsMrkDiscoveryKeyringInput (software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient kmsClient, Wrappers_Compile.Option<DiscoveryFilter> discoveryFilter, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> grantTokens, dafny.DafnySequence<? extends Character> region) {
    this._kmsClient = kmsClient;
    this._discoveryFilter = discoveryFilter;
    this._grantTokens = grantTokens;
    this._region = region;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    CreateAwsKmsMrkDiscoveryKeyringInput o = (CreateAwsKmsMrkDiscoveryKeyringInput)other;
    return true && this._kmsClient == o._kmsClient && java.util.Objects.equals(this._discoveryFilter, o._discoveryFilter) && java.util.Objects.equals(this._grantTokens, o._grantTokens) && java.util.Objects.equals(this._region, o._region);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._kmsClient);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._discoveryFilter);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._grantTokens);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._region);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("AwsCryptographyMaterialProvidersTypes.CreateAwsKmsMrkDiscoveryKeyringInput.CreateAwsKmsMrkDiscoveryKeyringInput");
    s.append("(");
    s.append(dafny.Helpers.toString(this._kmsClient));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._discoveryFilter));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._grantTokens));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._region));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<CreateAwsKmsMrkDiscoveryKeyringInput> _TYPE = dafny.TypeDescriptor.<CreateAwsKmsMrkDiscoveryKeyringInput>referenceWithInitializer(CreateAwsKmsMrkDiscoveryKeyringInput.class, () -> CreateAwsKmsMrkDiscoveryKeyringInput.Default());
  public static dafny.TypeDescriptor<CreateAwsKmsMrkDiscoveryKeyringInput> _typeDescriptor() {
    return (dafny.TypeDescriptor<CreateAwsKmsMrkDiscoveryKeyringInput>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final CreateAwsKmsMrkDiscoveryKeyringInput theDefault = CreateAwsKmsMrkDiscoveryKeyringInput.create(null, Wrappers_Compile.Option.<DiscoveryFilter>Default(DiscoveryFilter._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>>Default(dafny.DafnySequence.<dafny.DafnySequence<? extends Character>>_typeDescriptor(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR))), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR));
  public static CreateAwsKmsMrkDiscoveryKeyringInput Default() {
    return theDefault;
  }
  public static CreateAwsKmsMrkDiscoveryKeyringInput create(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient kmsClient, Wrappers_Compile.Option<DiscoveryFilter> discoveryFilter, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> grantTokens, dafny.DafnySequence<? extends Character> region) {
    return new CreateAwsKmsMrkDiscoveryKeyringInput(kmsClient, discoveryFilter, grantTokens, region);
  }
  public static CreateAwsKmsMrkDiscoveryKeyringInput create_CreateAwsKmsMrkDiscoveryKeyringInput(software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient kmsClient, Wrappers_Compile.Option<DiscoveryFilter> discoveryFilter, Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> grantTokens, dafny.DafnySequence<? extends Character> region) {
    return create(kmsClient, discoveryFilter, grantTokens, region);
  }
  public boolean is_CreateAwsKmsMrkDiscoveryKeyringInput() { return true; }
  public software.amazon.cryptography.services.kms.internaldafny.types.IKMSClient dtor_kmsClient() {
    return this._kmsClient;
  }
  public Wrappers_Compile.Option<DiscoveryFilter> dtor_discoveryFilter() {
    return this._discoveryFilter;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends dafny.DafnySequence<? extends Character>>> dtor_grantTokens() {
    return this._grantTokens;
  }
  public dafny.DafnySequence<? extends Character> dtor_region() {
    return this._region;
  }
}
