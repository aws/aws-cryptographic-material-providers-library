// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
namespace aws.cryptography.keyStore


//= aws-encryption-sdk-specification/framework/key-store/key-storage.md#type
//= type=implication
//# A union that MUST hold the following three options
//#
//#- ActiveHierarchicalSymmetricVersion [ActiveHierarchicalSymmetric](#activehierarchicalsymmetric)
//#- HierarchicalSymmetricVersion [HierarchicalSymmetric](#hierarchicalsymmetric)
//#- ActiveHierarchicalSymmetricBeacon
@documentation("Describes the key that an encrypted blob represents.")
union HierarchicalKeyType {
  @documentation("The version the active branch key. This version is used to encrypt messages.")
  ActiveHierarchicalSymmetricVersion: ActiveHierarchicalSymmetric,
  @documentation("The version for a decrypt only branch key type. These are used to decrypt messages. For every ACTIVE that has ever been, there exists a Version.")
  HierarchicalSymmetricVersion: HierarchicalSymmetric,
  @documentation("The information regarding a symmetric beacon key.")
  ActiveHierarchicalSymmetricBeacon: ActiveHierarchicalSymmetricBeacon
}

//= aws-encryption-sdk-specification/framework/key-store/key-storage.md#activehierarchicalsymmetric
//= type=implication
//# A structure that MUST have one member,
//# the UTF8 Encoded value of the version of the branch key.
@documentation("Information for the active symmetric branch key.")
structure ActiveHierarchicalSymmetric {
  @required
  @documentation("The version of this active key.")
  Version: String,
}

//= aws-encryption-sdk-specification/framework/key-store/key-storage.md#hierarchicalsymmetric
//= type=implication
//# A structure that MUST have one member,
//# the UTF8 Encoded value of the version of the branch key.
@documentation("Information for a specific decrypt only branch key version.")
structure HierarchicalSymmetric {
  @required
  @documentation("The version of this key.")
  Version: String,
}
@documentation("Information for a symmetric beacon key. At this time there is no additional information.")
structure ActiveHierarchicalSymmetricBeacon {}


//= aws-encryption-sdk-specification/framework/key-store/key-storage.md#encryptedhierarchicalkey
//= type=implication
//# This structure MUST include all of the following fields:
//#
//#- [BranchKeyId](./structures.md#branch-key-id)
//#- [Type](#type)
//#- CreateTime: Timestamp in ISO 8601 format in UTC, to microsecond precision.
//#- KmsArn: The AWS KMS Key ARN used to protect the CiphertextBlob value.
//#- [EncryptionContext](./structures.md#encryption-context-3)
//#- CiphertextBlob: The encrypted binary for the hierarchical key.
@documentation("Information about an encrypted hierarchical key. This abstracts the structure of this information from the underlying storage.")
structure EncryptedHierarchicalKey {
  @required
  @documentation("The identifier for this encrypted key.")
  Identifier: String,

  @required
  @documentation("The type of encrypted key.")
  Type: HierarchicalKeyType,

  @required
  @documentation("The create time as an ISO 8061 UTC string.")
  CreateTime: String,

  @required
  @documentation("The KMS ARN which protects this encrypted key.")
  KmsArn: String,

  @required
  @documentation("The encryption context needed to decrypt this encrypted key. This includes the user the provided custom encryption context, as well as the other Branch Key attributes.")
  EncryptionContext: EncryptionContextString,

  @required
  @documentation("The ciphertext for this encrypted key.")
  CiphertextBlob: Blob,
}

map EncryptionContextString {
  key: String,
  value: String,
}

@aws.polymorph#extendable
resource KeyStorageInterface {

//= aws-encryption-sdk-specification/framework/key-store/key-storage.md#interface
//= type=implication
//# The KeyStorageInterface MUST support the following operations:
//#
//#- [WriteNewEncryptedBranchKey](#writenewencryptedbranchkey)
//#- [WriteNewEncryptedBranchKeyVersion](#writenewencryptedbranchkeyversion)
//#- [GetEncryptedActiveBranchKey](#getencryptedactivebranchkey)
//#- [GetEncryptedBranchKeyVersion](#getencryptedbranchkeyversion)
//#- [GetEncryptedBeaconKey](#getencryptedbeaconkey)
//#- [GetKeyStorageInfo](#getkeystorageinfo)
  operations: [
    WriteNewEncryptedBranchKey,
    WriteNewEncryptedBranchKeyVersion,
    GetEncryptedActiveBranchKey,
    GetEncryptedBranchKeyVersion,
    GetEncryptedBeaconKey,
    GetKeyStorageInfo,
  ]
}

@aws.polymorph#reference(resource: KeyStorageInterface)
structure KeyStorageInterfaceReference {}

@documentation("WriteNewEncryptedBranchKey persists the active item, decrypt only (version) item, and Beacon Key Item of a newly created Branch Key.")
operation WriteNewEncryptedBranchKey {
  input: WriteNewEncryptedBranchKeyInput,
  output: WriteNewEncryptedBranchKeyOutput,
}
@documentation("WriteNewEncryptedBranchKeyVersion persists the new active item, decrypt only (version) item of a newly generated Branch Key version.")
operation WriteNewEncryptedBranchKeyVersion {
  input: WriteNewEncryptedBranchKeyVersionInput,
  output: WriteNewEncryptedBranchKeyVersionOutput,
}
@documentation("Get the ACTIVE branch key for encryption for an existing branch key.")
operation GetEncryptedActiveBranchKey {
  input: GetEncryptedActiveBranchKeyInput,
  output: GetEncryptedActiveBranchKeyOutput,
}
@documentation("Get a specific branch key version for an existing branch key.")
operation GetEncryptedBranchKeyVersion {
  input: GetEncryptedBranchKeyVersionInput,
  output: GetEncryptedBranchKeyVersionOutput,
}
@documentation("Get the beacon key associated with an existing branch key.")
operation GetEncryptedBeaconKey {
  input: GetEncryptedBeaconKeyInput,
  output: GetEncryptedBeaconKeyOutput,
}
@documentation("Gets information about the underlying storage system.")
operation GetKeyStorageInfo {
  input: GetKeyStorageInfoInput,
  output: GetKeyStorageInfoOutput,
}

//= aws-encryption-sdk-specification/framework/key-store/key-storage.md#writenewencryptedbranchkey
//= type=implication
//# The WriteNewEncryptedBranchKey caller MUST provide:
//#
//#- An [EncryptedHierarchicalKey](#encryptedhierarchicalkey) with a [type](#type) of ActiveHierarchicalSymmetricVersion
//#- An [EncryptedHierarchicalKey](#encryptedhierarchicalkey) with a [type](#type) of HierarchicalSymmetricVersion
//#- An [EncryptedHierarchicalKey](#encryptedhierarchicalkey) with a [type](#type) of ActiveHierarchicalSymmetricBeacon
@documentation("
The information required to atomically write an a new branch key into a key store.
The identifiers for all keys passed should be the same.
")
structure WriteNewEncryptedBranchKeyInput {
  @required
  @documentation("
  The active representation of this branch key.
  The plain-text cryptographic material of the Active must be the same as the Version.
  ")
  Active: EncryptedHierarchicalKey,
  @required
  @documentation("
  The decrypt representation of this branch key.
  The plain-text cryptographic material of the Version must be the same as the Active.
  ")
  Version: EncryptedHierarchicalKey,
  @required
  @documentation("
  An HMAC key used to support searchable encryption.
  This should be a different cryptographic material from the other two.
  ")
  Beacon: EncryptedHierarchicalKey,
}
//= aws-encryption-sdk-specification/framework/key-store/dynamodb-key-storage.md#writenewencryptedbranchkey
//= type=implication
//# If DDB TransactWriteItems is successful, this operation MUST return a successful response containing no additional data.
@documentation("The output of writing a new branch key. There is currently no additional information returned.")
structure WriteNewEncryptedBranchKeyOutput {}
//= aws-encryption-sdk-specification/framework/key-store/key-storage.md#writenewencryptedbranchkeyversion
//= type=implication
//# The WriteNewEncryptedBranchKeyVersion caller MUST provide:
//#
//#- An [EncryptedHierarchicalKey](#encryptedhierarchicalkey) with a [type](#type) of ActiveHierarchicalSymmetricVersion
//#- An [EncryptedHierarchicalKey](#encryptedhierarchicalkey) with a [type](#type) of HierarchicalSymmetricVersion
@documentation("
The information required to atomically write a new version for an existing branch key into a key store.
The identifiers for all keys passed should be the same.
")
structure WriteNewEncryptedBranchKeyVersionInput {
  @required
  @documentation("
  The new active version to be written to the key store.
  The plain-text cryptographic material of the Active must be the same as the Version.
  ")
  Active: EncryptedHierarchicalKey,
  @required
  @documentation("
  The decrypt representation of this branch key version.
  The plain-text cryptographic material of the `Version` must be the same as the `Active`.
  ")
  Version: EncryptedHierarchicalKey,
  @required
  @documentation("
  The previous active version.
  This key should be used as an optimistic lock on the new version.
  This means that when updating the current active record
  the existing active record should be equal to this value.
  ")
  oldActive: EncryptedHierarchicalKey
}
@documentation("The output of writing a new version for an existing branch key. There is currently no additional information returned.")
structure WriteNewEncryptedBranchKeyVersionOutput {}

@documentation("Get the ACTIVE version for a particular Branch Key.")
structure GetEncryptedActiveBranchKeyInput {

  //= aws-encryption-sdk-specification/framework/key-store/key-storage.md#getencryptedactivebranchkey
  //= type=implication
  //# The GetEncryptedActiveBranchKey caller MUST provide the same inputs as the [GetActiveBranchKey](../branch-key-store.md#getactivebranchkey) operation.

  @required
  @documentation("The identifier for the Branch Key to get the ACTIVE version for.")
  Identifier: String,
}
//= aws-encryption-sdk-specification/framework/key-store/key-storage.md#getencryptedactivebranchkey
//= type=implication
//# It MUST return an [EncryptedHierarchicalKey](#encryptedhierarchicalkey).
@documentation("Outputs for getting a Branch Key's ACTIVE version.")
structure GetEncryptedActiveBranchKeyOutput {
  @required
  @documentation("The encrypted materials for the ACTIVE Branch Key.")
  Item: EncryptedHierarchicalKey,
}
@documentation("Inputs for getting a version of a Branch Key.")
structure GetEncryptedBranchKeyVersionInput {

  //= aws-encryption-sdk-specification/framework/key-store/key-storage.md#getencryptedbranchkeyversion
  //= type=implication
  //# The GetEncryptedBranchKeyVersion caller MUST provide the same inputs as the [GetBranchKeyVersion](../branch-key-store.md#getbranchkeyversion) operation.

  @required
  @documentation("The identifier for the Branch Key to get a particular version for.")
  Identifier: String,
  @required
  @documentation("The version to get.")
  Version: String,
}
//= aws-encryption-sdk-specification/framework/key-store/key-storage.md#getencryptedbranchkeyversion
//= type=implication
//# It MUST return an [EncryptedHierarchicalKey](#encryptedhierarchicalkey).
@documentation("Outputs for getting a version of a Branch Key.")
structure GetEncryptedBranchKeyVersionOutput {
  @required
  @documentation("The materials for the Branch Key.")
  Item: EncryptedHierarchicalKey,
}
@documentation("Inputs for getting a Beacon Key")
structure GetEncryptedBeaconKeyInput {

  //= aws-encryption-sdk-specification/framework/key-store/key-storage.md#getencryptedbeaconkey
  //= type=implication
  //# The GetEncryptedBeaconKey caller MUST provide the same inputs as the [GetBeaconKey](../branch-key-store.md#getbeaconkey) operation.

  @required
  @documentation("The identifier of the Branch Key the Beacon Key is associated with.")
  Identifier: String,
}
//= aws-encryption-sdk-specification/framework/key-store/key-storage.md#getencryptedbeaconkey
//= type=implication
//# It MUST return an [EncryptedHierarchicalKey](#encryptedhierarchicalkey).
@documentation("Outputs for getting a Beacon Key")
structure GetEncryptedBeaconKeyOutput {
  @required
  @documentation("The materials for the Beacon Key.")
  Item: EncryptedHierarchicalKey,
}

@documentation("Input for getting information about the underlying storage.")
structure GetKeyStorageInfoInput {}
//= aws-encryption-sdk-specification/framework/key-store/key-storage.md#getkeystorageinfo
//= type=implication
//# It MUST return the physical table name.
@documentation("Output containing information about the underlying storage.")
structure GetKeyStorageInfoOutput {
  @required
  @documentation("The name of the physical resource used for storage.")
  Name: Utf8Bytes,

  @required
  @documentation("The Logical Key Store Name associated with this Storage.")
  LogicalName: Utf8Bytes,
}
