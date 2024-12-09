// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

module {:options "/functionSyntax:4" } MutationsConstants {
  module ErrorMessages {
    const COMMITMENT_INDEX_UUID_DISAGREE :=
      "The Mutation Index read from storage and the Mutation Commitment are for different Mutations."
      + " Initialize Mutation cannot proceed, this Branch Key in an invalid state."
      + " Recommend auditing Storage's history for malicious writes."
      + " If confident in the integrity of Storage and the Branch Key,"
      + " delete the Mutation Index to proceed with the in-flight Mutation."
  }
}

        
