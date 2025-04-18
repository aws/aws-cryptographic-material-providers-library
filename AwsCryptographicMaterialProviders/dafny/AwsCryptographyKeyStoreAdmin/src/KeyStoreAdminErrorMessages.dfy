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
}
