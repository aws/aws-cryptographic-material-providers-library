// Class KeyMetadata
// Dafny class KeyMetadata compiled into Java
package software.amazon.cryptography.services.kms.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public class KeyMetadata {
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _AWSAccountId;
  public dafny.DafnySequence<? extends Character> _KeyId;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _Arn;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _CreationDate;
  public Wrappers_Compile.Option<Boolean> _Enabled;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _Description;
  public Wrappers_Compile.Option<KeyUsageType> _KeyUsage;
  public Wrappers_Compile.Option<KeyState> _KeyState;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _DeletionDate;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _ValidTo;
  public Wrappers_Compile.Option<OriginType> _Origin;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _CustomKeyStoreId;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> _CloudHsmClusterId;
  public Wrappers_Compile.Option<ExpirationModelType> _ExpirationModel;
  public Wrappers_Compile.Option<KeyManagerType> _KeyManager;
  public Wrappers_Compile.Option<CustomerMasterKeySpec> _CustomerMasterKeySpec;
  public Wrappers_Compile.Option<KeySpec> _KeySpec;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends EncryptionAlgorithmSpec>> _EncryptionAlgorithms;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends SigningAlgorithmSpec>> _SigningAlgorithms;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends KeyAgreementAlgorithmSpec>> _KeyAgreementAlgorithms;
  public Wrappers_Compile.Option<Boolean> _MultiRegion;
  public Wrappers_Compile.Option<MultiRegionConfiguration> _MultiRegionConfiguration;
  public Wrappers_Compile.Option<java.lang.Integer> _PendingDeletionWindowInDays;
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends MacAlgorithmSpec>> _MacAlgorithms;
  public Wrappers_Compile.Option<XksKeyConfigurationType> _XksKeyConfiguration;
  public KeyMetadata (Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> AWSAccountId, dafny.DafnySequence<? extends Character> KeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Arn, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CreationDate, Wrappers_Compile.Option<Boolean> Enabled, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Description, Wrappers_Compile.Option<KeyUsageType> KeyUsage, Wrappers_Compile.Option<KeyState> KeyState, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> DeletionDate, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ValidTo, Wrappers_Compile.Option<OriginType> Origin, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CustomKeyStoreId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CloudHsmClusterId, Wrappers_Compile.Option<ExpirationModelType> ExpirationModel, Wrappers_Compile.Option<KeyManagerType> KeyManager, Wrappers_Compile.Option<CustomerMasterKeySpec> CustomerMasterKeySpec, Wrappers_Compile.Option<KeySpec> KeySpec, Wrappers_Compile.Option<dafny.DafnySequence<? extends EncryptionAlgorithmSpec>> EncryptionAlgorithms, Wrappers_Compile.Option<dafny.DafnySequence<? extends SigningAlgorithmSpec>> SigningAlgorithms, Wrappers_Compile.Option<dafny.DafnySequence<? extends KeyAgreementAlgorithmSpec>> KeyAgreementAlgorithms, Wrappers_Compile.Option<Boolean> MultiRegion, Wrappers_Compile.Option<MultiRegionConfiguration> MultiRegionConfiguration, Wrappers_Compile.Option<java.lang.Integer> PendingDeletionWindowInDays, Wrappers_Compile.Option<dafny.DafnySequence<? extends MacAlgorithmSpec>> MacAlgorithms, Wrappers_Compile.Option<XksKeyConfigurationType> XksKeyConfiguration) {
    this._AWSAccountId = AWSAccountId;
    this._KeyId = KeyId;
    this._Arn = Arn;
    this._CreationDate = CreationDate;
    this._Enabled = Enabled;
    this._Description = Description;
    this._KeyUsage = KeyUsage;
    this._KeyState = KeyState;
    this._DeletionDate = DeletionDate;
    this._ValidTo = ValidTo;
    this._Origin = Origin;
    this._CustomKeyStoreId = CustomKeyStoreId;
    this._CloudHsmClusterId = CloudHsmClusterId;
    this._ExpirationModel = ExpirationModel;
    this._KeyManager = KeyManager;
    this._CustomerMasterKeySpec = CustomerMasterKeySpec;
    this._KeySpec = KeySpec;
    this._EncryptionAlgorithms = EncryptionAlgorithms;
    this._SigningAlgorithms = SigningAlgorithms;
    this._KeyAgreementAlgorithms = KeyAgreementAlgorithms;
    this._MultiRegion = MultiRegion;
    this._MultiRegionConfiguration = MultiRegionConfiguration;
    this._PendingDeletionWindowInDays = PendingDeletionWindowInDays;
    this._MacAlgorithms = MacAlgorithms;
    this._XksKeyConfiguration = XksKeyConfiguration;
  }

  @Override
  public boolean equals(Object other) {
    if (this == other) return true;
    if (other == null) return false;
    if (getClass() != other.getClass()) return false;
    KeyMetadata o = (KeyMetadata)other;
    return true && java.util.Objects.equals(this._AWSAccountId, o._AWSAccountId) && java.util.Objects.equals(this._KeyId, o._KeyId) && java.util.Objects.equals(this._Arn, o._Arn) && java.util.Objects.equals(this._CreationDate, o._CreationDate) && java.util.Objects.equals(this._Enabled, o._Enabled) && java.util.Objects.equals(this._Description, o._Description) && java.util.Objects.equals(this._KeyUsage, o._KeyUsage) && java.util.Objects.equals(this._KeyState, o._KeyState) && java.util.Objects.equals(this._DeletionDate, o._DeletionDate) && java.util.Objects.equals(this._ValidTo, o._ValidTo) && java.util.Objects.equals(this._Origin, o._Origin) && java.util.Objects.equals(this._CustomKeyStoreId, o._CustomKeyStoreId) && java.util.Objects.equals(this._CloudHsmClusterId, o._CloudHsmClusterId) && java.util.Objects.equals(this._ExpirationModel, o._ExpirationModel) && java.util.Objects.equals(this._KeyManager, o._KeyManager) && java.util.Objects.equals(this._CustomerMasterKeySpec, o._CustomerMasterKeySpec) && java.util.Objects.equals(this._KeySpec, o._KeySpec) && java.util.Objects.equals(this._EncryptionAlgorithms, o._EncryptionAlgorithms) && java.util.Objects.equals(this._SigningAlgorithms, o._SigningAlgorithms) && java.util.Objects.equals(this._KeyAgreementAlgorithms, o._KeyAgreementAlgorithms) && java.util.Objects.equals(this._MultiRegion, o._MultiRegion) && java.util.Objects.equals(this._MultiRegionConfiguration, o._MultiRegionConfiguration) && java.util.Objects.equals(this._PendingDeletionWindowInDays, o._PendingDeletionWindowInDays) && java.util.Objects.equals(this._MacAlgorithms, o._MacAlgorithms) && java.util.Objects.equals(this._XksKeyConfiguration, o._XksKeyConfiguration);
  }
  @Override
  public int hashCode() {
    long hash = 5381;
    hash = ((hash << 5) + hash) + 0;
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._AWSAccountId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Arn);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._CreationDate);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Enabled);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Description);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyUsage);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyState);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._DeletionDate);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ValidTo);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._Origin);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._CustomKeyStoreId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._CloudHsmClusterId);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._ExpirationModel);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyManager);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._CustomerMasterKeySpec);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeySpec);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._EncryptionAlgorithms);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._SigningAlgorithms);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._KeyAgreementAlgorithms);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._MultiRegion);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._MultiRegionConfiguration);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._PendingDeletionWindowInDays);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._MacAlgorithms);
    hash = ((hash << 5) + hash) + java.util.Objects.hashCode(this._XksKeyConfiguration);
    return (int)hash;
  }

  @Override
  public String toString() {
    StringBuilder s = new StringBuilder();
    s.append("ComAmazonawsKmsTypes.KeyMetadata.KeyMetadata");
    s.append("(");
    s.append(dafny.Helpers.toString(this._AWSAccountId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._KeyId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Arn));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._CreationDate));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Enabled));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Description));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._KeyUsage));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._KeyState));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._DeletionDate));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ValidTo));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._Origin));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._CustomKeyStoreId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._CloudHsmClusterId));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._ExpirationModel));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._KeyManager));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._CustomerMasterKeySpec));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._KeySpec));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._EncryptionAlgorithms));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._SigningAlgorithms));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._KeyAgreementAlgorithms));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._MultiRegion));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._MultiRegionConfiguration));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._PendingDeletionWindowInDays));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._MacAlgorithms));
    s.append(", ");
    s.append(dafny.Helpers.toString(this._XksKeyConfiguration));
    s.append(")");
    return s.toString();
  }
  private static final dafny.TypeDescriptor<KeyMetadata> _TYPE = dafny.TypeDescriptor.<KeyMetadata>referenceWithInitializer(KeyMetadata.class, () -> KeyMetadata.Default());
  public static dafny.TypeDescriptor<KeyMetadata> _typeDescriptor() {
    return (dafny.TypeDescriptor<KeyMetadata>) (dafny.TypeDescriptor<?>) _TYPE;
  }

  private static final KeyMetadata theDefault = KeyMetadata.create(Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), dafny.DafnySequence.<Character> empty(dafny.TypeDescriptor.CHAR), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(ArnType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<Boolean>Default(dafny.TypeDescriptor.BOOLEAN), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(DescriptionType._typeDescriptor()), Wrappers_Compile.Option.<KeyUsageType>Default(KeyUsageType._typeDescriptor()), Wrappers_Compile.Option.<KeyState>Default(KeyState._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(dafny.DafnySequence.<Character>_typeDescriptor(dafny.TypeDescriptor.CHAR)), Wrappers_Compile.Option.<OriginType>Default(OriginType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(CustomKeyStoreIdType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends Character>>Default(CloudHsmClusterIdType._typeDescriptor()), Wrappers_Compile.Option.<ExpirationModelType>Default(ExpirationModelType._typeDescriptor()), Wrappers_Compile.Option.<KeyManagerType>Default(KeyManagerType._typeDescriptor()), Wrappers_Compile.Option.<CustomerMasterKeySpec>Default(CustomerMasterKeySpec._typeDescriptor()), Wrappers_Compile.Option.<KeySpec>Default(KeySpec._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends EncryptionAlgorithmSpec>>Default(dafny.DafnySequence.<EncryptionAlgorithmSpec>_typeDescriptor(EncryptionAlgorithmSpec._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends SigningAlgorithmSpec>>Default(dafny.DafnySequence.<SigningAlgorithmSpec>_typeDescriptor(SigningAlgorithmSpec._typeDescriptor())), Wrappers_Compile.Option.<dafny.DafnySequence<? extends KeyAgreementAlgorithmSpec>>Default(dafny.DafnySequence.<KeyAgreementAlgorithmSpec>_typeDescriptor(KeyAgreementAlgorithmSpec._typeDescriptor())), Wrappers_Compile.Option.<Boolean>Default(dafny.TypeDescriptor.BOOLEAN), Wrappers_Compile.Option.<MultiRegionConfiguration>Default(MultiRegionConfiguration._typeDescriptor()), Wrappers_Compile.Option.<java.lang.Integer>Default(PendingWindowInDaysType._typeDescriptor()), Wrappers_Compile.Option.<dafny.DafnySequence<? extends MacAlgorithmSpec>>Default(dafny.DafnySequence.<MacAlgorithmSpec>_typeDescriptor(MacAlgorithmSpec._typeDescriptor())), Wrappers_Compile.Option.<XksKeyConfigurationType>Default(XksKeyConfigurationType._typeDescriptor()));
  public static KeyMetadata Default() {
    return theDefault;
  }
  public static KeyMetadata create(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> AWSAccountId, dafny.DafnySequence<? extends Character> KeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Arn, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CreationDate, Wrappers_Compile.Option<Boolean> Enabled, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Description, Wrappers_Compile.Option<KeyUsageType> KeyUsage, Wrappers_Compile.Option<KeyState> KeyState, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> DeletionDate, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ValidTo, Wrappers_Compile.Option<OriginType> Origin, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CustomKeyStoreId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CloudHsmClusterId, Wrappers_Compile.Option<ExpirationModelType> ExpirationModel, Wrappers_Compile.Option<KeyManagerType> KeyManager, Wrappers_Compile.Option<CustomerMasterKeySpec> CustomerMasterKeySpec, Wrappers_Compile.Option<KeySpec> KeySpec, Wrappers_Compile.Option<dafny.DafnySequence<? extends EncryptionAlgorithmSpec>> EncryptionAlgorithms, Wrappers_Compile.Option<dafny.DafnySequence<? extends SigningAlgorithmSpec>> SigningAlgorithms, Wrappers_Compile.Option<dafny.DafnySequence<? extends KeyAgreementAlgorithmSpec>> KeyAgreementAlgorithms, Wrappers_Compile.Option<Boolean> MultiRegion, Wrappers_Compile.Option<MultiRegionConfiguration> MultiRegionConfiguration, Wrappers_Compile.Option<java.lang.Integer> PendingDeletionWindowInDays, Wrappers_Compile.Option<dafny.DafnySequence<? extends MacAlgorithmSpec>> MacAlgorithms, Wrappers_Compile.Option<XksKeyConfigurationType> XksKeyConfiguration) {
    return new KeyMetadata(AWSAccountId, KeyId, Arn, CreationDate, Enabled, Description, KeyUsage, KeyState, DeletionDate, ValidTo, Origin, CustomKeyStoreId, CloudHsmClusterId, ExpirationModel, KeyManager, CustomerMasterKeySpec, KeySpec, EncryptionAlgorithms, SigningAlgorithms, KeyAgreementAlgorithms, MultiRegion, MultiRegionConfiguration, PendingDeletionWindowInDays, MacAlgorithms, XksKeyConfiguration);
  }
  public static KeyMetadata create_KeyMetadata(Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> AWSAccountId, dafny.DafnySequence<? extends Character> KeyId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Arn, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CreationDate, Wrappers_Compile.Option<Boolean> Enabled, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> Description, Wrappers_Compile.Option<KeyUsageType> KeyUsage, Wrappers_Compile.Option<KeyState> KeyState, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> DeletionDate, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> ValidTo, Wrappers_Compile.Option<OriginType> Origin, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CustomKeyStoreId, Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> CloudHsmClusterId, Wrappers_Compile.Option<ExpirationModelType> ExpirationModel, Wrappers_Compile.Option<KeyManagerType> KeyManager, Wrappers_Compile.Option<CustomerMasterKeySpec> CustomerMasterKeySpec, Wrappers_Compile.Option<KeySpec> KeySpec, Wrappers_Compile.Option<dafny.DafnySequence<? extends EncryptionAlgorithmSpec>> EncryptionAlgorithms, Wrappers_Compile.Option<dafny.DafnySequence<? extends SigningAlgorithmSpec>> SigningAlgorithms, Wrappers_Compile.Option<dafny.DafnySequence<? extends KeyAgreementAlgorithmSpec>> KeyAgreementAlgorithms, Wrappers_Compile.Option<Boolean> MultiRegion, Wrappers_Compile.Option<MultiRegionConfiguration> MultiRegionConfiguration, Wrappers_Compile.Option<java.lang.Integer> PendingDeletionWindowInDays, Wrappers_Compile.Option<dafny.DafnySequence<? extends MacAlgorithmSpec>> MacAlgorithms, Wrappers_Compile.Option<XksKeyConfigurationType> XksKeyConfiguration) {
    return create(AWSAccountId, KeyId, Arn, CreationDate, Enabled, Description, KeyUsage, KeyState, DeletionDate, ValidTo, Origin, CustomKeyStoreId, CloudHsmClusterId, ExpirationModel, KeyManager, CustomerMasterKeySpec, KeySpec, EncryptionAlgorithms, SigningAlgorithms, KeyAgreementAlgorithms, MultiRegion, MultiRegionConfiguration, PendingDeletionWindowInDays, MacAlgorithms, XksKeyConfiguration);
  }
  public boolean is_KeyMetadata() { return true; }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_AWSAccountId() {
    return this._AWSAccountId;
  }
  public dafny.DafnySequence<? extends Character> dtor_KeyId() {
    return this._KeyId;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_Arn() {
    return this._Arn;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_CreationDate() {
    return this._CreationDate;
  }
  public Wrappers_Compile.Option<Boolean> dtor_Enabled() {
    return this._Enabled;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_Description() {
    return this._Description;
  }
  public Wrappers_Compile.Option<KeyUsageType> dtor_KeyUsage() {
    return this._KeyUsage;
  }
  public Wrappers_Compile.Option<KeyState> dtor_KeyState() {
    return this._KeyState;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_DeletionDate() {
    return this._DeletionDate;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_ValidTo() {
    return this._ValidTo;
  }
  public Wrappers_Compile.Option<OriginType> dtor_Origin() {
    return this._Origin;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_CustomKeyStoreId() {
    return this._CustomKeyStoreId;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends Character>> dtor_CloudHsmClusterId() {
    return this._CloudHsmClusterId;
  }
  public Wrappers_Compile.Option<ExpirationModelType> dtor_ExpirationModel() {
    return this._ExpirationModel;
  }
  public Wrappers_Compile.Option<KeyManagerType> dtor_KeyManager() {
    return this._KeyManager;
  }
  public Wrappers_Compile.Option<CustomerMasterKeySpec> dtor_CustomerMasterKeySpec() {
    return this._CustomerMasterKeySpec;
  }
  public Wrappers_Compile.Option<KeySpec> dtor_KeySpec() {
    return this._KeySpec;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends EncryptionAlgorithmSpec>> dtor_EncryptionAlgorithms() {
    return this._EncryptionAlgorithms;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends SigningAlgorithmSpec>> dtor_SigningAlgorithms() {
    return this._SigningAlgorithms;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends KeyAgreementAlgorithmSpec>> dtor_KeyAgreementAlgorithms() {
    return this._KeyAgreementAlgorithms;
  }
  public Wrappers_Compile.Option<Boolean> dtor_MultiRegion() {
    return this._MultiRegion;
  }
  public Wrappers_Compile.Option<MultiRegionConfiguration> dtor_MultiRegionConfiguration() {
    return this._MultiRegionConfiguration;
  }
  public Wrappers_Compile.Option<java.lang.Integer> dtor_PendingDeletionWindowInDays() {
    return this._PendingDeletionWindowInDays;
  }
  public Wrappers_Compile.Option<dafny.DafnySequence<? extends MacAlgorithmSpec>> dtor_MacAlgorithms() {
    return this._MacAlgorithms;
  }
  public Wrappers_Compile.Option<XksKeyConfigurationType> dtor_XksKeyConfiguration() {
    return this._XksKeyConfiguration;
  }
}
