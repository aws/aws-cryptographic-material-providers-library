// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

module {:options "/functionSyntax:4" } KeyStoreAdminErrorMessages {
  const NO_MUTATE_TO_HV_1: string :=
    "At this time, a Mutation cannot change a Branch Key from HV-2 to HV-1. The request dictated 'TerminalHierarchyVersion := v1' and was therefore rejected. Remove the 'TerminalHierarchyVersion' parameter or set it to at least 'v2'."

  const UNSUPPORTED_KEY_MANAGEMENT_STRATEGY :=
    "Unsupported KeyManagementStrategy."
    + " Only KeyManagementStrategy.AwsKmsReEncrypt and KeyManagementStrategy.AwsKmsDecryptEncrypt"
    + " is allowed when terminal hierarchical version is 1."
    + " Only KeyManagementStrategy.kmsSimple is allowed when terminal hierarchical version is 2."

  const UNSUPPORTED_KEY_MANAGEMENT_STRATEGY_HV_2: string :=
    "Only KeyManagementStrategy.AwsKmsSimple is allowed when mutating to hv-2."

  const UNSUPPORTED_DOWNGRADE_HV: string :=
    "Mutation which Downgrades hierarchical version (example: from v2 to v1) is not supported."

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

  const INVALID_COMMITMENT_UTF8 := "Mutation Commitment read from storage contains invalid UTF-8."
  const INVALID_INDEX_UTF8 := "Mutation Index read from storage contains invalid UTF-8."
  const INVALID_COMMITMENT_UUID := "Mutation Commitment read from storage has an invalid UUID."
}
