// Interface IAwsCryptographicMaterialProvidersClient
// Dafny trait IAwsCryptographicMaterialProvidersClient compiled into Java
package software.amazon.cryptography.materialproviders.internaldafny.types;

@SuppressWarnings({"unchecked", "deprecation"})
public interface IAwsCryptographicMaterialProvidersClient {
  public Wrappers_Compile.Result<IKeyring, Error> CreateAwsKmsKeyring(CreateAwsKmsKeyringInput input);
  public Wrappers_Compile.Result<IKeyring, Error> CreateAwsKmsDiscoveryKeyring(CreateAwsKmsDiscoveryKeyringInput input);
  public Wrappers_Compile.Result<IKeyring, Error> CreateAwsKmsMultiKeyring(CreateAwsKmsMultiKeyringInput input);
  public Wrappers_Compile.Result<IKeyring, Error> CreateAwsKmsDiscoveryMultiKeyring(CreateAwsKmsDiscoveryMultiKeyringInput input);
  public Wrappers_Compile.Result<IKeyring, Error> CreateAwsKmsMrkKeyring(CreateAwsKmsMrkKeyringInput input);
  public Wrappers_Compile.Result<IKeyring, Error> CreateAwsKmsMrkMultiKeyring(CreateAwsKmsMrkMultiKeyringInput input);
  public Wrappers_Compile.Result<IKeyring, Error> CreateAwsKmsMrkDiscoveryKeyring(CreateAwsKmsMrkDiscoveryKeyringInput input);
  public Wrappers_Compile.Result<IKeyring, Error> CreateAwsKmsMrkDiscoveryMultiKeyring(CreateAwsKmsMrkDiscoveryMultiKeyringInput input);
  public Wrappers_Compile.Result<IKeyring, Error> CreateAwsKmsHierarchicalKeyring(CreateAwsKmsHierarchicalKeyringInput input);
  public Wrappers_Compile.Result<IKeyring, Error> CreateAwsKmsRsaKeyring(CreateAwsKmsRsaKeyringInput input);
  public Wrappers_Compile.Result<IKeyring, Error> CreateAwsKmsEcdhKeyring(CreateAwsKmsEcdhKeyringInput input);
  public Wrappers_Compile.Result<IKeyring, Error> CreateMultiKeyring(CreateMultiKeyringInput input);
  public Wrappers_Compile.Result<IKeyring, Error> CreateRawAesKeyring(CreateRawAesKeyringInput input);
  public Wrappers_Compile.Result<IKeyring, Error> CreateRawRsaKeyring(CreateRawRsaKeyringInput input);
  public Wrappers_Compile.Result<IKeyring, Error> CreateRawEcdhKeyring(CreateRawEcdhKeyringInput input);
  public Wrappers_Compile.Result<ICryptographicMaterialsManager, Error> CreateDefaultCryptographicMaterialsManager(CreateDefaultCryptographicMaterialsManagerInput input);
  public Wrappers_Compile.Result<ICryptographicMaterialsManager, Error> CreateRequiredEncryptionContextCMM(CreateRequiredEncryptionContextCMMInput input);
  public Wrappers_Compile.Result<ICryptographicMaterialsCache, Error> CreateCryptographicMaterialsCache(CreateCryptographicMaterialsCacheInput input);
  public Wrappers_Compile.Result<IClientSupplier, Error> CreateDefaultClientSupplier(CreateDefaultClientSupplierInput input);
  public Wrappers_Compile.Result<EncryptionMaterials, Error> InitializeEncryptionMaterials(InitializeEncryptionMaterialsInput input);
  public Wrappers_Compile.Result<DecryptionMaterials, Error> InitializeDecryptionMaterials(InitializeDecryptionMaterialsInput input);
  public Wrappers_Compile.Result<dafny.Tuple0, Error> ValidEncryptionMaterialsTransition(ValidEncryptionMaterialsTransitionInput input);
  public Wrappers_Compile.Result<dafny.Tuple0, Error> ValidDecryptionMaterialsTransition(ValidDecryptionMaterialsTransitionInput input);
  public Wrappers_Compile.Result<dafny.Tuple0, Error> EncryptionMaterialsHasPlaintextDataKey(EncryptionMaterials input);
  public Wrappers_Compile.Result<dafny.Tuple0, Error> DecryptionMaterialsWithPlaintextDataKey(DecryptionMaterials input);
  public Wrappers_Compile.Result<AlgorithmSuiteInfo, Error> GetAlgorithmSuiteInfo(dafny.DafnySequence<? extends java.lang.Byte> input);
  public Wrappers_Compile.Result<dafny.Tuple0, Error> ValidAlgorithmSuiteInfo(AlgorithmSuiteInfo input);
  public Wrappers_Compile.Result<dafny.Tuple0, Error> ValidateCommitmentPolicyOnEncrypt(ValidateCommitmentPolicyOnEncryptInput input);
  public Wrappers_Compile.Result<dafny.Tuple0, Error> ValidateCommitmentPolicyOnDecrypt(ValidateCommitmentPolicyOnDecryptInput input);
}
