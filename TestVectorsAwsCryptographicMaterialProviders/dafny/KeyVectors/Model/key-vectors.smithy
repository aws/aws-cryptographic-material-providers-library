namespace aws.cryptography.materialProvidersTestVectorKeys

/////////////
// KeyVectors Creation
@aws.polymorph#localService(
  sdkId: "KeyVectors",
  config: KeyVectorsConfig,
)
service KeyVectors {
  version: "20223-04-18",
  resources: [],
  operations: [
    CreateTestVectorKeyring,
    CreateWappedTestVectorKeyring,
    CreateWrappedTestVectorCmm,
    GetKeyDescription,
    SerializeKeyDescription,
  ]
}

structure KeyVectorsConfig {
  @required
  keyManifiestPath: String
}

operation CreateTestVectorKeyring {
  input: TestVectorKeyringInput,
  output: aws.cryptography.materialProviders#CreateKeyringOutput,
}

operation CreateWappedTestVectorKeyring {
  input: TestVectorKeyringInput,
  output: aws.cryptography.materialProviders#CreateKeyringOutput,
}

operation CreateWrappedTestVectorCmm {
  input: TestVectorCmmInput,
  output: CreateWrappedTestVectorCmmOutput,
}

structure TestVectorCmmInput {
  @required
  keyDescription: KeyDescription,
  @required
  forOperation: CmmOperation,
}

@enum([
  {
    name: "ENCRYPT",
    value: "ENCRYPT",
  },
  {
    name: "DECRYPT",
    value: "DECRYPT",
  },
])
string CmmOperation

@aws.polymorph#positional
structure CreateWrappedTestVectorCmmOutput {
  @required
  cmm: aws.cryptography.materialProviders#CryptographicMaterialsManagerReference,
}

@readonly
operation GetKeyDescription {
  input: GetKeyDescriptionInput,
  output: GetKeyDescriptionOutput,
}
@readonly
operation SerializeKeyDescription {
  input: SerializeKeyDescriptionInput,
  output: SerializeKeyDescriptionOutput,
}

structure GetKeyDescriptionInput {
  @required
  json: Blob
}
structure GetKeyDescriptionOutput {
  @required
  keyDescription: KeyDescription
}

structure SerializeKeyDescriptionInput {
  @required
  keyDescription: KeyDescription
}

structure SerializeKeyDescriptionOutput {
  @required
  json: Blob
}

structure TestVectorKeyringInput {
  @required
  keyDescription: KeyDescription,
}

union KeyDescription {
  Kms: KMSInfo,
  KmsMrk: KmsMrkAware,
  KmsMrkDiscovery: KmsMrkAwareDiscovery,
  RSA: RawRSA,
  AES: RawAES,
  Static: StaticKeyring,
  KmsRsa: KmsRsaKeyring,
  Hierarchy: HierarchyKeyring,
  RequiredEncryptionContext: RequiredEncryptionContextCMM,
  Caching: CachingCMM,
}

structure KMSInfo {
  @required
  keyId: String,
}
structure KmsMrkAware {
  @required
  keyId: String,
}
structure KmsMrkAwareDiscovery {
  @required
  keyId: String,
  @required
  defaultMrkRegion: String,
  awsKmsDiscoveryFilter: aws.cryptography.materialProviders#DiscoveryFilter,
}
structure RawRSA {
  @required
  keyId: String,
  @required
  providerId: String,
  @required
  padding: aws.cryptography.materialProviders#PaddingScheme,
}
structure RawAES {
  @required
  keyId: String,
  @required
  providerId: String,
}
structure StaticKeyring {
  @required
  keyId: String,
}

structure KmsRsaKeyring {
  @required
  keyId: String,
  @required
  encryptionAlgorithm: com.amazonaws.kms#EncryptionAlgorithmSpec,
}

structure HierarchyKeyring {
  @required
  keyId: String,
}

structure RequiredEncryptionContextCMM {
  @required
  underlying: KeyDescription,
  @required
  requiredEncryptionContextKeys: aws.cryptography.materialProviders#EncryptionContextKeys
}

structure CachingCMM {
  @required
  underlying: KeyDescription,
  @required
  cacheLimitTtlSeconds: aws.cryptography.materialProviders#PositiveInteger,
  limitBytes: aws.cryptography.materialProviders#PositiveLong,
  limitMessages: aws.cryptography.materialProviders#PositiveInteger,
  @aws.polymorph#javadoc("The entry identifier for get. The cache entry values are set on creation. Use the limits on the CMM to control behavior.")
  getEntryIdentifier: Blob,
  @aws.polymorph#javadoc("The entry identifier for put. The cache entry values are set on creation. Use the limits on the CMM to control behavior.")
  putEntryIdentifier: Blob,
}

@error("client")
structure KeyVectorException {
  @required
  message: String,
}


