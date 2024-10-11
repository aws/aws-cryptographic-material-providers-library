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

list EncryptedHierarchicalKeys {
  member: EncryptedHierarchicalKey
}


@documentation(
"To avoid information loss, overwrites to a EncryptedHierarchicalKey
are done conditioned on the old value.")
structure OverWriteEncryptedHierarchicalKey {
  @required
  EncryptedHierarchicalKey: EncryptedHierarchicalKey

  @required
  @documentation("The previous itme. Used to construct an optimistic lock for the overwrite.")
  Old: EncryptedHierarchicalKey
}

list OverWriteEncryptedHierarchicalKeys {
  member: OverWriteEncryptedHierarchicalKey
}

@documentation(
"Information on an in-flight Mutation of a Branch Key.
This ensures:
- only one Mutation affects a Branch Key at a time  
- all items of a Branch Key are mutated consistently")
structure MutationLock {
  @required
  @documentation("The Branch Key under Mutation.")
  Identifier: String

  @required
  @documentation("The create time as an ISO 8061 UTC string.")
  CreateTime: String

  @required
  @documentation("A unique identifier for the Mutation.")
  UUID: String

  @required
  @documentation("A commitment of the Original Mutable Properities of the Branch Key.")
  Original: Blob

  @required
  @documentation("A commitment of the Terminal Mutable Properities of the Branch Key.")
  Terminal: Blob

  @required
  Enc: Blob
}

@documentation("Information on an in-flight Mutation of a Branch Key.")
structure MutationIndex {
  @required
  @documentation("The Branch Key under Mutation.")
  Identifier: String

  @required
  @documentation("The create time as an ISO 8061 UTC string.")
  CreateTime: String

  @required
  @documentation("A unique identifier for the Mutation.")
  UUID: String

  @required
  PageIndex: Blob

  @required
  Enc: Blob
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
    GetItemsForInitializeMutation,
    WriteInitializeMutation,
    QueryForVersions,
    WriteMutatedVersions,
    UpdateMutationIndex,
    GetMutationLock,
    GetMutationLockAndIndex,
    DeleteMutationLockAndIndex
  ]
}

@aws.polymorph#reference(resource: KeyStorageInterface)
structure KeyStorageInterfaceReference {}

@documentation("WriteNewEncryptedBranchKey persists the active item, decrypt only (version) item, and Beacon Key Item of a newly created Branch Key.")
operation WriteNewEncryptedBranchKey {
  input: WriteNewEncryptedBranchKeyInput,
  output: WriteNewEncryptedBranchKeyOutput,
  errors: [
    KeyStorageException
    AlreadyExistsConditionFailed
  ] 
}
@documentation("WriteNewEncryptedBranchKeyVersion persists the new active item, decrypt only (version) item of a newly generated Branch Key version.")
operation WriteNewEncryptedBranchKeyVersion {
  input: WriteNewEncryptedBranchKeyVersionInput,
  output: WriteNewEncryptedBranchKeyVersionOutput,
  errors: [
    KeyStorageException
    AlreadyExistsConditionFailed
    OldEncConditionFailed
  ]
}
@documentation("Get the ACTIVE branch key for encryption for an existing branch key.")
operation GetEncryptedActiveBranchKey {
  input: GetEncryptedActiveBranchKeyInput,
  output: GetEncryptedActiveBranchKeyOutput,
  errors: [ KeyStorageException ]
}
@documentation("Get a specific branch key version for an existing branch key.")
operation GetEncryptedBranchKeyVersion {
  input: GetEncryptedBranchKeyVersionInput,
  output: GetEncryptedBranchKeyVersionOutput,
  errors: [ KeyStorageException ]
}
@documentation("Get the beacon key associated with an existing branch key.")
operation GetEncryptedBeaconKey {
  input: GetEncryptedBeaconKeyInput,
  output: GetEncryptedBeaconKeyOutput,
  errors: [ KeyStorageException ]
}
@documentation("Gets information about the underlying storage system.")
operation GetKeyStorageInfo {
  input: GetKeyStorageInfoInput,
  output: GetKeyStorageInfoOutput
  errors: [ KeyStorageException ]
}

@documentation(
"Gets the ACTIVE branch key and the beacon key,
and looks for a Mutation Lock & Index,
returning them if found.")
operation GetItemsForInitializeMutation {
  input: GetItemsForInitializeMutationInput
  output: GetItemsForInitializeMutationOutput
  errors: [KeyStorageException]
}

@documentation(
"Atomically writes,
in the terminal state of a Mutation:  
- new ACTIVE item  
- version (decrypt only) for new ACTIVE  
- beacon key
Also writes the Mutation Lock & Index.")
operation WriteInitializeMutation {
  input: WriteInitializeMutationInput
  output: WriteInitializeMutationOutput
  errors: [
    KeyStorageException,
    MutationLockConditionFailed,
    AlreadyExistsConditionFailed,
    OldEncConditionFailed
  ]
}

@documentation(
"Query Storage for a page of version (decrypt only) items
of a Branch Key.")
operation QueryForVersions {
  input: QueryForVersionsInput
  output: QueryForVersionsOutput
  errors: [KeyStorageException]
}

@documentation(
"Atomically writes,
in the terminal state of a Mutation,
a page of version (decrypt only) items,
conditioned on:
- every version already exsisting
- every version's enc has not changed
- the original of a Mutation Lock commits to the original provided  
- the terminal of a Mutation Lock commits to the terminal provided  
")
operation WriteMutatedVersions {
  input: WriteMutatedVersionsInput
  output: WriteMutatedVersionsOutput
  errors: [
    KeyStorageException
    MutationLockConditionFailed
    OldEncConditionFailed
    NoLongerExistsConditionFailed
  ]
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
  Active: OverWriteEncryptedHierarchicalKey,
  @required
  @documentation("
  The decrypt representation of this branch key version.
  The plain-text cryptographic material of the `Version` must be the same as the `Active`.
  ")
  Version: EncryptedHierarchicalKey
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

structure GetItemsForInitializeMutationInput {
  @documentation("The Branch Key to Mutate.")
  @required
  Identifier: String
}
structure GetItemsForInitializeMutationOutput {
  @required
  @documentation("The materials for the Branch Key.")
  ActiveItem: EncryptedHierarchicalKey
  @documentation("The materials for the Beacon Key.")
  @required
  BeaconItem: EncryptedHierarchicalKey
  @documentation("The Mutation Lock, if it exists.")
  MutationLock: MutationLock
  @documentation("A Mutation Index, if it exists.")
  MutationIndex: MutationIndex
}

structure WriteInitializeMutationInput {
  @required
  @documentation("
  The active representation of this branch key,
  generated with the Mutation's terminal properities.  
  The plain-text cryptographic material of the Active must be the same as the Version.")
  Active: OverWriteEncryptedHierarchicalKey,
  @required
  @documentation("
  The decrypt representation of this branch key version,
  generated with the Mutation's terminal properities.  
  The plain-text cryptographic material of the `Version` must be the same as the `Active`.")
  Version: EncryptedHierarchicalKey,
  @required
  @documentation("
  The mutated HMAC key used to support searchable encryption.
  The cryptographic material is identical to the existing beacon,
  but is now authorized with the Mutation's terminal properities.")
  Beacon: OverWriteEncryptedHierarchicalKey,
  @required // Smithy will copy documentation traits from existing shapes
  MutationLock: MutationLock
  @required
  MutationIndex: MutationIndex
}
structure WriteInitializeMutationOutput {}

structure QueryForVersionsInput {
  @documentation(
  "Optional.
  If set, Query will start at this index and read forward.  
  Otherwise, Query will start at the indexes begining.
  The Default Storage is DDB;
  see Amazon DynamoDB's defination of exclusiveStartKey for details.
  Note: While the Default Storage is DDB,
  the Key Store transforms the exclusiveStartKey into an opaque representation.")
  PageIndex: Blob
  @required
  @documentation("The Identifier of the Branch Key.")
  Identifier: String
  @required // @range(min: 1) Smithy-Dafny may not respect range
  @documentation("The maximum read items.")
  PageSize: Integer
}

structure QueryForVersionsOutput {
  @documentation(
  "If none-empty, Query did not finish searching storage.  
  Next Query should resume from here.
  The Default Storage is DDB;
  see Amazon DynamoDB's defination of exclusiveStartKey for details.
  Note: While the Default Storage is DDB,
  the Key Store transforms the exclusiveStartKey into an opaque representation.")
  @required
  PageIndex: Blob
  @documentation("Up to pageSize list of version (decrypt only) items of a Branch Key.")
  @required
  Items: EncryptedHierarchicalKeys
}

structure WriteMutatedVersionsInput {
  @documentation("List of version (decrypt only) items of a Branch Key to overwrite conditionally.")
  @required
  Items: OverWriteEncryptedHierarchicalKeys
  @required
  MutationLock: MutationLock
}
structure WriteMutatedVersionsOutput {}

@documentation("Updates a Mutation Index.")
operation UpdateMutationIndex {
  input: UpdateMutationIndexInput
  output: UpdateMutationIndexOutput
  errors: [
    KeyStorageException
    OldEncConditionFailed
    NoLongerExistsConditionFailed]
}
structure UpdateMutationIndexInput {
  @required
  MutationIndex: MutationIndex
  @required
  OldMutationIndex: MutationIndex
}
structure UpdateMutationIndexOutput {}

@documentation(
"Check for Mutation Lock on a Branch Key ID.
If one exists, returns the Mutation Lock.
Otherwise, returns nothing.")
operation GetMutationLock {
  input: GetMutationLockInput
  output: GetMutationLockOutput
  errors: [KeyStorageException]
}
structure GetMutationLockInput {
  @documentation("The Branch Key to check for a Mutation Lock.")
  @required
  Identifier: String
}
structure GetMutationLockOutput {
  @documentation("If not present, there is no Mutation Lock.")
  MutationLock: MutationLock
}

@documentation(
"Check for Mutation Lock on a Branch Key ID.
If one exists, returns the Mutation Lock.
Otherwise, returns nothing.")
operation GetMutationLockAndIndex {
  input: GetMutationLockAndIndexInput
  output: GetMutationLockAndIndexOutput
  errors: [KeyStorageException]
}
structure GetMutationLockAndIndexInput {
  @required
  Identifier: String
}
structure GetMutationLockAndIndexOutput {
  MutationLock: MutationLock
  MutationIndex: MutationIndex
}

@documentation("Delete an existing Mutation Lock & Mutation Index.")
operation DeleteMutationLockAndIndex {
  input: DeleteMutationLockAndIndexInput
  output: DeleteMutationLockAndIndexOutput
  errors: [
    KeyStorageException,
    MutationLockConditionFailed
  ]
}
structure DeleteMutationLockAndIndexInput {
  @required
  MutationLock: MutationLock
}
structure DeleteMutationLockAndIndexOutput {}

@error("client")
structure KeyStorageException {
  @required
  message: String,
}

@error("client")
@documentation("Write to Storage failed due to Mutation Lock condition failure.")
structure MutationLockConditionFailed {
  @required
  message: String
}

@error("client")
@documentation("Write to Storage failed. An item already exists for this Branch Key ID & Type.")
structure AlreadyExistsConditionFailed {
  @required
  message: String
}

@error("client")
@documentation("Write to Storage failed. Item was deleted since it was read.")
structure NoLongerExistsConditionFailed {
  @required
  message: String
}

@error("client")
@documentation("Write to Storage failed; cipher-text attribute of an item was updated since it was read.")
structure OldEncConditionFailed {
  @required
  message: String
}
