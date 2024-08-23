// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
namespace aws.cryptography.keyStoreAdmin

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
use aws.cryptography.keyStore#EncryptionContext

@dafnyUtf8Bytes
string Utf8Bytes

@reference(service: TrentService)
structure KmsClientReference {}

@reference(service: DynamoDB_20120810)
structure DdbClientReference {}

@localService(
  sdkId: "KeyStoreAdmin",
  config: KeyStoreAdminConfig,
  dependencies: [
    DynamoDB_20120810,
    TrentService
  ] 
)
service KeyStoreAdmin {
  version: "2023-04-01",

  operations: [
    CreateKey,
    VersionKey
  ],
  errors: [
    VersionRaceException,
    KeyStoreAdminException
  ]
}

structure KeyStoreAdminConfig {

  @required
  @javadoc("The logical name for this Key Store, which is cryptographically bound to the keys it holds. This appears in the Encryption Context of KMS requests as `tablename`.")
  logicalKeyStoreName: String,

  @javadoc("The storage configuration for this Key Store.")
  storage: aws.cryptography.keyStore#Storage,

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

  @required
  @documentation("Multi-Region or Single Region AWS KMS Key used to protect the Branch Key, but not aliases!")
  kmsArn: String // KMS Arn validation MUST occur in Dafny

  @required
  @documentation("The KMS client this Key Store uses to call AWS KMS.")
  kmsClient: KmsClientReference
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
  output: VersionKeyOutput,
  errors: [ VersionRaceException ]
}

@javadoc("Inputs for versioning a Branch Key.")
structure VersionKeyInput {

  //= aws-encryption-sdk-specification/framework/branch-key-store.md#versionkey
  //= type=implication
  //# - MUST supply a `branch-key-id`
  @required
  @javadoc("The identifier for the Branch Key to be versioned.")
  branchKeyIdentifier: String

  @required
  @documentation("Multi-Region or Single Region AWS KMS Key used to protect the Branch Key, but not aliases!")
  kmsArn: String // KMS Arn validation MUST occur in Dafny

  @required
  @documentation("The KMS client this Key Store uses to call AWS KMS.")
  kmsClient: KmsClientReference
}

@javadoc("Outputs for versioning a Branch Key.")
structure VersionKeyOutput {
}


// Errors

// Can be thrown by VersionKey
@error("client")
@retryable
@documentation("Operation was rejected due to a race with VersionKey. No items were changed. Retry operation when no other agent is Versioning this Branch Key ID.")
structure VersionRaceException {
  @required
  message: String
}

@error("client")
structure KeyStoreAdminException {
  @required
  message: String
}
