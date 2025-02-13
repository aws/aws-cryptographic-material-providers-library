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
    ApplyMutation,
    DescribeMutation
  ],
  errors: [
    KeyStoreAdminException,
    MutationConflictException,
    MutationInvalidException,
    aws.cryptography.keyStore#KeyStorageException,
    aws.cryptography.keyStore#VersionRaceException,
    aws.cryptography.keyStore#BranchKeyCiphertextException,
    aws.cryptography.keyStore#AlreadyExistsConditionFailed,
    aws.cryptography.keyStore#NoLongerExistsConditionFailed,
    UnexpectedStateException,
    MutationFromException,
    MutationToException,
    MutationVerificationException,
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
Thus, permissions to modify the Key Store's storage is sufficient
to influence the properties of mutations in flight
without needing a KMS key permission,
which would otherwise be needed to do the same.
As an extreme example,
an actor with only write access to the storage
could modify an in-flight Mutation's terminal KMS Key ARN.
Thus, AWS Crypto Tools recommends using 'KMS Symmetric Encryption'
instead of 'Trust Storage' to ensure that Branch Keys are
only modified via actors with KMS key permissions.")
structure TrustStorage {}

// TODO: verify version before release
@documentation(
"Key Store Admin protects any non-cryptographic
items stored with this Key.
Using 'KMS Symmetric Encryption' is a best practice,
as it prevents actors with only write access to the Key Store's storage
from tampering with Mutations.
For a Mutation, the System Key setting MUST be consistent across the Initialize Mutation and all the Apply Mutation calls.")
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
"Rotates the Branch Key by creating a new ACTIVE version of an existing Branch Key,
along with a complementing Version (DECRYPT_ONLY) in the Key Store.
This generates a fresh AES-256 key which all future encrypts will use
for the Key Derivation Function,
until VersionKey is executed again.
This operation can race against other Version Key requests or Initialize Mutation requests for the same Branch Key.
Should that occur, all but one of the requests will fail.
Race errors are either 'Version Race Exceptions' or 'Key Storage Exceptions'.")
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

@documentation(
"Starts a Mutation to all Items of a Branch Key ID.
Mutates the Beacon Key.
Either Mutates the Active & its version (decrypt only), or versions the Branch Key,
depending on the 'Do Not Version' argument.
Regardless, if operation is successful,
the Beacon, Active, & the Active's version are in the terminal state.
Establishes the Mutation Commitment; simultaneous conflicting Mutations are prevented by the Mutation Commitment.
A Mutation changes the Encryption Context and/or KMS Key associated with a Branch Key.
As such, a Mutation can cause actors to loose access to a Branch Key,
if the actor's access was predicated on particular Encryption Context value or KMS Key.
Mutations MUST be completed via subsequent invocations of the Apply Mutation Operation,
first invoked with the Mutation Token returned in 'Initialize Mutation Output'.
If access to a KMS Key is revoked while a Mutation is in-flight,
the Branch Key will be stuck in a mixed state.
This is not ideal, but once access to the KMS Key is restored,
the Mutation can be continued by calling 'Describe Mutation'
and then calling 'Apply Mutation' as normal.
With respect to the output's Mutation Token, this operation is idempotent;
if invoked with the same request as an in-flight Mutation,
the operation will return successful
with the same Mutation Token as earlier requests.
The 'Initialize Mutation Flag' of the output indicates
if the request was for a novel Mutation or one already in-flight.
'MutationConflictException' is thrown if a different Mutation/change is already in-flight.
This operation can race against other Initialize Mutation requests or Version Key requests for the same Branch Key.
Should that occur, all but one of the requests will fail.
Race errors are either 'VersionRaceException' or 'KeyStorageException'.")
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

  // Smithy's Effective Docuemtnation will utilize System Key's documentation trait
  @required
  SystemKey: SystemKey

  @documentation(
  "Optional. Defaults to False, which Versions (or Rotates) the Branch Key,
  creating a new Version that has only ever been in the terminal state.
  Setting this value to True disables the rotation.
  This is a Security vs Performance trade off.
  Mutating a Branch Key can change the security domain of the Branch Key.
  Some application's Threat Models benefit from ensuring a new Version
  is created whenever a Mutation occurs,
  allowing the application to track under which security domain data
  was protected.
  However, not all Threat Models call for this.
  Particularly if Mutations are triggered in response to external actors,
  creating a new Version for every Mutation request can needlessly grow
  the item count of a Branch Key.")
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

  LastModifiedTime: String
}

// TODO: assert release is v1.9.0
@documentation(
"Define the Mutation in terms of the terminal, or end state,
value for a particular Branch Key property.
The original value will be REPLACED with this value.
As of v1.9.0, a Mutation can either:
- replace the KmsArn protecting the Branch Key
- replace the custom encryption context
- replace both the KmsArn and the custom encryption context")
structure Mutations {
  @documentation(
  "Optional. If not set, there will be no change to the KMS ARN.
  If set, ReEncrypt all Items of the Branch Key
  to be authorized by this
  AWS Key Management Service Key.
  A Multi-Region or Single Region AWS KMS Key are permitted,
  but not aliases!")
  TerminalKmsArn: String // KMS Arn validation MUST occur in Dafny
  @documentation(
  "Optional. If not set, there will be no change to the Encryption Context.
  ReEncrypt all Items of the Branch Key
  to be authorized with this custom encryption context.
  An empty Encryption Context is not allowed.")
  TerminalEncryptionContext: aws.cryptography.keyStore#EncryptionContextString // EC non Empty MUST be validated in Dafny
}

@documentation(
"Applies the Mutation to a page of Branch Key Items.
If all Items have been mutated, removes the Mutation Commitment and Index.
This operation can race other Apply Mutation requests for the same Branch Key.
Should that occur, all but one of the requests will fail with a 'Key Storage Exception'.
Note that the Mutation Token only contains serializable members;
the 'System Key' and 'Strategy' settings are separate parameters.
In particular, the 'System Key' setting MUST be consistent across
the Initialize Mutation and all the Apply Mutation calls of a Mutation.")
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
  "Optional. Defaults to 3 if not set.
  For Default DynamoDB Table Storage, the maximum page size is 98.
  At most, Apply Mutation will mutate pageSize Items.
  Note that, at least for Storage:DynamoDBTable,
  two additional \"item\" are consumed by the Mutation Commitment and Mutation Index verification.
  Thus, if the pageSize is 24, 26 requests will be sent in the Transact Write Request.")
  PageSize: Integer

  @documentation("Optional. Defaults to reEncrypt with a default KMS Client.")
  Strategy: KeyManagementStrategy

  @required
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
  LastModifiedTime: String
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
  @documentation("ISO 8601 timestamp of last time the Mutation was Initialized or Applied.")
  LastModifiedTime: String
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
@documentation("
Exception thrown for various unexpected events or invalid inputs.")
structure KeyStoreAdminException {
  @required
  message: String
}

@error("client")
@documentation("
Exception thrown when a mutation for the configured
Branch Key ID is already in-flight. Nothing was changed.")
structure MutationConflictException {
  @required
  message: String
}

@error("client")
@documentation("
 Exception thrown when there is an error with the input for
 InitializeMutation, ApplyMutation, or DescribeMutation.
 Exception also thrown when validating the encoding of mutation index
 and the mutation commitment attributes.
 If thrown on these operations, an audit of that Branch Key ID 
 and its versions is recommended.
")
structure MutationInvalidException {
  @required
  message: String
}

@error("client")
@documentation("
 Exception thrown if a Branch Key Item is encountered that is not in 
 the original or the terminal state.
 The library cannot perform any operation on this branch key.
 The only way this can be thrown is if the item was modified outside the library.
")
structure UnexpectedStateException {
  @required
  message: String
}

@error("client")
@documentation("
 Thrown when signature generation or signature verification
 with the configured System Key fails.
 This could be caused by KMS denying access to the System Key.
 It could also be caused by the incorrect System Key being used.
 Finally, it could indicate that someone has tampered with
 the Mutation Commitment or Mutation Index persisted to the Key Store's Storage.
")
structure MutationVerificationException {
  @required
  message: String
}

@error("client")
@documentation("
 Thrown when mutating an item from original to terminal,
 specifically when the operation fails when moving to the new key.
 Generally, this indicates access to the terminal KMS Key has been denied.
")
structure MutationToException {
  @required
  message: String
}

@error("client")
@documentation("
 Thrown when mutating an item from original to terminal,
 specifically when the operation fails when moving from the old key.
 Generally, this indicates access to the original KMS Key has been denied.
")
structure MutationFromException {
  @required
  message: String
}

@error("client")
@documentation("This feature is not yet implemented.")
structure UnsupportedFeatureException {
  @required
  message: String
}
