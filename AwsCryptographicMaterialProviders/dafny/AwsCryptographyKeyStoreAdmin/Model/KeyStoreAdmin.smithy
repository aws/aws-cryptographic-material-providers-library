// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
namespace aws.cryptography.keyStoreAdmin

// The top level namespace for this project.
// Contains an entry-point for helper methods,
// and common structures used throughout this project.

use aws.polymorph#reference
use aws.polymorph#localService

use com.amazonaws.dynamodb#DynamoDB_20120810
use com.amazonaws.kms#TrentService
use aws.cryptography.primitives#AwsCryptographicPrimitives
use aws.cryptography.keyStore#KeyStore

use aws.cryptography.keyStore#EncryptionContext
use aws.cryptography.keyStore#GrantTokenList

// Even these structures are
// never used in this model directly,
// the Dafny generator in Smithy-Dafny needs these
// to generate the correct Dafny Shim due to a bug.
@reference(service: TrentService)
structure KmsClientReference {}
@reference(service: DynamoDB_20120810)
structure DdbClientReference {}
@reference(service: KeyStore)
structure KeyStoreReference {}
@reference(service: AwsCryptographicPrimitives)
structure PrimitivesReference {}

@localService(
  sdkId: "KeyStoreAdmin",
  config: KeyStoreAdminConfig,
  dependencies: [
    AwsCryptographicPrimitives,
    DynamoDB_20120810,
    TrentService,
    KeyStore
  ] 
)
service KeyStoreAdmin {
  version: "2023-04-01",
  operations: [
    CreateKey,
    VersionKey,
    InitializeMutation,
    ApplyMutation
    DescribeMutation
  ],
  errors: [
    KeyStoreAdminException
    MutationConflictException
    MutationInvalidException
    aws.cryptography.keyStore#KeyStorageException
    aws.cryptography.keyStore#VersionRaceException
    aws.cryptography.keyStore#BranchKeyCiphertextException
    aws.cryptography.keyStore#AlreadyExistsConditionFailed
    aws.cryptography.keyStore#NoLongerExistsConditionFailed
    UnexpectedStateException
    MutationFromException
    MutationToException
    MutationVerificationException
    UnsupportedFeatureException
  ]
}

structure KeyStoreAdminConfig {
  @required
  @documentation(
  "The logical name for this Key Store,
  which is cryptographically bound to the keys it holds.
  This appears in the Encryption Context of KMS requests as `tablename`.

  There SHOULD be a one to one mapping between the Storage's physical name,
  i.e: DynamoDB Table Names,
  and the Logical KeyStore Name.
  This value can be set to the DynamoDB table name itself
  (Storage's physical name),
  but does not need to.

  Controlling this value independently enables restoring from DDB table backups
  even when the table name after restoration is not exactly the same.")
  logicalKeyStoreName: String,

  @required
  @documentation("The storage configuration for this Key Store.")
  storage: aws.cryptography.keyStore#Storage
}

// KMS Arn validation MUST occur in Dafny
union KmsSymmetricKeyArn {
  @documentation(
  "Key Store is restricted to only this KMS Key ARN.
  If a different KMS Key ARN is encountered
  when creating, versioning, or getting a Branch Key or Beacon Key,
  KMS is never called and an exception is thrown.
  While a Multi-Region Key (MKR) may be provided,
  the whole ARN, including the Region,
  is persisted in Branch Keys and
  MUST strictly equal this value to be considered valid.")
  KmsKeyArn: String,

  @documentation(
  "If an MRK ARN is provided,
  and the persisted Branch Key holds an MRK ARN,
  then those two ARNs may differ in region,
  although they must be otherwise equal.
  If either ARN is not an MRK ARN, then
  KmsMRKeyArn behaves exactly as kmsKeyArn.")
  KmsMRKeyArn: String,
}

@documentation(
"Items of a non-cryptographic material nature are protected by KMS.
This is done by including all attributes of an item as Encryption Context
in a KMS Encrypt or Decrypt call,
effectively signing the attributes.
As a best practice,
this KMS Key should be distinct from those used to protect Branch Keys.")
structure KmsSymmetricEncryption {
  @required
  KmsArn: com.amazonaws.kms#KeyIdType
  @required
  AwsKms: aws.cryptography.keyStore#AwsKms
}

@documentation(
"The Storage is trusted enough for items of non-cryptographic material nature,
even if those items can affect the cryptographic materials.
Permissions to modify the data store are sufficient
to influence the contents of mutations in flight
without needing a KMS key permission,
which would otherwise be needed to do the same.")
structure TrustStorage {}

// TODO: verify version before release
@documentation(
"Key Store Admin protects any non-cryptographic
items stored with this Key.
As of v1.9.0, TrustStorage is the default behavior.")
union SystemKey {
  kmsSymmetricEncryption: KmsSymmetricEncryption
  trustStorage: TrustStorage
}

@documentation("
Key Store Items are authenticated and re-wrapped via a Decrypt and then Encrypt request.
This is two separate requests to Key Management, as compared to one.
This is primarily intended for Branch Key Mutations
that need to use separate credentials to change
the KMS Key that protects a Branch Key.

Branch Key Items in the original state
will be Decrypted by the Decrypt KMS Client,
and then Encrypted to the terminal state
via the Encrypt KMS Client.

Generation of a new Branch Key Version
is done via GenerateDataKeyWithoutPlaintext,
and then Decrypt and Encrypt requests against the Encrypt Client.
")
structure AwsKmsDecryptEncrypt {
  @documentation("The KMS Client (and Grant Tokens) used to Decrypt Branch Key Store Items.")
  decrypt: aws.cryptography.keyStore#AwsKms
  @documentation(
    "The KMS Client (and Grant Tokens) used to Encrypt Branch Key Store Items
     and to Generate new Cryptographic Material.")
  encrypt: aws.cryptography.keyStore#AwsKms
}

@documentation(
  "This configures which Key Management Operations will be used
   AND the Key Management Clients (and Grant Tokens) used to invoke those Operations.")
union KeyManagementStrategy {
  @documentation(
  "Key Store Items are authenticated and re-wrapped via KMS ReEncrypt,
  executed with the provided Grant Tokens and KMS Client.
  This is one request to Key Management, as compared to two.
  But only one set of credentials can be used.")
  AwsKmsReEncrypt: aws.cryptography.keyStore#AwsKms,

  AwsKmsDecryptEncrypt: AwsKmsDecryptEncrypt
}



@documentation(
"Create a new Branch Key in the Key Store.
Additionally create a Beacon Key that is tied to this Branch Key.")
operation CreateKey {
  input: CreateKeyInput,
  output: CreateKeyOutput
  errors: [
    UnsupportedFeatureException
    aws.cryptography.keyStore#KeyStorageException
    aws.cryptography.keyStore#AlreadyExistsConditionFailed
    KeyStoreAdminException
  ]
}

structure CreateKeyInput {
  @documentation("The identifier for the created Branch Key.")
  Identifier: String,

  @documentation(
  "Custom encryption context for the Branch Key.
  Required if branchKeyIdentifier is set.")
  EncryptionContext: aws.cryptography.keyStore#EncryptionContext

  @required
  @documentation(
  "Multi-Region or Single Region AWS KMS Key
  used to protect the Branch Key, but not aliases!")
  KmsArn: KmsSymmetricKeyArn

  Strategy: KeyManagementStrategy
}

structure CreateKeyOutput {
  @required
  @documentation("A identifier for the created Branch Key.")
  Identifier: String
}

@documentation(
  "Create a new ACTIVE version of an existing Branch Key,
   along with a complementing Version (DECRYPT_ONLY) in the Key Store.
   This generates a fresh AES-256 key which all future encrypts will use
   for the Key Derivation Function,
   until VersionKey is executed again.")
operation VersionKey {
  input: VersionKeyInput,
  output: VersionKeyOutput,
  errors: [
    UnsupportedFeatureException
    aws.cryptography.keyStore#VersionRaceException
    aws.cryptography.keyStore#KeyStorageException    
    aws.cryptography.keyStore#NoLongerExistsConditionFailed
    aws.cryptography.keyStore#BranchKeyCiphertextException    
    KeyStoreAdminException    
  ]
}

structure VersionKeyInput {
  @required
  @documentation("The identifier for the Branch Key to be versioned.")
  Identifier: String

  @required
  @documentation("Multi-Region or Single Region AWS KMS Key ARN used to protect the Branch Key, but not aliases!")
  KmsArn: KmsSymmetricKeyArn

  Strategy: KeyManagementStrategy
}

structure VersionKeyOutput {
}

@documentation("
Starts a Mutation to all Items of a Branch Key ID.
Versions the Branch Key ID, such that the new version only has existed in the final state.
Mutates the Beacon Key.
Establishes the Mutation Commitment; Simultaneous conflicting Mutations are prevented by the Mutation Commitment.
Mutations MUST be completed via subsequent invocations of the Apply Mutation Operation,
first invoked with the Mutation Token returned in InitializeMutationOutput.")
operation InitializeMutation {
  input: InitializeMutationInput
  output: InitializeMutationOutput
  errors: [
    KeyStoreAdminException
    MutationConflictException
    MutationInvalidException
    aws.cryptography.keyStore#VersionRaceException
    aws.cryptography.keyStore#KeyStorageException
    aws.cryptography.keyStore#BranchKeyCiphertextException
    MutationVerificationException
    MutationToException
    MutationFromException
    UnsupportedFeatureException
  ]
}

structure InitializeMutationInput {
  @documentation("The identifier for the Branch Key to be mutated.")
  @required
  Identifier: String

  @documentation("Describes the Mutation that will be applied to all Items of the Branch Key.")
  @required
  Mutations: Mutations

  @documentation("Optional. Defaults to reEncrypt with a default KMS Client.")
  Strategy: KeyManagementStrategy

  @documentation("Optional. Defaults to TrustStorage. See System Key.")
  SystemKey: SystemKey

  @documentation("Optional. Defaults to False. As of v1.9.0, setting this true throws a UnsupportedFeatureException.")
  DoNotVersion: Boolean
}

structure MutationToken {
  @documentation("The identifier for the Branch Key being mutated.")
  @required
  Identifier: String
  
  @documentation("UUID of the Mutation.")
  @required
  UUID: String,

  @documentation("ISO 8601 time when the mutation was initialized.")
  @required
  CreateTime: String
}

@enum([
  { // "This is a new mutation."
    name: "Created",
    value: "Created"
  },
  { // "A matching mutation already existed."
    name: "Resumed",
    value: "Resumed"
  },
  { // "A matching mutation already existed, but no Page Index was found."
    name: "ResumedWithoutIndex",
    value: "ResumedWithoutIndex"
  }])
string InitializeMutationFlag

structure MutatedBranchKeyItem {
  @required
  @documentation("The item type changed. i.e: branch:version:<uuid> or branch:MUTATION_COMMITMENT.")
  ItemType: String

  @required
  @documentation("Brief description of what occurred. i.e: Mutation Applied, New Active Created, Mutation Commitment Created, Mutation Commitment Removed.")
  Description: String // This could be an enum, which might be an optimization in some runtimes, ignoring Dafny
}

@documentation("Details what items of the Branch Key ID were changed on this invocation.")
list MutatedBranchKeyItems {
  member: MutatedBranchKeyItem
}

structure InitializeMutationOutput {
  @documentation("Pass the Mutation Token to the Apply Mutation operation to continue the Mutation.")
  @required
  MutationToken: MutationToken
  
  @required
  MutatedBranchKeyItems: MutatedBranchKeyItems

  @required
  InitializeMutationFlag: InitializeMutationFlag
}

// TODO: assert release is v1.9.0
@documentation("
Define the Mutation in terms of the terminal, or end state,
value for a particular Branch Key property.
The original value will be REPLACED with this value.
As of v1.9.0, a Mutation can either:
- replace the KmsArn protecting the Branch Key
- replace the custom encryption context
- replace both the KmsArn and the custom encryption context")
structure Mutations {
  @documentation(
  "ReEncrypt all Items of the Branch Key
  to be authorized by this
  AWS Key Management Service Key.
  A Multi-Region or Single Region AWS KMS Key are permitted,
  but not aliases!")
  TerminalKmsArn: String // KMS Arn validation MUST occur in Dafny
  @documentation(
  "ReEncrypt all Items of the Branch Key
  to be authorized with this custom encryption context.
  An empty Encryption Context is not allowed.")
  TerminalEncryptionContext: aws.cryptography.keyStore#EncryptionContextString // EC non Empty MUST be validated in Dafny
}

@documentation("Applies the Mutation to a page of Branch Key Items. If all Items have been mutated, removes the Mutation Commitment and Index.")
operation ApplyMutation {
  input:  ApplyMutationInput
  output: ApplyMutationOutput
  errors: [
    aws.cryptography.keyStore#KeyStorageException
    aws.cryptography.keyStore#BranchKeyCiphertextException    
    MutationInvalidException
    UnexpectedStateException
    MutationVerificationException
    MutationToException
    MutationFromException
    KeyStoreAdminException
  ]
}

structure ApplyMutationInput {
  @required
  MutationToken: MutationToken

  @documentation(
  "For Default DynamoDB Table Storage, the maximum page size is 99.
  At most, Apply Mutation will mutate pageSize Items.
  Note that, at least for Storage:DynamoDBTable,
  two additional \"item\" are consumed by the Mutation Commitment and Mutation Index verification.
  Thus, if the pageSize is 24, 26 requests will be sent in the Transact Write Request.")
  PageSize: Integer

  @documentation("Optional. Defaults to reEncrypt with a default KMS Client.")
  Strategy: KeyManagementStrategy

  @documentation("Optional. Defaults to TrustStorage. See System Key.")
  SystemKey: SystemKey
}

union ApplyMutationResult {
  @documentation("Continue applying the mutation. Invoke Apply Mutation with this Mutation Token.")
  ContinueMutation: MutationToken
  @documentation("All items have been mutated. The mutation is complete.")
  CompleteMutation: MutationComplete
}

structure MutationComplete {}

structure ApplyMutationOutput {
  @required
  MutationResult: ApplyMutationResult
  @required
  MutatedBranchKeyItems: MutatedBranchKeyItems
}

// TODO: verify version before release
@documentation("
Define the Mutable Properties of a Branch Key.
As of v1.9.0, the Mutable Properties are:
- The KmsArn protecting the Branch Key
- The custom encryption context of a Branch Key")
structure MutableBranchKeyProperties {
  @required
  @documentation("The KmsArn protecting the Branch Key.")
  KmsArn: String // KMS Arn validation MUST occur in Dafny
  @required  
  @documentation("The custom Encryption Context authenticated with this Branch Key.")
  CustomEncryptionContext: aws.cryptography.keyStore#EncryptionContextString // EC non Empty MUST be validated in Dafny
}

@documentation(
"Check for an in-flight Mutation on a Branch Key ID.
If one exists, return a description of the mutation.")
operation DescribeMutation {
  input:  DescribeMutationInput
  output: DescribeMutationOutput
  errors: [
    KeyStoreAdminException
    aws.cryptography.keyStore#KeyStorageException
    UnsupportedFeatureException
  ]
}

structure DescribeMutationInput {
  @documentation("The identifier for the Branch Key.")
  @required
  Identifier: String
}

structure MutationDescription {
  @required
  @documentation("Detailed description of the Mutation for this Branch Key.")
  MutationDetails: MutationDetails
  @required
  @documentation("This token can be passed to Apply Mutation to continue the Mutation.")
  MutationToken: MutationToken
}

structure MutationDetails {
  @required
  @documentation("The original properties of the Branch Key.")
  Original: MutableBranchKeyProperties
  @required
  @documentation("The terminal properties of the Branch Key.")
  Terminal: MutableBranchKeyProperties
  @required
  @documentation("The input for this mutation.")
  Input: Mutations
  @required
  @documentation("String description of the System Key.")
  SystemKey: String
  @required
  @documentation("ISO 8601 time when the mutation was initialized.")
  CreateTime: String
  @required
  @documentation("UUID of the Mutation.")
  UUID: String
}

@documentation("If a Mutation is In Flight for this Branch Key.")
union MutationInFlight {
  Yes: MutationDescription
  No: String
}

structure DescribeMutationOutput {
  @required
  MutationInFlight: MutationInFlight
}

// Errors

@error("client")
structure KeyStoreAdminException {
  @required
  message: String
}

// TODO-Mutations-GA : Document recovery
@error("client")
@documentation("A Mutation for this Branch Key ID is already inflight! Nothing was changed. See <link>.")
structure MutationConflictException {
  @required
  message: String,
}

// TODO-Mutations-FF : Document recovery
@error("client")
structure MutationInvalidException {
  @required
  message: String,
}

// TODO-Mutations-GA : Document recovery
@error("client")
structure UnexpectedStateException {
  @required
  message: String,
}

// TODO-Mutations-GA : Document recovery
@error("client")
@documentation(
"Key Management generic error encountered while authenticating
an item already in the terminal state.
Possibly, access to the terminal KMS Key was withdrawn.")
structure MutationVerificationException {
  @required
  message: String,
}

// TODO-Mutations-GA : Document recovery
@error("client")
@documentation(
"Key Management generic error encountered while mutating
an item from original to terminal.
Possibly, access to the terminal KMS Key was withdrawn.")
structure MutationToException {
  @required
  message: String,
}

// TODO-Mutations-GA : Document recovery
@error("client")
@documentation(
"Key Management generic error encountered while mutating
an item from original to terminal.
Possibly, access to the terminal KMS Key was withdrawn.")
structure MutationFromException {
  @required
  message: String,
}

@error("client")
@documentation("This feature is not yet implemented.")
structure UnsupportedFeatureException {
  @required
  message: String,
}