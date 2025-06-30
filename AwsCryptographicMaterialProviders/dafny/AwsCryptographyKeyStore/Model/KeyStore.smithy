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

use aws.cryptography.primitives#AwsCryptographicPrimitives
use aws.cryptography.materialProviders#AwsCryptographicMaterialProviders


@dafnyUtf8Bytes
string Utf8Bytes

@reference(service: TrentService)
structure KmsClientReference {}

@reference(service: DynamoDB_20120810)
structure DdbClientReference {}

@reference(service: AwsCryptographicPrimitives)
structure PrimitivesReference {}

@reference(service: AwsCryptographicMaterialProviders)
structure MaterialProvidersReference {}

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
  errors: [
    KeyStoreException
    BranchKeyCiphertextException
  ]
}

@documentation("The identifier for the Branch Key.")
string BranchKeyIdentifier

@documentation("Timestamp in ISO 8601 format in UTC, to microsecond precision, that this Branch Key Item's Material was generated.")
string CreateTime

@documentation("Schema Version of the Branch Key. All items of the same Branch Key Identifier SHOULD have the same hierarchy-version. The hierarchy-version determines how the Branch Key Store protects and validates the branch key with KMS.")
@enum([
  { name: "v1", value: "1" },
  { name: "v2", value: "2" }
])
string HierarchyVersion

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
  //# - [KMS Client](#kms-client)
  
  @javadoc("An identifier for this Key Store.")
  id: String,
  @javadoc("The AWS KMS grant tokens that are used when this Key Store calls to AWS KMS.")
  grantTokens: GrantTokenList,
  @javadoc("The DynamoDB client this Key Store uses to call Amazon DynamoDB. If None is provided and the KMS ARN is, the KMS ARN is used to determine the Region of the default client.")
  ddbClient: DdbClientReference,
  @javadoc("The KMS client this Key Store uses to call AWS KMS.  If None is provided and the KMS ARN is, the KMS ARN is used to determine the Region of the default client.")
  kmsClient: KmsClientReference,
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
  kmsConfiguration: KMSConfiguration
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
@documentation(
  "Create a new Branch Key in the Key Store. Additionally create a Beacon Key that is tied to this Branch Key.
  This creates 3 items: the ACTIVE branch key item, the DECRYPT_ONLY for the ACTIVE branch key item, and the beacon key.
  In DynamoDB, the sort-key for the ACTIVE branch key is 'branch:ACTIVE`; the sort-key for the decrypt_only is 'branch:version:<uuid>'; the sort-key for the beacon key is `beacon:ACTIVE'.
  The active branch key and the decrypt_only items have the same AES-256 key.
  The beacon key AES-256 is unqiue.
  For Hierarchy Version 1, KMS is called 3 times; GenerateDataKeyWithoutPlaintext is called twice, ReEncrypt is called once.
  For Hierarchy Version 2, KMS is called 5 times; GenerateDataKey follwed by Encrypt twice to create the ACTIVE branch key and decrypt_only. Another GenerateDataKey follwed by Encrypt creates the beacon key.
  ")
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

  @documentation("Optional. Defaults to v1.")
  hierarchyVersion: HierarchyVersion
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
@javadoc(
  "Rotates an exsisting Branch Key; this generates a fresh AES-256 key which all future encrypts will use for the Key Derivation Function, until VersionKey is executed again.
   Rotation is accomplished by first authenticating the ACTIVE branch key item according to it's hierarchy-version with KMS.
   Then, again using KMS, new material is generated and encrypted, creating a new ACTIVE and corresponding decrypt_only.
   These two items are then writen to the DynamoDB table via a TransactionWriteItems;
   this only overwrites the ACTIVE item, the corresponding decrypt_only is a new item.
   This leaves all the previous decrypt_only items avabile to service decryption of previous rotations.
   See Branch Key Store Developer Guide's 'Rotate your active branch key': https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/rotate-branch-key.html
   ")
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

//XX= aws-encryption-sdk-specification/framework/structures.md#structure-3
//XX= type=implication
//XX# This structure MUST include all of the following fields:
//XX# 
//XX# - [Branch Key](#branch-key)
//XX# - [Branch Key Id](#branch-key-id)
//XX# - [Branch Key Version](#branch-key-version)
//XX# - [Encryption Context](#encryption-context-3)
//XX# - [KMS ARN](#kms-arn)
//XX# - [Create Time](#create-time)
//XX# - [Hierarchy Version](#hierarchy-version)
structure BranchKeyMaterials {
    @required
    branchKeyIdentifier: String,

    @required
    branchKeyVersion: Utf8Bytes,

    @required
    encryptionContext: EncryptionContext,

    @required
    branchKey: Secret,

    @required
    @documentation("The AWS KMS Key ARN used to protect this Branch Key.")
    kmsArn: com.amazonaws.kms#KeyIdType

    @required
    createTime: CreateTime

    @required
    hierarchyVersion: HierarchyVersion
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

  @required
  @documentation("The AWS KMS Key ARN used to protect this Branch Key.")
  kmsArn: com.amazonaws.kms#KeyIdType

  @required
  createTime: CreateTime

  @required
  hierarchyVersion: HierarchyVersion
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

@error("client")
@documentation("
The cipher-text or branch key materials incorporated into the cipher-text,
such as the encryption context, is corrupted, missing, or otherwise invalid.
For branch keys,
the branch key materials is a combination of:
- the encryption context
- storage identifiers (partition key, sort key, logical name)
- metadata that binds the Branch Key to encrypted data (version)
- create-time
- hierarchy-version

If any of the above are modified without calling KMS,
the branch key's cipher-text becomes invalid.
")
structure BranchKeyCiphertextException {
  @required
  message: String
}
