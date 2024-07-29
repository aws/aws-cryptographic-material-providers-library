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
//#- [WriteNewKeyToStore](#writenewkeytostore)
//#- [WriteNewBranchKeyVersionToKeystore](#writenewbranchkeyversiontokeystore)
//#- [GetEncryptedActiveBranchKey](#getencryptedactivebranchkey)
//#- [GetEncryptedBranchKeyVersion](#getencryptedbranchkeyversion)
//#- [GetEncryptedBeaconKey](#getencryptedbeaconkey)
//#- [GetTableName](#gettablename)
  operations: [
    WriteNewKeyToStore,
    WriteNewBranchKeyVersionToKeystore,
    GetEncryptedActiveBranchKey,
    GetEncryptedBranchKeyVersion,
    GetEncryptedBeaconKey,
    GetTableName,
  ]
}

@aws.polymorph#reference(resource: EncryptedKeyStore)
structure EncryptedKeyStoreReference {}

operation WriteNewKeyToStore {
  input: WriteNewKeyToStoreInput,
  output: WriteNewKeyToStoreOutput,
}
operation WriteNewBranchKeyVersionToKeystore {
  input: WriteNewBranchKeyVersionToKeystoreInput,
  output: WriteNewBranchKeyVersionToKeystoreOutput,
}
operation GetEncryptedActiveBranchKey {
  input: GetEncryptedActiveBranchKeyInput,
  output: GetEncryptedActiveBranchKeyOutput,
}
operation GetEncryptedBranchKeyVersion {
  input: GetEncryptedBranchKeyVersionInput,
  output: GetEncryptedBranchKeyVersionOutput,
}
operation GetEncryptedBeaconKey {
  input: GetEncryptedBeaconKeyInput,
  output: GetEncryptedBeaconKeyOutput,
}
operation GetTableName {
  input: GetTableNameInput,
  output: GetTableNameOutput,
}

//= aws-encryption-sdk-specification/framework/key-store/encrypted-key-store.md#writenewkeytostore
//= type=implication
//# The WriteNewKeyToStore caller MUST provide:
//#
//#- An [EncryptedHierarchicalKey](#encryptedhierarchicalkey) with a [type](#type) of ActiveHierarchicalSymmetricVersion
//#- An [EncryptedHierarchicalKey](#encryptedhierarchicalkey) with a [type](#type) of HierarchicalSymmetricVersion
//#- An [EncryptedHierarchicalKey](#encryptedhierarchicalkey) with a [type](#type) of ActiveHierarchicalSymmetricBeacon
structure WriteNewKeyToStoreInput {
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
structure WriteNewKeyToStoreOutput {}
//= aws-encryption-sdk-specification/framework/key-store/encrypted-key-store.md#writenewbranchkeyversiontokeystore
//= type=implication
//# The WriteNewBranchKeyVersionToKeystore caller MUST provide:
//#
//#- An [EncryptedHierarchicalKey](#encryptedhierarchicalkey) with a [type](#type) of ActiveHierarchicalSymmetricVersion
//#- An [EncryptedHierarchicalKey](#encryptedhierarchicalkey) with a [type](#type) of HierarchicalSymmetricVersion
structure WriteNewBranchKeyVersionToKeystoreInput {
  @required
  Active: EncryptedHierarchicalKey,
  @required
  Version: EncryptedHierarchicalKey,
  @required
  oldActive: EncryptedHierarchicalKey
}
structure WriteNewBranchKeyVersionToKeystoreOutput {}
structure GetEncryptedActiveBranchKeyInput {

  //= aws-encryption-sdk-specification/framework/key-store/encrypted-key-store.md#getencryptedactivebranchkey
  //= type=implication
  //# The GetEncryptedActiveBranchKey caller MUST provide the same inputs as the [GetActiveBranchKey](../branch-key-store.md#getactivebranchkey) operation.

  @required
  Identifier: String,
}
//= aws-encryption-sdk-specification/framework/key-store/encrypted-key-store.md#getencryptedactivebranchkey
//= type=implication
//# It MUST return an [EncryptedHierarchicalKey](#encryptedhierarchicalkey).
structure GetEncryptedActiveBranchKeyOutput {
  @required
  Item: EncryptedHierarchicalKey,
}
structure GetEncryptedBranchKeyVersionInput {

  //= aws-encryption-sdk-specification/framework/key-store/encrypted-key-store.md#getencryptedbranchkeyversion
  //= type=implication
  //# The GetEncryptedBranchKeyVersion caller MUST provide the same inputs as the [GetBranchKeyVersion](../branch-key-store.md#getbranchkeyversion) operation.

  @required
  Identifier: String,
  @required
  Version: String,
}
//= aws-encryption-sdk-specification/framework/key-store/encrypted-key-store.md#getencryptedbranchkeyversion
//= type=implication
//# It MUST return an [EncryptedHierarchicalKey](#encryptedhierarchicalkey).
structure GetEncryptedBranchKeyVersionOutput {
  @required
  Item: EncryptedHierarchicalKey,
}
structure GetEncryptedBeaconKeyInput {

  //= aws-encryption-sdk-specification/framework/key-store/encrypted-key-store.md#getencryptedbeaconkey
  //= type=implication
  //# The GetEncryptedBeaconKey caller MUST provide the same inputs as the [GetBeaconKey](../branch-key-store.md#getbeaconkey) operation.

  @required
  Identifier: String,
}
//= aws-encryption-sdk-specification/framework/key-store/encrypted-key-store.md#getencryptedbeaconkey
//= type=implication
//# It MUST return an [EncryptedHierarchicalKey](#encryptedhierarchicalkey).
structure GetEncryptedBeaconKeyOutput {
  @required
  Item: EncryptedHierarchicalKey,
}
structure GetTableNameInput {}
//= aws-encryption-sdk-specification/framework/key-store/encrypted-key-store.md#gettablename
//= type=implication
//# It MUST return the physical table name.
structure GetTableNameOutput {
  @required
  Name: Utf8Bytes,
}
