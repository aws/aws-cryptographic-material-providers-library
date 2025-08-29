// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
namespace aws.cryptography.keyStore

// The top level namespace for this project.
// Contains an entry-point for helper methods,
// and common structures used throughout this project.

use aws.polymorph#localService
use aws.polymorph#reference
use aws.polymorph#extendable
use aws.polymorph#dafnyUtf8Bytes
use aws.polymorph#javadoc

use com.amazonaws.dynamodb#TableName
use com.amazonaws.dynamodb#TableArn
use com.amazonaws.dynamodb#DynamoDB_20120810

use com.amazonaws.kms#TrentService


@dafnyUtf8Bytes
string Utf8Bytes

@reference(service: TrentService)
structure KmsClientReference {}

@reference(service: DynamoDB_20120810)
structure DdbClientReference {}

@localService(
  sdkId: "KeyStore",
  config: KeyStoreConfig,
  dependencies: [
    DynamoDB_20120810,
    TrentService
  ] 
)
service KeyStore {
  version: "2023-04-01",

  //= aws-encryption-sdk-specification/framework/branch-key-store.md#operations
  //= type=implication
  //# The Keystore MUST support the following operations:
  //#
  //#- [GetKeyStoreInfo](#getkeystoreinfo)
  //#- [CreateKeyStore](#createkeystore)
  //#- [CreateKey](#createkey)
  //#- [VersionKey](#versionkey)
  //#- [GetActiveBranchKey](#getactivebranchkey)
  //#- [GetBranchKeyVersion](#getbranchkeyversion)
  //#- [GetBeaconKey](#getbeaconkey)
  operations: [
    GetKeyStoreInfo,
    CreateKeyStore,
    CreateKey,
    VersionKey,
    GetActiveBranchKey,
    GetBranchKeyVersion,
    GetBeaconKey
  ],
  errors: [KeyStoreException]
}

structure KeyStoreConfig {

  //= aws-encryption-sdk-specification/framework/branch-key-store.md#initialization
  //= type=implication
  //# The following inputs MUST be specified to create a KeyStore:
  //# 
  //# - [Table Name](#table-name)
  //# - [AWS KMS Configuration](#aws-kms-configuration)
  //# - [Logical KeyStore Name](#logical-keystore-name)

  @required
  @javadoc("The DynamoDB table name that backs this Key Store.")
  ddbTableName: TableName,
  @required
  @javadoc("Configures Key Store's KMS Key ARN restrictions.")
  kmsConfiguration: KMSConfiguration,
  @required
  @javadoc("The logical name for this Key Store, which is cryptographically bound to the keys it holds. This appears in the Encryption Context of KMS requests as `tablename`.")
  logicalKeyStoreName: String,

  //= aws-encryption-sdk-specification/framework/branch-key-store.md#initialization
  //= type=implication
  //# The following inputs MAY be specified to create a KeyStore:
  //# 
  //# - [ID](#keystore-id)
  //# - [AWS KMS Grant Tokens](#aws-kms-grant-tokens)
  //# - [DynamoDb Client](#dynamodb-client)
  //# - [Require Consistent Reads](#require-consistent-reads)
  //# - [KMS Client](#kms-client)
  
  @javadoc("An identifier for this Key Store.")
  id: String,
  @javadoc("The AWS KMS grant tokens that are used when this Key Store calls to AWS KMS.")
  grantTokens: GrantTokenList,
  @javadoc("The DynamoDB client this Key Store uses to call Amazon DynamoDB. If None is provided and the KMS ARN is, the KMS ARN is used to determine the Region of the default client.")
  ddbClient: DdbClientReference,
  @javadoc("The KMS client this Key Store uses to call AWS KMS.  If None is provided and the KMS ARN is, the KMS ARN is used to determine the Region of the default client.")
  kmsClient: KmsClientReference,

  @javadoc("Whether read operations are required to perform consistent reads. If set to true read operations return results which reflect the most recently executed write operations. Defaults to false.")
  requireConsistentReads: Boolean,
}

//= aws-encryption-sdk-specification/framework/branch-key-store.md#aws-kms-configuration
//= type=implication
//# `KMS Key ARN` and `KMS MRKey ARN` MUST take an additional argument
//# that is a KMS ARN.
@javadoc("Configures Key Store's KMS Key ARN restrictions.")
union KMSConfiguration {
  @javadoc("Key Store is restricted to only this KMS Key ARN. If a different KMS Key ARN is encountered when creating, versioning, or getting a Branch Key or Beacon Key, KMS is never called and an exception is thrown. While a Multi-Region Key (MKR) may be provided, the whole ARN, including the Region, is persisted in Branch Keys and MUST strictly equal this value to be considered valid.")
  // The Key Store (released on 2023-07-24) only allowed for this.
  kmsKeyArn: com.amazonaws.kms#KeyIdType,

  @javadoc("If an MRK ARN is provided, and the Key Store table holds an MRK ARN, then those two ARNs may differ in region, although they must be otherwise equal. If either ARN is not an MRK ARN, then mrkKmsKeyArn behaves exactly as kmsKeyArn.")
  kmsMRKeyArn: com.amazonaws.kms#KeyIdType,


  @javadoc("The Key Store can use the KMS Key ARNs already persisted in the Backing Table. The VersionKey and CreateKey Operations are NOT supported and will fail with a runtime exception. There is no Multi-Region logic with this configuration; if a Multi-Region Key is encountered, and the region in the ARN is not the region of the KMS Client, requests will Fail with KMS Exceptions.")
  // Creates a Discovery Key Store
  discovery: Discovery,

  @javadoc("The Key Store can use the KMS Key ARNs already persisted in the Backing Table. The VersionKey and CreateKey Operations are NOT supported and will fail with a runtime exception. If a Multi-Region Key is encountered, the region in the ARN is changed to the configured region.")
  // Creates an MRDiscovery Key Store
  mrDiscovery: MRDiscovery
}

structure Discovery {}

//= aws-encryption-sdk-specification/framework/branch-key-store.md#aws-kms-configuration
//= type=implication
//# `MRDiscovery` MUST take an additional argument, which is a region.
structure MRDiscovery {
  @required
  @javadoc("Any MRK ARN discovered will have its region replaced with this.")
  region : com.amazonaws.kms#RegionType
}

@javadoc("Returns the configuration information for a Key Store.")
operation GetKeyStoreInfo {
  output: GetKeyStoreInfoOutput
}

@javadoc("The configuration information for a Key Store.")
structure GetKeyStoreInfoOutput {
  @required
  @javadoc("An identifier for this Key Store.")
  keyStoreId: String,
  @required
  @javadoc("The DynamoDB table name that backs this Key Store.")
  keyStoreName: TableName,
  @required
  @javadoc("The logical name for this Key Store, which is cryptographically bound to the keys it holds.")
  logicalKeyStoreName: String,
  @required
  @javadoc("The AWS KMS grant tokens that are used when this Key Store calls to AWS KMS.")
  grantTokens: GrantTokenList,
  @required
  @javadoc("Configures Key Store's KMS Key ARN restrictions.")
  kmsConfiguration: KMSConfiguration,
  @required
  @javadoc("The consistent reads configuration of this keystore instance.")
  requireConsistentReads: Boolean,
}

@javadoc("Create the DynamoDB table that backs this Key Store based on the Key Store configuration. If a table already exists, validate it is configured as expected.")
operation CreateKeyStore {
  input: CreateKeyStoreInput,
  output: CreateKeyStoreOutput
}


structure CreateKeyStoreInput {
}

@javadoc("Outputs for Key Store DynamoDB table creation.")
structure CreateKeyStoreOutput {
  @required
  @javadoc("The ARN of the DynamoDB table that backs this Key Store.")
  tableArn: com.amazonaws.dynamodb#TableArn
}

// CreateKey will create two keys to add to the key store
// One is the branch key, which is used in the hierarchical keyring
// The second is a beacon key that is used as a root key to
// derive different beacon keys per beacon.
@javadoc("Create a new Branch Key in the Key Store. Additionally create a Beacon Key that is tied to this Branch Key.")
operation CreateKey {
  input: CreateKeyInput,
  output: CreateKeyOutput
}

//= aws-encryption-sdk-specification/framework/branch-key-store.md#createkey
//= type=implication
//# The CreateKey caller MUST provide:
//# - An optional branch key id
//# - An optional encryption context
structure CreateKeyInput {
  @javadoc("The identifier for the created Branch Key.")
  branchKeyIdentifier: String,

  @javadoc("Custom encryption context for the Branch Key. Required if branchKeyIdentifier is set.")
  encryptionContext: EncryptionContext
}

@javadoc("Outputs for Branch Key creation.")
structure CreateKeyOutput {
  @required
  @javadoc("A identifier for the created Branch Key.")
  branchKeyIdentifier: String
}

// VersionKey will create a new branch key under the 
// provided branchKeyIdentifier and rotate the "older" material 
// on the key store under the branchKeyIdentifier. This operation MUST NOT
// rotate the beacon key under the branchKeyIdentifier.
@javadoc("Create a new ACTIVE version of an existing Branch Key in the Key Store, and set the previously ACTIVE version to DECRYPT_ONLY.")
operation VersionKey {
  input: VersionKeyInput,
  output: VersionKeyOutput
}

@javadoc("Inputs for versioning a Branch Key.")
structure VersionKeyInput {

  //= aws-encryption-sdk-specification/framework/branch-key-store.md#versionkey
  //= type=implication
  //# - MUST supply a `branch-key-id`
  @required
  @javadoc("The identifier for the Branch Key to be versioned.")
  branchKeyIdentifier: String
}

@javadoc("Outputs for versioning a Branch Key.")
structure VersionKeyOutput {
}

@javadoc("Get the ACTIVE version for a particular Branch Key from the Key Store.")
operation GetActiveBranchKey {
  input: GetActiveBranchKeyInput,
  output: GetActiveBranchKeyOutput
}

@javadoc("Inputs for getting a Branch Key's ACTIVE version.")
structure GetActiveBranchKeyInput {
  @required
  @javadoc("The identifier for the Branch Key to get the ACTIVE version for.")
  branchKeyIdentifier: String
}

@javadoc("Outputs for getting a Branch Key's ACTIVE version.")
structure GetActiveBranchKeyOutput {

  //= aws-encryption-sdk-specification/framework/branch-key-store.md#getactivebranchkey
  //= type=implication
  //# - MUST supply a `branch-key-id`
  @required
  @javadoc("The materials for the Branch Key.")
  branchKeyMaterials: BranchKeyMaterials,
}

@javadoc("Get a particular version of a Branch Key from the Key Store.")
operation GetBranchKeyVersion {
  input: GetBranchKeyVersionInput,
  output: GetBranchKeyVersionOutput
}

@javadoc("Inputs for getting a version of a Branch Key.")
structure GetBranchKeyVersionInput {
  //= aws-encryption-sdk-specification/framework/branch-key-store.md#getbranchkeyversion
  //= type=implication
  //# - MUST supply a `branch-key-id`
  @required
  @javadoc("The identifier for the Branch Key to get a particular version for.")
  branchKeyIdentifier: String,

  //= aws-encryption-sdk-specification/framework/branch-key-store.md#getbranchkeyversion
  //= type=implication
  //# - MUST supply a `branchKeyVersion`
  @required
  @javadoc("The version to get.")
  branchKeyVersion: String
}

@javadoc("Outputs for getting a version of a Branch Key.")
structure GetBranchKeyVersionOutput {
  @required
  @javadoc("The materials for the Branch Key.")
  branchKeyMaterials: BranchKeyMaterials,
}

@javadoc("Get a Beacon Key from the Key Store.")
operation GetBeaconKey {
  input: GetBeaconKeyInput,
  output: GetBeaconKeyOutput
}

@javadoc("Inputs for getting a Beacon Key")
structure GetBeaconKeyInput {
  //= aws-encryption-sdk-specification/framework/branch-key-store.md#getbeaconkey
  //= type=implication
  //# - MUST supply a `branch-key-id`
  @required
  @javadoc("The identifier of the Branch Key the Beacon Key is associated with.")
  branchKeyIdentifier: String
}

@javadoc("Outputs for getting a Beacon Key")
structure GetBeaconKeyOutput {
  @required
  @javadoc("The materials for the Beacon Key.")
  beaconKeyMaterials: BeaconKeyMaterials,
}

list GrantTokenList {
  member: String
}

//= aws-encryption-sdk-specification/framework/structures.md#structure-3
//= type=implication
//# This structure MUST include all of the following fields:
//# 
//# - [Branch Key](#branch-key)
//# - [Branch Key Id](#branch-key-id)
//# - [Branch Key Version](#branch-key-version)
//# - [Encryption Context](#encryption-context-3)
structure BranchKeyMaterials {
    @required
    branchKeyIdentifier: String,

    @required
    branchKeyVersion: Utf8Bytes,

    @required
    encryptionContext: EncryptionContext,

    @required
    branchKey: Secret,
}

structure BeaconKeyMaterials {
  //= aws-encryption-sdk-specification/framework/structures.md#structure-4
  //= type=implication
  //# This structure MUST include the following fields:
  //# - [Beacon Key Id](#beacon-key-id)
  //# - [Encryption Context](#encryption-context-4)
  @required
  beaconKeyIdentifier: String,

  @required
  encryptionContext: EncryptionContext,

  //= aws-encryption-sdk-specification/framework/structures.md#structure-4
  //= type=implication
  //# This structure MAY include the following fields:
  //# - [Beacon Key](#beacon-key)
  //# - [HMAC Keys](#hmac-keys)

  beaconKey: Secret,

  hmacKeys: HmacKeyMap
}

map HmacKeyMap {
  // This key refers to the beacon name for which this value was derived.
  key: String,
  // HKDF derived from the beacon key and the UTF Encoding of the beacon name.
  value: Secret
}

blob Secret

map EncryptionContext {
  key: Utf8Bytes,
  value: Utf8Bytes,
}

// Errors

@error("client")
structure KeyStoreException {
  @required
  message: String,
}
