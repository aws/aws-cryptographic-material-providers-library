namespace aws.cryptography.materialProviders

use aws.polymorph#reference
use aws.polymorph#positional
use aws.polymorph#extendable
use aws.polymorph#javadoc

//= aws-encryption-sdk-specification/framework/cmm-interface.md#supported-cmms
//= type=implication
//# Note: A user MAY create their own custom CMM.
@extendable
//= aws-encryption-sdk-specification/framework/cmm-interface.md#overview
//= type=implication
//# The CMM interface describes the interface that all CMMs MUST implement.
resource CryptographicMaterialsManager {
  //= aws-encryption-sdk-specification/framework/cmm-interface.md#behaviors
  //= type=implication
  //# The CMM Interface MUST support the following behaviors:
  operations: [GetEncryptionMaterials, DecryptMaterials]
}

// CMM Structures

@reference(resource: CryptographicMaterialsManager)
structure CryptographicMaterialsManagerReference {}

// CMM Operations

operation GetEncryptionMaterials {
  input: GetEncryptionMaterialsInput,
  output: GetEncryptionMaterialsOutput,
}

structure GetEncryptionMaterialsInput {
  //= aws-encryption-sdk-specification/framework/cmm-interface.md#encryption-materials-request
  //= type=implication
  //# The encryption materials request MUST include the following:
  //#   
  //# - [Encryption Context](structures.md#encryption-context)
  //#   - The encryption context provided MAY be empty.
  //# - [Commitment Policy](./commitment-policy.md#supported-commitment-policy-enum)

  @required
  encryptionContext: EncryptionContext,

  @required
  commitmentPolicy: CommitmentPolicy,

  //= aws-encryption-sdk-specification/framework/cmm-interface.md#encryption-materials-request
  //= type=implication
  //# The encryption request MAY include the following:
  //# 
  //# - [Algorithm Suite Id](algorithm-suites.md#algorithm-suite-id)
  //# - Required Encryption Context Keys - a set of strings.
  //# - Max Plaintext Length
  //#   - This value represents the maximum length of the plaintext to be encrypted
  //#     using the returned materials.
  //#     The length of the plaintext to be encrypted MUST not be larger than this value.

  algorithmSuiteId: AlgorithmSuiteId,

  maxPlaintextLength: Long,

  requiredEncryptionContextKeys: EncryptionContextKeys,
}

structure GetEncryptionMaterialsOutput {
  @required
  encryptionMaterials: EncryptionMaterials
}

operation DecryptMaterials {
  input: DecryptMaterialsInput,
  output: DecryptMaterialsOutput,
}

structure DecryptMaterialsInput {
//= aws-encryption-sdk-specification/framework/cmm-interface.md#decrypt-materials-request
//= type=implication
//# The decrypt materials request MUST include the following:
//# 
//# - [Algorithm Suite Id](algorithm-suites.md#algorithm-suite-id)
//# - [Commitment Policy](./commitment-policy.md#supported-commitment-policy-enum)
//# - [Encrypted Data Keys](structures.md#encrypted-data-keys)
//# - [Encryption Context](structures.md#encryption-context)
//#   - The encryption context provided MAY be empty.

  @required
  algorithmSuiteId: AlgorithmSuiteId,

  @required
  commitmentPolicy: CommitmentPolicy,

  @required
  encryptedDataKeys: EncryptedDataKeyList,

  @required
  encryptionContext: EncryptionContext,

  //= aws-encryption-sdk-specification/framework/cmm-interface.md#decrypt-materials-request
  //= type=implication
  //# The decrypt materials request MAY include the following:
  //# 
  //# - [Reproduced Encryption Context](structures.md#encryption-context)

  reproducedEncryptionContext: EncryptionContext,
}

structure DecryptMaterialsOutput {
  @required
  decryptionMaterials: DecryptionMaterials 
}

// CMM Constructors

@positional
@javadoc("Outputs for creating a Default Cryptographic Materials Manager.")
structure CreateCryptographicMaterialsManagerOutput {
  @required
  @javadoc("The created Default Cryptographic Materials Manager.")
  materialsManager: CryptographicMaterialsManagerReference 
}

@javadoc("Creates a Default Cryptographic Materials Manager.")
operation CreateDefaultCryptographicMaterialsManager {
  input: CreateDefaultCryptographicMaterialsManagerInput,
  output: CreateCryptographicMaterialsManagerOutput,
}

@javadoc("Inputs for creating a Default Cryptographic Materials Manager.")
structure CreateDefaultCryptographicMaterialsManagerInput {
  @required
  @javadoc("The Keyring that the created Default Cryptographic Materials Manager will use to wrap data keys.")
  keyring: KeyringReference 
}

@positional
@javadoc("Outputs for creating an Required Encryption Context Cryptographic Materials Manager.")
structure CreateRequiredEncryptionContextCMMOutput {
  @required
  @javadoc("The created Required Encryption Context Cryptographic Materials Manager.")
  materialsManager: CryptographicMaterialsManagerReference
}

@javadoc("Creates an Required Encryption Context Cryptographic Materials Manager.")
operation CreateRequiredEncryptionContextCMM {
  input: CreateRequiredEncryptionContextCMMInput,
  output: CreateRequiredEncryptionContextCMMOutput,
}

@javadoc("Inputs for creating an Required Encryption Context Cryptographic Materials Manager.")
structure CreateRequiredEncryptionContextCMMInput {
  @javadoc("The Cryptographic Materials Manager that the created Required Encryption Context Cryptographic Materials Manager will delegate to. Either a Keyring or underlying Cryptographic Materials Manager must be specified.")
  underlyingCMM: CryptographicMaterialsManagerReference,
  @javadoc("The Keyring that the created Cryptographic Materials Manager will use to wrap data keys. The created Required Encryption Context CMM will delegate to a Default Cryptographic Materials Manager created with this Keyring. Either a Keyring or an underlying Cryptographic Materials Manager must be specified as input.")
  keyring: KeyringReference,
  @required
  @javadoc("A list of Encryption Context keys which are required to be supplied during encryption and decryption, and correspond to Encryption Context key-value pairs which are not stored on the resulting message.")
  requiredEncryptionContextKeys: EncryptionContextKeys
}

@positional
@javadoc("Outputs for creating a Caching Cryptographic Materials Manager.")
structure CreateCachingCMMOutput {
  @required
  @javadoc("The created Caching Cryptographic Materials Manager.")
  materialsManager: CryptographicMaterialsManagerReference
}

@javadoc("Creates a Caching Cryptographic Materials Manager.")
operation CreateCachingCMM {
  input: CreateCachingCMMInput,
  output: CreateCachingCMMOutput,
}

@javadoc("Inputs for creating a Caching Cryptographic Materials Manager.")
structure CreateCachingCMMInput {

  //= aws-encryption-sdk-specification/framework/caching-cmm.md#initialization
  //= type=implication
  //# On caching CMM initialization,
  //# the caller MUST provide the following values:
  //# - [Underlying Cryptographic Materials Cache (CMC)](#underlying-cryptographic-materials-cache)
  //# - [Cache Limit TTL](#cache-limit-ttl)
  @required
  @javadoc("The Cryptographic Materials Cache the Caching Cryptographic Materials Manager will use to cache requests.")
  underlyingCMC: CryptographicMaterialsCacheReference,
  @required
  @javadoc("Sets the maximum lifetime for entries in the cache, for both encrypt and decrypt operations. When the specified amount of time passes after initial creation of the entry, the entry will be considered unusable, and the next operation will incur a cache miss.")
  cacheLimitTtlSeconds: PositiveInteger,

  //= aws-encryption-sdk-specification/framework/caching-cmm.md#initialization
  //= type=implication
  //# Additionally, the caller MUST provide one of the following values:
  //# - [Underlying Cryptographic Materials Manager (CMM)](#underlying-cryptographic-materials-manager)
  //# - [Keyring](keyring-interface.md)
  @javadoc("The Cryptographic Materials Manager that the created Caching Cryptographic Materials Manager will delegate to. Either a Keyring or underlying Cryptographic Materials Manager must be specified.")
  underlyingCMM: CryptographicMaterialsManagerReference,
  @javadoc("The Keyring that the created Cryptographic Materials Manager will use to wrap data keys. The created Caching CMM will delegate to a Default Cryptographic Materials Manager created with this Keyring. Either a Keyring or an underlying Cryptographic Materials Manager must be specified as input.")
  keyring: KeyringReference,

  //= aws-encryption-sdk-specification/framework/caching-cmm.md#initialization
  //= type=implication
  //# Finally, the caching CMM MUST optionally accept the following values:
  //# - [Partition ID](#partition-id)
  //# - [Limit Bytes](#limit-bytes)
  //# - [Limit Messages](#limit-messages)
  @javadoc("Sets the partition ID for this CMM. By default, two CMMs will never use each other's cache entries. This helps ensure that CMMs with different delegates won't incorrectly use each other's encrypt and decrypt results. However, in certain special circumstances it can be useful to share entries between different CMMs - for example, if the backing CMM is constructed based on some parameters that depend on the operation, you may wish for delegates constructed with the same parameters to share the same partition. To accomplish this, set the same partition ID and backing cache on both CMMs; entries cached from one of these CMMs can then be used by the other. This should only be done with careful consideration and verification that the CMM delegates are equivalent for your application's purposes. By default, the partition ID is set to a random UUID to avoid any collisions.")
  partitionKey: Utf8Bytes,
  @javadoc("Sets the maximum number of plaintext bytes that can be encrypted under the same cached data key. This does not affect decrypt operations. Specifying this limit is optional; by default, the limit is set to 2^63 - 1. If this limit is set to zero, keys can only be cached if they are used for zero-length messages.")
  limitBytes: Long,
  @javadoc("Sets the maximum number of individual messages that can be encrypted under the same cached data key. This does not affect decrypt operations. Specifying this limit is optional; by default, the limit is set to 2^32. This is also the maximum accepted value.")
  limitMessages: Integer,

}
