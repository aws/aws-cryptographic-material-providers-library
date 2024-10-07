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

@localService(
  sdkId: "KeyStoreAdmin",
  config: KeyStoreAdminConfig,
  dependencies: [
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
    // ResumeMutation,
    // DescribeMutation
  ],
  errors: [
    KeyStoreAdminException,
    MutationConflictException,
    MutationInvalidException,
    aws.cryptography.keyStore#VersionRaceException
    MutationLockInvalidException
    UnexpectedStateException
    MutationFromException
    MutationToException
    MutationVerificationException
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
union KMSIdentifier {
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
  kmsMRKeyArn behaves exactly as kmsKeyArn.")
  KmsMRKeyArn: String,
}

// TODO-Mutations-FF :
// For GA of Mutations,  of Mutations, only ReEncrypt is allowd
// structure AwsKmsDecryptEncrypt {
//   @documentation("The KMS Client (and Grant Tokens) used to Decrypt Branch Key Store Items.")
//   decrypt: aws.cryptography.keyStore#AwsKms
//   @documentation(
//     "The KMS Client (and Grant Tokens) used to Encrypt Branch Key Store Items
//      and to Generate new Cryptographic Material.")
//   encrypt: aws.cryptography.keyStore#AwsKms
// }

@documentation(
  "This configures which Key Management Operations will be used
   AND the Key Management Clients (and Grant Tokens) used to invoke those Operations.")
union KeyManagementStrategy {
  @documentation(
  "Key Store Items are authenicated and re-wrapped via KMS ReEncrypt,
  executed with the provided Grant Tokens and KMS Client.
  This is one request to Key Management, as compared to two.
  But only one set of credentials can be used.")
  AwsKmsReEncrypt: aws.cryptography.keyStore#AwsKms
  // TODO-Mutations-FF :
  // For GA of Mutations, only ReEncrypt is allowd
  // @documentation(
  //   "Key Store Items are authenicated and re-wrapped via a Decrypt and then Encrypt request.
  //    This is two separate requests to Key Management, as compared to one. 
  //    But the Decrypt requests will use the Decrypt KMS Client (and Grant Tokens),
  //    while the Encrypt requests will use the Encrypt KMS Client (and Grant Tokens).
  //    This option affords for different credentials to be utilized,
  //    based on the operation.
  //    When Generating new material,
  //    KMS GenerateDataKeyWithoutPlaintext will be executed against
  //    the Encrypt option.")
  // AwsKmsDecryptEncrypt: AwsKmsDecryptEncrypt
}

@documentation(
"Create a new Branch Key in the Key Store.
Additionally create a Beacon Key that is tied to this Branch Key.")
operation CreateKey {
  input: CreateKeyInput,
  output: CreateKeyOutput
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
  KmsArn: KMSIdentifier

  Strategy: KeyManagementStrategy
}

structure CreateKeyOutput {
  @required
  @documentation("A identifier for the created Branch Key.")
  Identifier: String
}


@documentation(
  "Create a new ACTIVE version of an existing Branch Key,
   along with a complementing Version (DECRYT_ONLY) in the Key Store.
   This generates a fresh AES-256 key which all future encrypts will use
   for the Key Derivation Function,
   until VersionKey is executed again.")
operation VersionKey {
  input: VersionKeyInput,
  output: VersionKeyOutput,
  errors: [aws.cryptography.keyStore#VersionRaceException]
}


structure VersionKeyInput {
  @required
  @documentation("The identifier for the Branch Key to be versioned.")
  Identifier: String

  @required
  @documentation("Multi-Region or Single Region AWS KMS Key used to protect the Branch Key, but not aliases!")
  KmsArn: KMSIdentifier

  Strategy: KeyManagementStrategy
}

structure VersionKeyOutput {
}

@documentation("
Starts a Mutation to all Items of a Branch Key ID.
Versions the Branch Key ID, such that the new version only has existed in the final state.
Mutates the Beacon Key.
Establishes the Mutation Lock; Simultaneous conflicting Mutations are prevented by the Mutation Lock.
Mutations MUST be completed via subsequent invocations of the Apply Mutation Operation, first invoked with the Mutation Token returned in InitializeMutationOutput.
Uses 1 read of 3 items and 1 write of 4 items.
By default, Key Management will be called 5 times; 2 x GenerateDataKeyWithoutPlaintext, 3 x ReEncrypt.")
operation InitializeMutation {
  input: InitializeMutationInput
  output: InitializeMutationOutput
  errors: [
    MutationConflictException,
    MutationInvalidException,
    aws.cryptography.keyStore#VersionRaceException,
    MutationVerificationException,
    MutationToException
    MutationFromException
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
}

structure MutationToken {
  @documentation("The identifier for the Branch Key being mutated.")
  @required
  Identifier: String
  
  @documentation("Describes the original state of the Branch Key.")
  @required
  Original: Blob

  @documentation("Describes the terminal (or final) state of the Branch Key.")
  @required
  Terminal: Blob

  @documentation("Indirectly describes which items have already been mutated. Used to determine where to continue applying mutations.")
  ExclusiveStartKey: Blob

  @documentation("UUID of the Mutation Lock. If not provided, a Query will be issued to find the Mutation Lock.")
  UUID: String,

  @documentation("ISO 8601 time when the mutation was initialized.")
  @required
  CreateTime: String
}

structure MutatedBranchKeyItem {
  @required
  @documentation("The item type changed. i.e: branch:version:<uuid> or MUTATION_LOCK:<uuid>")
  ItemType: String

  @required
  @documentation("Brief description of what occurred. i.e: Mutation Applied, New Active Created, Mutation Lock Created, Mutation Lock Removed.")
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
}

// TODO: assert release is v1.8.0
@documentation("
Define the Mutation in terms of the terminal, or end state,
value for a particular Branch Key property.
The original value will be REPLACED with this value.
As of v1.8.0, a Mutation can either:
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
  An empty Encyrption Context is not allowed.")
  TerminalEncryptionContext: aws.cryptography.keyStore#EncryptionContextString // EC non Empty MUST be validated in Dafny
}

@documentation("Applies the Mutation to a page of Branch Key Items. If all Items have been mutated, removes the Mutation Lock.")
operation ApplyMutation {
  input:  ApplyMutationInput
  output: ApplyMutationOutput
  errors: [
    MutationLockInvalidException
    UnexpectedStateException
    MutationVerificationException
    MutationToException
    MutationFromException
  ]
}

structure ApplyMutationInput {
  @required
  MutationToken: MutationToken

  @documentation(
  "For Default DynamoDB Table Storage, the maximum page size is 99.
  At most, Apply Mutation will mutate pageSize Items.
  Note that, at least for Storage:DynamoDBTable,
  an additional \"item\" is consumed by the Mutation Lock verification.
  Thus, if the pageSize is 24, 25 requests will be sent in the Transact Write Request.")
  PageSize: Integer

  @documentation("Optional. Defaults to reEncrypt with a default KMS Client.")
  Strategy: KeyManagementStrategy
}

union ApplyMutationResult {
  @documentation("Continue applying the mutation. Invoke Apply Mutation with this Mutation Token.")
  ContinueMutation: MutationToken
  @documentation("All items have been mutated; the Mutation Lock has been removed. The mutation is complete.")
  CompleteMutation: MutationComplete
}

structure MutationComplete {}

structure ApplyMutationOutput {
  @required
  MutationResult: ApplyMutationResult
  @required
  MutatedBranchKeyItems: MutatedBranchKeyItems
}

// @documentation(
//   "If the inputs align with a Mutation that is marked as already in-flight,
//   this operation returns a Mutation Token that can be used to continue the in-flight
//   Mutation.
//   If no in-flight Mutation is detected, nothing is returned.
//   If the inputs do not align, a MutationConflictException is thrown.")
// operation ResumeMutation {
//   input:  ResumeMutationInput
//   output: ResumeMutationOutput
//   errors: [MutationLockDisagreesException, KeyStoreAdminException]
// }

// @error("client")
// @documentation("Mutation Lock does not agree with the provided Branch Key Properities.")
// structure MutationLockDisagreesException {
//   @required
//   message: String,
// }
// // TODO: verify version before release
// @documentation("
// Define the Mutatable Properities of a Branch Key.
// As of v1.8.0, the Mutable Properities are:
// - The KmsArn protecting the Branch Key
// - The custom encryption context of a Branch Key")
// structure MutableBranchKeyProperities {
//   @required
//   @documentation("The KmsArn protecting the Branch Key.")
//   KmsArn: String // KMS Arn validation MUST occur in Dafny
//   @required  
//   @documentation("The custom Encryption Context authenicated with this Branch Key.")
//   CustomEncryptionContext: aws.cryptography.keyStore#EncryptionContextString // EC non Empty MUST be validated in Dafny
// }


// structure ResumeMutationInput {
//   @documentation("The identifier for the Branch Key.")
//   @required
//   Identifier: String

//   @documentation(
//   "Describes the original mutable branch key properities.
//   All members of the input MUST be supplied,
//   or the operation will return an exception.")
//   @required
//   Original: MutableBranchKeyProperities

//   @documentation(
//   "Describes the terminal mutable branch key properities.
//   All members of the input MUST be supplied,
//   or the operation will return an exception.")
//   @required
//   Terminal: MutableBranchKeyProperities

//   @documentation("Optional. Defaults to reEncrypt with a default KMS Client.")
//   Strategy: KeyManagementStrategy
// }

// structure ResumeMutationOutput {
//   @documentation("
//   If present,
//   pass the Mutation Token to the Apply Mutation
//   operation to continue the Mutation.
//   Otherwise, there is no indication of an in-flight Mutation.")
//   mutationToken: MutationToken
// }
// @documentation(
//   "Check for Mutation Lock on a Branch Key ID.
//   If one exists, returns a Mutation Token.
//   Otherwise, returns nothing.")
// operation DescribeMutation {
//   input:  DescribeMutationInput
//   output: DescribeMutationOutput
// }

// structure DescribeMutationInput {
//   @documentation("The identifier for the Branch Key.")
//   @required
//   Identifier: String
// }

// structure DescribeMutationOutput {
//   @documentation("
//   If present,
//   pass the Mutation Token to the Apply Mutation
//   operation to continue the Mutation.
//   Otherwise, there is no Mutation Lock.")
//   MutationToken: MutationToken
// }

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
@documentation(
"Branch Key Authorization failed while Initializing the Mutation.
No Mutation Lock was created; no items were changed.")
structure MutationInvalidException {
  @required
  message: String,
}

// TODO-Mutations-GA : Document recovery
@error("client")
@documentation(
"Mutation Lock disagrees with provided Mutation Token.
Mutation Lock still exists but Mutation cannot proceed.
No items were changed.
Recommend identifying latest author of Mutation Lock
and validating their access;
or checking the integrity of Mutation Token.")
structure MutationLockInvalidException {
  @required
  message: String,
}

// TODO-Mutations-GA : Document recovery
@error("client")
@documentation(
"An Item was encountered that is not
in an expected state.
Mutation Lock is still present;
no items were changed by this request.
Recommend audting backing table access;
an Item of a Branch Key MUST be in
either the original or terminal states during a Mutation;
encountered item(s) in other states.")
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
