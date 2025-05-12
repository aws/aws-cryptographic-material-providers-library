// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

module {:options "/functionSyntax:4" } KeyStoreAdminErrorMessages {
  const UNSUPPORTED_DOWNGRADE_HV: string :=
    "At this time, a Mutation cannot change a Branch Key from `hiearchy-version-2` to `hiearchy-version-1`. The request attempted to change from `hiearchy-version-2` to `hiearchy-version-1` by setting 'TerminalHierarchyVersion := v1' when the Branch Key is already at `hiearchy-version-2`."

  const UNSUPPORTED_KEY_MANAGEMENT_STRATEGY_DECRYPT_ENCRYPT_VERSION :=
    "Unsupported KeyManagementStrategy."
    + " For versioning branch keys,"
    + " KeyManagementStrategy.AwsKmsDecryptEncrypt is not supported"

  const UNSUPPORTED_KEY_MANAGEMENT_STRATEGY_MUTATIONS :=
    "Unsupported KeyManagementStrategy."
    + " KeyManagementStrategy.AwsKmsSimple, KeyManagementStrategy.AwsKmsReEncrypt and KeyManagementStrategy.AwsKmsDecryptEncrypt"
    + " are allowed when terminal hierarchical version is 1."
    + " Only KeyManagementStrategy.AwsKmsDecryptEncrypt and KeyManagementStrategy.AwsKmsSimple is"
    + " allowed when terminal hierarchical version is 2."

  const UNSUPPORTED_KEY_MANAGEMENT_STRATEGY_MUTATIONS_HV_2: string :=
    "Only KeyManagementStrategy.AwsKmsDecryptEncrypt and KeyManagementStrategy.AwsKmsSimple is allowed when mutating to hv-2."

  const INVALID_COMMITMENT_UTF8 := "Mutation Commitment read from storage contains invalid UTF-8."
  const INVALID_INDEX_UTF8 := "Mutation Index read from storage contains invalid UTF-8."
  const INVALID_COMMITMENT_UUID := "Mutation Commitment read from storage has an invalid UUID."

  const NOT_UNIQUE_TERMINAL_EC_AND_EXISTING_ATTRIBUTE :=
    "Initialize Mutation has failed before any writes occurred."
    + " This Branch Key has been modified outside of the library"
    + " to include an attribute pair that is not prefixed with 'aws-crypto-ec'."
    + " This modification, done without using an AWS Crypto Tools library,"
    + " prevents the Branch Key from being used with 'hierarchy-version-2'."
    + " Remove this modification while maintaining the Branch Key's cryptographic integrity,"
    + " and it should be possible to use this Branch Key."

  function TokenAndMutationCommitmentDisagree(
    mutationTokenIdentifier: string,
    mutationCommitmentUUID: string,
    mutationTokenUUID: string
  ): string
  {
    "The Token and the Mutation Commitment read from storage disagree."
    + " This indicates that the Token is for a different Mutation than the one in-flight."
    + " A possible cause is this token is from an earlier Mutation that already finished?"
    + " Branch Key ID: " + mutationTokenIdentifier + ";"
    + " Mutation Commitment UUID: " + mutationCommitmentUUID + ";"
    + " Token UUID: " + mutationTokenUUID + ";"
  }

  function NoMutationInFlight(
    mutationTokenIdentifier: string
  ): string
  {
    "No Mutation is in-flight for this Branch Key ID " + mutationTokenIdentifier + " ."
  }

  function NoMutationIndexExists(
    mutationTokenIdentifier: string
  ): string
  {
    "No Mutation Index exists for this in-flight mutation of Branch Key ID " + mutationTokenIdentifier + " ."
  }

  function IndexAndCommitmentUUIDDisagree(
    nameonly indexUUID: string,
    nameonly commitmentUUID: string
  ): string
  {
    "Mutation Index or Mutation Commitment is corrupted; their UUIDs MUST be equal."
    + " MUTATION_INDEX uuid: " + indexUUID + ";"
    + " MUTATION_COMMITMENT uuid: " + commitmentUUID + ";"
  }

  function IndexAndCommitmentBKIDDisagree(
    nameonly indexBKID: string,
    nameonly commitmentBKID: string
  ): string
  {
    "Mutation Index or Mutation Commitment is corrupted; their Branch Key IDs MUST be equal."
    + " MUTATION_INDEX Branch Key ID: " + indexBKID + ";"
    + " MUTATION_COMMITMENT Branch Key ID: " + commitmentBKID + ";"
  }

  function UnsupportedLocalOperation (
    localOperation: string
  ): string {
    "Internal Error: " + localOperation + " local operation is not supported"
  }
}
