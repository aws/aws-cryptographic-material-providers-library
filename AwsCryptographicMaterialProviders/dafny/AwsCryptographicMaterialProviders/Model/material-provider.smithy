namespace aws.cryptography.materialProviders

use aws.cryptography.keyStore#KeyStore
use aws.cryptography.primitives#AwsCryptographicPrimitives
use com.amazonaws.dynamodb#DynamoDB_20120810
use com.amazonaws.kms#TrentService

@range(min: 0)
integer PositiveInteger

@range(min: 0)
long PositiveLong

// AwsCryptographicMaterialProviders Creation
@aws.polymorph#localService(
  sdkId: "MaterialProviders",
  config: MaterialProvidersConfig,
  dependencies: [
    AwsCryptographicPrimitives,
    DynamoDB_20120810,
    TrentService,
    KeyStore
  ]
)
service AwsCryptographicMaterialProviders {
  version: "2021-11-01",
  resources: [
    Keyring,
    CryptographicMaterialsManager,
    ClientSupplier,
  ],
  operations: [
    // Keyrings
    CreateAwsKmsKeyring,
    CreateAwsKmsDiscoveryKeyring,
    CreateAwsKmsMultiKeyring,
    CreateAwsKmsDiscoveryMultiKeyring,
    CreateAwsKmsMrkKeyring,
    CreateAwsKmsMrkMultiKeyring,
    CreateAwsKmsMrkDiscoveryKeyring,
    CreateAwsKmsMrkDiscoveryMultiKeyring,
    CreateAwsKmsHierarchicalKeyring,
    CreateAwsKmsRsaKeyring,
    CreateAwsKmsEcdhKeyring,
    CreateMultiKeyring,
    CreateRawAesKeyring,
    CreateRawRsaKeyring,
    CreateRawEcdhKeyring,

    // CMMs
    CreateDefaultCryptographicMaterialsManager,
    CreateRequiredEncryptionContextCMM,

    // CMCs
    CreateCryptographicMaterialsCache,

    // ClientSupplier
    CreateDefaultClientSupplier,

    // Materials
    InitializeEncryptionMaterials,
    InitializeDecryptionMaterials,
    ValidEncryptionMaterialsTransition,
    ValidDecryptionMaterialsTransition,
    EncryptionMaterialsHasPlaintextDataKey,
    DecryptionMaterialsWithPlaintextDataKey,

    // AlgorithmSuiteInfo
    GetAlgorithmSuiteInfo,
    ValidAlgorithmSuiteInfo,

    // Commitment
    ValidateCommitmentPolicyOnEncrypt,
    ValidateCommitmentPolicyOnDecrypt,

    // Cache Utilities
    GetCacheIdentifier,
  ],
  errors: [AwsCryptographicMaterialProvidersException],
}

structure MaterialProvidersConfig {}

// Cache Utilities

@documentation("Computes the cache entry identifier used internally by the Hierarchical Keyring. Requires the keyring to be a Hierarchical Keyring.")
operation GetCacheIdentifier {
  input: GetCacheIdentifierInput,
  output: GetCacheIdentifierOutput
}

@documentation("Inputs for computing a cache identifier.")
structure GetCacheIdentifierInput {
  @required
  @documentation("The Hierarchical Keyring whose internal state is used to compute the cache identifier.")
  keyring: KeyringReference,

  @required
  @documentation("The branch key identifier.")
  branchKeyId: String,

  @documentation("The branch key version. If provided, computes the decrypt-path cache identifier. If omitted, computes the encrypt-path cache identifier.")
  branchKeyVersion: String,
}

@documentation("Outputs for computing a cache identifier.")
structure GetCacheIdentifierOutput {
  @required
  @documentation("The computed cache entry identifier.")
  identifier: Blob,
}

// Errors

@error("client")
structure AwsCryptographicMaterialProvidersException {
  @required
  message: String,
}
