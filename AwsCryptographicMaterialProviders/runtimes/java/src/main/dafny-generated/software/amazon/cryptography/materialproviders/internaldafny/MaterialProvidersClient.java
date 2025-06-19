// Class MaterialProvidersClient
// Dafny class MaterialProvidersClient compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny;

@SuppressWarnings({"unchecked", "deprecation"})
public class MaterialProvidersClient implements software.amazon.cryptography.materialproviders.internaldafny.types.IAwsCryptographicMaterialProvidersClient {
  public MaterialProvidersClient() {
    this._config = (AwsCryptographyMaterialProvidersOperations_Compile.Config)null;
  }
  public void __ctor(AwsCryptographyMaterialProvidersOperations_Compile.Config config)
  {
    (this)._config = config;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> CreateAwsKmsKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsKeyringInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
      _out0 = AwsCryptographyMaterialProvidersOperations_Compile.__default.CreateAwsKmsKeyring((this).config(), input);
      output = _out0;
    }
    return output;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> CreateAwsKmsDiscoveryKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsDiscoveryKeyringInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
      _out0 = AwsCryptographyMaterialProvidersOperations_Compile.__default.CreateAwsKmsDiscoveryKeyring((this).config(), input);
      output = _out0;
    }
    return output;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> CreateAwsKmsMultiKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsMultiKeyringInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
      _out0 = AwsCryptographyMaterialProvidersOperations_Compile.__default.CreateAwsKmsMultiKeyring((this).config(), input);
      output = _out0;
    }
    return output;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> CreateAwsKmsDiscoveryMultiKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsDiscoveryMultiKeyringInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
      _out0 = AwsCryptographyMaterialProvidersOperations_Compile.__default.CreateAwsKmsDiscoveryMultiKeyring((this).config(), input);
      output = _out0;
    }
    return output;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> CreateAwsKmsMrkKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsMrkKeyringInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
      _out0 = AwsCryptographyMaterialProvidersOperations_Compile.__default.CreateAwsKmsMrkKeyring((this).config(), input);
      output = _out0;
    }
    return output;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> CreateAwsKmsMrkMultiKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsMrkMultiKeyringInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
      _out0 = AwsCryptographyMaterialProvidersOperations_Compile.__default.CreateAwsKmsMrkMultiKeyring((this).config(), input);
      output = _out0;
    }
    return output;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> CreateAwsKmsMrkDiscoveryKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsMrkDiscoveryKeyringInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
      _out0 = AwsCryptographyMaterialProvidersOperations_Compile.__default.CreateAwsKmsMrkDiscoveryKeyring((this).config(), input);
      output = _out0;
    }
    return output;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> CreateAwsKmsMrkDiscoveryMultiKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsMrkDiscoveryMultiKeyringInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
      _out0 = AwsCryptographyMaterialProvidersOperations_Compile.__default.CreateAwsKmsMrkDiscoveryMultiKeyring((this).config(), input);
      output = _out0;
    }
    return output;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> CreateAwsKmsHierarchicalKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsHierarchicalKeyringInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
      _out0 = AwsCryptographyMaterialProvidersOperations_Compile.__default.CreateAwsKmsHierarchicalKeyring((this).config(), input);
      output = _out0;
    }
    return output;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> CreateAwsKmsRsaKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsRsaKeyringInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
      _out0 = AwsCryptographyMaterialProvidersOperations_Compile.__default.CreateAwsKmsRsaKeyring((this).config(), input);
      output = _out0;
    }
    return output;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> CreateAwsKmsEcdhKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateAwsKmsEcdhKeyringInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
      _out0 = AwsCryptographyMaterialProvidersOperations_Compile.__default.CreateAwsKmsEcdhKeyring((this).config(), input);
      output = _out0;
    }
    return output;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> CreateMultiKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateMultiKeyringInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
      _out0 = AwsCryptographyMaterialProvidersOperations_Compile.__default.CreateMultiKeyring((this).config(), input);
      output = _out0;
    }
    return output;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> CreateRawAesKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateRawAesKeyringInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
      _out0 = AwsCryptographyMaterialProvidersOperations_Compile.__default.CreateRawAesKeyring((this).config(), input);
      output = _out0;
    }
    return output;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> CreateRawRsaKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateRawRsaKeyringInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
      _out0 = AwsCryptographyMaterialProvidersOperations_Compile.__default.CreateRawRsaKeyring((this).config(), input);
      output = _out0;
    }
    return output;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> CreateRawEcdhKeyring(software.amazon.cryptography.materialproviders.internaldafny.types.CreateRawEcdhKeyringInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IKeyring, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
      _out0 = AwsCryptographyMaterialProvidersOperations_Compile.__default.CreateRawEcdhKeyring((this).config(), input);
      output = _out0;
    }
    return output;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager, software.amazon.cryptography.materialproviders.internaldafny.types.Error> CreateDefaultCryptographicMaterialsManager(software.amazon.cryptography.materialproviders.internaldafny.types.CreateDefaultCryptographicMaterialsManagerInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
      _out0 = AwsCryptographyMaterialProvidersOperations_Compile.__default.CreateDefaultCryptographicMaterialsManager((this).config(), input);
      output = _out0;
    }
    return output;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager, software.amazon.cryptography.materialproviders.internaldafny.types.Error> CreateRequiredEncryptionContextCMM(software.amazon.cryptography.materialproviders.internaldafny.types.CreateRequiredEncryptionContextCMMInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsManager, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
      _out0 = AwsCryptographyMaterialProvidersOperations_Compile.__default.CreateRequiredEncryptionContextCMM((this).config(), input);
      output = _out0;
    }
    return output;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache, software.amazon.cryptography.materialproviders.internaldafny.types.Error> CreateCryptographicMaterialsCache(software.amazon.cryptography.materialproviders.internaldafny.types.CreateCryptographicMaterialsCacheInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.ICryptographicMaterialsCache, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
      _out0 = AwsCryptographyMaterialProvidersOperations_Compile.__default.CreateCryptographicMaterialsCache((this).config(), input);
      output = _out0;
    }
    return output;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier, software.amazon.cryptography.materialproviders.internaldafny.types.Error> CreateDefaultClientSupplier(software.amazon.cryptography.materialproviders.internaldafny.types.CreateDefaultClientSupplierInput input)
  {
    Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier, software.amazon.cryptography.materialproviders.internaldafny.types.Error> output = (Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier, software.amazon.cryptography.materialproviders.internaldafny.types.Error>)null;
    if(true) {
      Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.IClientSupplier, software.amazon.cryptography.materialproviders.internaldafny.types.Error> _out0;
      _out0 = AwsCryptographyMaterialProvidersOperations_Compile.__default.CreateDefaultClientSupplier((this).config(), input);
      output = _out0;
    }
    return output;
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> InitializeEncryptionMaterials(software.amazon.cryptography.materialproviders.internaldafny.types.InitializeEncryptionMaterialsInput input) {
    return AwsCryptographyMaterialProvidersOperations_Compile.__default.InitializeEncryptionMaterials((this).config(), input);
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials, software.amazon.cryptography.materialproviders.internaldafny.types.Error> InitializeDecryptionMaterials(software.amazon.cryptography.materialproviders.internaldafny.types.InitializeDecryptionMaterialsInput input) {
    return AwsCryptographyMaterialProvidersOperations_Compile.__default.InitializeDecryptionMaterials((this).config(), input);
  }
  public Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> ValidEncryptionMaterialsTransition(software.amazon.cryptography.materialproviders.internaldafny.types.ValidEncryptionMaterialsTransitionInput input) {
    return AwsCryptographyMaterialProvidersOperations_Compile.__default.ValidEncryptionMaterialsTransition((this).config(), input);
  }
  public Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> ValidDecryptionMaterialsTransition(software.amazon.cryptography.materialproviders.internaldafny.types.ValidDecryptionMaterialsTransitionInput input) {
    return AwsCryptographyMaterialProvidersOperations_Compile.__default.ValidDecryptionMaterialsTransition((this).config(), input);
  }
  public Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> EncryptionMaterialsHasPlaintextDataKey(software.amazon.cryptography.materialproviders.internaldafny.types.EncryptionMaterials input) {
    return AwsCryptographyMaterialProvidersOperations_Compile.__default.EncryptionMaterialsHasPlaintextDataKey((this).config(), input);
  }
  public Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> DecryptionMaterialsWithPlaintextDataKey(software.amazon.cryptography.materialproviders.internaldafny.types.DecryptionMaterials input) {
    return AwsCryptographyMaterialProvidersOperations_Compile.__default.DecryptionMaterialsWithPlaintextDataKey((this).config(), input);
  }
  public Wrappers_Compile.Result<software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo, software.amazon.cryptography.materialproviders.internaldafny.types.Error> GetAlgorithmSuiteInfo(dafny.DafnySequence<? extends java.lang.Byte> input) {
    return AwsCryptographyMaterialProvidersOperations_Compile.__default.GetAlgorithmSuiteInfo((this).config(), input);
  }
  public Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> ValidAlgorithmSuiteInfo(software.amazon.cryptography.materialproviders.internaldafny.types.AlgorithmSuiteInfo input) {
    return AwsCryptographyMaterialProvidersOperations_Compile.__default.ValidAlgorithmSuiteInfo((this).config(), input);
  }
  public Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> ValidateCommitmentPolicyOnEncrypt(software.amazon.cryptography.materialproviders.internaldafny.types.ValidateCommitmentPolicyOnEncryptInput input) {
    return AwsCryptographyMaterialProvidersOperations_Compile.__default.ValidateCommitmentPolicyOnEncrypt((this).config(), input);
  }
  public Wrappers_Compile.Result<dafny.Tuple0, software.amazon.cryptography.materialproviders.internaldafny.types.Error> ValidateCommitmentPolicyOnDecrypt(software.amazon.cryptography.materialproviders.internaldafny.types.ValidateCommitmentPolicyOnDecryptInput input) {
    return AwsCryptographyMaterialProvidersOperations_Compile.__default.ValidateCommitmentPolicyOnDecrypt((this).config(), input);
  }
  public AwsCryptographyMaterialProvidersOperations_Compile.Config _config;
  public AwsCryptographyMaterialProvidersOperations_Compile.Config config()
  {
    return this._config;
  }
  private static final dafny.TypeDescriptor<MaterialProvidersClient> _TYPE = dafny.TypeDescriptor.<MaterialProvidersClient>referenceWithInitializer(MaterialProvidersClient.class, () -> (MaterialProvidersClient) null);
  public static dafny.TypeDescriptor<MaterialProvidersClient> _typeDescriptor() {
    return (dafny.TypeDescriptor<MaterialProvidersClient>) (dafny.TypeDescriptor<?>) _TYPE;
  }
  @Override
  public java.lang.String toString() {
    return "MaterialProviders.MaterialProvidersClient";
  }
}
