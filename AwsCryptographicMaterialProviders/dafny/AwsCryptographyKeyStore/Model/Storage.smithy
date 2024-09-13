// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
namespace aws.cryptography.keyStore


//= aws-encryption-sdk-specification/framework/key-store/encrypted-key-store.md#type
//= type=implication
//# A union that MUST hold the following three options
//#
//#- ActiveHierarchicalSymmetricVersion [HierarchicalSymmetricVersion](#hierarchicalsymmetricversion)
//#- HierarchicalSymmetricVersion [HierarchicalSymmetricVersion](#hierarchicalsymmetricversion)
//#- ActiveHierarchicalSymmetricBeacon
union BranchKeyType {
  ActiveHierarchicalSymmetricVersion: String,
  //= aws-encryption-sdk-specification/framework/key-store/encrypted-key-store.md#hierarchicalsymmetricversion
  //= type=implication
  //# A structure that MUST have one member,
  //# the UTF8 Encoded value of the version of the branch key.
  HierarchicalSymmetricVersion: String,
  ActiveHierarchicalSymmetricBeacon: ActiveHierarchicalSymmetricBeacon
}

structure ActiveHierarchicalSymmetricBeacon {}


//= aws-encryption-sdk-specification/framework/key-store/encrypted-key-store.md#encryptedhierarchicalkey
//= type=implication
//# This structure MUST include all of the following fields:
//#
//#- [BranchKeyId](./structures.md#branch-key-id)
//#- [Type](#type)
//#- CreateTime: Timestamp in ISO 8601 format in UTC, to microsecond precision.
//#- KmsArn: The AWS KMS Key ARN used to protect the CiphertextBlob value.
//#- [EncryptionContext](./structures.md#encryption-context-3)
//#- CiphertextBlob: The encrypted binary for the hierarchical key.
structure EncryptedHierarchicalKey {
  @required
  Identifier: String,

  @required
  Type: BranchKeyType,

  @required
  CreateTime: String,

  @required
  KmsArn: String,

  @required
  EncryptionContext: EncryptionContextString,

  @required
  CiphertextBlob: Blob,
}

structure MutationLock {
  @required
  Identifier: String

  @required
  CreateTime: String

  @required
  UUID: String

  @required
  Original: Blob

  @required
  Terminal: Blob
}

map EncryptionContextString {
  key: String,
  value: String,
}

@aws.polymorph#extendable
resource EncryptedKeyStore {

//= aws-encryption-sdk-specification/framework/key-store/encrypted-key-store.md#interface
//= type=implication
//# The EncryptedKeyStore MUST support the following operations:
//#
//#- [WriteNewKey](#writenewkeytostore)
//#- [WriteNewVersion](#writenewbranchkeyversiontokeystore)
//#- [GetActive](#getencryptedactivebranchkey)
//#- [GetVersion](#getencryptedbranchkeyversion)
//#- [GetBeacon](#getencryptedbeaconkey)
//#- [DescribeEncryptedKeyStore](#gettablename)
  operations: [
    WriteNewKey,
    WriteNewVersion,
    GetActive,
    GetVersion,
    GetBeacon,
    DescribeEncryptedKeyStore,
    GetItemsForInitializeMutation,
    WriteItemsForInitializeMutation,
    QueryForVersions,
    WriteMutatedVersions,
    WriteCompleteMutation
  ]
  errors: [EncryptedKeyStoreException]
}

@aws.polymorph#reference(resource: EncryptedKeyStore)
structure EncryptedKeyStoreReference {}

operation WriteNewKey {
  input: WriteNewKeyInput,
  output: WriteNewKeyOutput,
}
operation WriteNewVersion {
  input: WriteNewVersionInput,
  output: WriteNewVersionOutput,
}
operation GetActive {
  input: GetActiveInput,
  output: GetActiveOutput,
}
operation GetVersion {
  input: GetVersionInput,
  output: GetVersionOutput,
}
operation GetBeacon {
  input: GetBeaconInput,
  output: GetBeaconOutput,
}
operation DescribeEncryptedKeyStore {
  input: DescribeEncryptedKeyStoreInput,
  output: DescribeEncryptedKeyStoreOutput,
  errors: [EncryptedKeyStoreException]
}
operation GetItemsForInitializeMutation {
  input: GetItemsForInitializeMutationInput
  output: GetItemsForInitializeMutationOutput
  errors: [EncryptedKeyStoreException]
}
operation WriteItemsForInitializeMutation {
  input: WriteItemsForInitializeMutationInput
  output: WriteItemsForInitializeMutationOutput
  errors: [EncryptedKeyStoreException]
}
operation QueryForVersions {
  input: QueryForVersionsInput
  output: QueryForVersionsOutput
  errors: [EncryptedKeyStoreException]
}
operation WriteMutatedVersions {
  input: WriteMutatedVersionsInput
  output: WriteMutatedVersionsOutput
  errors: [EncryptedKeyStoreException]
}
operation WriteCompleteMutation {
  input: WriteCompleteMutationInput
  output: WriteCompleteMutationOutput
  errors: [EncryptedKeyStoreException]
}

//= aws-encryption-sdk-specification/framework/key-store/encrypted-key-store.md#writenewkeytostore
//= type=implication
//# The WriteNewKey caller MUST provide:
//#
//#- An [EncryptedHierarchicalKey](#encryptedhierarchicalkey) with a [type](#type) of ActiveHierarchicalSymmetricVersion
//#- An [EncryptedHierarchicalKey](#encryptedhierarchicalkey) with a [type](#type) of HierarchicalSymmetricVersion
//#- An [EncryptedHierarchicalKey](#encryptedhierarchicalkey) with a [type](#type) of ActiveHierarchicalSymmetricBeacon
structure WriteNewKeyInput {
  @required
  Active: EncryptedHierarchicalKey,
  @required
  Version: EncryptedHierarchicalKey,
  @required
  Beacon: EncryptedHierarchicalKey,
}
//= aws-encryption-sdk-specification/framework/key-store/dynamodb-encrypted-key-store.md#writenewkeytostore
//= type=implication
//# If DDB TransactWriteItems is successful, this operation MUST return a successful response containing no additional data.
structure WriteNewKeyOutput {}
//= aws-encryption-sdk-specification/framework/key-store/encrypted-key-store.md#writenewbranchkeyversiontokeystore
//= type=implication
//# The WriteNewVersion caller MUST provide:
//#
//#- An [EncryptedHierarchicalKey](#encryptedhierarchicalkey) with a [type](#type) of ActiveHierarchicalSymmetricVersion
//#- An [EncryptedHierarchicalKey](#encryptedhierarchicalkey) with a [type](#type) of HierarchicalSymmetricVersion
structure WriteNewVersionInput {
  @required
  Active: EncryptedHierarchicalKey,
  @required
  Version: EncryptedHierarchicalKey,
  @required
  oldActive: EncryptedHierarchicalKey
}
structure WriteNewVersionOutput {}
structure GetActiveInput {

  //= aws-encryption-sdk-specification/framework/key-store/encrypted-key-store.md#getencryptedactivebranchkey
  //= type=implication
  //# The GetActive caller MUST provide the same inputs as the [GetActiveBranchKey](../branch-key-store.md#getactivebranchkey) operation.

  @required
  Identifier: String,
}
//= aws-encryption-sdk-specification/framework/key-store/encrypted-key-store.md#getencryptedactivebranchkey
//= type=implication
//# It MUST return an [EncryptedHierarchicalKey](#encryptedhierarchicalkey).
structure GetActiveOutput {
  @required
  Item: EncryptedHierarchicalKey,
}
structure GetVersionInput {

  //= aws-encryption-sdk-specification/framework/key-store/encrypted-key-store.md#getencryptedbranchkeyversion
  //= type=implication
  //# The GetVersion caller MUST provide the same inputs as the [GetBranchKeyVersion](../branch-key-store.md#getbranchkeyversion) operation.

  @required
  Identifier: String,
  @required
  Version: String,
}
//= aws-encryption-sdk-specification/framework/key-store/encrypted-key-store.md#getencryptedbranchkeyversion
//= type=implication
//# It MUST return an [EncryptedHierarchicalKey](#encryptedhierarchicalkey).
structure GetVersionOutput {
  @required
  Item: EncryptedHierarchicalKey,
}
structure GetBeaconInput {

  //= aws-encryption-sdk-specification/framework/key-store/encrypted-key-store.md#getencryptedbeaconkey
  //= type=implication
  //# The GetBeacon caller MUST provide the same inputs as the [GetBeaconKey](../branch-key-store.md#getbeaconkey) operation.

  @required
  Identifier: String,
}
//= aws-encryption-sdk-specification/framework/key-store/encrypted-key-store.md#getencryptedbeaconkey
//= type=implication
//# It MUST return an [EncryptedHierarchicalKey](#encryptedhierarchicalkey).
structure GetBeaconOutput {
  @required
  Item: EncryptedHierarchicalKey,
}
structure DescribeEncryptedKeyStoreInput {}
//= aws-encryption-sdk-specification/framework/key-store/encrypted-key-store.md#gettablename
//= type=implication
//# It MUST return the physical table name.
structure DescribeEncryptedKeyStoreOutput {
  @required
  Name: Utf8Bytes,
}

structure GetItemsForInitializeMutationInput {
  @required
  Identifier: String
}
structure GetItemsForInitializeMutationOutput {
  @required
  activeItem: EncryptedHierarchicalKey
  @required
  beaconItem: EncryptedHierarchicalKey
  mutationLock: MutationLock
}

structure WriteItemsForInitializeMutationInput {
  @required
  active: EncryptedHierarchicalKey,
  @required
  oldActive: EncryptedHierarchicalKey,
  @required
  version: EncryptedHierarchicalKey,
  @required
  beacon: EncryptedHierarchicalKey,
  @required
  mutationLock: MutationLock
}
structure WriteItemsForInitializeMutationOutput {}

list EncryptedHierarchicalKeys {
  member: EncryptedHierarchicalKey
}

structure QueryForVersionsInput {
  exclusiveStartKey: Blob
  @required
  Identifier: String
  @required @range(min: 1)
  pageSize: Integer
}

structure QueryForVersionsOutput {
  @required
  exclusiveStartKey: Blob
  @required
  items: EncryptedHierarchicalKeys
}

structure WriteMutatedVersionsInput {
  @required
  items: EncryptedHierarchicalKeys
  @required
  Identifier: String
  @required
  Original: Blob
  @required
  Terminal: Blob
  @documentation("If set to True, the Mutation Lock will be deleted. Effectively defaults to false")
  CompleteMutation: Boolean
}


structure WriteMutatedVersionsOutput {}

structure WriteCompleteMutationInput {
  @required
  Identifier: String
  @required
  Original: Blob
  @required
  Terminal: Blob
}

structure WriteCompleteMutationOutput {}

@error("client")
structure EncryptedKeyStoreException {
  @required
  message: String,
}
